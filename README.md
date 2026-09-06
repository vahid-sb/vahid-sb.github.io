# Vahid S. Bokharaie — personal website

A fast static website (plain HTML/CSS/JS, no framework). Nothing needs to run on a
server. A tiny Python script (`build.py`) regenerates the blog when you add a post —
but the files here are already built and ready to upload as-is.

## What's in here

| File / folder    | What it is |
|------------------|------------|
| `index.html`     | The main page (about, research, software, trajectory, publications, contact) |
| `thoughts.html`  | The **Thoughts & Past Work** page — list of posts, filterable by category, newest first *(generated)* |
| `posts/`         | One HTML file per post — the full text pages *(generated)* |
| `posts_data.py`  | **The one file you edit** to add posts and set their dates |
| `build.py`       | Regenerates `thoughts.html` + `posts/` from `posts_data.py` |
| `CNAME`          | Your custom domain (`vahid-sb.com`) |
| `.nojekyll`      | Tells GitHub Pages to serve every file as-is |

---

## 1 — Put it online (GitHub Pages)

You already have the repository **`vahid-sb/vahid-sb.github.io`** — a GitHub *user site*,
which is the simplest kind. Use it.

1. Open <https://github.com/vahid-sb/vahid-sb.github.io>.
2. Upload **all** of these files into the repository root, keeping the `posts/` folder.
   - **Web browser:** *Add file → Upload files*, then drag everything in. To keep the
     `posts/` folder, drag the `posts` folder itself along with the loose files. Commit to `main`.
   - **Git (command line):** copy these files into your local clone, then
     `git add -A && git commit -m "New website" && git push`.
3. **Settings → Pages**: Source = *Deploy from a branch*, Branch = **main**, Folder = **/ (root)**, Save.
   (For a `username.github.io` repo this is usually already enabled.)
4. Within a minute or two the site is live at **https://vahid-sb.github.io** — open it and
   click around to confirm everything works *before* touching your domain.

---

## 2 — Point `vahid-sb.com` at it (moving off Adobe Portfolio)

Your domain currently resolves to Adobe Portfolio. Log in to wherever you manage the
domain's **DNS** and replace the existing records with these:

**Apex domain** (`@`, i.e. `vahid-sb.com`) — four `A` records:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**(Recommended) IPv6** — four `AAAA` records:

```
2606:50c0:8000::153
2606:50c0:8001::153
2606:50c0:8002::153
2606:50c0:8003::153
```

**`www` subdomain** — one `CNAME` record pointing to `vahid-sb.github.io`.

Delete the old Adobe Portfolio A/CNAME records. Then in GitHub, **Settings → Pages →
Custom domain**, enter `vahid-sb.com`, Save, and tick **Enforce HTTPS** once it becomes
available (the `CNAME` file in this repo already declares the domain).

DNS changes take anywhere from a few minutes to a day to propagate; GitHub then issues a
free HTTPS certificate automatically. The current GitHub Pages IP addresses are listed at
GitHub's docs page *"Managing a custom domain for your GitHub Pages site"* — they very
rarely change, but worth a glance.

---

## 3 — Add or edit a blog post

1. Open **`posts_data.py`**.
2. Copy an existing entry and change `slug`, `date` (`YYYY-MM-DD` — you decide it),
   `category`, `title`, and `body`. The **first paragraph** of the body is the teaser
   shown on the Thoughts page. New categories become filter buttons automatically.
3. Run:

   ```
   python3 build.py
   ```

4. Upload the updated `thoughts.html` and the new `posts/<slug>.html` (and `posts_data.py`).

The Thoughts page is **always sorted by date, newest first**, no matter what order the
entries sit in the file.

---

## 4 — Things to personalize (a few placeholders I left for you)

Open `index.html` and search for these to make them exactly right:

- **Current role** — the "Now · 2022 —" entry says *"Autonomous driving … · Germany"*.
  Add your real company/title/city if you want them shown.
- **Dates** — the years in the *Trajectory* section are my best estimates; adjust freely.
- **Citations** — the main page shows *"800+"*; edit or remove the number.

(Your email is **not** on the page anymore — the Contact section is a private form, see below.)

---

## 5 — Contact form setup (keeps your email private)

The Contact section is a form, not a visible email address. It sends messages through
**Formspree** (free), so visitors never see where the mail goes.

1. Go to **formspree.io**, create a free account.
2. Create a new form and set its destination to **whatever address you want messages sent
   to** (e.g. your Gmail). Formspree gives you an endpoint like `https://formspree.io/f/abcdwxyz`.
3. In `index.html`, find `https://formspree.io/f/YOUR_FORM_ID` and replace `YOUR_FORM_ID`
   with your form's id, then re-upload `index.html`.
4. Send yourself one test message — Formspree asks you to confirm the destination the first time.

Prefer not to make an account? **web3forms.com** does the same with just an access key —
tell me and I'll wire that version instead.

That's it. Tell me any of these and I can hand you an updated `index.html`.
