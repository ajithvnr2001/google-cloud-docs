---
url: https://docs.cloud.google.com/python/docs/reference/connectgateway/latest/google.cloud.gkeconnect.gateway_v1beta1.types.GenerateCredentialsRequest
title: Class GenerateCredentialsRequest (0.13.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:10:51.646225+00:00
---

# Class GenerateCredentialsRequest (0.13.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/connectgateway/latest/google.cloud.gkeconnect.gateway_v1beta1.types.GenerateCredentialsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GenerateCredentialsRequest (0.13.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.2 (latest)  0.13.1  0.12.0  0.11.0  0.10.4  0.9.2  0.8.11  0.7.0  0.6.3  0.5.2  0.4.1  0.3.0  0.2.3  0.1.0 
    
    
    GenerateCredentialsRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A request for connection information for a particular membership.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The Fleet membership resource.   
`force_use_agent` |  `bool`   
Optional. Whether to force the use of Connect Agent-based transport. This will return a configuration that uses Connect Agent as the underlying transport mechanism for cluster types that would otherwise have used a different transport. Requires that Connect Agent be installed on the cluster. Setting this field to false is equivalent to not setting it.   
`version` |  `str`   
Optional. The Connect Gateway version to be used in the resulting configuration. Leave this field blank to let the server choose the version (recommended).   
`kubernetes_namespace` |  `str`   
Optional. The namespace to use in the kubeconfig context. If this field is specified, the server will set the `namespace` field in kubeconfig context. If not specified, the `namespace` field is omitted.   
`operating_system` |  `[google.cloud.gkeconnect.gateway_v1beta1.types.GenerateCredentialsRequest.OperatingSystem](https://docs.cloud.google.com/python/docs/reference/connectgateway/latest/google.cloud.gkeconnect.gateway_v1beta1.types.GenerateCredentialsRequest.OperatingSystem)`   
Optional. The operating system where the kubeconfig will be used.   
  
## Classes 

### OperatingSystem
    
    
    OperatingSystem(value)

Operating systems requiring specialized kubeconfigs.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
