---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/external-authentication/
title: Authenticate users \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:44.247340+00:00
---

# Authenticate users  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/external-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Authenticate users

Supported in:

[ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This document applies only to the standalone Google SecOps SOAR platform.  Note: This document only applies if you have not yet completed Stage 1 of [SOAR Migration to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp). After the completion of Stage 1, refer to [Google Cloud Authentication](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication). 

This document describes how to configure a SAML provider with one of these use cases:

  * For Okta, see [Configure Okta in Google SecOps SOAR](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/saml-configuration-for-okta).
  * For Google Workspace, see [Configure SAML for Google Workspace](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/saml-configuration-for-g-suite).
  * For Azure, see [Configure SAML for Microsoft Azure](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/saml-configuration-for-azure).



After you configure the SAML provider, you can authenticate users in the Google SecOps SOAR platform, as follows:

  1. Go to **SOAR Settings > Advanced > External Authentication**.
  2. On the **Provider** page, click  add  **Add**.
  3. In the **Provider Type** field, select the required SAML provider. For example, **Okta** or **Google Workspace**.
  4. In the **Provider Name** field, enter the name of the instance. For example, **Okta Customer name**. 
  5. Set the **Configuration** settings using the following details: Field | Description  
---|---  
Provider name | Name of the SAML provider.  
IdP Metadata | SAML metadata that shares configuration information between the Identity Provider (IdP) and the Service Provider (SP). If you use a certificate, set `WantAuthnRequestsSigned="true"` in the XML; otherwise, set it to `false`.  
Identifier | The SP ID in the SAML provider. This term is referred to as **Entity ID** in Google Workspace, though service providers can use different names.  
ACS URL | Google SecOps SOAR server name. Can be an IP URL, Hostname URL, or Local Host URL.  
To sign in with SAML, you must do the following:  

     1. Connect to the platform with the same URL pattern as configured in this field.
     2. Make sure that the URL contains the IP address of the Google SecOps SOAR server, followed by `/saml2`.  
Unsolicited Response  |  This setting is also known as an _IdP-Initiated response_. It lets SAML users access the Google SecOps SOAR platform directly from their IdP application. For example, if your company uses Okta, users can enter Google SecOps SOAR directly through the Okta application. **Note** : You can use an unsolicited response only when you have a single SAML provider configured in the platform.   
Auto-redirect |  Auto-redirect automatically sends users who aren't signed in to the IdP login page. To force a user to sign in to the platform directly, append `?autoExternalLogin=false` to the URL. Example: `https://example.com/#/login?autoExternalLogin=false`. **Note** : You can use this option only when you configure a single provider.   
  6. Click **Test** to verify that the configuration works.
  7. Click **Save**.
  8. Select one of the user creation types as needed:
     * **Manual** : Add users, individually, in the **User Management** window. For details on how to add users, see [Manage users](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/how-do-i-add-a-new-user-to-the-platform).
     * **Just in Time** : Automatically create the user (at login) in Google SecOps. When you select this option, an advanced tab opens with more parameters. For details, see [Configure just-in-time provisioning](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/what-is-justintime-user-provisioning).
     * **IdP Group Mapping** : Create the user automatically in Google SecOps based on the IdP group assignment. When you select this option, an advanced tab opens with more parameters. For more information on IdP group mapping, see [Map IdP groups to SOAR roles](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/idp-group-mapping-soar-only).



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
