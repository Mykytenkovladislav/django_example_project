import aiohttp
import asyncio
import json
import os
from aiohttp import ClientSession
from aiohttp.web_exceptions import HTTPError

API = ("http://api.weatherstack.com/current?access_key=3438564562d8d3600069b3a05762c850&query=Kharkiv",
       "https://www.metaweather.com/api/location/922137/",
       'https://api.oceandrivers.com:443/v1.0/getAemetStation/kharkiv/lastdata/')
TEMPERATURE_STORE = []


async def get_weather_details_async(api_link, session):
    try:
        response = await session.request(method='GET', url=api_link)
        response.raise_for_status()
        print(f"Response status ({api_link}): {response.status}")
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error ocurred: {err}")
    response_json = await response.json()
    return response_json


async def weatherstack(api_link, session):
    response = await get_weather_details_async(api_link, session)
    current_info = response.get('current')
    temperature = current_info.get('temperature', None)
    print(f"Temperature by WEATHERSTACK_API: {temperature}")
    TEMPERATURE_STORE.append(temperature)


async def metaweather(api_link, session):
    response = await get_weather_details_async(api_link, session)
    current_info = response.get("consolidated_weather", [{}])[0]
    temperature = current_info.get('the_temp', None)
    print(f"Temperature by METAWEATHER_API: {temperature}")
    TEMPERATURE_STORE.append(temperature)


async def oceandrivers(api_link, session):
    response = await get_weather_details_async(api_link, session)
    temperature = response.get('TEMPERATURE', None)
    print(f"Temperature by OCEANDRIVERS_API: {temperature}")
    TEMPERATURE_STORE.append(temperature)


async def running_program():
    async with ClientSession() as session:
        await asyncio.gather(weatherstack(API[0], session), metaweather(API[1], session), oceandrivers(API[2], session))
        temperature = 0.0
        for i in TEMPERATURE_STORE:
            temperature += i
        print(f'Median temperature is: {temperature/3}')


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(running_program())
    loop.close()


if __name__ == '__main__':
    main()
