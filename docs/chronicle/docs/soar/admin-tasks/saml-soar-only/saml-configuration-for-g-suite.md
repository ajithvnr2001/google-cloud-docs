---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/saml-configuration-for-g-suite/
title: Configure Google Workspace for SAML \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:28.152139+00:00
---

# Configure Google Workspace for SAML  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/saml-configuration-for-g-suite/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Google Workspace for SAML

Supported in:

[ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This document applies only to the standalone Google SecOps SOAR platform. 

**Note:** This document only applies if you have not yet completed Stage 1 of [SOAR Migration to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp). After the completion of Stage 1, refer to [Google Cloud Authentication](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication).

This document explains how to configure Google Workspace for authentication and how to connect it to the Google SecOps SOAR platform. 

## Configure Google Workspace for SSO

  1. Go to the [Google Admin Portal](https://admin.google.com/u/5/?pli=1).
  2. Select **Apps** > **Web and mobile apps**.
  3. In the **Add App** menu, select **Add custom SAML app**.
  4. Enter a name in **New Name of App** , upload an app icon, and then click **Continue**.
  5. On the **Google IdP Information** page, click **Next**.
  6. On the **Service Provider Details** page, enter the following information, and then click **Next** :
     * **ACS URL** : `https://{your_siemplify_server_IP_address}/Saml2/Acs`
     * **Entity ID** : `https://{your_siemplify_server_IP_address}/Saml2`
  7. In the **Attribute Mapping** screen, click **Add New Mapping**.
  8. Set the **Primary email** to `email`.
  9. Make sure that the **Service Status** is on.



## Configure Google Workspace in Google SecOps SOAR

  1. Go to **Settings > Advanced > External Authentication**.
  2. Create a new custom SAML provider.
  3. In the **Provider Type** menu, select **G Suite**.
  4. In the **Provider Name** field, enter a name (for example, `mycompany_workspace`).



Complete the following fields. When you're finished, click **Save** :

**IdP Metadata**

  1. Return to the Google Workspace app that you created, select **Download Metadata** from the menu, and save the XML file.
  2. In the Google SecOps SOAR platform, click the **IdP Metadata** field, and then **Upload** to upload the saved file.

**Identifier**

  1. Return to the Google Workspace app, expand **Service provider details** , and click **Manage Certificates**.
  2. Under **Google Identity Provider Details** , locate the **Entity ID** and copy and paste its contents into the Google SecOps SOAR **Identifier** field.
  3. In the Google SecOps SOAR platform, paste the contents into the **Identifier** field.

**ACS URL**

  1. Return to the Google Workspace app, expand **Service Provider details** , and copy the contents of the **ACS URL** field.
  2. In the Google SecOps SOAR platform, paste the contents into the **ACS URL** field, making sure to remove the trailing `"/Acs"` at the end.



For more information, see [Authenticate users using SSO](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/external-authentication).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
