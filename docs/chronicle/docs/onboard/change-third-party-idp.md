---
url: https://docs.cloud.google.com/chronicle/docs/onboard/change-third-party-idp/
title: Change authentication \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:36.011741+00:00
---

# Change authentication  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/onboard/change-third-party-idp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change authentication

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how to change the identity provider (IdP) of a Google SecOps instance. You might need to do this to switch to a different third-party IdP or to migrate from a third-party IdP to Cloud Identity.

This document covers the following procedures:

  * Change the third-party identity provider
  * Migrate from a third-party identity provider to Cloud Identity



## Change the third-party identity provider

This section describes how to change your Google SecOps instance to use a different third-party identity provider. Complete the following steps:

  1. Set up the new [third-party identity provider and workforce identity pool](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).

  2. In Google SecOps, under **Settings** > **SOAR settings** > **Advanced** > **IDP group mapping** , change the [IdP group mapping](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform#map-and-authenticate-users) to reference groups in the new identity provider.

**Important:** If you don't change this configuration before changing the identity provider in the following steps, you get an HTTP `403` error when accessing Google SecOps. If this happens, contact [Google SecOps Support](https://docs.cloud.google.com/chronicle/docs/getting-support) or your Google representative.



### Update SSO settings

Complete the following steps to change the SSO configuration for Google SecOps:

  1. Open the Google Cloud console, and then select the Google Cloud project that is linked to Google SecOps.

  2. Go to **Security > Google SecOps**.

  3. On the **Overview** page, click the **Single Sign-On** tab. This page displays the IdPs you configured when [Configuring a third-party identity provider for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).

  4. Use the **Single Sign-On** menu to change SSO providers.

  5. Right-click the **Test SSO setup** link, and then open a private or incognito window.

     * If you see a login screen, then SSO setup is successful. Continue with the next step.
     * If you don't see a login screen, check the configuration of the third-party identity provider. See [Configure a third-party identity provider for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).
  6. Return to Google Cloud console, click the **Security > Google SecOps > Overview** page, and then click the **Single Sign-On** tab.

  7. Click **Save** at the bottom of the page to update the new provider.

  8. Verify that you can sign in to Google SecOps.




## Migrate from third-party identity provider to Cloud Identity

This section describes how to change the SSO configuration from using a third-party identity provider to Google Cloud Identity. Complete the following steps:

  1. Make sure you configure either Cloud Identity or Google Workspace as the identity provider.
  2. Grant the predefined Chronicle IAM roles and custom roles to users and groups in the Google SecOps-bound project.
  3. Grant the **Chronicle SOAR Admin** role to the relevant users or groups.
  4. In Google SecOps, under **Settings** > **SOAR settings** > **Advanced** > **IDP group mapping** , add the **Chronicle SOAR Admin**. For more information, see [IdP group mapping](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform#map-and-authenticate-users).

**Important:** You must update this configuration before changing the IdP in the following steps. Skipping this step results in an HTTP `403` error when accessing Google SecOps. If you encounter this error, contact [Google SecOps Support](https://docs.cloud.google.com/chronicle/docs/getting-support) or your Google representative.
  5. Open the Google Cloud console, and then select the Google Cloud project is linked to Google SecOps.

  6. Go to **Security > Chronicle SecOps**.

  7. On the **Overview** page, click the **Single Sign-On** tab. This page displays the IdPs you configured when [Configuring a third-party identity provider for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).

  8. Select the **Google Cloud Identity** checkbox.

  9. Right-click the **Test SSO setup** link, and then open a private or incognito window.

     * If you see a login screen, then SSO setup is successful. Continue with the next step.
     * If you don't see a login screen, check the configuration of the identity provider.
  10. Return to Google Cloud console, and then click **Security > Chronicle SecOps** > **Overview** page > **Single Sign-On** tab.

  11. Click **Save** at the bottom of the page to update the new provider.

  12. Verify that you can sign in to Google SecOps.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
