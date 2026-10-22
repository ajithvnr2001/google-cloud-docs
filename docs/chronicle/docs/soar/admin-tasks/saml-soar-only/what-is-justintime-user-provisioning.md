---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/what-is-justintime-user-provisioning/
title: Configure just-in-time provisioning \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:18.380806+00:00
---

# Configure just-in-time provisioning  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/what-is-justintime-user-provisioning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure just-in-time provisioning

Supported in:

[ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This document applies only to the standalone Google SecOps SOAR platform. 

**Note:** This section only applies if you have not yet completed Stage 1 of [SOAR Migration to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp). After the completion of Stage 1, refer to [Access Google Secops instance](https://docs.cloud.google.com/chronicle/docs/onboard/log-in-to-new-instance).

This document explains how to configure just-in-time (JIT) provisioning for Okta users and Azure users.

With JIT enabled, Google Security Operations SOAR automatically creates the user after a successful SAML sign-in from the configured Identity Provider (IdP), such as Okta or Google Workspace.

**Note:** To set up JIT, the administrator must define all relevant fields in the Google SecOps SOAR platform and then map them to the SAML provider. You can only configure JIT for one SAML provider at a time. 

##  Define JIT provisioning for Okta users

  1. In Google SecOps SOAR, go to **Settings > Advanced > External Authentication**.
  2. Select **Okta** and enter the required parameters.
  3. Select the **JIT provisioning** checkbox to display the mapping fields.
  4. In Okta, click **Directory > Profile Editor**. Copy the exact field names and enter them into the corresponding fields in Google SecOps SOAR.
  5. Confirm the fields are identical in the Google SecOps SOAR platform and in Okta, and then save.



##  Define JIT provisioning for Azure users

  1. In Google SecOps SOAR, go to **Settings > Advanced > External Authentication**.
  2. Select **Azure** and enter the required parameters.
  3. Select the **JIT provisioning** checkbox to display the mapping fields, then use the following standard claim URIs:
     * **First Name Attribute** : `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname`.
     * **Last Name Attribute** : `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname`.
     * **User Name Attribute** : `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name`.
     * **Email Attribute** : `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name`. The Email Attribute can also sometimes be seen as `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`.

**Note:** If Google SecOps SOAR expects the **LoginID** to be the user's email, set **NameID** to `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress` and map **Email** to **NameID** in your IdP. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
