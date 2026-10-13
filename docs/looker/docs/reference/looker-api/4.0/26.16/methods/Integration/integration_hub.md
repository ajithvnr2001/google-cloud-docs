---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Integration/integration_hub/
title: Get Integration Hub \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:57.632306+00:00
---

# Get Integration Hub  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Integration/integration_hub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Get Integration Hub Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.16 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.18 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Get information about a Integration Hub.

## Request

GET /integration_hubs/{integration_hub_id} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

integration_hub_id

string 

Id of integration_hub

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields.

## Response

### 200: Integration Hub

Datatype

Description

(object)

[IntegrationHub](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/IntegrationHub)

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

ID of the hub.

url

string 

URL of the hub.

label

_lock_

string 

Label of the hub.

official

_lock_

boolean 

Whether this hub is a first-party integration hub operated by Looker.

fetch_error_message

_lock_

string 

An error message, present if the integration hub metadata could not be fetched. If this is present, the integration hub is unusable.

authorization_token

string 

(Write-Only) An authorization key that will be sent to the integration hub on every request.

has_authorization_token

_lock_

boolean 

Whether the authorization_token is set for the hub.

legal_agreement_signed

_lock_

boolean 

Whether the legal agreement message has been signed by the user. This only matters if legal_agreement_required is true.

legal_agreement_required

_lock_

boolean 

Whether the legal terms for the integration hub are required before use.

legal_agreement_text

_lock_

string 

The legal agreement text for this integration hub.

### 400: Bad Request

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

## Examples

### Kotlin

[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt#L356 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt")  
---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
