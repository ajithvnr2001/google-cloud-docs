---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/generateLossClusters/
title: Method: locations.generateLossClusters \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:56:10.730254+00:00
---

# Method: locations.generateLossClusters  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/generateLossClusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: locations.generateLossClusters Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.generateLossClusters

Generates loss clusters from evaluation results. This is a statelss API method that would not modify the EvaluationSet resource.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{location}:generateLossClusters`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`location` `string` Required. The resource name of the Location. Format: `projects/{project}/locations/{location}`

### Request body

The request body contains data with the following structure: | Fields  
  
`configs[]` `object (`[LossAnalysisConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/generateLossClusters#LossAnalysisConfig)`)` Required. Configuration for the analysis algorithm. Analysis for multiple metrics and multiple candidates could be specified. | `source` `Union type`  
  
The source of evaluation data to analyze. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`evaluationSet` `string` Reference to a persisted EvaluationSet. The service will read items from this set. | `inlineResults` `object (`[EvaluationResultList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/generateLossClusters#EvaluationResultList)`)` Inline evaluation results. Useful for ephemeral analysis in notebooks/SDKs where data isn't persisted. End of mutually exclusive fields.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

## EvaluationResultList

This type has no fields. A wrapper to allow providing a list of items inline.

## LossAnalysisConfig

Configuration for the loss analysis job. | Fields  
  
`metric` `string` Required. The metric to analyze (e.g., "tool_use_quality"). This filters the EvaluationItems in the EvalSet to only those where EvaluationResult.metric matches this value. | `candidate` `string` Required. The candidate model/agent to analyze (e.g., "gemini-3.0-pro"). This targets the specific CandidateResult within the EvaluationResult. | JSON representation  
---  
      
    
    {
      "metric": string,
      "candidate": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
