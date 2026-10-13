---
url: https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies
title: REST Resource: projects.locations.gatewaySecurityPolicies \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:13.737490+00:00
---

# REST Resource: projects.locations.gatewaySecurityPolicies  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Reference ](https://docs.cloud.google.com/secure-web-proxy/docs/apis)



Send feedback 

#  REST Resource: projects.locations.gatewaySecurityPolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GatewaySecurityPolicy
    * JSON representation
  * Methods



## Resource: GatewaySecurityPolicy

The GatewaySecurityPolicy resource contains a collection of GatewaySecurityPolicyRules and associated metadata.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "description": string,
      "tlsInspectionPolicy": string
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the resource. Name is of the form projects/{project}/locations/{location}/gatewaySecurityPolicies/{gatewaySecurityPolicy} gatewaySecurityPolicy should match the pattern:(^[a-z](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1beta1/\[a-z0-9-\]{0,61}\[a-z0-9\])?$).  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The timestamp when the resource was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The timestamp when the resource was updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`description` |  `string` Optional. Free-text description of the resource.  
`tlsInspectionPolicy` |  `string` Optional. Name of a TLS Inspection Policy resource that defines how TLS inspection will be performed for any rule(s) which enables it.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies/create)`

|  Creates a new GatewaySecurityPolicy in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies/delete)`

|  Deletes a single GatewaySecurityPolicy.  
  
### `[get](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies/get)`

|  Gets details of a single GatewaySecurityPolicy.  
  
### `[list](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies/list)`

|  Lists GatewaySecurityPolicies in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies/patch)`

|  Updates the parameters of a single GatewaySecurityPolicy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
