---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways
title: REST Resource: projects.locations.securityGateways \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:10.726902+00:00
---

# REST Resource: projects.locations.securityGateways  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Reference ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference)



Send feedback 

#  REST Resource: projects.locations.securityGateways Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SecurityGateway
    * JSON representation
  * State
  * Hub
    * JSON representation
  * InternetGateway
    * JSON representation
  * ServiceDiscovery
    * JSON representation
  * ApiGateway
    * JSON representation
  * OperationDescriptor
    * JSON representation
  * Methods



## Resource: SecurityGateway

The information about a security gateway resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "displayName": string,
      "externalIps": [
        string
      ],
      "state": enum ([State](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways#State)),
      "hubs": {
        string: {
          object ([Hub](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways#Hub))
        },
        ...
      },
      "delegatingServiceAccount": string,
      "proxyProtocolConfig": {
        object ([ProxyProtocolConfig](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig))
      },
      "serviceDiscovery": {
        object ([ServiceDiscovery](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways#ServiceDiscovery))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the resource.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the resource was last modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`displayName` |  `string` Optional. An arbitrary user-provided name for the SecurityGateway. Cannot exceed 64 characters.  
`externalIps[]` |  `string` Output only. IP addresses that will be used for establishing connection to the endpoints.  
`state` |  `enum (`[State](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways#State)`)` Output only. The operational state of the SecurityGateway.  
`hubs` |  `map (key: string, value: object (`[Hub](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways#Hub)`))` Optional. Map of Hubs that represents regional data path deployment with GCP region as a key.  
`delegatingServiceAccount` |  `string` Output only. Service account used for operations that involve resources in consumer projects.  
`proxyProtocolConfig` |  `object (`[ProxyProtocolConfig](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/ProxyProtocolConfig)`)` Optional. Shared proxy configuration for all apps.  
`serviceDiscovery` |  `object (`[ServiceDiscovery](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways#ServiceDiscovery)`)` Optional. Settings related to the Service Discovery.  
  
## State

Represents the different states of a SecurityGateway.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`CREATING` | SecurityGateway is being created.  
`UPDATING` | SecurityGateway is being updated.  
`DELETING` | SecurityGateway is being deleted.  
`RUNNING` | SecurityGateway is running.  
`DOWN` | SecurityGateway is down and may be restored in the future.  
`ERROR` | SecurityGateway encountered an error and is in an indeterministic state.  
  
## Hub

The Hub message contains information pertaining to the regional data path deployments.

JSON representation  
---  
      
    
    {
      "internetGateway": {
        object ([InternetGateway](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways#InternetGateway))
      }
    }  
  
Fields  
---  
`internetGateway` |  `object (`[InternetGateway](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways#InternetGateway)`)` Optional. Internet Gateway configuration.  
  
## InternetGateway

Represents the Internet Gateway configuration.

JSON representation  
---  
      
    
    {
      "assignedIps": [
        string
      ]
    }  
  
Fields  
---  
`assignedIps[]` |  `string` Output only. List of IP addresses assigned to the Cloud NAT.  
  
## ServiceDiscovery

Settings related to the Service Discovery.

JSON representation  
---  
      
    
    {
      "apiGateway": {
        object ([ApiGateway](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways#ApiGateway))
      }
    }  
  
Fields  
---  
`apiGateway` |  `object (`[ApiGateway](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways#ApiGateway)`)` Required. External API configuration.  
  
## ApiGateway

If Service Discovery is done through API, defines its settings.

JSON representation  
---  
      
    
    {
      "resourceOverride": {
        object ([OperationDescriptor](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways#OperationDescriptor))
      }
    }  
  
Fields  
---  
`resourceOverride` |  `object (`[OperationDescriptor](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways#OperationDescriptor)`)` Required. Enables fetching resource model updates to alter service behavior per Chrome profile.  
  
## OperationDescriptor

API operation descriptor.

JSON representation  
---  
      
    
    {
      "path": string
    }  
  
Fields  
---  
`path` |  `string` Required. Contains the URI path fragment where HTTP request is sent.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways/create)`

|  Creates a new Security Gateway in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways/delete)`

|  Deletes a single SecurityGateway.  
  
### `[get](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways/get)`

|  Gets details of a single SecurityGateway.  
  
### `[getIamPolicy](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways/list)`

|  Lists SecurityGateways in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways/patch)`

|  Updates the parameters of a single SecurityGateway.  
  
### `[setIamPolicy](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/chrome-enterprise-premium/docs/reference/rest/v1/projects.locations.securityGateways/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-02 UTC."],[],[]] 
