---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations/fetchRestrictedAgents/
title: Method: integrations.fetchRestrictedAgents \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:33.161567+00:00
---

# Method: integrations.fetchRestrictedAgents  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations/fetchRestrictedAgents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: integrations.fetchRestrictedAgents Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.integrations.fetchRestrictedAgents

Identifies remote agents that would be restricted from running an updated version of the integration, typically due to environment incompatibilities like unsupported Python versions.

### HTTP request

`GET https://{endpoint}/v1beta/{name}:fetchRestrictedAgents`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The unique name of the integration. Format: projects/{project}/locations/{location}/instances/{instance}/integrations/{integration}  
  
### Query parameters

Parameters  
---  
`requiredPythonVersion` |  `enum (`[PythonVersion](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.integrations#PythonVersion)`)` Required. Python version required for the updated integration. Query parameter.  
`pushRequest` |  `boolean` Optional. Indicates whether the integration is pushed to a different mode (production/staging). False by default. Query parameter.  
  
### Request body

The request body must be empty.

### Response body

Response message for geting the restricted agents for an integration update.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "agents": [
        string
      ]
    }  
  
Fields  
---  
`agents[]` |  `string` Output only. Agents display names blocklist for the integration update.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.integrations.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
