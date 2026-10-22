---
url: https://docs.cloud.google.com/identity/docs/how-to/view-allowlisted-domains-audit-logs/
title: Viewing audit logs \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:46.593158+00:00
---

# Viewing audit logs  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/view-allowlisted-domains-audit-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Viewing audit logs

Audit logs are generated for modifications made using the Allowlisted Domains API, including the creation and deletion of domains in the allowlist. These actions are logged in the backend with specific activity types, such as `Add trusted domains` or `Remove trusted domains`. Administrators can check these audit logs to validate if a domain was added or deleted in the last 6 months.

To view audit logs, follow these steps:

  1. In the **Google Admin console** , go to **Menu** > **Security** > [**Security center**](https://support.google.com/a/answer/1219251#securitycenter) > **Investigation tool**.   
Requires having the Security center administrator privilege.
  2. For **Data source** , select **Admin log events**.
  3. Click **Add Condition**.
  4. For the attribute, select **Event** , select **Is** as the operator, and choose **Add trusted domains** or **Remove trusted domains**.
  5. Click **Search**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
