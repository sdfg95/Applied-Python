import aiohttp
import asyncio
import os


async def download_image(session, url, filename):
    async with session.get(url) as response:
        if response.status == 200:
            with open(filename, 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)


async def main(num_images, output_dir):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        tasks = []
        for i in range(num_images):
            image_url = f"https://picsum.photos/200/300"
            filename = os.path.join(output_dir, f"image_{i}.jpg")
            tasks.append(download_image(session, image_url, filename))
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    num_images = 5
    output_directory = "../../artifacts/5.1"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    asyncio.run(main(num_images, output_directory))
