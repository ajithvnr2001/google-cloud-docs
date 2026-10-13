---
url: https://docs.cloud.google.com/kms/docs/reference/rest/v1/KeyProjectResolutionMode/
title: KeyProjectResolutionMode \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:50.999761+00:00
---

# KeyProjectResolutionMode  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/reference/rest/v1/KeyProjectResolutionMode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Reference ](https://docs.cloud.google.com/kms/docs/apis)



Send feedback 

#  KeyProjectResolutionMode Stay organized with collections  Save and categorize content based on your preferences. 

Defines the resolution mode enum for the project or folder. The `[KeyProjectResolutionMode](https://docs.cloud.google.com/kms/docs/reference/rest/v1/KeyProjectResolutionMode)` determines the mechanism by which `[AutokeyConfig](https://docs.cloud.google.com/kms/docs/reference/rest/v1/AutokeyConfig)` identifies a `[keyProject](https://docs.cloud.google.com/kms/docs/reference/rest/v1/AutokeyConfig#FIELDS.key_project)` at its specific configuration node. This parameter also determines if Autokey can be used within this project or folder.

Enums  
---  
`KEY_PROJECT_RESOLUTION_MODE_UNSPECIFIED` | Default value. When KeyProjectResolutionMode is set to KEY_PROJECT_RESOLUTION_MODE_UNSPECIFIED for a folder and that folder has a keyProject set, the folder acts like its KeyProjectResolutionMode is DEDICATED_KEY_PROJECT.  
`DEDICATED_KEY_PROJECT` | Keys are created in a dedicated project specified by `keyProject`.  
`RESOURCE_PROJECT` | Keys are created in the same project as the resource requesting the key. The `keyProject` must not be set when this mode is used.  
`DISABLED` | Disables the AutokeyConfig. When this mode is set, any AutokeyConfig from higher levels in the resource hierarchy are ignored for this resource and its descendants. This setting can be overridden by a more specific configuration at a lower level. For example, if Autokey is disabled on a folder, it can be re-enabled on a sub-folder or project within that folder by setting a different mode (e.g., DEDICATED_KEY_PROJECT or RESOURCE_PROJECT).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
