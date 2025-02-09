from fastapi import APIRouter, Response

from app.api.utils.logging import get_logger

router = APIRouter()

logger = get_logger()

def health():
    logger.debug("app is healthy...")

    return Response("ok", status_code=200)


router.add_api_route(
    path="/health",
    endpoint=health,
    methods=["GET"],
    tags=["health"],
)

