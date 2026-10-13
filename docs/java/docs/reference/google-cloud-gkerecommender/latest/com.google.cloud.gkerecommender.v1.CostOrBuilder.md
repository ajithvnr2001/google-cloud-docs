---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.CostOrBuilder
title: Interface CostOrBuilder (0.19.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:05:05.534470+00:00
---

# Interface CostOrBuilder (0.19.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.CostOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CostOrBuilder (0.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.19.0 (latest)  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface CostOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCostPerMillionInputTokens()
    
    
    public abstract Amount getCostPerMillionInputTokens()

Optional. The cost per million input tokens. $/input token = ($/output token) / output-to-input-cost-ratio.

` .google.cloud.gkerecommender.v1.Amount cost_per_million_input_tokens = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Amount](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.Amount)` | The costPerMillionInputTokens.  
  
### getCostPerMillionInputTokensOrBuilder()
    
    
    public abstract AmountOrBuilder getCostPerMillionInputTokensOrBuilder()

Optional. The cost per million input tokens. $/input token = ($/output token) / output-to-input-cost-ratio.

` .google.cloud.gkerecommender.v1.Amount cost_per_million_input_tokens = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AmountOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.AmountOrBuilder)` |   
  
### getCostPerMillionOutputTokens()
    
    
    public abstract Amount getCostPerMillionOutputTokens()

Optional. The cost per million output tokens, calculated as: $/output token = GPU $/s / (1/output-to-input-cost-ratio * input tokens/s + output tokens/s)

` .google.cloud.gkerecommender.v1.Amount cost_per_million_output_tokens = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Amount](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.Amount)` | The costPerMillionOutputTokens.  
  
### getCostPerMillionOutputTokensOrBuilder()
    
    
    public abstract AmountOrBuilder getCostPerMillionOutputTokensOrBuilder()

Optional. The cost per million output tokens, calculated as: $/output token = GPU $/s / (1/output-to-input-cost-ratio * input tokens/s + output tokens/s)

` .google.cloud.gkerecommender.v1.Amount cost_per_million_output_tokens = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AmountOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkerecommender/latest/com.google.cloud.gkerecommender.v1.AmountOrBuilder)` |   
  
### getOutputInputCostRatio()
    
    
    public abstract float getOutputInputCostRatio()

Optional. The output-to-input cost ratio. This determines how the total GPU cost is split between input and output tokens. If not provided, `4.0` is used, assuming a 4:1 output:input cost ratio.

`optional float output_input_cost_ratio = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The outputInputCostRatio.  
  
### getPricingModel()
    
    
    public abstract String getPricingModel()

Optional. The pricing model used to calculate the cost. Can be one of: `3-years-cud`, `1-year-cud`, `on-demand`, `spot`. If not provided, `spot` will be used.

`string pricing_model = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pricingModel.  
  
### getPricingModelBytes()
    
    
    public abstract ByteString getPricingModelBytes()

Optional. The pricing model used to calculate the cost. Can be one of: `3-years-cud`, `1-year-cud`, `on-demand`, `spot`. If not provided, `spot` will be used.

`string pricing_model = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pricingModel.  
  
### hasCostPerMillionInputTokens()
    
    
    public abstract boolean hasCostPerMillionInputTokens()

Optional. The cost per million input tokens. $/input token = ($/output token) / output-to-input-cost-ratio.

` .google.cloud.gkerecommender.v1.Amount cost_per_million_input_tokens = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the costPerMillionInputTokens field is set.  
  
### hasCostPerMillionOutputTokens()
    
    
    public abstract boolean hasCostPerMillionOutputTokens()

Optional. The cost per million output tokens, calculated as: $/output token = GPU $/s / (1/output-to-input-cost-ratio * input tokens/s + output tokens/s)

` .google.cloud.gkerecommender.v1.Amount cost_per_million_output_tokens = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the costPerMillionOutputTokens field is set.  
  
### hasOutputInputCostRatio()
    
    
    public abstract boolean hasOutputInputCostRatio()

Optional. The output-to-input cost ratio. This determines how the total GPU cost is split between input and output tokens. If not provided, `4.0` is used, assuming a 4:1 output:input cost ratio.

`optional float output_input_cost_ratio = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the outputInputCostRatio field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
