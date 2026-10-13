---
url: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.ServerTlsPolicy
title: Class ServerTlsPolicy (0.13.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:38.018694+00:00
---

# Class ServerTlsPolicy (0.13.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.ServerTlsPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ServerTlsPolicy (0.13.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.4 (latest)  0.13.3  0.12.0  0.11.0  0.10.0  0.9.21  0.8.0  0.7.2  0.6.1  0.5.0  0.4.2  0.3.2  0.2.0  0.1.5 
    
    
    ServerTlsPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

ServerTlsPolicy is a resource that specifies how a server should authenticate incoming requests. This resource itself does not affect configuration unless it is attached to a target HTTPS proxy or endpoint config selector resource.

ServerTlsPolicy in the form accepted by Application Load Balancers can be attached only to TargetHttpsProxy with an `EXTERNAL`, `EXTERNAL_MANAGED` or `INTERNAL_MANAGED` load balancing scheme. Traffic Director compatible ServerTlsPolicies can be attached to EndpointPolicy and TargetHttpsProxy with Traffic Director `INTERNAL_SELF_MANAGED` load balancing scheme.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. Name of the ServerTlsPolicy resource. It matches the pattern `projects/*/locations/{location}/serverTlsPolicies/{server_tls_policy}`  
`description` |  `str`   
Free-text description of the resource.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp when the resource was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp when the resource was updated.   
`labels` |  `MutableMapping[str, str]`   
Set of label tags associated with the resource.   
`allow_open` |  `bool`   
This field applies only for Traffic Director policies. It is must be set to false for Application Load Balancer policies. Determines if server allows plaintext connections. If set to true, server allows plain text connections. By default, it is set to false. This setting is not exclusive of other encryption modes. For example, if `allow_open` and `mtls_policy` are set, server allows both plain text and mTLS connections. See documentation of other encryption modes to confirm compatibility. Consider using it if you wish to upgrade in place your deployment to TLS while having mixed TLS and non-TLS traffic reaching port :80.   
`server_certificate` |  `[google.cloud.network_security_v1.types.CertificateProvider](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.CertificateProvider)`   
Optional if policy is to be used with Traffic Director. For Application Load Balancers must be empty. Defines a mechanism to provision server identity (public and private keys). Cannot be combined with `allow_open` as a permissive mode that allows both plain text and TLS is not supported.   
`mtls_policy` |  `[google.cloud.network_security_v1.types.ServerTlsPolicy.MTLSPolicy](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.ServerTlsPolicy.MTLSPolicy)`   
This field is required if the policy is used with Application Load Balancers. This field can be empty for Traffic Director. Defines a mechanism to provision peer validation certificates for peer to peer authentication (Mutual TLS - mTLS). If not specified, client certificate will not be requested. The connection is treated as TLS and not mTLS. If `allow_open` and `mtls_policy` are set, server allows both plain text and mTLS connections.   
  
## Classes 

### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### MTLSPolicy
    
    
    MTLSPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Specification of the MTLSPolicy.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
