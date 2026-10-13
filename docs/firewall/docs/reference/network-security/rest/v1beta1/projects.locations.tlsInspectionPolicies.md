---
url: https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1beta1/projects.locations.tlsInspectionPolicies
title: REST Resource: projects.locations.tlsInspectionPolicies \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:53.407150+00:00
---

# REST Resource: projects.locations.tlsInspectionPolicies  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1beta1/projects.locations.tlsInspectionPolicies

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Reference ](https://docs.cloud.google.com/firewall/docs/apis)



Send feedback 

#  REST Resource: projects.locations.tlsInspectionPolicies Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: TlsInspectionPolicy

The TlsInspectionPolicy resource contains references to CA pools in Certificate Authority Service and associated metadata.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "caPool": string,
      "trustConfig": string,
      "minTlsVersion": enum ([TlsVersion](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1beta1/projects.locations.tlsInspectionPolicies#TlsVersion)),
      "tlsFeatureProfile": enum ([Profile](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1beta1/projects.locations.tlsInspectionPolicies#Profile)),
      "customTlsFeatures": [
        string
      ],
      "excludePublicCaSet": boolean
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the resource. Name is of the form projects/{project}/locations/{location}/tlsInspectionPolicies/{tlsInspectionPolicy} tlsInspectionPolicy should match the pattern:(^[a-z](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1beta1/\[a-z0-9-\]{0,61}\[a-z0-9\])?$).  
`description` |  `string` Optional. Free-text description of the resource.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`caPool` |  `string` Required. A CA pool resource used to issue interception certificates. The CA pool string has a relative resource path following the form "projects/{project}/locations/{location}/caPools/{caPool}".  
`trustConfig` |  `string` Optional. A TrustConfig resource used when making a connection to the TLS server. This is a relative resource path following the form "projects/{project}/locations/{location}/trustConfigs/{trustConfig}". This is necessary to intercept TLS connections to servers with certificates signed by a private CA or self-signed certificates. Note that Secure Web Proxy does not yet honor this field.  
`minTlsVersion` |  `enum (`[TlsVersion](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1beta1/projects.locations.tlsInspectionPolicies#TlsVersion)`)` Optional. Minimum TLS version that the firewall should use when negotiating connections with both clients and servers. If this is not set, then the default value is to allow the broadest set of clients and servers (TLS 1.0 or higher). Setting this to more restrictive values may improve security, but may also prevent the firewall from connecting to some clients or servers. Note that Secure Web Proxy does not yet honor this field.  
`tlsFeatureProfile` |  `enum (`[Profile](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1beta1/projects.locations.tlsInspectionPolicies#Profile)`)` Optional. The selected Profile. If this is not set, then the default value is to allow the broadest set of clients and servers ("PROFILE_COMPATIBLE"). Setting this to more restrictive values may improve security, but may also prevent the TLS inspection proxy from connecting to some clients or servers. Note that Secure Web Proxy does not yet honor this field.  
`customTlsFeatures[]` |  `string` Optional. List of custom TLS cipher suites selected. This field is valid only if the selected tlsFeatureProfile is CUSTOM. The [compute.SslPoliciesService.ListAvailableFeatures][] method returns the set of features that can be specified in this list. Note that Secure Web Proxy does not yet honor this field.  
`excludePublicCaSet` |  `boolean` Optional. If FALSE (the default), use our default set of public CAs in addition to any CAs specified in trustConfig. These public CAs are currently based on the Mozilla Root Program and are subject to change over time. If TRUE, do not accept our default set of public CAs. Only CAs specified in trustConfig will be accepted. This defaults to FALSE (use public CAs in addition to trustConfig) for backwards compatibility, but trusting public root CAs is _not recommended_ unless the traffic in question is outbound to public web servers. When possible, prefer setting this to "false" and explicitly specifying trusted CAs and certificates in a TrustConfig. Note that Secure Web Proxy does not yet honor this field.  
  
## TlsVersion

The minimum version of TLS protocol that can be used by clients or servers to establish a connection with the TLS inspection proxy.

Enums  
---  
`TLS_VERSION_UNSPECIFIED` | Indicates no TLS version was specified.  
`TLS_1_0` | TLS 1.0  
`TLS_1_1` | TLS 1.1  
`TLS_1_2` | TLS 1.2  
`TLS_1_3` | TLS 1.3  
  
## Profile

Profile specifies the set of TLS cipher suites (and possibly other features in the future) that can be used by the firewall when negotiating TLS connections with clients and servers. The meaning of these fields is identical to the load balancers' SSLPolicy resource.

Enums  
---  
`PROFILE_UNSPECIFIED` | Indicates no profile was specified.  
`PROFILE_COMPATIBLE` | Compatible profile. Allows the broadest set of clients, even those which support only out-of-date SSL features to negotiate with the TLS inspection proxy.  
`PROFILE_MODERN` | Modern profile. Supports a wide set of SSL features, allowing modern clients to negotiate SSL with the TLS inspection proxy.  
`PROFILE_RESTRICTED` | Restricted profile. Supports a reduced set of SSL features, intended to meet stricter compliance requirements.  
`PROFILE_CUSTOM` | Custom profile. Allow only the set of allowed SSL features specified in the custom_features field of SslPolicy.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1beta1/projects.locations.tlsInspectionPolicies/create)`

|  Creates a new TlsInspectionPolicy in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1beta1/projects.locations.tlsInspectionPolicies/delete)`

|  Deletes a single TlsInspectionPolicy.  
  
### `[get](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1beta1/projects.locations.tlsInspectionPolicies/get)`

|  Gets details of a single TlsInspectionPolicy.  
  
### `[list](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1beta1/projects.locations.tlsInspectionPolicies/list)`

|  Lists TlsInspectionPolicies in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1beta1/projects.locations.tlsInspectionPolicies/patch)`

|  Updates the parameters of a single TlsInspectionPolicy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-24 UTC."],[],[]] 
