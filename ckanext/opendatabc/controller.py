import ckan.lib.base as base
import ckan.plugins.toolkit as toolkit
from email.mime.text import MIMEText
from email.mime.message import MIMEMessage
from email.MIMEMultipart import MIMEMultipart

import ckan.lib.helpers as h
import gnupg
import smtplib
import stripe

class MembershipController(base.BaseController):

    def signup(self):

        if toolkit.request.method == 'POST':
	    
	    # Replace this with your api key
	    stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"
	    token = toolkit.request.POST['stripeToken']
	    
	    try:
                gpg = gnupg.GPG( options=["--batch"])
                charge = stripe.Charge.create(
                amount=1000,
                currency="cad",
                card=token,
                description="payinguser@example.com",
                )
                message = MIMEMultipart()
                message['Subject'] = "OpenDataBc Membership"
                message['From'] = "opendatabc@opengovgear.com"
                message['To'] = "membership@opendatabc.ca"

                msg = []
                s = smtplib.SMTP('localhost')
                for key, value in toolkit.request.POST.items():
                    if not key.startswith('stripe'):
                        msg.append(key + ": " + value + "\n")
                keys = gpg.list_keys()
                string_msg = "".join(msg)
                string_msg.encode('utf-8')
                encrypted_msg = gpg.encrypt(string_msg, keys[-2]['fingerprint'], always_trust="True")
                body = MIMEText(str(encrypted_msg), 'plain','utf-8')
                message.attach(body)
                s.sendmail("ubuntu@app", "membership@opendatabc.ca", message.as_string())
                s.quit()
                h.flash_notice('Your application has been recieved.')
            except stripe.error.CardError, e:
                h.flash_notice('Card Error.')
            except stripe.error.InvalidRequestError, e:
                h.flash_notice('Your request is invalid. Please contact the site admins.')
            except stripe.error.AuthenticationError, e:
                h.flash_notice('Cannot Connect to Stripe Servers.')
            except stripe.error.APIConnectionError, e:
                h.flash_notice('There has been an error connecting to Stripe Servers.')
            except stripe.error.StripeError, e:
                h.flash_notice('Cannot Connect to Stripe Servers.')
            except Exception, e:
                h.flash_notice('There has been an error. Please contact the site admins.')
        return base.render('membership/membership_form.html')
