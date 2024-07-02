from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import marvin

load_dotenv()


def get_youtube_transcript(video_id: str) -> str:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([entry["text"] for entry in transcript])
    return full_text


def create_summary_of_transcript(transcript: str) -> str:
    instructions = f"Create a concise summary of this YouTube transcript: {transcript}"
    summary = marvin.generate(n=1, instructions=instructions)
    return summary[0]


def extract_keywords_from_transcript(transcript: str, *, n: int = 5) -> list[str]:
    instructions = f"Extract keywords from this YouTube transcript: {transcript}"
    keywords = marvin.generate(n=n, instructions=instructions)
    return keywords


def create_social_media_posts(transcript: str, *, n: int = 1) -> list[str]:
    instructions = (
        f"Create a social media post from this YouTube transcript: {transcript}"
    )
    posts = marvin.generate(n=n, instructions=instructions)
    return posts


if __name__ == "__main__":
    transcript = get_youtube_transcript("fcMr4NllFUM")
    summary = create_summary_of_transcript(transcript)
    print(f"Summary: {summary}")
    keywords = extract_keywords_from_transcript(transcript)
    print(f"Keywords: {keywords}")
    social_media_posts = create_social_media_posts(transcript, n=2)
    print("Social media post:")
    for i, post in enumerate(social_media_posts, start=1):
        print(f"{i}. {post}")
