---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/EmbedConfig/
title: EmbedConfig \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:46.973323+00:00
---

# EmbedConfig  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/EmbedConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  EmbedConfig Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.18 (latest) 

Datatype

Description

(object)

object 

domain_allowlist

string[] 

alert_url_allowlist

string[] 

alert_url_param_owner

string 

Owner of who defines the alert/schedule params on the base url

alert_url_label

string 

Label for the alert/schedule url

sso_auth_enabled

boolean 

Is SSO embedding enabled for this Looker

embed_cookieless_v2

boolean 

Is Cookieless embedding enabled for this Looker

embed_content_navigation

boolean 

Is embed content navigation enabled for this looker

embed_content_management

boolean 

Is embed content management enabled for this Looker

embed_vis_modernization_default

_lock_

boolean 

Default net new visualizations in embedded context to Modern theme

strict_sameorigin_for_login

boolean 

When true, prohibits the use of Looker login pages in non-Looker iframes. When false, Looker login pages may be used in non-Looker hosted iframes.

look_filters

boolean 

When true, filters are enabled on embedded Looks

hide_look_navigation

boolean 

When true, removes navigation to Looks from embedded dashboards and explores.

permissions

_lock_

object 

Tree of allowed embed permissions

embed_enabled

_lock_

boolean 

True if embedding is licensed for this Looker instance.

## Related Types

  * [Setting](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Setting "Setting")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
