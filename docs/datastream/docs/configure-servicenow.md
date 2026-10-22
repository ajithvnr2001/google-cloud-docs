---
url: https://docs.cloud.google.com/datastream/docs/configure-servicenow/
title: Configure a ServiceNow instance for CDC \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:36.053965+00:00
---

# Configure a ServiceNow instance for CDC  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-servicenow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure a ServiceNow instance for CDC Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use Datastream to replicate data from a ServiceNow instance to a [supported destination](https://docs.cloud.google.com/datastream/docs/destinations), such as BigQuery or Cloud Storage. Before creating a connection profile, you set up a dedicated integration user, configure basic or OAuth 2.0 authentication, and allowlist Datastream IP addresses if needed.

## Before you begin

Before you start configuring ServiceNow for use with Datastream, ensure that you have:

  * An active ServiceNow instance, for example, `company.service-now.com`.
  * Administrator privileges on the ServiceNow instance to create users, assign roles, and manage the OAuth Application Registry.
  * Knowledge of your ServiceNow instance version.



## Configure an integration user

In ServiceNow, you can either create a new user or adjust the settings for an existing account to allow Datastream access. For security and auditing purposes, we highly recommend that you create a dedicated integration user.

  1. In ServiceNow, navigate to **User Administration > Users**.
  2. To create a new user, click **New**. To edit an existing user, search for the **User ID** in the user list and click it to open the record.
  3. Configure user details:

     * Enter a unique name in the **User ID** field, for example, `datastream_integration`. You set the user identifier only for new users.
     * If you select OAuth authentication for the connector, we recommend that you enter values in the **First name** and **Last name** fields to better identify the user record.
     * **Identity configuration** : based on your ServiceNow platform version:

       * **Xanadu and later** : select **Machine** in the **Identity type** drop-down. This automatically enables **Web service access only**.
       * **Pre-Xanadu** : select the **Web service access only** checkbox.
  4. Save the record:

     * For new users, click **Submit**.
     * For existing users, click **Update**.
  5. If you created a new user, reopen the record. Find the user in the list and click their **User ID** to access the record options.

  6. Set password:

     1. Click **Set Password** in the form header.
     2. Enter a strong password and click **Save Password**.
     3. If you use basic authentication for the connector, take note of the password because it's required when configuring the connection profile.
  7. Assign permissions. You must grant the integration user read access to all tables that you want to replicate. Additionally, the connector requires explicit read permissions for the `sys_db_object`, `sys_table_rotation` and `sys_dictionary` system metadata tables.


Because of the granular nature of the ServiceNow roles and [Access Control List (ACL)](https://www.servicenow.com/docs/r/platform-security/access-control/access-control-rules.html) system, the specific configuration required to grant these permissions is customer-specific. 

  * We highly recommend assigning the **snc_read_only** role to your user, because it ensures the user session is strictly limited to read-only access across the entire platform.
  * The **admin** role grants comprehensive access to all tables in the instance. If your security policies permit, assigning the **admin** role is the simplest method for ensuring full connector access.



## Optional: Configure OAuth 2.0 client credentials

OAuth 2.0 is the most secure and recommended authentication method for using the ServiceNow connector with Datastream. It uses a **Client ID** and **Client secret** instead of a permanent password.

  1. Activate the OAuth 2.0 plugin for your instance. For more information, see the [ServiceNow documentation](https://www.servicenow.com/docs/r/platform-security/authentication/t_ActivateOAuth.html).
  2. Make sure that the `com.snc.platform.security.oauth.is.active` system property is set to `true`. For more information, see the [ServiceNow documentation](https://www.servicenow.com/docs/r/platform-security/authentication/t_SetTheOAuthProperty.html).
  3. Make sure that the `glide.oauth.inbound.client.credential.grant_type.enabled` system property is set to `true`. For more information, see the [ServiceNow documentation](https://www.servicenow.com/docs/r/platform-security/authentication/create-cc-sys-prop.html).
  4. Set up inbound OAuth configuration. Depending on your instance security requirements, you can select one of the following OAuth configuration scopes:

     * Broadly scoped: when using broadly scoped OAuth, the token bearer inherits the associated user roles and access control lists (ACLs).
     * [Granular REST API auth scoped](https://www.servicenow.com/docs/r/platform-security/authentication/rest-api-auth-scope.html): this type of OAuth configuration restricts to specific REST APIs and methods permitted by the scope in addition to associated user roles and ACLs.
  5. Create the OAuth integration record. For more information, see the ServiceNow documentation:

     * [For Zurich platform version and later](https://www.servicenow.com/docs/r/platform-security/authentication/configure-an-oauth-client-credential-grant.html)
     * [For pre-Zurich platform versions](https://www.servicenow.com/docs/r/platform-security/authentication/add-oauth-application-user.html)
  6. After you create the OAuth integration record, the configuration depends on the platform version and OAuth scope:

     * **Broadly scoped configuration** :

       * _Zurich and later:_ in the **Auth scope** section for your integration record, make sure that there aren't any entries in the **Auth scope** or **Limit authorization to the following APIs** fields, and that the **Allow access only to APIs in selected scope** checkbox isn't selected.
       * _Pre-Zurich:_ in the **Scope restriction** drop-down, select **Broadly scoped** and leave the **Auth scopes** list empty.
     * **Granular REST API Auth scoped configuration** : optionally, use auth scopes to further limit the token bearer to specific REST APIs and methods permitted by the scope. The Datastream connector only requires `GET` access to the Table API. Depending on the platform version, perform the following steps:

       * _Zurich and later_ : in the **Auth scope** section for your integration record, select an authorization scope and limit its access to the Table API.

**Note:** If you create the authorization scope when editing your integration record, the scope has access to all API methods of the Table API by default. To further limit access to the `GET` method only, you must manually edit the newly created record by navigating to **System Web Services > API Auth Scopes > REST API Auth Scope**.
       * _Pre-Zurich_ :

         1. Restrict access to the Table API for the selected authorization scope. For more information, see the [ServiceNow documentation](https://www.servicenow.com/docs/r/yokohama/platform-security/authentication/configure-rest-api-auth-scope.html).
         2. Add the scope under the **Auth Scopes** section.
         3. Select **Securely scoped** in the **Scope Restriction** box.



## Optional: Configure IP address access control

If your ServiceNow instance uses [IP Address Access Control](https://www.servicenow.com/docs/r/platform-security/authentication/t_AccessControl.html), you must explicitly allowlist [Datastream IP addresses](https://docs.cloud.google.com/datastream/docs/ip-allowlists-and-regions).

The following steps are only required if you have an IP address access control `DENY` rule that covers Datastream IP addresses. By default, there are no IP restrictions on access to the instance.

  1. In ServiceNow, navigate to **System Security > IP Address Access Control**.
  2. Click **New**.
  3. In the record creation form, apply the following settings: 
     1. In the **Type** drop-down, select **Allow**.
     2. In the **Direction** drop-down, select **Inbound**.
     3. In the **Range start** and **Range end** fields, enter the specific IP address or range of addresses from the list of [Datastream IP addresses](https://docs.cloud.google.com/datastream/docs/ip-allowlists-and-regions).
     4. Make sure that the **Active** checkbox is selected.
  4. Click **Submit**.
  5. Repeat the previous steps for every IP address in the list of Datastream addresses.



## What's next

  * Learn more about the [ServiceNow source](https://docs.cloud.google.com/datastream/docs/sources-servicenow).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
