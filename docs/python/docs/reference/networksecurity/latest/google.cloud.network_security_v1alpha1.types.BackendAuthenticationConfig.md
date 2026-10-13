---
url: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.BackendAuthenticationConfig
title: Class BackendAuthenticationConfig (0.13.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:08:52.298525+00:00
---

# Class BackendAuthenticationConfig (0.13.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.BackendAuthenticationConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BackendAuthenticationConfig (0.13.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.4 (latest)  0.13.3  0.12.0  0.11.0  0.10.0  0.9.21  0.8.0  0.7.2  0.6.1  0.5.0  0.4.2  0.3.2  0.2.0  0.1.5 
    
    
    BackendAuthenticationConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

BackendAuthenticationConfig message groups the TrustConfig together with other settings that control how the load balancer authenticates, and expresses its identity to, the backend:

  * `trustConfig` is the attached TrustConfig.

  * `wellKnownRoots` indicates whether the load balance should trust backend server certificates that are issued by public certificate authorities, in addition to certificates trusted by the TrustConfig.

  * `clientCertificate` is a client certificate that the load balancer uses to express its identity to the backend, if the connection to the backend uses mTLS.




You can attach the BackendAuthenticationConfig to the load balancer's BackendService directly determining how that BackendService negotiates TLS.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. Name of the BackendAuthenticationConfig resource. It matches the pattern `projects/*/locations/{location}/backendAuthenticationConfigs/{backend_authentication_config}`  
`description` |  `str`   
Optional. Free-text description of the resource.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp when the resource was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp when the resource was updated.   
`labels` |  `MutableMapping[str, str]`   
Set of label tags associated with the resource.   
`client_certificate` |  `str`   
Optional. A reference to a certificatemanager.googleapis.com.Certificate resource. This is a relative resource path following the form "projects/{project}/locations/{location}/certificates/{certificate}". Used by a BackendService to negotiate mTLS when the backend connection uses TLS and the backend requests a client certificate. Must have a CLIENT_AUTH scope.   
`trust_config` |  `str`   
Optional. A reference to a TrustConfig resource from the certificatemanager.googleapis.com namespace. This is a relative resource path following the form "projects/{project}/locations/{location}/trustConfigs/{trust_config}". A BackendService uses the chain of trust represented by this TrustConfig, if specified, to validate the server certificates presented by the backend. Required unless wellKnownRoots is set to PUBLIC_ROOTS.   
`well_known_roots` |  `[google.cloud.network_security_v1alpha1.types.BackendAuthenticationConfig.WellKnownRoots](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.BackendAuthenticationConfig.WellKnownRoots)`   
Well known roots to use for server certificate validation.   
`etag` |  `str`   
Output only. Etag of the resource.   
  
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
  
### WellKnownRoots
    
    
    WellKnownRoots(value)

Enum to specify the well known roots to use for server certificate validation.
    
    
        The well-known roots are a set of root CAs
        managed by Google. CAs in this set can be added
        or removed without notice.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
