# FastMCP Echo Server & Client

This project demonstrates a complete FastMCP (Model Context Protocol) setup with both a server and client implementation.

## FastMCP Echo Server

The server (`fastmcp_echo_server.py`) provides:

### Tools
- **`echo_tool`**: Takes text input and returns it unchanged

### Resources
- **`echo://static`**: Static resource that returns "Echo!"
- **`echo://{text}`**: Template resource that echoes the input text

### Prompts
- **`echo`**: Takes text input and returns it as a prompt

## MCP Client

The client (`mcp_client.py`) demonstrates how to:

- Initialize connection with MCP server
- List and call tools
- List and read resources
- List and get prompts
- Handle MCP protocol communication

## Running the Demo

### 1. Start the FastMCP Server

```bash
# Install dependencies
pip install fastmcp

# Run the server
python fastmcp_echo_server.py
```

The server will start on `http://localhost:8000` by default.

### 2. Run the MCP Client

In a separate terminal:

```bash
# Run the client (make sure server is running first)
python mcp_client.py
```

## Expected Output

The client will demonstrate:

1. **Server Connection**: Initialize and connect to the MCP server
2. **Tool Discovery**: Find the `echo_tool`
3. **Tool Execution**: Call `echo_tool` with "Hello from MCP Client!"
4. **Resource Discovery**: Find both static and template resources
5. **Resource Reading**: Read `echo://static` and `echo://hello`
6. **Prompt Discovery**: Find the `echo` prompt
7. **Prompt Execution**: Get prompt with "Hello from MCP Client!"

## Sample Output

```
🚀 Starting FastMCP Echo Server Demonstration
📡 Server URL: http://localhost:8000
🔄 Initializing connection with MCP server...
✅ Successfully connected to FastMCP server
   Server: Echo Server
   Version: 1.0.0

🛠️  Discovering tools...
✅ Found 1 tools
   • echo_tool: Echo the input text

🔧 Calling echo_tool...
✅ Tool call successful: Hello from MCP Client!

📁 Discovering resources...
✅ Found 2 resources
   • Static Echo Resource: echo://static
   • Template Echo Resource: echo://{text}

📖 Reading static resource: echo://static
✅ Resource read successful: Echo!

📖 Reading template resource: echo://hello
✅ Resource read successful: Echo: hello

💬 Discovering prompts...
✅ Found 1 prompts
   • echo: Echo prompt

💬 Getting echo prompt...
✅ Prompt get successful: Hello from MCP Client!

✅ Demonstration completed successfully!
```

## MCP Protocol Details

The client uses the Model Context Protocol (MCP) with JSON-RPC 2.0 over HTTP to communicate with the server. It demonstrates:

- **Initialization**: Handshake and capability negotiation
- **Tool Calling**: Remote procedure calls to server tools
- **Resource Access**: Reading server-provided resources
- **Prompt Generation**: Getting structured prompts from the server

## Customization

### Server URL
To connect to a different server URL, modify `BASE_URL` in `mcp_client.py`:

```python
BASE_URL = "http://your-server-url:port"
```

### Server Implementation
The server uses the `fastmcp` library. Make sure it's installed:

```bash
pip install fastmcp
```

## Requirements

- Python 3.8+
- `fastmcp` library
- `requests` library (for the client)

Install all dependencies:

```bash
pip install fastmcp requests
```
