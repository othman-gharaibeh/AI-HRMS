from typing import Optional, Dict

from pydantic import BaseModel


class HRPipelineState(BaseModel):

    candidate_id: Optional[int] = None
    job_position_id: Optional[int] = None

    #Inputs
    candidate_resume: str = ""
    job_title: str = ""
    job_description: str = ""
    required_skills: str = ""

    #Outputs
    screening_output: Dict = {}
    interview_output: Optional[Dict] = None
    final_output: Dict = {}