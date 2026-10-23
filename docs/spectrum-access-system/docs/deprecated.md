---
url: https://docs.cloud.google.com/spectrum-access-system/docs/deprecated/
title: Spectrum Access System has been deprecated \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:48.025163+00:00
---

# Spectrum Access System has been deprecated  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/deprecated/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)



Send feedback 

#  Spectrum Access System has been deprecated Stay organized with collections  Save and categorize content based on your preferences. 

Spectrum Access System has been deprecated. We are exiting this business to focus our engineering efforts on high-impact innovation that will better serve the needs of our Google Cloud customers. To allow time for migration to other SAS solutions, Spectrum Access System continues to operate until June 10, 2027.

## Migrating from Spectrum Access System to another SAS solution

To migrate from Spectrum Access System to another SAS solution, use SAS Portal API. If you don't have access to the SAS Portal API, complete the steps in this section to gain access.

### Pre-requisites

Before you can gain access to the SAS Portal API, you must have the following:

  * Access to a Google Cloud project.
  * Access to Google Cloud CLI.
  * Access to the [SAS Portal](https://wirelessconnectivity.google.com/sas).



### Obtaining access to the SAS Portal API

To obtain access to the SAS Portal API, you must do the following:

  1. Enable the SAS Portal API in the target Google Cloud project.

  2. Configure a service account:

     1. Create the service account.

     2. Grant the **Owner** role to the service account.

     3. Generate keys for the service account.

  3. Add the service account email as an administrator in the SAS Portal.

  4. Activate the service account using gcloud CLI.

  5. Obtain the access token.

  6. Test your configuration.




Complete the steps in this section to configure access to the SAS Portal API:

  1. Access the Google Cloud console and select your target Google Cloud project.

  2. Enable the required APIs:

     1. Navigate to the **Enabled APIs & services** page.

     2. At the top of the page, click **ENABLE APIS AND SERVICES**.

     3. Search for **SAS Portal API**.

     4. Enable the **SAS Portal API**.

  3. In the **Enabled APIs & services** page, select the **SAS Portal API**.

  4. Select the **Credentials** tab.

  5. Click **Create Credentials** \--> **Service account**.

  6. In the **Create service account** page, do the following:

     1. Specify a meaningful name for the service account, then click **CREATE AND CONTINUE**.

     2. From the **Select a role** drop-down list, select **Basic** \--> **Owner** , and click **CONTINUE**.

     3. Click **DONE** to finish creating the service account.

  7. Navigate to the **Credentials** section of the page.

  8. Select the service account you just created. 

  9. Select the **Keys** tab.

  10. Click **ADD KEY** \--> **Create a new key**.

  11. For **Key type** select **JSON** and click **CREATE**. This triggers a download of a file containing the key in JSON format. Save this file; you will use it to activate the service account and generate your access token.

  12. Navigate to the **Credentials** section of the page.

  13. Copy the full email address of the service account you created earlier.

  14. Access the [SAS Portal](https://wirelessconnectivity.google.com/sas).

  15. In the SAS Portal, do the following:

     1. Select your organization.

     2. Click the **Lock/Unlock** (padlock) button to unlock the form.

     3. Click the **Add** (plus) button to access the **User Management** section.

     4. Click **Admin** and paste the full email of the service account you copied earlier.

     5. Click **Share**.

     6. Click the **Lock/Unlock** (padlock) button to lock the form.

  16. Activate the service account using the following gcloud CLI command:
         
         gcloud auth activate-service-account --key-file KEY_FILE
         

Replace `KEY_FILE` with the full path and name of the JSON key file you downloaded earlier.

  17. Print the access token using the following gcloud CLI command:
         
         gcloud auth print-access-token
         

  18. Test your configuration using the following command:
         
         curl -X GET -H "X-Goog-User-Project: PROJECT_ID"  -H "Content-Type: application/json" \
           -H "Authorization: Bearer ACCESS_TOKEN" "https://prod-tt-sasportal.googleapis.com/v1alpha1/customers"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `ACCESS_TOKEN`: the access token you printed earlier.



### Select a new SAS solution

You can transition to another SAS solution any time before June 10, 2027. A complete list of FCC-authorized SAS administrators is available on the [WInnForum website](https://cbrs.wirelessinnovation.org/sas-administrators).

### Export your data

You can export your current network data and device configurations using the [Google SAS Portal API](https://developers.google.com/spectrum-access-system/reference/rest/v1alpha1/customers.devices/list).

To gain access to the API, follow the steps in [SAS Portal API Usage](https://docs.cloud.google.com/spectrum-access-system/docs/X).

### Deregister your devices

After you've migrated to a new SAS solution, use the [Spectrum Access System Portal](http://g.co/sasportal) to deregister all of your all of your Citizens Broadband Radio Service Devices (CBSDs) from Spectrum Access System.

### Get migration support

To get help with migrating to another SAS solution, contact [Spectrum Access System support](mailto:sas-support@google.com).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
