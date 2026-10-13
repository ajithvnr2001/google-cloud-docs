---
url: https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.DeleteJobTemplateRequest
title: Class DeleteJobTemplateRequest (1.22.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:48.254172+00:00
---

# Class DeleteJobTemplateRequest (1.22.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.DeleteJobTemplateRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DeleteJobTemplateRequest (1.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.22.0 (latest)  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.2  1.14.0  1.13.1  1.12.5  1.11.0  1.10.1  1.9.1  1.8.2  1.7.0  1.6.1  1.5.0  1.4.3  1.3.2  1.2.1  1.1.0  1.0.1  0.5.1  0.4.1  0.3.1  0.2.1  0.1.0 
    
    
    DeleteJobTemplateRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for `TranscoderService.DeleteJobTemplate`.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The name of the job template to delete. `projects/{project}/locations/{location}/jobTemplates/{job_template}`  
`allow_missing` |  `bool`   
If set to true, and the job template is not found, the request will succeed but no action will be taken on the server.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
