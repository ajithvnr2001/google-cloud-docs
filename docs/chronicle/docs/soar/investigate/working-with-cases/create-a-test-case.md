---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/create-a-test-case/
title: Validate case workflows with test cases \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:36.955781+00:00
---

# Validate case workflows with test cases  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/create-a-test-case/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Validate case workflows with test cases

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to create and use a test case, which acts like a sandboxed version of a regular case. Any actions you perform on entities in a test case don't affect the same entities in other cases. A test case includes only the alert that triggered the event and is populated using existing data. You can use it to simulate a playbook or test behavior on the **IDE** page.

To create a test case, follow these steps:

  1. In the platform, go to the **Cases** page.
  2. Select the required case.
  3. Locate the target alert (on the **Alert** tab in the legacy experience, or within the alert details pane in the enhanced experience).
  4. Click more_vert **Alert Options** and select **Ingest alert as test case**.
  5. Select the required environment and click **Simulate**.
  6. Refresh the page.



A new test case appears in the case queue or list view. It's marked with the label **Test** on the case card and contains only one alert.

You can now use the test case in the Playbook Simulator, or the **IDE testing** page.

**Note:** Any changes that you make to entity properties in the test case won't affect those entities outside the test case.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
