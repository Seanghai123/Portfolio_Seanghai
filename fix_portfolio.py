"""Usage:  python fix_portfolio.py index.html
Creates index.fixed.html next to the original (original is untouched)."""
import re, sys

src = sys.argv[1] if len(sys.argv) > 1 else "index.html"
out = src.rsplit(".", 1)[0] + ".fixed.html"
html = open(src, encoding="utf-8").read()

def sub(label, pattern, repl, flags=0):
    global html
    html, n = re.subn(pattern, repl, html, flags=flags)
    print(f"{'OK  ' if n else 'MISS'} {label} ({n})")

# 1. Email (mailto link + visible text)
sub("email", r"hseang815@gmail\.com", "mr.seanghai.num123@gmail.com")

# 2. Spacing / typo fixes
sub("4th-year", r"4th-yearInformation", "4th-year Information")
sub("comma after strong", r"</strong>,a real", "</strong>, a real")
sub("team names", r"Touch Vengkorng,\s*Seang hai\s*,\s*Bun menghong",
    "Touch Vengkorng, Seang Hai, Bun Menghong")
sub("caption names", r"Uy Chakriya\s*,\s*Bun menghong", "Uy Chakriya, Bun Menghong")

# 3. Honest, specific headline
sub("headline",
    r"<h1>Full-Stack Developer \| Turning ideas into practical web applications\.</h1>",
    "<h1>Front-End Developer | Next.js · React · Tailwind CSS</h1>")

# 4. Shorter hero paragraph (2-3 sentences)
new_lede = ('<p class="lede">I\u2019m a 4th-year Information Technology student at the National '
            'University of Management. I built the login page for <strong>NUM-Digital-Scheduler</strong>, '
            'a class-scheduling system, and presented the staff dashboard of a '
            '<strong>Banking Management System</strong> in C# and SQL Server. '
            'Seeking an internship to grow as a full-stack developer.</p>')
sub("hero paragraph", r'<p class="lede\s*">.*?</p>', lambda m: new_lede, re.S)

# 5. Language level
sub("Khmer level", r"Khmer — Fluent", "Khmer — Native")

open(out, "w", encoding="utf-8").write(html)
print("Saved ->", out)