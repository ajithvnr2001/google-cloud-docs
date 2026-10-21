---
url: https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/use-events-viewer/
title: Use the Events Viewer \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:35:14.538023+00:00
---

# Use the Events Viewer  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/use-events-viewer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use the Events Viewer

Supported in:

Google SecOps 

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

**Note:** This document applies to the **enhanced Cases experience** for Google SecOps unified customers. 

When you investigate a security finding, high-level summaries only tell part of the story. To figure out exactly what happened, you often need to look at the underlying data that triggered the detection.

The **Events Viewer** is an interactive side panel that lets you dive directly into the individual Unified Data Model (UDM) events and raw logs that triggered a detection. By analyzing these records, you can verify suspicious activity, map attacker behavior, and gather the technical indicators needed for incident response.

To understand the broader triage workflow, see [Investigation and case management overview](https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/investigation-management-overview).

## Access event details during an investigation

You can open the Events Viewer from any workspace context where you are actively reviewing detections or case timelines:

  * **From the Case List View:** Expand a case row, click a specific detection to open its summary drawer, and select the **Events** tab.
  * **From the Full Detection Page:** Navigate to a dedicated detection view and go to the **Events** section at the bottom of the page.
  * **From the Case Overview:** Select a case and locate the **UDM Events** widget to view events directly tied to the overall investigation.

**Note:** For alerts ingested using a SOAR connector rather than Google SecOps SIEM, UDM events still appear in the events list. However, when you open the event details in the **Events Viewer** , you might not see the same level of parsed field detail or raw log telemetry as you would for an event ingested directly through the SIEM connector.

Clicking any event row in these tables instantly opens the detailed **Events Viewer** panel.

## Analyze evidence using event fields and raw logs

The Events Viewer organizes event data into two tabs, letting you pivot between structured platform data and the original source telemetry.

### Validate activity with structured event fields

The **Event fields** tab translates complex log data into clean, parsed UDM objects. This view is ideal for quickly identifying key security indicators without sorting through unformatted text.

  * **Isolate critical attributes:** Use the inline filter to quickly search for specific UDM paths, such as target hostnames, source IP addresses, or user command lines.
  * **Customize your analysis view:** Add or remove UDM fields as columns to tailor the event table to your immediate investigative needs (for example, adding file hashes when investigating malware execution).



### Inspect original telemetry with the raw log

The **Raw log** tab displays the unparsed, original JSON or text payload exactly as it was received from the source device. 

  * **Verify parser accuracy:** Cross-reference the parsed UDM fields with the raw payload to ensure critical context wasn't dropped or misclassified during ingestion.
  * **Extract deep technical context:** Look for vendor-specific metadata or specialized error codes that might not map directly to standard UDM fields but are crucial for determining an attack's success.



## Take investigative actions from the Events Viewer

As you isolate key indicators within the Events Viewer, you can take immediate action on individual records or rule groups to streamline triage and tune detection logic:

  * **Pin items as core evidence:** Expand the event entries down to the lowest level of the row hierarchy and mark the checkbox next to the specific record. Click the **pin** icon that appears. This action copies the item directly to the **Pinned** section of your case workspace for historical timelines and executive summaries.
  * **Create detection exclusions:** Mark the checkboxes next to one or more rows and click **Create Exclusion** to open the configuration dialog. Exclusions filter out detections that meet your specified conditions. You can configure exclusions at two levels: 
    * **Rule Set level:** Select an entire rule group to apply the exclusion conditions across all rules in that group simultaneously.
    * **Individual Rule level:** Expand the rule set group and select specific, individual rules to isolate your exclusion parameters.
  * **Manage exclusion status upon creation:** Toggle the **Enable exclusion upon creation** setting depending on your deployment needs: 
    * Leave the setting enabled to apply the exclusion logic to live platform traffic immediately upon clicking **Create**.
    * Disable the setting to save your exclusion logic to the platform without activating it. This lets you safely store, edit, or test your logic later without altering current detection behavior.



For more details on managing exclusion rules, see [Manage rule exclusions](https://docs.cloud.google.com/chronicle/docs/investigation/alert-suppression#manage-rule-exclusions).

## Troubleshooting

Use this table to quickly resolve common issues encountered while viewing event details:

Issue description | Root cause and resolution  
---|---  
Events fail to load in the viewer table. | Usually caused by temporary interface latency. Refresh your browser page. If the issue persists, verify that your log sources are actively ingesting data.  
The raw JSON view is empty. | The underlying log source may be configured to discard raw logs after parsing. Check your ingestion settings or verify the health of the log parser.  
A specific UDM field cannot be added as a column. | Ensure the field contains valid data for the selected event type. Custom or unsupported sub-fields cannot be rendered as standalone table columns.  
The **Events Viewer** or **Raw log** tab lacks complete field details or telemetry for an event. | Check the alert's ingestion source. Alerts ingested using SOAR connectors display UDM events in event lists, but opening event details might not yield full raw log telemetry because connectors manage alert metadata directly without storing raw SIEM logs. Inspect the alert details panel instead to review available metadata.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
