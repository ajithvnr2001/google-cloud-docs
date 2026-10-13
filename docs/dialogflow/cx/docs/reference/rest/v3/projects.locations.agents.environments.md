---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments
title: REST Resource: projects.locations.agents.environments \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:01.224356+00:00
---

# REST Resource: projects.locations.agents.environments  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents.environments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Environment
    * JSON representation
  * VersionConfig
    * JSON representation
  * TestCasesConfig
    * JSON representation
  * WebhookConfig
    * JSON representation
  * Methods



## Resource: Environment

Represents an environment for an agent. You can create multiple versions of your agent and publish them to separate environments. When you edit an agent, you are editing the draft agent. At any point, you can save the draft agent as an agent version, which is an immutable snapshot of your agent. When you save the draft agent, it is published to the default environment. When you create agent versions, you can publish them to custom environments. You can create a variety of custom environments for testing, development, production, etc.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "versionConfigs": [
        {
          object ([VersionConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#VersionConfig))
        }
      ],
      "updateTime": string,
      "testCasesConfig": {
        object ([TestCasesConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#TestCasesConfig))
      },
      "webhookConfig": {
        object ([WebhookConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#WebhookConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` The name of the environment. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>`.  
`displayName` |  `string` Required. The human-readable name of the environment (unique in an agent). Limit of 64 characters.  
`description` |  `string` The human-readable description of the environment. The maximum length is 500 characters. If exceeded, the request is rejected.  
`versionConfigs[]` |  `object (`[VersionConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#VersionConfig)`)` A list of configurations for flow versions. You should include version configs for all flows that are reachable from [`Start Flow`][Agent.start_flow] in the agent. Otherwise, an error will be returned.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time of this environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`testCasesConfig` |  `object (`[TestCasesConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#TestCasesConfig)`)` The test cases config for continuous tests of this environment.  
`webhookConfig` |  `object (`[WebhookConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#WebhookConfig)`)` The webhook configuration for this environment.  
  
## VersionConfig

Configuration for the version.

JSON representation  
---  
      
    
    {
      "version": string
    }  
  
Fields  
---  
`version` |  `string` Required. Flow, playbook and tool versions are supported. Format for flow version: projects//locations//agents//flows//versions/. Format for playbook version: projects//locations//agents//playbooks//versions/. Format for tool version: projects//locations//agents//tools//versions/.  
  
## TestCasesConfig

The configuration for continuous tests.

JSON representation  
---  
      
    
    {
      "testCases": [
        string
      ],
      "enableContinuousRun": boolean,
      "enablePredeploymentRun": boolean
    }  
  
Fields  
---  
`testCases[]` |  `string` A list of test case names to run. They should be under the same agent. Format of each test case name: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/testCases/<TestCaseID>`  
`enableContinuousRun` |  `boolean` Whether to run test cases in `[TestCasesConfig.test_cases](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#TestCasesConfig.FIELDS.test_cases)` periodically. Default false. If set to true, run once a day.  
`enablePredeploymentRun` |  `boolean` Whether to run test cases in `[TestCasesConfig.test_cases](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#TestCasesConfig.FIELDS.test_cases)` before deploying a flow version to the environment. Default false.  
  
## WebhookConfig

Configuration for webhooks.

JSON representation  
---  
      
    
    {
      "webhookOverrides": [
        {
          object ([Webhook](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook))
        }
      ]
    }  
  
Fields  
---  
`webhookOverrides[]` |  `object (`[Webhook](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook)`)` The list of webhooks to override for the agent environment. The webhook must exist in the agent. You can override fields in `[`genericWebService`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.FIELDS.generic_web_service)` and `[`serviceDirectory`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook.FIELDS.service_directory)`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments/create)`

|  Creates an `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)` in the specified `[Agent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#Agent)`.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments/delete)`

|  Deletes the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
  
### `[deployFlow](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments/deployFlow)`

|  Deploys a flow to the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments/get)`

|  Retrieves the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments/list)`

|  Returns the list of all environments in the specified `[Agent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#Agent)`.  
  
### `[lookupEnvironmentHistory](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments/lookupEnvironmentHistory)`

|  Looks up the history of the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments/patch)`

|  Updates the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
  
### `[runContinuousTest](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments/runContinuousTest)`

|  Kicks off a continuous test under the specified `[Environment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments#Environment)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-21 UTC."],[],[]] 
