---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sso-onelogin/
title: Configure SSO using OneLogin \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:33.515874+00:00
---

# Configure SSO using OneLogin  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sso-onelogin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Configure SSO using OneLogin Stay organized with collections  Save and categorize content based on your preferences. 

This section describes how to configure SSO using OneLogin for use enterprise-wide OneLogin credentials to sign into Contact Center AI Platform (CCAI Platform) and the agent adapter. OneLogin SSO uses the Security Assertion Markup Language (SAML) authentication protocol.

## Before you begin

To configure SSO using OneLogin, be sure you have the following:

  * A OneLogin account
  * An SSO URL
  * An entity ID
  * An email mapping field, usually Name ID
  * A SAML certificate (in Base64)
  * CCAI Platform administrator credentials



## Configure OneLogin for SSO

To configure OneLogin, follow these steps:

  * In the CCAI Platform portal, invite a user and ensure the user is also invited to the OneLogin app with the same email address.

  * Ensure you have a OneLogin Admin account: [](https://www.onelogin.com/)<https://www.onelogin.com/>

  * Create a SAML application for CCAI Platform, but first ensure you are in the administration portal by clicking **Administration**.



  1. Click **Applications > Applications**.

  2. Click **Add App**.

  3. Search for _saml_.

  4. Select the **SAML Custom Connector (Advanced)** , or another SAML app you want to use.

  5. Click **Configuration**.

  6. Set end points.

![OneLogin configuration display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/16331e05b85ffa.png)

  7. Click **Save**.

  8. Open the **SSO** page from the menu.

  9. Select the preferred **SAML Signature Algorithm**.

  10. Copy the Issuer URL and the SAML 2.0 Endpoint (HTTP) in OneLogin and save for later use.

![Issuer and SAML endpoint display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/16331e05b8ca09.png)

  11. Click **View details**.

  12. Copy the X.509 Certificate and save for later use.

  13. Navigate to **User > Users**.

  14. Select a user.

**Note:** The user's email address must exist in the CCAI Platform portal user's list.
  15. Click **Applications**.

  16. Click the **+** icon to add the **SAML Custom Connector (Advanced)** application.




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

  3. Sign in with your OneLogin credentials.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
