---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-api-keys/
title: Authenticate to legacy SOAR API \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:17.125505+00:00
---

# Authenticate to legacy SOAR API  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-api-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Authenticate to legacy SOAR API

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** If you've migrated to Google Cloud, you need to migrate from the legacy SOAR API to the new Chronicle API. For more information, see [Authenticating to API](https://docs.cloud.google.com/chronicle/docs/reference/authentication) .

To authenticate and connect using the legacy Google Security Operations SOAR API, you must first create an API key.

You can access the SOAR API over port 443.

To create a new API key:

  1. Go to **Settings > Advanced > API keys**.
  2. Click  add **Add**.
  3. On the **API** page, enter the name for the application that requires API access to Google SecOps SOAR.
  4. Select the required permission group for this API key. The groups on this menu are defined on the **Organizations > Permissions** page.
  5. Select the environments to associate with the API key. If you select all current environments, the key only applies to environments that exist at the time of creation. To confirm access to new environments, use a permission group with **All Environments** enabled.
  6. Select the SOC role. For information about SOC roles, see [Control access to the platform](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/control-access-to-platform).
  7. Click **Save**. The new key appears on the **API keys** page.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
