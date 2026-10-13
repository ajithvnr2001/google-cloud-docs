---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/TerraformModule/
title: TerraformModule \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:40:44.486905+00:00
---

# TerraformModule  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/TerraformModule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  TerraformModule Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TerraformFile
    * JSON representation



Represents a Terraform module, which is a collection of Terraform files. Eg: { "source": "git::[https://github.com/my-org/my-repo"](https://github.com/my-org/my-repo), "files": [ { "path": "/path/to/file/main.tf", "content": "tf file content" } ] }

JSON representation  
---  
      
    
    {
      "source": string,
      "files": [
        {
          object ([TerraformFile](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/TerraformModule#TerraformFile))
        }
      ]
    }  
  
Fields  
---  
`source` |  `string` The source of the Terraform module.  
`files[]` |  `object (`[TerraformFile](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/TerraformModule#TerraformFile)`)` The files within the Terraform module.  
  
## TerraformFile

Represents a single Terraform file.

JSON representation  
---  
      
    
    {
      "path": string,
      "content": string
    }  
  
Fields  
---  
`path` |  `string` The path of the Terraform file.  
`content` |  `string` The content of the Terraform file.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
