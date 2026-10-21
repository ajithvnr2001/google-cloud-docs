---
url: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/RepoSource/
title: RepoSource \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:25.945287+00:00
---

# RepoSource  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/RepoSource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Reference ](https://docs.cloud.google.com/build/docs/api)



Send feedback 

#  RepoSource Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Location of the source in a Google Cloud Source Repository.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "repoName": string,
      "dir": string,
      "invertRegex": boolean,
      "substitutions": {
        string: string,
        ...
      },
    
      // Union field revision can be only one of the following:
      "branchName": string,
      "tagName": string,
      "commitSha": string
      // End of list of possible types for union field revision.
    }  
  
Fields  
---  
`projectId` |  `string` Optional. ID of the project that owns the Cloud Source Repository. If omitted, the project ID requesting the build is assumed.  
`repoName` |  `string` Required. Name of the Cloud Source Repository.  
`dir` |  `string` Optional. Directory, relative to the source root, in which to run the build.This must be a relative path. If a step's `dir` is specified and is an absolute path, this value is ignored for that step's execution.  
`invertRegex` |  `boolean` Optional. Only trigger a build if the revision regex does NOT match the revision regex.  
`substitutions` |  `map (key: string, value: string)` Optional. Substitutions to use in a triggered build. Should only be used with triggers.runAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
Union field `revision`. A revision within the Cloud Source Repository must be specified in one of these ways. `revision` can be only one of the following:  
`branchName` |  `string` Regex matching branches to build.The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at <https://github.com/google/re2/wiki/Syntax>  
`tagName` |  `string` Regex matching tags to build.The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at <https://github.com/google/re2/wiki/Syntax>  
`commitSha` |  `string` Explicit commit SHA to build.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-17 UTC."],[],[]] 
