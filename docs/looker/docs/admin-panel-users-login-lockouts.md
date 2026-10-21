---
url: https://docs.cloud.google.com/looker/docs/admin-panel-users-login-lockouts/
title: Admin settings - Login lockouts \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:46:39.801103+00:00
---

# Admin settings - Login lockouts  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-users-login-lockouts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Login lockouts Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

Looker automatically locks out user accounts for five minutes after someone has tried to log in to an account and failed to enter the proper credentials four times in a row from a single IP address. If an account is locked, that account is not allowed to login from that same IP address, even with the proper credentials, until the five-minute lockout period expires. Lockouts occur on a per-user credential and per-IP address basis, so a user credential that is locked out on an IP address can still attempt to log in from a different IP address, or a different user credential can attempt to log in from that same IP address.

> The lockout policy does not apply to [signed embed](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding) users.

The **Login Lockouts** page in the **Users** section of the **Admin** menu shows a list of user credentials that are currently locked out because their owners exceeded the maximum number of failed login attempts.

## Included information

Column | Definition  
---|---  
User ID | The user ID associated with the locked account. If there is not an account associated with the credentials used for the unsuccessful login attempts, this column is empty.  
Name | The name associated with the locked account. If there is not an account associated with the credentials used for the unsuccessful login attempts, this column shows "No matching account."  
Email | The email address used with the unsuccessful login attempts.  
Time Remaining | The amount of time left before the account unlocks.  
Authentication Type | The authentication method through which the unsuccessful login attempts were made. Possible options are:

  * `email`: Invalid email address and password combination
  * `api`: Invalid Looker API credentials
  * `totp`: Invalid two-factor authentication codes
  * `ldap`: Invalid LDAP credentials

  
IP Address | The IP address from which the unsuccessful logins were attempted.  
Actions | Shows the **Unlock** button, which lets you unlock the user account.  
  
## Unlocking an account

Looker admins can unlock an account that is currently locked, letting that user attempt to log in again before the five-minute lockout period expires. Click the **Unlock** button next to the user account that you want to unlock. Looker will display a confirmation dialog box. Click **Unlock** on the dialog box to unlock the user account.

If there is a user account associated with the credentials used for the login attempts, the dialog box includes a link to that user account page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
