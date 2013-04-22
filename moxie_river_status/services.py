import logging

from datetime import datetime
from lxml import etree

from moxie.core.service import Service
from moxie.core.tasks import get_resource
from moxie.core.kv import kv_store

from .domain import RiverStatus

logger = logging.getLogger(__name__)


class RiverStatusService(Service):

    def __init__(self, url, hmap_key='river-status',
            last_updated_key='river-status-updated'):
        self.url = url
        self.hmap_key = hmap_key
        self.last_updated_key = last_updated_key

    def get_status(self):
        return [RiverStatus(*rs) for rs in kv_store.hgetall(
            self.hmap_key).items()]

    def get_last_updated(self):
        return kv_store.get(self.last_updated_key)

    def set_status(self, status_map):
        last_updated = datetime.now()
        kv_store.set(self.last_updated_key, last_updated)
        return kv_store.hmset(self.hmap_key, status_map)

    def update_status(self, force_update=False):
        xml = get_resource(self.url, force_update)
        if not xml:
            logger.warning('Failed to update river status')
            return False
        xml = etree.parse(open(xml), parser=etree.HTMLParser())
        tbody = xml.getroot().find(".//div[@id='sidebar']/table")

        status_map = {}
        for i, tr in enumerate(tbody.findall('tr')):
            name = tr[0].text.split(':')[0]
            status = tr[1][0].attrib['src'][:-4].split('_')[-1]
            status_map[name] = status
            logger.info('River: %s - Status: %s' % (name, status))
        self.set_status(status_map)
        return True
