import os
from flask import Blueprint, render_template_string, send_from_directory

documentacion_bp = Blueprint('documentacion', __name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@documentacion_bp.route('/swagger.json')
def swagger_json():
    return send_from_directory(BASE_DIR, 'swagger.json')

@documentacion_bp.route('/')
@documentacion_bp.route('')
def swagger_ui():
    return render_template_string("""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>API ADSO 4089 - Documentación Swagger</title>
  <link rel="icon" type="image/png" href="/static/swagger-ui/favicon-32x32.png" sizes="32x32" />
  <link rel="stylesheet" href="/static/swagger-ui/swagger-ui.css" />
  <style>
    html {
      box-sizing: border-box;
      overflow: -moz-scrollbars-vertical;
      overflow-y: scroll;
    }
    *, *:before, *:after {
      box-sizing: inherit;
    }
    body {
      margin: 0;
      background: #fafafa;
    }
    .topbar {
      display: none;
    }
  </style>
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="/static/swagger-ui/swagger-ui-bundle.js"></script>
  <script src="/static/swagger-ui/swagger-ui-standalone-preset.js"></script>
  <script>
    window.onload = function() {
      const ui = SwaggerUIBundle({
        url: "/doc/swagger.json",
        dom_id: '#swagger-ui',
        deepLinking: true,
        presets: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIStandalonePreset
        ],
        plugins: [
          SwaggerUIBundle.plugins.DownloadUrl
        ],
        layout: "StandaloneLayout"
      });
      window.ui = ui;
    };
  </script>
</body>
</html>
""")