from crewai import LLM
from django.conf import settings


basic_llm = LLM(
    model=settings.OPENAI_MODEL,
    api_key=settings.OPENAI_APIKEY,
    temperature=settings.OPENAI_DEFAULT_TEMPERATURE,
)
