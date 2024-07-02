from pydantic import BaseModel


class YouTubeVideoResponse(BaseModel):
    transcript: str


class TranscriptRequest(BaseModel):
    transcript: str
    number: int = 0


class SummaryResponse(BaseModel):
    summary: str


class KeywordsResponse(BaseModel):
    keywords: list[str]


class SocialMediaPostsResponse(BaseModel):
    posts: list[str]
