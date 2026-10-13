---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1beta.types.SelfManagedSource
title: Class SelfManagedSource (0.5.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:13.221574+00:00
---

# Class SelfManagedSource (0.5.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1beta.types.SelfManagedSource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SelfManagedSource (0.5.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.5 (latest)  0.5.4  0.4.0  0.3.0  0.2.0  0.1.3 
    
    
    SelfManagedSource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Details of the self-managed source instance.

## Attributes  
  
---  
**Name** | **Description**  
`ip_address` |  `str`   
Required. The IP address of the source instance. This IP address should be a stable IP address that can be accessed by the Memorystore instance throughout the migration process.   
`port` |  `int`   
Required. The port of the source instance. This port should be a stable port that can be accessed by the Memorystore instance throughout the migration process.   
`network_attachment` |  `str`   
Required. The resource name of the Private Service Connect Network Attachment used to establish connectivity to the source instance. This network attachment has the following requirements: 1\. It must be in the same project as the Memorystore instance. 2\. It must be in the same region as the Memorystore instance. 3\. The subnet attached to the network attachment must be in the same VPC network as the source instance nodes. Format: projects/{project}/regions/{region}/networkAttachments/{network_attachment}   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
