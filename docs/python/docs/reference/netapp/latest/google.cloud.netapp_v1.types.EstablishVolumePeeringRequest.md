---
url: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.EstablishVolumePeeringRequest
title: Class EstablishVolumePeeringRequest (0.10.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:18.777480+00:00
---

# Class EstablishVolumePeeringRequest (0.10.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.EstablishVolumePeeringRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class EstablishVolumePeeringRequest (0.10.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.2 (latest)  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.24  0.2.0  0.1.0 
    
    
    EstablishVolumePeeringRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

EstablishVolumePeeringRequest establishes cluster and svm peerings between the source and destination clusters.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The volume resource name, in the format `projects/{project_id}/locations/{location}/volumes/{volume_id}`  
`peer_cluster_name` |  `str`   
Required. Name of the user's local source cluster to be peered with the destination cluster.   
`peer_svm_name` |  `str`   
Required. Name of the user's local source vserver svm to be peered with the destination vserver svm.   
`peer_ip_addresses` |  `MutableSequence[str]`   
Optional. List of IPv4 ip addresses to be used for peering.   
`peer_volume_name` |  `str`   
Required. Name of the user's local source volume to be peered with the destination volume.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
