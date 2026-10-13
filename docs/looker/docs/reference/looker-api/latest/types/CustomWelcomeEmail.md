---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CustomWelcomeEmail/
title: CustomWelcomeEmail \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:37.865804+00:00
---

# CustomWelcomeEmail  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CustomWelcomeEmail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  CustomWelcomeEmail Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

Datatype

Description

(object)

object 

enabled

boolean 

If true, custom email content will replace the default body of welcome emails

content

string 

The HTML to use as custom content for welcome emails. Script elements and other potentially dangerous markup will be removed.

subject

string 

The text to appear in the email subject line. Only available with a whitelabel license and whitelabel_configuration.advanced_custom_welcome_email enabled.

header

string 

The text to appear in the header line of the email body. Only available with a whitelabel license and whitelabel_configuration.advanced_custom_welcome_email enabled.

## Related Methods

  * [Config/custom_welcome_email](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/custom_welcome_email "Config/custom_welcome_email")
  * [Config/update_custom_welcome_email](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/update_custom_welcome_email "Config/update_custom_welcome_email")



## Related Types

  * [Setting](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Setting "Setting")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
