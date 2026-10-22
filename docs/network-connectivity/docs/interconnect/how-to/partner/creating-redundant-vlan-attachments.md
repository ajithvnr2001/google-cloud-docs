---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-redundant-vlan-attachments/
title: Duplicate a VLAN attachment for redundancy \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:32.978296+00:00
---

# Duplicate a VLAN attachment for redundancy  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-redundant-vlan-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Duplicate a VLAN attachment for redundancy Stay organized with collections  Save and categorize content based on your preferences. 

If you have an existing VLAN attachment for a Partner Interconnect connection, you can create a second one to build redundancy. We recommend redundancy so that if one VLAN attachment fails, the other one can continue to serve traffic.

To create a redundant VLAN attachment, it must connect to Google Cloud in the same metropolitan area (city) as the existing VLAN attachment but in a different [edge availability domain](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#edge-availability-domain) (metro availability zone).

**Note:** To build a redundant topology, you must create and configure additional resources. For more information, see [Redundancy and SLA](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#redundancy).

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Click **Add VLAN attachment**.

  3. Select **Partner Interconnect** , and then click **Continue**.

  4. Click **I already have a service provider**.

  5. Under **Redundancy** , select **Add a redundant VLAN to an existing VLAN**.

  6. In the **Select VLAN attachment** field, select the attachment that you want to build redundancy for. The new redundant attachment uses the same VPC network and region as the existing one.

  7. Specify the details of your VLAN attachments:

     * **Cloud Router** : Choose the Cloud Router that's associated with the existing attachment. The Cloud Router must have an ASN of `16550`. If you don't have an existing Cloud Router that you can use, [create one](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/creating-routers) with an ASN of `16550`.
     * **VLAN attachment name** : A name for the attachment. This name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the attachment, such as `my-attachment`.
  8. Click **Create** to create the attachments, which takes a few minutes.

  9. After creation is complete, copy the pairing keys. You need to share these keys with your service provider when you request a connection with them.

  10. Click **OK** to view a list of your VLAN attachments.




###  gcloud 

Use the existing Cloud Router in the network and region that contains the existing VLAN attachment. The Cloud Router must have an ASN of `16550`. If you don't have an existing Cloud Router that you can use, [create one](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/creating-routers) before you create a VLAN attachment. When you create the Cloud Router, use `16550` for the BGP ASN.

  1. Describe your existing VLAN attachment to view its details. Record its edge availability domain (metro availability zone).

  2. Create a VLAN attachment of type `PARTNER`, specifying the name of your duplicate Cloud Router and a different edge availability domain from the existing VLAN attachment:
         
         gcloud compute interconnects attachments partner create my-second-attachment \
            --region=REGION \
            --router=ROUTER_NAME \
            --edge-availability-domain=AVAILABILITY_DOMAIN
         

Replace the following:

     * `REGION`: the region that your VLAN attachment is located in

     * `ROUTER_NAME`: the name of your duplicate Cloud Router

     * `AVAILABILITY_DOMAIN`: an edge availability domain that's different from your existing VLAN attachment

  3. Describe the attachment to retrieve its pairing key; you need to share this key with your service provider when you request a connection with them:
         
         gcloud compute interconnects attachments describe my-second-attachment \
            --region=REGION
         

The output is similar to the following:
         
         adminEnabled: false
         edgeAvailabilityDomain: AVAILABILITY_DOMAIN_2
         creationTimestamp: '2017-12-01T08:29:09.886-08:00'
         id: '7976913826166357434'
         kind: compute#interconnectAttachment
         labelFingerprint: 42WmSpB8rSM=
         name: my-second-attachment
         pairingKey: 7e51371e-72a3-40b5-b844-2e3efefaee59/us-central1/2
         region: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-central1
         router: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-central1/routers/my-router
         selfLink: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-central1/interconnectAttachments/my-second-attachment
         state: PENDING_PARTNER
         type: PARTNER
         

The `pairingKey` field contains the pairing key that you need to share with your service provider. Treat the pairing key as sensitive information until your VLAN attachment is configured.

The state of the VLAN attachment is `PENDING_PARTNER` until you request a connection with your service provider and they complete its configuration. After the configuration is complete, the state of the attachment changes to `ACTIVE`.




**Important:** When you request a redundant connection from your service provider, choose the same metropolitan area that contains your existing VLAN attachment. You can find the existing attachment's location from your service provider.

## What's next?

  * To request a connection from your service provider, see [Request connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/requesting-connections).

  * To create a Partner Interconnect connection, see the [Partner Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/provisioning-overview).

  * To learn more about Cloud Interconnect options, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

  * To help you solve common issues that you might encounter when using Partner Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#partner).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
