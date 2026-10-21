---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Explanation/
title: Explanation \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:58:44.754318+00:00
---

# Explanation  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Explanation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Explanation Stay organized with collections  Save and categorize content based on your preferences. 

Explanation of a prediction (provided in `[PredictResponse.predictions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/PredictResponse#FIELDS.predictions)`) produced by the Model on a given `[instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/explain#body.request_body.FIELDS.instances)`.

Fields  
  
`attributions[]` `object (`[Attribution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ModelExplanation#Attribution)`)` Output only. feature attributions grouped by predicted outputs.For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. `[Attribution.output_index](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ModelExplanation#Attribution.FIELDS.output_index)` can be used to identify which output this attribution is explaining.By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of `0.4` for approving a loan application, the model's decision is to reject the application since `p(reject) = 0.6 > p(approve) = 0.4`, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class.If users set `[ExplanationParameters.top_k](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ExplanationSpec#ExplanationParameters.FIELDS.top_k)`, the attributions are sorted by `[instanceOutputValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ModelExplanation#Attribution.FIELDS.instance_output_value)` in descending order. If `[ExplanationParameters.output_indices](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ExplanationSpec#ExplanationParameters.FIELDS.output_indices)` is specified, the attributions are stored by `[Attribution.output_index](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ModelExplanation#Attribution.FIELDS.output_index)` in the same order as they appear in the outputIndices. | `neighbors[]` `object (`[Neighbor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Explanation#Neighbor)`)` Output only. List of the nearest neighbors for example-based explanations.For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated. | JSON representation  
---  
      
    
    {
      "attributions": [
        {
          object ([Attribution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ModelExplanation#Attribution))
        }
      ],
      "neighbors": [
        {
          object ([Neighbor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Explanation#Neighbor))
        }
      ]
    }  
  
## Neighbor

Neighbors for example-based explanations.

Fields  
  
`neighborId` `string` Output only. The neighbor id. | `neighborDistance` `number` Output only. The neighbor distance. | JSON representation  
---  
      
    
    {
      "neighborId": string,
      "neighborDistance": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
