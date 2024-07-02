from fastapi import FastAPI

from models import (
    YouTubeVideoResponse,
    TranscriptRequest,
    SummaryResponse,
    KeywordsResponse,
    SocialMediaPostsResponse,
)
from youtube import (
    get_youtube_transcript,
    create_summary_of_transcript,
    extract_keywords_from_transcript,
    create_social_media_posts,
)

app = FastAPI()


@app.get("/transcript")
async def transcript(video_id: str) -> YouTubeVideoResponse:
    """Get a transcript for a video id"""
    transcript = get_youtube_transcript(video_id)
    return YouTubeVideoResponse(transcript=transcript)


@app.post("/summarize")
async def summarize(request: TranscriptRequest) -> SummaryResponse:
    """Summarize a transcript"""
    summary = create_summary_of_transcript(request.transcript)
    return SummaryResponse(summary=summary)


@app.post("/keywords")
async def keywords(request: TranscriptRequest) -> KeywordsResponse:
    """Extract keywords from a transcript"""
    keywords = extract_keywords_from_transcript(request.transcript, n=request.number)
    return KeywordsResponse(keywords=keywords)


@app.post("/social-media-posts")
async def social_media_posts(request: TranscriptRequest) -> SocialMediaPostsResponse:
    """Create social media posts from a transcript"""
    posts = create_social_media_posts(request.transcript, n=request.number)
    return SocialMediaPostsResponse(posts=posts)
