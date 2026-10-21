---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/add-gateway-ha-vpn-interconnect/
title: Add an HA VPN gateway to HA VPN over Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:48.971198+00:00
---

# Add an HA VPN gateway to HA VPN over Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/add-gateway-ha-vpn-interconnect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Add an HA VPN gateway to HA VPN over Cloud Interconnect Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for adding HA VPN gateways to your existing [HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect) deployment.

HA VPN over Cloud Interconnect lets you encrypt the traffic that traverses your Dedicated Interconnect or Partner Interconnect connections. Learn how to [deploy HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-deploy-process).

You might need to add HA VPN tunnels to your HA VPN over Cloud Interconnect deployment after you have increased the capacity of your VLAN attachments. Another scenario for adding tunnels is when your Cloud VPN monitoring alerts have detected that your existing VPN tunnels have exceeded the recommended 50% utilization threshold. This threshold ensures that you have sufficient capacity for tunnel failover in the event of VLAN attachment failure.

To increase the capacity in your HA VPN over Cloud Interconnect deployment, you must add HA VPN tunnels. Use the same procedures that you would normally use to add an HA VPN tunnel between an existing HA VPN gateway and an external peer VPN gateway. For more information, see [Add a tunnel from an HA VPN gateway to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/adding-a-tunnel#add-tunnel-from-ha-vpn-to-peer).

You only need to add one or more HA VPN gateways if all existing HA VPN gateway interfaces are already connected to all available peer VPN gateway interfaces. As an alternative, you can also add one or more peer VPN gateways to your on-premises network.

You can only associate HA VPN gateways with encrypted VLAN attachments by using the Google Cloud CLI or the HA VPN API. You can't perform this action with the Google Cloud console after you complete the initial deployment of HA VPN over Cloud Interconnect.

To create an HA VPN gateway, perform the following steps.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.vpnGateways.create`
  * `compute.vpnGateways.delete`
  * `compute.vpnGateways.get`
  * `compute.vpnGateways.list`
  * `compute.vpnGateways.use`
  * `compute.vpnGateways.setLabels`



**Roles**

  * `roles/compute.networkAdmin`



###  gcloud 

  1. Create an HA VPN gateway.

For example, the following command creates an HA VPN gateway and assigns the gateway interfaces to your encrypted VLAN attachments:
         
         gcloud compute vpn-gateways create vpn-gateway-c \
            --network NETWORK_NAME \
            --region REGION \
            --interconnect-attachments \
              ATTACHMENT_1[,ATTACHMENT_2]
         

For the `--interconnect-attachments` parameter, you can list up to two VLAN attachments. The first VLAN attachment is assigned to interface 0 (`if0`) of the HA VPN gateway. If you specify the optional second VLAN attachment, it is assigned to interface 1 (`if1`).

An example command might look like the following:
         
         gcloud compute vpn-gateways create vpn-gateway-c \
             --network network-a \
             --region us-central1 \
             --interconnect-attachments \
               attachment-a-zone1,attachment-a-zone2
         

  2. If you configured the encrypted VLAN attachments to use regional internal IP addresses for your HA VPN gateways, view the gateway's details. Two internal IP addresses from your reserved ranges are automatically assigned to the gateway.

To view the regional internal IP addresses assigned to your HA VPN gateway's interfaces, use the following command:
         
         gcloud compute vpn-gateways describe VPN_GATEWAY_NAME
         

The output might look similar to the following:
         
         creationTimestamp: '2022-10-14T16:22:31.748-07:00'
         id: '678310480370225624'
         kind: compute#vpnGateway
         labelFingerprint: 2345567=
         name: vpn-gateway-c
         network: https://www.googleapis.com/compute/v1/projects/project-id/global/networks/network-a
         region: https://www.googleapis.com/compute/v1/projects/project-id/regions/us-central1
         selfLink: https://www.googleapis.com/compute/v1/projects/project-id/regions/us-central1/vpnGateways/vpn-gateway-c
         stackType: IPV4_ONLY
         vpnInterfaces:
         – id: 0
         interconnectAttachment: https://www.googleapis.com/compute/v1/projects/project-id/regions/us-central1/interconnectAttachments/attachment-a-zone1
         ipAddress: 192.168.20.3
         – id: 1
         interconnectAttachment: https://www.googleapis.com/compute/v1/projects/project-id/regions/us-central1/interconnectAttachments/attachment-a-zone2
         ipAddress: 192.168.21.3
         




###  API 

To create the full configuration for an HA VPN gateway, use the API commands in the following sections. All field values used in these sections are example values.

To create an HA VPN gateway, make a `POST` request by using the [`vpnGateways.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnGateways/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnGateways
       {
         "name": "vpn-gateway-c",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME",
         "vpnInterfaces": [
            {
                interconnectAttachment: "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/attachment-a-zone1"
            },
            {
                interconnectAttachment: "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/attachment-a-zone2"
            }
         ]
       }
    

If you configured the encrypted VLAN attachments to use regional internal IP addresses for your HA VPN gateways, then internal IP addresses from your reserved ranges are automatically assigned to the gateway.

To view the regional internal IP addresses assigned to your HA VPN gateway, use the [`vpnGateways.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnGateways/get):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnGateways/VPN_GATEWAY_NAME
    

The output might look similar to the following: 
    
    
    {
    "kind": "compute#vpnGateway",
    "id": "678310480370225624",
    "creationTimestamp": "2022-10-14T16:22:31.748-07:00",
    "name": "vpn-gateway-c",
    "region": "https://www.googleapis.com/compute/v1/projects/project-id/regions/us-central1",
    "network": "https://www.googleapis.com/compute/v1/projects/project-id/global/networks/network-a",
    "selfLink": "https://www.googleapis.com/compute/v1/projects/project-id/regions/us-central1/vpnGateways/vpngw-test",
    "labelFingerprint": "2345567=",
    "vpnInterfaces": [
      {
        "id": 0,
        "ipAddress": "192.168.20.3",
        "interconnectAttachment": "https://www.googleapis.com/compute/v1/projects/project-id/regions/us-central1/interconnectAttachments/attachment-a-zone1"
      },
      {
        "id": 1,
        "ipAddress": "192.168.21.3",
        "interconnectAttachment": "https://www.googleapis.com/compute/v1/projects/project-id/regions/us-central1/interconnectAttachments/attachment-a-zone2"
      }
     ],
    "stackType": "IPV4_ONLY"
    }
    

## What's next?

  * If you need to add more HA VPN tunnels, see [Add a VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/adding-a-tunnel).

  * To learn about HA VPN monitoring, see [View logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
