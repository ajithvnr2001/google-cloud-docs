---
url: https://docs.cloud.google.com/chronicle/docs/install/forwarder-management-configurations/
title: Configure forwarders in the Google SecOps platform \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:56.618762+00:00
---

# Configure forwarders in the Google SecOps platform  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/install/forwarder-management-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure forwarders in the Google SecOps platform

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Caution:** The forwarder is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations). The forwarder component is being phased out of the Google SecOps platform and will reach end-of-life (EOL) in January 2027. **Apr 1, 2026** : New Google SecOps customers cannot use the forwarder component. **Jan 1, 2027** : The forwarder is officially EOL. No further patches, including security patches, will be released. **Apr 1, 2027** : Data is no longer allowed to be ingested from the forwarder component. **Google recommends using Bindplane for Google SecOps as the primary solution for log collection. For more information, see[Use Bindplane with Google SecOps](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent)**.**Note:** Forwarder configuration files not created with the Google Security Operations UI or the forwarder management API cannot be managed with the Google SecOps UI. You need to re-create those configurations using the Google SecOps UI or the forwarder management API to take advantage of the forwarder management features.

This page describes how to create, manage, and download forwarder configurations using the Google SecOps user interface (UI). 

Forwarder configuration is a two-step process:

  1. Add forwarder configuration: This establishes the framework for your configuration.
  2. Add collector configuration: This defines the source of data that the forwarder will ingest. Without at least one collector, the forwarder does not have any data to work with.



Once you've added one or more collectors, the forwarder configuration is complete. You can then download it and deploy it onto a machine or device that has the forwarder software installed.

For information about how to install and configure the Google SecOps forwarder, system requirements, and details about configuration settings, see [Install and configure the forwarder](https://docs.cloud.google.com/chronicle/docs/install/install-forwarder).

## Add forwarder configuration

Instead of _adding_ a new forwarder, you can _clone_ one or more existing forwarders. For details, see Clone forwarders.

To add a new forwarder, follow these steps:

  1. In the navigation bar, click **Settings**.
  2. Under **Settings** , click **Forwarders**.
  3. Click **Add new forwarder**.
  4. In the **Forwarder name** field, type a name.
  5. Optional: Expand the **Configuration values** section and specify the values. For information about the configuration settings, see [Determine the configuration](https://docs.cloud.google.com/chronicle/docs/install/install-forwarder#determinedata).

  6. Click **Submit**.

The forwarder is added and **Add collector configuration** window appears.




## Add collector configuration

You can add one or more collectors to an existing forwarder. To add a new collector to a forwarder, follow these steps:

  1. In the navigation bar, click **Settings**.
  2. Under Settings, click **Forwarders**.
  3. On the **Forwarders** page, find the forwarder you want. If the list of forwarders is long, use the **Search** field.
  4. Hold the pointer over the forwarder for which you want to add a collector. The more_vert **expand menu icon** displays.
  5. Click the more_vert **expand menu icon**.
  6. Select **Add new collector**.
  7. In the **Collector name** field, type a name.
  8. Click the **Log type** field to view a list of log types, and do one of the following:

     * If you don't see the log type you want, start typing its name in the box to view more suggestions. For a complete list of supported log types, see [Supported data sets](https://docs.cloud.google.com/chronicle/docs/supported-datasets).
     * Select a log type from the list.
  9. Optional: Expand the **Configuration values** section and specify the values. For information about the configuration settings, see [Determine the configuration](https://docs.cloud.google.com/chronicle/docs/install/install-forwarder#determinedata).

  10. Optional: Expand the **Advanced settings** section and specify any of the following:

     * **Max seconds per batch:** The number of seconds between batches. The default is `10`.
     * **Max bytes per batch:** The number of bytes queued before the forwarder batch upload. The minimum is `204800 bytes`, which is `200 KB`. The maximum is `1048576 bytes`, which is `1MB`. The default is `1,048,576 bytes`, which is `1MB`.
  11. Recommended: **Disk buffer:** Click the toggle to the on position to enable disk buffering for the collector. For details about disk buffering, see [Disk buffering](https://docs.cloud.google.com/chronicle/docs/install/install-forwarder#diskbuffering). When enabled, you can specify the following settings:

     * **Directory path:** The directory path for files written.
     * **Maximum Buffered File Size (in bytes):** The maximum disk size used by the collector before backlogged messages are buffered to disk. The default is `1,073,741,824`. The maximum is `4,294,967,296`.
  12. Optional: **Override timezone** : Click the toggle to the on position to override the default time zone for your logs by selecting a custom one from the **Timezone** list. only if your raw logs don't include the correct time zone at the source. Ensure that the logs have consistent timestamps before enabling it.

The selected time zone is applied on the server side in Google SecOps. The forwarder ignores this setting, even if the generated configuration file contains it.

  13. Click the **Collector type** field and select a collector type. Each collector type has its own settings that you can configure. For details about the collector types and their settings, see [Determine the configuration](https://docs.cloud.google.com/chronicle/docs/install/install-forwarder#determinedata).

  14. Click **Submit**.




## Download configuration files

Downloading the forwarder configuration files requires at least one collector. If you try to download a forwarder without a collector, you get an error.

You can download the forwarder configuration (`.conf`) file, authentication (`_auth.conf`) file, or both, for any forwarder listed in your Google SecOps instance as long as it has at least one collector. After downloading the files, deploy them on the Windows or Linux system where the Google SecOps forwarder resides.

To download forwarder configuration files:

  1. In the navigation bar, click **Settings**.
  2. Under Settings, click **Forwarders**. The page displays the list of forwarders.
  3. On the **Forwarders** page, find the forwarder you want. If the list of forwarders is long, use the **Search** field.

  4. Hold the pointer over the forwarder for which you want to download configuration files. The more_vert **expand menu icon** displays.

  5. Click the more_vert **expand menu icon**.

  6. Select **Download**.

  7. In the **Download forwarder configuration** dialog, do one of the following:

     * To download the forwarder configuration file, click the **download icon** next to the **`.conf`** file type.
     * To download the forwarder authentication file, click the **download icon** next to the **`_auth.conf`** file type.
     * To download both files, click **Download all**.



## Manage forwarders

This section describes how to view and manage forwarders.

### List the forwarders in a Google SecOps instance

  1. In the navigation bar, click **Settings**.
  2. Under Settings, click **Forwarders**. The page displays the list of forwarders.
  3. Optional: Sort the list by clicking the **Name** or **Last updated** column.



Optionally, use the search field to narrow the results in your list.

### Clone forwarders

Cloning lets you create a copy of one or more forwarder configurations.

To clone a forwarder configuration, follow these steps:

  1. On the Forwarders page, select the checkbox for each forwarder that you want to clone.

  2. Click the more_vert **expand menu icon**.

  3. Select **Clone**.

  4. Click **Clone**. A copy of each forwarder configuration is added.




### Edit a forwarder configuration

  1. In the navigation bar, click **Settings**.
  2. Under Settings, click **Forwarders**. The page displays the list of forwarders.
  3. Hold the pointer over the forwarder for which you want to edit the configuration. The more_vert **expand menu icon** displays.

  4. Click the more_vert **expand menu icon**.

  5. Select **Edit forwarder configuration**.

  6. Make your changes to the configuration. For more information, see the configuration steps in the procedure for adding forwarders.

  7. Click **Update**

  8. Restart the forwarder for your changes to take effect.




### Delete forwarders

  1. On the Forwarders page, select the checkbox for each forwarder that you want to delete.

  2. Click the more_vert **expand menu icon**.

  3. Select **Delete**.

  4. In the Delete Forwarder dialog, click **Delete**.




## Manage collectors

This section describes how to view and manage collectors.

### List the collectors in a Google SecOps instance

  1. In the navigation bar, click **Settings**.
  2. Under Settings, click **Forwarders**. The page displays the list of forwarders.
  3. Click the expander arrow next to the **Name** column heading. This expands all of the forwarders, displaying up to five collectors for each forwarder.
  4. If a forwarder has more than five collectors, click the **See all collectors** link.



### Edit a collector configuration

  1. In the navigation bar, click **Settings**.
  2. Under Settings, click **Forwarders**. The page displays the list of forwarders.
  3. Click the arrow_right expander arrow of the forwarder for which you want to edit a collector.

  4. If there are more than five collectors, click the **See all collectors** link.

  5. Hold the pointer over the collector for which you want to edit the configuration. The **Edit** option displays.

  6. Click **Edit**.

  7. Make your changes to the configuration. For more information, see the configuration steps in the procedure for adding collectors.

  8. Click **Update**.




### Delete a collector

  1. In the navigation bar, click **Settings**.
  2. Under Settings, click **Forwarders**. The page displays the list of forwarders.
  3. Click the arrow_right**expander arrow** of the forwarder for which you want to delete a collector.

  4. If there are more than five collectors, click the **See all collectors** link.

  5. Hold the pointer over the collector for which you want to edit the configuration. The **Delete** option displays.

  6. Click **Delete**.

  7. To confirm, click **Delete** in the Delete collector dialog.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
