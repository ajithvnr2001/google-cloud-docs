---
url: https://docs.cloud.google.com/chronicle/docs/event-processing/manage-parser-updates/
title: Manage prebuilt parsers \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:37:35.502687+00:00
---

# Manage prebuilt parsers  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/event-processing/manage-parser-updates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage prebuilt parsers 

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document provides guidance on how to manage parsers within Google Security Operations. It details how to handle updates to prebuilt parsers, create parser extensions, and control access to parser management.

### What are parsers?

In Google Security Operations, a parser is a set of instructions that transforms raw log data from various sources into the Unified Data Model (UDM) format. Normalizing raw logs into UDM is essential because it allows Google SecOps to analyze, search, and correlate security events effectively across all your ingested data, regardless of the original log format. For a general overview of log parsing, see [Overview of log parsing](https://docs.cloud.google.com/chronicle/docs/event-processing/parsing-overview).

### Why are parsers needed?

Parsers are crucial for making your security data usable within Google SecOps. Without proper parsing, raw logs remain unstructured and cannot be effectively searched, correlated with other security events, or used by detection rules. The normalization process enriches the raw data, mapping key fields into a standardized schema that powers Google SecOps's analytical capabilities.

### Which parsers appear in the platform?

The **Parsers** page in the Google SecOps platform displays prebuilt parsers only for the log types for which you have already ingested data. If you have not yet ingested any logs for a specific log type, the corresponding prebuilt parser won't appear in the platform.

For example, log types like `UDM` (ingested using the `udmevents` API or without raw logs) and certain Mandiant logs (ingested using the `CreateEntities` API) don't require or have associated parsers since they are already in a structured format. Consequently, these won't be listed on the **Parsers** page.

To see a prebuilt parser in the platform, make sure that you have successfully ingested data for that specific log type.

This document covers the following key aspects of parser management:

  * Manage prebuilt parser updates
  * Manage prebuilt parser versions
  * Create an extension
  * Control access to parser management

**Note:** Only UTF-8 characters are supported in UDM field mappings. Using other encodings can cause parsing failures and make logs unsearchable.

### Parser types

Understanding parser types and their functions:

Parser type | Description  
---|---  
Prebuilt | Parsers created by Google SecOps that include built-in mappings to transform original log data into UDM fields.  
Prebuilt extended | A prebuilt parser created by customers with additional mapping instructions to extract additional data from an original raw log and insert it into the UDM record.  
Custom | A parser that is not prebuilt and has custom data mapping instructions to transform original log data to UDM fields. For more information, see [Configure custom parsers](https://docs.cloud.google.com/chronicle/docs/event-processing/configure-custom-parsers).  
Custom extended | A custom parser with additional mapping instructions that uses a parser extension to extract additional data from an original raw log and insert it into the UDM record.  
  
## Manage prebuilt parser updates

Google SecOps typically updates its prebuilt parsers during the fourth week of each month. These updates are first made available to customers for early access and testing. As upcoming parser updates become available, they are marked as **Pending** update in the parser list. You can examine the difference between the earlier and the newer parser versions, or make the parser update active early to test it, or skip the update and [create a custom parser](https://docs.cloud.google.com/chronicle/docs/event-processing/configure-custom-parsers).

**Important:** This feature requires automatic parser updates to be active. To turn on this setting, see Opt in and out of automatic parser updates.

To view the pending update do the following:

  1. [Log in](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui) to your Google SecOps instance.

  2. Select **Settings** > **SIEM Settings** > **Parsers**.

  3. Click filter_alt **Filter**.

  4. Select **Prebuilt** , **Active** , and **Prebuilt Extended** from the list.

A list of active (default), prebuilt parsers displays. Upcoming parser updates are marked as **Pending** in the **Update** column.

  5. Click more_vert **Menu** and select **View pending update** from the list.

The **Compare parsers** page appears. Here, you can view the following:

     * The code difference between current and the upcoming parser version

     * Analyze the impact of the upcoming parser version on your detection rules

     * The changelogs in the **Change logs** tab

     * The generated UDM event for the sampled raw log

**Note:** The displayed sample is random and might not show all changed fields. You can change the log sample by clicking _edit_ Edit and entering your own sample. Then, click _refresh_ Refresh to update.
     * The date and time the parser was created

     * The date and time the parser code was last updated

You can either make the parser update active early, skip the update and [create a custom parser](https://docs.cloud.google.com/chronicle/docs/event-processing/configure-custom-parsers), or wait for the update to be auto-applied during the fourth week of the month.




### Make the parser update active early

The parser management feature lets you make the parser update active early. For example, if you want to test it.

To make the parser update active early, follow these steps:

  1. On the **Compare parsers** page, click **Make parser update active**.

The **Confirm parser update** dialog appears.

  2. Click **Confirm**.

The parser is activated for the normalization process after 20 minutes.

**Note:** This parser version remains active until the next release cycle.



### Skip prebuilt parser updates

To skip the current and future prebuilt parser updates, create a custom parser as follows:

  1. On the **Compare parsers** page, click **Skip update**.

The **Skip update and create custom parser** window appears.

  2. Click **Create custom parser**.

  3. For the **Type of parser to start with** , select either the current **Prebuilt Parser** , or the **Pending Parser Update**.

  4. Click **Create**.

**Note:** If a custom parser already exists for this log source, you cannot create another one. The following message is displayed, **A custom parser already exists for this log source**.

The selected version is activated for the normalization process after 20 minutes. It appears as **Custom** and **Active** in the parsers list on the **Parsers** page. The earlier prebuilt version appears as **Prebuilt** and **Inactive**.

**Note:** All future prebuilt parser updates remain visible, but they're not applied unless you disable the custom parser and revert to the prebuilt version.



### Revert an early update of the prebuilt parser

If you activated the parser update early, you can still revert to the previous version until the fourth week of the month, when the update is automatically activated.

To switch back to the previous parser version, follow these steps:

  1. From the apps **Application menu** , select **Settings** > **Parsers**.

  2. Click more_vert **Menu** against the parser that you want to revert.

  3. Click **View**.

The **View prebuilt parser** page appears.

  4. Click **Revert to previous version**.

The **Revert to previous** dialog appears. You can click **Compare Parsers** on the dialog to see the difference between the current and the previous versions.

  5. Click **Confirm** to revert the parser to its previous version.

The parser is reverted to its previous version after 20 minutes.




### Analyze the impact of the upcoming parser version

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

**Note:** This feature may not be available to all customers in all regions. Private preview features are not manageable in the Public Preview Manager page in the Google SecOps platform. 

The **impact check** lets you assess the potential impact of the upcoming parser version on your detection rules before applying the changes. For any negatively affected rules, you can follow the links to investigate and update your rules accordingly.

For single-event rules, the analysis checks the detections that your detection rules generated over the last 30 days. It runs both the current and the upcoming parser versions on the events corresponding to those detections. This process regenerates the detections to check for mismatches.

For multi-event rules, the analysis uses a sample of your events rather than all events to perform a heuristic analysis. If events don't match, this analysis marks the outcome as **Potentially failing**.

To run an analysis of the impact of the upcoming parser version on your detection rules, do the following:

  1. In the Google SecOps Console, go to **Settings** > **SIEM Settings** > **Parsers**.
  2. Select a specific **Log type** (prebuilt parser).
  3. Select one of the parser update options: **Update to latest version** , **Rollback to last used version** , or **Opt-in to a Release Candidate**.
  4. Go to the parser **Impact** tab and click **Check impact on rules**. The impact check may take some time to complete.
  5. Upon completion, the system displays the following:

     * Parser metadata and a list of rules that the new version affects, detailing the rule type and the UDM fields showing differences.
     * The system categorizes any negatively affected rules as follows:

       * **Failing** : The new parser did not raise a detection, but the current parser did.
       * **Potentially failing** : Rules (including multi-event) where UDM fields in the rule logic have changed. You must further investigate these rules.

For each of these, follow the link to the rule editor to investigate and edit the rule to get it to work with the new parser version.




## Manage prebuilt parser versions

Google SecOps provides and maintains prebuilt parsers to make sure your logs are parsed correctly. You can control how new parser versions are applied in your environment to meet your organization's needs.

This section describes the full parser version management lifecycle in Google SecOps. This includes opting in and out of automatic updates, comparing the logic between versions, manually updating to new versions, and rolling back to previous versions.

**Note:** You can preview Google prebuilt parsers to test new versions. However, you cannot use the preview tool to test an updated prebuilt parser while you have an active custom parser running. You must deactivate your custom parser and revert to using a prebuilt one.

### Opt in and out of automatic parser updates

If you turn off automatic updates, the parser stays on its current version until you turn on auto-updates or manually update it. To turn off automatic updates, do the following:

  1. From the apps **Application menu** , select **Settings** > **Parsers**.

  2. Click more_vert**Menu** for the required prebuilt parser.

  3. Click **Turn off auto updates**.




When automatic updates are enabled, the parser updates with every new stable release. To turn on automatic updates, do the following:

  1. From the apps **Application menu** , select **Settings** > **Parsers**.

  2. Click more_vert**Menu** for the required prebuilt parser.

  3. Click **Turn on auto updates**.


**Important:** Opting in to a preview parser requires that automatic updates are active and that the parser is on the latest version. Disabling updates removes the preview option and restores the last used stable version for that log type.

### Update a parser version manually

If automatic updates are off, you can choose when to update a parser to a new version. This lets you review changes before applying them.

**Note:** You can only upgrade to the latest parser version and not any versions in between. To update a parser, do the following:

  1. From the apps **Application menu** , select **Settings** > **Parsers**.

  2. Click more_vert**Menu** for the required parser.

  3. Select **Update to latest version**.

The **Compare parsers** page appears. You can view the following:

     * The code difference between the current and the new parser version.

     * The **Change log** tab, which summarizes changes.

     * The UDM output for the sampled raw log. To test the output against a different log, click edit **Edit** to edit the sampled raw log.

     * The date and time the parser code last updated.

  4. Click **Update parser** to update it to the latest version.




### Roll back a parser version

You can revert a parser to the version that you last used, regardless of its automatic update status. To roll back a parser version, do the following:

  1. From the apps **Application menu** , select **Settings** > **Parsers**.

  2. Click more_vert**Menu** for the required parser.

  3. Select **Roll back to last used version**.

The **Compare parsers** page appears. You can view the following:

     * The code difference between the current and the last used parser version.

     * The **Change log** tab, which shows changes.

     * The UDM output for the sampled raw log. To test the output against a different log, click edit **Edit** to edit the sampled raw log.

     * The date and time the parser code last updated.

  4. Click **Proceed to roll back** to revert to the last used version.




The parser rolls back to the last version you used. For example, if you upgraded from version 17.0 to 24.0, rolling back will return you to 17.0, not 23.0.

You can perform only one consecutive rollback. After you perform a rollback, the **Roll back** option is no longer available.

**Note:** Parser updates take about 30 minutes. During this time, you might experience temporary inconsistencies in event parsing.

### Support policy for previous parser versions

Only the latest stable version of a prebuilt parser receives bug fixes and enhancements. If you disable automatic updates and remain on an earlier parser version, that version doesn't receive patches or updates. If you report issues with this earlier version, the next stable release includes the fix. You must manually upgrade your parser to the latest stable version to receive the fix.

## Create an extension

Parser extensions provide a flexible way to extend the capabilities of existing prebuilt (default) parsers. They don't replace prebuilt parsers. Instead, they enable the seamless extraction of additional fields from the original raw log into the UDM record. A parser extension is different from a custom parser. 

To create a parser extension, see [Using parser extensions](https://docs.cloud.google.com/chronicle/docs/event-processing/using-parser-extensions).

## Control access to parser management

By default, users with **Administrator** and **Editor** roles can manage parser updates. New permissions can be granted to control who can view and manage these updates. 

For more information about managing users and groups, or assigning roles, see the [role-based access control user guide](https://docs.cloud.google.com/chronicle/docs/administration/rbac).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
