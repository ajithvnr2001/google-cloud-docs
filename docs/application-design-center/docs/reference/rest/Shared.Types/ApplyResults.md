---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ApplyResults/
title: ApplyResults \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:38.762312+00:00
---

# ApplyResults  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ApplyResults/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  ApplyResults Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TerraformOutput
    * JSON representation



Outputs and artifacts from applying a deployment.

JSON representation  
---  
      
    
    {
      "content": string,
      "artifacts": string,
      "outputs": {
        string: {
          object ([TerraformOutput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ApplyResults#TerraformOutput))
        },
        ...
      }
    }  
  
Fields  
---  
`content` |  `string` Location of a blueprint copy and other manifests in Google Cloud Storage. Format: `gs://{bucket}/{object}`  
`artifacts` |  `string` Location of artifacts (e.g. logs) in Google Cloud Storage. Format: `gs://{bucket}/{object}`  
`outputs` |  `map (key: string, value: object (`[TerraformOutput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ApplyResults#TerraformOutput)`))` Map of output name to output info.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## TerraformOutput

Describes a Terraform output.

JSON representation  
---  
      
    
    {
      "sensitive": boolean,
      "value": value
    }  
  
Fields  
---  
`sensitive` |  `boolean` Identifies whether Terraform has set this output as a potential sensitive value.  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Value of output.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
