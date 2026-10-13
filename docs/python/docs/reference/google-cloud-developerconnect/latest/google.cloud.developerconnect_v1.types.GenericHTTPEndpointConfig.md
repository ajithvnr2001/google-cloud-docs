---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GenericHTTPEndpointConfig
title: Class GenericHTTPEndpointConfig (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:35.455767+00:00
---

# Class GenericHTTPEndpointConfig (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GenericHTTPEndpointConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GenericHTTPEndpointConfig (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    GenericHTTPEndpointConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Defines the configuration for connections to an HTTP service provider.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`basic_authentication` |  `[google.cloud.developerconnect_v1.types.GenericHTTPEndpointConfig.BasicAuthentication](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GenericHTTPEndpointConfig.BasicAuthentication)`   
Optional. Basic authentication with username and password. This field is a member of `oneof`_ `authentication`.   
`bearer_token_authentication` |  `[google.cloud.developerconnect_v1.types.GenericHTTPEndpointConfig.BearerTokenAuthentication](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GenericHTTPEndpointConfig.BearerTokenAuthentication)`   
Optional. Bearer token authentication with a token. This field is a member of `oneof`_ `authentication`.   
`host_uri` |  `str`   
Required. Immutable. The service provider's https endpoint.   
`service_directory_config` |  `[google.cloud.developerconnect_v1.types.ServiceDirectoryConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ServiceDirectoryConfig)`   
Optional. Configuration for using Service Directory to privately connect to a HTTP service provider. This should only be set if the Http service provider is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the HTTP service provider will be made over the public internet.   
`ssl_ca_certificate` |  `str`   
Optional. The SSL certificate to use for requests to the HTTP service provider.   
  
## Classes 

### BasicAuthentication
    
    
    BasicAuthentication(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Basic authentication with username and password.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### BearerTokenAuthentication
    
    
    BearerTokenAuthentication(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bearer token authentication with a token.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
