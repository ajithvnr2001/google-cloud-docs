---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/configure-multiple-saml-providers/
title: Configure multiple SAML providers \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:29.238628+00:00
---

# Configure multiple SAML providers  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/configure-multiple-saml-providers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure multiple SAML providers

Supported in:

[ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This document applies only to the standalone Google SecOps SOAR platform. 

**Note:** This document only applies if you have not yet completed Stage 1 of [SOAR Migration to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp). After the completion of Stage 1, refer to [Google SecOps - Multiple providers](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-mssp-instance#set-up-gcp-auth-to-access-soar).

When managing security for diverse clients, a key challenge for Managed Security Service Providers (MSSPs) is accommodating their various authentication methods and Identity Providers (IdPs). By configuring multiple instances for each SAML provider, MSSPs can efficiently handle these unique requirements.

This document explains how this approach can simplify customer onboarding, improve management, and enhance security by ensuring each customer's configurations are isolated.

To configure a few different providers for Okta, follow these steps: 

  1. Go to **Settings** > **Advanced** > **External Authentication**.
  2. Click  add  **Add** , select the **Provider Type** , and then enter the **Provider name**.
  3. Configure the SAML parameters as required. 
  4. Repeat this procedure as many times as needed.



## Sign in as a SAML user

  1. Click **Sign in with SAML**.
  2. In the next screen, you're prompted to add your **Login Identifier** (this can be either an email or a username).
  3. Click **Login with External Provider**.

For more information, see [Authenticate users using SSO.](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/external-authentication)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
