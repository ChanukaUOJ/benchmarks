import asyncio
from concurrent.futures import ThreadPoolExecutor
from locust import HttpUser, task, between
from aiohttp import ClientSession
from active_ministry_list_direct_api_calls.active_ministry_list import BenchmarkTestingService
from active_ministry_list_direct_api_calls.util_functions import IncomingServiceAttributes

executor = ThreadPoolExecutor(max_workers=5)  # adjust parallel threads if needed

class WebsiteUserDirectApi(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        self.config = {"BASE_URL_QUERY": self.host}
        self.benchmark_service = BenchmarkTestingService(self.config)
        self.statService = IncomingServiceAttributes(self.config)

    @task
    def benchmarkApiDirect(self):
        presidentId = "2403-03-01_cit_1"
        selectedDate = "2025-10-18"

        # run asyncio code in a separate thread
        def run_async():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            async def async_task():
                # create a session per async thread
                async with ClientSession() as session:
                    return await self.benchmark_service.benchmarkTestingAPI(
                        session=session,
                        presidentId=presidentId,
                        selectedDate=selectedDate,
                        statService=self.statService
                    )
            return loop.run_until_complete(async_task())

        result = executor.submit(run_async).result()
        # result now has the response
        print(f"Got {len(result)} portfolios")
