# Observability Copilot MCP Example

This example demonstrates how to expose observability functions (logs and metrics) via an MCP server using [fastmcp](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/fastmcp/echo.py).

## Requirements

- Python 3.8+
- Install dependencies:
  ```
  pip install fastapi uvicorn
  ```

## Running the Server

Start the MCP server:

```
python observability_copilot.py
```

The server will be available at `http://localhost:8000`.

## Example Usage

You can interact with the server using HTTP requests or integrate it with an MCP-compatible agent.
