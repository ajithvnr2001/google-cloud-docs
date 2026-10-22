---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/working-with-collaborator-groups/
title: Work with collaborator user groups \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:06.945270+00:00
---

# Work with collaborator user groups  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/working-with-collaborator-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Work with collaborator user groups

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document introduces the _collaborator user group_ in Google Security Operations, a hybrid designed to bridge the gap between basic user and view-only user groups.

You can assign various permissions to a collaborator user group, specifically for selected modules within the platform. This functionality encourages a Managed Security Service Provider (MSSP) or an Enterprise company to collaborate effectively, run joint investigations, and discuss cases in real-time with their customers or end users.

The SOC manager can grant the collaboration user group either **view-only** or **edit** access to the following areas of the platform:

  * **Dashboards** : A collaborator group with dashboard access who can view metrics, trends, and Key Performance Indicators (KPIs) related to security operations. This access lets them monitor the overall health of the environment without being able to modify the underlying data or settings.
  * **Search** : With search access, a collaborator group can execute queries to investigate security events, review logs, and look for specific indicators of compromise. This powerful investigative tool lets them perform threat hunting or gather information relevant to an ongoing incident.
  * **Cases** : A collaborator user group can have access to a case and see an alert view specifically designed for their role. 
  * **Entity Explorer** : A collaborator group with Entity Explorer access can view detailed information about specific entities within the network, such as users, endpoints, IP addresses, or files. They can see an entity's timeline, associated alerts, and relationships to other entities, which is crucial for understanding the scope of an incident and an attacker's lateral movement.
  * **Reports** : A collaborator group with access can view pre-generated reports on various security topics, such as vulnerability scans, compliance audits, or incident summaries.
  * **Command Center** : Access to the Command Center can provide a collaborator group with a consolidated, real-time overview of all security operations. This might include a live feed of alerts, a summary of active cases, and a dashboard of key metrics.
  * **SLA** : The Service Level Agreement (SLA) lets the collaborator group track the performance of the security team in meeting defined response and resolution times for security incidents. This view gives them visibility into operational efficiency and helps ensure that security events are handled in a timely manner according to established agreements.
  * **Workdesk** : You can assign a **Manual** action (or an entire playbook block) in the playbook to a collaborator user group, along with writing a targeted message to them in the playbook action. The collaborator sees this message in both the **Pending Actions** widget in the playbook customized overview and in **Your Workdesk**.
  * **Workdesk: My Requests** : The collaborator user has access to the **My Requests** tab, where the user can choose to ask for a specific request from a selection of predefined requests.



##  Create a Collaborator user group

To create a Collaborator user group, follow these high-level main steps:

  1. Make sure you've purchased the Enterprise license, which gives you access to unlimited collaborators.
  2. Create a new **Collaborator** permissions group or use the predefined **Collaborator** group. For more information, see [Work with permission groups](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups).



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
