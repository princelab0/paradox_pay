from django.conf import settings

class PayPalSettingsError(Exception):
    """Raised when settings be bad."""
    

TEST = getattr(settings, "PAYPAL_TEST", True)


RECEIVER_EMAIL = 'abch@ontreat.com'


# API Endpoints.
POSTBACK_ENDPOINT = "https://esewa.com.np/epay/main"
SANDBOX_POSTBACK_ENDPOINT = "http://dev.esewa.com.np/epay/main"

# Images
IMAGE = getattr(settings, "eSewa_IMAGE", "/static/images/btn_buynowCC_LG.gif")
SUBSCRIPTION_IMAGE = "/static/images/btn_buynowCC_LG.gif"
SANDBOX_IMAGE = getattr(settings, "eSewa_SANDBOX_IMAGE", "/static/images/btn_buynowCC_LG.gif")
SUBSCRIPTION_SANDBOX_IMAGE = "/static/images/btn_buynowCC_LG.gif"