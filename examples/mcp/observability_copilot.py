from fastmcp.server import FastMCP
from fastapi import FastAPI
from typing import List, Optional

# Example data
LOG_SOURCES = ["service-a", "service-b", "service-c"]
ERRORS = {
    "service-a": ["Error 1", "Error 2"],
    "service-b": ["Error 3"],
    "service-c": []
}
METRICS = {
    "service-a": {"cpu": 70, "mem": 512},
    "service-b": {"cpu": 55, "mem": 256},
    "service-c": {"cpu": 80, "mem": 1024}
}
WARNINGS = {
    "service-a": 5,
    "service-b": 2,
    "service-c": 8
}

app = FastAPI(title="Observability Copilot MCP Server")
mcp = FastMCP(app)

# Register functions using the tool decorator with the correct format according to docs
@mcp.tool(
    description="Returns the user ID of the currently logged-in user."
)
def get_current_user_id() -> dict:
    # In a real implementation, fetch from auth/session
    return {"user_id": "user-123"}

@mcp.tool(
    description="Returns log sources accessible to the user."
)
def list_log_sources(user_id: str) -> dict:
    # In a real implementation, filter by user_id
    return {"sources": LOG_SOURCES}

@mcp.tool(
    description="Returns the most recent errors from a log source."
)
def get_recent_errors(source: str, limit: int = 5) -> dict:
    errors = ERRORS.get(source, [])
    return {"errors": errors[:limit]}

@mcp.tool(
    description="Returns metrics for a service in a given time range."
)
def get_metrics(service: str, time_range: str = "last_hour") -> dict:
    metrics = METRICS.get(service, {})
    return {"metrics": metrics}

@mcp.tool(
    description="Returns sources with the most warnings."
)
def top_warning_sources(limit: int = 3) -> dict:
    sorted_sources = sorted(WARNINGS.items(), key=lambda x: x[1], reverse=True)
    top_sources = [s[0] for s in sorted_sources[:limit]]
    return {"sources": top_sources}

if __name__ == "__main__":
    import uvicorn
    # Try a higher port number that's less likely to be in use
    uvicorn.run(app, host="0.0.0.0", port=8000)
