---
url: https://docs.cloud.google.com/security-command-center/docs/connect-secops-azure/
title: Connect to Microsoft Azure for log data collection \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:47.180870+00:00
---

# Connect to Microsoft Azure for log data collection  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/connect-secops-azure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Connect to Microsoft Azure for log data collection Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Security Command Center curated detections, threat investigation, and Cloud Infrastructure Entitlement Management (CIEM) capabilities for Microsoft Azure require the ingestion of Microsoft Azure logs using the Security Operations console ingestion pipeline. The Microsoft Azure log types required for ingestion differ based on what you are configuring:

  * CIEM requires data from the Azure Cloud Services (AZURE_ACTIVITY) log type.
  * Curated detections require data from multiple log types. To learn more about the different Microsoft Azure log types, see [Supported devices and required log types](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#azure-supported-devices).



## Curated detections

Curated detections in the Enterprise tier of Security Command Center help identify threats in Microsoft Azure environments using both event and context data.

These rule sets require the following data to function as designed. You must ingest Azure data from each of these data sources to have maximum rule coverage.

  * [Azure cloud services](https://azure.microsoft.com/en-us/free/cloud-services/)
  * [Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/), previously Azure Active Directory
  * [Microsoft Entra ID audit logs](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-audit-logs), previously Azure AD audit logs
  * [Microsoft Defender for Cloud](https://www.microsoft.com/en-us/security/business/cloud-security/microsoft-defender-cloud)
  * [Microsoft Graph API Activity](https://learn.microsoft.com/en-us/graph/use-the-api)



For more information, see the following in the Google SecOps documentation:

  * [Supported devices and required log types for Azure](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#azure-supported-devices): information about the data required by each rule set.

  * [Ingest Azure and Microsoft Entra ID data](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#ingest-azure) and [Create an Azure Event Hub feed](https://docs.cloud.google.com/chronicle/docs/administration/create-azure-feed): steps to collect Azure and Microsoft Entra ID log data.

  * [Curated detections for Azure data](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#azure-curated-detections): summary of the Azure rule sets in the Cloud Threats Category curated detections.

  * [Use curated detections to identify threats](https://docs.cloud.google.com/chronicle/docs/detection/use-curated-detections): how to use curated detections in Google SecOps.




For information about the type of log data that customers with Security Command Center Enterprise can ingest directly to the Google SecOps tenant, see [Google SecOps log data collection](https://docs.cloud.google.com/security-command-center/docs/secops-limits#microsoft-logs).

## Configure Microsoft Azure log ingestion for CIEM

To generate CIEM findings for your Microsoft Azure environment, the CIEM capabilities require data from Azure activity logs for each Azure subscription or management group that needs to be analyzed.

### Before you begin

To export activity logs for your Azure subscriptions or management groups, [configure a Microsoft Azure storage account](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-azure-activity-logs#configure_a_storage_account).

### Configure Microsoft Azure log ingestion for management groups

  1. To configure Azure activity logging for management groups, use the [Management group API](https://learn.microsoft.com/en-us/rest/api/monitor/management-group-diagnostic-settings/create-or-update).

**Note:** The Microsoft Azure portal does not support configuring diagnostic settings for management groups.
  2. To ingest exported activity logs from the storage account, [configure a feed in Security Operations console](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-azure-activity-logs#configure_a_feed_in_to_ingest_the_azure_logs).

  3. Set an **Ingestion label** for the feed by setting **Label** to `CIEM` and the **Value** to `TRUE`.




### Configure Microsoft Azure log ingestion for subscriptions

  1. To configure Azure activity logging for subscriptions, do the following:

     1. In the Azure console, search for **Monitor.**
     2. In the left navigation pane, click the **Activity log** link.
     3. Click **Export Activity Logs**.
     4. Perform the following actions for each subscription or management group for which logs need to be exported: 
        1. In the **subscription** menu, select the Microsoft Azure subscription from which you want to export activity logs.
        2. Click **Add diagnostic setting.**
        3. Enter a name for the diagnostic setting.
        4. In **Log categories** , select **Administrative**.
        5. In **Destination details** , select **Archive to a storage account**.
        6. Select the subscription and storage account that you created, and click **Save**.
  2. To ingest exported activity logs from the storage account, [configure a feed in Security Operations console](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-azure-activity-logs#configure_a_feed_in_to_ingest_the_azure_logs).

  3. Set an **Ingestion label** for the feed by setting **Label** to `CIEM` and the **Value** to `TRUE`.




## What's next

  * To enable CIEM, see [Enable the CIEM detection service](https://docs.cloud.google.com/security-command-center/docs/ciem-enable-service).
  * To learn more about CIEM features, see [Overview of CIEM](https://docs.cloud.google.com/security-command-center/docs/ciem-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
