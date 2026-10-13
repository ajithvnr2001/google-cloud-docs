---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/DeveloperConnectSourceConfig/
title: DeveloperConnectSourceConfig \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:20.248255+00:00
---

# DeveloperConnectSourceConfig  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/DeveloperConnectSourceConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  DeveloperConnectSourceConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * GitReference
    * JSON representation



This config specifies the location of a source (such as GitHub or Bitbucket) through Developer Connect.

JSON representation  
---  
      
    
    {
      "developerConnectRepoUri": string,
      "reference": {
        object ([GitReference](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/DeveloperConnectSourceConfig#GitReference))
      },
      "dir": string,
      "fetchedCommitSha": string
    }  
  
Fields  
---  
`developerConnectRepoUri` |  `string` Required. The Developer Connect Git repository link, formatted as `projects/*/locations/*/connections/*/gitRepositoryLinks/*`.  
`reference` |  `object (`[GitReference](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/DeveloperConnectSourceConfig#GitReference)`)` Required. The reference (for example, a branch, tag, or commit SHA) from which the content should be read.  
`dir` |  `string` Required. The sub-directory within the repository from which to read content. The path must be relative to the repository's root such as dir1/dir2. To read content from the root dir, provide "/" as the value of the field.  
`fetchedCommitSha` |  `string` Output only. The SHA of the commit deduced from GitReference.  
  
## GitReference

The Git reference. Can be a commit SHA, branch name, or tag name.

JSON representation  
---  
      
    
    {
    
      // Union field reference can be only one of the following:
      "branch": string,
      "refTag": string,
      "commitSha": string
      // End of list of possible types for union field reference.
    }  
  
Fields  
---  
Union field `reference`. The reference from which the content such as Infrastructure as Code (IaC) should be read. `reference` can be only one of the following:  
`branch` |  `string` Optional. The name of the branch from which content should be read. For example: "main"  
`refTag` |  `string` Optional. The reference tag from which content should be read. For example: "v1.2.3"  
`commitSha` |  `string` Optional. The full SHA hash of a specific commit from which content should be read.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
