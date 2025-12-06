#!/usr/bin/env python3
"""
FastMCP Client using the official FastMCP Client library

This client uses the FastMCP Client to properly connect to FastMCP servers
using the correct protocol (SSE, WebSocket, etc.)
"""

import asyncio
from fastmcp import Client


async def demonstrate_fastmcp_server():
    """Demonstrate the FastMCP Echo Server using the official client."""

    print("🚀 Starting FastMCP Client Demonstration")
    print("📡 Connecting to http://localhost:8000")

    try:
        # Create and connect the client
        async with Client("http://localhost:8000/mcp") as client:
            print("✅ Successfully connected to FastMCP server")
            # Note: FastMCP Client may not expose server_info directly

            # List and demonstrate tools
            print("\n🛠️  Discovering tools...")
            tools = await client.list_tools()
            print(f"✅ Found {len(tools)} tools")
            for tool in tools:
                print(f"   • {tool.name}: {tool.description}")

            # Call the echo tool
            if tools:
                print("\n🔧 Calling echo_tool...")
                result = await client.call_tool(tool.name, {"text": "Hello from FastMCP Client!"})
                print(f"✅ Tool call successful: {result}")

            # List and demonstrate resources
            print("\n📁 Discovering resources...")
            resources = await client.list_resources()
            print(f"✅ Found {len(resources)} resources")
            for resource in resources:
                print(f"   • {resource.name}: {resource.uri}")
                if hasattr(resource, 'description') and resource.description:
                    print(f"     Description: {resource.description}")

            # Read the static resource
            static_uri = resource.uri
            print(f"\n📖 Reading static resource: {static_uri}")
            try:
                result = await client.read_resource(static_uri)
                print(f"✅ Resource read successful: {result}")
            except Exception as e:
                print(f"❌ Resource read failed: {e}")

            # # Read the template resource
            # template_uri = "echo://hello"
            # print(f"\n📖 Reading template resource: {template_uri}")
            # try:
            #     result = await client.read_resource(template_uri)
            #     print(f"✅ Resource read successful: {result}")
            # except Exception as e:
            #     print(f"❌ Resource read failed: {e}")

            # List and demonstrate prompts
            print("\n💬 Discovering prompts...")
            prompts = await client.list_prompts()
            print(f"✅ Found {len(prompts)} prompts")
            for prompt in prompts:
                print(f"   • {prompt.name}: {prompt.description}")

            # Get the echo prompt
            if prompts:
                print("\n💬 Getting echo prompt...")
                try:
                    result = await client.get_prompt(prompt.name, {"text": "Hello from FastMCP Client!"})
                    print(f"✅ Prompt get successful: {result}")
                except Exception as e:
                    print(f"❌ Prompt get failed: {e}")

            print("\n✅ Demonstration completed successfully!")

    except Exception as e:
        print(f"❌ Demonstration failed: {e}")
        print("\n💡 Make sure the FastMCP server is running on http://localhost:8000")
        return 1

    return 0


def main():
    """Main function to run the FastMCP client demonstration."""
    try:
        return asyncio.run(demonstrate_fastmcp_server())
    except KeyboardInterrupt:
        print("\n🛑 Client interrupted")
        return 1


if __name__ == "__main__":
    exit(main())
