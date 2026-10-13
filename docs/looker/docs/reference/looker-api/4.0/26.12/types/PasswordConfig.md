---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/PasswordConfig/
title: PasswordConfig \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:49.246150+00:00
---

# PasswordConfig  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/PasswordConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  PasswordConfig Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.12 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

Datatype

Description

(object)

object 

can

_lock_

object 

Operations the current user is able to perform on this object

min_length

integer 

Minimum number of characters required for a new password. Must be between 7 and 100

require_numeric

boolean 

Require at least one numeric character

require_upperlower

boolean 

Require at least one uppercase and one lowercase letter

require_special

boolean 

Require at least one special character

expiration_enabled

boolean 

Enable/Disable password expiration policy.

expiration_duration_days

integer 

Number of days before passwords expire. Must be between 30 and 365.

policy_enabled_at

_lock_

string 

The timestamp of when the password expiration policy was last enabled.

## Related Methods

  * [Auth/password_config](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/Auth/password_config "Auth/password_config")
  * [Auth/update_password_config](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/Auth/update_password_config "Auth/update_password_config")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
