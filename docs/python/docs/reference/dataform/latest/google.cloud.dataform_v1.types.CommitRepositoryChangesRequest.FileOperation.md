---
url: https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1.types.CommitRepositoryChangesRequest.FileOperation
title: Class FileOperation (0.11.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:07.916094+00:00
---

# Class FileOperation (0.11.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1.types.CommitRepositoryChangesRequest.FileOperation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class FileOperation (0.11.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.4 (latest)  0.11.3  0.10.0  0.9.0  0.8.0  0.7.0  0.6.2  0.5.16  0.4.1  0.3.0  0.2.3  0.1.0 
    
    
    FileOperation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a single file operation to the repository.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`write_file` |  `[google.cloud.dataform_v1.types.CommitRepositoryChangesRequest.FileOperation.WriteFile](https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1.types.CommitRepositoryChangesRequest.FileOperation.WriteFile)`   
Represents the write operation. This field is a member of `oneof`_ `operation`.   
`delete_file` |  `[google.cloud.dataform_v1.types.CommitRepositoryChangesRequest.FileOperation.DeleteFile](https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1.types.CommitRepositoryChangesRequest.FileOperation.DeleteFile)`   
Represents the delete operation. This field is a member of `oneof`_ `operation`.   
  
## Classes 

### DeleteFile
    
    
    DeleteFile(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents the delete file operation.

### WriteFile
    
    
    WriteFile(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents the write file operation (for files added or modified).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
