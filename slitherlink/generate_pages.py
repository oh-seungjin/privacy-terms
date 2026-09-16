"""Generate static, full-text policy pages in the repository's 8 languages."""
import json
from html import escape as esc
from pathlib import Path
BASE=Path(__file__).resolve().parent
DATA=json.loads((BASE/'translations.json').read_text(encoding='utf8'))
LANGS=[('ko','한국어'),('en','English'),('ja','日本語'),('zh-hans','简体中文'),('es','Español'),('fr','Français'),('de','Deutsch'),('pt-br','Português (Brasil)')]
KINDS=['index','privacy','terms','support','delete-account']
ROOT='https://oh-seungjin.github.io/privacy-terms/slitherlink/'

def filename(kind,lang):return kind+('' if lang=='ko' else '-'+lang)+'.html'
def rich(text):return esc(text).replace('dhalska2@gmail.com','<a href="mailto:dhalska2@gmail.com">dhalska2@gmail.com</a>')
for lang,label in LANGS:
    d=DATA[lang];html_lang={'zh-hans':'zh-Hans','pt-br':'pt-BR'}.get(lang,lang)
    for kind in KINDS:
        title=d['nav'][KINDS.index(kind)]
        alternatives='\n'.join(f'<link rel="alternate" hreflang="{l}" href="{ROOT}{filename(kind,l)}">' for l,_ in LANGS)
        nav=''.join(f'<a href="{filename(k,lang)}"'+(' aria-current="page"' if k==kind else '')+f'>{esc(d["nav"][i])}</a>' for i,k in enumerate(KINDS))
        languages=''.join(f'<a href="{filename(kind,l)}" lang="{l}" hreflang="{l}"'+(' aria-current="page"' if l==lang else '')+f'>{name}</a>' for l,name in LANGS)
        options=''.join(f'<option value="{filename(kind,l)}"'+(' selected' if l==lang else '')+f'>{name}</option>' for l,name in LANGS)
        if kind=='index':
            body=f'<p class="eyebrow">SLITHERLINK</p><h1>{esc(d["tag"])}</h1><p class="lead">{esc(d["intro"])}</p><div class="cards">'+''.join(f'<a class="card" href="{filename(k,lang)}"><strong>{esc(d["nav"][i])}</strong><span aria-hidden="true">↗</span></a>' for i,k in enumerate(KINDS) if i)+ '</div>'
        else:
            body=f'<h1>{esc(title)}</h1><p class="date">{esc(d["date"])}</p>'
            body+='\n'.join(f'<section><h2>{i+1}. {esc(h)}</h2><p>{rich(p)}</p></section>' for i,(h,p) in enumerate(d[kind]))
        if kind=='privacy':
            body+='<aside><p><a href="https://www.apple.com/legal/privacy/">Apple Privacy</a> · <a href="https://policies.google.com/privacy">Google Privacy</a> · <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub Privacy</a> · <a href="https://supabase.com/privacy">Supabase Privacy</a></p></aside>'
        if kind=='terms':body+='<p><a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Apple Standard EULA</a></p>'
        subject='Slitherlink%20Data%20Deletion' if kind=='delete-account' else 'Slitherlink%20Support'
        body+=f'<aside><h2>{esc(d["contact"])}</h2><p>Next Studio · 넥스트 스튜디오<br><a href="mailto:dhalska2@gmail.com?subject={subject}">dhalska2@gmail.com</a></p></aside>'
        page=f'''<!doctype html>
<html lang="{html_lang}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Slitherlink · {esc(title)} · Next Studio">
<title>Slitherlink · {esc(title)}</title>
<link rel="stylesheet" href="style.css"><link rel="icon" href="icon.png">
<link rel="canonical" href="{ROOT}{filename(kind,lang)}">
{alternatives}
<link rel="alternate" hreflang="x-default" href="{ROOT}{filename(kind,'en')}">
</head>
<body><a class="skip" href="#content">{esc(d['skip'])}</a>
<main><div class="top"><a class="brand" href="{filename('index',lang)}"><img src="icon.png" width="40" height="40" alt=""> SLITHERLINK</a><label><span class="sr-only">Language</span><select class="language" aria-label="Language" onchange="location.href=this.value">{options}</select></label></div>
<nav aria-label="{esc(title)}">{nav}</nav>
<noscript><div class="languages" aria-label="Language">{languages}</div></noscript>
<article id="content">{body}</article>
<footer>© 2026 Next Studio · 넥스트 스튜디오<br><a href="mailto:dhalska2@gmail.com">dhalska2@gmail.com</a></footer></main></body></html>
'''
        (BASE/filename(kind,lang)).write_text(page,encoding='utf8')
print('Generated 40 static pages in 8 languages.')
