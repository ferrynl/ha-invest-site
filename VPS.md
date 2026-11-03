# Home Invest-website uitrollen in Coolify

1. Pak het ZIP-bestand uit in de hoofdmap van een Git-repository die Coolify kan lezen. Commit en push de Dockerfile, .dockerignore, demo_server.py en de volledige map dist.
2. Kies in het gewenste Coolify-project **New Resource** en verbind de Git-repository en branch.
3. Kies **Dockerfile** als build pack. Stel **Base Directory** in op / en **Dockerfile Location** op /Dockerfile.
4. Stel **Ports Exposes** in op 80. Vul bij **Domains** het gewenste HTTPS-domein in en laat het domein via DNS naar de VPS wijzen.
5. Klik op **Deploy**. Controleer de uitrollog, open het domein en test de taalkiezer en demo.

Coolify bouwt één container met de drie taalversies en de echte Home Invest-demo. De container controleert regelmatig of de homepage bereikbaar is. De demo maakt zelf een tijdelijke SQLite-database aan. Je hoeft geen volumes of omgevingsvariabelen in te stellen. De installatiehandleiding voor de Home Assistant-app staat op de website zelf.

[Officiële Coolify-documentatie voor Dockerfile-uitrol](https://coolify.io/docs/applications/builds/dockerfile)

## Demo na een update controleren

Open /demo-nl.html en kies **Open de live demo**. Onder /app/ draait de echte Home Invest-interface met een vooraf gevulde, fictieve portefeuille. De container haalt tijdens het bouwen een vastgelegde commit van de openbare app-repository op. De demo heeft eigen tijdelijke opslag en blokkeert schrijfacties. De Coolify-poort blijft 80.
