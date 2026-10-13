---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.sessions.entityTypes/create/
title: Method: projects.agent.sessions.entityTypes.create \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:44.952284+00:00
---

# Method: projects.agent.sessions.entityTypes.create  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.sessions.entityTypes/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Method: projects.agent.sessions.entityTypes.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates a session entity type.

If the specified session entity type already exists, overrides the session entity type.

This method doesn't work with Google Assistant integration. Contact Dialogflow support if you need to use session entities with Google Assistant integration.

### HTTP request

`POST https://{endpoint}/v2beta1/{parent=projects/*/agent/sessions/*}/entityTypes`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The session to create a session entity type for. Supported formats: - `projects/<Project ID>/agent/sessions/<Session ID>, -`projects//locations//agent/sessions/`, -`projects//agent/environments//users//sessions/`, -`projects//locations//agent/environments//users//sessions/`,If `Location ID` is not specified we assume default 'us' location. If `Environment ID` is not specified, we assume default 'draft' environment. If `User ID` is not specified, we assume default '-' user. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dialogflow.sessionEntityTypes.create`

  
  
### Request body

The request body contains an instance of `[SessionEntityType](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.environments.users.sessions.entityTypes#SessionEntityType)`.

### Response body

If successful, the response body contains a newly created instance of `[SessionEntityType](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.environments.users.sessions.entityTypes#SessionEntityType)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
