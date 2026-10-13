---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remoteAgents/list/
title: Method: remoteAgents.list \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:57:30.009491+00:00
---

# Method: remoteAgents.list  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remoteAgents/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: remoteAgents.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.remoteAgents.list

Lists RemoteAgents. Use this method to browse all configured remote agents and their current states. Supports filtering by name, identifier, state, or environments. Note that deleted agents are not included in the response.

### HTTP request

`GET https://{endpoint}/v1alpha/{parent}/remoteAgents`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent, which owns this collection of remote agents. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of remote agents to return. The service may return fewer than this value. If unspecified, at most 100 remote agents will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `remoteAgents.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `remoteAgents.list` must match the call that provided the page token.  
`filter` |  `string` Optional. Filter to be applied over multiple remote Agent fields. Only the following filters are allowed: name, identifier, state, environments, logging level, primary remote agent identifier, display name.  
`orderBy` |  `string` Optional. Configures ordering of remote agents in the response. If not specified, remote agents are returned in descending order of their create time. The default ordering is by create time in descending order. The orderBy string is a comma separated list of fields. For example: "createTime desc, updateTime" Supported fields: * `order` * `displayName`  
  
### Request body

The request body must be empty.

### Response body

ListRemoteAgentsResponse contains the list of remote agents.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "remoteAgents": [
        {
          object ([RemoteAgent](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remoteAgents#RemoteAgent))
        }
      ],
      "totalSize": integer,
      "nextPageToken": string
    }  
  
Fields  
---  
`remoteAgents[]` |  `object (`[RemoteAgent](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remoteAgents#RemoteAgent)`)` Output only. The list of remote agents, ordered by displayName.  
`totalSize` |  `integer` Output only. The total number of remote agents.  
`nextPageToken` |  `string` Output only. A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.remoteAgents.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
