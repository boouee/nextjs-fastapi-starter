from fastapi import FastAPI, Request
from time import time
import httpx
import asyncio
from urllib.parse import parse_qs

app = FastAPI()

hostName = "localhost"
serverPort = 8080
#url = 'https://anderepostfach.amocrm.ru/api/v4/'
url = 'https://mrealtymoscow.amocrm.ru/api/v4/users'
bearer = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImJkNWI5MmMwOTQzOWFmZjIzNDg2NjY3ZGQ0ZDkwZTQ0MTJlNTU3YTZmZjI5NDRmZTNhMDVjMTczZTM4YjU0YjYxYzBmNWM0MjIyNzRkZGNmIn0.eyJhdWQiOiIyNGVjM2VkMS05ZTk3LTQ3MjItOGZmZC0xMzcxZjlhMTA4ZTAiLCJqdGkiOiJiZDViOTJjMDk0MzlhZmYyMzQ4NjY2N2RkNGQ5MGU0NDEyZTU1N2E2ZmYyOTQ0ZmUzYTA1YzE3M2UzOGI1NGI2MWMwZjVjNDIyMjc0ZGRjZiIsImlhdCI6MTcyNzM0MjE3MywibmJmIjoxNzI3MzQyMTczLCJleHAiOjE3NjcyMjU2MDAsInN1YiI6IjExMjgyMjU4IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMxODUyMzY2LCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJjcm0iLCJmaWxlcyIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiLCJwdXNoX25vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiOTE1NjA2YzMtMTllNi00YWU0LWE4NTQtNDhiZmEwZTk3NzAyIiwiYXBpX2RvbWFpbiI6ImFwaS1iLmFtb2NybS5ydSJ9.kS2Sr3YisHkImnywzGAZTt7gBaLehdwbiQbB0tz9COL8uLou-skVDf5-Ypl50X3UIyX1AGwYx4tcqnDxxM5zwv5S4HjCgYlHDJyk0JXAzBpd8IHEaGHROTguL3tQYcCeqBcRoDEhumQtosS1GnPFDIOXkjlBBANiZZ2EPU_IWbIdVTkTmEjkQIJq1oBLwASXq6YnuhpqvLBWPzal4s4UeCdhzP-yHHY3-1A7eal1-1wdSZ-7qyeCJsClA9bdnRXvaaZtr2hDYcUUhcaYlngEaz6eZMurmmpLZqGD51K0-u8PEoJthUURo4sw3bUSb71KLQqrdgrgvtvE4vrV4u14zQ'
#bearer = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjUyNGQ5YzBjMDIyNDdlOGZkOTY4Njg4Mjc2MmE5YzM5NmFlYjE4NjNhYzdiYTdhNmFlODFmYmM2N2U4ODkzZDkxMWE3MjAyYmQzYjQ1YmFjIn0.eyJhdWQiOiI4NTMwOGUxZC1lMWM3LTQxZjYtYWI2OS00OTNhYmZlZGM1N2YiLCJqdGkiOiI1MjRkOWMwYzAyMjQ3ZThmZDk2ODY4ODI3NjJhOWMzOTZhZWIxODYzYWM3YmE3YTZhZTgxZmJjNjdlODg5M2Q5MTFhNzIwMmJkM2I0NWJhYyIsImlhdCI6MTcyNjcyMjAzOSwibmJmIjoxNzI2NzIyMDM5LCJleHAiOjE3Mjc2NTQ0MDAsInN1YiI6IjExNTM4MzI2IiwiZ3JhbnRfdHlwZSI6IiIsImFjY291bnRfaWQiOjMxOTU4ODEwLCJiYXNlX2RvbWFpbiI6ImFtb2NybS5ydSIsInZlcnNpb24iOjIsInNjb3BlcyI6WyJjcm0iLCJmaWxlcyIsImZpbGVzX2RlbGV0ZSIsIm5vdGlmaWNhdGlvbnMiLCJwdXNoX25vdGlmaWNhdGlvbnMiXSwiaGFzaF91dWlkIjoiMTE4ZGZhYTgtOGZkMC00MjY5LTlkNmItOTdiMjM3ZjIyNWQ1IiwiYXBpX2RvbWFpbiI6ImFwaS1iLmFtb2NybS5ydSJ9.Sq5hbis_rAp-0s3VV67-ZUXk0Elgk6KRDzZOtF7eYBVlUo2xUvTsz7BOpbqlTErzu0G9uj6DRsxXlMUlndkjR3NW0m7cL-Rz99NCZL86RNHN6ooFojEe1so1hOnEsNrjHPAHWoc213UWEbf2kROh3eKeauOM7w74fbLt_Pz5Eee_SRuKmEEUfCRQqJ-HsCMcSlLEaJgJMKdyXaLnaceLjE2kDMV71PWYJUcBockzqdCgA1I96xOCs1ANzFAi6g5-E2lTxc0RhrHUcz8XxYyMDOlpb_oIbMhOSSyrHm_GIXDlbVcEmRQs8-PGGW1mXy1Jp9nagK0umH2H7JUs_nDn6Q'

headers = {
  'User-Agent': 'My App v1.0',
  'Authorization': bearer
}
# main.py

async def get_body(request: Request):
    return await request.json()

async def get_users(client):
    response = await client.get(url + 'users', headers=headers)
    return response.text

async def check_lead(client, name):
    response = await client.get(url + 'leads?name=' + name, headers=headers)
    return response.text

async def post_lead(client, data):
    response = await client.post(url + 'leads', headers=headers, data=data)
    return response.text

async def task(request):
    async with httpx.AsyncClient() as client:
        tasks = [request(client) for i in range(100)]
        result = await asyncio.gather(*tasks)
        return result
        print(result)

#fn: str, name: str | None = None

@app.get('/api/{fn}')
async def users():
    start = time()
    return fn
    #function = get_users if fn == 'users' else check_lead
    #output = await task(function(name))
    #print("time: ", time() - start)
    #return output

@app.post('/api')
async def f(request: Request):
    start = time()
    output = await task(post_lead)
    print("time: ", time() - start)
    return output