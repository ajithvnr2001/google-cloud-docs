---
url: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.publishers
title: REST Resource: projects.locations.publishers \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:43.229963+00:00
---

# REST Resource: projects.locations.publishers  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.publishers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  REST Resource: projects.locations.publishers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Publisher
    * JSON representation
  * PublisherTier
  * Methods



## Resource: Publisher

Represents a verified Publisher of Skills. Prepopulated publishers include `publishers/cloud.google.com` and `publishers/workspace.google.com`.

JSON representation  
---  
      
    
    {
      "name": string,
      "verifiedPrefix": string,
      "displayName": string,
      "publisherTier": enum ([PublisherTier](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.publishers#PublisherTier)),
      "documentationUri": string,
      "supportUri": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Resource name of the publisher. Format: `projects/{project}/locations/{location}/publishers/{publisher}`  
`verifiedPrefix` |  `string` Required. The verified prefix (e.g. "snowflake-", "google-") associated with this publisher. The system uses this prefix to enforce name-squatting rules during Skill registration. Must be globally unique across all publishers.  
`displayName` |  `string` Optional. Human readable display name of the publisher.  
`publisherTier` |  `enum (`[PublisherTier](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.publishers#PublisherTier)`)` Output only. The curation tier of the publisher.  
`documentationUri` |  `string` Optional. URI pointing to official publisher documentation.  
`supportUri` |  `string` Optional. URI pointing to the support portal or email.  
  
## PublisherTier

Curation tier representing the publisher's level of verification.

Enums  
---  
`PUBLISHER_TIER_UNSPECIFIED` | Default value. Unspecified.  
`FIRST_PARTY` | First-party Google-curated and verified global publishers.  
`THIRD_PARTY` | Third-party verified enterprise partner publishers.  
`PRIVATE` | Private publishers within the developer's workspace/project.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.publishers/get)`

|  Fetches details of a specific Publisher.  
  
### `[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.publishers/list)`

|  Lists all Publishers in a location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-24 UTC."],[],[]] 
