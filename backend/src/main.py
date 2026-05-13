from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.core.config import settings
from src.exception_handlers.base_exception import BaseAppException
from src.api.endpoints.user_endpoint import user_router
from src.api.endpoints.category_endpoint import category_route
from src.api.endpoints.place_endpoint import places_route
from src.api.endpoints.comment_endpoint import comment_router


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.debug,
    docs_url="/docs",
)


@app.exception_handler(BaseAppException)
async def app_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.message}
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


app.include_router(user_router)
app.include_router(category_route)
app.include_router(places_route)
app.include_router(comment_router)

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app", host="127.0.0.1", port=8000, reload=True # for docker host is 0.0.0.0 and not relaod include
)