---
url: https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/ProjectSettings/
title: ProjectSettings \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:56.054770+00:00
---

# ProjectSettings  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/ProjectSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Reference ](https://docs.cloud.google.com/artifact-registry/docs/apis)



Send feedback 

#  ProjectSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * RedirectionState



The Artifact Registry settings that apply to a Project.

JSON representation  
---  
      
    
    {
      "name": string,
      "legacyRedirectionState": enum ([RedirectionState](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/ProjectSettings#RedirectionState)),
      "pullPercent": integer
    }  
  
Fields  
---  
`name` |  `string` The name of the project's settings.Always of the form: projects/{project-id}/projectSettingsIn update request: never set In response: always set  
`legacyRedirectionState` |  `enum (`[RedirectionState](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/ProjectSettings#RedirectionState)`)` The redirection state of the legacy repositories in this project.  
`pullPercent` |  `integer` The percentage of pull traffic to redirect from GCR to AR when using partial redirection.  
  
## RedirectionState

The possible redirection states for legacy repositories.

Enums  
---  
`REDIRECTION_STATE_UNSPECIFIED` | No redirection status has been set.  
`REDIRECTION_FROM_GCR_IO_DISABLED` | Redirection is disabled.  
`REDIRECTION_FROM_GCR_IO_ENABLED` | Redirection is enabled.  
`REDIRECTION_FROM_GCR_IO_ENABLED_AND_COPYING` | Redirection is enabled and missing images are copied from GCR  
`REDIRECTION_FROM_GCR_IO_PARTIAL_AND_COPYING` | Redirection is partially enabled and missing images are copied from GCR  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-13 UTC."],[],[]] 
