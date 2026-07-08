# 100Hires Portfolio Project — Gourav Goyal

**Name:** Gourav Goyal
**Email:** Gouravgoyal2603@gmail.com
**Date:** July 2026

---

## Step 1 — Environment Setup

### Tools Installed

- **Cursor IDE** — Downloaded and installed from https://cursor.com/
- **Claude Code extension** — Installed via Cursor Extensions panel and logged in
- **Codex extension** — Installed via Cursor Extensions panel and logged in
- **Git** — Configured with my name (Gourav Goyal) and email (Gouravgoyal2603@gmail.com)
- **GitHub** — Created a public repository at github.com

### Steps Completed

1. Installed Cursor IDE from cursor.com
2. Installed Claude Code extension in Cursor — logged in
3. Installed Codex extension in Cursor — logged in
4. Created public GitHub repository named "100hires-portfolio"
5. Opened repository in Cursor
6. Created README.md file
7. Committed and pushed to GitHub
8. Sent GitHub link via email reply

### Issues I Ran Into and How I Solved Them

**Issue 1 — Claude Code account:**
When I first set up Claude Code, it was connected to a work account. I logged out using `claude logout` in the terminal and logged back in with my primary account (Gouravgoyal2603@gmail.com).

**Issue 2 — Codex installation:**
Could not find the Extensions panel initially. Figured out that Ctrl+Shift+X opens Extensions marketplace. Installed Codex successfully.

**Issue 3 — README.md not created during repo setup:**
Skipped README during repository creation. Solved by using GitHub's built-in file editor.

**Issue 4 — Git configuration:**
Configured Git manually using terminal:
`git config --global user.name "Gourav Goyal"`
`git config --global user.email "Gouravgoyal2603@gmail.com"`

---

## Step 2 — AI-Powered SEO Content Production Research

### Project Objective

This repository documents original research into how practitioners use AI to produce, optimize, and distribute SEO content at scale. Material collected includes LinkedIn posts and YouTube transcripts from 10 verified experts active in 2025-2026.

This is not a summary of blog posts about AI SEO. It is a structured collection of what these people are actually saying and doing right now.

### Selection Methodology

Five criteria used to qualify each expert:

1. **Active in 2025-2026** — posted or published within last 3 months
2. **Practitioner, not pundit** — works with real clients, not just a content creator
3. **AI tools in actual use** — demonstrates AI in workflow, not just talks about it
4. **Specific and verifiable** — shares numbers, case studies, reproducible methods
5. **Not on generic Top-10 listicles** — deliberately excluded names on every mainstream list

Full methodology in `research/expert-selection-log.md`

### Why These 10 Experts

| # | Name | Role | Why Selected |
|---|------|------|--------------|
| 1 | Kevin Indig | Growth Advisor, ex-Shopify | Bridges technical SEO and AI strategy; practitioner-grade newsletter |
| 2 | Michael King | Founder, iPullRank | AI Search Marketer of Year 2025; Relevance Engineering framework |
| 3 | Aleyda Solis | SEO Consultant, Orainti | SEOFOMO newsletter; bridges classic SEO with AI search practically |
| 4 | Wil Reynolds | Founder, Seer Interactive | Search intent + AI intersection; underrated outside generic lists |
| 5 | Mark Williams-Cook | Co-founder, Candour | Core Updates newsletter; data-driven UK practitioner |
| 6 | Suganthan Mohanadasan | SEO Consultant, Norway | Niche technical AI SEO; rarely on generic lists |
| 7 | Gael Breton | Co-founder, Authority Hacker | Built actual AI content systems with documented results |
| 8 | Ross Simmonds | CEO, Foundation Marketing | Pioneered GEO; Create Once Distribute Forever framework |
| 9 | Himani Kankaria | Founder, Missive Digital, India | India-based practitioner building AI SEO workflows for real clients |
| 10 | Shiyam Sunder | SEO Consultant, India | India-based technical SEO actively using AI in content production |

### Data Collection Workflow

**YouTube Transcripts**
Used `youtube-transcript-api` Python library via script built with Claude Code (`research/youtube-transcripts/fetch_transcripts.py`). Collected transcripts for Michael King, Ross Simmonds, and Gael Breton. Shiyam Sunder has no personal YouTube channel — his content is via LinkedIn and TripleDart blog instead.

**LinkedIn Posts**
Collected manually — LinkedIn restricts automated scraping. Visited each expert's profile, filtered for AI + SEO posts from 2025-2026, saved post text, date, URL, and engagement in structured markdown files.

### Scripts and Prompts

**fetch_transcripts.py** — Python script built with Claude Code to fetch YouTube transcripts automatically using youtube-transcript-api library.

**Claude Code Prompts Used:**

Prompt 1 — YouTube Transcript Script:
"Write a Python script that takes a list of YouTube video URLs, uses youtube-transcript-api to fetch each transcript, and saves each one as a markdown file in research/youtube-transcripts/<expert-name>/ with video title, URL, and full transcript text."

Prompt 2 — Folder Structure:
"Create folder structure for research project with research/linkedin-posts/, research/youtube-transcripts/, and research/other/ subfolders."

**How Claude Code Was Used:**
Claude Code wrote the initial versions of scripts. All research decisions — which experts to select, what content to collect, how to annotate — were made manually by me. AI was used as a tool to move faster, not to make decisions.

### Repository Structure
100hires-portfolio/
├── README.md
├── requirements.txt
├── .gitignore
├── research/
│   ├── sources.md
│   ├── expert-selection-log.md
│   ├── linkedin-posts/
│   │   ├── kevin-indig/
│   │   ├── michael-king/
│   │   ├── aleyda-solis/
│   │   ├── wil-reynolds/
│   │   ├── mark-williams-cook/
│   │   ├── suganthan-mohanadasan/
│   │   ├── gael-breton/
│   │   ├── ross-simmonds/
│   │   ├── himani-kankaria/
│   │   └── shiyam-sunder/
│   └── youtube-transcripts/
│       ├── fetch_transcripts.py
│       ├── michael-king/
│       ├── gael-breton/
│       └── ross-simmonds/
### Early Patterns Found

- 8 of 10 experts use AI for topical mapping and query fan-out — not just drafting
- All 10 emphasize human judgment on top of AI output
- GEO emerging as next layer above traditional SEO
- Answer-first content structure consistent across all experts

### Known Limitations

- LinkedIn posts collected manually — platform restricts automated scraping
- Shiyam Sunder has no personal YouTube channel — LinkedIn posts used instead
- Some videos had no auto-generated transcripts available

---

## About Me

I am Gourav Goyal, a digital marketer with 1+ year of hands-on experience in SEO, Meta Ads, Shopify, and AI-powered workflows. I use Claude and ChatGPT daily in my current role for content automation and reporting. This project was my first time working with GitHub, Cursor, and Python scripts — I figured out each step independently using YouTube tutorials and documentation.
