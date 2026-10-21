---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GenerateLossClustersResponse/
title: GenerateLossClustersResponse \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:18:48.211018+00:00
---

# GenerateLossClustersResponse  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GenerateLossClustersResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  GenerateLossClustersResponse Stay organized with collections  Save and categorize content based on your preferences. 

Response message for EvaluationAnalyticsService.GenerateLossClusters.

Fields  
  
`analysisTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp when this analysis was completed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `results[]` `object (`[LossAnalysisResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GenerateLossClustersResponse#LossAnalysisResult)`)` The analysis results, one per config provided in the request. | JSON representation  
---  
      
    
    {
      "analysisTime": string,
      "results": [
        {
          object ([LossAnalysisResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GenerateLossClustersResponse#LossAnalysisResult))
        }
      ]
    }  
  
## LossAnalysisResult

The top-level result for loss analysis, stored within an EvalSet.

Fields  
  
`config` `object (`[LossAnalysisConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/generateLossClusters#LossAnalysisConfig)`)` The configuration used to generate this analysis. | `analysisTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp when this analysis was performed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `clusters[]` `object (`[LossCluster](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GenerateLossClustersResponse#LossCluster)`)` The list of identified loss clusters. | JSON representation  
---  
      
    
    {
      "config": {
        object ([LossAnalysisConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/generateLossClusters#LossAnalysisConfig))
      },
      "analysisTime": string,
      "clusters": [
        {
          object ([LossCluster](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GenerateLossClustersResponse#LossCluster))
        }
      ]
    }  
  
## LossCluster

Represents a semantic grouping of failures (e.g., "Hallucination of Action").

Fields  
  
`clusterId` `string` Unique identifier for the loss cluster within the scope of the analysis result. | `taxonomyEntry` `object (`[LossTaxonomyEntry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GenerateLossClustersResponse#LossTaxonomyEntry)`)` The structured definition of the loss taxonomy for this cluster. | `itemCount` `integer` The total number of EvaluationItems falling into this cluster. | `examples[]` `object (`[LossExample](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GenerateLossClustersResponse#LossExample)`)` A list of examples that belong to this cluster. This links the cluster back to the specific EvaluationItems and Rubrics. | JSON representation  
---  
      
    
    {
      "clusterId": string,
      "taxonomyEntry": {
        object ([LossTaxonomyEntry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GenerateLossClustersResponse#LossTaxonomyEntry))
      },
      "itemCount": integer,
      "examples": [
        {
          object ([LossExample](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GenerateLossClustersResponse#LossExample))
        }
      ]
    }  
  
## LossTaxonomyEntry

Defines a specific entry in the loss pattern taxonomy.

Fields  
  
`l1Category` `string` The primary category of the loss (e.g., "Hallucination", "Tool Calling"). This field is typically required. | `l2Category` `string` The secondary category of the loss (e.g., "Hallucination of Action", "Incorrect Tool Selection"). | `description` `string` A detailed description of this loss pattern. Example: "The agent verbally confirms an action without executing the tool." | JSON representation  
---  
      
    
    {
      "l1Category": string,
      "l2Category": string,
      "description": string
    }  
  
## LossExample

Represents a specific example of a loss pattern.

Fields  
  
`failedRubrics[]` `object (`[FailedRubric](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FailedRubric)`)` The specific rubric(s) that failed and caused this example to be classified here. An example might fail multiple rubrics, but only specific ones trigger this loss pattern. | `source` `Union type`  
  
The source of this example. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`evaluationItem` `string` Reference to the persisted EvalItem resource name. Format: projects/.../locations/.../evaluationItems/{itemId} Used when analysis is run on an EvalSet. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "failedRubrics": [
        {
          object ([FailedRubric](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FailedRubric))
        }
      ],
    
      // source
      "evaluationItem": string
      // Union type
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
