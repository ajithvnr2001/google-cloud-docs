---
url: https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.endpoints
title: REST Resource: projects.locations.endpoints \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:33.026082+00:00
---

# REST Resource: projects.locations.endpoints  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.endpoints

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  REST Resource: projects.locations.endpoints Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Endpoint
    * JSON representation
  * Methods



## Resource: Endpoint

Represents an Endpoint.

JSON representation  
---  
      
    
    {
      "name": string,
      "endpointId": string,
      "displayName": string,
      "description": string,
      "interfaces": [
        {
          object ([Interface](https://docs.cloud.google.com/agent-registry/reference/rest/v1/Interface))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "attributes": {
        string: {
          object
        },
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the Endpoint. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`.  
`endpointId` |  `string` Output only. A stable, globally unique identifier for Endpoint.  
`displayName` |  `string` Output only. Display name for the Endpoint.  
`description` |  `string` Output only. Description of an Endpoint.  
`interfaces[]` |  `object (`[Interface](https://docs.cloud.google.com/agent-registry/reference/rest/v1/Interface)`)` Required. The connection details for the Endpoint.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`attributes` |  `map (key: string, value: object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format))` Output only. Attributes of the Endpoint.Valid values:

  * `agentregistry.googleapis.com/system/RuntimeReference`: {"uri": "//..."} - the URI of the underlying resource hosting the Endpoint, for example, the GKE Deployment.

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.endpoints/get)`

|  Gets details of a single Endpoint.  
  
### `[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.endpoints/list)`

|  Lists Endpoints in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-24 UTC."],[],[]] 
