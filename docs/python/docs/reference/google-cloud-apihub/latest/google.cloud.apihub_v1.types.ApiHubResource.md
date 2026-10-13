---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApiHubResource
title: Class ApiHubResource (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:28.948756+00:00
---

# Class ApiHubResource (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApiHubResource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ApiHubResource (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 
    
    
    ApiHubResource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

ApiHubResource is one of the resources such as Api, Operation, Deployment, Definition, Spec and Version resources stored in API-Hub.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`api` |  `google.cloud.apihub_v1.types.Api`   
This represents Api resource in search results. Only name, display_name, description and owner fields are populated in search results. This field is a member of `oneof`_ `resource`.   
`operation` |  `[google.cloud.apihub_v1.types.ApiOperation](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ApiOperation)`   
This represents ApiOperation resource in search results. Only name, description, spec and details fields are populated in search results. This field is a member of `oneof`_ `resource`.   
`deployment` |  `[google.cloud.apihub_v1.types.Deployment](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Deployment)`   
This represents Deployment resource in search results. Only name, display_name, description, deployment_type and api_versions fields are populated in search results. This field is a member of `oneof`_ `resource`.   
`spec` |  `[google.cloud.apihub_v1.types.Spec](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Spec)`   
This represents Spec resource in search results. Only name, display_name, description, spec_type and documentation fields are populated in search results. This field is a member of `oneof`_ `resource`.   
`definition` |  `[google.cloud.apihub_v1.types.Definition](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Definition)`   
This represents Definition resource in search results. Only name field is populated in search results. This field is a member of `oneof`_ `resource`.   
`version` |  `[google.cloud.apihub_v1.types.Version](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Version)`   
This represents Version resource in search results. Only name, display_name, description, lifecycle, compliance and accreditation fields are populated in search results. This field is a member of `oneof`_ `resource`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
