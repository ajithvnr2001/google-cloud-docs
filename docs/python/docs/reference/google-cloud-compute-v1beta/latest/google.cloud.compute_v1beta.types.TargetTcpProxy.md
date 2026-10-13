---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.TargetTcpProxy
title: Class TargetTcpProxy (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:44.470630+00:00
---

# Class TargetTcpProxy (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.TargetTcpProxy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TargetTcpProxy (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    TargetTcpProxy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a Target TCP Proxy resource.

A target TCP proxy is a component of a Proxy Network Load Balancer. The forwarding rule references the target TCP proxy, and the target proxy then references a backend service. For more information, readProxy Network Load Balancer overview.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`creation_timestamp` |  `str`   
Output only. [Output Only] Creation timestamp inRFC3339 text format. This field is a member of `oneof`_ `_creation_timestamp`.   
`description` |  `str`   
An optional description of this resource. Provide this property when you create the resource. This field is a member of `oneof`_ `_description`.   
`id` |  `int`   
[Output Only] The unique identifier for the resource. This identifier is defined by the server. This field is a member of `oneof`_ `_id`.   
`kind` |  `str`   
Output only. [Output Only] Type of the resource. Alwayscompute#targetTcpProxy for target TCP proxies. This field is a member of `oneof`_ `_kind`.   
`load_balancing_scheme` |  `str`   
Specifies the type of load balancing scheme used by this target proxy. Check the LoadBalancingScheme enum for the list of possible values. This field is a member of `oneof`_ `_load_balancing_scheme`.   
`name` |  `str`   
Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. This field is a member of `oneof`_ `_name`.   
`proxy_bind` |  `bool`   
This field only applies when the forwarding rule that references this target proxy has a loadBalancingScheme set toINTERNAL_SELF_MANAGED. When this field is set to true, Envoy proxies set up inbound traffic interception and bind to the IP address and port specified in the forwarding rule. This is generally useful when using Traffic Director to configure Envoy as a gateway or middle proxy (in other words, not a sidecar proxy). The Envoy proxy listens for inbound requests and handles requests when it receives them. The default is false. This field is a member of `oneof`_ `_proxy_bind`.   
`proxy_header` |  `str`   
Specifies the type of proxy header to append before sending data to the backend, either NONE or PROXY_V1. The default is NONE. Check the ProxyHeader enum for the list of possible values. This field is a member of `oneof`_ `_proxy_header`.   
`region` |  `str`   
Output only. [Output Only] URL of the region where the regional TCP proxy resides. This field is not applicable to global TCP proxy. This field is a member of `oneof`_ `_region`.   
`self_link` |  `str`   
[Output Only] Server-defined URL for the resource. This field is a member of `oneof`_ `_self_link`.   
`service` |  `str`   
URL to the BackendService resource. This field is a member of `oneof`_ `_service`.   
  
## Classes 

### LoadBalancingScheme
    
    
    LoadBalancingScheme(value)

Specifies the type of load balancing scheme used by this target proxy.

### ProxyHeader
    
    
    ProxyHeader(value)

Specifies the type of proxy header to append before sending data to the backend, either NONE or PROXY_V1. The default is NONE.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
