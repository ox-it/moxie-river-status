import logging
from datetime import timedelta

from flask import request

from moxie.core.views import ServiceView, accepts
from moxie.core.representations import JSON, HAL_JSON

from .representations import HALRiversStatusRepresentation
from .services import RiverStatusService

logger = logging.getLogger(__name__)


class Status(ServiceView):

    expires = timedelta(minutes=10)

    def handle_request(self):
        service = RiverStatusService.from_context()
        last_updated = service.get_last_updated()
        status = service.get_status()
        return status, last_updated

    @accepts(HAL_JSON, JSON)
    def as_hal_json(self, response):
        return HALRiversStatusRepresentation(*response,
                endpoint=request.url_rule.endpoint).as_json()
