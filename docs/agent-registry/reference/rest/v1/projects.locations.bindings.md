---
url: https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings
title: REST Resource: projects.locations.bindings \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:35.368809+00:00
---

# REST Resource: projects.locations.bindings  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  REST Resource: projects.locations.bindings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Binding
    * JSON representation
  * AuthProviderBinding
    * JSON representation
  * Source
    * JSON representation
  * Target
    * JSON representation
  * Methods



## Resource: Binding

Represents a user-defined Binding.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "source": {
        object ([Source](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings#Source))
      },
      "target": {
        object ([Target](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings#Target))
      },
      "createTime": string,
      "updateTime": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "authProviderBinding": {
        object ([AuthProviderBinding](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings#AuthProviderBinding))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Required. Identifier. The resource name of the Binding. Format: `projects/{project}/locations/{location}/bindings/{binding}`.  
`displayName` |  `string` Optional. User-defined display name for the Binding. Can have a maximum length of `63` characters.  
`description` |  `string` Optional. User-defined description of a Binding. Can have a maximum length of `2048` characters.  
`source` |  `object (`[Source](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings#Source)`)` Optional. The source Agent of the Binding.  
`target` |  `object (`[Target](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings#Target)`)` Required. The target Agent Registry Resource of the Binding.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when this binding was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when this binding was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
The configuration for the Binding. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`authProviderBinding` |  `object (`[AuthProviderBinding](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings#AuthProviderBinding)`)` The binding for AuthProvider.  
End of mutually exclusive fields.  
  
## AuthProviderBinding

The AuthProvider of the Binding.

JSON representation  
---  
      
    
    {
      "authProvider": string,
      "scopes": [
        string
      ],
      "continueUri": string
    }  
  
Fields  
---  
`authProvider` |  `string` Required. The resource name of the target AuthProvider. Format:

  * `projects/{project}/locations/{location}/authProviders/{authProvider}`

  
`scopes[]` |  `string` Optional. The list of OAuth2 scopes of the AuthProvider.  
`continueUri` |  `string` Optional. The continue URI of the AuthProvider. The URI is used to reauthenticate the user and finalize the managed OAuth flow.  
  
## Source

The source of the Binding.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "identifier": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The type of the source, currently only supports Agents. Potential future fields include 'tag', etc. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`identifier` |  `string` The identifier of the source Agent. Format:

  * `urn:agent:{publisher}:{namespace}:{name}`

  
End of mutually exclusive fields.  
  
## Target

The target of the Binding.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "identifier": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The type of the target, currently only supports an AgentRegistry Resource. Potential future fields include 'tag', etc. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`identifier` |  `string` The identifier of the target Agent, MCP Server, or Endpoint. Format:

  * `urn:agent:{publisher}:{namespace}:{name}`
  * `urn:mcp:{publisher}:{namespace}:{name}`
  * `urn:endpoint:{publisher}:{namespace}:{name}`

  
End of mutually exclusive fields.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings/create)`

|  Creates a new Binding in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings/delete)`

|  Deletes a single Binding.  
  
### `[fetchAvailable](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings/fetchAvailable)`

|  Fetches available Bindings.  
  
### `[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings/get)`

|  Gets details of a single Binding.  
  
### `[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings/list)`

|  Lists Bindings in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings/patch)`

|  Updates the parameters of a single Binding.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
