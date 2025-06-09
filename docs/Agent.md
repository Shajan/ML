# Guidelines for Adding LLM Capabilities to Products

This document provides a step-by-step guide for adding LLM (Large Language Model) capabilities to your product, using an example scenario with a cloud service for logs and metrics and an agent called "Observability Copilot".

---

## 1. Collect User Questions or Tasks

Start by listing questions or tasks a user might expect an AI Agent to solve. For example:

- "Show me the most recent errors."
- "List all log sources I have access to."
- "Get metrics for service X in the last hour."
- "Find the top 5 sources with the most warnings."
- "Who am I logged in as?"

---

## 2. Design Functions to Answer These Questions

For each question, design a function that would answer it. Give each function a meaningful name and describe its purpose and parameters.

### Example Functions

| Function Name           | Description                                               | Parameters                        |
|------------------------|-----------------------------------------------------------|-----------------------------------|
| `get_current_user_id`  | Returns the user ID of the currently logged-in user.      | None                              |
| `list_log_sources`     | Returns log sources accessible to the user.               | `user_id` (string)                |
| `get_recent_errors`    | Returns the most recent errors from a log source.         | `source` (string), `limit` (int)  |
| `get_metrics`          | Returns metrics for a service in a given time range.      | `service` (string), `time_range` (string) |
| `top_warning_sources`  | Returns sources with the most warnings.                   | `limit` (int)                     |

---

## 3. Simplify and Document Functions

Ensure each function is simple, has a clear description, and well-defined parameters. This helps LLMs and agents understand and execute them.

---

## 4. Implement as an MCP Server

Wrap these functions in an MCP (Model Context Protocol) server. You can use [fastmcp](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/fastmcp/echo.py) as a reference.

**Example Python Implementation:**

```python
# See examples/mcp/observability_copilot.py for the full implementation
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/get_current_user_id")
def get_current_user_id():
    """Returns the user ID of the currently logged-in user."""
    return {"user_id": "user-123"}

# ...other endpoints as described above...
```

---

## 5. Register and Test with an Agent

Register your MCP server with any agent that supports MCP (e.g., VS Code's GitHub Copilot Agent). Test the agent using the questions collected in step 1.

---

## 6. If Needed, Create an Agent

If no existing agent is available, create one. (This is covered in a different section.)

---

## Example Scenario: Observability Copilot

Suppose you have a cloud service for storing and querying logs and metrics. The above process enables you to expose relevant APIs to LLMs and agents, making your product more intelligent and user-friendly.

See [`examples/mcp/observability_copilot.py`](../examples/mcp/observability_copilot.py) and the README in `examples/mcp/` for a working example and instructions.
