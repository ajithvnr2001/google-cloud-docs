---
url: https://docs.cloud.google.com/looker/docs/alternate-login/
title: Enabling the alternate login option \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:02.398491+00:00
---

# Enabling the alternate login option  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/alternate-login/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Enabling the alternate login option Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Alternate login is not available for [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview). By default, the backup authentication method for Looker (Google Cloud core) is [OAuth](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication#using_oauth_as_a_backup_authentication_method).

Looker can authenticate users using one of several authentication server types, such as [Google OAuth](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-google), [LDAP](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-ldap), [SAML](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml), or [OpenID Connect](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-openid-connect). Enabling any of these authentication methods will disable other authentication systems, such as email and password.

Looker admins can give a user an alternate login option that uses their email address if the user has either an Admin [role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) or the [`login_special_email` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#login_special_email).

## Enabling alternate login on the Looker instance

Before you can enable the alternate login option for a user, you need to configure the Looker instance to accept email credentials by followin these steps:

  1. Navigate to the **Authentication** section of the **Admin** panel, and select the enabled authentication type, [Google OAuth](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-google), [LDAP](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-ldap), [SAML](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml), or [OpenID Connect](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-openid-connect).
  2. In the **Migration Options** section, enable the **Alternate login for admins and specified users** toggle.



## Granting the user permission to use alternate login

Only users with the Admin role or the [`login_special_email` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#login_special_email) may use alternate login. One way to grant the `login_special_email` permission to a non-admin user is to create a new role that contains that permission and then assign that role to the user, as follows:

  1. Navigate to the **Roles** page, located under the **Users** section in the **Admin** panel.
  2. Click the **New Permission Set** button.
  3. Enter a name for the new permission set, for example, **Alternate Login**.
  4. Select the box labeled **login_special_email**.
  5. Click **New Permission Set**.
  6. Click **New Role**.
  7. Enter a name for the new role, such as **Alternate Login Role**.
  8. In the **Permission Set** list, select your new permission set from the list.
  9. In the **Model Set** list, select **All**.
  10. In the **Users** list, select the user who is to be granted the alternate login permission.
  11. Click the **New Role** button to save the new role.
  12. Click **Confirm**.



## Creating email credentials for the user

Once the user has been granted permission to use email credentials, the next step is to create the credentials. To create email credentials, a Looker admin can either use the [Looker API](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest) to make a `POST` request or use the [Looker API SDK](https://github.com/looker-open-source/sdk-codegen/tree/main/examples) in the programming language of the admin's choice.

### Making a POST request to the Looker API

Because of its manual nature, this is a better method to use when you have only a limited number of users for whom you want to set up the alternate login option.

This example uses a `curl` command to make a `POST` request to the `create_user_credentials_email` API endpoint using a temporary access token:

  1. To generate the temporary token (`ACCESS_TOKEN`), follow the **Authentication without an SDK** instructions on the [Looker API authentication](https://docs.cloud.google.com/looker/docs/api-auth#authentication_without_a_sdk) documentation page.
  2. Using this temporary token in the authorization header, send a `POST` request to the Looker API using the user's `user_id`, and include their email in the body of the request.
         
         curl -H "Authorization: token ACCESS_TOKEN" -H 'Content-Type: application/json' -X POST -d '{ "email": "example_name@example_email.com" }' https://<instance_name<.api.looker.com/api/4.0/users/{user_id}/credentials_email
         

  3. On the **Users** page in the **Admin** panel, find the user account and click **Edit**.

  4. Click the **Send reset link** button. This will send an email to the email address you specified in your `POST` request.




To use the alternate login method, when the user logs in to Looker they will need to click the **Alternate Login** link and then enter their name and email address. They can still authenticate using their OAuth, LDAP, SAML, or OpenID Connect credentials through the **Authenticate** button.

### Using the Looker API SDK

Rather than going through the manual steps of making requests directly to the Looker API, you can instead use a Looker-provided SDK to interact with the API in a programming language of your choice. After you have imported the Looker API SDK and established a client connection, follow these steps:

  1. Use the `create_user_credentials_email(user_id, body)` function, inserting the `user_id` and `body` as specified in the [Looker API documentation](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/User/create_user_credentials_email). You can follow a similar example from this Looker Community post about [automatically provisioning users with the Looker API](https://www.googlecloudcommunity.com/gc/Developing-Applications/Automatically-Provisioning-Users-with-the-Looker-API/td-p/577037).
  2. Once the user accounts have been updated using the SDK method, on the **Users** page in the **Admin** panel, find the user account and click **Edit**.
  3. Click the **Send reset link** button. This will send an email to the email address you specified in your `POST` request.



To use the alternate login method, when the user logs in to Looker, they will need to click the **Alternate Login** link and then enter their name and email address. They can still authenticate using their OAuth, LDAP, SAML, or OpenID Connect credentials through the **Authenticate** button.

## Disabling alternate login on the Looker instance

**Warning:** Looker Support recommends against disabling the alternate login option entirely. It serves as a fallback method to avoid complete lockout from the Looker instance if the primary IdP connection encounters issues.

To disable the alternate login option, follow these steps:

  1. Navigate to the **Authentication** section of the **Admin** panel, and select the enabled authentication type: [Google OAuth](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-google), [LDAP](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-ldap), [SAML](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml), or [OpenID Connect](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-openid-connect).
  2. In the **Migration Options** section, disable the **Alternate login for admins and specified users** toggle.

**Note:** Disabling alternate login globally does not automatically delete existing email credentials from user accounts. If unauthorized login attempts target existing user email credentials, Looker continues to send automated failed login attempt notification emails. To stop these emails and completely remove email credentials, administrators must delete the email credentials from affected user accounts using the [`DELETE /users/{user_id}/credentials_email`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/User/delete_user_credentials_email) endpoint in the Looker API. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
