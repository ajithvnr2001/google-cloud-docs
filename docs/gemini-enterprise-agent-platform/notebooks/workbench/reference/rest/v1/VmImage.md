---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v1/VmImage/
title: VmImage \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:54:25.972938+00:00
---

# VmImage  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v1/VmImage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  VmImage Stay organized with collections  Save and categorize content based on your preferences. 

Definition of a custom Compute Engine virtual machine image for starting a notebook instance with the environment installed directly on the VM.

JSON representation  
---  
      
    
    {
      "project": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "imageName": string,
      "imageFamily": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`project` |  `string` Required. The name of the Google Cloud project that this VM image belongs to. Format: `{projectId}`  
The reference to an external Compute Engine VM image. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`imageName` |  `string` Use VM image name to find the image.  
`imageFamily` |  `string` Use this VM image family to find the image; the newest image in this family will be used.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
