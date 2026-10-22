---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/order-oci-ports/
title: Order OCI ports \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:42.402552+00:00
---

# Order OCI ports  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/order-oci-ports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Order OCI ports Stay organized with collections  Save and categorize content based on your preferences. 

After you order your Cross-Cloud Interconnect connections, order your Oracle Cloud Infrastructure (OCI) ports.

## Before you begin

Make sure that you have sufficient quota to order the FastConnect resources that you need.

## Order FastConnect ports

For each of your Cross-Cloud Interconnect connections, you need an OCI port.

**Caution:** Use the following procedure twice—once to create the primary port and again to create the redundant port.

###  Console 

**Note:** For the most up-to-date information about how to order a FastConnect port, see [FastConnect: Colocation with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm) in the OCI documentation.

  1. Sign in to the OCI console.

  2. Make sure that the **Regions** list shows the region where you want to purchase OCI ports.

  3. In the menu menu, select **Networking**. Under **Customer connectivity** , select **FastConnect**.

  4. Click **Create FastConnect**.

  5. On the **Connection type** page, select the **FastConnect direct** box, and then click **Next**.

  6. Fill out the **Configuration** page:

     1. Enter a name for the connection.
     2. Select a **Compartment**.
     3. Under **Cross-connect type** , select the **Cross-connect group** box. It's important to make this choice even if you do not plan to use LACP. After you do, the page updates to include additional fields.
     4. Enter the **Number of cross-connects** to use for the connection. Choose the same number of links that you specified when ordering your Cross-Cloud Interconnect ports. For example, if you ordered a connection of size 20 Gb/s (2 x 10 Gb/s), enter **2** in this field. If you ordered a 100-Gb/s connection, set this field to **1**.

**Note:** Set this field to reflect the number of links in this cross-connect group. _Setting the number of cross-connects to 2 does not set up redundancy_. To set up redundancy, order two cross-connect groups by following the cross-connect group ordering process twice.
     5. Enter a **Port speed**. Use the same capacity that you selected when ordering your Cross-Cloud Interconnect connections. To view the list of valid capacities, see [Port capacity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#port-capacity). The OCI console might list additional options, but they can't be used with Cross-Cloud Interconnect.

     6. Leave the **Enable MACsec encryption** field cleared. This must be disabled until turn up completes.

     7. Select a **Physical location**.

     8. Specify whether to use the same OCI router as other FastConnect connections by checking the **Specify router proximity** box. This step is important when you order the redundant port. Make sure to place the redundant port on a different router than the primary port. If both ports are placed on the same router, you would lose both connections during maintenance work on the router. Then fill in the related fields that are displayed.

     9. Optional: Use the **Tag namespace** , **Tag key** , and **Tag value** fields to create tags that represent the resource.

  7. Click **Create**.




## Generate LOAs

For Google to provision your connection, it must have a letter of authorization (LOA) for each of your OCI ports.

Use the following procedure for each link that you created. In the OCI interface, links are known as _cross-connects_.

For example, suppose you ordered two FastConnect connections, each of which has two links. In this case, you need four LOA documents.

###  Console 

  1. Sign in to the OCI console.

  2. Make sure that the **Regions** list shows the region where you purchased your FastConnect resources.

  3. In the menu menu, select **Networking**. In the **Customer connectivity** section, select **FastConnect**.

  4. Click the name of the appropriate connection.

  5. In the **Cross-connects** section, click the name of the appropriate link.

  6. On the **Cross-connects** tab, locate the **Letter of Authorization** field. Click the corresponding **View** link.

  7. Click **Print** and follow prompts to print the LOA to a PDF to save it locally.




## Send the LOAs to Google

After you order your Cross-Cloud Interconnect connections, you should receive confirmation email messages from Google. Each of these messages includes instructions for sending your OCI LOAs to Google. Now that you have the LOAs, do the following:

  1. Decide which OCI port should be connected to each Cross-Cloud Interconnect connection.

  2. Locate the LOA documents for that port. The number of relevant LOAs depends on the number of links that you specified for each port. For example, if the port has two links (or cross-connects), then you have two LOAs.

  3. Respond to each of the Google emails, and attach the appropriate LOA documents.




Make a note of the instructions that you provide to Google regarding which Cross-Cloud Interconnect port connects to which OCI port. You need this information later in the process when you configure your OCI resources.

After you respond to both emails, Google sends you an email acknowledging receipt of the LOAs.

Still later, after Google provisions your Cross-Cloud Interconnect connections, you receive another set of emails stating that the work is complete. At that point, the Cross-Cloud Interconnect ports are active, although the OCI ports are not.

When you receive this confirmation, you can finish the required configuration.

## Check the status of your Google Cloud ports

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Click the name of your Cross-Cloud Interconnect connection.

  3. On the **Interconnect details** page, locate the **Link circuit info** table.

  4. Check the **Receiving Optical Power** and the **Transmitting Optical Power** columns. The value in these columns should be **OK**.




At this point, it is normal to see a red checkmark in the **Link State** column.

## Verify and enable OCI ports

Check to see whether your OCI links are all receiving a signal from Google. If they are, enable them.

###  Console 

For each of your links, complete the following steps:

  1. Sign in to the OCI console.

  2. Make sure that the **Regions** list shows the region where you want to purchase OCI ports.

  3. In the menu menu, select **Networking**. In the **Customer connectivity** section, select **FastConnect**.

  4. Click the name of the appropriate FastConnect resource.

  5. Under **Cross-connects** , click the name of the link that you want to verify.

  6. In the **Cross-Connection Information** box, locate the **Light Level Indicator**. Verify that a green checkmark appears next to the field.

  7. If all of the fields appear as expected, click **Activate**.

  8. In the **Confirmation** dialog, click **Activate**.

  9. To verify the activation, go back to the previous page and review the **Cross-connects** table. The value in the **Life Cycle** column should be **Provisioning**.




[ Previous arrow_back  Order Cross-Cloud Interconnect connections  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/order-google-connections)

[ Next Configure your Google Cloud resources  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/configure-google-resources)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
