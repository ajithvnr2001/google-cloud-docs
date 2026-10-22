---
url: https://docs.cloud.google.com/chronicle/docs/event-processing/block-enrichment-flows/
title: Manage enrichment blocks \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:34.911739+00:00
---

# Manage enrichment blocks  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/event-processing/block-enrichment-flows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage enrichment blocks

This document explains how _enrichment blocks_ give you granular control over the data enrichment process. The default enrichment process uses contextual data from different sources, analyzes the data, and overwrites Unified Data Model (UDM) field data according to internal logic. The default process usually works as expected. However, in certain cases, overwriting the UDM field data causes unexpected behavior, such as improperly triggering detection-engine rules.

**Note:** To use enrichment blocks, you must be a user with global access for [Data RBAC](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview).

## Configure and view enrichment blocks

Only Google Security Operations users with _Chronicle Admin_ and _Editor_ privileges can configure enrichment blocks; all Google SecOps users can view the **Enrichment Blocks** interface. 

The basic configuration of an enrichment block requires three sequential parameters: **Enrichment Type** , **Target Log Type** , and **Source**. The options available for **Target Log Type** depend on the selected **Enrichment Type** , and the available options for **Source** depend on the selected **Target Log Type**. 

You can't delete an enrichment block. 

Enrichment blocks can be enabled, disabled, and re-enabled.

The **Enrichment Blocks** dialog includes the **Enabled Blocks** tab and **Disabled Blocks** tabs. The tables in both tabs display the basic configuration parameters of the enrichment block, the UTC date on which the block was last enabled, and the (optional) user-specified reason for the block. The table in the **Disabled Blocks** tab includes the UTC date on which the block was disabled.

### Revised enrichment block time logic

A change in the status of an enrichment block takes effect within 5-10 minutes.

The key effect of enabling or disabling a block is its synchronized start time:

  * **Enabling a block (de-enrichment)** : Google SecOps de-enriches all associated fields starting from 00:00:00 UTC of the current date and continues going forward.

  * **Disabling a block (re-enrichment)** : Google SecOps re-enriches all associated fields starting from 00:00:00 UTC of the current date and continues enriching going forward.




Example: On Tuesday, September 16, at 23:59:59 UTC, you enable an enrichment block. Google SecOps de-enriches all the associated enriched fields from 0:00:00 Tuesday, September 16 UTC—and continues implementing the enrichment block going forward. On Wednesday, September 17, at 09:00:00 UTC, you _disable_ the enrichment block. Google SecOps re-enriches all the associated fields from 0:00:00 Wednesday, September 17 UTC—and continues enriching all the relevant data going forward. 

### Create and enable an enrichment block

To create and enable an enrichment block, do the following:

  1. Go to **Settings** > **Enrichment Blocks**.
  2. Configure the following:

     1. From the **Enrichment Type** list, select one of the following options:

        * **All Types**. Applies to all items in the list, which is populated based on the data and log types that Google SecOps ingests.
        * **[Asset](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment#asset_enrichment)**. When it's not in the enrichment block, this option does the following: 
          * Extracts fields, such as `hostname`, `asset_id`, `mac`, `ip` (if `asset_id` is empty).
          * Enriches fields that include anything under `Asset` (for example, `hostname`, `asset_id`, `mac`, or `ip`) from [`Noun`](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list#noun).
          * Uses enrichment sources, such as `DHCP` and `Asset Context` (for example, `Tanium Asset` or `CrowdStrike`).
        * **[GeoIP](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment#ip_geolocation_enrichment)**. When it's not in the enrichment block, this option does the following: 
          * Extracts fields, such as `ip` if it's public or routable.
          * Enriches fields that include [`artifact.ip`](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list#artifact), `artifact.location`, `artifact.network`, [`location`](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list#location).
          * Uses enrichment sources from the Google GeoIP Service.
        * **[Google Threat Intel](https://docs.cloud.google.com/chronicle/docs/event-processing/entity-graph#ingest-google-threat-intelligence-data)**. When it's not in the enrichment block, this option does the following: 
          * Extracts relevant fields. 
          * Enriches the [`File`](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list#file) or `process.file` fields.
          * Uses enrichment sources from VirusTotal file metadata.
        * **[Process](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment#process_enrichment)**. When it's not in the enrichment block, this option does the following: 
          * Extracts fields, such as `process.product_specific_process_id`.
          * Enriches fields, which include anything under `Process`.
          * Uses enrichment sources, such as EDR logs (for example, from CrowdStrike or SentinelOne).
        * **[User](https://docs.cloud.google.com/chronicle/docs/event-processing/data-enrichment#user_enrichment)**. When it's not in the enrichment block, this option does the following: 
          * Extracts fields, such as `user.email_addresses`, `user.userid`, `user.windows_sid`, `user.employee_id`, `user.product_object_id`.
          * Enriches fields that include anything under `User`.
          * Uses enrichment sources, such as user-context logs (for example, from Workday or Windows AD).
     2. From the **Target Log Type** list, select the required option, which depends on the selected **Enrichment Type**. Example options include **All Types** , **Windows_Sysmon** , **CB_EDR** , and **BRO_JSON**.

**Note:** **All Types** applies to all items in the list, which is populated based on the data and log types that Google SecOps ingests.
     3. From the **Source** list, select the required option. The available options depend on the selected **Target Log Type**. Example options include **All Types** , **INFOBLOX_DHCP** , **WINDOWS_AD** , and **VIRUSTOTAL_FILE_METADATA**.

  3. Click **Enable Block** to open the **Enable Block** dialog and display the configuration from the previous steps. 

  4. Optional: In the **Reason for blocking** field, enter the reason for the enrichment block.

  5. After you review the information, click **Enable Block**. The **Enabled Blocks** table displays a row for the enabled enrichment block. 

After approximately 5-10 minutes, Google SecOps implements the enrichment block (that is, _de-enriches_ all associated enriched fields) from 0:00:00 of the current date UTC and going forward. After this time, we recommend that you verify the results are as you expect.




### Disable an enrichment block

To disable an enrichment block, do the following:

  1. Go to **Settings** > **Enrichment Blocks**.
  2. On the **Enabled Blocks** tab, find the enrichment block, click more_vert **More** in that row, and select **Disable Block**. A confirmation dialog opens.
  3. Review the information and click **Disable Block**. The **Disabled Blocks** table displays a row for the disabled enrichment block, and the corresponding row is removed from the **Enabled Blocks** table. 

After approximately 5-10 minutes, Google SecOps _re-enriches_ all the associated fields from 0:00:00 of the current date UTC and going forward. After this time, we recommend that you verify the results are as you expect.




### Re-enable an enrichment block

To re-enable an enrichment block, do the following:

  1. Go to **Settings** > **Enrichment Blocks**.
  2. On the **Disabled Blocks** tab, find the enrichment block, click more_vert **More** in that row, and select **Enable Block**. A confirmation dialog opens.
  3. Review the information and click **Enable Block**. The **Enabled Blocks** table displays a row for the re-enabled enrichment block, and the corresponding row is removed from the **Disabled Blocks** table. 

After approximately 5-10 minutes, Google SecOps implements the enrichment block (that is, _de-enriches_ all associated enriched fields) from 0:00:00 of the current date UTC and going forward. After this time, we recommend that you verify the results are as you expect.




## Example workflow for an enrichment block

This workflow demonstrates how to use an enrichment block to resolve a rule improperly triggered by unwanted data overwrites:

  1. **Validate the rule** : You receive an alert and determine it was triggered improperly. You confirm the rule logic is correct—it's not a candidate for a [rule exclusion](https://docs.cloud.google.com/chronicle/docs/detection/rule-exclusions).
  2. **Identify the log source** : You review the alert and realize the trigger conditions were met by a CrowdStrike log.
  3. **Investigate the enrichment source** : Use the [Event Viewer](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#event-viewer) to identify which external source modified the critical field. The following steps show one way to open the Event Viewer (but there are alternative steps): 

     1. On the Google SecOps console, go to **Detections** > **Alerts & IOCs**.
     2. Select the improperly triggered detection and drill down to the event.
     3. Click the event timestamp to open the [Event Viewer](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#event-viewer). The [**Event Fields** tab](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#event-fields-tab) is displayed by default. Each enriched field is identified with an **E** , and expanding the node shows the enrichment sources. 
     4. On the **Event Fields** tab, expand the node of the problematic enriched field to identify the source. You learn that the field that triggered the alert had been enriched by Okta.
  4. **Create and enable an enrichment block** : Create and turn on an enrichment block that disables `User` data from Okta as a source of enrichment in your CrowdStrike logs.

  5. **Verify resolution** : After waiting 5-10 minutes for the enrichment block to take effect, verify that the alert is no longer triggered improperly.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
