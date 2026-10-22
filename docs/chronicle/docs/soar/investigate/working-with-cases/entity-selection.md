---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/entity-selection/
title: Perform entity selection \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:31.175412+00:00
---

# Perform entity selection  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/entity-selection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Perform entity selection

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how Google Security Operations extracts and uses entities from ingested alerts. When Google SecOps ingests an alert, it also includes the underlying security events. These events are analyzed to extract key indicators—such as IP addresses, usernames, and domains—which are then modeled as objects called _entities_. Each entity includes its own set of properties. 

## View the properties of an entity

  1. On the **Cases** page, select a case. In the default case view, entities appear in the **Entity Highlights** section on the **Case Overview** tab (or the **Alerts** tab in the legacy experience). 
  2. Click **View Details** to open a side drawer that shows all properties of the selected entity. 
  3. Click an entity name to open the **Entity Explorer** in a new tab. The **Entity Explorer** displays all cases associated with the selected entity. 



## Entity Selection action

When an alert is ingested, a playbook is automatically or semi-automatically triggered, depending on the configured conditions. Google SecOps uses these playbooks to determine how to handle the alert. 

Each action within a playbook operates on a specific group of entities. The **Entity Selection** action lets you define these groups based on entity properties. For example, you can create a group containing only internal entities to be used with actions tailored for internal assets. 

Use the **Entity Selection** action to build different groups depending on the logic you want to apply. When you use this method, it helps each action operate only on the relevant entities. 

### Create a new entity group

To create an entity group using the **Entity Selection** action, follow these steps:

  1. Go to the **Playbooks** page and click **Open Step Selection**. 
  2. In the **Step Selection** tab, select **Actions > Flow**. 
  3. Drag **Entity Selection** into the second box labeled **Drag a step over here**. 
  4. Double-click the **Entity Selection** box to configure the new group of entities. 
  5. Add the conditions needed to select the new group of entities. For example, select all IP address entities that were enriched by VirusTotal v3 and flagged as malicious by more than ten engines.
  6. Once defined, the new entity group becomes available for all subsequent actions in the playbook. 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
