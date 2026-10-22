---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/saml-configuration-for-azure/
title: Configure Microsoft Azure for SAML \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:25.479148+00:00
---

# Configure Microsoft Azure for SAML  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/saml-configuration-for-azure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Microsoft Azure for SAML

Supported in:

[ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This document applies only to the standalone Google SecOps SOAR platform. 

**Note:** This document only applies if you have not yet completed Stage 1 of [SOAR Migration to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp). After the completion of Stage 1, refer to [Google Cloud - Third-Party Identity Authentication](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).

This document explains how to configure SAML for Microsoft Azure to use with the standalone Google Security Operations SOAR platform.

## Before you begin

Confirm that you've set up a SAML account in Microsoft Azure by completing the instructions in the following Quickstart guides:

  * [ Create and assign a user account](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/add-application-portal-assign-users)
  * [ Add an enterprise application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/add-application-portal)
  * [ View enterprise applications](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/view-applications-portal)

**Note:** Keep the Azure portal open in a separate browser window. You'll need to copy and paste the information from it into the Google SecOps SOAR platform.

## Configure SAML in Microsoft Azure

To configure SAML in Microsoft Azure, follow these steps:

  1. Sign in to the Azure portal.
  2. Go to **Enterprise Applications**.
  3. Locate your company's SAML sign-on app.
  4. In the sidebar, select **Single Sign-on**.
  5. **Basic SAML Configuration** , configure the following fields and save your changes: 
     1. **Identifier (Entity ID)** : `https://platform_Address/Saml2/`
     2. **Reply URL (Assertion Consumer Service URL)** : `https://platform_Address/Saml2/ACS`
     3. **Sign on URL** : `https://platform_Address/Saml2/`



## Configure Azure in Google SecOps SOAR

  1. Go to **Settings > Advanced > External Authentication**.
  2. Create a new SAML provider.
  3. In the **Provider Type** menu, select **Custom SAML Provider**.
  4. Enter a provider name. For example, `mycompany_Azure`.



Complete the following fields using information from the Azure portal:

**IdP Metadata**

  1. Return to the Azure portal.
  2. In **SAML Certificates** , go to the **Federation Metadata XML** field.
  3. Click **Download** and save the Federation Metadata XML file.
  4. Return to the Google SecOps SOAR platform.
  5. In the **IdP Metadata** field, upload the Federation Metadata XML file to the **IdP Metadata** field.

**Identifier**

  1. Return to the Azure portal.
  2. Go to **Set up \** and click the **Microsoft Entra Identifier** field.
  3. Copy the data from the **Microsoft Entra Identifier** field.
  4. Return to the Google SecOps SOAR platform.
  5. Paste the value into the **Identifier** field.

**ACS URL**

  1. Return to the Azure portal.
  2. Go to **Basic SAML Configuration** > the **Sign On URL** field.
  3. Copy the data from the Azure **Sign On URL** field.
  4. Return to the Google SecOps SOAR platform.
  5. Paste the value into the **ACS URL** field.



## Field mapping

Google SecOps SOAR field | Microsoft Azure field  
---|---  
IdP Metadata  | Federation Metadata XML   
Identifier  | Microsoft Entra Identifier   
ACS URL  | Sign on URL   
  
For more information, see [Authenticate users using SSO.](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/external-authentication)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
