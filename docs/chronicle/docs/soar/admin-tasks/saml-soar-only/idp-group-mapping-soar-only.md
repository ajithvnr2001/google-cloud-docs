---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/idp-group-mapping-soar-only/
title: Map IdP groups for SOAR standalone access \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:38.788022+00:00
---

# Map IdP groups for SOAR standalone access  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/idp-group-mapping-soar-only/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Map IdP groups for SOAR standalone access

Supported in:

[ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This document applies only to the standalone Google SecOps SOAR platform. 

**Note:** This section only applies if you have not yet completed Stage 1 of [SOAR Migration to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp). After the completion of Stage 1, refer to [Access Google Secops instance](https://docs.cloud.google.com/chronicle/docs/onboard/log-in-to-new-instance).

This document explains how to automatically create users in the Google Security Operations SOAR platform based on their Identity Provider (IdP) group assignments. **Note:** This feature is only available when a single provider is defined. 

## Before you begin

Read through and complete the instructions in [Authenticate users using SSO](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/external-authentication).

## Set up the IdP group mapping

The following procedure assumes you're setting up the **IdP group mapping** in the Google SecOps SOAR-only platform: 

  1. Select the **IdP group mapping** option. This opens an advanced tab where you can configure parameters based on the fields in your SAML provider.
     * **First Name Attribute** : Name of the attribute that contains the given name (for example, **first name** in Google Workspace).
     * **Last Name Attribute** : Name of the attribute that contains the user's family name (for example, **last name** in Google Workspace).
     * **Login ID Attribute** : Name of the attribute that contains the user's unique ID (for example, **subject** in Google Workspace).
     * **Email Attribute** : Name of the attribute that contains the user's primary address (for example, **primary email** in Google Workspace).
     * **Group Name Attribute** : Name of the attribute that contains the groups to which the user belongs within the organization (for example, **groups** in Google Workspace). 
  2. After you've defined the attributes, click  add  **Add IDP Group**.
  3. Complete the IdP group mapping table. For each IdP group from your SAML provider, you must assign the following:
     * A SOAR SOC role
     * A permission group
     * An environment or environment group (you can assign both at the same time).  
For more information about these fields, see [Control access to platform](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/control-access-to-platform).
  4. When you're finished mapping the IdP groups, click **Save**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
