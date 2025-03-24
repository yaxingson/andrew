import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP('AndrewServer')

@mcp.tool()
async def coding():
  pass


if __name__ == '__main__':
  mcp.run(transport='stdio')
