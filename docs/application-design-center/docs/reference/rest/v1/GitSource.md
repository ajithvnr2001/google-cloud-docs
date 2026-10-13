---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/GitSource/
title: GitSource \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:19.805207+00:00
---

# GitSource  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/GitSource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  GitSource Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * DeveloperConnectConfig
    * JSON representation



Defines how to access a Git source.

JSON representation  
---  
      
    
    {
      "repo": string,
      "dir": string,
      "commitSha": string,
      "developerConnectConfig": {
        object ([DeveloperConnectConfig](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/GitSource#DeveloperConnectConfig))
      },
      "refTag": string
    }  
  
Fields  
---  
`repo` |  `string` Required. Location of the git repo to build.  
`dir` |  `string` Optional. Directory, relative to the source root, in which to run the build. This must be a relative path. If a step's `dir` is specified and is an absolute path, this value is ignored for that step's execution.  
`commitSha` |  `string` Output only. The commit SHA of the git repo deduced from given refTag.  
`developerConnectConfig  
**(deprecated)**` |  `object (`[DeveloperConnectConfig](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/GitSource#DeveloperConnectConfig)`)` This item is deprecated!Optional. This config defines the location of a source through Developer Connect. Used to access private git repos.  
`refTag` |  `string` Required. The reference tag of the git repo.  
  
## DeveloperConnectConfig

This config defines the location of a source through Developer Connect.

JSON representation  
---  
      
    
    {
      "gitRepositoryLink": string
    }  
  
Fields  
---  
`gitRepositoryLink` |  `string` Required. The Developer Connect Git repository link, formatted as `projects/*/locations/*/connections/*/gitRepositoryLink/*`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
