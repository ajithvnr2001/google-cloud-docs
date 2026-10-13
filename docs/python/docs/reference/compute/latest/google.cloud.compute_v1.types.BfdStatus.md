---
url: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.BfdStatus
title: Class BfdStatus (1.56.0rc1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:02.173834+00:00
---

# Class BfdStatus (1.56.0rc1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.BfdStatus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BfdStatus (1.56.0rc1) Stay organized with collections  Save and categorize content based on your preferences. 

1.56.0-rc1  1.55.0 (latest)  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.1  1.19.2  1.18.0  1.17.0  1.16.1  1.15.0  1.14.1  1.13.0  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.1  0.1.0 
    
    
    BfdStatus(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Next free: 15

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`bfd_session_initialization_mode` |  `str`   
The BFD session initialization mode for this BGP peer. If set to ACTIVE, the Cloud Router will initiate the BFD session for this BGP peer. If set to PASSIVE, the Cloud Router will wait for the peer router to initiate the BFD session for this BGP peer. If set to DISABLED, BFD is disabled for this BGP peer. Check the BfdSessionInitializationMode enum for the list of possible values. This field is a member of `oneof`_ `_bfd_session_initialization_mode`.   
`config_update_timestamp_micros` |  `int`   
Unix timestamp of the most recent config update. This field is a member of `oneof`_ `_config_update_timestamp_micros`.   
`control_packet_counts` |  `[google.cloud.compute_v1.types.BfdStatusPacketCounts](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.BfdStatusPacketCounts)`   
Control packet counts for the current BFD session. This field is a member of `oneof`_ `_control_packet_counts`.   
`control_packet_intervals` |  `MutableSequence[[google.cloud.compute_v1.types.PacketIntervals](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.PacketIntervals)]`   
Inter-packet time interval statistics for control packets.   
`local_diagnostic` |  `str`   
The diagnostic code specifies the local system's reason for the last change in session state. This allows remote systems to determine the reason that the previous session failed, for example. These diagnostic codes are specified in section 4.1 ofRFC5880 Check the LocalDiagnostic enum for the list of possible values. This field is a member of `oneof`_ `_local_diagnostic`.   
`local_state` |  `str`   
The current BFD session state as seen by the transmitting system. These states are specified in section 4.1 ofRFC5880 Check the LocalState enum for the list of possible values. This field is a member of `oneof`_ `_local_state`.   
`negotiated_local_control_tx_interval_ms` |  `int`   
Negotiated transmit interval for control packets. This field is a member of `oneof`_ `_negotiated_local_control_tx_interval_ms`.   
`rx_packet` |  `[google.cloud.compute_v1.types.BfdPacket](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.BfdPacket)`   
The most recent Rx control packet for this BFD session. This field is a member of `oneof`_ `_rx_packet`.   
`tx_packet` |  `[google.cloud.compute_v1.types.BfdPacket](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.BfdPacket)`   
The most recent Tx control packet for this BFD session. This field is a member of `oneof`_ `_tx_packet`.   
`uptime_ms` |  `int`   
Session uptime in milliseconds. Value will be 0 if session is not up. This field is a member of `oneof`_ `_uptime_ms`.   
  
## Classes 

### BfdSessionInitializationMode
    
    
    BfdSessionInitializationMode(value)

The BFD session initialization mode for this BGP peer. If set to ACTIVE, the Cloud Router will initiate the BFD session for this BGP peer. If set to PASSIVE, the Cloud Router will wait for the peer router to initiate the BFD session for this BGP peer. If set to DISABLED, BFD is disabled for this BGP peer.

### LocalDiagnostic
    
    
    LocalDiagnostic(value)

The diagnostic code specifies the local system's reason for the last change in session state. This allows remote systems to determine the reason that the previous session failed, for example. These diagnostic codes are specified in section 4.1 ofRFC5880

### LocalState
    
    
    LocalState(value)

The current BFD session state as seen by the transmitting system. These states are specified in section 4.1 ofRFC5880

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
