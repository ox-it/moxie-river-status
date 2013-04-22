from .services import RiverStatusService

from moxie import create_app
from moxie.worker import celery

BLUEPRINT_NAME = 'river_status'


@celery.task
def import_river_status(force_update=False):
    app = create_app()
    with app.blueprint_context(BLUEPRINT_NAME):
        river_service = RiverStatusService.from_context()
        river_service.update_status(force_update)
