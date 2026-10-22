---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-authenticate/
title: Authenticate \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:15.124955+00:00
---

# Authenticate  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-authenticate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Authenticate Stay organized with collections  Save and categorize content based on your preferences. 

To authenticate with CCAI Platform, you must implement a token endpoint to generate a JSON web token as the response.

## Get company secret

**Warning:** It is imperative to store your `COMPANY_SECRET` securely on your server so the application can validate your identity. Without this precaution in place, it is possible for malicious entities to act on your behalf.

  1. Sign into the Contact Center AI Platform portal using an account with administrator permissions.

  2. Go to **Settings > Developer Settings**.

  3. Copy the Company Secret as `COMPANY_SECRET`.




## Token endpoint

The token endpoint must return a JWT containing the current user's information. The response is similar to the following:
    
    
    {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.n...."}
    

The token is created with:

  1. `alg` of `HS256`.

  2. `payload` must contain user identifier, name and email. Even if the user is an anonymous user and has not yet authenticated, the identifier is required in order for the SDK to work as expected.

  3. Sign the signature with `COMPANY_SECRET`



    
    
    header = {"alg": "HS256"}
    payload = {
      "iss": "{YOUR_COMPANY_NAME}",
      "iat": $unix_timestamp_now,
      "exp": $unix_timestamp_now + 3600,
      "identifier": "{CURRENT_USER_ID}",
      "name": "{CURRENT_USER_NAME}",
      "email": "{CURRENT_USER_EMAIL}",
    }
    
    token = jwt_encode(header, payload, COMPANY_SECRET)
    

## Examples

Here are some examples, we are using `/auth/token` as the endpoint.

### Express (Node.js)
    
    
    const express = require('express')
    const jwt = require('jsonwebtoken')
    
    const COMPANY_NAME = 'AMCE'
    const COMPANY_SECRET = '__read_from_config__'
    
    const app = express()
    app.use(express.json())
    app.use(your_session_middleware)
    
    app.get('/auth/token', function (req, res) {
      const now = parseInt(Date.now() / 1000, 10)
      const payload = {
        'iss': COMPANY_NAME,
        'iat': now,
        'exp': now + 3600,
      }
      if (req.user) {
        payload.identifier = req.user.id,
        payload.name = req.user.name
        payload.email = req.user.email
      }
      const token = jwt.sign(payload, COMPANY_SECRET, { algorithm: 'HS256' })
      res.json({ token })
    })
    

### Flask (Python)
    
    
    import time
    from flask import Flask, request
    from joserfc import jwt, jwk
    
    app = Flask(__name__)
    
    COMPANY_NAME = 'AMCE'
    COMPANY_SECRET = '__read_from_config__'
    secret_key = jwk.OctKey.import_key(COMPANY_SECRET)
    
    @app.route('/auth/token')
    def auth_token():
        now = int(time.time())
        payload = {
          'iss': COMPANY_NAME,
          'iat': now,
          'exp': now + 3600,
        }
        if (request.user) {
          payload.identifier = request.user.id,
          payload.name = request.user.name
          payload.email = request.user.email
        }
        token = jwt.encode({'alg': 'HS256'}, payload, secret_key)
        return {'token': token}
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
