import os
from typing import Any, Dict, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Estación Eq. 04 - UI/CSS",
    version="0.1.0",
    description="Servicio inicial para Hito 1 de la estación UI/CSS (Equipo 04).",
)


class StyleRequest(BaseModel):
    component: Optional[str] = "card"
    theme: Optional[str] = "light"
    options: Optional[Dict[str, Any]] = None


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "online"}


@app.post("/api/v1/ui-css/style")
def generate_style(payload: StyleRequest) -> Dict[str, Any]:
    return {
        "station": "eq04-ui-css",
        "mode": "mock",
        "status": "ok",
        "input_received": payload.model_dump(),
        "css_rules": {
            "theme": payload.theme,
            "component": payload.component,
            "styles": {
                "backgroundColor": "#ffffff" if payload.theme == "light" else "#121212",
                "color": "#111111" if payload.theme == "light" else "#f5f5f5",
                "borderRadius": "8px",
                "padding": "16px",
            },
        },
    }


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
  
