---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/rerun-playbooks/
title: Rerun automated playbooks \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:47.036422+00:00
---

# Rerun automated playbooks  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/rerun-playbooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Rerun automated playbooks

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document describes how to rerun a playbook associated with a case alert. This feature allows for up to nine reruns (10 total runs, including the initial execution) per alert.

This feature can be useful in the following situations:

  * **Data freshness** : Obtain more up-to-date results after the initial run.
  * **Error recovery** : Rerun the entire playbook following one or more failed steps.
  * **Logic updates** : Run the playbook with new logic after making changes on the **Playbooks** page.



To rerun a playbook, follow these steps:

  1. On the **Cases** page, go to the **Playbooks** tab of the selected alert.
  2. Locate the playbook you want to rerun.
  3. Click  replay  **Rerun Playbook**.



Each time you rerun the playbook, the system updates the iteration number and writes informative messages to the case wall.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
