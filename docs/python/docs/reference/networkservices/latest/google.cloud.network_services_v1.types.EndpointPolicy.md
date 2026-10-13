---
url: https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1.types.EndpointPolicy
title: Class EndpointPolicy (0.10.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:46.571463+00:00
---

# Class EndpointPolicy (0.10.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1.types.EndpointPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class EndpointPolicy (0.10.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.4 (latest)  0.10.3  0.9.0  0.8.0  0.7.0  0.6.0  0.5.24  0.4.1  0.3.0  0.2.2  0.1.1 
    
    
    EndpointPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

EndpointPolicy is a resource that helps apply desired configuration on the endpoints that match specific criteria. For example, this resource can be used to apply "authentication config" an all endpoints that serve on port 8080.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. Name of the EndpointPolicy resource. It matches pattern `projects/{project}/locations/*/endpointPolicies/{endpoint_policy}`.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp when the resource was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp when the resource was updated.   
`labels` |  `MutableMapping[str, str]`   
Optional. Set of label tags associated with the EndpointPolicy resource.   
`type_` |  `[google.cloud.network_services_v1.types.EndpointPolicy.EndpointPolicyType](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1.types.EndpointPolicy.EndpointPolicyType)`   
Required. The type of endpoint policy. This is primarily used to validate the configuration.   
`authorization_policy` |  `str`   
Optional. This field specifies the URL of AuthorizationPolicy resource that applies authorization policies to the inbound traffic at the matched endpoints. Refer to Authorization. If this field is not specified, authorization is disabled(no authz checks) for this endpoint.   
`endpoint_matcher` |  `[google.cloud.network_services_v1.types.EndpointMatcher](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1.types.EndpointMatcher)`   
Required. A matcher that selects endpoints to which the policies should be applied.   
`traffic_port_selector` |  `[google.cloud.network_services_v1.types.TrafficPortSelector](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1.types.TrafficPortSelector)`   
Optional. Port selector for the (matched) endpoints. If no port selector is provided, the matched config is applied to all ports.   
`description` |  `str`   
Optional. A free-text description of the resource. Max length 1024 characters.   
`server_tls_policy` |  `str`   
Optional. A URL referring to ServerTlsPolicy resource. ServerTlsPolicy is used to determine the authentication policy to be applied to terminate the inbound traffic at the identified backends. If this field is not set, authentication is disabled(open) for this endpoint.   
`client_tls_policy` |  `str`   
Optional. Deprecated: This field is not used and is a no-op. A URL referring to a ClientTlsPolicy resource. ClientTlsPolicy can be set to specify the authentication for traffic from the proxy to the actual endpoints. More specifically, it is applied to the outgoing traffic from the proxy to the endpoint. This is typically used for sidecar model where the proxy identifies itself as endpoint to the control plane, with the connection between sidecar and endpoint requiring authentication. If this field is not set, authentication is disabled(open). Applicable only when EndpointPolicyType is SIDECAR_PROXY.   
  
## Classes 

### EndpointPolicyType
    
    
    EndpointPolicyType(value)

The type of endpoint policy.

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
