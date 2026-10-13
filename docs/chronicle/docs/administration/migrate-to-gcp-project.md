---
url: https://docs.cloud.google.com/chronicle/docs/administration/migrate-to-gcp-project/
title: Migrate to a Google Cloud project \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:58.335801+00:00
---

# Migrate to a Google Cloud project  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/administration/migrate-to-gcp-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate to a Google Cloud project

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** For a comprehensive, end-to-end demo on the Migration process, see the [Google SecOps SIEM Legacy Infra Migration video ](https://youtu.be/Bg8VZftcrlg?si=3mvcaSucWS-KfZkd).

This document explains how to migrate an existing Google SecOps instance to a customer-owned Google Cloud project.

By linking a Google SecOps instance to a Google Cloud project, you can use Google Cloud services for key capabilities, for example:

  * Examine ingested data and monitor the project for potential security threats. 

  * Use authentication and monitoring features, including:

    * Cloud Identity integration for accessing a range of Google Cloud services, such as authentication, Identity and Access Management, Cloud Monitoring, and Cloud Audit Logs.

    * IAM and Workforce Identity Federation support for authenticating with your existing third-party IdP.


**Important:** If you have multiple frontend paths, self-service migration to Google Cloud projects and Workforce Identity Federation isn't supported. In this case, contact [Google SecOps Support](https://console.cloud.google.com/support) for assistance with the migration.

Before you begin, make sure you have the legacy Administrator role in your Google SecOps SIEM instance to perform the steps in this document.

To migrate an existing Google SecOps instance to a customer-owned Google Cloud project, do the following:

  1. Sign in to Google SecOps.
  2. Select **Settings > SIEM Settings**.
  3. Click **Google Cloud Platform**.
  4. Enter the Google Cloud project ID to link the project to the Google SecOps instance.
  5. Click **Generate link**.
  6. Click **Connect to Google Cloud Platform**. The Google Cloud console opens. If you enter an incorrect Google Cloud project ID in the Google SecOps application, return to the **Google Cloud Platform** page in Google SecOps and enter the correct project ID.
  7. On the Google Cloud console, go to **Security > Google SecOps**.
  8. Verify the service account that the system created for the Google Cloud project.
  9. Optional: You can configure single sign-on (SSO) at this point. Alternatively, you can do that in the next step, [Migrate from legacy authentication to Google Cloud authentication](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-auth-to-gcp-auth).
  10. Click **Connect**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
