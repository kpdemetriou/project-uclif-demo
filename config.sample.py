from UCLIFAuth import UCLIFAuthScopes

APP_DEBUG = False

OAUTH2_CLIENT_ID = "YOUR-CLIENT-ID-HERE"
OAUTH2_CLIENT_SECRET = "YOUR-CLIENT-SECRET-HERE"
OAUTH2_REDIRECT_URI = "https://uclif-demo.philonas.net/info"
OAUTH2_SCOPE_TOKENS = [
    UCLIFAuthScopes.UUID,
    UCLIFAuthScopes.TARGETED_ID,
    UCLIFAuthScopes.USERNAME,
    UCLIFAuthScopes.SCOPED_USERNAME,
    UCLIFAuthScopes.EMAIL,
    UCLIFAuthScopes.TITLE,
    UCLIFAuthScopes.FIRST_NAME,
    UCLIFAuthScopes.LAST_NAME,
    UCLIFAuthScopes.FULL_NAME,
    UCLIFAuthScopes.DEPARTMENT,
    UCLIFAuthScopes.AFFILIATIONS,
    UCLIFAuthScopes.SCOPED_AFFILIATIONS,
    UCLIFAuthScopes.GROUPS,
]

HTTP_SERVER = "wsgiref"
HTTP_HOST = "127.0.0.1"
HTTP_PORT = 8080
