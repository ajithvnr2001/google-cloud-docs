---
url: https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.DeleteFederationRequest
title: Class DeleteFederationRequest (1.24.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:09:15.989510+00:00
---

# Class DeleteFederationRequest (1.24.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.DeleteFederationRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DeleteFederationRequest (1.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.24.0 (latest)  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.3  1.17.0  1.16.1  1.15.5  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.3  1.5.1  1.4.1  1.3.1  1.2.0  1.1.2  1.0.0  0.3.3  0.2.2  0.1.0 
    
    
    DeleteFederationRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for DeleteFederation.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The relative resource name of the metastore federation to delete, in the following form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.   
`request_id` |  `str`   
Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request. For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments. The request ID must be a valid `UUID `__ A zero UUID (00000000-0000-0000-0000-000000000000) is not supported.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
