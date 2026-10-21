---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/create-a-manual-case/
title: Create a case manually \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:34:38.054277+00:00
---

# Create a case manually  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/create-a-manual-case/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a case manually

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

You can manually create a case to enter specific data. This is useful when you need to ingest information on an alert; for example, information that was reported from sources that aren't integrated with your detection pipeline (for example, alerts reported from non-cyber channels). 

  1. On the **Cases** page, click  add  **Add > Create Manual Case**.
  2. Enter the following case properties: 
     * **Case Title** : Enter a title for the new case. 
     * **Creation Reason** : Enter the reason for creating the case. 
     * **Environment** : Select the specific environment being monitored. 
     * **Assigned To** : Assign the case to a specific role or user. 
     * **Priority** : Set the priority level for the case. 
     * **Mark as Important** : Click the **Mark as important** toggle on if the case should be flagged as important. 
  3. Click **Next**.
  4. In the **Alert** step, enter the following alert information: 
     * **Alert Name** : Enter a name for the security alert. 
     * **Occurrence Time** : In the calendar, select the date and time the alert occurred. 
     * **SLA** : Specify a date and time by which the SOC team should resolve the case. 
  5. Click **Next**. 
  6. In **Entities** , select any required existing entities, as follows; you can:
     * Add an existing entity or create a new one with a corresponding identifier.
     * Mark an entity as suspicious (this highlights it in red).
  7. Click **Next**. 
  8. In **Tags** , select any existing tags, create new tags, or leave blank, according to your needs. 
  9. Click **Next**. 
  10. In **Playbooks** , configure how playbooks attach to the new case: 
     * **Attach playbooks automatically** : Enable the toggle to allow matching system triggers to attach playbooks automatically. 
     * **Attach alert playbooks manually** : Select one or more alert-scoped playbooks from the menu to execute on individual alerts. 
     * **Attach case playbooks manually** : Select one or more case-scoped playbooks from the menu to run across the overarching case container. 

_Note: You can attach up to 30 unique playbooks per alert or case. Automatically attached playbooks take precedence over manually attached playbooks._

  11. Click **Finish**. 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
