---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chrome-enterprise-premium/
title: Collect Chrome Enterprise Premium Context Access Aware Data \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:59.886963+00:00
---

# Collect Chrome Enterprise Premium Context Access Aware Data  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chrome-enterprise-premium/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Chrome Enterprise Premium Context Access Aware Data

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can connect your organization to Google Security Operations, enable the Identity-Aware Proxy (IAP) API, and set up feeds to ingest the following data to Google Security Operations. The feeds include Chrome Enterprise Premium content specific to IAP and context access aware data.

  * [Google Cloud Logs](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs)
  * [Cloud Identity Devices](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices)
  * [Cloud Identity Device Users](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers)



## Before you begin

Before you set up feeds to ingest Chrome Enterprise Premium data, complete the following tasks:

  * Connect your Google Cloud organization to Google Security Operations by completing the following sections: 
    1. [Enable telemetry ingestion to Google Security Operations](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs#enabling_gcp_telemetry_ingestion).
    2. [Enable the export of Google Cloud logs to Google Security Operations](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs#exporting_google_cloud_logs_to_chronicle).
  * Enable the Cloud Identity API and create a service account to authenticate the API.
  * Create a domain-wide delegation.
  * Create a user for impersonation.



### Enable the Cloud Identity API and create a service account

  1. In the Google Cloud console, select the Google Cloud project for which you want to enable the API, and then go to the **APIs & Services** page:

[Go to **APIs & Services**](https://console.cloud.google.com/apis/dashboard)

  2. Click **Enable APIs and Services**.

  3. Search for "Cloud Identity API".

  4. In the search results, click **Cloud Identity API**.

  5. Click **Enable**.

  6. Create a service account:

     1. In the Google Cloud console, select **IAM & Admin > Service Accounts**.
     2. Click **Create service account**.
     3. On the **Create service account page** , enter a name for the service account.
     4. Click **Done**.
  7. Select the service account that you created.

  8. Copy and save the ID that appears in the **Unique ID** field. You use this ID when you create a domain-wide delegation.

  9. Select the **Keys** tab.

  10. Click **Add key > Create new key**.

  11. Select **JSON** as the **Key type**.

  12. Click **Create**.

  13. Copy and save the JSON key. You use this key when you set up feeds.




For more information, see [Enable the Cloud Identity API and create a service account to authenticate the API](https://docs.cloud.google.com/identity/docs/how-to/setup-devices#enabling_the_api_and_setting_up_credentials).

### Create a domain-wide delegation

To control API access for the service account using domain-wide delegation, do the following:

  1. From the Google Admin console Home page, select **Security > Access and Data Controls > API Controls**.
  2. Select **Domain-wide delegation > Manage Domain-Wide Delegation**.
  3. Click **Add new**.
  4. Enter the service account client ID. The service account client ID is the unique ID that you obtained when you created a service account.
  5. In **OAuth scopes** , enter `https://www.googleapis.com/auth/cloud-identity.devices.readonly`.
  6. Click **Authorize**.



For more information, see [Control API access with domain-wide delegation](https://support.google.com/a/answer/162106#zippy=%2Cset-up-domain-wide-delegation-for-a-client)

### Create a user for impersonation

  1. From the Google Admin console Home page, select **Directory > Users**.
  2. To add a new user, do the following: 
     1. Click **Add new user**.
     2. Enter a name for the user.
     3. Enter the email address associated with the user.
     4. Click **Create** , and then click **Done**.
  3. To create a new role and assign a privilege, do the following: 
     1. Select the newly created username.
     2. Click **Admin roles and privileges**.
     3. Click **Create custom role**.
     4. Click **Create new role**.
     5. Enter a name for the role.
     6. Select **Services > Mobile Devices Management**, and then select the **Manage Devices and Setting** privilege.
     7. Click **Continue**.
  4. To assign the role to the user, do the following: 
     1. Click **Assign Users**.
     2. Navigate to the newly created user and click **Assign Role**.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Field name** (for example, **Chrome Enterprise Premium logs**).
  5. Select **Third party API** as the **Source type**.
  6. In the **Log type** list, select either **GCP Cloud Identity Devices** or **GCP Cloud Identity Device Users**.
  7. Click **Next**.
  8. On the **Input parameters** tab, specify the following details:

**Note:** The options that appear on the **Input parameters** tab depend on the source and log type that you specified on the **Set Properties** tab.
     * **OAuth JWT endpoint**. Enter `https://oauth2.googleapis.com/token`.
     * **JWT claims issuer**. Specify <insert_service_account@project.iam.gserviceaccount.com>. This is the service account you created in the section Enable the Cloud Identity API and create a service account.
     * **JWT claims subject**. Enter the email of the user that you created in the section Create a user for impersonation.
     * **JWT claims audience**. Enter `https://oauth2.googleapis.com/token`.
     * **RSA private key**. Enter the JSON key that was created when you created a service account to authenticate the API.
     * **API version**. Optional. You can leave this field blank.
  9. Click **Next**.

  10. On the **Finalize** tab, review the values that you entered and then click **Submit**.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
