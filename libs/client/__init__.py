import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from contextlib import AsyncExitStack
from typing import Optional

class MCPClient:
  def __init__(self):
    self.session: Optional[ClientSession] = None
    self.exit_stack = AsyncExitStack()

  async def connect_mcp_server(self, script_path:str):
    is_python = script_path.endswith('.py')
    is_js = script_path.endswith('.js')

    if not (is_python or is_js):
      raise ValueError('')

    command = 'python' if is_python else 'node'

    server_params = StdioServerParameters(
      command=command,
      args=[script_path],
      env=None,
    )

    stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
  




  async def process_query(self, query:str):
    pass

  async def chat(self):
    while True:
      try:
        query = input('\nQuery: ').strip()

        if query.lower() == 'quit':
          break
        
      except Exception as e:
        pass

  async def cleanup(self):
    self.exit_stack.aclose()

__all__ = ['MCPClient']
