---
url: https://docs.cloud.google.com/looker/docs/best-practices/troubleshooting-failed-login-attempt-emails/
title: Troubleshooting excessive failed login attempt emails \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:34.680338+00:00
---

# Troubleshooting excessive failed login attempt emails  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/troubleshooting-failed-login-attempt-emails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Troubleshooting excessive failed login attempt emails Stay organized with collections  Save and categorize content based on your preferences. 

If you or your users experience an uptick in automated "Failed Looker login attempt" emails, this page describes the issue and how to resolve it.

## The issue

Automated failed login emails are triggered when someone enters an incorrect password for a valid user's email address on the public Looker login page. These alerts are intended to notify users of unauthorized activity on their accounts.

When an organization authenticates users with a third-party Identity Provider (IdP) such as SAML, LDAP, or Google OAuth, and disables the **Alternate login for admins and specified users** toggle on the instance, it may still receive "Failed Looker login attempt" emails. This situation occurs when bots bypass the UI and send direct `POST` requests to the Looker alternate login endpoint.

This scenario can lead to security concerns for users who believe that their accounts have been compromised; however, this notification behavior is by design and doesn't mean that an account has been compromised.

## Solution

If you haven't enabled [two-factor authentication (2FA)](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-two-factor) on your Looker instance, we strongly recommend that you enable 2FA.

Upgrade the instance to Looker 26.6.17 or later. This release introduces a patch that returns a 404 error on the targeted backdoor endpoint whenever the alternate login option is disabled. Once you've upgraded your Looker instance, contact [Looker Support](https://console.cloud.google.com/support/) to enable the corresponding backend feature flag to activate this behavior. The bot requests will be quietly dropped rather than processed by the authentication system, permanently stopping the automated alert spam.

Alternatively, configure a global [IP allowlist](https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist) to restrict access strictly to known corporate network or VPN IP ranges.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
