"""
Fetch YouTube transcripts for expert research.
Run locally: pip install youtube-transcript-api
Then: python fetch_transcripts.py
"""

from youtube_transcript_api import YouTubeTranscriptApi
import os
import re

# Fill this in: expert_folder_name -> list of (video_title, youtube_video_id)
# video_id is the part after "v=" in a YouTube URL, e.g. https://www.youtube.com/watch?v=blG6gss-mUY -> blG6gss-mUY
VIDEOS = {
    "gael-breton": [
        # https://www.youtube.com/watch?v=JMbRFcQobHU
        ("What a Real AI Business Looks Like (No Hype)", "JMbRFcQobHU"),
    ],
    "michael-king": [
        # https://www.youtube.com/watch?v=JjPfPT37li0
        ("Your Inbox Might Be the Next AI Search Signal", "JjPfPT37li0"),
    ],
    "ross-simmonds": [
        # https://www.youtube.com/watch?v=gJR7rDkpqik
        ("The Marketing Engineer: Nick Lafferty on Building AI Systems for Profound", "gJR7rDkpqik"),
    ],
    "shiyam-sunder": [
        # Add real video IDs here if he has a channel, or leave empty and use podcast appearances
    ],
}

OUTPUT_ROOT = "research/youtube-transcripts"

def slugify(title):
    return re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

def fetch_and_save(api, expert, title, video_id):
    folder = os.path.join(OUTPUT_ROOT, expert)
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, f"{slugify(title)}.md")

    try:
        fetched = api.fetch(video_id)
        full_text = " ".join([snippet.text for snippet in fetched])
    except Exception as e:
        print(f"FAILED for {video_id}: {e}")
        return

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"**Video URL:** https://www.youtube.com/watch?v={video_id}\n\n")
        f.write("## Transcript\n\n")
        f.write(full_text)

    print(f"Saved: {filename}")

if __name__ == "__main__":
    api = YouTubeTranscriptApi()
    for expert, videos in VIDEOS.items():
        for title, video_id in videos:
            fetch_and_save(api, expert, title, video_id)
