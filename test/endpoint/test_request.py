import aiohttp
import asyncio

async def fetch_stream(url, payload):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            async for line in response.content.iter_any():  # ストリーミングレスポンスの読み込
                print(line.decode().strip(), flush=True, end="")

            print("\n", flush=True)

async def main():
    url = "http://localhost:8000/stream_chat"
    message = {"content": "自己紹介をしてくれますか？"}
    await fetch_stream(url, message)

if __name__ == "__main__":
    asyncio.run(main())

