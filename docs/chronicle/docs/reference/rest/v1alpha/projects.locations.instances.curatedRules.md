---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.curatedRules
title: REST Resource: projects.locations.instances.curatedRules \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:53.054675+00:00
---

# REST Resource: projects.locations.instances.curatedRules  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.curatedRules

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.curatedRules Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CuratedRule
    * JSON representation
  * Methods



## Resource: CuratedRule

Represents a rule authored by Chronicle's Google Cloud Threat Intelligence (GCTI).

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "severity": {
        object ([Severity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Severity))
      },
      "metadata": {
        string: string,
        ...
      },
      "type": enum ([RuleType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/RuleType)),
      "precision": enum ([CuratedRulePrecision](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/CuratedRulePrecision)),
      "tactics": [
        {
          object ([MitreTactic](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/MitreTactic))
        }
      ],
      "techniques": [
        {
          object ([MitreTechnique](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/MitreTechnique))
        }
      ],
      "updateTime": string,
      "curatedRuleSet": string,
      "description": string
    }  
  
Fields  
---  
`name` |  `string` Required. Full resource name for the curated rule. Format: projects/{project}/locations/{location}/instances/{instance}/curatedrules/{rule}  
`displayName` |  `string` Output only. Unique display name of the curated rule.  
`severity` |  `object (`[Severity](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/Severity)`)` Output only. The severity of the curated rule.  
`metadata` |  `map (key: string, value: string)` Output only. Additional unstructured metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`type` |  `enum (`[RuleType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/RuleType)`)` Output only. User-facing type of the curated rule.  
`precision` |  `enum (`[CuratedRulePrecision](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/CuratedRulePrecision)`)` Output only. Precision level of the curated rule.  
`tactics[]` |  `object (`[MitreTactic](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/MitreTactic)`)` Output only. Mitre tactics covered by the curated rule.  
`techniques[]` |  `object (`[MitreTechnique](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/MitreTechnique)`)` Output only. Mitre techniques covered by the curated rule.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the curated rule was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`curatedRuleSet` |  `string` Output only. The parent CuratedRuleSet that the rule is listed under. Format: projects/{project}/locations/{location}/instances/{instance}/curatedRuleSetCategories/{category}/curatedRuleSets/{ruleSet}  
`description` |  `string` Output only. The description of the curated rule.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.curatedRules/get)`

|  Gets a CuratedRule.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.curatedRules/list)`

|  Lists CuratedRules.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-22 UTC."],[],[]] 
