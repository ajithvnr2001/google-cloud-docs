---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/order-alibaba-ports/
title: Order Alibaba Cloud ports \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:09.474667+00:00
---

# Order Alibaba Cloud ports  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/order-alibaba-ports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Order Alibaba Cloud ports Stay organized with collections  Save and categorize content based on your preferences. 

After you order your Cross-Cloud Interconnect connections, order your Alibaba Cloud Express Connect ports. These ports establish private, high-bandwidth connectivity between your Google Cloud and Alibaba Cloud environments. To ensure a highly available connection, you must order both a primary port and a redundant port.

**Caution:** Use the following procedure twice—once to create the primary port and again to create the redundant port.

## Order Express Connect ports

For each of your Cross-Cloud Interconnect connections, you need an Express Connect port.

###  Console 

  1. Sign in to the Alibaba Cloud Express Connect console.
  2. On the **Express Connect** page, click **Create Physical Connection**.
  3. For **Region** , select the city that you want to connect to by choosing one of the following in the **Connectivity Provider** menu:

     * For the **China (Hong Kong)** region, select **Other (Chinese Mainland)**.
     * For all other regions, select **Connectivity Provider Outside Chinese Mainland**.
  4. For **Access Point** , select the Alibaba Cloud name for the remote location.

  5. For **Port Type** , select **10 GE Single-Mode Optical Port**.

  6. Leave **Redundant Physical Connection ID** empty when ordering the primary port. You will set it when ordering the redundant port.

  7. Check the box that you have read and understood the billing rules.

  8. Click **OK** to place the order.

_Repeat the same process when ordering the redundant port_. However, for the second port, set the **Redundant Physical Connection ID** menu to the primary port that you previously ordered.

Wait a few minutes for the ports to be allocated.

  9. After the port is allocated, click **Apply for LOA**.

  10. For **Company Name** , enter **Google Cloud**.

  11. For **Construction Company that Enters Data Centers of Alibaba Cloud** , enter **Google Cloud**.

  12. For **Leased Line Type** , select **Fiber Connection**.

  13. For **Construction Schedule** , select the date tomorrow.

  14. For **Leased Line Bandwidth** in Mbps, enter **10000**.

  15. The menu requires that you enter information for a field engineer even though it is not used:

     1. Click **Add Field Engineer**.
     2. For **Name** , enter **NotApplicable**.
     3. For **Contact Information** , enter your phone number.
     4. For **ID Number** , enter **Unknown colo facility**.
     5. For **Gender** , enter your gender. 
  16. Click **OK**.

  17. On the page that appears, click **OK**.




## Generate LOAs

For Google to provision your connection, it must have a letter of authorization (LOA) for each of your Alibaba Cloud ports.

After you order the Express Connect port, the port waits for a review process that can take between ten minutes and two business days. After review completes, click the button to download the LOA document. If you are unable to download an LOA document after two business days, open a support ticket.

## Send the LOAs to Google

After you order your Cross-Cloud Interconnect connections, you should receive confirmation email messages from Google. Each of these messages includes instructions for sending your Alibaba Cloud LOAs to Google. Now that you have the LOAs, do the following:

  1. Decide which Alibaba Cloud Express Connect port must be connected to each Cross-Cloud Interconnect connection.

  2. Locate the LOA document for that port.

  3. Respond to each of the Google emails, and attach the appropriate LOA documents.




Make a note of the instructions that you provide to Google regarding which Cross-Cloud Interconnect port connects to which Alibaba Cloud port. You need this information later in the process when you configure your Alibaba Cloud resources.

After you respond to both emails, Google sends you an email acknowledging receipt of the LOAs.

Still later, after Google provisions your Cross-Cloud Interconnect connections, you receive another set of emails stating that the work is complete. At that point, Alibaba Cloud has not yet provisioned the pigtail for the Express Connect port.

  1. Click **Confirm Delivery**.
  2. For **Leased Line ID/Cable ID** , enter the connection ticket ID that Google provides you.
  3. For **ODF Port Specification** , enter the Patch Panel information from the LOA document that you previously downloaded.
  4. Click **OK**.



Alibaba Cloud completes the pigtail connection within four business days. Google tests your Cross-Cloud Interconnect once each day to check for connection completion. After the connection is detected, Google sends an email that your port is ready to use.

## Check the status of your Google Cloud ports

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Click the name of your Cross-Cloud Interconnect connection.

  3. On the **Interconnect details** page, locate the **Link circuit info** table.

  4. Check the **Receiving Optical Power** and the **Transmitting Optical Power** columns. The value in these columns must be **OK**.




[ Previous arrow_back  Order Cross-Cloud Interconnect connections  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/order-google-connections)

[ Next Configure your Google Cloud resources  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/configure-google-resources)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
