---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/delete-ha-vpn-interconnect/
title: Delete HA VPN over Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:00.572921+00:00
---

# Delete HA VPN over Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/delete-ha-vpn-interconnect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Delete HA VPN over Cloud Interconnect Stay organized with collections  Save and categorize content based on your preferences. 

This page provides the steps required to delete an HA VPN over Cloud Interconnect deployment.

To delete an HA VPN over Cloud Interconnect deployment, delete its components in the following order:

  1. Delete the VPN tunnels. For more information, see [Delete a VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-tunnel).

  2. Delete the HA VPN Cloud Router.

Before you delete the HA VPN Cloud Router, verify that the Cloud Router is not managing any other active BGP sessions.

For more information, see [List and delete Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-routers).

  3. Delete the HA VPN gateways. For more information, see [Delete a VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-gateway).

  4. Delete the encrypted VLAN attachments. For more information, see [Delete VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/delete-vlan-attachments) for Dedicated Interconnect and [Delete VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/delete-vlan-attachments) for Partner Interconnect.

  5. Release any internal IP ranges that you reserved for your encrypted VLAN attachments. For more information, see [Delete a static internal IPv4 or IPv6 address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#delete_a_static_internal_ip_address).

  6. Delete the encrypted Cloud Router used for Cloud Interconnect. For more information, see [List and delete Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-routers).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
