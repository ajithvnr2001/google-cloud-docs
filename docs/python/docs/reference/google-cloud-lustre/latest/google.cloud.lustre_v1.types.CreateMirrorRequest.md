---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-lustre/latest/google.cloud.lustre_v1.types.CreateMirrorRequest
title: Class CreateMirrorRequest (0.4.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:22:44.376088+00:00
---

# Class CreateMirrorRequest (0.4.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-lustre/latest/google.cloud.lustre_v1.types.CreateMirrorRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreateMirrorRequest (0.4.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.3 (latest)  0.4.2  0.3.0  0.2.0  0.1.2 
    
    
    CreateMirrorRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request for CreateMirror.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. Parent instance resource where the mirror will be created, in the format: `projects/{project}/locations/{location}/instances/{instance}`  
`mirror_id` |  `str`   
Required. The ID to use for the mirror. \- Must contain only lowercase letters, numbers, and hyphens. \- Must start with a letter. \- Must be between 1-63 characters. \- Must end with a number or a letter. The ID cannot be changed after the mirror is created.   
`mirror` |  `[google.cloud.lustre_v1.types.Mirror](https://docs.cloud.google.com/python/docs/reference/google-cloud-lustre/latest/google.cloud.lustre_v1.types.Mirror)`   
Required. The mirror to create.   
`request_id` |  `str`   
Optional. The unique ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate mirrors for at least 60 minutes. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate mirrors. The request ID must be a valid UUID version 4 with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). This request is only idempotent if a `request_id` is provided.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
