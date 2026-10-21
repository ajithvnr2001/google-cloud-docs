---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk/zendesk-config/
title: Zendesk configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:54:29.240203+00:00
---

# Zendesk configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk/zendesk-config/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Zendesk configuration Stay organized with collections  Save and categorize content based on your preferences. 

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

This page describes how to set up authentication and permissions before creating the Zendesk data store.

## Enable token access

To allow the Zendesk to authenticate and interact with your Zendesk instance, you must enable token access. Follow these steps to enable token access:

  1. Navigate to your Zendesk instance and sign in with an administrator account.
  2. In the navigation menu, expand **Apps and integrations** , then select **API configuration** from **APIs**.
  3. Select the **Allow API token access** checkbox.
  4. Click **Save**.



## Set up authentication and permissions

For secure integration using OAuth 2.0, you must register your application in Zendesk to obtain the necessary client ID and client secret.

### Create an OAuth client and obtain authentication credentials

To create an OAuth client in Zendesk and obtain the authentication credentials, follow these steps:

  1. Navigate to your Zendesk instance and sign in with an administrator account.

**Note:** Your instance URL is in the format `https://<var>your-subdomain</var>.zendesk.com`.
  2. Click the Zendesk Products icon, then select **Admin Center**.

![Zendesk Admin Center interface.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/admincenter.png)Zendesk Admin Center
  3. In the navigation menu, expand **Apps and integrations** and select **OAuth clients** from **APIs**.

  4. Click **Add OAuth client**.

  5. Enter the following client details:

     * **Name:** Enter a descriptive name for your application.
     * Optional: **Description:** Enter a short description.
     * Optional: **Company:** Enter your company name.
     * Optional: **Logo:** Provide a logo, which appears on the consent screen.
     * **Unique Identifier (Client ID):** Provide a unique name for your client. You can edit the initial suggestion, but it must be unique.
     * **Client kind:** Select **Public** for applications running in a browser or on a mobile device, or **Confidential** for applications running on secure servers.
     * **Redirect URLs (Required):** Enter `https://vertexaisearch.cloud.google.com/oauth-redirect`. This is the URL Zendesk redirects to after authorization, receiving the authorization code.
  6. Click **Save** to obtain the client secret.

     * **Client ID:** The value from the **Unique Identifier** field.
     * **Client secret:** A new **Secret** field appears. Copy this secret and save it immediately in a secure location. For security, the full secret is shown only once. If you lose it, you must regenerate it.
![Generated client secret displayed in the interface.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/secret.png)Generated client credentials
  7. Click **Save** again to finalize the changes.




### Set up permissions

To set up the required permissions, follow these steps:

  1. Navigate to your Zendesk instance and sign in with an administrator account.
  2. Click the Zendesk Products icon, then select **Admin Center**.
  3. In the navigation menu, expand **Apps and integrations** and select **OAuth Clients** from **Connections**.
  4. Click **Add client**.
  5. Enter the following client details:

     * **Name** : Enter a descriptive name. This cannot be changed.
     * **OAuth grant type** : Select **Authorization code**.
     * **Client ID** : Enter the client ID obtained from the Create an OAuth client in Zendesk section.
     * **Client Secret** : Enter the client secret value obtained from the Create an OAuth client in Zendesk section.
     * **Authorize URL** : The authorization endpoint is typically in the format `https://<var>your-subdomain</var>.zendesk.com/oauth/authorize`. Replace `<var>your-subdomain</var>` with your actual Zendesk subdomain.
     * **Token URL** : The token endpoint is typically in the format `https://<var>your-subdomain</var>.zendesk.com/oauth/token`. Replace `<var>your-subdomain</var>` with your actual Zendesk subdomain. ![Fields for entering API scopes in the Zendesk Admin Center.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/scopes.png)Add scopes
     * **Scopes** : Enter the following scopes separated by spaces, based on your connection mode:
Connection mode | Scope | Purpose  
---|---|---  
**Federated search** | `read`, `users:read` | Required to perform searching across Zendesk data.  
**Federated search and actions** | `tickets:write` | Required to perform search, create, update, and merge tickets.  
`hc:write` | Required to create category and update post.  
**Note:** Before you configure these details, ensure that token access is enabled in Zendesk.
  6. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
