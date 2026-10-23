---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/order-google-connections/
title: Order Cross-Cloud Interconnect connections \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:22.974821+00:00
---

# Order Cross-Cloud Interconnect connections  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/order-google-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Order Cross-Cloud Interconnect connections Stay organized with collections  Save and categorize content based on your preferences. 

To start establishing a physical connection between Google Cloud and Alibaba Cloud, order your Cross-Cloud Interconnect connections.

## Before you begin

This section describes required permissions, information, and setup steps.

### Required roles

Before proceeding, you need the required permissions. Ask your administrator to make sure that you have the [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the Identity and Access Management (IAM) documentation.

### Required information

Make sure that you have the names of the remote location and Google Cloud location that you want to use. If you don't have this information, see [Choose your locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/choose-locations). 

### Project selection

If you're using the Google Cloud CLI, set your project ID by using the [`gcloud config set` command](https://docs.cloud.google.com/sdk/gcloud/reference/config/set).
    
    
    gcloud config set project PROJECT_ID

The gcloud CLI instructions on this page assume that you have set your project ID. 

## Order your connections

When you order a Cross-Cloud Interconnect connection, Google reserves a port on a router at the location that you specify. Google later uses this port to create your connection to an Alibaba router.

To satisfy the Cross-Cloud Interconnect [ service level agreement](https://cloud.google.com/network-connectivity/docs/interconnect/sla), order two connections: a primary connection and a redundant one.

After you place each order, you get an email confirming your order.

### Console

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to **Physical connections**](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Click **Set up physical connection**.
  3. In the form that's displayed, select **Cross-Cloud Interconnect connection** , and then click **Continue**.
  4. On the next page, keep the default selection of **Order new Cross-Cloud Interconnect connection** , and then click **Continue**.
  5. On the **Create Cross-Cloud Interconnect connection** page, enter details about the primary connection: 
     * Enter a **Name** for the connection.
     * Optional: Enter a **Description**.
     * In the **Remote cloud provider** field, select **Alibaba Cloud**.
     * In the **Remote location** field, select the Alibaba location.
     * In the **Google Cloud location** field, select the Cross-Cloud Interconnect location.
     * Choose a **Capacity** based on what you're ordering for your Alibaba Cloud Express Connect circuit. For more information about port capacity, see [Port capacity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#port-capacity). 

For help with setting the **Remote location** or **Location** field, see [Choose your locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/choose-locations). 

  6. Click **Next**.
  7. In the next form, enter details about your redundant connection: 
     * Enter a **Name** for the connection.
     * Optional: Enter a **Description**.
     * Leave the **Remote location** and **Google Cloud location** fields set to the same values that you selected for the primary connection.
  8. Click **Next**.
  9. Enter an email address in the **Technical contact** field.
  10. Click **Next**.
  11. Review the order, including the information about billing. If the summary of your details is correct, click **Place order**. If not, go back and edit the connection details. Then return to this step and place the order.
  12. In the order confirmation dialog, click **Submit**.



### gcloud

Use the [`gcloud compute interconnects create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/create).

Related to this command, note the following:

  * Cross-Cloud Interconnect is similar to Dedicated Interconnect in the sense that it does not require you to use a partner provider. For that reason, set the `--interconnect-type` flag to `DEDICATED`.
  * Alibaba Cloud does not support [Link Aggregation Control Protocol (LACP)](https://en.wikipedia.org/wiki/Link_aggregation). 
  * Set `--requested-link-count` to `1` and set `--link-type` to `LINK_TYPE_ETHERNET_10G_LR`. If you need more capacity, order additional Cross-Cloud Interconnect connections. 



Complete the following steps:

  1. Create the primary connection: 
         
         gcloud compute interconnects create CONNECTION_NAME_1 \
             --interconnect-type=DEDICATED \
             --link-type=CAPACITY \
             --requested-link-count=1 \
             --location=GOOGLE_CLOUD_LOCATION_1 \
             --remote-location=REMOTE_LOCATION \
             --description=DESCRIPTION_1 \
             --noc-contact-email=CONTACT_EMAIL_1

Replace the following:

     * `CONNECTION_NAME_1`: the name of the primary Cross-Cloud Interconnect connection
     * `CAPACITY`: the capacity of the connection—for example, `LINK_TYPE_ETHERNET_10G_LR` or `LINK_TYPE_ETHERNET_100G_LR`
     * `GOOGLE_CLOUD_LOCATION_1`: one of the two edge availability zones associated with the Google Cloud location you want to use—for example, `fra-zone1-58`
     * `REMOTE_LOCATION`: the remote location
     * `DESCRIPTION_1`: an optional description of your connection 
     * `CONTACT_EMAIL_1`: an email address that Google can use to contact you
  2. Create the redundant connection: 
         
         gcloud compute interconnects create CONNECTION_NAME_2 \
             --interconnect-type=DEDICATED \
             --link-type=CAPACITY \
             --requested-link-count=1 \
             --location=GOOGLE_CLOUD_LOCATION_2 \
             --remote-location=REMOTE_LOCATION \
             --description=DESCRIPTION_2 \
             --noc-contact-email=CONTACT_EMAIL_2

Replace the following:

     * `CONNECTION_NAME_2`: the name of the redundant Cross-Cloud Interconnect connection
     * `CAPACITY`: the capacity of the connection; this value must be the same as the capacity of the primary connection
     * `GOOGLE_CLOUD_LOCATION_2`: one of the two edge availability zones associated with the Google Cloud location you want to use; do not use the same zone that you used for the primary location—for example, if you chose `fra-zone1-58` for the primary connection, use `fra-zone2-58` for the secondary one
     * `REMOTE_LOCATION`: the same remote location that you specified in the preceding step, when you created the primary connection
     * `DESCRIPTION_2`: an optional description of your redundant connection
     * `CONTACT_EMAIL_2`: an email address that Google can use to contact you about the redundant location

For help with setting the **Remote location** or **Location** field, see [Choose your locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/choose-locations).

[ Previous arrow_back  Choose your locations  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/choose-locations)

[ Next Order Alibaba Cloud ports  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/order-alibaba-ports)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
