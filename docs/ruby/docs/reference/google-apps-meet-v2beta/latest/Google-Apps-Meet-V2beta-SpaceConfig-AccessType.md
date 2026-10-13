---
url: https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpaceConfig-AccessType/
title: Google Meet V2BETA API - Module Google::Apps::Meet::V2beta::SpaceConfig::AccessType (v0.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:50.542497+00:00
---

# Google Meet V2BETA API - Module Google::Apps::Meet::V2beta::SpaceConfig::AccessType (v0.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpaceConfig-AccessType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Meet V2BETA API - Module Google::Apps::Meet::V2beta::SpaceConfig::AccessType (v0.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.0 (latest)  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.1  0.5.0  0.4.0  0.3.2  0.2.2  0.1.0 

Reference documentation and code samples for the Google Meet V2BETA API module Google::Apps::Meet::V2beta::SpaceConfig::AccessType.

Possible access types for a meeting space.

## Constants 

### ACCESS_TYPE_UNSPECIFIED

**value:** 0  
Default value specified by the user's organization. Note: This is never returned, as the configured access type is returned instead.

### OPEN

**value:** 1  
Anyone with the join information (for example, the URL or phone access information) can join without knocking.

### TRUSTED

**value:** 2  
Members of the host's organization, invited external users, and dial-in users can join without knocking. Everyone else must knock.

### RESTRICTED

**value:** 3  
Only invitees can join without knocking. Everyone else must knock.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
