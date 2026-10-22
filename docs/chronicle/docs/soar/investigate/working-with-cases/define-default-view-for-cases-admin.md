---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/define-default-view-for-cases-admin/
title: Configure the default case view \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:10.840948+00:00
---

# Configure the default case view  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/define-default-view-for-cases-admin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure the default case view

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how administrators can configure a unified default view for all cases shown on the **Cases** page. This unified view helps analysts quickly assess and act on the most critical case information. 

To define a default view, go to **Settings > Case Data > Views > Default Case View**. 

## Access the Default Case View

The **Default Case View** editor displays a set of system widget and a layout template where you can place them. Use the editor to build a case overview that meets your organization's needs.

### Customize your view layout

You can customize the layout by dragging widgets from the side pane into the layout area. Available widgets include the following:

  * **Custom Fields Form** : displays any custom fields you've defined. Analysts can use this section to enter structured case data. Learn how to [create custom fields](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/adding-custom-fields). 
  * **Alerts** : displays alert-level information for all alerts grouped into the case, including alert name, number of events, and priority. 
  * **Case Description** : A free-text field for analysts to enter notes or context about the case. 
  * **Entities Highlights** : displays highlighted fields for each entity associated with the case. 
  * **Latest Case Wall Activity** : displays recent activities posted to the case wall within a configurable time window. 
  * **Pending Actions** : Lists all playbook actions that require analyst input to keep the playbook running. 
  * **Recommendations** : Displays similar cases and suggests analysts and tags to assign to the case. 
  * **Statistics** : Displays the distribution of selected entity fields. 
  * **HTML** : Supports HTML code to create insights and inject relevant information from playbook results. Gives the option to return safe code without potentially malicious JavaScript. 
  * **Key Value** : Displays a single key-value pair, such as `Key: Product`, `Value: [Alert.Product]`. 
  * **Free Text** : Lets you display static free-text content in the case overview. 
  * **Entities Graph** : Displays a visual graph and details of the case entities. 
  * **Insights:** Shows insights from playbooks, general logic, or manual analyst input in HTML format. 
  * **Quick Actions** : Displays action buttons that let analysts run predefined actions on cases directly from the case overview. For more information, see [Create a Quick Action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/quick-actions). 
  * **Gemini Summary** : Provides an AI-generated case summary and remediation suggestions.
  * **Composite Detections** : Available only for users of the Google SecOps unified platform. This widget helps analysts understand the components of alerts within a case. For [composite alerts](https://docs.cloud.google.com/chronicle/docs/detection/rule-chaining) (from chained rules), this widget shows:
    * Contributing detections
    * Alert lineage
    * Associated UDM events
  * For single alerts, it displays only their specific UDM events. This helps analysts understand alert structure and root cause.
  * **Rule Overview** : Available only for users of the Google SecOps unified platform. This widget provides information on the curated or custom rule associated with an alert, including a **View Details** button that opens a rule-overview sidebar with comprehensive rule information, including Rule Details (Name, Description, State, Severity, MITRE tags) and YARA-L Rule Code. It also includes a friendly link to manage the rule in the [Curated detections tab](https://docs.cloud.google.com/chronicle/docs/detection/use-curated-detections).



### Add widgets

To add widgets to the layout, do the following:

  1. Drag a widget from the pane to the template on the right. 
  2. You can rearrange the widgets as needed to create your preferred layout. 



### Edit widgets

To configure or update a widget:

  1. Click  settings  **Configuration**. Some widgets offer additional fields for configuration. For example, in the latest wall activity, you can specify the timeframe and activity types. 
  2. On the **Cases** page, update the widget title, tooltip, or width (50% or 100%), as needed. 
  3. Click **Save**. 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
