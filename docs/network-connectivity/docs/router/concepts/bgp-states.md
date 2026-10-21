---
url: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states/
title: BGP session states \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:28:32.188911+00:00
---

# BGP session states  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# BGP session states

When you check the status of a Cloud Router, the system provides information about the router's Border Gateway Protocol (BGP) peering sessions. This information includes each BGP session's state. The following table explains the possible values of the BGP session state field.

For information about checking Cloud Router status, see [View router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details).

State | Description | Corresponding BGP peer status  
---|---|---  
`Connect` | The BGP peer has been successfully configured, but the BGP session has not yet been established. | `DOWN`  
`Disabled` | The BGP peer has been intentionally stopped. For more information, see the documentation about the [ `CONFIG-DISABLED log message`](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-log-messages#config-disabled-in-logs).  | `DOWN`  
`Established` | The BGP peer has been successfully configured, and the BGP session is established. | `UP`  
`Idle` | You have successfully configured the BGP peer, but a problem occurred. For example, the state is `IDLE` if an internal error has prevented Cloud Router from configuring MD5 authentication. (In these cases, the BGP peer status has a `statusReason` of `MD5_AUTH_INTERNAL_PROBLEM`.) If the state is `IDLE`, you don't need to do anything. Cloud Router tries to recover and bring the session back up. For more information, see [MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication). | `DOWN`  
`The VPN tunnel or Interconnect attachment is unknown.` | Cloud Router couldn't find a VPN tunnel or VLAN attachment associated with the peer. | `DOWN`  
`The VPN Tunnel is not in Established state.` | The VPN tunnel has gone down. | `DOWN`  
`This interface or BGP peer is invalid.` | The Cloud Router has been configured for Network Connectivity Center, but the Cloud Router interface has not been associated with a spoke. | `DOWN`  
`No interface found for the bgp peer.` | Cloud Router couldn't find the interface associated with the peer. | `DOWN`  
  
## What's next

  * For information about BFD diagnostic messages, session states, and status messages, see [BFD diagnostic messages and session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd-states).

  * For information about Cloud Router logging and metrics, see [Viewing Cloud Router logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics). Cloud Router logs can help you understand why a BGP session went down.

  * To troubleshoot issues with Cloud Router, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/resources/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
