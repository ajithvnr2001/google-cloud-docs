---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/create_embed_url_as_me/
title: Create Embed URL \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:10.202278+00:00
---

# Create Embed URL  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/create_embed_url_as_me/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Create Embed URL Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Create an Embed URL

Creates an embed URL that runs as the Looker user making this API call. ("Embed as me") This embed URL can then be used to instantiate a Looker embed session in a "Powered by Looker" (PBL) web application.

This is similar to Private Embedding (<https://docs.cloud.google.com/looker/docs/r/admin/embed/private-embed>). Instead of logging into the Web UI to authenticate, the user has already authenticated against the API to be able to make this call. However, unlike Private Embed where the user has access to any other part of the Looker UI, the embed web session created by requesting the EmbedUrlResponse.url in a browser only has access to content visible under the `/embed` context.

An embed URL can only be used once, and must be used within 5 minutes of being created. After it has been used to request a page from the Looker server, the URL is invalid. Future requests using the same URL will fail. This is to prevent 'replay attacks'.

The `target_url` property must be a complete URL of a Looker Embedded UI page - scheme, hostname, path starting with "/embed" and query params. To load a dashboard with id 56 and with a filter of `Date=1 years`, the looker Embed URL would look like `https://myname.looker.com/embed/dashboards/56?Date=1%20years`. The best way to obtain this target_url is to navigate to the desired Looker page in your web browser, copy the URL shown in the browser address bar, insert "/embed" after the host/port, and paste it into the `target_url` property as a quoted string value in this API request.

#### Security Note

Protect this signed URL as you would an access token or password credentials - do not write it to disk, do not pass it to a third party, and only pass it through a secure HTTPS encrypted transport.

## Request

POST /embed/token_url/me 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[EmbedParams](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/EmbedParams)

Embed parameters

Expand EmbedParams definition... 

target_url

string 

The complete URL of the Looker UI page to display in the embed context. For example, to display the dashboard with id 34, `target_url` would look like: `https://mycompany.looker.com:9999/dashboards/34`. `target_uri` MUST contain a scheme (HTTPS), domain name, and URL path. Port must be included if it is required to reach the Looker server from browser clients. If the Looker instance is behind a load balancer or other proxy, `target_uri` must be the public-facing domain name and port required to reach the Looker instance, not the actual internal network machine name of the Looker instance.

session_length

integer 

Number of seconds the signed embed session will be valid after the embed session is started. Defaults to 300 seconds. Maximum session length accepted is 2592000 seconds (30 days).

force_logout_login

boolean 

When true, the embed session will purge any residual Looker login state (such as in browser cookies) before creating a new login state with the given embed user info. Defaults to true.

## Response

### 200: Embed URL

Datatype

Description

(object)

[EmbedUrlResponse](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/EmbedUrlResponse)

url

_lock_

string 

The embed URL. Any modification to this string will make the URL unusable.

### 400: Bad Request

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 403: Permission Denied

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 404: Not Found

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 409: Resource Already Exists

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 422: Validation Error

Datatype

Description

(object)

[ValidationError](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ValidationError)

message

_lock_

string 

Error details

errors

[ValidationErrorDetail](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ValidationErrorDetail)[] 

Expand ValidationErrorDetail definition... 

field

_lock_

string 

Field with error

code

_lock_

string 

Error code

message

_lock_

string 

Error info message

documentation_url

_lock_

string 

Documentation link

documentation_url

_lock_

string 

Documentation link

### 429: Too Many Requests

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
