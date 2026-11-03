# Home Invest-website uitrollen in Coolify

1. Pak het ZIP-bestand uit in de hoofdmap van een Git-repository die Coolify kan lezen. Commit en push de Dockerfile, .dockerignore en de volledige map dist.
2. Kies in het gewenste Coolify-project **New Resource** en verbind de Git-repository en branch.
3. Kies **Dockerfile** als build pack. Stel **Base Directory** in op / en **Dockerfile Location** op /Dockerfile.
4. Stel **Ports Exposes** in op 80. Vul bij **Domains** het gewenste HTTPS-domein in en laat het domein via DNS naar de VPS wijzen.
5. Klik op **Deploy**. Controleer de uitrollog, open het domein en test de taalkiezer en demo.

Coolify bouwt een Nginx-container met de drie taalversies. De container controleert regelmatig of de homepage bereikbaar is. De website gebruikt geen database, volumes of omgevingsvariabelen. De installatiehandleiding voor de Home Assistant-app staat op de website zelf.

[Officiële Coolify-documentatie voor Dockerfile-uitrol](https://coolify.io/docs/applications/builds/dockerfile)
