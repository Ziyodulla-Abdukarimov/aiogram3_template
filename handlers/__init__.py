from aiogram import Router


def setup_routers() -> Router:
    from .users import start
    from .errors import error_handler

    router = Router()

    router.include_routers(
        start.router,
        error_handler.router,
    )

    return router
