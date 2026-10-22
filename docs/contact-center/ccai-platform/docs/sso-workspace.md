---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sso-workspace/
title: Configure SSO using Google Workspace \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:16.414580+00:00
---

# Configure SSO using Google Workspace  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sso-workspace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Configure SSO using Google Workspace Stay organized with collections  Save and categorize content based on your preferences. 

This section describes how to configure SSO using Google Workspace for use enterprise-wide Google Workspace credentials to sign into Contact Center AI Platform (CCAI Platform) and the agent adapter. Google Workspace SSO uses the Security Assertion Markup Language (SAML) authentication protocol.

## Before you begin

To configure SSO using Google Workspace, be sure you have the following:

  * Google Workspace administrator credentials
  * An SSO URL
  * An entity ID
  * An email mapping field, usually Name ID
  * A SAML certificate (in Base64)
  * CCAI Platform administrator credentials



## Configure Workspace for SSO

To configure Google Workspace, follow these steps:

  1. In Google Workspace Admin Console, go to **Apps > Web and mobile apps**.

  2. Click **Add app**.

  3. Select **Add custom SAML app**.

  4. In the **App name field** , add a name that will help you identify this SAML app as belonging to your knowledge base, like CCAI Platform instance SSO.

  5. Click **Continue**.

You'll be directed to the Google Identity Provider detail page. Google offers two options for getting the Google Workspace IdP info CCAI Platform instance needs. For CCAI Platform, used the section option.

  6. Copy the **SSO URL** , **Entity ID** , and **certificate**.




## Configure your CCAI Platform instance for SSO

To configure SSO for your CCAI Platform instance, follow these steps:

  1. In the Google Cloud console, go to the project selector dashboard and select the project that contains your instance. 

[Project selector dashboard](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. In the navigation menu, click **CCAI Platform**. 

[CCAI Platform instances](https://console.cloud.google.com/contact-center-ai-platform)

The **CCAI Platform instances** page displays.

  3. In the **Name** column, click the instance that you want to configure SSO for.
  4. On the **CCAI Platform instance Detail** page, click edit **Edit**.
  5. For the login method, select **SAML**.
  6. In the **Single sign-on URL** field, enter your SSO URL.
  7. In the **Entity ID** field, enter your entity ID.
  8. In the **Email field mapping** field, enter a text string such as `Email name` or `Name ID`. This is used as a label for the email name field on the SSO sign-in page.
  9. In the **Authentication contexts** field, select the authentication context that you want. If your IdP configuration doesn't require the authentication context to be specified, then leave this field empty. For more information, see [Authentication context](https://docs.cloud.google.com/contact-center/ccai-platform/docs/authentication-context).
  10. In the **Certificate** field, enter your SAML certificate. Be sure to include `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` from the certificate.
  11. Click **Save**.



## Add your CCAI Platform instance service provider details into the Google Workspace SAML App configuration

  1. Return to the Google Workspace Admin console and select **Continue**.

  2. In the **Service Provider** page enter the following details.

     * Enter the **ACS** URL: `https://{my_instance_id}.ccaiplatform.com/saml/v1/consume`

     * Enter the **Identifier (Entity ID)** URL: `https://{my_instance_id}.ccaiplatform.com/saml/v1/metadata`

     * Enter the **Start** URL: `https://{my_instance_id}.ccaiplatform.com/`

     * Set the **Name ID** format to Email.

  3. Click **Continue** at the bottom of the screen.

  4. Select the user group that will be able to access the application.

  5. Click **Finish**.




## Verify SSO authentication

To verify SSO authentication, follow these steps:

  1. Go to the agent adapter in your customer relationship management (CRM) application.

  2. Click **Login with company SSO**. A sign-in page displays.

  3. Sign in with your Google Workspace credentials.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
