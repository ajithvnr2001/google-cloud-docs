---
url: https://docs.cloud.google.com/iap/docs/enable-external-identities/
title: Enabling external identities \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:56.220629+00:00
---

# Enabling external identities  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/enable-external-identities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Enabling external identities Stay organized with collections  Save and categorize content based on your preferences. 

This article shows you how to configure Identity-Aware Proxy (IAP) to use external identities. By combining IAP and Identity Platform, you can authenticate users with a wide range of identity providers (such as OAuth, SAML, OIDC, and more), instead of just Google accounts.

## Enabling and configuring Identity Platform

IAP uses Identity Platform to authenticate external identities. See the [Quickstart for Identity Platform](https://docs.cloud.google.com/identity-platform/docs/quickstart-cicp) to learn how to enable it.

If you want to utilize multiple tenants, you'll also need to follow the steps in [Getting started with multi-tenancy](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-quickstart). If you don't need to isolate resources, you can skip this step and configure all your providers at the project level. Consult the [overview on external identities](https://docs.cloud.google.com/iap/docs/external-identities) if you're unsure if you should turn on multi-tenancy.

Finally, you'll need to enable providers. The [quickstart](https://docs.cloud.google.com/identity-platform/docs/quickstart-cicp) shows how to use simple username and password authentication, but Identity Platform supports a wide range of provider types, including:

  * Email and password
  * OAuth (such as Google, Facebook, Twitter, and more)
  * SAML
  * OIDC
  * Phone number
  * Anonymous



See the rest of the [Identity Platform documentation](https://docs.cloud.google.com/identity-platform/docs) to learn how to configure other providers. Note that phone number and anonymous authentication are not supported for use with multi-tenancy. Passwordless sign-in using an email link is not supported with IAP.

## Enabling IAP to use external identities

Once you've set up Identity Platform, you can configure IAP to use it for authentication.

  1. Open the IAP page in the Google Cloud console.  
[ Open the IAP page](https://console.cloud.google.com/security/iap)

  2. Select the same project that you configured Identity Platform with. Using different projects is not supported.

  3. Select the **Applications** tab.

  4. Locate the service you want to restrict access to by using IAP.

  5. Toggle the switch in the IAP column to **On**.

  6. In the side panel, click **Start** in the box labeled **Use external identities for authorization**.

  7. Confirm your selection.

  8. In the Identity Platform side panel:

     1. Choose whether to build your own sign-in page, or have IAP create one for you.

Letting IAP create the sign-in page is the fastest way to get started. You don't need to deploy additional services or write any new code, and can specify minor customizations using JSON. See [Hosting an authentication UI on Cloud Run](https://docs.cloud.google.com/iap/docs/cloud-run-sign-in) to learn more.

**Domain restricted sharing:** If the project is subject to the [domain restricted sharing constraint in an organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains), you will be unable to create public services by default. You can use [tags](https://docs.cloud.google.com/run/docs/configuring/tags) and a conditional policy to exempt specific services from this constraint. For more information, see the blog post about [creating public Cloud Run services](https://cloud.google.com/blog/topics/developers-practitioners/how-create-public-cloud-run-services-when-domain-restricted-sharing-enforced) when domain restricted sharing is enforced.

Building your own page is more complex, but gives you full control of the authentication flow and experience. See [Creating an authentication UI with FirebaseUI](https://docs.cloud.google.com/iap/docs/using-firebaseui) and [Creating a custom authentication UI](https://docs.cloud.google.com/iap/docs/create-custom-auth-ui) for more information.

     2. If you chose to build your own UI, enter an **Authentication URL**. IAP will redirect unauthenticated requests it receives to this URL.

Including your API key in the URL is optional. If you don't provide a key, the Google Cloud console will append your default key automatically.

     3. Select whether to use **project providers** or **tenants**.

     4. Check the boxes of the providers or tenants to enable. Select **Configure providers** if you need to modify your providers or tenants.

  9. Click **Save**.




Congratulations! IAP is configured to authenticate users with external identities.

## Switching back to Google identities

You cannot use IAM for authorization when using external identities. If you want to switch back to Google identities so you can leverage IAM, follow these steps:

  1. Return to the IAP page in the Google Cloud console.  
[ Open the IAP page](https://console.cloud.google.com/security/iap)

  2. Select the resource configured to use IAP.

  3. Open the Identity Platform information panel.

  4. Select **Use IAM to manage this resource**.




Note that switching back to Google identities will clear your authentication URL and associated project and tenants.

## What's next

  * [Host a sign-in page on Cloud Run](https://docs.cloud.google.com/iap/docs/cloud-run-sign-in).
  * [Create a sign-in page with FirebaseUI](https://docs.cloud.google.com/iap/docs/using-firebaseui).
  * [Create a custom sign-in page](https://docs.cloud.google.com/iap/docs/create-custom-auth-ui).
  * Gain a deeper understanding of how [external identities work with IAP](https://docs.cloud.google.com/iap/docs/external-identities).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
