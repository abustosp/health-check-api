# Health Check API

Script en Python para verificar endpoints HTTP de salud y enviar alertas por correo cuando alguno falla o es inalcanzable.

## Que hace
- Lee URLs desde `DOMAINS`.
- Hace un GET por URL con timeout configurable.
- Considera saludable solo un HTTP 200.
- Si hay fallos, envia un correo HTML a los receptores.

## Requisitos
- Python 3.12+
- Dependencia: `requests` (ver `requirements.txt`)
- Opcional: `python-dotenv` para cargar `.env`
- Acceso a un servidor SMTP

## Configuracion (variables de entorno)
- `DOMAINS`: URLs separadas por `|`, `;`, `,` o saltos de linea.
- `TIMEOUT_REQUEST`: segundos de espera por request (default: `30`).
- `RECEPTORES`: correos separados por `;`.
- `SMTP_SERVER`: host SMTP.
- `SMTP_PORT`: puerto SMTP (ej. `587`).
- `SMTP_USER`: usuario SMTP.
- `SMTP_PASSWORD`: password SMTP.
- `SMTP_FROM_EMAIL`: remitente.
- `TEMPLATE_PATH`: ruta al HTML de la plantilla (ej. `./utils/templates/mail.html`).

## Ejecutar en local
1. `cp .env.example .env` y completa los valores.
2. `pip install -r requirements.txt`
3. `python main.py`

Si queres cargar `.env` automaticamente:
```bash
pip install python-dotenv
```

## Ejecutar con Docker
```bash
docker compose up --build
```

`compose.yaml` carga `.env` y monta `./utils/templates` dentro del contenedor.

## Plantilla de correo
- Archivo por defecto: `utils/templates/mail.html`
- Placeholder requerido: `{{SERVICIOS}}`

## Ejemplo de `.env`
```env
DOMAINS=https://example.com/health|https://api.example.com/status
TIMEOUT_REQUEST=30
RECEPTORES=ops@example.com;devops@example.com
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
SMTP_USER=usuario
SMTP_PASSWORD=secreto
SMTP_FROM_EMAIL=monitor@example.com
TEMPLATE_PATH=./utils/templates/mail.html
```
