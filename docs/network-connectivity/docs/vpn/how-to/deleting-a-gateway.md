---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-gateway/
title: Delete a VPN gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:47.278789+00:00
---

# Delete a VPN gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Delete a VPN gateway Stay organized with collections  Save and categorize content based on your preferences. 

The following procedures enable you to delete an HA VPN gateway or a Classic VPN gateway. HA VPN uses the `vpn-gateways` command option, and Classic VPN uses the `target-vpn-gateways` command option.

After you delete an HA VPN gateway, any peer gateway resources that you created still exist.

Before removing a Cloud VPN gateway, [delete all associated VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-tunnel).

## Delete an HA VPN gateway

To delete an existing HA VPN gateway, complete the following steps.

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

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list?tab=gateways)

  2. Find the row that contains the **Gateway name** that you want to delete.

  3. Click the **Gateway name**.

  4. On the **Google VPN gateway details** page, under **VPN tunnels** , select the checkboxes next to the tunnels that you want to delete.

  5. To delete the tunnels, click **Delete**.

  6. In the confirmation dialog box, click **Delete**.

  7. To delete the gateway, at the top of the page, click **Delete**.

  8. In the confirmation dialog box, click **Delete**.




###  gcloud 

In the following commands, replace the following:

  * `PROJECT_ID`: the ID of your project
  * `GATEWAY_NAME`: the name of your VPN gateway
  * `REGION`: the region where your VPN gateway resides



To delete the gateway, follow these steps:

  1. Identify the name and region of the VPN gateway that you want to delete, and then use that information in later steps. To list all VPN gateways, run the following command:
         
         gcloud compute vpn-gateways list
            --project=PROJECT_ID
         

  2. Determine if the VPN gateway has any VPN tunnels that need to be deleted. To list all tunnels associated with the gateway, run the following command:
         
         gcloud compute vpn-gateways describe GATEWAY_NAME \
            --region=REGION \
            --project=PROJECT_ID \
            --format='flattened(tunnels)'
         

  3. [Delete each existing tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-tunnel).

  4. Delete the VPN gateway:
         
         gcloud compute vpn-gateways delete GATEWAY_NAME \
            --region=REGION \
            --project=PROJECT_ID
         




###  API 

To delete tunnels first, make a DELETE request by using the [`vpnTunnels.delete`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels/delete) method:
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnTunnels/TUNNEL_NAME
    

Make a DELETE request by using the [`vpnGateways.delete`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnGateways/delete) method:
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnGateways/GATEWAY_NAME
    

## Delete a Classic VPN gateway

To delete an existing Classic VPN gateway, complete the following steps.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.vpnGateways.get`
  * `compute.vpnGateways.list`
  * `compute.externalVpnGateways.get`
  * `compute.externalVpnGateways.list`
  * `compute.vpnGateways.create`
  * `compute.vpnGateways.delete`
  * `compute.vpnGateways.get`
  * `compute.vpnGateways.list`
  * `compute.vpnGateways.use`
  * `compute.vpnGateways.setLabels`
  * `compute.externalVpnGateways.create`
  * `compute.externalVpnGateways.delete`
  * `compute.externalVpnGateways.get`
  * `compute.externalVpnGateways.list`
  * `compute.externalVpnGateways.use`
  * `compute.externalVpnGateways.setLabels`



**Roles**

  * `roles/compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the **VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list?tab=gateways)

  2. Find the row that contains the **Gateway name** that you want to delete.

  3. Click the **Gateway name**.

  4. On the **Google VPN gateway details** page, under **VPN tunnels** , select the checkboxes next to the tunnels that you want to delete.

  5. To delete the tunnels, click **Delete**.

  6. In the confirmation dialog box, click **Delete**.

  7. To delete the gateway, at the top of the page, click **Delete**.

  8. In the confirmation dialog box, click **Delete**.


**Note:** Using the Google Cloud console to delete a VPN gateway removes the three associated forwarding rules and the target VPN gateway object. The regional external IP address remains in your project, so it can be re-used or deleted separately.

###  gcloud 

In the following commands, replace the following:

  * `PROJECT_ID`: the ID of your project
  * `GATEWAY_NAME`: the name of your VPN gateway
  * `REGION`: the region where your VPN gateway resides
  * `FR_NAME`: the name of each forwarding rule



To delete the gateway, follow these steps:

  1. Identify the name and region of the VPN gateway that you want to delete, and then use that information in later steps. To list all VPN gateways, run the following command:
         
         gcloud compute target-vpn-gateways list
            --project=PROJECT_ID
         

  2. Determine if the VPN gateway has any VPN tunnels that need to be deleted. To list all tunnels associated with the gateway, run the following command:
         
         gcloud compute target-vpn-gateways describe GATEWAY_NAME \
            --region=REGION \
            --project=PROJECT_ID \
            --format='flattened(tunnels)'
         

  3. [Delete each existing tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-tunnel).

  4. Determine the names of the three forwarding rules associated with the target VPN gateway:
         
         gcloud compute target-vpn-gateways describe GATEWAY_NAME \
            --region=REGION \
            --project=PROJECT_ID \
            --format='flattened(forwardingRules)'
         

  5. Delete the forwarding rules; repeat this command for each forwarding rule:
         
         gcloud compute forwarding-rules delete FR_NAME \
            --region=REGION \
            --project=PROJECT_ID
         

  6. Delete the target VPN gateway:
         
         gcloud compute target-vpn-gateways delete GATEWAY_NAME \
            --region=REGION \
            --project=PROJECT_ID
         




###  API 

To delete tunnels first, make a DELETE request by using the [`vpnTunnels.delete`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels/delete) method:
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnTunnels/TUNNEL_NAME
    

Make a DELETE request by using the [`targetVpnGateways.delete`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways/delete) method:
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/targetVpnGateways/GATEWAY_NAME
    

## Recommended follow-up

After deleting a VPN gateway, consider doing the following:

  * Review your firewall rules and [delete the rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#deleting_firewall_rules) that you no longer need.
  * For Classic VPN, you can [delete the external IP address](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/delete) previously used by the VPN gateway.



## What's next

  * To view Cloud Logging and Monitoring information, see [View logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics).
  * To use high-availability and high-throughput scenarios or multiple subnet scenarios, see [Advanced configurations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
