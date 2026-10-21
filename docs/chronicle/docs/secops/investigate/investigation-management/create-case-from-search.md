---
url: https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/create-case-from-search/
title: Attach SIEM search results to cases \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:17:27.409568+00:00
---

# Attach SIEM search results to cases  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/create-case-from-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Attach SIEM search results to cases

Supported in:

Google SecOps 

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

**Note:** This document applies to the **enhanced Cases experience** for Google SecOps unified customers. 

Google SecOps connects your threat hunting and search workflows directly to case management. You can attach individual UDM events or detections from your SIEM search results table straight to a case as core evidence.

This integration lets you:

  * **Enrich an existing case:** Add events or detections related to a case you're investigating.
  * **Create a new case:** Investigate a threat hunt hypothesis.

**Note:** If you're creating a standalone case without search data see [Create a case manually](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/create-a-manual-case).



For more information, see [Investigation and case management overview](https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/investigation-management-overview).

## Example use case

Consider a threat hunting scenario where an analyst is investigating a suspicious file hash across the organization:

  1. **Threat hunt:** The analyst runs a UDM search for the hash to evaluate its potential spread.
  2. **Evidence selection:** Instead of manually exporting search results, the analyst selects the specific events and detections directly from the results table.
  3. **Case creation:** The analyst creates a new case, which automatically includes those selected items as core evidence.
  4. **Investigation & documentation:** The analyst documents their findings with internal comments and continues the investigation.



## Prerequisites

To attach SIEM search results to a case, your environment must meet the following requirement:

  * **Chronicle API migration:** Your environment must be migrated to the Chronicle API framework (Stage 2 migration) to allow SIEM data to communicate with the new Cases experience interface.



For more information, see the [SOAR migration FAQ](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-faq) and the [Chronicle API migration guide](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/api-migration-guide).

## Supported data types for case evidence

From the SIEM search results table, you can manually attach specific record types to a case:

  * **UDM Events:** You can attach individual log entries to a case singly or in bulk. There are no restrictions on how many cases a UDM event can link to.
  * **Detections:** You can add rules engine findings to a case singly or in bulk. There are no restrictions on how many cases a single detection can link to.
  * **Alerts:** You cannot manually attach alerts to cases from the search results table. The platform automatically ingests and groups alerts into cases using system playbooks and predefined grouping rules. However, you can reassign or move an existing alert to a different case directly from the alert details view.

**Note:** A case maintains a maximum capacity of 500 detections and 5,000 UDM events. This includes all manual additions (such as UDM events or detections), automated agent reports, and any underlying events extracted during attachment. To ensure data completeness, if you attach an item right before reaching these thresholds, the platform successfully attaches all of its associated underlying events, even if the total count temporarily exceeds the limit.



## Create a new case from search results

When you initialize a new case using search data, the platform creates an investigation container and automatically seeds it with your selected parameters.

  1. From the navigation menu, go to **Investigation > SIEM Search**.
  2. Run a query to find your target data. For more information about filtering your results, see [Overview of procedural filtering](https://docs.cloud.google.com/chronicle/docs/investigation/filtering-overview).
  3. Locate the event or detection data you want to use as evidence.
  4. Open the action menu: 
     * **For UDM events (Results tab):**
       * **Single event:** Locate your target row and click more_vert.
       * **Multiple events:** Mark the checkboxes next to the target rows, and then click more_vert.
     * **For detections (Alerts & Detections tab):**
       * **Single detection:** Hold the pointer over the target row and click more_vert.
       * **Multiple detections:** Mark the checkboxes next to the target rows, and then click more_vert.
  5. Select **Create case from evidence**.
  6. In the **Create Case from evidence** dialog, configure the following required fields: 
     * **Title:** Enter a descriptive name for the investigation.
     * **Environment:** Select the target environment scope.
     * **Assign to:** Designate the owner analyst.
     * **Priority:** Specify the severity level.
  7. Click **Continue**.



## Attach search results to an existing case

Use this workflow to add new data and historical UDM context to an active investigation.

  1. From the navigation menu, go to **Investigation > SIEM Search**.
  2. Run a query to find your target data. For more information about filtering your results, see [Overview of procedural filtering](https://docs.cloud.google.com/chronicle/docs/investigation/filtering-overview).
  3. Locate the event or detection data you want to add.
  4. Open the action menu: 
     * **For UDM events (Results tab):**
       * **Single event:** Locate your target row and click more_vert.
       * **Multiple events:** Mark the checkboxes next to the target rows, and then click more_vert.
     * **For detections (Alerts & Detections tab):**
       * **Single detection:** Hold the pointer over the target row and click more_vert.
       * **Multiple detections:** Mark the checkboxes next to the target rows, and then click more_vert.
  5. Select **Attach to existing case**.
  6. From the case list, search for and select your target case.
  7. Confirm the selection to add the data to the case scope.



## Troubleshooting

Use this table to quickly resolve common issues encountered while managing evidence from the search interface:

Issue description | Root cause and resolution  
---|---  
The assignment options are grayed out or unclickable for a specific row. | You selected an alert row. Manual case assignment is disabled for alerts because the platform automatically groups them. Deselect the alert to restore action choices.  
The case list does not display the target investigation case. | Ensure that your active session environment matches the environment configured on the target case. Mismatched environment boundaries filter out case visibility.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
