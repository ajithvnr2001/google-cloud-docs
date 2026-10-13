---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.types.SearchDeploymentRevisionsRequest
title: Class SearchDeploymentRevisionsRequest (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:53:21.026647+00:00
---

# Class SearchDeploymentRevisionsRequest (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1.types.SearchDeploymentRevisionsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SearchDeploymentRevisionsRequest (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.4.0  0.3.0  0.2.11  0.1.2 
    
    
    SearchDeploymentRevisionsRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Request object for `SearchDeploymentRevisions`.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The name of parent orchestration cluster resource. Format should be - "projects/{project_id}/locations/{location_name}/orchestrationClusters/{orchestration_cluster}".   
`query` |  `str`   
Required. Supported queries: 1\. "" : Lists all revisions across all deployments. 2\. "latest=true" : Lists latest revisions across all deployments. 3\. "name={name}" : Lists all revisions of deployment with name {name}. 4\. "name={name} latest=true": Lists latest revision of deployment with name {name}   
`page_size` |  `int`   
Optional. The maximum number of deployment revisions to return per page. max page size = 100, default page size = 20.   
`page_token` |  `str`   
Optional. The page token, received from a previous search call. It can be provided to retrieve the subsequent page.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
