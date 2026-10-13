---
url: https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies.rules
title: REST Resource: projects.locations.gatewaySecurityPolicies.rules \u00a0|\u00a0 Cloud Service Mesh v1.21 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:57:26.311422+00:00
---

# REST Resource: projects.locations.gatewaySecurityPolicies.rules  |  Cloud Service Mesh v1.21  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies.rules

You are viewing archived v1.21 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.21 ](https://docs.cloud.google.com/service-mesh/v1.21/docs)



Send feedback 

#  REST Resource: projects.locations.gatewaySecurityPolicies.rules Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GatewaySecurityPolicyRule
    * JSON representation
  * BasicProfile
  * Methods



## Resource: GatewaySecurityPolicyRule

The GatewaySecurityPolicyRule resource is in a nested collection within a GatewaySecurityPolicy and represents a traffic matching condition and associated action to perform.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "enabled": boolean,
      "priority": integer,
      "description": string,
      "sessionMatcher": string,
      "applicationMatcher": string,
      "tlsInspectionEnabled": boolean,
    
      // Union field profile can be only one of the following:
      "basicProfile": enum ([BasicProfile](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies.rules#BasicProfile))
      // End of list of possible types for union field profile.
    }  
  
Fields  
---  
`name` |  `string` Required. Immutable. Name of the resource. ame is the full resource name so projects/{project}/locations/{location}/gatewaySecurityPolicies/{gatewaySecurityPolicy}/rules/{rule} rule should match the pattern: (^[a-z](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/\[a-z0-9-\]{0,61}\[a-z0-9\])?$).  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the rule was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the rule was updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`enabled` |  `boolean` Required. Whether the rule is enforced.  
`priority` |  `integer` Required. Priority of the rule. Lower number corresponds to higher precedence.  
`description` |  `string` Optional. Free-text description of the resource.  
`sessionMatcher` |  `string` Required. CEL expression for matching on session criteria.  
`applicationMatcher` |  `string` Optional. CEL expression for matching on L7/application level criteria.  
`tlsInspectionEnabled` |  `boolean` Optional. Flag to enable TLS inspection of traffic matching on , can only be true if the parent GatewaySecurityPolicy references a TLSInspectionConfig.  
Union field `profile`.`profile` can be only one of the following:  
`basicProfile` |  `enum (`[BasicProfile](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies.rules#BasicProfile)`)` Required. Profile which tells what the primitive action should be.  
  
## BasicProfile

enum to define the primitive action.

Enums  
---  
`BASIC_PROFILE_UNSPECIFIED` | If there is not a mentioned action for the target.  
`ALLOW` | Allow the matched traffic.  
`DENY` | Deny the matched traffic.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies.rules/create)`

|  Creates a new GatewaySecurityPolicy in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies.rules/delete)`

|  Deletes a single GatewaySecurityPolicyRule.  
  
### `[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies.rules/get)`

|  Gets details of a single GatewaySecurityPolicyRule.  
  
### `[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies.rules/list)`

|  Lists GatewaySecurityPolicyRules in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies.rules/patch)`

|  Updates the parameters of a single GatewaySecurityPolicyRule.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-18 UTC."],[],[]] 
