from crewai.flow import Flow, start
from core.crews import ResumeScreeningCrew
from core.utils import pars_json_output


class HRPipelineFlow(Flow[HRPipelineState]):
    @start
    async def screen_resume(self):
        result = await(
            ResumeScreeningCrew.
        )