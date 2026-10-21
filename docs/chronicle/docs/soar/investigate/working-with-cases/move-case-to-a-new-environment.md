---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/move-case-to-a-new-environment/
title: Relocate cases between environments \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:24:16.844137+00:00
---

# Relocate cases between environments  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/move-case-to-a-new-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Relocate cases between environments

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to move a case from one environment to another, or duplicate it across environments. This is useful if your organization uses multiple environments and you need to transfer or share cases between them.

**Note:** Verify that the setting to allow case transfers between environments is enabled on the **Settings** page. For more information, see [Work with environments](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/work-with-environments). 

To move or duplicate a case to another environment, follow these steps:

  1. Go to the **Cases** page.
  2. Open the case you want to move.
  3. In the case view, click **Environment** and then select the target environment.
  4. In the **New Environment** dialog, select one of the following options: 
     * **Confirm** : Creates a copy of the case in the selected environment. The new case has a different case ID.
     * **Close current case** (checkbox) **> Confirm**: Closes the case in the current environment and creates a new case with a different case ID in the selected environment.



  


**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
