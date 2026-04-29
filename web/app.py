from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import os

from agents.asset_agent import discover_assets
from agents.scan_agent import scan_target
from agents.report_agent import generate_report

app = FastAPI()
templates = Jinja2Templates(directory="web/templates")

REPORT_PATH = "reports/output/security_report.md"

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/scan", response_class=HTMLResponse)
def scan(request: Request, target: str = Form(...)):
    assets = discover_assets(target)
    findings = scan_target(assets)
    report = generate_report(target, findings)

    os.makedirs("reports/output", exist_ok=True)
    with open(REPORT_PATH, "w") as f:
        f.write(report)

    return templates.TemplateResponse("index.html", {"request": request, "result": findings, "target": target, "report_ready": True})

@app.get("/download")
def download():
    return FileResponse(REPORT_PATH, filename="security_report.md")
