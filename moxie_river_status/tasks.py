import urllib2

from lxml import etree

from celery.utils.log import get_task_logger

from moxie import create_app
from moxie.core.tasks import get_resource
from moxie.core.kv import kv_store
from moxie.worker import celery

logger = get_task_logger(__name__)
BLUEPRINT_NAME = 'river_status'


@celery.task
def import_river_status(url=None, force_update=False):
    app = create_app()
    with app.blueprint_context(BLUEPRINT_NAME):
        url = url or app.config['OSM_IMPORT_URL']
        xml = get_resource(url, force_update)
        xml = etree.parse(open(xml), parser=etree.HTMLParser())
        tbody = xml.getroot().find(".//div[@id='sidebar']/table")

        for i, tr in enumerate(tbody.findall('tr')):
            name = tr[0].text.split(':')[0]
            status = tr[1][0].attrib['src'][:-4].split('_')[-1]
            logger.info('River: %s - Status: %s' % (name, status))
