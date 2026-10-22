---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/manage-security-certificates/
title: Manage security certificates in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:35.392021+00:00
---

# Manage security certificates in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/manage-security-certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Manage security certificates in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

The backup/recovery appliance uses digital certificates to ensure secure communication between appliances. All entities in a configuration must have matching security certificates in order to establish a secure relationship.

There are two methods to establish a secure relationship between entities:

  * Exchange certificates between two entities
  * Download a certificate from each appliance and then upload them to the other appliance.



## View certificates

Use these instructions to view the certificate of all entities connected to the local appliance in the non-sharing mode:

  1. In the appliance management console, click the **Manage** tab and select **Appliances** from the drop-down menu.
  2. Select an appliance.
  3. Click **Configure Appliance** to open the **Appliance Configuration** page.
  4. Go to **Appliance Settings > Certificates**. A list of all appliances connected to the local appliance is displayed, along with the corresponding certificates.



## Delete a certificate

You might need to delete an existing certificate in the following situations:

  * To disconnect the communication.
  * When an existing certificate becomes invalid. In such cases, you might need to remove the old one and upload the new certificate.



Use these instructions to delete a security certificate:

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu.
  2. Select an appliance.
  3. Click **Configure Appliance** to open the **Appliance Configuration** page.
  4. Go to **Appliance Manager > Certificate**.
  5. Select the certificate and click the **Remove** button.
  6. Click **Yes** in the confirmation dialog.



## Download a certificate

Use these instructions to download a security certificate:

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu.

The **Appliances** page opens.

  2. Select an appliance.

  3. Click **Configure Appliance** to open the **Appliance Configuration** page.

  4. Click the gear icon in the bottom left corner of the page and select **Download Certificate** from the drop-down menu.

**Note:** To join this backup/recovery appliance to another, you will have to upload this certificate to the other appliance.



## Upload a certificate

Use these instructions to upload a security certificate:

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu.

The **Appliances** page opens.

  2. Select an appliance.

  3. Click **Configure Appliance** to open the **Appliance Configuration** page.

  4. Click the gear icon in the bottom left corner of the page and select **Upload Certificate** from the drop-down menu. The **Choose a certificate to import** window opens.

  5. Browse and select the certificate file and then click **Open**. The certificate is listed in the certificate store at **Manage** > **Appliances** > **System** > **Configuration** > **Appliance Settings** > **Certificates**.




## Exchange certificates

Certificate exchange is a quick way to download certificates when you have secure administrative access to both appliances.

Use these instructions to exchange security certificates between two backup/recovery appliances:

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu.

The **Appliances** page opens.

  2. Select an appliance.

  3. Click **Configure Appliance** to open the **Appliance Configuration** page.

  4. Click the gear icon in the bottom left corner of the page and select **Certificate Exchange** from the drop-down menu.

The **Exchange Certificates** dialog appears.

  5. Enter the IP address of the remote appliance.

  6. In the space provided, enter the administrator password to access the remote appliance.

  7. Click **Exchange**. The security certificates are exchanged between the local appliance and the remote appliance. After the certificates are exchanged, the local appliance can be joined with the remote appliance.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
