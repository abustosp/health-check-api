# Health Check API

Script en Python para verificar endpoints de salud y notificar por correo si alguno falla.

## Que hace
- Lee una lista de URLs desde variables de entorno.
- Hace un GET a cada URL con timeout configurable.
- Considera saludable solo un HTTP 200.
- Si hay fallos, envia un correo HTML a una lista de receptores.

## Requisitos
- Python 3.12+
- Dependencias: `requests` (ver `requirements.txt`)
- Opcional: `python-dotenv` si quieres cargar un archivo `.env` en local

## Configuracion (variables de entorno)
- `DOMAINS`: lista de URLs separadas por `|`, `;`, `,` o saltos de linea.
- `TIMEOUT_REQUEST`: segundos de espera por request (default: `30`).
- `RECEPTORES`: correos separados por `;`.
- `SMTP_SERVER`: host SMTP.
- `SMTP_PORT`: puerto SMTP (ej. `587`).
- `SMTP_USER`: usuario SMTP.
- `SMTP_PASSWORD`: password SMTP.
- `SMTP_FROM_EMAIL`: remitente.
- `TEMPLATE_PATH`: ruta al HTML de la plantilla.

## Ejecutar en local
```bash
pip install -r requirements.txt
python main.py
```

Si usas `.env` en local, instala `python-dotenv`:
```bash
pip install python-dotenv
```

## Ejecutar con Docker Compose
```bash
docker compose up --build
```

El `compose.yaml` carga un `.env` y monta `./utils/templates` dentro del contenedor.

## Plantilla de correo
- Plantilla por defecto: `utils/templates/mail.html`
- Usa el placeholder `{{SERVICIOS}}` para inyectar la lista de fallos.

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
TEMPLATE_PATH=/app/utils/templates/mail.html
```

Para ejecucion local puedes usar `TEMPLATE_PATH=./utils/templates/mail.html`.
