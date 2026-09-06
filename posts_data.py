# ─────────────────────────────────────────────────────────────────────────────
#  YOUR BLOG POSTS  —  edit this file to add, remove, or change posts.
#
#  Each post is one entry in the POSTS list below. Fields:
#     slug     : short id used in the URL, lowercase-with-hyphens (must be unique)
#     date     : YYYY-MM-DD  ← YOU set this. The blog is always sorted by it,
#                newest first. (You can post-date or back-date freely.)
#     category : one of  "Research"  "Essays"  "Film"  "Life & Society"  "Notes"
#                (add your own — new categories appear as filter buttons automatically)
#     title    : the post title
#     body     : the full text. Separate paragraphs with a BLANK LINE.
#                The FIRST paragraph is what shows on the Thoughts page as the teaser.
#                You can use normal HTML inside (e.g. <a href="...">link</a>, <em>…</em>).
#
#  After editing, run:  python3 build.py   (regenerates thoughts.html + posts/)
# ─────────────────────────────────────────────────────────────────────────────

SCHOLAR = "https://scholar.google.de/citations?user=1pur7AwAAAAJ&hl=en"

POSTS = [
    {
        "slug": "welcome",
        "date": "2026-01-05",
        "category": "Notes",
        "title": "What this page is",
        "body": """This is where I write in the open. Some of it is my own scientific work — new papers, tools I've released, results worth sharing. Some of it isn't: notes on films I've watched, and the occasional longer argument about life and the questions I keep coming back to.

I'm a control engineer and neuroscientist by training, so the research posts lean technical. The rest is just me thinking out loud. Use the filters at the top to read only what interests you — for example, tap <strong>Research</strong> to see only my scientific work.""",
    },
    {
        "slug": "uncertainty-preprint",
        "date": "2025-11-15",
        "category": "Research",
        "title": "New preprint: decision-making under uncertainty",
        "body": """A new preprint looks at how people adapt their strategies when the consequences of their choices are uncertain. Using a set-shifting task, we tracked pupil-linked arousal — a proxy for the brain's noradrenaline system — and related it to moment-to-moment decisions.

The thread back to my other work is the same one that runs through all of it: how a system, biological or engineered, adjusts its own behaviour in the face of uncertainty.

<a href="%s" target="_blank" rel="noopener">Read it on Google Scholar &#8599;</a>""" % SCHOLAR,
    },
    {
        "slug": "mitfat-joss",
        "date": "2021-03-01",
        "category": "Research",
        "title": "MiTfAT, peer-reviewed in JOSS",
        "body": """MiTfAT is a Python library for analysing molecular and functional MRI data — loading, cleaning, clustering, and visualising time-series from fMRI experiments. It grew out of the imaging work I did at the Max Planck Institute, and it's now peer-reviewed and published in the Journal of Open Source Software.

<a href="https://joss.theoj.org/papers/10.21105/joss.02827" target="_blank" rel="noopener">Read the JOSS paper &#8599;</a> &nbsp;&middot;&nbsp; <a href="https://github.com/vahid-sb/MiTfAT" target="_blank" rel="noopener">MiTfAT on GitHub &#8599;</a>""",
    },
    {
        "slug": "covid-modeling",
        "date": "2021-02-15",
        "category": "Research",
        "title": "Modeling COVID-19 containment and vaccination",
        "body": """Early in the pandemic I built an age-stratified compartmental model to ask a concrete question: given limited doses, how should a vaccine be distributed across age groups, and how do containment policies change that answer? The study appeared in PLOS ONE.

The tools behind it are open source — <a href="https://github.com/vahid-sb/MiTepid_sim" target="_blank" rel="noopener">MiTepid_sim</a> for simulation and <a href="https://github.com/vahid-sb/MiTepid_opt" target="_blank" rel="noopener">MiTepid_opt</a> for fitting parameters to real data.

<a href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0247439" target="_blank" rel="noopener">Read it in PLOS ONE &#8599;</a>""",
    },
]
