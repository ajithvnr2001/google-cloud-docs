---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/saml-provider/
title: Configure SAML providers to authenticate to clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:47.495008+00:00
---

# Configure SAML providers to authenticate to clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/saml-provider/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Configure SAML providers to authenticate to clusters Stay organized with collections  Save and categorize content based on your preferences. 

This document is for **platform administrators** , or whoever manages identity setup in your organization. It explains how to configure your chosen [Security Assertion Markup Language (SAML)](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html) identity provider for authentication to Kubernetes clusters that aren't on Google Cloud.

## Register a client application with your provider

During the authentication flow, the cluster uses the following information to verify and redirect users:

  * `EntityID` \- This is a unique identifier that represents the cluster authentication mechanism for the provider. This is derived from the URL of the API server. For example, if the APISERVER-URL is `https://cluster.company.com`, then the `EntityID` should be `https://cluster.company.com:11001`. Note that the URL has no trailing slashes.
  * `AssertionConsumerServiceURL` \- This is the callback URL. The response is forwarded to this URL after the provider authenticates the user. For example, if the APISERVER-URL is `https://cluster.company.com`, then the `AssertionConsumerServiceURL` should be `https://cluster.company.com:11001/saml-callback`.



## Provider setup information

This section provides steps for registering a client application with Microsoft Entra ID. If you use a different identity provider, see the provider's documentation to set up a client application.

  1. If you haven't done so already, [Set up a Microsoft Entra tenant](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-create-new-tenant).
  2. [Register an application in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app).
  3. In the Microsoft Entra admin center, open the **App registrations** page and select your application. The application overview page opens.
  4. In the navigation menu, click **Authentication**.
  5. In the **Platform configurations** section, select **Enterprise Applications**.
  6. In the **Set up Single Sign-On with SAML** , edit the **Basic SAML Configuration**.
  7. In the **Identifier (Entity ID)** section, select **Add Identifier**.
  8. Enter the _EntityID_ and _Reply URL_ that you derived from Register a client application with your provider
  9. Click **Save** to save these settings.
  10. Review the **Attributes & Claims** section to add any new attributes.
  11. In the **SAML Certificates** section, click **Certificate (Base64)** to download the identity provider certificate.
  12. In the **Set up app** section, copy the **Login URL** and **Azure AD identifier**.



### Set SAML assertion lifespan

For enhanced security, configure your SAML provider to issue assertions with a short lifespan, such as 10 minutes. This setting is configurable within your SAML provider's settings.

Setting the lifespan to less than 5 minutes might cause login issues if the clocks between the cluster and your SAML provider aren't synchronized.

## Share provider details

Share the following provider information with your cluster administrator for cluster setup:

  * `idpEntityID` \- This the unique identifier for the identity provider. It corresponds to the URL of the provider and is also called _Azure AD identifier_.
  * `idpSingleSignOnURL` \- This is the endpoint to which the user is redirected for sign up. This is also called the _Login URL_.
  * `idpCertificateDataList`\- This is the public certificate used by the identity provider for SAML assertion verification.



## What's next

  * [Configure authentication for individual clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/per-cluster)
  * [Configure authentication for your fleet](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
