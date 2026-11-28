import json

from crewai.flow import Flow, start
from core.crews import ResumeScreeningCrew
from core.utils import parse_json_output

class HrPipelineFlow(Flow[HRPipelineState]):

    @start
    async def screen_resume(self):
        result = await(
            ResumeScreeningCrew().crew().kickoff_async(
                inputs={
                    "candidate_resume": self.candidate_resume,
                    "job_title": self.job_title,
                    "job_description": self.job_description,
                    "required_skills": self.required_skills
                }
            )
        )
        try:
            self.state.screening_output = parse_json_output(result.raw)
        except json.JSONDecodeError as exc:
            self.state.screening_output = {"error": "Invalid JSON"}
        return self.state.screening_output