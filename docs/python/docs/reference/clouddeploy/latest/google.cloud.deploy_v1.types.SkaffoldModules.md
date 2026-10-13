---
url: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.SkaffoldModules
title: Class SkaffoldModules (2.12.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:15.680969+00:00
---

# Class SkaffoldModules (2.12.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.SkaffoldModules

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SkaffoldModules (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.0  2.9.0  2.8.0  2.7.1  2.6.3  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.0  1.19.1  1.18.1  1.17.3  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.1  1.1.1  1.0.0  0.3.2  0.2.0  0.1.1 
    
    
    SkaffoldModules(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Skaffold Config modules and their remote source.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`configs` |  `MutableSequence[str]`   
Optional. The Skaffold Config modules to use from the specified source.   
`git` |  `[google.cloud.deploy_v1.types.SkaffoldModules.SkaffoldGitSource](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.SkaffoldModules.SkaffoldGitSource)`   
Optional. Remote git repository containing the Skaffold Config modules. This field is a member of `oneof`_ `source`.   
`google_cloud_storage` |  `[google.cloud.deploy_v1.types.SkaffoldModules.SkaffoldGCSSource](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.SkaffoldModules.SkaffoldGCSSource)`   
Optional. Cloud Storage bucket containing the Skaffold Config modules. This field is a member of `oneof`_ `source`.   
`google_cloud_build_repo` |  `[google.cloud.deploy_v1.types.SkaffoldModules.SkaffoldGCBRepoSource](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.SkaffoldModules.SkaffoldGCBRepoSource)`   
Optional. Cloud Build V2 repository containing the Skaffold Config modules. This field is a member of `oneof`_ `source`.   
  
## Classes 

### SkaffoldGCBRepoSource
    
    
    SkaffoldGCBRepoSource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Cloud Build V2 Repository containing Skaffold Configs.

### SkaffoldGCSSource
    
    
    SkaffoldGCSSource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Cloud Storage bucket containing Skaffold Config modules.

### SkaffoldGitSource
    
    
    SkaffoldGitSource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Git repository containing Skaffold Config modules.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
