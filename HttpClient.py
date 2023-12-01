import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:

        payload = {'station': 'RTL'}

        async with session.post(url = 'http://localhost:8080/radio-change/', data = payload) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:100])
        
        async with session.get('http://localhost:8080/radio') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:100])

asyncio.run(main())