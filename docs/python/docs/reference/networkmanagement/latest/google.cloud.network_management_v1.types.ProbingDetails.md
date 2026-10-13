---
url: https://docs.cloud.google.com/python/docs/reference/networkmanagement/latest/google.cloud.network_management_v1.types.ProbingDetails
title: Class ProbingDetails (1.38.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:04.597023+00:00
---

# Class ProbingDetails (1.38.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networkmanagement/latest/google.cloud.network_management_v1.types.ProbingDetails

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ProbingDetails (1.38.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.38.0 (latest)  1.37.0  1.36.0  1.35.0  1.34.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.1  1.25.3  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.17.3  1.16.0  1.15.1  1.14.0  1.13.3  1.12.0  1.11.0  1.10.0  1.9.1  1.8.2  1.7.1  1.6.0  1.5.4  1.4.0  1.3.3  1.2.1  1.1.0  1.0.2  0.2.0  0.1.1 
    
    
    ProbingDetails(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Results of active probing from the last run of the test.

## Attributes  
  
---  
**Name** | **Description**  
`result` |  `[google.cloud.network_management_v1.types.ProbingDetails.ProbingResult](https://docs.cloud.google.com/python/docs/reference/networkmanagement/latest/google.cloud.network_management_v1.types.ProbingDetails.ProbingResult)`   
The overall result of active probing.   
`verify_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The time that reachability was assessed through active probing.   
`error` |  `google.rpc.status_pb2.Status`   
Details about an internal failure or the cancellation of active probing.   
`abort_cause` |  `[google.cloud.network_management_v1.types.ProbingDetails.ProbingAbortCause](https://docs.cloud.google.com/python/docs/reference/networkmanagement/latest/google.cloud.network_management_v1.types.ProbingDetails.ProbingAbortCause)`   
The reason probing was aborted.   
`sent_probe_count` |  `int`   
Number of probes sent.   
`successful_probe_count` |  `int`   
Number of probes that reached the destination.   
`endpoint_info` |  `[google.cloud.network_management_v1.types.EndpointInfo](https://docs.cloud.google.com/python/docs/reference/networkmanagement/latest/google.cloud.network_management_v1.types.EndpointInfo)`   
The source and destination endpoints derived from the test input and used for active probing.   
`probing_latency` |  `[google.cloud.network_management_v1.types.LatencyDistribution](https://docs.cloud.google.com/python/docs/reference/networkmanagement/latest/google.cloud.network_management_v1.types.LatencyDistribution)`   
Latency as measured by active probing in one direction: from the source to the destination endpoint.   
`destination_egress_location` |  `[google.cloud.network_management_v1.types.ProbingDetails.EdgeLocation](https://docs.cloud.google.com/python/docs/reference/networkmanagement/latest/google.cloud.network_management_v1.types.ProbingDetails.EdgeLocation)`   
The EdgeLocation from which a packet, destined to the internet, will egress the Google network. This will only be populated for a connectivity test which has an internet destination address. The absence of this field *must not* be used as an indication that the destination is part of the Google network.   
`edge_responses` |  `MutableSequence[[google.cloud.network_management_v1.types.ProbingDetails.SingleEdgeResponse](https://docs.cloud.google.com/python/docs/reference/networkmanagement/latest/google.cloud.network_management_v1.types.ProbingDetails.SingleEdgeResponse)]`   
Probing results for all edge devices.   
`probed_all_devices` |  `bool`   
Whether all relevant edge devices were probed.   
  
## Classes 

### EdgeLocation
    
    
    EdgeLocation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Representation of a network edge location as per <https://cloud.google.com/vpc/docs/edge-locations>.

### ProbingAbortCause
    
    
    ProbingAbortCause(value)

Abort cause types.

### ProbingResult
    
    
    ProbingResult(value)

Overall probing result of the test.
    
    
        - The user lacks permission to access some of the network
          resources required to run the test.
        - No valid source endpoint could be derived from the
          request.
        - An internal error occurred.
    

### SingleEdgeResponse
    
    
    SingleEdgeResponse(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Probing results for a single edge device.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
