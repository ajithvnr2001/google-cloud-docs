---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/EvaluationSpec/
title: EvaluationSpec \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:10.514745+00:00
---

# EvaluationSpec  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/EvaluationSpec/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  EvaluationSpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Variant
    * JSON representation
  * Allocation
    * JSON representation
  * AllocationSlot
    * JSON representation
  * EvaluationRule
    * JSON representation



EvaluationSpec holds rules for evaluating the value of a flag.

JSON representation  
---  
      
    
    {
      "variants": [
        {
          object ([Variant](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/EvaluationSpec#Variant))
        }
      ],
      "defaultTarget": string,
      "allocations": [
        {
          object ([Allocation](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/EvaluationSpec#Allocation))
        }
      ],
      "rules": [
        {
          object ([EvaluationRule](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/EvaluationSpec#EvaluationRule))
        }
      ],
      "attributes": [
        string
      ]
    }  
  
Fields  
---  
`variants[]  
**(deprecated)**` |  `object (`[Variant](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/EvaluationSpec#Variant)`)` This item is deprecated!Optional. A list of variants.  
`defaultTarget` |  `string` Required. Default variant or allocation of the flag.  
`allocations[]` |  `object (`[Allocation](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/EvaluationSpec#Allocation)`)` Optional. A list of allocations.  
`rules[]` |  `object (`[EvaluationRule](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/EvaluationSpec#EvaluationRule)`)` Optional. Evaluation rules define the logic for evaluating the flag against a given context. The rules are evaluated sequentially in their specified order.  
`attributes[]` |  `string` Optional. Names of the context attributes that are used in the evaluation rules and allocations.  
  
## Variant

Variant is an identifier for a value (name assigned to a value). DEPRECATED: Use Flag.Variants instead.

JSON representation  
---  
      
    
    {
      "name": string,
    
      // Union field value can be only one of the following:
      "boolValue": boolean,
      "intValue": string,
      "stringValue": string,
      "doubleValue": number
      // End of list of possible types for union field value.
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the variant. Max length: 128 bytes.  
Union field `value`. value is a single flag value for the variant. `value` can be only one of the following:  
`boolValue` |  `boolean` Optional. Boolean flag value.  
`intValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Integer flag value.  
`stringValue` |  `string` Optional. String flag value.  
`doubleValue` |  `number` Optional. Double flag value.  
  
## Allocation

Allocation defines a set of weighted flag variants, specifying how traffic is split based on the randomization unit.

JSON representation  
---  
      
    
    {
      "id": string,
      "randomizedOn": string,
      "description": string,
      "slots": [
        {
          object ([AllocationSlot](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/EvaluationSpec#AllocationSlot))
        }
      ]
    }  
  
Fields  
---  
`id` |  `string` Required. Allocation ID. Max length: 128 bytes.  
`randomizedOn` |  `string` Required. Key of the context attribute that is used for traffic splitting.  
`description` |  `string` Optional. Description of the allocation. Max length: 500 bytes.  
`slots[]` |  `object (`[AllocationSlot](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/EvaluationSpec#AllocationSlot)`)` Required. Slots defines the weighted distribution of variants.  
  
## AllocationSlot

AllocationSlot specifies a variant and the proportion of traffic allocated to it.

JSON representation  
---  
      
    
    {
      "variant": string,
      "weight": integer
    }  
  
Fields  
---  
`variant` |  `string` Required. Variant of the allocation slot.  
`weight` |  `integer` Required. Weight defines the proportion of traffic to allocate to the variant, relative to other slots in the same allocation.  
  
## EvaluationRule

EvaluationRule defines a single rule for evaluating a feature flag. A rule consists of a condition that, if met, assigns a specific variant or allocation to the user.

JSON representation  
---  
      
    
    {
      "id": string,
      "condition": string,
      "target": string
    }  
  
Fields  
---  
`id` |  `string` Required. Evaluation rule ID. Max length: 128 bytes.  
`condition` |  `string` Required. A Common Expression Language (CEL) expression that evaluates to a boolean. The expression is evaluated against the provided context. If it returns true, the rule's target is applied.  
`target` |  `string` Required. The target variant or allocation to apply if the condition is met. This should match the name of a defined variant or allocation's ID.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
