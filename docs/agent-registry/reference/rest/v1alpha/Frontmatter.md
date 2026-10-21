---
url: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/Frontmatter/
title: Frontmatter \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:46.208454+00:00
---

# Frontmatter  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/Frontmatter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  Frontmatter Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Structured metadata attributes extracted from the package's local SKILL.md frontmatter.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "license": string,
      "compatibility": string,
      "metadata": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the skill.  
`description` |  `string` Required. Functional description.  
`license` |  `string` Optional. License.  
`compatibility` |  `string` Optional. Environmental dependencies or local sidecars.  
`metadata` |  `map (key: string, value: string)` Optional. Extensible flattened map mapping custom tags, authors, and version parameters.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-24 UTC."],[],[]] 
