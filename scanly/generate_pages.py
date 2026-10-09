"""PageBeam(scanly) 공개 페이지 생성기: 9개 언어 × (소개, 개인정보, 약관, 지원, 계정 삭제) + 언어 선택 허브."""
from html import escape as esc
from pathlib import Path

from content_asia import JA, ZH_HANS, ZH_HANT
from content_eu import DE, ES, FR, PT
from content_ko_en import EMAIL, EN, KO

ROOT = Path(__file__).resolve().parent
SITE = "https://oh-seungjin.github.io/privacy-terms/scanly"
KINDS = ("index", "privacy", "terms", "support", "delete-account")
LANGUAGES = {"ko": KO, "en": EN, "ja": JA, "de": DE, "fr": FR, "es": ES, "pt-br": PT, "zh-hant": ZH_HANT, "zh-hans": ZH_HANS}


def nav(data, current):
    return "".join(f'<a href="{k}.html"' + (' aria-current="page"' if k == current else "") + f'>{esc(data["nav"][i])}</a>' for i, k in enumerate(KINDS))


def language_options(current, kind):
    return "".join(f'<option value="../{c}/{kind}.html"' + (" selected" if c == current else "") + f'>{esc(d["label"])}</option>' for c, d in LANGUAGES.items())


def alternates(kind):
    links = "\n".join(f'<link rel="alternate" hreflang="{d["html"]}" href="{SITE}/{c}/{kind}.html">' for c, d in LANGUAGES.items())
    return links + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}/en/{kind}.html">'


def page(code, kind, data):
    if kind == "index":
        title = "PageBeam"
        content = (f'<p class="muted">DOCUMENT · PDF · SCANNER</p><h1>{esc(data["tag"])}</h1><p class="lead">{esc(data["intro"])}</p><ul class="features">'
                   + "".join(f"<li>{esc(i)}</li>" for i in data["features"]) + f'</ul><p class="lead">{esc(data["offline"])}</p>')
    else:
        key = {"delete-account": "delete"}.get(kind, kind)
        title = data[f"{key}_title"]
        content = f'<h1>{esc(title)}</h1><p class="date">{esc(data["date"])}</p><p class="lead">{esc(data[f"{key}_intro"])}</p>'
        content += "".join(f"<section><h2>{i}. {esc(h)}</h2><p>{esc(t)}</p></section>" for i, (h, t) in enumerate(data[kind], 1))
        content += f'<aside class="contact"><h2>{esc(data["contact"])}</h2><p>Next Studio<br><a href="mailto:{EMAIL}?subject=PageBeam%20{kind}">{EMAIL}</a></p></aside>'
    return f'''<!doctype html>
<html lang="{data['html']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="PageBeam · {esc(title)} · Next Studio"><title>PageBeam · {esc(title)}</title>
<link rel="icon" href="../icon.png"><link rel="stylesheet" href="../style.css"><link rel="canonical" href="{SITE}/{code}/{kind}.html">
{alternates(kind)}</head><body><a class="skip" href="#content">{esc(data['skip'])}</a><main>
<header class="top"><a class="brand" href="index.html"><img src="../icon.png" alt="" width="34" height="34">PageBeam</a><label><span class="skip">{esc(data['choose'])}</span><select class="language" aria-label="{esc(data['choose'])}" onchange="location.href=this.value">{language_options(code, kind)}</select></label></header>
<nav aria-label="PageBeam">{nav(data, kind)}</nav><article id="content">{content}</article><footer>{esc(data['copyright'])}<br><a href="mailto:{EMAIL}">{EMAIL}</a></footer></main></body></html>'''


for locale, strings in LANGUAGES.items():
    dest = ROOT / locale
    dest.mkdir(exist_ok=True)
    for kind in KINDS:
        (dest / f"{kind}.html").write_text(page(locale, kind, strings), encoding="utf-8")

links = "".join(f'<a href="{c}/index.html" hreflang="{d["html"]}">{esc(d["label"])}</a>' for c, d in LANGUAGES.items())
(ROOT / "index.html").write_text(
    f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="PageBeam official website"><title>PageBeam · Next Studio</title><link rel="icon" href="icon.png"><link rel="stylesheet" href="style.css"></head><body><main><header class="top"><span class="brand"><img src="icon.png" alt="" width="34" height="34">PageBeam</span></header><article><p class="muted">DOCUMENT · PDF · SCANNER</p><h1>PageBeam</h1><p class="lead">Choose your language.</p><div class="cards">{links}</div></article><footer>© 2026 Next Studio</footer></main></body></html>''',
    encoding="utf-8")
print(f"Generated {len(LANGUAGES) * len(KINDS) + 1} pages.")
