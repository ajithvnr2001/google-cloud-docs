---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-alert-type-trigger-in-a-playbook/
title: Trigger playbooks by alert type \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:16.019115+00:00
---

# Trigger playbooks by alert type  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-alert-type-trigger-in-a-playbook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Trigger playbooks by alert type 

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document describes how to use the **Alert Type** trigger to trigger a playbook, based on the **Rule Generator** name. 

  1. Go to the **Response > Playbooks** page and create a new playbook. 
  2. Drag the **Alert Type** trigger to a playbook step and double-click it to open it.
  3. The **Parameters** field requires the Rule Generator name of each alert that can trigger this playbook. Select the Rule Generator name from the menu.  
If you don't remember the Rule Generator name of the alert you want to trigger, go to **Cases > Overview**.
  4. In the **Alerts** widget, click **View Details**. The side drawer opens with case details. 
  5. Copy and paste this Rule Generator name, or select it from the menu. 
  6. Continue building the playbook. Once you've finished, this Rule Generator triggers the playbook for generated alerts. 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
