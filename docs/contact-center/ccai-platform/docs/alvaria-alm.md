---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/alvaria-alm/
title: Alvaria Advanced List Management integration \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:59.080699+00:00
---

# Alvaria Advanced List Management integration  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/alvaria-alm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Alvaria Advanced List Management integration Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to integrate Alvaria Advanced List Management (ALM) with the Contact Center AI Platform (CCAI Platform) outbound dialer. This integration lets you combine Alvaria's list and campaign management capabilities with the dialing capability of CCAI Platform. The integration exchanges contact and result files through a shared Cloud Storage bucket.

This configuration provides the following benefits:

  * **Continuous campaign management** : Continuously feed contact files from ALM to the CCAI Platform outbound dialer. Pause, stop, and resume campaigns based on business needs.
  * **Flexible delimiter support** : The integration supports various delimiters for contact files, including commas, pipes, tabs, and semicolons.
  * **Branded caller ID** : The integration supports the use of branded caller IDs. If this information is included in the contact data, the CCAI Platform dialer displays the brand to the end-user.



## How the integration works

The integration operates through a continuous cycle of file exchanges between Alvaria ALM and CCAI Platform.

  1. **Contact file delivery** : Alvaria ALM prepares contact files and delivers them to the specified Cloud Storage location. These files are identified by the **Contact list file prefix** that you configure.
  2. **File pick-up** : After a new campaign is set up in CCAI Platform using the specified **Contact list file prefix** and activated, the system automatically detects when new files that match the specific prefix are available in the Cloud Storage location.
  3. **Data import and dialing** : CCAI Platform reads the contact data from the files and adds the contacts to the corresponding campaign and dials out to the specified `@NUMBER` in the ALM contact file. If the Alvaria Advanced Outreach (AO) contact file contains an `@ANI` field, it is mapped to the **Outbound Number** field in the CCAI Platform outbound dialer. If the passed outbound number is not registered on CCAI Platform, the system uses the default outbound number. The `FIRST\_NM` and `LAST\_NM` fields from the AO contact file display in the call adapter as the end-user's name after the call is connected. If both fields are blank, the `@ACCOUNT` value displays instead.
  4. **File deletion** : After CCAI Platform successfully processes a contact file, it is deleted from the Cloud Storage location.
  5. **Result file generation** : After a dialing attempt, CCAI Platform creates a result file containing contact outcomes and disposition information (both system and agent codes). This file uses the return file prefix that you configure.
  6. **Result file delivery** : CCAI Platform puts the result file in the same Cloud Storage bucket for Alvaria to retrieve.
  7. **Result processing** : Alvaria ALM retrieves these result files, parses the data, and updates the contact and campaign records. This lets Alvaria manage lists based on the outcomes provided by CCAI Platform. AO deletes the result file after parsing the data, and updates its contact and campaign records.



## Before you begin

Ensure you have the following:

  * An active Alvaria ALM account
  * A Cloud Storage bucket 
    * The external list should be enabled.
  * The **Campaigns > Campaigns Manager** permission



## Enable the Alvaria ALM integration

Enable the integration globally for your instance.

To enable the Alvaria ALM integration, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.
  2. Locate the Alvaria ALM Integration section and click the toggle to the on position. The global file pick-up and authentication settings appear.
  3. Enter the **GCS Bucket Name** for your designated Cloud Storage bucket.
  4. Under **Service Account Key** , upload the JSON file containing your Google Cloud service account credentials.
  5. Optional: Enter a specific **Folder path** within the Cloud Storage bucket where files are exchanged.
  6. Click **Save**.



The integration is active for your instance. The Alvaria ALM campaign type is available in the campaign manager.

## Configure Alvaria ALM

In your Alvaria ALM environment, you need to perform several configuration steps to prepare your campaigns to deliver contact files to the designated Cloud Storage bucket. For detailed instructions, see [Alvaria Advanced Outreach System Configuration](https://nh4osotdanwob39y5u.alvaria.com/go/aspect/premiseportfolio.aspectalm.ao24.aoandcxintegrationguide.configuration.outreachconfiguration.advancedoutreachconfiguration).

Here is a high-level overview of the steps for configuring Alvaria ALM:

  1. **Campaign setup** : Create and configure a campaign.
  2. **Cloud Storage location** : Specify the Cloud Storage location where contact files are to be stored.
  3. **System environment variable** : Set the **CLOUD_VENDOR** environment variable to `GCP`.
  4. **Batch dialer configuration** : Configure the batch dialer, confirming access to the Cloud Storage location. Ensure the destination path is the full URI path to the Cloud Storage bucket.
  5. **Service creation** : Define a service and specify the batch resulting filename.
  6. **Strategy building** : Define a strategy that includes how lists are defined.
  7. **List and service parameters** : Define parameters for the batch dialer strategy, such as call flow, don't call options, batch size, and interval.
  8. **Timezone management** : Configure timezone management on the ALM side for Alvaria ALM campaign types. CCAI Platform doesn't support the population of the time zone field using CSV from Alvaria unless it's provided in the timezone code format that's defined on the CCAI Platform portal.
  9. **List activation** : Select the lists to be dialed against a specific service and start the list.



After a list is activated, AO begins delivering contact records as files to the configured storage location for CCAI Platform to process.

## Create a campaign

After the global integration is enabled, you can create a campaign in CCAI Platform to process files from Alvaria.

To create a campaign, follow these steps:

  1. In the CCAI Platform portal, click **Campaigns**. If you don't see the **Campaigns** menu, click menu **Menu**.
  2. Select **Add Campaign**. The **Add Campaign** dialog appears.
  3. In the **Campaign Name** field, enter a unique name for your campaign.
  4. In the **Campaign Type** field, select **Alvaria ALM**. Additional configuration fields appear.
  5. Next to **Campaign Folder** , confirm the root folder path. This field is uneditable but displays the full path from which contact files are retrieved as specified in Alvaria ALM Integration settings.
  6. From the **Select file's delimiter** menu, select the delimiter that your Alvaria contact files use. Options include **comma** , **pipe** , **tab** , and **semicolon**. Alvaria uses a pipe as its default delimiter.
  7. In the **Contact list file prefix** field, enter a unique prefix to identify incoming contact files from Alvaria for your existing campaign.
  8. In the **Return file prefix** field, enter the prefix that CCAI Platform uses for the result files it generates.
  9. Click **Save**.



The new campaign is created and ready to process files. Contact files are loaded as they become available in the Cloud Storage bucket. The Alvaria campaign continues to pick up files with the specified contact list file prefix and dial out until you manually pause it on the **Campaign Manager** page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
