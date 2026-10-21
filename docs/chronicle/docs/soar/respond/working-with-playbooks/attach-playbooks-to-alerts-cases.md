---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/attach-playbooks-to-alerts-cases/
title: Attach playbooks to alerts or cases \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:34:07.085484+00:00
---

# Attach playbooks to alerts or cases  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/attach-playbooks-to-alerts-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Attach playbooks to alerts or cases

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** The **Cases scope playbook** features described in this document are not available to all customers in all regions.

This document outlines the attachment limits and priority settings for playbooks associated with an alert or case in Google Security Operations, followed by the steps necessary to manually add a playbook or playbook block to an active investigation.

### Attachment and execution limits

To preserve platform stability, keep track of the following capacity thresholds:

  * **Alert scope limits** : You can attach a total of 10 playbooks to any single alert. Only one playbook can attach automatically using an ingestion trigger, and an additional 9 playbooks can be attached manually. (Customers who have the [Reaction Triggers](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-reaction-triggers-in-playbooks) feature or the [Cases playbook](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/case-playbooks) feature enabled can attach a total of 30 playbooks.)
  * **Case scope limits** : The platform supports attaching up to 30 playbooks directly to a case container. Similar to alert playbooks, the system limits automatic playbook attachment upon ingestion to one case playbook per case. (This feature is not available to all customers in all regions.)
  * **Rerun limits** : Each unique playbook can be rerun a maximum of 10 times within a single case or alert. (Customers who have the [Reaction Triggers](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-reaction-triggers-in-playbooks) feature or the [Cases playbook](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/case-playbooks) feature enabled can rerun playbooks up to 30 times.)



### Playbook execution priority

You can set a playbook's priority between **1** (highest priority) and **3** (lowest priority). If multiple playbooks are attached, the playbook with the highest priority executes first. The default priority is **2** (medium). 

## Manually attach a playbook or playbook block

To add an existing playbook or a modular playbook block directly to an alert or case, follow these steps:

  1. In the **Cases** or **Alert** tab, click the specific container where you want to add the playbook.
  2. On the **Playbooks** tab, click **Add Playbook**. 
  3. Choose the playbook or the playbook block to add.
  4. Set the execution priority (the default is **2**).
  5. If the selected playbook block requires input parameters, confirm or modify the fields inside the **Inputs** dialog. If no inputs are required by the block logic, this dialog is skipped automatically.



The added playbook or playbook block appears directly on the **Playbooks** tab in the case or alert overview.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
