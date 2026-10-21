---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/create-block-list-to-exclude-entities-from-alerts/
title: Exclude entities from alerts \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:53.140439+00:00
---

# Exclude entities from alerts  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/create-block-list-to-exclude-entities-from-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Exclude entities from alerts

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

You can create a blocklist of items to prevent the system from grouping alerts by specific entities, or to exclude entities from being displayed in the system. 

## Add a new blocklist item

To add a new blocklist item, follow these steps:

  1. Go to **SOAR Settings > Environments > Blocklist**.
  2. Click add **Add Blocklist**.
  3. Enter the **Entity Identifier**.
  4. Select the **Entity Type**.
  5. Choose the appropriate **Action** : 
     * **Do not group alerts** : The entity won't be used to group alerts. Alerts containing this entity remain visible.
     * **Do not create entity** : The system doesn't create or process this entity.
  6. Choose the relevant **Environment**.
  7. Click **Add**.



For more information about how grouped alerts are managed, see [Configure alert grouping](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/alert-grouping-mechanism-admin). 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
