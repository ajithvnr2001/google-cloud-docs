---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ArtifactLocation/
title: ArtifactLocation \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:39.056071+00:00
---

# ArtifactLocation  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ArtifactLocation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  ArtifactLocation Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * DeveloperConnectExportConfig
    * JSON representation



Defines the location for storing an artifact, such as generated IaC.

JSON representation  
---  
      
    
    {
    
      // Union field location can be only one of the following:
      "developerConnectExportConfig": {
        object ([DeveloperConnectExportConfig](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ArtifactLocation#DeveloperConnectExportConfig))
      },
      "gcsUri": string
      // End of list of possible types for union field location.
    }  
  
Fields  
---  
Union field `location`. Specifies the type of destination for the artifact. `location` can be only one of the following:  
`developerConnectExportConfig` |  `object (`[DeveloperConnectExportConfig](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ArtifactLocation#DeveloperConnectExportConfig)`)` Optional. Source Code Management(SCM) config for storing the content, such as generated IaC. Supports sources integrated with Developer Connect like GitHub, GitHub Enterprise, GitLab, and Bitbucket.  
`gcsUri` |  `string` Optional. The Cloud Storage URI for storing the generated IaC.  
  
## DeveloperConnectExportConfig

Through Developer Connect, defines a location where content such as Infrastructure as Code (IaC) is stored.

JSON representation  
---  
      
    
    {
      "developerConnectRepoUri": string,
      "branch": string,
      "dir": string,
      "commitSha": string
    }  
  
Fields  
---  
`developerConnectRepoUri` |  `string` Required. The Developer Connect Git repository link, formatted as `projects/*/locations/*/connections/*/gitRepositoryLinks/*`.  
`branch` |  `string` Optional. The branch in repo to which the content such as Infrastructure as Code (IaC) should be written to. If empty, Application Design Center will create a branch and push the changes.  
`dir` |  `string` Required. Directory, relative to the source repo, where content such as Infrastructure as Code (IaC) will be stored. This must be a relative path.To specify the root directory, use '/'. If the path or any subdirectories do not exist, they will be created.  
`commitSha` |  `string` Output only. The SHA of the Git commit that contains the exported content such as Infrastructure as Code (IaC).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
