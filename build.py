import re
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
"full":"De volledige app bevat een alleen-lezen demo met 10 brokers, 150 aandelen en 10 valuta’s. Open Mijn account → Profiel kiezen → Demo. Zonder account vind je de keuze in het taalvenster.",
"source":"Broncode","docs":"Uitgebreide handleiding","screens":["Rapporten","Over Home Invest","Trading 212 importeren","Trade Republic importeren","Revolut importeren"],
"features":[("Dashboard","Bekijk posities per valuta, zoek en filter en vergelijk maximaal zes posities. Sleep modules naar je eigen indeling en kies per module de breedte en zichtbaarheid."),("Transacties en dividend","Volg aankopen, verkopen en netto dividend per brokeraccount. Beheerders kunnen transacties corrigeren met wijzigingshistorie en splitsingen en omzettingen verwerken."),("Importeren en exporteren","Importeer Trading 212 via CSV of API, of gebruik CSV-bestanden van Trade Republic en Revolut. Controleer het voorbeeld, koppel instrumenten en bekijk regels die aandacht vragen. Overlappende Trading 212-imports worden per rekening op bron-ID gecontroleerd."),("Rapporten en valuta","Bekijk rendement, dividend, kosten en belastingen. Bedragen blijven per valuta gescheiden en historische wisselkoersen ondersteunen omrekening."),("Beveiliging en herstel","Beheer gebruikers en rollen, meld je op ondersteunde HTTPS-omgevingen aan met passkeys en download of herstel lokale SQLite-back-ups. Bij herstel maakt de app eerst een veiligheidskopie."),("Home Assistant-sensoren","Toon de portefeuillewaarde per valuta en het totaal in euro op je Home Assistant-dashboard via optionele lokale REST-sensoren.")],
"privacy":"Je transacties en instellingen blijven in SQLite op je eigen installatie. Voor koersupdates en optionele brokerverbindingen gebruikt de app externe diensten. Koersen kunnen vertraagd of tijdelijk onbeschikbaar zijn.",
"steps":["Gebruik Home Assistant OS met Supervisor. Home Assistant Container heeft geen appwinkel.","Open Instellingen → Apps → App store → ⋮ → Repositories.","Voeg de onderstaande GitHub-repository toe.","Zoek Home Invest, installeer en start de app. De eerste build kan even duren.","Schakel Weergeven in zijbalk in, open Home Invest en kies je taal. Probeer de demo of maak bij Instellingen een brokeraccount aan."],
},
"en": {
"nav":["Features","Demo","Screenshots","Installation"],
"badge":"Free · Open source · Local",
"title":"Your investments.<br>Your data.",
"intro":"Track your portfolio, returns and dividends across brokers from Home Assistant. Home Invest is free and stores your data on your own installation.",
"full":"The full app includes a read-only demo with 10 brokers, 150 stocks and 10 currencies. Open My account → Choose profile → Demo. Without an account, use the language dialog.",
"source":"Source code","docs":"Full documentation","screens":["Reports","About Home Invest","Importing Trading 212","Importing Trade Republic","Importing Revolut"],
"features":[("Dashboard","View positions by currency, search and filter, and compare up to six positions. Drag modules into place and choose their width and visibility."),("Transactions and dividends","Track buys, sales and net dividends per brokerage account. Admins can correct transactions with a change history and handle splits and conversions."),("Imports and exports","Import Trading 212 via CSV or API, or use CSV exports from Trade Republic and Revolut. Review a preview, match instruments and revisit rows that need attention. Overlapping Trading 212 imports are checked by source ID per account."),("Reports and currencies","Review returns, dividends, fees and taxes. Amounts are kept separate by currency and historical exchange rates support conversion."),("Security and recovery","Manage users and roles, sign in with passkeys on supported HTTPS setups, and download or restore local SQLite backups. The app creates a safety copy before restoring."),("Home Assistant sensors","Show portfolio value by currency and the euro total on your Home Assistant dashboard through optional local REST sensors.")],
"privacy":"Your transactions and settings stay in SQLite on your own installation. Price updates and optional broker connections use external services. Quotes may be delayed or temporarily unavailable.",
"steps":["Use Home Assistant OS with Supervisor. Home Assistant Container has no app store.","Open Settings → Apps → App store → ⋮ → Repositories.","Add the GitHub repository below.","Find Home Invest, install it and start the app. The first build can take a while.","Enable Show in sidebar, open Home Invest and choose your language. Explore the demo or add a brokerage account in Settings."],
},
"es": {
"nav":["Funciones","Demo","Capturas","Instalación"],
"badge":"Gratis · Código abierto · Local",
"title":"Tus inversiones.<br>Tus datos.",
"intro":"Sigue tu cartera, rentabilidad y dividendos de varios brókeres desde Home Assistant. Home Invest es gratis y guarda los datos en tu propia instalación.",
"full":"La aplicación completa incluye una demo de solo lectura con 10 brókeres, 150 acciones y 10 divisas. Abre Mi cuenta → Elegir perfil → Demo. Sin cuenta, usa el selector de idioma.",
"source":"Código fuente","docs":"Documentación completa","screens":["Informes","Acerca de Home Invest","Importación de Trading 212","Importación de Trade Republic","Importación de Revolut"],
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
<link rel="stylesheet" href="assets/site.css">
<header><a class="brand" href="{pages[lang]}"><span>◈</span> Home Invest</a><nav>{nav}</nav><div>{languages}</div></header>
<main><section class="hero"><p class="eyebrow">{t['badge']}</p><h1>{t['title']}</h1><p>{t['intro']}</p><div class="actions"><a class="button" href="install-{lang}.html">{i} →</a><a href="demo-{lang}.html">{d} ↗</a></div></section>
<section id="demo"></section>
<section id="features"><p class="eyebrow">02 / Home Invest</p><h2>{f}</h2><p>{t['privacy']}</p><div class="grid">{features}</div></section>
<section id="screens"><p class="eyebrow">03 / Home Invest</p><h2>{s}</h2><div class="grid">{screenshots}</div></section>
<section id="install"><p class="eyebrow">04 / Home Assistant</p><h2>{i}</h2><div class="card"><ol>{steps}</ol><p><code>{repo}</code></p><div class="actions"><a class="button" href="{repo}">{t['source']}</a><a href="{repo}/blob/main/portfolio/DOCS.md">{t['docs']}</a></div></div></section></main>
<footer><strong>Home Invest</strong><p>{t['badge']}</p><nav>{nav}</nav></footer></html>
"""


    sections = dict(re.findall(r'<section id="([^"]+)">(.*?)</section>', page, re.S))
    hero = page.split("<main>", 1)[1].split("</section>", 1)[0] + "</section>"
    tiles = "".join(
        f'<a class="card tile" href="{key}-{lang}.html"><span class="eyebrow">0{index}</span><h3>{label} <span>↗</span></h3></a>'
        for index, (key, label) in enumerate(zip(ids, t["nav"]), 1)
    )
    tour = {
        "nl": ("Open de live demo", "Probeer de echte app", "Klik door dezelfde schermen die je na installatie krijgt. Filter je portefeuille op broker, vergelijk posities en bekijk rendement en dividend in de rapporten.", "De openbare demo gebruikt een fictieve portefeuille en is alleen-lezen. Je hebt geen account of brokerbestand nodig.", ["Wissel van broker of valuta op het dashboard.", "Open Aandelen en bekijk het koersverloop van een positie.", "Ga naar Rapporten en wissel tussen rendement, kosten en dividend."]),
        "en": ("Launch the live demo", "Try the full app", "Explore the same screens you get after installation. Filter the portfolio by broker, compare positions and review performance and dividends in Reports.", "The public demo uses a fictional portfolio and is read-only. You can start without an account or broker file.", ["Switch brokers or currencies on the dashboard.", "Open Stocks and inspect the price history of a position.", "Go to Reports and explore returns, fees and dividends."]),
        "es": ("Abrir la demo en vivo", "Prueba la aplicación real", "Explora las mismas pantallas que tendrás tras instalarla. Filtra la cartera por bróker, compara posiciones y consulta rentabilidad y dividendos en Informes.", "La demo pública usa una cartera ficticia y es de solo lectura. Puedes empezar sin cuenta ni archivos del bróker.", ["Cambia de bróker o divisa en el panel.", "Abre Acciones y consulta el historial de una posición.", "En Informes, explora la rentabilidad, las comisiones y los dividendos."]),
    }
    launch, title, intro, notice, tasks = tour[lang]
    demo_url = "/app/?profile=demo#home"
    instructions = "".join(f"<li>{task}</li>" for task in tasks)
    sections["demo"] = f'<p class="eyebrow">LIVE / HOME INVEST</p><h2>{title}</h2><p>{intro}</p><p>{notice}</p><a class="button" href="{demo_url}">{launch} ↗</a><div class="card walkthrough"><ol>{instructions}</ol><p>{t["full"]}</p></div>'
    hero = hero.replace(f'{d} ↗', f'{launch} ↗').replace(f'href="demo-{lang}.html"', f'href="{demo_url}"')
    hero = hero.replace("</section>", '<div class="hero-line" aria-hidden="true"><svg viewBox="0 0 500 110"><path d="M0 99 L50 94 L93 99 L136 70 L179 77 L224 55 L273 64 L321 35 L370 43 L423 19 L470 25 L500 4"/></svg></div></section>')
    preview = f'<a class="showcase" href="screens-{lang}.html"><img src="assets/rapporten-preview.png" alt="{t["screens"][0]}"></a>'
    journey = {
        "nl": ("Van brokerbestand naar portefeuilleoverzicht", [("01", "Importeer je historie", "Maak per broker een rekening aan. Bekijk het importvoorbeeld en controleer instrumenten en kosten voordat je de boekingen opslaat."), ("02", "Onderzoek je posities", "Filter het dashboard op broker en valuta. Open een aandeel om koershistorie en gebeurtenissen per positie te zien."), ("03", "Volg je resultaat", "Bekijk rendement, ontvangen dividend, kosten en belastingen in de rapporten. Bewaar een lokale back-up voor herstel.")]),
        "en": ("From broker export to portfolio overview", [("01", "Import your history", "Create an account for each broker. Review the import preview and check instruments and fees before saving transactions."), ("02", "Explore your positions", "Filter the dashboard by broker and currency. Open a stock to inspect its price history and transactions."), ("03", "Track your results", "Review performance, dividends received, fees and taxes in Reports. Keep a local backup for recovery.")]),
        "es": ("De la exportación del bróker al resumen de cartera", [("01", "Importa tu historial", "Crea una cuenta por bróker. Revisa la vista previa y comprueba los instrumentos y comisiones antes de guardar las operaciones."), ("02", "Explora tus posiciones", "Filtra el panel por bróker y divisa. Abre una acción para ver su historial de precios y sus operaciones."), ("03", "Sigue tus resultados", "Consulta rentabilidad, dividendos recibidos, comisiones e impuestos en Informes. Guarda una copia local para poder restaurarla.")]),
    }
    journey_title, journey_steps = journey[lang]
    journey_cards = "".join(f'<article class="card"><span class="eyebrow">{number}</span><h3>{heading}</h3><p>{description}</p></article>' for number, heading, description in journey_steps)
    workflow = f'<div class="workflow"><h2>{journey_title}</h2><div class="grid">{journey_cards}</div></div>'
    sections["features"] += workflow
    landing = hero + preview + workflow + f'<section class="grid overview">{tiles}</section><section class="home-details"><h2>{f}</h2><p>{t["privacy"]}</p><div class="grid">{features}</div></section>'
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
