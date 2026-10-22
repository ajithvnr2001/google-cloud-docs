---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sso-okta/
title: Configure SSO using Okta \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:03.977811+00:00
---

# Configure SSO using Okta  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sso-okta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Configure SSO using Okta Stay organized with collections  Save and categorize content based on your preferences. 

This section describes how to configure SSO using Okta for use enterprise-wide Okta credentials to sign into Contact Center AI Platform (CCAI Platform) and the agent adapter. Okta SSO uses the Security Assertion Markup Language (SAML) authentication protocol.

## Before you begin

To configure SSO using Okta, be sure you have the following:

  * An Okta account
  * An SSO URL
  * An entity ID
  * An email mapping field, usually Name ID
  * A SAML certificate (in Base64)
  * CCAI Platform administrator credentials



## Configure Okta for SSO

To configure Okta, follow these steps:

  1. In the Okta Admin Dashboard, Go to **Applications > Applications**

  2. Click **Create App Integration**

  3. Select **SAML 2.0** , then Click **Next**.

  4. Click **Next**.

  5. Specify a **Name** and **Logo**.

  6. Click **Next**.

  7. On the Configure SAML screen enter these values:

**Single sign on URL:** `https://<environmentname>.domain.co/saml/v1/consume`

Check **Use this for Recipient URL and Destination URL**

**Audience URI (SP Entity ID)** : `https://<environmentname>.domain.co/saml/v1/metadata`

**Name ID format** : customer provides, (For example, EmailAddress)

  8. On the **Feedback** panel provide feedback selections.

Suggested selections:

I'm an Okta customer adding an internal app

This is an internal app that we have created

  9. Click **Finish**.

  10. On the **Sign On** tab of the page that displays, click **View Setup Instructions** to launch a new tab.




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



## Verify SSO authentication

To verify SSO authentication, follow these steps:

  1. Go to the agent adapter in your customer relationship management (CRM) application.

  2. Click **Login with company SSO**. A sign-in page displays.

  3. Sign in with your Okta credentials.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
