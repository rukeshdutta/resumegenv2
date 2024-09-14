from anthropic import Anthropic
from config import ANTHROPIC_API_KEY

client = Anthropic(api_key=ANTHROPIC_API_KEY)

def extract_keywords(job_description):
    prompt = f"""Given the following job description, extract the most important keywords that a job applicant should focus on in their resume:

    Job Description:
    {job_description}

    Please provide a list of 10-15 important keywords or phrases, separated by commas."""

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=300,
        system="You are an expert in job market trends and resume writing.",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    keywords = [keyword.strip() for keyword in response.content[0].text.split(',')]
    return keywords