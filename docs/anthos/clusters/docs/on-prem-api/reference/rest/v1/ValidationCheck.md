---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest/v1/ValidationCheck/
title: ValidationCheck \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:28.767967+00:00
---

# ValidationCheck  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest/v1/ValidationCheck/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  ValidationCheck Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Options
  * ValidationCheckStatus
    * JSON representation
  * ValidationCheckResult
    * JSON representation
  * State
  * Scenario



ValidationCheck represents the result of preflight check.

JSON representation  
---  
      
    
    {
      "option": enum ([Options](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck#Options)),
      "status": {
        object ([ValidationCheckStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck#ValidationCheckStatus))
      },
      "scenario": enum ([Scenario](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck#Scenario))
    }  
  
Fields  
---  
`option` |  `enum (`[Options](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck#Options)`)` Options used for the validation check  
`status` |  `object (`[ValidationCheckStatus](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck#ValidationCheckStatus)`)` Output only. The detailed validation check status.  
`scenario` |  `enum (`[Scenario](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck#Scenario)`)` Output only. The scenario when the preflight checks were run.  
  
## Options

Enums  
---  
`OPTIONS_UNSPECIFIED` | Default value. Standard preflight validation check will be used.  
`SKIP_VALIDATION_CHECK_BLOCKING` | Prevent failed preflight checks from failing.  
`SKIP_VALIDATION_ALL` | Skip all preflight check validations.  
  
## ValidationCheckStatus

ValidationCheckStatus defines the detailed validation check status.

JSON representation  
---  
      
    
    {
      "result": [
        {
          object ([ValidationCheckResult](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck#ValidationCheckResult))
        }
      ]
    }  
  
Fields  
---  
`result[]` |  `object (`[ValidationCheckResult](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck#ValidationCheckResult)`)` Individual checks which failed as part of the Preflight check execution.  
  
## ValidationCheckResult

ValidationCheckResult defines the details about the validation check.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck#State)),
      "description": string,
      "category": string,
      "reason": string,
      "details": string
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/ValidationCheck#State)`)` The validation check state.  
`description` |  `string` The description of the validation check.  
`category` |  `string` The category of the validation.  
`reason` |  `string` A human-readable message of the check failure.  
`details` |  `string` Detailed failure information, which might be unformatted.  
  
## State

Enums  
---  
`STATE_UNKNOWN` | The default value. The check result is unknown.  
`STATE_FAILURE` | The check failed.  
`STATE_SKIPPED` | The check was skipped.  
`STATE_FATAL` | The check itself failed to complete.  
`STATE_WARNING` | The check encountered a warning.  
  
## Scenario

Enums  
---  
`SCENARIO_UNSPECIFIED` | Default value. This value is unused.  
`CREATE` | The validation check occurred during a create flow.  
`UPDATE` | The validation check occurred during an update flow.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
