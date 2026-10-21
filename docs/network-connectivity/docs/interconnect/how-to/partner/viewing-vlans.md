---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/viewing-vlans/
title: View VLAN attachments \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:05.256100+00:00
---

# View VLAN attachments  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/viewing-vlans/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  View VLAN attachments Stay organized with collections  Save and categorize content based on your preferences. 

You can view a list of all the VLAN attachments in your project and the details about each one. For example, you can view the name of an attachment, whether it's an attachment for Dedicated Interconnect or Partner Interconnect, and its associated Cloud Router.

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Select a VLAN attachment to view its details.




###  gcloud 

  1. List all VLAN attachments that are in your project:
         
         gcloud compute interconnects attachments list
         

The output is similar to the following:
         
         NAME: my-attachment
         REGION: us-east1
         TYPE: PARTNER
         INTERCONNECT: some-partner-interconnect
         ROUTER: my-router
         
         NAME: my-second-attachment
         REGION: us-west1
         TYPE: DEDICATED
         INTERCONNECT: some-dedicated-interconnect
         ROUTER: my-second-router
         ...
         

  2. Describe the VLAN attachment to view more information about it:
         
         gcloud compute interconnects attachments describe NAME
         

Replace `NAME` with the name of your VLAN attachment.

The output is similar to the following for IPv4 VLAN attachments:
         
         adminEnabled: false
         edgeAvailabilityDomain: AVAILABILITY_DOMAIN_1
         bandwidth: BPS_1G
         cloudRouterIpAddress: 169.254.67.201/29
         creationTimestamp: '2017-12-01T08:29:09.886-08:00'
         customerRouterIpAddress: 169.254.67.202/29
         id: '7976913826166357434'
         kind: compute#interconnectAttachment
         labelFingerprint: 42WmSpB8rSM=
         name: NAME
         pairingKey: 7e51371e-72a3-40b5-b844-2e3efefaee59/us-central1/2
         partnerMetadata:
           interconnectName: New York (2)
           partnerName: My Service Provider Inc
           portalUrl: https://service-provider-portal.com
         region: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-central1
         router: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-central1/routers/my-router
         selfLink: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-central1/interconnectAttachments/NAME
         stackType: IPV4_ONLY
         state: PENDING_CUSTOMER
         type: PARTNER
         vlanTag8021q: 1000
         

The output is similar to the following for IPv4 and IPv6 (dual stack) VLAN attachments:
         
         adminEnabled: true
         edgeAvailabilityDomain: AVAILABILITY_DOMAIN_1
         bandwidth: BPS_1G
         cloudRouterIpAddress: 169.254.67.201/29
         cloudRouterIpv6Address: 2600:2d00:0:1::1/125
         creationTimestamp: '2017-12-01T08:31:11.580-08:00'
         customerRouterIpAddress: 169.254.67.202/29
         customerRouterIpv6Address: 2600:2d00:0:1::2/125
         description: Interconnect for Customer 1
         id: '7193021941765913888'
         interconnect: https://www.googleapis.com/compute/alpha/projects/partner-project/global/interconnects/lga-2
         kind: compute#interconnectAttachment
         labelFingerprint: 42WmSpB8rSM=
         name: partner-attachment
         partnerMetadata:
           interconnectName: New York (2)
           partnerName: Partner Inc
           portalUrl: https://partner-portal.com
         region: https://www.googleapis.com/compute/alpha/projects/partner-project/regions/us-central1
         selfLink: https://www.googleapis.com/compute/alpha/projects/partner-project/regions/us-central1/interconnectAttachments/customer-attachment
         stackType: IPV4_IPV6
         state: ACTIVE
         type: PARTNER
         vlanTag8021q: 1000
         




**Note:** The VLAN ID for the connection is for the Google Cloud side of the connection. To configure your on-premises router for Layer 2 connections, use the VLAN ID provided by your service provider.

## What's next

  * To create a Partner Interconnect connection, see the [Partner Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/provisioning-overview).

  * To learn more about Cloud Interconnect options, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

  * To help you solve common issues that you might encounter when using Partner Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#partner).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
