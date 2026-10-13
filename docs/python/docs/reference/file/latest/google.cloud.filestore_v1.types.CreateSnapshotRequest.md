---
url: https://docs.cloud.google.com/python/docs/reference/file/latest/google.cloud.filestore_v1.types.CreateSnapshotRequest
title: Class CreateSnapshotRequest (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:11.302041+00:00
---

# Class CreateSnapshotRequest (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/file/latest/google.cloud.filestore_v1.types.CreateSnapshotRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreateSnapshotRequest (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.0  1.15.0  1.14.0  1.13.2  1.12.0  1.11.0  1.10.1  1.9.5  1.8.0  1.7.0  1.6.2  1.5.1  1.4.1  1.3.0  1.2.3  1.1.3  1.0.0  0.2.3  0.1.0 
    
    
    CreateSnapshotRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

CreateSnapshotRequest creates a snapshot.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The Filestore Instance to create the snapshots of, in the format `projects/{project_id}/locations/{location}/instances/{instance_id}`  
`snapshot_id` |  `str`   
Required. The ID to use for the snapshot. The ID must be unique within the specified instance. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and cannot end with a hyphen.   
`snapshot` |  `[google.cloud.filestore_v1.types.Snapshot](https://docs.cloud.google.com/python/docs/reference/file/latest/google.cloud.filestore_v1.types.Snapshot)`   
Required. A snapshot resource.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
