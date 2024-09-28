from fastapi import FastAPI
from time import time
import httpx
import asyncio
from urllib.parse import parse_qs

app = FastAPI()

hostName = "localhost"
serverPort = 8080
url = 'https://anderepostfach.amocrm.ru/api/v4/users'
bearer = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjUyNGQ5YzBjMDIyNDdlOGZkOTY4Njg4Mjc2MmE5YzM5NmFlYjE4NjNhYzdiYTdhNmFlODFmYmM2N2U4ODkzZDkxMWE3MjAyYmQzYjQ1YmFjIn0.eyJhdWQiOiI4NTMwOGUxZC1lMWM3LTQxZjYtYWI2OS00OTNhYmZlZGM1N2YiLCJqdGkiOiI1MjRkOWMwYzAyMjQ3ZThmZDk2ODY4ODI3NjJhOWMzOTZhZWIxODYzYWM3YmE3YTZhZTgxZmJjNjdlODg5M2Q5MTFhNzIwMmJkM2I0NWJhYyIsImlhdCI6MTcyNjcyMjAzOSwibmJmIjoxNzI2NzIyMDM5LCJleHAiOjE3Mjc2NTQ0MDAsInN1YiI6IjExNTM4MzI2IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMxOTU4ODEwLCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJjcm0iLCJmaWxlcyIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiLCJwdXNoX25vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiMTE4ZGZhYTgtOGZkMC00MjY5LTlkNmItOTdiMjM3ZjIyNWQ1IiwiYXBpX2RvbWFpbiI6ImFwaS1iLmFtb2NybS5ydSJ9.Sq5hbis_rAp-0s3VV67-ZUXk0Elgk6KRDzZOtF7eYBVlUo2xUvTsz7BOpbqlTErzu0G9uj6DRsxXlMUlndkjR3NW0m7cL-Rz99NCZL86RNHN6ooFojEe1so1hOnEsNrjHPAHWoc213UWEbf2kROh3eKeauOM7w74fbLt_Pz5Eee_SRuKmEEUfCRQqJ-HsCMcSlLEaJgJMKdyXaLnaceLjE2kDMV71PWYJUcBockzqdCgA1I96xOCs1ANzFAi6g5-E2lTxc0RhrHUcz8XxYyMDOlpb_oIbMhOSSyrHm_GIXDlbVcEmRQs8-PGGW1mXy1Jp9nagK0umH2H7JUs_nDn6Q'

headers = {
  'User-Agent': 'My App v1.0',
  'Authorization': bearer
}
# main.py

async def request(client):
    response = await client.get(url, headers=headers)
    return response.text

async def task():
    async with httpx.AsyncClient() as client:
        tasks = [request(client) for i in range(100)]
        result = await asyncio.gather(*tasks)
        print(result)

@app.get('/')
async def f():
    start = time()
    await task()
    print("time: ", time() - start)