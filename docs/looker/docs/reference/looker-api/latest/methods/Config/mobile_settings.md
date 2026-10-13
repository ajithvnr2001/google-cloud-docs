---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/mobile_settings/
title: Get Mobile_Settings \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:28.922166+00:00
---

# Get Mobile_Settings  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/mobile_settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Get Mobile_Settings Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Get all mobile settings.

## Request

GET /mobile/settings 

Datatype

Description

Request

HTTP Request 

## Response

### 200: Mobile_Settings

Datatype

Description

(object)

[MobileSettings](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/MobileSettings)

mobile_force_authentication

_lock_

boolean 

Specifies whether the force authentication option is enabled for mobile

mobile_app_integration

_lock_

boolean 

Specifies whether mobile access for this instance is enabled.

mobile_feature_flags

[MobileFeatureFlags](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/MobileFeatureFlags)[] 

Expand MobileFeatureFlags definition... 

feature_flag_name

_lock_

string 

Specifies the name of feature flag.

feature_flag_state

_lock_

boolean 

Specifies the state of feature flag

enhanced_search_enabled

_lock_

boolean 

Specifies whether enhanced search is enabled on this instance.

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
