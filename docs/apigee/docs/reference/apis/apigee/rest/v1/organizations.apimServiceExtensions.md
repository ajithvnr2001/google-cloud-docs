---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions
title: REST Resource: organizations.apimServiceExtensions \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:16.802490+00:00
---

# REST Resource: organizations.apimServiceExtensions  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.apimServiceExtensions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ApimServiceExtension
    * JSON representation
  * NetworkConfig
    * JSON representation
  * Extension
    * JSON representation
  * SupportedEvent
  * Methods



## Resource: ApimServiceExtension

APIM Service Extension is a resource under an Apigee Organization that is used to create APIM Service Extension to route traffic to existing X instances.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "lbForwardingRule": string,
      "network": string,
      "networkConfigs": [
        {
          object ([NetworkConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions#NetworkConfig))
        }
      ],
      "extensions": [
        {
          object ([Extension](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions#Extension))
        }
      ],
      "state": enum (State),
      "extensionProcessor": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. unique name of the APIM service extension. The name must conform with RFC-1034, is restricted to lower-cased letters, numbers and hyphens, and can have a maximum length of 63 characters. Additionally, the first character must be a letter and the last a letter or a number.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time that this resource was created on the server.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time that this resource was updated on the server.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lbForwardingRule` |  `string` Required. Name of the Google Cloud LB forwarding rule. Format: projects/{project}/regions/{region}/forwardingRules/{forwardingRule} projects/{project}/global/forwardingRules/{forwardingRule}  
`network` |  `string` Required. The network where the forwarding rule is created. Format: projects/{project}/global/networks/{network}  
`networkConfigs[]` |  `object (`[NetworkConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions#NetworkConfig)`)` Required. List of network configurations for the APIM service extension.  
`extensions[]` |  `object (`[Extension](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions#Extension)`)` Optional. List of extensions that are part of the service extension. Refer to <https://cloud.google.com/service-extensions/docs/quotas#limits> for any limits.  
`state` |  `enum (`State`)` Output only. State of the APIM service extension. Values other than `ACTIVE` mean the resource is not ready to use.  
`extensionProcessor` |  `string` Required. Name of the proxy deployed in the Apigee X instance.  
  
## NetworkConfig

Network configuration for the APIM service extension.

JSON representation  
---  
      
    
    {
      "region": string,
      "subnet": string
    }  
  
Fields  
---  
`region` |  `string` Required. The region for the PSC NEG.  
`subnet` |  `string` Required. The subnet for the PSC NEG. Format: projects/{project}/regions/{region}/subnetworks/{subnet}  
  
## Extension

Extension configuration for Apigee extension processor service extension.

JSON representation  
---  
      
    
    {
      "name": string,
      "matchCondition": string,
      "failOpen": boolean,
      "hostname": string,
      "supportedEvents": [
        enum ([SupportedEvent](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions#SupportedEvent))
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the `LbTrafficExtension` resource. The name must conform with RFC-1034, is restricted to lower-cased letters, numbers and hyphens, and can have a maximum length of 63 characters. Additionally, the first character must be a letter and the last a letter or a number.  
`matchCondition` |  `string` Optional. Match Condition for CEL expression. Refer to <https://cloud.google.com/service-extensions/docs/cel-matcher-language-reference> for more details.  
`failOpen` |  `boolean` Optional. Whether this request should fail open.  
`hostname` |  `string` Required. One of the hostnames of Apigee EnvGroup where the proxy is deployed. This hostname (i.e FDQN) will be used to route traffic from the specified forwarding rule to the environment in Apigee X instance where the proxy is deployed for handling extension traffic. Format: ^([a-zA-Z0-9. _-])+$  
`supportedEvents[]` |  `enum (`[SupportedEvent](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions#SupportedEvent)`)` Optional. Supported events for the Service Extension. If not specified, all events are supported.  
  
## SupportedEvent

Supported event for the Service Extension.

Enums  
---  
`SUPPORTED_EVENT_UNSPECIFIED` | Unspecified event.  
`REQUEST_HEADERS` | Request headers event.  
`REQUEST_BODY` | Request body event.  
`RESPONSE_HEADERS` | Response headers event.  
`RESPONSE_BODY` | Response body event.  
`REQUEST_TRAILERS` | Request trailers event.  
`RESPONSE_TRAILERS` | Response trailers event.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions/create)`

|  Creates an APIM ServiceExtension in an organization.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions/delete)`

|  Deletes APIM service extension from an organization.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions/get)`

|  Gets APIM service extension details.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions/list)`

|  Lists all APIM service extensions in an organization.  
  
### `[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apimServiceExtensions/patch)`

|  Updates an APIM service extension in an organization.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
