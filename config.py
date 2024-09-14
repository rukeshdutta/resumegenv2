import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# Get Anthropic API key from environment variable
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

# Sections for resume
SECTIONS = [
    "Professional Summary",
    "Work Experience",
    "Skills",
    "Education",
    "Projects",
    "Certifications"
]

# Ensure API key is set
if not ANTHROPIC_API_KEY:
    raise ValueError("ANTHROPIC_API_KEY is not set in the environment variables.")
