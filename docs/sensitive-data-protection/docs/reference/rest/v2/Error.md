---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error/
title: Error \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:44.923064+00:00
---

# Error  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  Error Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ErrorExtraInfo



Details information about an error encountered during job execution or the results of an unsuccessful activation of the JobTrigger.

JSON representation  
---  
      
    
    {
      "details": {
        object ([Status](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Status))
      },
      "timestamps": [
        string
      ],
      "extraInfo": enum ([ErrorExtraInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error#ErrorExtraInfo))
    }  
  
Fields  
---  
`details` |  `object (`[Status](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Status)`)` Detailed error codes and messages.  
`timestamps[]` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The times the error occurred. List includes the oldest timestamp and the last 9 timestamps.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`extraInfo` |  `enum (`[ErrorExtraInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error#ErrorExtraInfo)`)` Additional information about the error.  
  
## ErrorExtraInfo

Additional information about the error.

Enums  
---  
`ERROR_INFO_UNSPECIFIED` | Unused.  
`IMAGE_SCAN_UNAVAILABLE_IN_REGION` | Image scan is not available in the region.  
`FILE_STORE_CLUSTER_UNSUPPORTED` | File store cluster is not supported for profile generation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-09 UTC."],[],[]] 
