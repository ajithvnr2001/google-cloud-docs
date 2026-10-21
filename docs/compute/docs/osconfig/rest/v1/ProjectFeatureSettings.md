---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/ProjectFeatureSettings/
title: ProjectFeatureSettings \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:25:58.109392+00:00
---

# ProjectFeatureSettings  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/ProjectFeatureSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  ProjectFeatureSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * PatchAndConfigFeatureSet



ProjectFeatureSettings represents the VM Manager feature settings in a project. For more information, see [Enable full VM Manager functionality](https://docs.cloud.google.com/compute/docs/manage-os#enable-full-vmm).

JSON representation  
---  
      
    
    {
      "name": string,
      "patchAndConfigFeatureSet": enum ([PatchAndConfigFeatureSet](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/ProjectFeatureSettings#PatchAndConfigFeatureSet))
    }  
  
Fields  
---  
`name` |  `string` Required. Immutable. Name specifies the URL for the ProjectFeatureSettings resource: `projects/projectId/locations/global/projectFeatureSettings` .  
`patchAndConfigFeatureSet` |  `enum (`[PatchAndConfigFeatureSet](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/ProjectFeatureSettings#PatchAndConfigFeatureSet)`)` Set PatchAndConfigFeatureSet for the project.  
  
## PatchAndConfigFeatureSet

The project-level PatchAndConfigFeatureSet for the VM Manager product.

Enums  
---  
`PATCH_AND_CONFIG_FEATURE_SET_UNSPECIFIED` | Not specified placeholder  
`OSCONFIG_B` | Enables only the basic set of VM Manager features in the project.  
`OSCONFIG_C` | Enables all VM Manager features in the project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
