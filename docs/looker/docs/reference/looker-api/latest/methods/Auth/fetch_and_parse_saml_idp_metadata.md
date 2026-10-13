---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/fetch_and_parse_saml_idp_metadata/
title: Parse SAML IdP Url \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:19.249224+00:00
---

# Parse SAML IdP Url  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/fetch_and_parse_saml_idp_metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Parse SAML IdP Url Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Fetch the given url and parse it as a SAML IdP metadata document and return the result.

Note that this requires that the url be public or at least at a location where the Looker instance can fetch it without requiring any special authentication.

Calls to this endpoint may be denied by [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/r/looker-core/overview).

## Request

POST /fetch_and_parse_saml_idp_metadata 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

string 

SAML IdP metadata public url

## Response

### 200: Parse result

Datatype

Description

(object)

[SamlMetadataParseResult](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/SamlMetadataParseResult)

can

_lock_

object 

Operations the current user is able to perform on this object

idp_issuer

_lock_

string 

Identify Provider Issuer

idp_url

_lock_

string 

Identify Provider Url

idp_cert

_lock_

string 

Identify Provider Certificate

idp_cert_multi

_lock_

[SamlIdpCertMulti](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/SamlIdpCertMulti)

Identity Provider Multiple Certificates

Expand SamlIdpCertMulti definition... 

signing

string[] 

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
