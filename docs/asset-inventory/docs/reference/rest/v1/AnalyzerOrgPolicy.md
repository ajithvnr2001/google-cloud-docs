---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicy/
title: AnalyzerOrgPolicy \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:05.821267+00:00
---

# AnalyzerOrgPolicy  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  AnalyzerOrgPolicy Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Rule
    * JSON representation
  * StringValues
    * JSON representation



This organization policy message is a modified version of the one defined in the Organization Policy system. This message contains several fields defined in the original organization policy with some new fields for analysis purpose.

JSON representation  
---  
      
    
    {
      "attachedResource": string,
      "appliedResource": string,
      "rules": [
        {
          object ([Rule](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicy#Rule))
        }
      ],
      "inheritFromParent": boolean,
      "reset": boolean
    }  
  
Fields  
---  
`attachedResource` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of an organization/folder/project resource where this organization policy is set.Notice that some type of constraints are defined with default policy. This field will be empty for them.  
`appliedResource` |  `string` The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of an organization/folder/project resource where this organization policy applies to.For any user defined org policies, this field has the same value as the [attachedResource] field. Only for default policy, this field has the different value.  
`rules[]` |  `object (`[Rule](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicy#Rule)`)` List of rules for this organization policy.  
`inheritFromParent` |  `boolean` If `inheritFromParent` is true, Rules set higher up in the hierarchy (up to the closest root) are inherited and present in the effective policy. If it is false, then no rules are inherited, and this policy becomes the effective root for evaluation.  
`reset` |  `boolean` Ignores policies set above this resource and restores the default behavior of the constraint at this resource. This field can be set in policies for either list or boolean constraints. If set, `rules` must be empty and `inheritFromParent` must be set to false.  
  
## Rule

This rule message is a customized version of the one defined in the Organization Policy system. In addition to the fields defined in the original organization policy, it contains additional field(s) under specific circumstances to support analysis results.

JSON representation  
---  
      
    
    {
      "condition": {
        object ([Expr](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Binding#Expr))
      },
      "conditionEvaluation": {
        object ([ConditionEvaluation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/ConditionEvaluation))
      },
    
      // Union field kind can be only one of the following:
      "values": {
        object ([StringValues](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicy#StringValues))
      },
      "allowAll": boolean,
      "denyAll": boolean,
      "enforce": boolean
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
`condition` |  `object (`[Expr](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Binding#Expr)`)` The evaluating condition for this rule.  
`conditionEvaluation` |  `object (`[ConditionEvaluation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/ConditionEvaluation)`)` The condition evaluation result for this rule. Only populated if it meets all the following criteria:

  * There is a `[condition](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicy#Rule.FIELDS.condition)` defined for this rule.
  * This rule is within `[AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.consolidated_policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedContainers#GovernedContainer.FIELDS.consolidated_policy)`, or `[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset.consolidated_policy](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#GovernedAsset.FIELDS.consolidated_policy)` when the `[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#GovernedAsset)` has `[AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset.governed_resource](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeOrgPolicyGovernedAssets#GovernedAsset.FIELDS.governed_resource)`.

  
Union field `kind`.`kind` can be only one of the following:  
`values` |  `object (`[StringValues](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/AnalyzerOrgPolicy#StringValues)`)` List of values to be used for this policy rule. This field can be set only in policies for list constraints.  
`allowAll` |  `boolean` Setting this to true means that all values are allowed. This field can be set only in Policies for list constraints.  
`denyAll` |  `boolean` Setting this to true means that all values are denied. This field can be set only in Policies for list constraints.  
`enforce` |  `boolean` If `true`, then the `Policy` is enforced. If `false`, then any configuration is acceptable. This field can be set only in Policies for boolean constraints.  
  
## StringValues

The string values for the list constraints.

JSON representation  
---  
      
    
    {
      "allowedValues": [
        string
      ],
      "deniedValues": [
        string
      ]
    }  
  
Fields  
---  
`allowedValues[]` |  `string` List of values allowed at this resource.  
`deniedValues[]` |  `string` List of values denied at this resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-08 UTC."],[],[]] 
