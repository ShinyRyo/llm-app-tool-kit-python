import aiohttp
import asyncio

async def fetch_stream():
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:8000/stream_chat', json={'content': '現在のイーサリアム価格をドルで取得してくれますか？'}, headers={'accept': 'text/event-stream'}) as response:
            async for chunk in response.content.iter_chunked(1024):  # 1KBのチャンクサイズ
                print(chunk.decode('utf-8'), end='', flush=True)

loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_stream())
