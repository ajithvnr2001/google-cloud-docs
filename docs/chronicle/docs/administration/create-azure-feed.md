---
url: https://docs.cloud.google.com/chronicle/docs/administration/create-azure-feed/
title: Create an Azure Event Hub feed \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:05.220443+00:00
---

# Create an Azure Event Hub feed  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/administration/create-azure-feed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create an Azure Event Hub feed

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document shows you how to set up an Azure Event Hub to send security data to Google Security Operations. You can create up to 10 Azure Event Hub feeds, which includes both active and inactive feeds.

**Important:** Google SecOps doesn't support ingestion from Azure sovereign clouds, including Azure China (operated by 21Vianet) and Azure Government. Only commercial Azure endpoints (for example, `*.servicebus.windows.net` for Event Hub or `*.blob.core.windows.net` for Blob Storage) are supported.

**Note:** Azure feeds collect data continuously. As a result, Google SecOps does not populate the **LAST SUCCEEDED ON** column for these feeds.  To set up an Azure feed, complete the following processes:

  1. **Create an event hub in Azure:** set up the required infrastructure in your Azure environment to receive and store the security data stream.

**Important:** When you create the Azure Event Hub, make sure you set its Cleanup Policy to **Delete**. Do not use the **Compact** cleanup policy (Log Compaction). Log compaction only retains the latest value of a key, which can prevent Google SecOps from ingesting all historical events and may cause the feed to stop processing.
  2. **Configure the feed in Google SecOps:** configure the feed in Google SecOps to connect to your Azure event hub and to begin ingesting data.




### Create an Azure Event Hub

To create an event hub in Azure, do the following:

  1. Create an [event hub namespace and event hub](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-create).

     * To ensure optimal data ingestion, deploy the Event Hub namespace in the same region as your Google SecOps instance. Deploying the event hub in a different region can reduce the throughput ingested into Google SecOps.

     * Set the partition count to 40 for optimal scaling. You must have the Premium Tier of Azure Event Hubs in order to set more than 32 partitions. **Note:** You can't change the partition count later in the standard and basic tiers. Partition count does not affect cost. 

     * To help prevent data loss due to Google SecOps quota limits, set a long retention time for your event hub. This ensures that logs aren't deleted before ingestion resumes after a quota throttle. For more information about event retention and retention time limitations, see [Event retention](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-features#event-retention).

     * For standard tier event hubs, enable **Auto inflate** to automatically scale throughput as needed. See [Automatically scale up Azure Event Hubs throughput units](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-auto-inflate) for more information.

     * For basic and standard tiers, one throughput unit (TU) in Azure Event Hub supports up to 1 MB per second of data ingestion. If the incoming event volume exceeds the capacity of the configured TUs, data loss may occur. For example, if you configure 5 TUs, the maximum supported ingestion rate is 5 MB per second. If events are sent at 20 MB per second, the Event Hub may crash. As a result, logs may be lost at the Event Hub level before they reach Google SecOps.

  2. [Obtain the event hub connection string](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-get-connection-string#azure-portal) required for Google SecOps to ingest data from the Azure event hub. This connection string authorizes Google SecOps to access and collect security data from your event hub. You have two options for providing a connection string:

     * **Event hub namespace level** : works for all event hubs within the namespace. It's a simpler option if you're using multiple event hubs and want to use the same connection string for all of them in your feed setup.

     * **Event hub level** : applies to a single event hub. This is a secure option if you need to grant access to only one event hub. Ensure that you remove `EntityPath` from the end of the connection string.

For example, change `Endpoint=<ENDPOINT>;SharedAccessKeyName=<KEY_NAME>;SharedAccessKey=<KEY>;EntityPath=<EVENT_HUB_NAME>` to `Endpoint=<ENDPOINT>;SharedAccessKeyName=<KEY_NAME>;SharedAccessKey=<KEY>`.

  3. Configure your applications, such as [Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/afds/waf-front-door-monitor) or [Microsoft Defender](https://learn.microsoft.com/en-us/defender), to send their logs to the event hub.

**Microsoft Defender users:** When configuring Microsoft Defender streaming, ensure that you enter your existing event hub name. If you leave this field blank, the system might create unnecessary event hubs and consume your limited feed quota. To keep things organized, use event hub names that match the log type.




### Configure network security (optional)

If you restrict network access to your your Azure Event Hub namespace (for example, using firewalls or private endpoints), you must add Google SecOps IP addresses to an allowlist to ensure that Google SecOps can connect and ingest data.

You have two options:

  * **Allowlist all Google IP addresses (recommended):** To ensure uninterrupted connectivity, allowlist all Google IP addresses. You can retrieve the list of Google IP addresses from the public JSON file: [`https://gstatic.com/ipranges/goog.json`](https://gstatic.com/ipranges/goog.json).
  * **Allowlist region-specific IP addresses:** If your security policy requires a more restricted list of IP addresses, contact [Google SecOps Support](https://console.cloud.google.com/support) to request the specific IP addresses for the region where your Google SecOps instance is deployed. These IP addresses can change if Google SecOps infrastructure is updated.



### Configure the Azure feed

To configure the Azure feed in Google SecOps, do the following:

  1. In the Google SecOps menu, select **SIEM Settings** , and then click **Feeds**.

  2. Click **Add new**.

  3. In the **Feed name** field, enter a name for the feed.

  4. In the **Source type** list, select **Microsoft Azure Event Hub**.

  5. Select the **Log type**. For example, to create a feed for Open Cybersecurity Schema Framework, select **Open Cybersecurity Schema Framework (OCSF)** as the **Log type**.

  6. Click **Next**. The **Add feed** window appears.

  7. Retrieve the information from the event hub that you created earlier in the Azure portal to fill in the following fields:

     * **Event hub name** : the event hub name
     * **Event hub consumer group** : the consumer group associated with your event hub

**Caution:** Don't create subscribers or retrieve data programmatically through the Data Explorer tab in the Azure portal for the consumer group. Doing so may result in data loss.
     * **Event hub connection string** : the event hub connection string

     * **Azure storage connection string** : Optional. The blob storage connection string

     * **Azure storage container name** : Optional. The blob storage container name

     * **Azure SAS token** : Optional. The SAS token

     * **Asset namespace** : Optional. The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : Optional. The label to be applied to the events from this feed

**Note:** Google SecOps manages its own checkpointing when ingesting data from Azure Event Hub. Only the event hub connection string is required. The other optional fields don't affect the checkpointing.
  8. Click **Next**. The **Finalize** screen appears.

  9. Review your feed configuration, and then click **Submit**.




### Verify data flow

To verify that your data is flowing into Google SecOps and your event hub is functioning correctly, you can perform these checks:

  * In Google SecOps, examine the dashboards and use the Raw Log Scan or Unified Data Model (UDM) search to verify that the ingested data is present in the correct format.

  * In the Azure portal, navigate to your event hub's page and inspect the graphs that display incoming and outgoing bytes. Ensure that the incoming and outgoing rates are roughly equivalent, indicating that messages are being processed and there is no backlog.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
