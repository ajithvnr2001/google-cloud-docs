---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.deployments
title: REST Resource: projects.locations.agents.environments.deployments \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:02.500907+00:00
---

# REST Resource: projects.locations.agents.environments.deployments  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.deployments

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents.environments.deployments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Deployment
    * JSON representation
  * State
  * Result
    * JSON representation
  * Methods



## Resource: Deployment

Represents a deployment in an environment. A deployment happens when a flow version configured to be active in the environment. You can configure running pre-deployment steps, e.g. running validation test cases, experiment auto-rollout, etc.

JSON representation  
---  
      
    
    {
      "name": string,
      "flowVersion": string,
      "state": enum ([State](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.deployments#State)),
      "result": {
        object ([Result](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.deployments#Result))
      },
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`name` |  `string` The name of the deployment. Format: projects//locations//agents//environments//deployments/.  
`flowVersion` |  `string` The name of the flow version for this deployment. Format: projects//locations//agents//flows//versions/.  
`state` |  `enum (`[State](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.deployments#State)`)` The current state of the deployment.  
`result` |  `object (`[Result](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.deployments#Result)`)` Result of the deployment.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Start time of this deployment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` End time of this deployment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## State

The state of the deployment.

Enums  
---  
`STATE_UNSPECIFIED` | State unspecified.  
`RUNNING` | The deployment is running.  
`SUCCEEDED` | The deployment succeeded.  
`FAILED` | The deployment failed.  
  
## Result

Result of the deployment.

JSON representation  
---  
      
    
    {
      "deploymentTestResults": [
        string
      ],
      "experiment": string
    }  
  
Fields  
---  
`deploymentTestResults[]` |  `string` Results of test cases running before the deployment. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/testCases/<TestCaseID>/results/<TestCaseResultID>`.  
`experiment` |  `string` The name of the experiment triggered by this deployment. Format: projects//locations//agents//environments//experiments/.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.deployments/get)`

|  Retrieves the specified `[Deployment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.deployments#Deployment)`.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.deployments/list)`

|  Returns the list of all deployments in the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-21 UTC."],[],[]] 
