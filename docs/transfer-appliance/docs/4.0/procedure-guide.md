---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide/
title: High-level overview \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:41.577166+00:00
---

# High-level overview  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Guides ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide)



Send feedback 

#  High-level overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the high-level procedure for ordering, installing, and returning Transfer Appliance. It includes the expected interactions between you and Google.

## Before you begin

Before ordering, use the following checklist to ensure that your environment supports using Transfer Appliance.

  * Review the [Transfer Appliance specifications](https://docs.cloud.google.com/transfer-appliance/docs/4.0/specifications) and confirm the following for your facility:

    * Power capabilities
    * Cooling capabilities
    * Physical space requirements
  * Identify the servers and the folders that contain data to transfer.

  * Confirm that employees performing the transfer have the correct permissions to access the data for the transfer.

  * Review that your data meets the following criteria:

    * Individual files are less than 5 terabytes (TB) in size.

    * File names follow [object naming guidelines](https://docs.cloud.google.com/storage/docs/objects#naming).

    * Files are regular files or Unix-style hidden files. Unix-style hidden files start with a `.` character.

    * Folders contain files. Empty folders are not created in Cloud Storage, because objects don't reside within subdirectories within a Cloud Storage bucket.

    * The maximum path length is 1024 bytes, which includes the optional object prefix specified when you provide Transfer Appliance Team with bucket configuration details.




## Prepare for the appliance

To prepare for Transfer Appliance, do the following:

  * When you're ready to transfer your data, [apply for Transfer Appliance](https://console.cloud.google.com/transfer/appliance) from the same Google Cloud project as your destination Cloud Storage bucket. You must have the [required permissions](https://docs.cloud.google.com/transfer-appliance/docs/4.0/order-appliance#enable_required_permissions) on the project to successfully apply for the Transfer Appliance.

  * When applying for Transfer Appliance, you can choose to use your appliance in either offline mode or online mode.

    * Offline mode allows you to copy data to the appliance. When the appliance is full, you send the appliance back to us.

    * Online mode enables streaming data copied to the appliance to your Cloud Storage bucket.

  * If you select online mode, you can toggle between offline and online mode once you have the appliance. If you select offline mode, you cannot toggle modes once you receive your appliance.




## Project Setup and Key Download

  1. Ensure you have the following permissions:

     * iam.serviceAccounts.getIamPolicy
     * resourcemanager.projects.getIamPolicy
     * resourcemanager.projects.setIamPolicy
     * storage.buckets.getIamPolicy
     * storage.buckets.setIamPolicy

You will be able to get these required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles). You can search for [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) for a given permission.

  2. Complete the project setup:

     1. Go to [appliances page](https://console.cloud.google.com/appliances)
     2. Find and select the appliance
     3. Click on the `Open Setup Checklist` button
     4. Complete the following steps: 
        1. `Enable API` will enable the required APIs for the appliance
        2. `Authorize the service accounts` will create service accounts used for online transfer and authorize service accounts to the output bucket
        3. (only for online transfer) [Create and Download](https://docs.cloud.google.com/transfer-appliance/docs/4.0/online-transfer#download-appliance-sa-key) the key of the appliance service account that is created during `Authorize the service accounts`



## Receive the appliance

To receive an appliance, follow these steps:

  1. Track the appliance shipped to you. We'll email you when it is delivered to your shipping address.

You can also track your shipment directly: [Track shipment](https://docs.cloud.google.com/transfer-appliance/docs/4.0/order-appliance#track)

After you receive the appliance, [confirm the Appliance Receipt](https://docs.cloud.google.com/transfer-appliance/docs/4.0/receive-appliance#confirm_receipt). Then, [verify the package contents](https://docs.cloud.google.com/transfer-appliance/docs/4.0/receive-appliance) to ensure that you have everything required to use the appliance.

**Important:** If you've received this email and didn't receive your appliance, contact Transfer Appliance Team for help.
  2. Before connecting the appliance to your network, [validate that it hasn't been tampered with during shipping](https://docs.cloud.google.com/transfer-appliance/docs/4.0/receive-appliance#validate) and submit the Transfer Appliance Attestation Passcode returned by the appliance in the appliance detail page of the Google Cloud console.

If the device was not tampered with during shipping, the credentials will be displayed in the Google Cloud console. Otherwise, the Google Cloud console will show an error message. If you encounter this error, contact the Transfer Appliance Team at [data-support@google.com](mailto:data-support@google.com) for assistance.

  3. After receiving login credentials from Google Cloud console, do the following:

     1. [Configure IP network ports](https://docs.cloud.google.com/transfer-appliance/docs/4.0/ip-network-ports).
     2. [Connect the appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/receive-appliance#connecting) to your network.
     3. [Configure the appliance software](https://docs.cloud.google.com/transfer-appliance/docs/4.0/receive-appliance#configure-appliance).



## Copying data to the appliance

To capture your data, follow these steps:

  1. Use copy tools of your choice to [copy data to the appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/transfer-data).

     * If you selected an online-capable appliance and enabled online copy on the appliance: The appliance streams the data you copy to the appliance to your Cloud Storage bucket. Files and empty directories are deleted from the appliance after they're successfully copied to your Cloud Storage bucket.

     * If you selected an offline-only device or disabled online copy on the appliance: After you complete all copying to the appliance, [finalize the copied data](https://docs.cloud.google.com/transfer-appliance/docs/4.0/return-appliance#finalizing) to prepare for shipping.

     * All files copied to the appliance must comply with Cloud Storage [file size limits](https://docs.cloud.google.com/storage/quotas#objects) and [naming guidelines](https://docs.cloud.google.com/storage/docs/naming-objects).

  2. Verify that you copied all data to the appliance before finalizing.

  3. [Finalize copied data](https://docs.cloud.google.com/transfer-appliance/docs/4.0/return-appliance#finalizing).

  4. Enter the passcode returned by the `ta finalize` command in the form included in the email titled _Google Transfer Appliance Return Instructions_ sent by the Transfer Appliance Team.

To view the passcode again, run `ta status`.

The Transfer Appliance Team responds with the shipping label for the Transfer Appliance for the given passcode.

**Note:** The passcode is specific to each appliance. If you have several Transfer Appliances, verify that the session ID printed on the shipping case matches the session ID of the passcode you are using.
  5. Once you receive the shipping label, turn off the appliance and disconnect all cables to it.

  6. Once you have the shipping label, [package and return the appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/return-appliance).




## Complete your copy

After returning the appliance, do the following to complete your transfer:

  1. Verify that we received your appliance.

Transfer Appliance Team emails you when we receive your appliance at our data transfer center. We'll start transferring data from the appliance to the destination Cloud Storage bucket indicated in [the appliance order form](https://docs.cloud.google.com/transfer-appliance/docs/4.0/order-appliance#order).

  2. Verify that we completed your transfer.

Transfer Appliance Team emails you when we've completed transferring data from the appliance to your Cloud Storage bucket.

  3. [Validate your data](https://docs.cloud.google.com/transfer-appliance/docs/4.0/access-data) in the destination Cloud Storage bucket to verify that your data transferred as you expected. We recommend that you don't delete your source data until you verify that it successfully transferred to your Cloud Storage bucket.

     * Data that's been transferred from your appliance is displayed in your Cloud Storage bucket.

     * The following additional directories are created:

       * A `storage-transfer` directory that contains your Storage Transfer Service logs.
       * A `transferappliance` directory that logs successful and failed transfers from the appliance.
       * Sometimes, a `cloud-ingest` directory that is used to coordinate the data uploaded from the appliance to your destination Transfer Appliance bucket.

You can delete these directories once your data transfer is complete and the data is fully available in your Transfer Appliance bucket.

  4. Optional: You may request a Transfer Appliance wipe certificate to verify that we've securely wiped all data after copying it to Cloud Storage. If you're interested in a wipe certificate, contact Transfer Appliance Team.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
