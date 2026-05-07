import logging
import aiohttp
import json
from typing import Any
from one_soul.profit.muscles.registry import Skill

logger = logging.getLogger("MCPSkill")

class MCPSkill(Skill):
    name = "mcp_connect"
    description = "Universal tool connector using Model Context Protocol (MCP)."

    async def execute(self, server_url: str = None, tool_name: str = None, arguments: dict = None) -> Any:
        """
        Connect to an MCP server and execute a tool.
        MCP is the industry standard (2026) for connecting agents to tools.
        """
        if not server_url or not tool_name:
            return "Error: MCP requires a server_url and tool_name."

        logger.info(f"Connecting to MCP Server: {server_url} | Tool: {tool_name}")

        # This is a simplified async MCP call (HuggingFace/Anthropic standard)
        payload = {
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": arguments or {}
            }
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(f"{server_url}/call", json=payload, timeout=30) as response:
                    if response.status == 200:
                        result = await response.json()
                        return result.get("result", "Success (No data)")
                    else:
                        return f"MCP Error: Status {response.status}"
        except Exception as e:
            logger.error(f"MCP Connection failed: {e}")
            return f"Error: Could not connect to MCP server. {str(e)}"
