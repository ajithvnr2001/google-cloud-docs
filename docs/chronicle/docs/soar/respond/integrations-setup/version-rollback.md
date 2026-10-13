---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/version-rollback/
title: Roll back response integrations \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:05.026446+00:00
---

# Roll back response integrations  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/version-rollback/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Roll back response integrations

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to roll back response integrations to a previously installed version. This is useful if a new version introduces unexpected behavior or if you need to revert custom code changes.

**Note:** This feature is not supported for custom or community integrations, or for customers in VPC-SC environments.

## Roll back to a previous version

To roll back to a previously installed version, follow these steps:

  1. Go to **Content Hub** and click the **Response Integrations** tab.
  2. Select the required response integration.
  3. Click **Details**.
  4. In the side drawer, click the **Versions** tab.
  5. Locate the **Last Installed** section and click **Rollback**.

**Caution:** A rollback reverts all content (standard code and custom modifications) to the state of the last installed version. Any custom work performed after that version was installed will be lost.

  6. In the confirmation dialog, click **Confirm**.
  7. Choose whether to override the existing ontology. For more information on managing ontologies, see [Ontology override](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/using-the-marketplace#ontology-override).
  8. Click **Confirm**. The system uninstalls the current version and restores the previous version.



**Important:** You can only roll back to a version if it was installed after the Rollback feature was enabled for your instance. The system creates a snapshot during the upgrade process; if no snapshot exists for a previous version, the Rollback option won't be available. Additionally, you cannot roll back to an integration version built for Python 2.7 or 3.7, as the current environment requires Python 3.11.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
