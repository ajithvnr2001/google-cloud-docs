---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Event/
title: Event \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:39:57.779252+00:00
---

# Event  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Event/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Event Stay organized with collections  Save and categorize content based on your preferences. 

An edge describing the relationship between an Artifact and an Execution in a lineage graph.

Fields  
  
`artifact` `string` Required. The relative resource name of the Artifact in the Event. | `execution` `string` Output only. The relative resource name of the Execution in the Event. | `eventTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. time the Event occurred.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `type` `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Event#Type)`)` Required. The type of the Event. | `labels` `map (key: string, value: string)` The labels with user-defined metadata to annotate events.label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Event (System labels are excluded).See <https://goo.gl/xmQnxf> for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. | JSON representation  
---  
      
    
    {
      "artifact": string,
      "execution": string,
      "eventTime": string,
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Event#Type)),
      "labels": {
        string: string,
        ...
      }
    }  
  
## Type

Describes whether an Event's Artifact is the Execution's input or output.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified whether input or output of the Execution.  
`INPUT` | An input of the Execution.  
`OUTPUT` | An output of the Execution.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
