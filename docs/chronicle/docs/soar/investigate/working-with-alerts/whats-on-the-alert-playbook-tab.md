---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/whats-on-the-alert-playbook-tab/
title: Review and manage alert playbook execution \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:23.714000+00:00
---

# Review and manage alert playbook execution  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/whats-on-the-alert-playbook-tab/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Review and manage alert playbook execution

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document provides a reference for the **Playbooks** tab, which appears on the **Cases** page when a Playbook is attached to an alert.

When you select a Playbook from this tab, a side drawer opens to display the execution summary and key metrics.

  * **Playbook name and status** : The name of the playbook and its current run status.
  * **Pending Action: waiting for user input** : The playbook is waiting for an analyst to take action. A push notification also informs the relevant user that the playbook is awaiting their input.
  * **Time and length of playbook run** : Shows the start time and the total duration of the playbook run.
  * **Integrations** : List of integrations used by this playbook. When you click an integration, it marks the specific step in the playbook viewer, letting the analyst to focus on it. 
  * **Playbook flow** : Each step that was run with its status and step result.
  * **Errors** : List of errors. Errors that stop the playbook are highlighted at the top of the summary, while skipped actions appear at the bottom. You can also choose to rerun the action or playbook from this point.



You can click any of the playbook steps to see information relating only to that step in the side drawer.

[ ![alertplaybooktab1](https://docs.cloud.google.com/static/chronicle/images/soar/alertplaybooktab1.png)](https://docs.cloud.google.com/static/chronicle/images/soar/alertplaybooktab1.png)

The following actions are available at the top of the **Playbooks** tab: 

  * autorenew  **Refresh** : Updates the **Playbooks** tab to display the latest information.
  * ![jumptocasewallicon](https://docs.cloud.google.com/static/chronicle/images/soar/jumptocasewallicon.png)**Jump to Case Wall** : Takes you to the case wall directly from the **Playbooks** tab.
  * add **Add Playbook** : Choose the playbook to add to the case.



Click  replay **Rerun Playbook** to rerun playbooks attached to alerts. For more information, see [Rerun playbooks](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/rerun-playbooks). 

[ ![alertplaybooktab3](https://docs.cloud.google.com/static/chronicle/images/soar/alertplaybooktab3.png)](https://docs.cloud.google.com/static/chronicle/images/soar/alertplaybooktab3.png)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
