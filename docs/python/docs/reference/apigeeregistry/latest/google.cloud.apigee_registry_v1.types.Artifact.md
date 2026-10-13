---
url: https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Artifact
title: Class Artifact (0.10.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:24:08.719545+00:00
---

# Class Artifact (0.10.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.Artifact

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Artifact (0.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.0 (latest)  0.9.0  0.8.0  0.7.0  0.6.18  0.5.1  0.4.0  0.3.2  0.2.1  0.1.2 
    
    
    Artifact(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Artifacts of resources. Artifacts are unique (single-value) per resource and are used to store metadata that is too large or numerous to be stored directly on the resource. Since artifacts are stored separately from parent resources, they should generally be used for metadata that is needed infrequently, i.e., not for display in primary views of the resource but perhaps displayed or downloaded upon request. The `ListArtifacts` method allows artifacts to be quickly enumerated and checked for presence without downloading their (potentially-large) contents.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Resource name.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Creation timestamp.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Last update timestamp.   
`mime_type` |  `str`   
A content type specifier for the artifact. Content type specifiers are Media Types (https://en.wikipedia.org/wiki/Media_type) with a possible "schema" parameter that specifies a schema for the stored information. Content types can specify compression. Currently only GZip compression is supported (indicated with "+gzip").   
`size_bytes` |  `int`   
Output only. The size of the artifact in bytes. If the artifact is gzipped, this is the size of the uncompressed artifact.   
`hash_` |  `str`   
Output only. A SHA-256 hash of the artifact's contents. If the artifact is gzipped, this is the hash of the uncompressed artifact.   
`contents` |  `bytes`   
Input only. The contents of the artifact. Provided by API callers when artifacts are created or replaced. To access the contents of an artifact, use GetArtifactContents.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
