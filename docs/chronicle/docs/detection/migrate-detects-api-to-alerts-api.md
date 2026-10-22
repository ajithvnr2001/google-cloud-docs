---
url: https://docs.cloud.google.com/chronicle/docs/detection/migrate-detects-api-to-alerts-api/
title: Migrate from CrowdStrike Detects API to Alerts API \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:07.643421+00:00
---

# Migrate from CrowdStrike Detects API to Alerts API  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/migrate-detects-api-to-alerts-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate from CrowdStrike Detects API to Alerts API

**Caution:** CrowdStrike is decommissioning its `Detects API` on September 30, 2025. This API is replaced by the `CrowdStrike Alerts API`.

This section describes how to migrate your configuration to use the Alerts API and prevent disruption to your data ingestion.

#### Who is affected?

This change affects you if you meet both of the following conditions:

  * You have active data feeds using the CrowdStrike Detection Cloud Monitoring API connector, which maps to the `CS_DETECTS` log type.
  * Your configured CrowdStrike API client for this feed doesn't have read privileges for alerts.



To prevent service disruption, complete one of the following procedures before September 30, 2025.

  * Option 1: Update permissions for your existing CrowdStrike API client (Recommended)
  * Option 2: Create and use a new CrowdStrike API client



#### Option 1: Update permissions for your existing CrowdStrike API client (Recommended)

This approach requires configuration changes only in your CrowdStrike Falcon console and has the lowest impact on existing detection rules that reference the `CS_DETECTS` log type.

Before you begin, identify API clients using the Detects API. CrowdStrike provides a dashboard to help you identify API clients that use deprecated endpoints. API clients used by the Google SecOps detection monitoring feed have a user agent string that starts with `Google-Chronicle-Security`.

To set up and use the dashboard, perform the following steps:

  1. Navigate to the [CrowdStrike support article](https://supportportal.crowdstrike.com/s/article/Dashboard-to-track-usage-of-the-deprecated-detects-API) and download the YAML file, titled, **PlannedDecommissionofthedetectsAPI(September30,2025)** , attached at the bottom of the page.
  2. In the Falcon console, navigate to **Next-Gen SIEM** > **Log management** > **Dashboards**.
  3. From the **Create dashboard** list, select **Create new**. ![Create new](https://docs.cloud.google.com/static/chronicle/images/Dashboards_crowdstrike_advisory.png)
  4. Click **Import dashboards**.
  5. Import the YAML file you downloaded. ![YAML file](https://docs.cloud.google.com/static/chronicle/images/Import_Dashboard.png)
  6. On the dashboard, navigate to the **Calls to the deprecated "/detects" API endpoints** table. This table lists the client IDs of all API clients calling the deprecated endpoint.
  7. For each API client ID identified in the previous step, grant the read permission for alerts as shown in the image. ![Read permissions](https://docs.cloud.google.com/static/chronicle/images/readpermissions.png)
  8. In the Falcon console, navigate to **OAuth2 API clients** tab. You might need to go through multiple pages to find a specific client ID.
  9. Select the API client you want to modify, and click **Edit API client**.
  10. In the table on the **Edit API client** form, select the **Read** checkbox for alerts. ![Edit API client form](https://docs.cloud.google.com/static/chronicle/images/OAuth2APIClients.png)
  11. Click **Update client details**.
  12. Verify the changes to ensure that the migration is successful.

     * Confirm that your CrowdStrike feeds in Google SecOps continue to receive data.
     * Check the dashboard in the Falcon console again after 30 minutes. The dashboard should no longer register any calls to the Detects API from the updated client IDs.



### Option 2: Create and use a new CrowdStrike API client

Use this option if you have trouble identifying your existing API client IDs. The Google SecOps connector for the `CS_DETECTS` log type automatically attempts to use the Alerts API first. If the required permissions are missing, it uses the Detects API. By creating a new client with the correct permissions, you can ensure that the connector uses the modern Alerts API.

  1. In the CrowdStrike Falcon console, navigate to the **OAuth2 API clients** section.
  2. Click **create API client**.
  3. In the table on the **Create API client** form, select the **Read** checkbox for alerts.
  4. From the **API client created** form, copy the information in the **Client ID** , **Secret** , and **Base URL** fields.
  5. In Google SecOps, navigate to **SIEM Settings** > **Feeds**.
  6. Locate your CrowdStrike Detection Monitoring (`CS_DETECTS`) feed and click **Edit Feed**.
  7. Replace the existing credentials with the client ID and client secret you copied from the Falcon console.
  8. Review your feed configuration and click **Submit**.
  9. Repeat these steps for each `CS_DETECTS` feed across all your Google SecOps instances.



#### Verify the changes

After updating the feed, verify that the migration was successful:

  * Confirm that your CrowdStrike feed in Google SecOps continues to receive data.
  * Check the dashboard in the Falcon console as described in the recommended method. The dashboard should no longer register any calls to the detects API.



For more details, see the official [CrowdStrike decommissioning notice](https://supportportal.crowdstrike.com/s/article/Tech-Alert-30-Day-Notice-Planned-Decommission-Announcement-of-the-DetectionSummaryEvent-and-detects-API).

### CrowdStrike Detections API deprecation in SOAR integration

The CrowdStrike Falcon SOAR integration used the **Detections** API within its actions and connectors. CrowdStrike's deprecation of this API affects the following actions and connectors:

  * **Add Comment to Detection**
  * **Close Detection**
  * **Update Detection**
  * **CrowdStrike - Detections Connector**



The SOAR CrowdStrike integration already supports the **Alerts** API, which replaces the **Detections** API. To use the new **Alerts** API, you must do the following:

  1. Install the CrowdStrike - Alerts Connector.
  2. Update playbooks to use the **Update Alert** and **Add Alert Comment** actions.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
