from app.tasks.routes import router as task_router

api_router.include_router(task_router)
