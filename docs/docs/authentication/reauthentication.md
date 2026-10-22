---
url: https://docs.cloud.google.com/docs/authentication/reauthentication/
title: Reauthentication \u00a0|\u00a0 Authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:19.972497+00:00
---

# Reauthentication  |  Authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/authentication/reauthentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Authentication ](https://docs.cloud.google.com/docs/authentication)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Reauthentication Stay organized with collections  Save and categorize content based on your preferences. 

This page describes some scenarios when you might need to authenticate again, even if you previously authenticated successfully. 

## Google Workspace session configuration

If you are accessing Google Cloud by using a Google Workspace user account, your Google Workspace administrator can configure the maximum session length, and whether reauthentication is required when the session expires. The credentials provided by local Application Default Credentials (ADC) files also expire when the session expires. You must refresh them by running the [`gcloud auth application-default login` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login) again.

If you have questions about your Google Workspace session configuration, contact your Google Workspace administrator. For information about setting the Google Workspace session length, see [Set session length for Google Cloud services](https://support.google.com/a/answer/9368756).

## Identity-Aware Proxy reauthentication

IAP can be configured to require reauthentication to protected services and applications after a specific period of time. For more information, see [IAP reauthentication](https://docs.cloud.google.com/iap/docs/configuring-reauth).

## Refresh token expiration

Refresh tokens can expire due to session length, or for other reasons. When they expire, you must authenticate again. For more information, see [Refresh token expiration](https://developers.google.com/identity/protocols/oauth2#expiration) in the Google Identity documentation.

## Sensitive actions

The following Google Cloud actions are considered sensitive actions:

  * Billing assignment changes

  * IAM allow policy changes at the organization, folder, or project level




Users who can perform sensitive actions are known as _privileged users_. To help protect against bad actors impersonating privileged users through cookie theft, Google Cloud requires reauthentication before sensitive actions can be performed.

Reauthentication for sensitive actions is in the process of rolling out across Google Cloud accounts. The rollout is expected to be complete in 2026.

### When reauthentication is required

When you initiate a sensitive action, you are required to reenter your password or complete multi-factor authentication (MFA) if all of the following conditions are met:

  * The action is initiated in the Google Cloud console.
  * You have not reauthenticated in the last 15 minutes.
  * Your user account is managed by Google.



User accounts managed by an external identity provider (IdP) and federated by using Workforce Identity Federation are not required to reauthenticate.

## Disable reauthentication

Reauthenticating for sensitive actions is enabled by default. To apply for an exception, [contact support](https://console.cloud.google.com/support) with your reason for the exception. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
