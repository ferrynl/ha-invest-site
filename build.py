from pathlib import Path
from html import escape

root = Path(__file__).parent / "dist"
repo = "https://github.com/ferrynl/ha-invest"
copy = {
"nl": {
"nav": ["Functies","Demo","Schermafbeeldingen","Installatie"],
"badge":"Gratis · Open source · Lokaal",
"title":"Jouw beleggingen.<br>Jouw data.",
"intro":"Volg je portefeuille, rendement en dividend over meerdere brokers vanuit Home Assistant. Home Invest is gratis en bewaart je gegevens op je eigen installatie.",
"demo":"Wissel van periode en zie hoe de waardegrafiek en het voorbeeldrendement veranderen. Alle cijfers in deze webdemo zijn fictief.",
"full":"De volledige app bevat een alleen-lezen demo met 10 brokers, 150 aandelen en 10 valuta’s. Open Mijn account → Profiel kiezen → Demo. Zonder account vind je de keuze in het taalvenster.",
"value":"Voorbeeldportefeuille","all":"Alles","source":"Broncode","docs":"Uitgebreide handleiding","screens":["Rapporten","Over Home Invest","Trading 212 importeren","Trade Republic importeren","Revolut importeren"],
"features":[("Dashboard","Bekijk posities per valuta, zoek en filter en vergelijk maximaal zes posities. Sleep modules naar je eigen indeling en kies per module de breedte en zichtbaarheid."),("Transacties en dividend","Volg aankopen, verkopen en netto dividend per brokeraccount. Beheerders kunnen transacties corrigeren met wijzigingshistorie en splitsingen en omzettingen verwerken."),("Importeren en exporteren","Importeer Trading 212 via CSV of API, of gebruik CSV-bestanden van Trade Republic en Revolut. Controleer het voorbeeld, koppel instrumenten en bekijk regels die aandacht vragen. Overlappende Trading 212-imports worden per rekening op bron-ID gecontroleerd."),("Rapporten en valuta","Bekijk rendement, dividend, kosten en belastingen. Bedragen blijven per valuta gescheiden en historische wisselkoersen ondersteunen omrekening."),("Beveiliging en herstel","Beheer gebruikers en rollen, meld je op ondersteunde HTTPS-omgevingen aan met passkeys en download of herstel lokale SQLite-back-ups. Bij herstel maakt de app eerst een veiligheidskopie."),("Home Assistant-sensoren","Toon de portefeuillewaarde per valuta en het totaal in euro op je Home Assistant-dashboard via optionele lokale REST-sensoren.")],
"privacy":"Je transacties en instellingen blijven in SQLite op je eigen installatie. Voor koersupdates en optionele brokerverbindingen gebruikt de app externe diensten. Koersen kunnen vertraagd of tijdelijk onbeschikbaar zijn.",
"steps":["Gebruik Home Assistant OS met Supervisor. Home Assistant Container heeft geen appwinkel.","Open Instellingen → Apps → App store → ⋮ → Repositories.","Voeg de onderstaande GitHub-repository toe.","Zoek Home Invest, installeer en start de app. De eerste build kan even duren.","Schakel Weergeven in zijbalk in, open Home Invest en kies je taal. Probeer de demo of maak bij Instellingen een brokeraccount aan."],
},
"en": {
"nav":["Features","Demo","Screenshots","Installation"],
"badge":"Free · Open source · Local",
"title":"Your investments.<br>Your data.",
"intro":"Track your portfolio, returns and dividends across brokers from Home Assistant. Home Invest is free and stores your data on your own installation.",
"demo":"Switch periods to see the value chart and example return change. All figures in this web demo are fictional.",
"full":"The full app includes a read-only demo with 10 brokers, 150 stocks and 10 currencies. Open My account → Choose profile → Demo. Without an account, use the language dialog.",
"value":"Example portfolio","all":"All","source":"Source code","docs":"Full documentation","screens":["Reports","About Home Invest","Importing Trading 212","Importing Trade Republic","Importing Revolut"],
"features":[("Dashboard","View positions by currency, search and filter, and compare up to six positions. Drag modules into place and choose their width and visibility."),("Transactions and dividends","Track buys, sales and net dividends per brokerage account. Admins can correct transactions with a change history and handle splits and conversions."),("Imports and exports","Import Trading 212 via CSV or API, or use CSV exports from Trade Republic and Revolut. Review a preview, match instruments and revisit rows that need attention. Overlapping Trading 212 imports are checked by source ID per account."),("Reports and currencies","Review returns, dividends, fees and taxes. Amounts are kept separate by currency and historical exchange rates support conversion."),("Security and recovery","Manage users and roles, sign in with passkeys on supported HTTPS setups, and download or restore local SQLite backups. The app creates a safety copy before restoring."),("Home Assistant sensors","Show portfolio value by currency and the euro total on your Home Assistant dashboard through optional local REST sensors.")],
"privacy":"Your transactions and settings stay in SQLite on your own installation. Price updates and optional broker connections use external services. Quotes may be delayed or temporarily unavailable.",
"steps":["Use Home Assistant OS with Supervisor. Home Assistant Container has no app store.","Open Settings → Apps → App store → ⋮ → Repositories.","Add the GitHub repository below.","Find Home Invest, install it and start the app. The first build can take a while.","Enable Show in sidebar, open Home Invest and choose your language. Explore the demo or add a brokerage account in Settings."],
},
"es": {
"nav":["Funciones","Demo","Capturas","Instalación"],
"badge":"Gratis · Código abierto · Local",
"title":"Tus inversiones.<br>Tus datos.",
"intro":"Sigue tu cartera, rentabilidad y dividendos de varios brókeres desde Home Assistant. Home Invest es gratis y guarda los datos en tu propia instalación.",
"demo":"Cambia el período para ver cómo varían el gráfico de valor y la rentabilidad de ejemplo. Todas las cifras de esta demo web son ficticias.",
"full":"La aplicación completa incluye una demo de solo lectura con 10 brókeres, 150 acciones y 10 divisas. Abre Mi cuenta → Elegir perfil → Demo. Sin cuenta, usa el selector de idioma.",
"value":"Cartera de ejemplo","all":"Todo","source":"Código fuente","docs":"Documentación completa","screens":["Informes","Acerca de Home Invest","Importación de Trading 212","Importación de Trade Republic","Importación de Revolut"],
"features":[("Panel","Consulta posiciones por divisa, busca, filtra y compara hasta seis posiciones. Arrastra los módulos y elige su anchura y visibilidad."),("Operaciones y dividendos","Sigue compras, ventas y dividendos netos por cuenta de bróker. Los administradores pueden corregir operaciones con historial y gestionar desdoblamientos y conversiones."),("Importación y exportación","Importa Trading 212 mediante CSV o API, o usa CSV de Trade Republic y Revolut. Revisa la vista previa, vincula instrumentos y consulta las filas pendientes. Trading 212 comprueba los identificadores de origen por cuenta en las importaciones solapadas."),("Informes y divisas","Consulta rentabilidad, dividendos, comisiones e impuestos. Los importes se separan por divisa y los tipos de cambio históricos permiten convertirlos."),("Seguridad y recuperación","Gestiona usuarios y roles, accede con llaves de acceso en entornos HTTPS compatibles y descarga o restaura copias locales de SQLite. La aplicación crea una copia de seguridad antes de restaurar."),("Sensores de Home Assistant","Muestra el valor por divisa y el total en euros en el panel de Home Assistant mediante sensores REST locales opcionales.")],
"privacy":"Tus operaciones y ajustes se guardan en SQLite en tu propia instalación. Las cotizaciones y conexiones opcionales con brókeres usan servicios externos. Las cotizaciones pueden llegar con retraso o no estar disponibles temporalmente.",
"steps":["Usa Home Assistant OS con Supervisor. Home Assistant Container no tiene tienda de aplicaciones.","Abre Ajustes → Aplicaciones → Tienda de aplicaciones → ⋮ → Repositorios.","Añade el repositorio de GitHub que aparece abajo.","Busca Home Invest, instala e inicia la aplicación. La primera compilación puede tardar.","Activa Mostrar en la barra lateral, abre Home Invest y elige el idioma. Prueba la demo o crea una cuenta de bróker en Ajustes."],
}}
files = ["rapporten-preview.png","over-ons-preview.png","trading212-upload.png","traderepublic-upload.png","revolut-upload.png"]
ids = ["features","demo","screens","install"]
pages = {"nl":"index.html","en":"en.html","es":"es.html"}

for lang, t in copy.items():
    f, d, s, i = t["nav"]
    nav = "".join(f'<a href="{key}-{lang}.html">{label}</a>' for key, label in zip(ids, t["nav"]))
    languages = " · ".join(f'<a href="{page}" data-language="{key}" hreflang="{key}" lang="{key}"{" aria-current=page" if key == lang else ""}>{key.upper()}</a>' for key, page in pages.items())
    features = "".join(f'<article class="card"><h3>{name}</h3><p>{desc}</p></article>' for name, desc in t["features"])
    screenshots = "".join(f'<figure><a href="assets/{file}"><img loading="lazy" src="assets/{file}" alt="{escape(caption)}"></a><figcaption>{caption}</figcaption></figure>' for file, caption in zip(files, t["screens"]))
    steps = "".join(f'<li>{step}</li>' for step in t["steps"])
    page = f"""<!doctype html>
<html lang="{lang}"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Home Invest · {t['badge']}</title><meta name="description" content="{escape(t['intro'])}">
<link rel="stylesheet" href="assets/site.css"><script src="assets/demo.js" defer></script>
<header><a class="brand" href="{pages[lang]}"><span>◈</span> Home Invest</a><nav>{nav}</nav><div>{languages}</div></header>
<main><section class="hero"><p class="eyebrow">{t['badge']}</p><h1>{t['title']}</h1><p>{t['intro']}</p><div class="actions"><a class="button" href="install-{lang}.html">{i} →</a><a href="demo-{lang}.html">{d} ↗</a></div></section>
<section id="demo"><p class="eyebrow">01 / {d}</p><h2>{t['value']}</h2><div class="demo">
<div class="card"><div aria-live="polite"><div id="value" class="metric">€ 24.860</div><p id="change">+2,1%</p></div>
<svg class="chart" viewBox="0 0 300 125" role="img" aria-label="{t['value']}"><path d="M0 87 L32 80 62 85 93 62 128 65 163 41 195 45 229 29 260 37 300 15"/></svg>
<div class="actions"><button type="button" data-period="1M" aria-pressed="true">1M</button><button type="button" data-period="1Y" aria-pressed="false">12M</button><button type="button" data-period="ALL" aria-pressed="false">{t['all']}</button></div></div>
<div class="card"><p>{t['demo']}</p><p>{t['full']}</p></div></div></section>
<section id="features"><p class="eyebrow">02 / Home Invest</p><h2>{f}</h2><p>{t['privacy']}</p><div class="grid">{features}</div></section>
<section id="screens"><p class="eyebrow">03 / Home Invest</p><h2>{s}</h2><div class="grid">{screenshots}</div></section>
<section id="install"><p class="eyebrow">04 / Home Assistant</p><h2>{i}</h2><div class="card"><ol>{steps}</ol><p><code>{repo}</code></p><div class="actions"><a class="button" href="{repo}">{t['source']}</a><a href="{repo}/blob/main/portfolio/DOCS.md">{t['docs']}</a></div></div></section></main>
<footer><strong>Home Invest</strong><p>{t['badge']}</p><nav>{nav}</nav></footer></html>
"""
    import re

    sections = dict(re.findall(r'<section id="([^"]+)">(.*?)</section>', page, re.S))
    hero = page.split("<main>", 1)[1].split("</section>", 1)[0] + "</section>"
    tiles = "".join(
        f'<a class="card tile" href="{key}-{lang}.html"><span class="eyebrow">0{index}</span><h3>{label} <span>↗</span></h3></a>'
        for index, (key, label) in enumerate(zip(ids, t["nav"]), 1)
    )
    preview = f'<a class="showcase" href="screens-{lang}.html"><img src="assets/rapporten-preview.png" alt="{t["screens"][0]}"></a>'
    landing = hero + preview + f'<section class="grid overview">{tiles}</section>'
    head, body = page.split("<main>", 1)
    footer = body.split("</main>", 1)[1]
    (root / pages[lang]).write_text(head + "<main>" + landing + "</main>" + footer, encoding="utf-8")
    for key, label in zip(ids, t["nav"]):
        detail_head = head.replace(f"<title>Home Invest · {t['badge']}</title>", f"<title>{label} · Home Invest</title>")
        for target in pages:
            detail_head = detail_head.replace(
                f'href="{pages[target]}" data-language="{target}"',
                f'href="{key}-{target}.html" data-language="{target}"',
            )
        detail_head = detail_head.replace(f'href="{key}-{lang}.html">{label}', f'href="{key}-{lang}.html" aria-current="page">{label}')
        content = f'<section class="detail" id="{key}">{sections[key].replace("<h2>", "<h1>", 1).replace("</h2>", "</h1>", 1)}</section>'
        (root / f"{key}-{lang}.html").write_text(detail_head + "<main>" + content + "</main>" + footer, encoding="utf-8")

