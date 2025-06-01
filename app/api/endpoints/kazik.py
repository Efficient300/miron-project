from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/kazik",
    tags=["Казино"],
)

templates = Jinja2Templates(directory="app/templates")



@router.get("/main", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})





@router.get("", response_class=HTMLResponse)
async def kazik_page(request: Request):
    return templates.TemplateResponse("kazik.html", {"request": request})