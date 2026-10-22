---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/saml-configuration-for-okta/
title: Configure Okta for SAML \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:33.132542+00:00
---

# Configure Okta for SAML  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/saml-configuration-for-okta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Okta for SAML

Supported in:

[ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This document applies only to the standalone Google SecOps SOAR platform. 

**Note:** This document only applies if you have not yet completed Stage 1 of [SOAR Migration to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp). After the completion of Stage 1, refer to [Google Cloud - Third-Party Identity Authentication](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).

This document explains how to configure Okta for authentication and how to configure the Google Security Operations SOAR platform to support this.

## Before you begin

To configure Okta in the Google SecOps SOAR platform, you must set up the SAML account in Okta. For details, see [ Create an app for SAML in Okta](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_saml.htm).

Once you set up the SAML account in Okta, you can configure the Okta settings in the Google SecOps SOAR platform:

  1. In the Google SecOps SOAR platform, go to **Settings > Advanced > External Authentication**.
  2. Click **Create a new SAML provider**.
  3. In the **Provider Type** menu, select **Okta**.
  4. Enter a provider name, such as `mycompany_Okta`, and click **Create**.
  5. Open the Okta portal and go to **Applications > Applications**.
  6. Select the SAML app you created.
  7. Click the **General** tab and go to **SAML Settings**.
  8. Copy the string in the **Audience Restriction** field.
  9. Return to the Google SecOps SOAR platform, and paste the string into the **ACS URL** field.
  10. Return to the Okta portal and in the SAML app, click the **Sign On** tab and locate and click **View SAML setup instructions**.
  11. Copy the string into the **Identity Provider Issuer** field.
  12. Return to the Google SecOps platform, and paste this string into the **Identifier** field.
  13. Return to the Okta portal. In **View SAML setup instructions** , go to the **Optional** heading and copy the Identity Provider (IdP) metadata into a text file. Save this file as **metadata.xml**.
  14. Return to the Google SecOps SOAR platform. Next to the **IdP Metadata** field, click  upload **Upload**.
  15. Click **Save > Test** to make sure the configuration is correct.

For more information, see [Authenticate users using SSO.](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/external-authentication)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
