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
    {
        "slug": "cdc-2024-part-1-autonomous-vehicles",
        "date": "2025-01-07",
        "category": "Research",
        "title": "Highlights from IEEE CDC 2024 — Part 1: Autonomous Vehicles",
        "body": """The IEEE Conference on Decision and Control (CDC) is the biggest annual gathering of control engineers and control theorists from around the world. I enjoyed IEEE CDC 2024 and decided to share the highlights from my perspective, for those who couldn't attend. In this first part I focus on autonomous vehicles, which were a prominent topic this year.

<strong>Plenary Talk 1.</strong> I suspect most people working on autonomous vehicles would agree that the biggest challenge is the <em>uncertainty</em> in the environment, and how to provide provable safety guarantees given that uncertainty. Two of the four plenaries dealt with autonomous vehicles, and one tackled uncertainty head-on: "Towards Safe and Resilient Autonomy Using Synergistic Control, Observation, and Learning," by Dimitra Panagou (University of Michigan). Her examples focused mainly on drones facing unexpected obstacles on a planned route — for instance a wall placed in their path — and the method her team developed to guarantee safety in such situations, with video clips of the results. She mentioned autonomous vehicles in her introduction, though the examples were drones; when I asked afterward, she said she could share more of her work on that topic, which I look forward to.

<strong>Plenary Talk 2.</strong> The other plenary was "Transforming Mobility through Learning and Control," by Karl Johansson (KTH), whose work I've followed for years and hold in high regard. He devoted much of it to platoons of cars — vehicles that communicate and coordinate along a route — with examples from his collaboration with Volvo, analyzing the congestion platoons can create on motorways and how to mitigate it. He was enthusiastic and encouraged younger control engineers to pursue the topic. I have to disagree here: except when platoons venture into unknown or hazardous areas, I don't see the benefit if each vehicle can already drive autonomously — and it introduces risk if the inter-vehicle communication is hacked, which is always possible. More compelling was his treatment of a single vehicle approaching a junction where other objects (vehicles, pedestrians) are occluded — incidentally, the best example I can think of for explaining observable vs. unobservable states, since here they are literally observable or not. His solution adds auxiliary devices at each junction that communicate what the vehicle can't see, including a worst-case analysis assuming a vehicle is always occluded behind the visible ones — useful for current industrial applications. The most interesting part, though, was theoretical and experimental work on the microscopic and macroscopic properties of traffic flows, using real-world recordings from routes in Sweden with Volvo and Scania. I've made a note to look into this more closely. His slides are <a href="https://people.kth.se/~kallej/bode24_handouts.pdf" target="_blank" rel="noopener">here</a>.

<strong>Other notable talks.</strong> Regular sessions were also dedicated to autonomous vehicles, of varying quality. Some works were intellectual curiosities rather than of near- or far-future use — a prime example, "A Feasibility Analysis at Signal-Free Intersections," proposed removing traffic lights so a device at each junction takes over and maneuvers all vehicles optimally; I find it impractical for various reasons. Others had real industrial relevance, such as "Uncertainty-Aware Decision-Making and Planning for Autonomous Forced Merging," a motion-planning scheme for a vehicle merging onto a road from a ramp given uncertainty in the estimated acceleration of adjacent vehicles.

<strong>There was more.</strong> Other talks covered the very important topic of the cybersecurity of self-driving cars, among others. You can search the "Autonomous vehicles" keyword in the <a href="https://css.paperplaza.net/conferences/conferences/CDC24/program/CDC24_KeywordIndexWeb.html" target="_blank" rel="noopener">conference program</a> to find the abstracts of all the relevant talks.

<em>Part 1 of 3 — originally published on <a href="https://www.linkedin.com/pulse/highlights-from-ieee-cdc-2024-part-1-autonomous-vahid-c2hge/" target="_blank" rel="noopener">LinkedIn</a>, January 7, 2025.</em>""",
    },
    {
        "slug": "cdc-2024-part-2-best-talk",
        "date": "2025-01-08",
        "category": "Research",
        "title": "Highlights from IEEE CDC 2024 — Part 2: The Best Talk of the Conference",
        "body": """One of the things I appreciate most about conferences like the IEEE Conference on Decision and Control is their approach to presenting research. Every presentation starts with a peer-reviewed paper submission; if accepted, the work earns a spot in the program. That gives researchers at every career stage — regardless of status, age, or experience — a chance to share their ideas. Each April I'm invited to review CDC submissions, and I make it a priority to give thorough, constructive reviews. It's a level playing field, which I find refreshing compared with fields such as neuroscience, where most presentations are invitation-only plenaries and the rest are relegated to poster sessions.

Each day opened with an hour-long plenary, followed by three sessions of six 20-minute talks. With 20 parallel sessions, an attendee can catch at most ~5% of the talks, so you have to plan carefully. Among everything I managed to see, one talk stood far above the rest — even above the plenaries: "Control-Coherent Koopman Modeling: A Physical Modeling Approach," by Prof. Harry Asada (MIT). Given how technical the topic is, let me try to explain why I think this work is ground-breaking and why more control engineers should know about it.

First, what is a Koopman operator? The idea goes back to Bernard Koopman and John von Neumann (1930–31), who proved that every nonlinear system can be transformed into an infinite-dimensional <em>linear</em> system — in more technical terms, mapped into a linear Hilbert space. The theorems, however, aren't constructive: they don't tell you how to obtain that infinite-dimensional system, and even if you could, you'd still need to approximate it with a finite-dimensional linear system to work with it. Finding that finite-dimensional approximation has been the subject of intense work for decades — if you've heard of Dynamic Mode Decomposition (DMD), that's one such method. This is what "Koopman modeling" in the title refers to.

But to control a system you need an input — and here lies the biggest shortcoming of current methods, and what makes Prof. Asada's work so ground-breaking. So far these methods have focused on systems with no inputs (in control terms, autonomous systems). Asada's work considers systems <em>with</em> inputs (non-autonomous systems) and provides a way to approximate a nonlinear system, including its relationship with the input, by a finite-dimensional linear system. Consider what that means: if you can find the Koopman model of a non-autonomous nonlinear system, the control problem becomes a <em>linear</em> control problem, no matter how nonlinear the original system was. He showed examples, including a highly nonlinear hydraulic system whose control problem became linear under this method. If you have even a cursory knowledge of nonlinear control, you can see why I found this so exciting.

While listening, an idea struck me. Researchers analyzing neuroscience data are often already familiar with DMD for signals such as EEG or electrophysiological recordings from Utah arrays — but, because of the limitation above, these approaches typically ignore the inputs to the system, inputs that here could be the stimuli a human or animal receives while interacting with the environment. One workaround I've used myself is to apply DMD to signals from different experimental conditions and compare the extracted modes. But what if we could incorporate inputs — such as visual stimuli — into the Koopman model more explicitly? In one tempting example: what if the subject is a human driver under critical scenarios? Could we gain new insight by building a Koopman model that treats visual stimuli as inputs and EEG signals as system states — and explore the relationship between those brain states and muscle movements such as steering or braking? These are still rough ideas, but theoretical breakthroughs like this make them worth investigating.

I had a very nice chat with Prof. Asada afterward and was pleasantly surprised to learn he's been extending the concept to human locomotion. He didn't go into detail but said the work would be published soon; I'm eager to see how they apply this framework to such an interesting problem.

If you'd like to know more, I recommend their preprint on <a href="https://arxiv.org/abs/2403.16306" target="_blank" rel="noopener">arXiv</a>.

<em>Part 2 of 3 — originally published on <a href="https://www.linkedin.com/pulse/highlights-from-ieee-cdc-2024-part-2-best-talk-vahid-xc66e/" target="_blank" rel="noopener">LinkedIn</a>, January 8, 2025.</em>""",
    },
    {
        "slug": "cdc-2024-part-3-a-little-bit-of-everything",
        "date": "2025-01-16",
        "category": "Research",
        "title": "Highlights from IEEE CDC 2024 — Part 3: A Little Bit of Everything",
        "body": """I've already shared what I found interesting at the IEEE Conference on Decision and Control 2024 in two previous posts. CDC 2024 was a huge conference in an interesting venue with many parallel tracks, and I saw only a small fraction of what was on offer. In this part I gather the various talks I found interesting but didn't cover before. A big shout-out to Maria Prandini, Luca Zaccarian, and Sophie Tarbouriech, who did an amazing job as the organizing committee.

<h2>Neuroscience</h2>

There weren't many neuroscience-related works at CDC 2024, which was a bit disappointing — at least not as many as I'd hoped. Among those I attended, one was notable: "Feedforward Regulation of Interneuronal Communication," which aimed to formulate a mechanism of neurotransmitter release in a chemical synapse. It's an ambitious goal, but given how hard it is to measure neurotransmitter concentration in the synaptic cleft, I don't see how such models can currently be tested experimentally — still, it's a step in the right direction. A few other talks touched on neuroscience, but from their titles and abstracts I could tell they suffer from the issues that are unfortunately common in the mathematical modeling of biological systems: they are far removed from what neuroscientists actually care about. If you have a mathematical or technical background and want to collaborate with biologists, I highly recommend "Letters to a Young Scientist" by the late E. O. Wilson — it helps you see how biologists view the world.

Another, on computational neuroscience, caught my attention: "Approximation of Koopman Operator Using Spiking Neural Networks." I file it under neuroscience because spiking neural networks are designed to work best with neuromorphic processors — though the talk was purely theoretical, with no implementation on a neuromorphic chip, which was a letdown. If you haven't heard of neuromorphic computing, the basic idea is that, unlike conventional processors, the units communicate using "spikes" (like the action potentials our neurons use). I recommend this <a href="https://ieeexplore.ieee.org/document/9612647" target="_blank" rel="noopener">IEEE Control Systems Magazine article</a> by Prof. Rodolphe Sepulchre (a preprint is findable by searching the title). I firmly believe neuromorphic computing can be a game-changer for certain models, but it needs investment from chip manufacturers — and right now few seem interested.

<h2>Data-Driven Control</h2>

Two data-driven talks stood out. "Data-Driven Architecture to Encode Information in the Kinematics of Robots and Artificial Avatars," a collaboration between groups in Naples and Hamburg, builds on the fact that people encode information in their movements — from how someone grabs a bottle you can tell whether they mean to pour from it or drink from it. Their work addressed not only intentions but emotions, e.g. detecting a person's emotion from wrist movements and carrying that into virtual reality. The other, "Towards eXplainable Data-Driven Control (XDDC): The Property-Preserving Framework," aimed to quantify how much we can trust a data-driven model or controller, bringing ideas from explainable AI into data-driven control — a concept I'm increasingly convinced deserves more attention.

<h2>Mathematical Epidemiology</h2>

Epidemiology is another topic I've worked on and enjoyed. One talk piqued my interest: "Spiking Systems in Population-Infection Dynamics," by the great Franco Blanchini. "Spiking" here refers to a phenomenon I hadn't realized could occur in epidemiological systems — the textbook case of a system that always converges to an equilibrium yet cannot be called stable. The talk mostly formulated and introduced the phenomenon in the epidemiological context; Prof. Blanchini said he's working on it now, and I'm very curious what comes out of it.

<h2>Large Language Models</h2>

Unsurprisingly, LLMs featured heavily. It began with a first-day plenary, "Ask Not What AI Can Do for Control, Ask What Control Can Do for AI," by Prof. Paolo Tabuada — I got stuck in on-site registration and missed the beginning, but it was a mathematically rigorous talk on how control theory can enhance LLMs. A whole session was dedicated to the topic; I attended two talks. "Prompt a Robot to Walk with Large Language Models" (Berkeley) fed a robot's coordinates in a virtual environment to an LLM and asked it to return low-level control actions. "REAL: Resilience and Adaptation using Large Language Models on Autonomous Aerial Robots" (MIT) claimed a scheme that uses LLM outputs to increase the resilience of the control system for scenarios it wasn't designed for. At the end of the second talk, someone asked why they used LLMs rather than the many methods control theory already offers for such cases, given that with LLMs you can claim nothing about stability. For a second I hoped for an honest answer — that they'd jumped on the LLM bandwagon because it's what everyone talks about. Instead the answer sounded a lot like what an LLM would produce if you fed it the question.

<h2>Model Reduction</h2>

A tutorial session, "Forty Plus Years of Model Reduction and Still Learning," gave a nice overview of the history of model reduction and the various approaches control theorists have proposed. I find that understanding the history of a technical concept often sheds light on its meaning — this isn't limited to model reduction; even fundamental ideas like the derivative gain new depth when you explore how they developed. Sometimes a concept's journey through history reveals insights a textbook won't.

<h2>Industry</h2>

Several companies had a notable presence. The one I liked most was Mitsubishi Electric Research Laboratories. They had a stand, and I spoke with one of their researchers who had given a talk titled "Inscribing and Separating an Ellipsoid and a Constrained Zonotope: Applications in Stochastic Control and Centering" — the title alone tells you what kind of research environment they have. They also work on autonomous vehicles and seem to be hiring; from what I gathered, it's a great place for a control engineer who wants to do research in an industrial setting.

<h2>Check out more</h2>

These were simply the topics of most interest to me. For everything that was on offer, see the full <a href="https://css.paperplaza.net/conferences/conferences/CDC24/program/" target="_blank" rel="noopener">conference program</a>.

<em>Part 3 of 3 — originally published on <a href="https://www.linkedin.com/pulse/highlights-from-ieee-cdc-2024-part-3-little-bit-vahid-b5rue/" target="_blank" rel="noopener">LinkedIn</a>, January 16, 2025.</em>""",
    },
]
