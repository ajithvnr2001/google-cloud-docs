---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/cases-overview2/
title: Case management overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:12:54.052962+00:00
---

# Case management overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/cases-overview2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Case management overview

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

Google Security Operations ingests alerts from a wide range of sources. Each alert includes its underlying security events and key indicators (such as sources, destinations, artifacts), which are parsed and analyzed. During this analysis, key indicators—such as source and destination IPs, file hashes, or user accounts—are extracted and represented as entities. Entities are persistent objects in the platform. They collect enrichment data, analyst comments, and historical context, letting analysts track entity behavior over time and across cases. Entities also appear on the visual canvas to help illustrate relationships in the threat landscape.

## Case creation and grouping

The **Cases** page is where analysts can investigate incoming alerts and manage incident workflows. Analysts can also: 

  * Automatically group additional alerts into existing cases based on shared entities and configurable rules.
  * Manually create cases or simulate cases for testing and training purposes.



## Case queue header and views

All active cases from various connectors appear in the case queue. Each case entry shows key metadata, such as:

  * Case name and unique ID
  * Case timestamp
  * Number of associated alerts
  * Assigned analyst (with avatar)
  * Case priority and stage (optional, depending on view)



Analysts can toggle between these views:

  * **Default view** : Shows case cards with essential information.
  * **Compact view** : Reduces visual footprint for faster scanning.
  * **List view** : Displays all cases in a table format for bulk operations or filtering.



## Case top bar

The **Case Top Bar** displays case-level context and available actions, as follows:

  * The case queue header displays the case title, ID, [priority, stage](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/what-actions-can-you-take-on-a-case), timestamp, change environment, and [tags](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/manage-tags-from-the-cases-screen).
  * It also shows the assigned analyst (name or role), and includes controls for [Chat](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/instant-messaging-on-a-case), [Close Case](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/how-to-close-cases), **Refresh** , [Explore](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/explore-entities-and-alerts-investigation), and the [Case Actions](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/what-actions-can-you-take-on-a-case) menu.



For details see [What's on the Cases page?](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/whats-on-the-cases-screen)

## Case tab

Each case includes several tabs that help analysts review, investigate, and act on case data. These tabs organize key information—from high-level summaries to detailed logs and alert data—into a consistent, navigable format.

### Case overview tab

The **Case Overview** tab displays case-specific widgets configured by the administrator. For details see [Explore the Case Overview tab](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/whats-on-the-case-overview-tab).

### Case Wall tab

The **Case Wall** tab displays a chronological log of all case-related events and actions, from creation to closure. When you open this tab, you can view case-related information such as tasks, user comments, pinned chat messages, manual and system actions, and file attachments (up to 50 MB per file). Each type of content is represented by an icon in the upper section of the Case Wall.

Actions you can do with this tab:

  * Click **View More** to display both the standard UI results and the corresponding JSON data.
  * To view event details, click one or more of the event icons.
  * To view events for all alerts in the case, select **All Alerts**.
**Icon** | **Description**  
---|---  
[ ![Action details icon](https://docs.cloud.google.com/static/chronicle/images/soar/casewalltab1.png)](https://docs.cloud.google.com/static/chronicle/images/soar/casewalltab1.png) |  Displays actions taken on alerts in a table, including the action name, timestamp, alert name, result, and status (**Completed** or **Faulted**).  
Click **Show More** to expand the results, parameters, and affected entities. Click **Show Less** to collapse the view.   
[ ![Case status change icon](https://docs.cloud.google.com/static/chronicle/images/soar/casewalltab2.png)](https://docs.cloud.google.com/static/chronicle/images/soar/casewalltab2.png) |  Displays all system- and user-generated case status changes, such as updates to the title, stage, priority, assignment, and closure.   
[ ![Task details icon](https://docs.cloud.google.com/static/chronicle/images/soar/casewalltab3.png)](https://docs.cloud.google.com/static/chronicle/images/soar/casewalltab3.png) |  Displays task-related activity. When a task is completed, click **Complete Task**. The status updates to **Completed** along with a timestamp and your comments.   
[ ![Comment icon](https://docs.cloud.google.com/static/chronicle/images/soar/casewalltab4.png)](https://docs.cloud.google.com/static/chronicle/images/soar/casewalltab4.png) |  Displays comments added manually or by the **Case Comment** action.   
[ ![Pinned chat icon](https://docs.cloud.google.com/static/chronicle/images/soar/casewalltab6.png)](https://docs.cloud.google.com/static/chronicle/images/soar/casewalltab6.png) |  Displays pinned messages from the **Instant Message** dialog.   
[ ![Favorite item icon](https://docs.cloud.google.com/static/chronicle/images/soar/casewalltab7.png)](https://docs.cloud.google.com/static/chronicle/images/soar/casewalltab7.png) |  Displays items marked as favorites in the Case Wall by clicking the yellow star icon.   
[ ![Sort icon](https://docs.cloud.google.com/static/chronicle/images/soar/casewalltab8.png)](https://docs.cloud.google.com/static/chronicle/images/soar/casewalltab8.png) |  Sorts event logs by timestamp, either from newest to oldest or oldest to newest.   
[ ![Insights icon](https://docs.cloud.google.com/static/chronicle/images/soar/casewalltab5.png)](https://docs.cloud.google.com/static/chronicle/images/soar/casewalltab5.png) |  Displays general insights and warnings about the case and associated entities.   
  * **Alert Overview** tab: Lists all alerts linked to the case, including associated events and metadata. This tab displays crucial information and events associated with the case.
  * The case queue—automatically refreshed every minute—lists all active cases and lets you manually refresh, sort, filter, add, or close cases as needed.



## Playbook automation

_Playbooks_ are predefined sets of actions that collect information from internal and external alert sources. They then make decisions on how to handle these alerts or perform operations on remote systems, such as blocking a firewall port or disabling an Active Directory user. Google SecOps performs these actions automatically or semi-automatically based on the playbook triggers on any alert ingestion.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
