---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-peer-gateway/
title: Delete an external peer VPN gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:50.405195+00:00
---

# Delete an external peer VPN gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-peer-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Delete an external peer VPN gateway Stay organized with collections  Save and categorize content based on your preferences. 

The following procedures enable you to delete an external peer VPN gateway resource for an HA VPN gateway. This resource represents your physical or software-based gateway in Google Cloud.

To add an external peer VPN gateway resource, see [Configure the peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-peer-gateway).

Before removing an external peer VPN gateway resource, [delete all associated VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-tunnel).

To delete an external peer VPN gateway resource, complete the following steps.

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

  1. In the Google Cloud console, go to the **VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list?tab=peerGateways)

  2. Find the row that contains the **Peer gateway name** that you want to delete.

  3. Under **In use by VPN tunnels** , click the name of the tunnel to delete.

  4. On the **VPN tunnel details** page, at the top of the page, click **Delete**.

  5. On the **VPN tunnels** page, wait for the tunnel to be deleted.

  6. Click the **Peer VPN gateways** tab.

  7. Under **Peer gateway name** , find the row that contains the gateway that you want to delete.

  8. In that row, to delete the gateway, click more_vert**Actions** , then select **Delete**.

  9. In the confirmation dialog box, click **Delete**.

  10. To confirm that the gateway has been deleted, at the top of the page, click refresh**Refresh**.




###  gcloud 

In the following commands, replace the following:

  * `PROJECT_ID`: the ID of your project
  * `EXTERNAL_GATEWAY_NAME`: the name of your external peer VPN gateway



To delete the gateway, follow these steps:

  1. Identify the name of the external peer VPN gateway that you want to delete, and then use that information in later steps. To list all VPN gateways, run the following command:
         
         gcloud compute external-vpn-gateways list
            --project=PROJECT_ID
         

  2. Determine if the VPN gateway has any VPN tunnels that need to be deleted. To list all tunnels associated with the gateway, run the following command:
         
         gcloud compute vpn-gateways describe EXTERNAL_GATEWAY_NAME \
            --project=PROJECT_ID \
            --format='flattened(tunnels)'
         

  3. [Delete each existing tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-tunnel).

  4. Delete the external peer VPN gateway.
         
         gcloud compute external-vpn-gateways delete EXTERNAL_GATEWAY_NAME \
            --project=PROJECT_ID
         




###  API 

To delete tunnels first, make a DELETE request by using the [`vpnTunnels.delete`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/externalVpnGateways/delete) method:
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnTunnels/TUNNEL_NAME
    

Make a DELETE request by using the [`externalVpnGateways.delete`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/externalVpnGateways/delete) method:
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/externalVpnGateways/EXTERNAL_GATEWAY_NAME
    

## What's next

  * To view Cloud Logging and Monitoring information, see [View logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics).
  * To use high-availability and high-throughput scenarios or multiple subnet scenarios, see [Advanced configurations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
