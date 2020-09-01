from prefect import Flow
import prefect
from loguru import logger
from prefect.engine.flow_runner import FlowRunner
from prefect.engine.results import LocalResult
from sample.tasks.sample_task import SampleTask

sample_task = SampleTask(
    target="sample_cache_file.pickle",
    checkpoint=True,
    result=LocalResult(dir="./cache"),
)

with Flow("Running example flow") as flow1:
    txt_result = sample_task()


FlowRunner(flow=flow1).run()

