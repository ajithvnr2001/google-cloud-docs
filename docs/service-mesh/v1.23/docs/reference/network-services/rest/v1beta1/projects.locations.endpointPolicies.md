---
url: https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies
title: REST Resource: projects.locations.endpointPolicies \u00a0|\u00a0 Cloud Service Mesh v1.23 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:01.772535+00:00
---

# REST Resource: projects.locations.endpointPolicies  |  Cloud Service Mesh v1.23  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies

You are viewing archived v1.23 Service Mesh documentation.

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
  * [ v1.23 ](https://docs.cloud.google.com/service-mesh/v1.23/docs)



Send feedback 

#  REST Resource: projects.locations.endpointPolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EndpointPolicy
    * JSON representation
  * EndpointPolicyType
  * EndpointMatcher
    * JSON representation
  * MetadataLabelMatcher
    * JSON representation
  * MetadataLabelMatchCriteria
  * MetadataLabels
    * JSON representation
  * TrafficPortSelector
    * JSON representation
  * Methods



## Resource: EndpointPolicy

EndpointPolicy is a resource that helps apply desired configuration on the endpoints that match specific criteria. For example, this resource can be used to apply "authentication config" an all endpoints that serve on port 8080.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "type": enum ([EndpointPolicyType](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies#EndpointPolicyType)),
      "authorizationPolicy": string,
      "endpointMatcher": {
        object ([EndpointMatcher](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies#EndpointMatcher))
      },
      "trafficPortSelector": {
        object ([TrafficPortSelector](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies#TrafficPortSelector))
      },
      "description": string,
      "serverTlsPolicy": string,
      "clientTlsPolicy": string
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the EndpointPolicy resource. It matches pattern `projects/{project}/locations/global/endpointPolicies/{endpointPolicy}`.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The timestamp when the resource was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The timestamp when the resource was updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`labels` |  `map (key: string, value: string)` Optional. Set of label tags associated with the EndpointPolicy resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`type` |  `enum (`[EndpointPolicyType](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies#EndpointPolicyType)`)` Required. The type of endpoint policy. This is primarily used to validate the configuration.  
`authorizationPolicy` |  `string` Optional. This field specifies the URL of AuthorizationPolicy resource that applies authorization policies to the inbound traffic at the matched endpoints. Refer to Authorization. If this field is not specified, authorization is disabled(no authz checks) for this endpoint.  
`endpointMatcher` |  `object (`[EndpointMatcher](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies#EndpointMatcher)`)` Required. A matcher that selects endpoints to which the policies should be applied.  
`trafficPortSelector` |  `object (`[TrafficPortSelector](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies#TrafficPortSelector)`)` Optional. Port selector for the (matched) endpoints. If no port selector is provided, the matched config is applied to all ports.  
`description` |  `string` Optional. A free-text description of the resource. Max length 1024 characters.  
`serverTlsPolicy` |  `string` Optional. A URL referring to ServerTlsPolicy resource. ServerTlsPolicy is used to determine the authentication policy to be applied to terminate the inbound traffic at the identified backends. If this field is not set, authentication is disabled(open) for this endpoint.  
`clientTlsPolicy` |  `string` Optional. A URL referring to a ClientTlsPolicy resource. ClientTlsPolicy can be set to specify the authentication for traffic from the proxy to the actual endpoints. More specifically, it is applied to the outgoing traffic from the proxy to the endpoint. This is typically used for sidecar model where the proxy identifies itself as endpoint to the control plane, with the connection between sidecar and endpoint requiring authentication. If this field is not set, authentication is disabled(open). Applicable only when EndpointPolicyType is SIDECAR_PROXY.  
  
## EndpointPolicyType

The type of endpoint policy.

Enums  
---  
`ENDPOINT_POLICY_TYPE_UNSPECIFIED` | Default value. Must not be used.  
`SIDECAR_PROXY` | Represents a proxy deployed as a sidecar.  
`GRPC_SERVER` | Represents a proxyless gRPC backend.  
  
## EndpointMatcher

A definition of a matcher that selects endpoints to which the policies should be applied.

JSON representation  
---  
      
    
    {
    
      // Union field matcher_type can be only one of the following:
      "metadataLabelMatcher": {
        object ([MetadataLabelMatcher](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies#MetadataLabelMatcher))
      }
      // End of list of possible types for union field matcher_type.
    }  
  
Fields  
---  
Union field `matcher_type`. Specifies type of the matcher used for this endpoint matcher. `matcher_type` can be only one of the following:  
`metadataLabelMatcher` |  `object (`[MetadataLabelMatcher](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies#MetadataLabelMatcher)`)` The matcher is based on node metadata presented by xDS clients.  
  
## MetadataLabelMatcher

The matcher that is based on node metadata presented by xDS clients.

JSON representation  
---  
      
    
    {
      "metadataLabelMatchCriteria": enum ([MetadataLabelMatchCriteria](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies#MetadataLabelMatchCriteria)),
      "metadataLabels": [
        {
          object ([MetadataLabels](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies#MetadataLabels))
        }
      ]
    }  
  
Fields  
---  
`metadataLabelMatchCriteria` |  `enum (`[MetadataLabelMatchCriteria](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies#MetadataLabelMatchCriteria)`)` Specifies how matching should be done.Supported values are: MATCH_ANY: At least one of the Labels specified in the matcher should match the metadata presented by xDS client. MATCH_ALL: The metadata presented by the xDS client should contain all of the labels specified here.The selection is determined based on the best match. For example, suppose there are three EndpointPolicy resources P1, P2 and P3 and if P1 has a the matcher as MATCH_ANY <A:1, B:1>, P2 has MATCH_ALL <A:1,B:1>, and P3 has MATCH_ALL <A:1,B:1,C:1>.If a client with label <A:1> connects, the config from P1 will be selected.If a client with label <A:1,B:1> connects, the config from P2 will be selected.If a client with label <A:1,B:1,C:1> connects, the config from P3 will be selected.If there is more than one best match, (for example, if a config P4 with selector <A:1,D:1> exists and if a client with label <A:1,B:1,D:1> connects), pick up the one with older creation time.  
`metadataLabels[]` |  `object (`[MetadataLabels](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies#MetadataLabels)`)` The list of label value pairs that must match labels in the provided metadata based on filterMatchCriteria This list can have at most 64 entries. The list can be empty if the match criteria is MATCH_ANY, to specify a wildcard match (i.e this matches any client).  
  
## MetadataLabelMatchCriteria

Possible criteria values that define logic of how matching is made.

Enums  
---  
`METADATA_LABEL_MATCH_CRITERIA_UNSPECIFIED` | Default value. Should not be used.  
`MATCH_ANY` | At least one of the Labels specified in the matcher should match the metadata presented by xDS client.  
`MATCH_ALL` | The metadata presented by the xDS client should contain all of the labels specified here.  
  
## MetadataLabels

Defines a name-pair value for a single label.

JSON representation  
---  
      
    
    {
      "labelName": string,
      "labelValue": string
    }  
  
Fields  
---  
`labelName` |  `string` Required. Label name presented as key in xDS Node Metadata.  
`labelValue` |  `string` Required. Label value presented as value corresponding to the above key, in xDS Node Metadata.  
  
## TrafficPortSelector

Specification of a port-based selector.

JSON representation  
---  
      
    
    {
      "ports": [
        string
      ]
    }  
  
Fields  
---  
`ports[]` |  `string` Optional. A list of ports. Can be port numbers or port range (example, [80-90] specifies all ports from 80 to 90, including 80 and 90) or named ports or * to specify all ports. If the list is empty, all ports are selected.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies/create)`

|  Creates a new EndpointPolicy in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies/delete)`

|  Deletes a single EndpointPolicy.  
  
### `[get](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies/get)`

|  Gets details of a single EndpointPolicy.  
  
### `[getIamPolicy](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies/list)`

|  Lists EndpointPolicies in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies/patch)`

|  Updates the parameters of a single EndpointPolicy.  
  
### `[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.23/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-18 UTC."],[],[]] 
