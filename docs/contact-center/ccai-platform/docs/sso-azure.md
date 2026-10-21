---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sso-azure/
title: Configure SSO using Azure \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:02.449474+00:00
---

# Configure SSO using Azure  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sso-azure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Configure SSO using Azure Stay organized with collections  Save and categorize content based on your preferences. 

This section explains how to configure SSO using Azure for use enterprise-wide Azure credentials to sign into Contact Center AI Platform (CCAI Platform) and the agent adapter. Azure SSO uses the Security Assertion Markup Language (SAML) authentication protocol.

## Before you begin

To configure SSO using Azure, be sure you have the following:

  * An Azure account
  * An SSO URL
  * An entity ID
  * An email mapping field, usually Name ID
  * A SAML certificate (in Base64)
  * CCAI Platform administrator credentials



## Configure Azure for SSO

To configure Azure, follow these steps:

  1. Sign in to your existing Azure account.

  2. Navigate to the **Azure Portal** and click **Enterprise applications** :

  3. From the **Enterprise applications** page, click **New application:**

  4. In the search box type **saml**.

  5. Click **Azure AD SAML Toolkit**.

  6. If preferred, change the application **Name** , then click **Create**.

  7. Click **Set up single sign on**.

  8. Click the **SAML** option.

  9. Beside **Basic SAML Configuration** , click **Edit**.

  10. For **Identifier (Entity ID)** , enter `https://<environmentname>.ccaiplatform.com/saml/v1/metadata`.

  11. For **Reply URL (Assertion Consumer Service URL)** , enter `https://<environmentname>.ccaiplatform.com/saml/v1/consume`.

  12. For **Sign on URL** , enter `https://<environmentname>.ccaiplatform.com/`.

  13. Click **Save** at the top of the screen.

  14. Beside **User Attributes & Claims**, click **Edit**.

  15. Click **Unique User Identifier (Name ID)**.

  16. Change **Source attribute** to **user mail** , then click **Save**.

  17. Verify that the **Unique User Identifier** has been changed to **user mail**.

  18. Copy and save the **Login URL** and **Azure AD Identifier** to use later in the **CCAI Platform portal**.

  19. Click the download link for **Certificate (Base64)**.

  20. Open the file in a text editor for later use.




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

  3. Sign in with your Azure credentials.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
