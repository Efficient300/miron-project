from fastapi import APIRouter , Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/first_page",
    tags=["first_page"]
)
templates = Jinja2Templates(directory="app/templates")
@router.get("")
async def get_first_page(request:Request):
    return templates.TemplateResponse("index.html",)