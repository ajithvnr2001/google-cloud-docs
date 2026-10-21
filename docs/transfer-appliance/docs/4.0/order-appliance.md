---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/order-appliance/
title: Order Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:53.936226+00:00
---

# Order Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/order-appliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Guides ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide)



Send feedback 

#  Order Transfer Appliance Stay organized with collections  Save and categorize content based on your preferences. 

You can order Transfer Appliance from the Google Cloud console. To order an appliance, enable the Transfer Appliance API and add the required Identity and Access Management (IAM) permissions to access the ordering page.

## Enable Transfer Appliance API

Enable the Transfer Appliance API.

[Transfer Appliance API](https://console.cloud.google.com/apis/library/transferappliance.googleapis.com)

## Enable required permissions

To get the permissions that you need to order Transfer Appliance and then view order information in the Google Cloud console, ask your administrator to grant you the following IAM roles on Transfer Appliance: 

  * Access to order Transfer Appliance: 
    * [Cloud KMS Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.admin) (`roles/cloudkms.admin`)
    * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
    * [Transfer Appliance Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.admin) (`roles/transferappliance.admin`)
  * Read-only access to order status information: [Transfer Appliance Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/transferappliance#transferappliance.viewer) (`roles/transferappliance.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Order Transfer Appliance

Once the required permissions are granted, go to the Transfer Appliance order page:

  1. On the **Order appliance** page, enter your delivery location and choose **Transfer Appliance** for the appliance type.

[Go to Transfer Appliance ordering](https://console.cloud.google.com/transfer/appliance)

  2. In the **Choose hardware specs** page, select storage capacity for the appliance and form factor. Choose one of the following types of connectivity options you want on the Transfer Appliance. Hardware specs cannot be changed after the order has been placed.

     * **Enabled** connectivity: Lets you set the appliance in [online mode](https://docs.cloud.google.com/transfer-appliance/docs/4.0/online-transfer#set_to_online_mode) and perform data transfers remotely.

     * **Disabled** connectivity: Blocks the appliance from going online. Data is transferred to the Transfer Appliance and must be shipped back to Google to upload data from the appliance to Cloud Storage.

  3. In the **Configure appliance settings** page

     * Enter a name for your appliance
     * Enter or Browse destination Cloud Storage bucket for the data to be ingested into from the appliance.
     * Choose the encryption type 
       * GMEK - Google Managed Encryption key
       * CMEK - Customer Managed Encryption key. Create and authorize the Transfer Appliance Service Agent to view and decrypt data during offline ingestion.
  4. In the **Enter contact and delivery information** page, enter contact and delivery details.

  5. In the **Review order** page, confirm that the entered information is correct and click **Submit order**.




Ordered appliances can be found in the [Google Cloud console](https://console.cloud.google.com/appliances). You can view order details such as Appliance ID, appliance status, appliance model, order status, and the date you placed the order.

## Next steps

### Prepare permissions and access

Complete [project setup](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide#project-setup-and-key-download) before the appliance gets delivered.

### Prepare Required Tools

Make sure there is side cutters or other wire cutting tool capable of cutting wire with a diameter of 2.5 millimeters (0.1 in) beforehand, to break or cut the tamper-evident wire tag attached to the appliance.

### Track Transfer Appliance

You can track your appliance's shipment, either to you or back to Google, by viewing the tracking details on the [orders](https://console.cloud.google.com/appliances/orders) page. On this page, select your order and then review the details under the **Shipments** tab.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
