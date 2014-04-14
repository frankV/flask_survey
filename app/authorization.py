#!/usr/bin/env python

import urllib
import argparse
import webbrowser
import time
import requests
import BaseHTTPServer
from config import SM_API_BASE, AUTH_CODE_ENDPOINT, ACCESS_TOKEN_ENDPOINT, REDIRECT_URI, HOST_NAME, PORT_NUMBER, api_key, client_id, client_secret

# Uses requests library: http://docs.python-requests.org/en/latest/

'''
OAuth 2.0 really needs to do three things.

1) Make a request for the OAuth Dialog form with client secret and redirect_uri.
2) After client has logged in / authorized the app, the redirect_uri is called
   with auth code or error - i.e. SurveyMonkey passes back control to a URL you
   own.
3) Finally the page redirected to must POST to /oauth/token to exchange the auth
   code for a long lived access token.

To run:

> cd ROOT_OF_PACKAGE
> pip install -r requirements.txt
> python ./guides/authorization.py CLIENT_ID CLIENT_SECRET API_KEY

This will launch an Oauth dialog in the default browser to allow the user to log
in to SurveyMonkey, and also launch a simple web server that will process one
request (which will be the redirection from the OAuth dialog).

When the user enters their credentials / authorizes the app, SurveyMonkey will
redirect to your local web server, which will then exchange the code it
receives for a long-lived access token.

***NOTE WELL*** - your redirect_uri on your Mashery application MUST be
                  http://127.0.0.1:8000 for this sample code to work.
'''



def oauth_dialog(client_id, redirect_uri, api_key):
    # Construct the oauth_dialog_url
    url_params = urllib.urlencode({
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'response_type': 'code',
        'api_key': api_key
    })
    auth_dialog_url = SM_API_BASE + AUTH_CODE_ENDPOINT + '?' + url_params

    print "\nThe auth dialog url was " + auth_dialog_url + "\n"
    webbrowser.open(auth_dialog_url,new=2)


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def print_message(s, message):
        s.wfile.write("<body><p>%s</p>" % message)
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>SurveyMonkey API - "
                      "OAuth Sample Redirect Page.</title></head>")

        from urlparse import urlparse, parse_qs
        # Step 2 Parse authorization token from redirect response
        authorization_code = parse_qs(urlparse(s.path).query).get('code', [])
        # parse_qs returns a list for every query param, just get the first one
        if len(authorization_code) > 0:
            authorization_code = authorization_code[0]
        else:
            authorization_code = None

        if authorization_code:
            # Step 3 - exchange your authorization code for a long lived access
            # token
            access_token = s.exchange_code_for_token(authorization_code,
                                                   api_key, client_id,
                                                   client_secret, REDIRECT_URI)
            if access_token:
                s.print_message('Your long lived access token is ' + \
                                access_token)
            else:
                s.print_message('Error getting authorization code')
        else:
            s.print_message('No Authorization Code was returned. '
                            'Were the username and password correct?')
        s.wfile.write("</body></html>")


    def exchange_code_for_token(s, auth_code, api_key, client_id, client_secret,
                                redirect_uri):
        data = {
            "client_secret": client_secret,
            "code": auth_code,
            "redirect_uri": redirect_uri,
            "client_id": client_id,
            "grant_type": "authorization_code"
        }

        access_token_uri = SM_API_BASE + ACCESS_TOKEN_ENDPOINT + '?api_key=' \
                           + api_key
        access_token_response = requests.post(access_token_uri, data=data)
        access_json = access_token_response.json()

        if 'access_token' in access_json:
            return access_json['access_token']
        else:
            s.print_message('Problems exchanging the auth code for your access'
                            ' token. Error message: %s' \
                            % access_json['error_description'])
            return None

# Bootstrap script to call into main
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Demo OAuth 2.0')

    parser.add_argument("client_id", help='Username from Mashery')
    parser.add_argument("client_secret", help='Secret from Mashery')
    parser.add_argument("api_key", help='API key for your app')
    args = parser.parse_args()

    client_id = args.client_id
    client_secret = args.client_secret
    api_key = args.api_key

    # Step 1 Load oauth dialog and take user input
    oauth_dialog(args.client_id, REDIRECT_URI, api_key)

    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    httpd.handle_request()
