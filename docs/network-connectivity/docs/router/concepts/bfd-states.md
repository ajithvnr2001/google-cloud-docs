---
url: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd-states/
title: BFD diagnostic messages and session states \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:28.629000+00:00
---

# BFD diagnostic messages and session states  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd-states/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# BFD diagnostic messages and session states

This document provides relevant Bidirectional Forwarding Detection (BFD) diagnostic messages, error codes, and status messages. These can be helpful indicators when troubleshooting. [RFC 5880](https://datatracker.ietf.org/doc/html/rfc5880#section-4.1) defines the diagnostic codes that specify the local system's reason for the last change in the BFD session state.

You can see these messages or codes when [viewing Cloud Router status](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details#viewing-router-status).

**Important:** BFD can only be enabled on provisioned VLAN attachments that use Dataplane version 2. You can view the `dataplaneVersion` for a VLAN attachment by viewing the attachment details in one of the following ways:

  * **API** : Use the [interconnectAttachments.get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments/get) method. You can use this method on VLAN attachments for either Dedicated Interconnect or Partner Interconnect. 
  * **Google Cloud CLI** : Use the `gcloud compute interconnects attachments describe ATTACHMENT-NAME` command where ATTACHMENT-NAME is the name of the VLAN attachment for either Dedicated Interconnect or Partner Interconnect. 



In the output of the API or gcloud CLI command, look for the `dataplaneVersion` field with a value of `2`. If the field is absent from the output, the VLAN attachment is using version 1 and cannot be used with BFD. For more information, contact your customer account team.

The Cloud Interconnect Dataplane v2 is unrelated to [ Google Kubernetes Engine (GKE) Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2)

The following table lists BFD diagnostic messages, their numeric error codes, and suggested follow-up actions.

BFD diagnostic message | Numeric code | Suggested action  
---|---|---  
NO_DIAGNOSTIC | `0` | No diagnostic information is available. For more information, see the [BFD State Machine](https://datatracker.ietf.org/doc/html/rfc5880#section-6.2) section of RFC 5880 and the BFD session state table in the next section.  
CONTROL_DETECTION_TIME_EXPIRED | `1` | Local BFD did not receive a control packet from the remote side within the (`num_rx_interval * bfd multiplier`) time period. This could happen when the forwarding link is down or BFD on the remote system is not functioning properly. Check connectivity to the remote system, and check the remote system's BFD session transmit counters.  
ECHO_FUNCTION_FAILED | `2` | —  
NEIGHBOR_SIGNALED_SESSION_DOWN | `3` | BFD neighbor signaled DOWN. Check the remote system BFD configuration and operational state.   
FORWARDING_PLANE_RESET | `4` | —  
PATH_DOWN | `5` | —  
CONCATENATED_PATH_DOWN | `6` | —  
ADMINISTRATIVELY_DOWN | `7` | BFD in the local system has been set to DOWN by the administrator due to a BFD software upgrade. Check that the state is back up after the upgrade.  
REVERSE_CONCATENATED_PATH_DOWN | `8` | —  
  
  


### BFD session states

The following table lists BFD session states and their numeric error codes.

BFD session state | Numeric code  
---|---  
ADMIN_DOWN | `0`  
DOWN | `1`  
INIT | `2`  
UP | `3`  
  
### BFD status messages

You can view BFD status messages under the `bfdStatus` field in command output from the [`gcloud compute routers get-status` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/get-status).

For field definitions and descriptions, see the [Cloud Router API documentation](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/getRouterStatus).

## What's next

  * To modify BFD settings on a BGP session, see [Update or disable BFD](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/updating-bfd).

  * For information about BGP session states, see [BGP session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states).

  * To troubleshoot issues with Cloud Router, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/resources/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
