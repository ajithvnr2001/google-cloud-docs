---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-tunnel/
title: Delete a VPN tunnel \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:46.877444+00:00
---

# Delete a VPN tunnel  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-tunnel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Delete a VPN tunnel Stay organized with collections  Save and categorize content based on your preferences. 

The following procedure applies to tunnels connected to either Classic VPN or HA VPN gateways.

To delete an existing Cloud VPN tunnel, complete the following steps.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.vpnGateways.get`
  * `compute.vpnGateways.list`
  * `compute.vpnGateways.create`
  * `compute.vpnGateways.delete`
  * `compute.vpnGateways.use`
  * `compute.vpnGateways.setLabels`
  * `compute.externalVpnGateways.get`
  * `compute.externalVpnGateways.list`
  * `compute.externalVpnGateways.create`
  * `compute.externalVpnGateways.delete`
  * `compute.externalVpnGateways.use`
  * `compute.externalVpnGateways.setLabels`



**Roles**

  * `roles/compute.networkAdmin`



###  Console 

To delete the tunnel, follow these steps:

  1. In the Google Cloud console, go to the **VPN** page.

[Go to VPN](https://console.cloud.google.com/vpn/list?tab=tunnels)

  2. Select the checkbox next to the VPN tunnel that you want to remove.

  3. At the top of the page, click **Delete**.

When you use the Google Cloud console to delete a VPN tunnel, Google Cloud also deletes any Border Gateway Protocol (BGP) sessions associated with the VPN tunnel.

  4. To confirm deletion, click **Delete** again.

  5. Optional: To confirm that the BGP sessions associated with the VPN tunnel are deleted, go to the Cloud Router details page. For more information, see [View Cloud Router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details).




###  gcloud 

In the following commands, replace the following:

  * `PROJECT_ID`: the ID of your project
  * `TUNNEL_NAME`: the name of your tunnel
  * `REGION`: the region where your tunnel resides



To delete the tunnel, follow these steps:

  1. Identify the name and region of the VPN tunnel that you want to delete, and then use that information in the next step. To list all VPN tunnels in your project, run the following command:
         
         gcloud compute vpn-tunnels list
            --project=PROJECT_ID
         

  2. To delete the VPN tunnel, run the following command:
         
         gcloud compute vpn-tunnels delete TUNNEL_NAME \
            --region=REGION \
            --project=PROJECT_ID
         

When you use Google Cloud CLI to delete a VPN tunnel, the command does not automatically delete the BGP sessions that are configured for the VPN tunnel.

  3. Optional: To delete the BGP sessions associated with the VPN tunnel, use the `gcloud compute routers remove-bgp-peer` command. For instructions, see [Remove a BGP session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp#remove_a_bgp_session).

To verify that the BGP sessions are deleted, go to the Cloud Router details page in the Google Cloud console, or run the `gcloud compute routers describe` command for a Cloud Router. For instructions, see [View Cloud Router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details).




###  API 

To delete the tunnel, follow these steps:

  1. Make a DELETE request by using the [`vpnTunnels.delete`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels/delete) method:
         
         DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnTunnels/TUNNEL_NAME
         

When you use the Cloud VPN API to delete a VPN tunnel, the API command does not delete any BGP sessions that are associated with the VPN tunnel.

  2. Optional: To delete the BGP sessions associated with the VPN tunnel, use the [`routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method to update the `bgpPeers[]` field. For instructions, see [Remove a BGP session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp#remove_a_bgp_session).

To verify that your BGP sessions are deleted, go to the Cloud Router details page in the Google Cloud console, or run the `gcloud compute routers describe` command for a Cloud Router. For instructions, see [View Cloud Router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details).




### Recommended follow-up

After deleting a VPN tunnel, consider the following:

  * Review your firewall rules and [delete the rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#deleting_firewall_rules) that you no longer need.

  * If the tunnel used Classic VPN policy-based routing or was a route-based VPN, review the routes in your Google Cloud network. [Delete any static routes](https://docs.cloud.google.com/vpc/docs/using-routes#deletingaroute) that you no longer need.

  * If you used the Google Cloud console to delete the tunnel for a Classic VPN gateway, static routes that were automatically created should already be removed. If you used the Google Cloud CLI to remove the tunnel, or if you created custom static routes for it, delete those tunnels manually.

  * If no more tunnels exist for the associated VPN gateway, you can [delete the VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-gateway).




## What's next

  * To view Cloud Logging and Monitoring information, see [View logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics).
  * To use high-availability and high-throughput scenarios or multiple subnet scenarios, see [Advanced configurations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
