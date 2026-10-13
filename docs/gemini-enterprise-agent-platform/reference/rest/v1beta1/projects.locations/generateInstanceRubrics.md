---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/generateInstanceRubrics/
title: Method: locations.generateInstanceRubrics \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:59.011075+00:00
---

# Method: locations.generateInstanceRubrics  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/generateInstanceRubrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: locations.generateInstanceRubrics Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.generateInstanceRubrics

Generates rubrics for a given prompt. A rubric represents a single testable criterion for evaluation. One input prompt could have multiple rubrics This RPC allows users to get suggested rubrics based on provided prompt, which can then be reviewed and used for subsequent evaluations.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{location}:generateInstanceRubrics`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`location` `string` Required. The resource name of the Location to generate rubrics from. Format: `projects/{project}/locations/{location}`

### Request body

The request body contains data with the following structure: | Fields  
  
`contents[]` `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content)`)` Required. The prompt to generate rubrics from. For single-turn queries, this is a single instance. For multi-turn queries, this is a repeated field that contains conversation history + latest request. | `predefinedRubricGenerationSpec` `object (`[PredefinedMetricSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Metric#PredefinedMetricSpec)`)` Optional. Specification for using the rubric generation configs of a pre-defined metric, e.g. "generic_quality_v1" and "instruction_following_v1". Some of the configs may be only used in rubric generation and not supporting evaluation, e.g. "fully_customized_generic_quality_v1". If this field is set, the `rubricGenerationSpec` field will be ignored. | `rubricGenerationSpec` `object (`[RubricGenerationSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Metric#RubricGenerationSpec)`)` Optional. Specification for how the rubrics should be generated. | `agentConfig` `object (`[DeprecatedAgentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/DeprecatedAgentConfig)`)` Optional. Agent configuration, required for agent-based rubric generation. | `metricResourceName` `string` Optional. The resource name of a registered metric. Rubric generation using predefined metric spec or LLMBasedMetricSpec is supported. If this field is set, the configuration provided in this field is used for rubric generation. The `predefinedRubricGenerationSpec` and `rubricGenerationSpec` fields will be ignored.

### Response body

Response message for EvaluationService.GenerateInstanceRubrics. If successful, the response body contains data with the following structure: | Fields  
  
`generatedRubrics[]` `object (`[Rubric](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Rubric)`)` Output only. A list of generated rubrics. | JSON representation  
---  
      
    
    {
      "generatedRubrics": [
        {
          object ([Rubric](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Rubric))
        }
      ]
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
