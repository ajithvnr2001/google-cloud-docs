---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ArtifactConfig
title: Class ArtifactConfig (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:28.841291+00:00
---

# Class ArtifactConfig (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ArtifactConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ArtifactConfig (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    ArtifactConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The artifact config of the artifact that is deployed.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`google_artifact_registry` |  `[google.cloud.developerconnect_v1.types.GoogleArtifactRegistry](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GoogleArtifactRegistry)`   
Optional. Set if the artifact is stored in Artifact registry. This field is a member of `oneof`_ `artifact_storage`.   
`google_artifact_analysis` |  `[google.cloud.developerconnect_v1.types.GoogleArtifactAnalysis](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GoogleArtifactAnalysis)`   
Optional. Set if the artifact metadata is stored in Artifact analysis. This field is a member of `oneof`_ `artifact_metadata_storage`.   
`uri` |  `str`   
Required. Immutable. The URI of the artifact that is deployed. e.g. `us-docker.pkg.dev/my-project/my-repo/image`. The URI does not include the tag / digest because it captures a lineage of artifacts.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
