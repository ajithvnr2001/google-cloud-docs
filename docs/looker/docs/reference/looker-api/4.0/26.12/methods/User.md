---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/
title: User Methods v4.0.26.12 \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:04.310343+00:00
---

# User Methods v4.0.26.12  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  User Methods v4.0.26.12 Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.12 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

  * [Search CredentialsEmail](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/search_credentials_email)
  * [Get Current User](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/me)
  * [Get All Users](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/all_users)
  * [Create User](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/create_user)
  * [Search Users](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/search_users)
  * [Search User Names](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/search_users_names)
  * [Get User by Id](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/user)
  * [Update User](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/update_user)
  * [Delete User](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/delete_user)
  * [Get User by Credential Id](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/user_for_credential)
  * [Delete Service Account](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/delete_service_account)
  * [Update Service Account](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/update_service_account)
  * [Get Email/Password Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/user_credentials_email)
  * [Create Email/Password Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/create_user_credentials_email)
  * [Update Email/Password Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/update_user_credentials_email)
  * [Delete Email/Password Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/delete_user_credentials_email)
  * [Get Two-Factor Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/user_credentials_totp)
  * [Create Two-Factor Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/create_user_credentials_totp)
  * [Delete Two-Factor Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/delete_user_credentials_totp)
  * [Get LDAP Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/user_credentials_ldap)
  * [Delete LDAP Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/delete_user_credentials_ldap)
  * [Get Google Auth Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/user_credentials_google)
  * [Delete Google Auth Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/delete_user_credentials_google)
  * [Get Saml Auth Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/user_credentials_saml)
  * [Delete Saml Auth Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/delete_user_credentials_saml)
  * [Get OIDC Auth Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/user_credentials_oidc)
  * [Delete OIDC Auth Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/delete_user_credentials_oidc)
  * [Get API Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/user_credentials_api3)
  * [Update API Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/update_user_credentials_api3)
  * [Delete API Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/delete_user_credentials_api3)
  * [Get All API Credentials](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/all_user_credentials_api3s)
  * [Create API Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/create_user_credentials_api3)
  * [Get Embedding Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/user_credentials_embed)
  * [Delete Embedding Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/delete_user_credentials_embed)
  * [Get All Embedding Credentials](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/all_user_credentials_embeds)
  * [Get Looker OpenId Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/user_credentials_looker_openid)
  * [Delete Looker OpenId Credential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/delete_user_credentials_looker_openid)
  * [Get Web Login Session](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/user_session)
  * [Delete Web Login Session](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/delete_user_session)
  * [Get All Web Login Sessions](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/all_user_sessions)
  * [Create Password Reset Token](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/create_user_credentials_email_password_reset)
  * [Get User Roles](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/user_roles)
  * [Set User Roles](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/set_user_roles)
  * [Get User Attribute Values](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/user_attribute_user_values)
  * [Set User Attribute User Value](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/set_user_attribute_user_value)
  * [Delete User Attribute User Value](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/delete_user_attribute_user_value)
  * [Send Password Reset Token](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/send_user_credentials_email_password_reset)
  * [Wipeout User Emails](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/wipeout_user_emails)
  * [Create an embed user from an external user ID](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/create_embed_user)
  * [Create Service Account](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/create_service_account)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
