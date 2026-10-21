---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-redundant-interconnect/
title: Duplicate a connection for redundancy \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:02.978239+00:00
---

# Duplicate a connection for redundancy  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-redundant-interconnect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Duplicate a connection for redundancy Stay organized with collections  Save and categorize content based on your preferences. 

If you have a single Dedicated Interconnect connection, you can create a second one so that you have redundant connections. Google recommends redundancy so that if one connection fails, the other connection can continue to serve traffic.

To create a redundant Dedicated Interconnect connection, you must create it in the same metropolitan area (city) as the existing one, but in a different [edge availability domain](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#edge-availability-domain) (metro availability zone). If you don't, the connections won't be redundant.

You can check the redundancy status of your Cloud Interconnect connections by adding them to a connection group. For more information, see [Create a Dedicated Interconnect connection group](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/ordering-dedicated-interconnect#create-group).

**Note:** To build a redundant topology, you must create and configure additional resources. For more information, see [Redundancy and SLA](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#redundancy) in the Dedicated Interconnect overview.**Note:** For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnects.create`
  * `compute.interconnects.get`
  * `compute.interconnectLocations.get`
  * `compute.interconnectLocations.list`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * Compute Network Admin (`roles/compute.networkAdmin`)



###  Console 

To find the city of the existing Dedicated Interconnect connection:

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Select the existing Dedicated Interconnect connection to view its details page.

  3. In the **Details** section, view the location address and record the city name. This is the city where the redundant connection must be configured.




To create the redundant Dedicated Interconnect connection:

  1. In the Google Cloud console, go to the **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Click **Set up connection**.

  3. Select **Dedicated Interconnect** , and then click **Continue**.

  4. Select **Order new Dedicated Interconnect** , and then click **Continue**.

  5. Specify the details of the Dedicated Interconnect connection:

     * **Name** : A name for the connection. This name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the connection, such as `my-interconnect-redundant`.
     * **Location** : Select **Choose** , and then filter the list of locations to the city where your existing connection is located. Select the same facility (if it supports more than one edge availability domain) or a different facility. To view the list of cities and their edge availability domains, see [All colocation facilities](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities).
     * **Capacity** : The total capacity of your connection, which is determined by the number and size of the circuits that you order. Use the same value as the existing connection.
  6. Click **Next**.

  7. Clear the **Create redundant interconnect** checkbox, and then click **Continue** to dismiss the SLA message.

Normally, when you create a Dedicated Interconnect connection, we recommend that you order a second redundant connection. In this case, because you're creating a redundant connection for an existing connection, you don't need to order another connection.

  8. Optional: Select an edge availability domain (metro availability zone).

If the location that you selected has more than one edge availability domain, you can choose a particular zone. Choose the zone that doesn't contain the existing Dedicated Interconnect connection that you're building redundancy for. If you have no additional connections in the same city, the Google Cloud console chooses the correct zone for you.

  9. Click **Next**.

  10. Specify your contact information:

     * **Company name** : The name of your organization to put in the LOA as the party authorized to request a connection.
     * **Technical contact** : An email address where notifications about this connection are sent. You don't need to enter your own address; you are included in all notifications. You can specify only one address.
  11. Review your order. Check that your Dedicated Interconnect connection details and contact information are correct. If everything is correct, click **Place order**. If not, go back and edit the connection details.

  12. On the order confirmation page, review the next steps and then select **Done**.




###  gcloud 

To find the city of the existing Dedicated Interconnect connection:

  1. [Describe the existing Dedicated Interconnect connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/viewing-interconnects) to view its location:
         
         gcloud compute interconnects describe INTERCONNECT_NAME
         

In the output, view the `location` field, which shows a URL such as `https://www.googleapis.com/compute/...<example>.../sin-zone1-388`. The last part of the URL is the name of the location (`sin-zone1-38`).

  2. [Describe the location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/listing-locations) to view the city in which it's located, passing the location name from the previous step:
         
         gcloud compute interconnects locations describe LOCATION_NAME
         




To create the redundant Dedicated Interconnect connection:

  1. Choose a facility where the redundant Dedicated Interconnect connection is to be located. From the list of [locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities), select one that's in the same city but in a different edge availability domain from the existing connection.

For example, if the existing connection is in `iad-zone2-1`, select a location that's in Ashburn but in zone 1, such as `iad-zone1-1`. You need this location name when you create the redundant connection.

  2. Create the redundant Dedicated Interconnect connection in the location that you selected:
         
         gcloud compute interconnects create INTERCONNECT_NAME \
              --customer-name=NAME \
              --interconnect-type=DEDICATED \
              --link-type=LINK_TYPE \
              --location=LOCATION_NAME \
              --requested-link-count=NUMBER_OF_LINKS \
             [--noc-contact-email=EMAIL_ADDRESS] \
             [--description=STRING]
         

Replace the following:

     * `INTERCONNECT_NAME`: the name for the Dedicated Interconnect connection; this name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the connection, such as `my-interconnect-redundant`
     * `NAME`: the name of your organization to put in the LOA as the party authorized to request a connection
     * `LINK_TYPE`: the per-circuit capacity of your Dedicated Interconnect connection; use the same value as the existing connection.
     * `LOCATION_NAME`: the name of the location that you selected in the previous step
     * `NUMBER_OF_LINKS`: number of circuits of type `link-type`; use the same value as the existing connection. For example, if the existing connection has 8 x 10-Gbps (80 Gbps) circuits, this number would be `8`. If the existing connection has 2 x 100-Gbps (200 Gbps) circuits, this number would be `2`.
     * `EMAIL_ADDRESS` and `STRING`: optional; for the NOC contact, you can specify only one email address—you don't need to enter your own address because you are included in all notifications



After you order a Dedicated Interconnect connection, Google Cloud sends you a confirmation through email, and allocates ports for you. When the allocation is complete, Google Cloud generates LOA-CFAs for your connections and sends them to you through email. All of the automated emails are sent to the NOC contact and the person who ordered the Dedicated Interconnect connection.

You can use the Dedicated Interconnect connection only after your connections are provisioned and tested for light levels and IP connectivity.

## What's next

  * To create the resources that are required to build a redundant topology, such as VLAN attachments and Cloud Routers, see [Establish 99.99% availability for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-9999-availability) or [Establish 99.9% availability for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-999-availability).

  * To create a Dedicated Interconnect connection, see the [Dedicated Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

  * To learn more about Cloud Interconnect options, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
