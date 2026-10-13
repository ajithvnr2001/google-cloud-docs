---
url: https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/Version/
title: Version \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:52.761240+00:00
---

# Version  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/Version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Reference ](https://docs.cloud.google.com/artifact-analysis/docs/apis)



Send feedback 

#  Version Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * VersionKind



Version contains structured information about the version of a package.

JSON representation  
---  
      
    
    {
      "epoch": integer,
      "name": string,
      "revision": string,
      "inclusive": boolean,
      "kind": enum ([VersionKind](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/Version#VersionKind)),
      "fullName": string
    }  
  
Fields  
---  
`epoch` |  `integer` Used to correct mistakes in the version numbering scheme.  
`name` |  `string` Required only when version kind is NORMAL. The main part of the version name.  
`revision` |  `string` The iteration of the package build from the above version.  
`inclusive` |  `boolean` Whether this version is specifying part of an inclusive range. Grafeas does not have the capability to specify version ranges; instead we have fields that specify start version and end versions. At times this is insufficient - we also need to specify whether the version is included in the range or is excluded from the range. This boolean is expected to be set to true when the version is included in a range.  
`kind` |  `enum (`[VersionKind](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/Version#VersionKind)`)` Required. Distinguishes between sentinel MIN/MAX versions and normal versions.  
`fullName` |  `string` Human readable version string. This string is of the form :- and is only set when kind is NORMAL.  
  
## VersionKind

Whether this is an ordinary package version or a sentinel MIN/MAX version.

Enums  
---  
`VERSION_KIND_UNSPECIFIED` | Unknown.  
`NORMAL` | A standard package version.  
`MINIMUM` | A special version representing negative infinity.  
`MAXIMUM` | A special version representing positive infinity.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-13 UTC."],[],[]] 
