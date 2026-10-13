---
url: https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/Rule/
title: Rule \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:09.324092+00:00
---

# Rule  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/Rule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Rule Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * CELExpression
    * JSON representation
  * RuleActionType



A rule in the cloud control.

JSON representation  
---  
      
    
    {
      "description": string,
      "ruleActionTypes": [
        enum ([RuleActionType](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/Rule#RuleActionType))
      ],
    
      // Union field implementation can be only one of the following:
      "celExpression": {
        object ([CELExpression](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/Rule#CELExpression))
      }
      // End of list of possible types for union field implementation.
    }  
  
Fields  
---  
`description` |  `string` Optional. The rule description. The maximum length is 2000 characters.  
`ruleActionTypes[]` |  `enum (`[RuleActionType](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/Rule#RuleActionType)`)` Required. The functionality that's enabled by the rule.  
Union field `implementation`. The rule implementation. `implementation` can be only one of the following:  
`celExpression` |  `object (`[CELExpression](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/Rule#CELExpression)`)` The rule's logic expression in Common Expression Language (CEL).  
  
## CELExpression

A Common Expression Language (CEL) expression that's used to create a rule.

JSON representation  
---  
      
    
    {
      "expression": string,
    
      // Union field criteria can be only one of the following:
      "resourceTypesValues": {
        object ([StringList](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/StringList))
      }
      // End of list of possible types for union field criteria.
    }  
  
Fields  
---  
`expression` |  `string` Required. The logical expression in CEL. The maximum length of the condition is 1000 characters. For more information, see [CEL expression](https://cloud.google.com/security-command-center/docs/compliance-manager-write-cel-expressions).  
Union field `criteria`. The criteria of the CEL expression. `criteria` can be only one of the following:  
`resourceTypesValues` |  `object (`[StringList](https://docs.cloud.google.com/security-command-center/docs/reference/cloudsecuritycompliance/rest/v1/StringList)`)` The resource instance types on which this expression is defined. The format is `<SERVICE_NAME>/<type>`. For example: `compute.googleapis.com/Instance`  
  
## RuleActionType

The action type of the rule.

Enums  
---  
`RULE_ACTION_TYPE_UNSPECIFIED` | Default value. This value is unused.  
`RULE_ACTION_TYPE_PREVENTIVE` | The rule is intended to prevent non-compliance.  
`RULE_ACTION_TYPE_DETECTIVE` | The rule is intended to detect non-compliance.  
`RULE_ACTION_TYPE_AUDIT` | The rule is intended to audit non-compliance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-07 UTC."],[],[]] 
