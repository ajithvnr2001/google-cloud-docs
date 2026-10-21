---
url: https://docs.cloud.google.com/iam/docs/workforce-oauth-app/
title: OAuth application integration overview \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:09:59.747867+00:00
---

# OAuth application integration overview  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/workforce-oauth-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  OAuth application integration overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of OAuth application integration in Google Cloud.

You can use OAuth application integration to integrate your OAuth-based applications with Google Cloud. Federated users can use their identity provider (IdP) to sign in to the applications and access their Google Cloud products and data. OAuth application integration is a feature of Workforce Identity Federation.

To use OAuth application integration, you must first create a workforce identity pool and provider. You can then register the OAuth-based application using OAuth 2.0. Applications must be registered in the organization where your workforce identity pool and provider are configured.

**Important:** OAuth application integration works only with Identity-Aware Proxy.

**Note:** OAuth application integration and the `projects.locations.oauthClients` API are only for [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). To create and manage standard OAuth 2.0 client IDs for Google Cloud users or services, go to the Google Cloud console, then go to [**APIs & Services >Credentials**](https://console.cloud.google.com/apis/credentials).

## OAuth application registration

To configure an application to access Google Cloud, you [register](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app#create) the application with Google Cloud by creating [OAuth client credentials](https://tools.ietf.org/html/rfc6749#section-4.4). The credential contains a client secret. The application uses the access token to access the Google Cloud products and data.

## OAuth client and credential security risks and mitigations

You must secure access to the IAM APIs and the client ID and secret. If the client ID and secret is leaked, security issues can result. These issues include the following:

  * Impersonation: A malicious user with your client ID and secret can create an application that masquerades as your legitimate application. They can then do the following:

    * Gain unauthorized access to the user data and permissions that your application is entitled to.
    * Perform actions on the user's behalf, such as posting content, making API calls, or modifying user settings.
    * Perform phishing attacks, wherein the malicious user creates a fake login page that resembles the OAuth provider. The page can then trick users into entering their credentials, which gives the credentials to the malicious user who can then access their accounts.
  * Reputational damage: A security breach can harm the reputation of your application and organization, causing users to lose trust.




In the event of a breach, to mitigate these and other risks, assess the nature of the breach and do the following:

  * Ensure that only trusted users have IAM access to the [OAuth client and credential API](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app).

  * Rotate the client secret immediately, by rotating the client credential, as follows:

    1. [Create a new client credential](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app#create-credential) for the OAuth client.
    2. [Disable the old client credential](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app#disable-credential).
    3. [Delete the old client credential](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app#delete-credential).



# What's next

  * Learn how to [Manage OAuth applications](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
