---
url: https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/investigation-management-overview/
title: Investigation and case management overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:11.549410+00:00
---

# Investigation and case management overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/investigation-management-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Investigation and case management overview

Supported in:

Google SecOps 

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

**Note:** This document applies to the **enhanced Cases experience** for Google SecOps unified customers. 

**Note:** The public preview feature only supports single-SIEM deployments (instances where a single Google SecOps instance ingests data into SOAR) and does not support federated or MSSP environments.

This document is for security analysts and SOC managers who want to understand and navigate the case management experience within Google Security Operations. This flow lets you efficiently triage, manage, and track security findings through their entire remediation lifecycle.

Google SecOps ingests raw log telemetry from a wide range of sources across your network ecosystem. The platform automatically parses these events into the Unified Data Model (UDM) format and analyzes them to generate actionable detections and alerts.

## Prerequisites

To use the new Cases experience, your environment must meet the following requirements:

  * **Infrastructure migration:** Your instance must be fully migrated to the Google Cloud framework. For more information, see the [SOAR migration overview](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp). If you manage a multi-tenant environment, see the [SOAR MSSP migration guide](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-mssp-instance).
  * **IAM permissions:** Users who need to access Cases must have the following IAM permissions assigned: 
    * `chronicle.caseDetections.get`
    * `chronicle.caseEvents.get`
    * `chronicle.views.get`
  * **Default views setup:** Before enabling the updated Cases experience, set up your default views under **SOAR Settings > Case Data > Views**. Make sure to manually copy over advanced widget configurations (such as **Safe HTML Rendering** or custom conditions) from the **Default Alert View** and **Default Case View** to the **New Default Alert View** and **New Default Case View** to preserve your preferred setups.



## Key terminology

  * **Investigation Management:** The end-to-end security analyst experience where you triage, investigate, and manage security issues.
  * **List view:** The default table layout that displays your cases, alerts, and detections in a full-width interface.
  * **Side-by-side view:** An interactive split-screen layout that lets you select an alert or detection from the list and inspect its detailed metadata, status, priority, creation date, and Gemini investigation insights in an adjacent pane without navigating away from the list.
  * **Case Queue:** Your list of active assigned cases, visible in both the list view and the side-by-side view layouts.
  * **Finding:** A general term for any security item you investigate. This includes alerts and non-alerting detections. Individual events, entities, and cases are not considered findings on their own; instead, a case is a collection of related findings.
  * **Detection:** A security signal triggered by a rule configured with alerting disabled (Alerting=Off). It flags potentially suspicious behavioral patterns in your environment, usually used for noisy rules, rules during the testing process, and similar scenarios where you are not sure that the rule is well tuned.
  * **Alert:** A security signal generated by a rule configured with alerting enabled (Alerting=ON) that requires analyst triage. Unlike events and detections, an alert is a security finding that should be investigated, and will either become a part of a new case, or grouped into an existing case.
  * **Entity:** An identifiable subject or asset (such as a user, hostname, IP address, or file hash) that represents the core building blocks of a security alert. It's used to enrich raw event logs with context, correlate isolated alerts, and track behavioral baselines across your network.
  * **Indicator of Compromise (IoC):** Known malicious data artifacts identified by threat intelligence feeds that suggest a resource may have been compromised or associated with malicious activity.
  * **Event:** A single record of activity in your network, stored as either a raw log or normalized into the UDM format.



## Compare the legacy Cases experience with the new Cases experience

The following table highlights the operational shift and key capability differences between the legacy Cases experience and the revamped, unified new Cases experience:

Capability and feature | Legacy Cases Experience | New Cases Experience  
---|---|---  
**Core focus** | Focused on reactive triage, investigation, and remediation workflows. | Expands to support broader workflows, such as proactive threat hunt investigations using raw data and detections.  
**Case structure and scope** | Cases are built around alert groups. | Cases are flexible, letting you group alerts, detections, and raw telemetry together.  
**Data and search integration** | Uses case-bound searches with queries restricted to a limited set of fields. | Integrates with UDM Search, letting you query raw data across the environment and link findings directly to new or existing cases. For details, see [Attach SIEM search results to cases](https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/create-case-from-search)  
**Analyst interface and triage** | Uses standard table views to navigate the case queue. | Adds a customizable case table with column filters, quick-action side drawers, and instant previews.  
**AI and threat visibility** | Driven by standard playbooks and manual analyst workflows. | Integrates AI-driven agentic workflows and [Triage and Investigation Agent (TIN)](https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent) visibility.  
**Navigation and sharing** | Uses session-bound URLs and standard product navigation. | Uses persistent URLs, streamlined navigation, and breadcrumbs for collaboration.  
  
## Where can I see cases?

The **Cases** page serves as the primary landing space for case triage and investigation management. This central layout displays your operational case queue and tracks total real-time case counts.

To streamline your investigative focus, you can apply specific column sorting parameters or use filters to display only the analyst context and metrics relevant to your immediate triage flow with the new Cases experience.

## Flexible case structure

Cases are flexible containers that allow you to group multiple data types into a single investigation. A case can contain a mix of alerts, detections, and individual events. 

Ingested data attaches to a case through two distinct methods:

  * **Alerts (Automated or Manual):** The platform can automatically group related alerts into an existing case based on grouping rules, or you can manually add an alert or move an alert to a different case during triage.
  * **Detections and Events (Manual Only):** Detections and individual telemetry events never group automatically. You must manually associate them, either directly from a detection view or by using UDM search results to link events to a new or existing case.



## How can I view and investigate alerts and detections?

From the main table view on the **Cases** page, you can inspect individual cases or review their underlying signals before diving into a full deep dive:

  * **Preview cases, alerts, and detections:** Click the **Preview case** icon to open a quick preview side-drawer. This layout lets you review critical context, take fast actions like assigning owners, and cycle through findings without leaving the main case queue page.
  * **View associated alerts and detections:** Expand any case row directly within the table to see a nested breakdown of its linked alerts, detections, severities, and risk scores.
  * **Inspect detection context:** Within an open case, selecting a specific alert or detection opens a side drawer summarizing its details, timeline metrics, and foundational event logs. For deep-dive analysis, you can jump directly from this preview panel to the dedicated, comprehensive page for that specific item.
  * **Analyze raw and normalized signals:** Review the underlying technical evidence associated with a case. To learn more about navigating these records, see [Use the Events Viewer](https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/use-events-viewer).



## What can I track within a case?

Opening a specific case loads all of the chronological activity, automation history, and contextual data required to resolve the security issue.

The **Case Top Bar** displays essential case-level details—including the title, ID, [priority, and stage](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/what-actions-can-you-take-on-a-case)—alongside options to collaborate using the built-in [Chat](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/instant-messaging-on-a-case) or execute [Case Actions](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/what-actions-can-you-take-on-a-case).

From this view, you can interact with the following tabs:

  * **Overview:** Displays a customizable layout featuring case-specific widgets—including lists of alerts and detections, associated UDM events, involved entities, and pending manual actions—a built-in Gemini summary, and historical context.

**Note:** The updated experience includes two dedicated views: **New Default Alert View** and **New Default Case View** (located under **SOAR Settings > Case Data > Views**). These default views display standard preconfigured widgets and don't automatically include custom widgets from your legacy views. To keep your current setup, you must manually copy your custom widgets and advanced configurations (such as **Safe HTML Rendering** settings or custom conditions) from the **Default Alert View** and **Default Case View** to these new views before enabling the feature.
    * **Dynamic Menu Navigation:** The side navigation panel matches the order of your widgets. Click any section title to jump straight to that specific widget (such as **UDM Events**).
    * **Visual Graph Mapping:** From the side navigation panel, you can also access the **Entities Graph** to visually map out asset interactions or entity relationships. For more information, see [Explore the Case Overview tab](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/whats-on-the-case-overview-tab).
  * **Case Wall:** Review a central, chronological log documenting every investigation step, user comment, file attachment, and system action taken over the lifecycle of the investigation. For more information, see the [Cases overview](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/cases-overview#case-wall-tab).

  * **Alerts & Detections:** Review the list of alerts and detections tied to the case, including their specific rule associations, metadata, and previews.




To customize how findings display in this tab, click  format_list_bulleted  **Layout view selection** to select a layout:

  * **List view:** Displays all alerts and detections in a full-width table.
  * **Side-by-side:** Opens a dual-pane layout so you can click any alert or detection in the list and inspect its detailed metadata, status, priority, creation date, and Gemini investigation insights in an adjacent side pane.

**Note:** For alerts ingested using a SOAR connector rather than Google SecOps SIEM, UDM events still appear in the events list. However, when you open the event details (Events Viewer), you might not see the same depth of parsed fields or raw log telemetry as you would for events ingested through the SIEM.
  * **Playbooks:** Track the real-time execution of automated playbooks triggered by the case and monitor individual step statuses. For more information, see [Work with Playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen).




## How do I take actions on cases?

As you investigate a case, you can update its status, assign ownership, or add tags to keep your tracking current.

You can quickly [close cases](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/how-to-close-cases), [change case priorities and stages](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/what-actions-can-you-take-on-a-case), update assignees, [apply tags](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/define-tags-in-cases-admin), or run broader [case actions](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/what-actions-can-you-take-on-a-case).

## Troubleshooting

This section outlines potential performance or access issues and their resolutions.

### Latency and limits

Initial loading of the case table layout can experience latency depending on overall data volume. The interface utilizes infinite scroll to handle large data pools; however, loading highly expansive result sets can introduce brief delays. Applying targeted filters helps optimize load times.

### Scale and capacity limits

To maintain system responsiveness and platform performance, Google SecOps enforces the following capacity thresholds per case:

  * **Detections:** A single case can hold up to 500 detections.
  * **UDM events:** A single case can hold up to 5,000 UDM events.



These limits apply across all manual additions, automated agent reports, and system-ingested findings. For more information about manually attaching events or detections from search results, see [Attach SIEM search results to cases](https://docs.cloud.google.com/chronicle/docs/secops/investigate/investigation-management/create-case-from-search). If a case reaches these thresholds, you must remove existing findings before attaching additional data.

### Error remediation

Use this table to quickly resolve common interface issues:

Issue description | Fix  
---|---  
Applied filters don't display expected results. | Verify that parameters are typed correctly and are valid for the active dataset.  
Queue customizations don't persist. | Ensure you save and apply your tailored table settings view.  
Unable to access case management features. | Confirm your instance has the Investigation Management experience enabled and verify your SOAR Admin permissions.  
The **Events** tab shows no events for an alert or case. | Check the alert's ingestion source. Alerts ingested through SOAR connectors don't store raw UDM logs in the SIEM backend, so raw event telemetry isn't available in this view. Inspect the alert details panel instead to review its parameters and context.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
