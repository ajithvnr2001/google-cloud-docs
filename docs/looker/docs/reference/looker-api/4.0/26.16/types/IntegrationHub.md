---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/IntegrationHub/
title: IntegrationHub \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:30.953693+00:00
---

# IntegrationHub  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/IntegrationHub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  IntegrationHub Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.16 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

Datatype

Description

(object)

object 

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

## Related Methods

  * [Integration/create_integration_hub](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Integration/create_integration_hub "Integration/create_integration_hub")
  * [Integration/integration_hub](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Integration/integration_hub "Integration/integration_hub")
  * [Integration/update_integration_hub](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Integration/update_integration_hub "Integration/update_integration_hub")
  * [Integration/accept_integration_hub_legal_agreement](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Integration/accept_integration_hub_legal_agreement "Integration/accept_integration_hub_legal_agreement")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
