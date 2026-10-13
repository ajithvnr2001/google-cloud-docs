---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentIntegrationDetails/
title: AgentIntegrationDetails \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:32:59.477909+00:00
---

# AgentIntegrationDetails  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentIntegrationDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  AgentIntegrationDetails Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * AgentIntegrationAction
    * JSON representation
  * AgentActionParameter
    * JSON representation
  * ImpactAnalysisActionsMetadata
    * JSON representation
  * RiskScore



Details of an integration that can be used to execute actions.

JSON representation  
---  
      
    
    {
      "integration": string,
      "integrationInstance": string,
      "displayName": string,
      "description": string,
      "actions": [
        {
          object ([AgentIntegrationAction](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentIntegrationDetails#AgentIntegrationAction))
        }
      ]
    }  
  
Fields  
---  
`integration` |  `string` Unique identifier of the integration.  
`integrationInstance` |  `string` Unique identifier of the integration instance.  
`displayName` |  `string` Display name of the integration.  
`description` |  `string` Description of the integration.  
`actions[]` |  `object (`[AgentIntegrationAction](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentIntegrationDetails#AgentIntegrationAction)`)` List of all actions that can be executed on the SIEM alert using this integration.  
  
## AgentIntegrationAction

Details of an action that can be executed.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "description": string,
      "parameters": [
        {
          object ([AgentActionParameter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentIntegrationDetails#AgentActionParameter))
        }
      ],
      "entityTypes": [
        string
      ],
      "shortDescription": string,
      "parametersDescription": string,
      "impactAnalysisActionsMetadata": {
        object ([ImpactAnalysisActionsMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentIntegrationDetails#ImpactAnalysisActionsMetadata))
      }
    }  
  
Fields  
---  
`displayName` |  `string` The name of the action.  
`description` |  `string` The description of the action.  
`parameters[]` |  `object (`[AgentActionParameter](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentIntegrationDetails#AgentActionParameter)`)` The parameters required for the action.  
`entityTypes[]` |  `string` The entity types that the action supports.  
`shortDescription` |  `string` Output only. The short description of the action.  
`parametersDescription` |  `string` Output only. Description of the parameters for AI use.  
`impactAnalysisActionsMetadata` |  `object (`[ImpactAnalysisActionsMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentIntegrationDetails#ImpactAnalysisActionsMetadata)`)` Output only. Metadata for the action.  
  
## AgentActionParameter

Details of a parameter required for an action. Details of an action that can be executed.

JSON representation  
---  
      
    
    {
      "mandatory": boolean,
      "defaultValue": string,
      "description": string,
      "name": string,
      "value": string,
      "type": string,
      "optionalValuesJson": string
    }  
  
Fields  
---  
`mandatory` |  `boolean` Required. Whether the parameter is mandatory.  
`defaultValue` |  `string` The default value of the parameter.  
`description` |  `string` The description of the parameter.  
`name` |  `string` The name of the parameter.  
`value` |  `string` The value of the parameter.  
`type` |  `string` Required. The type of the parameter.  
`optionalValuesJson` |  `string` The optional values for the parameter in JSON format.  
  
## ImpactAnalysisActionsMetadata

Metadata for an action.

JSON representation  
---  
      
    
    {
      "reversibilityRiskScore": enum ([RiskScore](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentIntegrationDetails#RiskScore)),
      "reversibilityRiskReasoning": string,
      "scopeRiskScore": enum ([RiskScore](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentIntegrationDetails#RiskScore)),
      "scopeRiskReasoning": string,
      "frictionRiskScore": enum ([RiskScore](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentIntegrationDetails#RiskScore)),
      "frictionRiskReasoning": string,
      "volumeRiskScore": enum ([RiskScore](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentIntegrationDetails#RiskScore)),
      "volumeRiskReasoning": string,
      "assetCriticalityRelevanceReasoning": string,
      "assetCriticalityCategories": [
        string
      ],
      "assetCriticalityCategoriesReasoning": string,
      "assetCriticalityRelevance": boolean
    }  
  
Fields  
---  
`reversibilityRiskScore` |  `enum (`[RiskScore](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentIntegrationDetails#RiskScore)`)` Output only. Risk score for the reversibility of the action. Reversibility is defined as the ease of undoing an action (e.g., stopping a temporary process vs. purging data).  
`reversibilityRiskReasoning` |  `string` Output only. Reasoning for the reversibility risk score. Reversibility is defined as the ease of undoing an action (e.g., stopping a temporary process vs. purging data).  
`scopeRiskScore` |  `enum (`[RiskScore](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentIntegrationDetails#RiskScore)`)` Output only. Risk score for the scope of the action. Scope is defined as the breadth of impact (e.g., an isolated user vs. foundational infrastructure).  
`scopeRiskReasoning` |  `string` Output only. Reasoning for the scope risk score. Scope is defined as the breadth of impact (e.g., an isolated user vs. foundational infrastructure).  
`frictionRiskScore` |  `enum (`[RiskScore](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentIntegrationDetails#RiskScore)`)` Output only. Risk score for the friction of the action. Friction is defined as the potential disruption to productivity (e.g., background analysis vs. locking a profile).  
`frictionRiskReasoning` |  `string` Output only. Reasoning for the friction risk score. Friction is defined as the potential disruption to productivity (e.g., background analysis vs. locking a profile).  
`volumeRiskScore` |  `enum (`[RiskScore](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/AgentIntegrationDetails#RiskScore)`)` Output only. Risk score for the volume of the action. Volume is defined as the scale of deployment (e.g., localized execution vs. fleet-wide orchestration).  
`volumeRiskReasoning` |  `string` Output only. Reasoning for the volume risk score. Volume is defined as the scale of deployment (e.g., localized execution vs. fleet-wide orchestration).  
`assetCriticalityRelevanceReasoning` |  `string` Output only. Reasoning for why the action is relevant for asset enrichment.  
`assetCriticalityCategories[]` |  `string` Output only. Categories for asset criticality.  
`assetCriticalityCategoriesReasoning` |  `string` Output only. Reasoning for why the action is relevant for asset criticality categories.  
`assetCriticalityRelevance` |  `boolean` Output only. Whether the action is relevant for asset enrichment.  
  
## RiskScore

Represents the risk classification of an integration action. The score is determined by evaluating operational parameters such as: - Reversibility: The ease of undoing an action (e.g., stopping a temporary process vs purging data). - Scope: The breadth of impact (e.g., an isolated user vs foundational infrastructure). - Friction: The potential disruption to productivity (e.g., background analysis vs. locking a profile). - Volume: The scale of deployment (e.g., localized execution vs fleet-wide orchestration).

Enums  
---  
`RISK_SCORE_UNSPECIFIED` | Unspecified risk score.  
`LOW` | Low risk score.  
`MEDIUM` | Medium risk score.  
`HIGH` | High risk score.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
