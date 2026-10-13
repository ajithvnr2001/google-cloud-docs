---
url: https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies
title: REST Resource: projects.locations.serverTlsPolicies \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:39:47.327023+00:00
---

# REST Resource: projects.locations.serverTlsPolicies  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Reference ](https://docs.cloud.google.com/load-balancing/docs/apis)



Send feedback 

#  REST Resource: projects.locations.serverTlsPolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ServerTlsPolicy
    * JSON representation
  * MTLSPolicy
    * JSON representation
  * ClientValidationMode
  * Methods



## Resource: ServerTlsPolicy

ServerTlsPolicy is a resource that specifies how a server should authenticate incoming requests. This resource itself does not affect configuration unless it is attached to a target HTTPS proxy or endpoint config selector resource.

ServerTlsPolicy in the form accepted by Application Load Balancers can be attached only to TargetHttpsProxy with an `EXTERNAL`, `EXTERNAL_MANAGED` or `INTERNAL_MANAGED` load balancing scheme. Traffic Director compatible ServerTlsPolicies can be attached to EndpointPolicy and TargetHttpsProxy with Traffic Director `INTERNAL_SELF_MANAGED` load balancing scheme.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "mtlsPolicy": {
        object ([MTLSPolicy](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies#MTLSPolicy))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the ServerTlsPolicy resource. It matches the pattern `projects/*/locations/{location}/serverTlsPolicies/{serverTlsPolicy}`  
`description` |  `string` Free-text description of the resource.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Set of label tags associated with the resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`mtlsPolicy` |  `object (`[MTLSPolicy](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies#MTLSPolicy)`)` This field is required if the policy is used with Application Load Balancers. This field can be empty for Traffic Director.Defines a mechanism to provision peer validation certificates for peer to peer authentication (Mutual TLS - mTLS). If not specified, client certificate will not be requested. The connection is treated as TLS and not mTLS. If `allowOpen` and `mtlsPolicy` are set, server allows both plain text and mTLS connections.  
  
## MTLSPolicy

Specification of the MTLSPolicy.

JSON representation  
---  
      
    
    {
      "clientValidationMode": enum ([ClientValidationMode](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies#ClientValidationMode)),
      "clientValidationTrustConfig": string
    }  
  
Fields  
---  
`clientValidationMode` |  `enum (`[ClientValidationMode](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies#ClientValidationMode)`)` When the client presents an invalid certificate or no certificate to the load balancer, the `clientValidationMode` specifies how the client connection is handled.Required if the policy is to be used with the Application Load Balancers. For Traffic Director it must be empty.  
`clientValidationTrustConfig` |  `string` Reference to the TrustConfig from certificatemanager.googleapis.com namespace.If specified, the chain validation will be performed against certificates configured in the given TrustConfig.Allowed only if the policy is to be used with Application Load Balancers.  
  
## ClientValidationMode

Mutual TLS certificate validation mode.

Enums  
---  
`CLIENT_VALIDATION_MODE_UNSPECIFIED` | Not allowed.  
`ALLOW_INVALID_OR_MISSING_CLIENT_CERT` | Allow connection even if certificate chain validation of the client certificate failed or no client certificate was presented. The proof of possession of the private key is always checked if client certificate was presented. This mode requires the backend to implement processing of data extracted from a client certificate to authenticate the peer, or to reject connections if the client certificate fingerprint is missing.  
`REJECT_INVALID` | Require a client certificate and allow connection to the backend only if validation of the client certificate passed.If set, requires a reference to non-empty TrustConfig specified in `clientValidationTrustConfig`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies/create)`

|  Creates a new ServerTlsPolicy in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies/delete)`

|  Deletes a single ServerTlsPolicy.  
  
### `[get](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies/get)`

|  Gets details of a single ServerTlsPolicy.  
  
### `[list](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies/list)`

|  Lists ServerTlsPolicies in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies/patch)`

|  Updates the parameters of a single ServerTlsPolicy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-14 UTC."],[],[]] 
