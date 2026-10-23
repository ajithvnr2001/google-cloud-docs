---
url: https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation/
title: Configure Workforce Identity Federation \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:54.381644+00:00
---

# Configure Workforce Identity Federation  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Configure Workforce Identity Federation Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to configure Workforce Identity Federation with an identity provider (IdP) that supports [OIDC](https://openid.net/connect/) or [SAML 2.0](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html).

For IdP-specific instructions, see the following:

  * [Configure Microsoft Entra ID-based Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id)
  * [Configure Okta-based Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta)



## Before you begin

  1. Make sure that you have a Google Cloud organization set up.
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. Enable the Identity and Access Management (IAM) and Resource Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,cloudresourcemanager.googleapis.com&redirect=https%3A//console.cloud.google.com)

  4. For sign-in, your IdP must provide signed authentication information: OIDC IdPs must provide a JWT, and SAML IdP responses must be signed. 
  5. To receive important information about changes to your organization or Google Cloud products, you must provide [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts). For more information, see the [Workforce Identity Federation overview](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#essential-contacts).



## Costs

Workforce Identity Federation is available as a no-cost feature. However, Workforce Identity Federation detailed audit logging uses Cloud Logging. To learn about Logging pricing, see [Google Cloud Observability pricing](https://docs.cloud.google.com/stackdriver/pricing#logs-costs). 

## Required roles

To get the permissions that you need to configure Workforce Identity Federation, ask your administrator to grant you the [Workforce Identity Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workforcePoolAdmin) (`roles/iam.workforcePoolAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Alternatively, the Owner basic role (`roles/owner`) also includes permissions to configure Workforce Identity Federation. You should not grant basic roles in a production environment, but you can grant them in a development or test environment. 

## Configure Workforce Identity Federation

To configure Workforce Identity Federation, you create a [workforce identity pool](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-identity-pools) and a [workforce identity pool provider](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-identity-pool-providers).

### Create a workforce identity pool

To create the pool, execute the following command:

###  gcloud 

To create the workforce identity pool, run the following command:
    
    
    gcloud iam workforce-pools create WORKFORCE_POOL_ID \
        --organization=ORGANIZATION_ID \
        --display-name="DISPLAY_NAME" \
        --description="DESCRIPTION" \
        --session-duration=SESSION_DURATION \
        --location=global
    

Replace the following:

  * `WORKFORCE_POOL_ID`: an ID that you choose to represent your Google Cloud workforce pool. The pool ID must be globally unique across all workforce identity pools in Google Cloud. For information on formatting the ID, see the [Query parameters](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/create#query-parameters) section in the API documentation.
  * `ORGANIZATION_ID`: the numeric organization ID of your Google Cloud organization for the workforce identity pool. Workforce identity pools are available across all projects and folders in the organization.
  * `DISPLAY_NAME`: Optional. A display name for your workforce identity pool.
  * `DESCRIPTION`: Optional. A workforce identity pool description.
  * `SESSION_DURATION`: Optional. The session duration, expressed as a number appended with `s`—for example, `3600s`. Session duration determines how long the Google Cloud access tokens, [console (federated)](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#console-federated) sign-in sessions, and gcloud CLI sign-in sessions from this workforce pool are valid. Session duration defaults to one hour (3600s). The session duration value must be between 15 minutes (900s) and 12 hours (43200s).

**Tip:** Run `gcloud iam workforce-pools create --help` to find other parameters you can customize for this command.

###  Console 

To create the workforce identity pool, do the following:

  1. In the Google Cloud console, go to the **Workforce Identity Pools** page:

[Go to Workforce Identity Pools](https://console.cloud.google.com/iam-admin/workforce-identity-pools?supportedpurview=organizationId)

  2. Select the organization for your workforce identity pool. Workforce identity pools are available across all projects and folders in an organization.

  3. Click **Create pool** and do the following:

     1. In the **Name** field, enter the display name of the pool. The pool ID is automatically derived from the name as you type, and it is displayed under the **Name** field. You can update the pool ID by clicking **Edit** next to the pool ID.

     2. Optional: In **Description** , enter a description of the pool.

     3. To create the workforce identity pool, click **Next**.




The workforce identity pool's session duration defaults to one hour (3600s). The session duration determines how long the Google Cloud access tokens, [console (federated)](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#console-federated), and gcloud CLI sign-in sessions from this workforce pool are valid. After you create the pool, you can [update the pool](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#update-pool) to set a custom session duration. The session duration must be from 15 minutes (900s) to 12 hours (43200s).

### Create a workforce identity pool provider

This section describes how to create a [workforce identity pool provider](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-identity-pool-providers) to enable your IdP users to access Google Cloud. You can configure the provider to use either the OIDC or SAML protocol.

#### Create an OIDC workforce pool provider

To create a workforce identity pool provider using the OIDC protocol, do the following:

  1. In your OIDC IdP, register a new application for Google Cloud Workforce Identity Federation. Note the client ID and issuer URI provided by the IdP. You use them in this document.

  2. If you plan to set up user access to the console, add the following redirect URL to your OIDC IdP:
         
         https://auth.cloud.google/signin-callback/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID
         

Replace the following:

     * `WORKFORCE_POOL_ID`: the workforce identity pool ID

     * `WORKFORCE_PROVIDER_ID`: the ID of the workforce identity pool provider that you create later in this document.

To learn how to configure console (federated) sign-in, see [Set up user access to the console (federated)](https://docs.cloud.google.com/iam/docs/workforce-console-sso).

  3. In Google Cloud, to create the provider, do the following:

### gcloud

### Code flow

To create an OIDC provider that uses [authorization code flow](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#oidc-flow-types) for web sign-in, run the following command:
         
         gcloud iam workforce-pools providers create-oidc WORKFORCE_PROVIDER_ID \
             --workforce-pool=WORKFORCE_POOL_ID \
             --display-name="DISPLAY_NAME" \
             --description="DESCRIPTION" \
             --issuer-uri="ISSUER_URI" \
             --client-id="OIDC_CLIENT_ID" \  
             --client-secret-value="OIDC_CLIENT_SECRET" \
             --web-sso-response-type="code" \
             --web-sso-assertion-claims-behavior="merge-user-info-over-id-token-claims" \
             --web-sso-additional-scopes="WEB_SSO_ADDITIONAL_SCOPES" \
             --attribute-mapping="ATTRIBUTE_MAPPING" \
             --attribute-condition="ATTRIBUTE_CONDITION" \
             --jwk-json-path="JWK_JSON_PATH" \
             --detailed-audit-logging \
             --location=global
         

Replace the following: 

     * `WORKFORCE_PROVIDER_ID`: A unique workforce identity pool provider ID. The prefix `gcp-` is reserved and can't be used in a workforce identity pool or workforce identity pool provider ID.
     * `WORKFORCE_POOL_ID`: The workforce identity pool ID to connect your IdP to.
     * `DISPLAY_NAME`: An optional user-friendly display name for the provider; for example, `idp-eu-employees`.
     * `DESCRIPTION`: An optional workforce provider description; for example, `IdP for Partner Example Organization employees`. 
     * `ISSUER_URI`: The OIDC issuer URI, in a valid URI format, that starts with `https`; for example, `https://example.com/oidc`. Note: For security reasons, `ISSUER_URI` must use the HTTPS scheme.
     * `OIDC_CLIENT_ID`: The OIDC client ID that is registered with your OIDC IdP; the ID must match the `aud` claim of the JWT that is issued by your IdP.
     * `OIDC_CLIENT_SECRET`: The OIDC client secret.
     * `WEB_SSO_ADDITIONAL_SCOPES`: Optional additional scopes to send to the OIDC IdP for console (federated) or gcloud CLI browser-based sign-in.
     * `ATTRIBUTE_MAPPING`: An [attribute mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings). The following is an example of an attribute mapping: 
           
           google.subject=assertion.oid
           google.groups=assertion.groups,
           attribute.costcenter=assertion.costcenter

This example maps the IdP attributes `assertion.oid`, `assertion.groups`, and `assertion.costcenter` in the OIDC assertion to the Google Cloud attributes `google.subject`, `google.groups`, and `attribute.costcenter`, respectively. 
     * `ATTRIBUTE_CONDITION`: An [attribute condition](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions); for example, `assertion.role == 'gcp-users'`. This example condition ensures that only users with the role `gcp-users` can sign in using this provider. **Warning:** If your multi-tenant IdP has a single issuer URI, you must use [attribute conditions](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions) to ensure that access is restricted to the correct tenant. For more information, see [Use attribute conditions when federating with GitHub or other multi-tenant identity providers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#use-attribute-conditions-multitenant). 
     * `JWK_JSON_PATH`: An optional path to a [locally uploaded OIDC JWKs](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#json-web-keys). If this parameter isn't supplied, Google Cloud instead uses your IdP's `/.well-known/openid-configuration` path to source the JWKs containing the public keys. For more information about locally uploaded OIDC JWKs, see [manage OIDC JWKs](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#manage-oidc-keys). **Note:** Local OIDC JWKs can be uploaded through [implicit flow or code flow](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#oidc-flow-types), but can only be used in [programmatic flow](https://docs.cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials), in which you directly call the STS `/token` endpoint with a credential from the third-party IdP to exchange for a Google Cloud access token for your workforce pool. You can't use local OIDC JWKs when signing in to the console (federated). 
     * Workforce Identity Federation _detailed audit logging_ logs information received from your IdP to Logging. Detailed audit logging can help you troubleshoot your workforce identity pool provider configuration. To learn how to troubleshoot attribute mapping errors with detailed audit logging, see [General attribute mapping errors](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#general-attribute-mapping-errors). To learn about Logging pricing, see [Google Cloud Observability pricing](https://docs.cloud.google.com/stackdriver/pricing#logs-costs).

To disable detailed audit logging for a workforce identity pool provider, omit the `--detailed-audit-logging` flag when you run `gcloud iam workforce-pools providers create`. To disable detailed audit logging, you can also [update the provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#update-oidc-provider). 

The `--web-sso-assertion-claims-behavior` flag controls how OIDC claims are included in the `assertion` object used for attribute mappings and attribute conditions. For the authorization code flow (`--web-sso-response-type="code"`), you can set this flag to one of the following values: 

     * `merge-user-info-over-id-token-claims`: Merges claims from the OIDC `UserInfo` endpoint with claims from the ID token. If both contain the same claim name, the `UserInfo` claim value takes precedence. Use this value when your IdP returns additional user attributes or group claims from the `UserInfo` endpoint. 
     * `only-id-token-claims`: Includes only claims from the ID token. Use this value when all claims required for your attribute mappings and conditions are already present in the ID token. 
In the command response, POOL_RESOURCE_NAME is the name of the pool; for example, `locations/global/workforcePools/enterprise-example-organization-employees`.

### Implicit flow

To create an OIDC provider that uses the [implicit flow](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#oidc-flow-types) for web sign-in, run the following command:
    
    gcloud iam workforce-pools providers create-oidc WORKFORCE_PROVIDER_ID \
        --workforce-pool=WORKFORCE_POOL_ID \
        --display-name="DISPLAY_NAME" \
        --description="DESCRIPTION" \
        --issuer-uri="ISSUER_URI" \
        --client-id="OIDC_CLIENT_ID" \
        --web-sso-response-type="id-token" \
        --web-sso-assertion-claims-behavior="only-id-token-claims" \
        --web-sso-additional-scopes="WEB_SSO_ADDITIONAL_SCOPES" \
        --attribute-mapping="ATTRIBUTE_MAPPING" \
        --attribute-condition="ATTRIBUTE_CONDITION" \
        --jwk-json-path="JWK_JSON_PATH" \
        --detailed-audit-logging \
        --location=global
    

Replace the following: 

     * `WORKFORCE_PROVIDER_ID`: A unique workforce identity pool provider ID. The prefix `gcp-` is reserved and can't be used in a workforce identity pool or workforce identity pool provider ID.
     * `WORKFORCE_POOL_ID`: The workforce identity pool ID to connect your IdP to.
     * `DISPLAY_NAME`: An optional user-friendly display name for the provider; for example, `idp-eu-employees`.
     * `DESCRIPTION`: An optional workforce provider description; for example, `IdP for Partner Example Organization employees`. 
     * `ISSUER_URI`: The OIDC issuer URI, in a valid URI format, that starts with `https`; for example, `https://example.com/oidc`. Note: For security reasons, `ISSUER_URI` must use the HTTPS scheme.
     * `OIDC_CLIENT_ID`: The OIDC client ID that is registered with your OIDC IdP; the ID must match the `aud` claim of the JWT that is issued by your IdP.
     * `WEB_SSO_ADDITIONAL_SCOPES`: Optional additional scopes to send to the OIDC IdP for console (federated) or gcloud CLI browser-based sign-in.
     * `ATTRIBUTE_MAPPING`: An [attribute mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings). The following is an example of an attribute mapping: 
           
           google.subject=assertion.oid
           google.groups=assertion.groups,
           attribute.costcenter=assertion.costcenter

This example maps the IdP attributes `assertion.oid`, `assertion.groups`, and `assertion.costcenter` in the OIDC assertion to the Google Cloud attributes `google.subject`, `google.groups`, and `attribute.costcenter`, respectively. 
     * `ATTRIBUTE_CONDITION`: An [attribute condition](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions); for example, `assertion.role == 'gcp-users'`. This example condition ensures that only users with the role `gcp-users` can sign in using this provider. **Warning:** If your multi-tenant IdP has a single issuer URI, you must use [attribute conditions](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions) to ensure that access is restricted to the correct tenant. For more information, see [Use attribute conditions when federating with GitHub or other multi-tenant identity providers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#use-attribute-conditions-multitenant). 
     * `JWK_JSON_PATH`: An optional path to a [locally uploaded OIDC JWKs](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#json-web-keys). If this parameter isn't supplied, Google Cloud instead uses your IdP's `/.well-known/openid-configuration` path to source the JWKs containing the public keys. For more information about locally uploaded OIDC JWKs, see [manage OIDC JWKs](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#manage-oidc-keys). **Note:** Local OIDC JWKs can be uploaded through [implicit flow or code flow](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#oidc-flow-types), but can only be used in [programmatic flow](https://docs.cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials), in which you directly call the STS `/token` endpoint with a credential from the third-party IdP to exchange for a Google Cloud access token for your workforce pool. You can't use local OIDC JWKs when signing in to the console (federated). 
     * Workforce Identity Federation _detailed audit logging_ logs information received from your IdP to Logging. Detailed audit logging can help you troubleshoot your workforce identity pool provider configuration. To learn how to troubleshoot attribute mapping errors with detailed audit logging, see [General attribute mapping errors](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#general-attribute-mapping-errors). To learn about Logging pricing, see [Google Cloud Observability pricing](https://docs.cloud.google.com/stackdriver/pricing#logs-costs).

To disable detailed audit logging for a workforce identity pool provider, omit the `--detailed-audit-logging` flag when you run `gcloud iam workforce-pools providers create`. To disable detailed audit logging, you can also [update the provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#update-oidc-provider). 

For the implicit flow (`--web-sso-response-type="id-token"`), you must set the `--web-sso-assertion-claims-behavior` flag to `only-id-token-claims`, which includes only claims from the ID token in the `assertion` object. The implicit flow doesn't support the `merge-user-info-over-id-token-claims` value. 

In the command response, POOL_RESOURCE_NAME is the name of the pool; for example, `locations/global/workforcePools/enterprise-example-organization-employees`.

The prefix `gcp-` is reserved and can't be used in a workforce identity pool or workforce identity pool provider ID.

For OIDC federation, you can use `assertion.NAME`: a string equal to the value of the like-named claim in the ID token payload.

### Console

###  Code flow 

In the Google Cloud console, to create an OIDC provider that uses [authorization code flow](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#oidc-flow-types), do the following:

     1. In the Google Cloud console, go to the **Workforce Identity Pools** page: 

[Go to Workforce Identity Pools](https://console.cloud.google.com/iam-admin/workforce-identity-pools)

     2. In the **Workforce Identity Pools** table, select the pool for which you want to create the provider.
     3. In the **Providers** section, click **add Add Provider**.
     4. In the **Select a Provider vendor** list, select your IdP. 

If your IdP isn't listed, then select **Generic Identity Provider**.

     5. In **Select an authentication protocol** , select **OpenID Connect (OIDC)**.
     6. In the **Create a provider** section, do the following: 
        1. In **Name** , enter the name for the provider.
        2. In **Description** , enter the description for the provider.
        3. In **Issuer (URL)** , enter the issuer URI. The OIDC issuer URI must be in a valid URI format and start with `https`; for example, `https://example.com/oidc`.
        4. In **Client ID** , enter the OIDC client ID that is registered with your OIDC IdP; the ID must match the `aud` claim of the JWT that is issued by your IdP.
        5. To create a provider that is enabled, make sure **Enable provider** is on.
        6. Click **Continue**.
     7. In the **Share your provider information with IdP** section, copy the URL. In your IdP, configure this URL as the redirect URI, which informs your IdP where to send the assertion token after logging in.
     8. Click **Continue**.
     9. In the **Configure OIDC Web Sign-in** section, do the following: 
        1. In the **Flow type** list, select **Code**.
        2. In the **Assertion claims behavior** list, select one of the following options: 
           * **User info and ID token** : merges claims from the `UserInfo` endpoint with claims from the ID token, preferring `UserInfo` claim values for the same claim name. Select this option when your IdP returns additional user attributes or group claims from the `UserInfo` endpoint.
           * **Only ID token** : includes only claims from the ID token. Select this option when all claims required for your attribute mappings and conditions are already present in the ID token.
        3. In the **Client secret** field, enter the client secret from your IdP.
        4. Optional: If you selected **Okta** as your IdP, add any extra OIDC scopes in the **Additional scopes beyond openid, profile, and email** field.
     10. Click **Continue**.
     11. In the **Configure provider** section, for **Detailed logging** , click the **Enable attribute value audit logging** toggle. 

Workforce Identity Federation _detailed audit logging_ logs information received from your IdP to Logging. Detailed audit logging can help you troubleshoot your workforce identity pool provider configuration. To learn how to troubleshoot attribute mapping errors with detailed audit logging, see [General attribute mapping errors](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#general-attribute-mapping-errors). To learn about Logging pricing, see [Google Cloud Observability pricing](https://docs.cloud.google.com/stackdriver/pricing#logs-costs).

To disable detailed audit logging for a workforce identity pool provider, leave the **Enable attribute value audit logging** toggle off when you create the provider. To disable detailed audit logging, you can also [update the provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#update-oidc-provider). 

     12. To create the provider, click **Submit**.

After the provider is created, you are redirected to the provider attributes page.

To configure attribute mappings and conditions, do the following:

     1. When prompted, sign in to your external IdP to validate the default attribute mappings.
     2. On the provider attributes page, view and edit the attribute mappings and conditions: 
        1. To add or edit attribute mappings, do the following: 
           1. Click **Add mapping** to add a new mapping, or edit the existing mappings.
           2. In the **Google _n_** field, where _n_ is a number, select a Google Cloud-supported key.
           3. In the corresponding **OIDC _n_** field, enter the IdP attribute name or a CEL expression. 
        2. To add an attribute condition, do the following: **Warning:** If your multi-tenant IdP has a single issuer URI, you must use [attribute conditions](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions) to ensure that access is restricted to the correct tenant. For more information, see [Use attribute conditions when federating with GitHub or other multi-tenant identity providers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#use-attribute-conditions-multitenant). 
           1. Click **Add condition**.
           2. In the **Attribute Conditions** field, enter a condition in [CEL format](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions); for example, `assertion.role == 'gcp-users'`. This example condition ensures that only users with the role `gcp-users` can sign in using this provider.
     3. To validate your mappings, click **Save and refetch token**.
     4. To complete the setup, click **Save and exit**.

###  Implicit flow 

In the Google Cloud console, to create an OIDC provider that uses [implicit flow](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#oidc-flow-types), do the following:

     1. In the Google Cloud console, go to the **Workforce Identity Pools** page: 

[Go to Workforce Identity Pools](https://console.cloud.google.com/iam-admin/workforce-identity-pools)

     2. In the **Workforce Identity Pools** table, select the pool for which you want to create the provider.
     3. In the **Providers** section, click **add Add Provider**.
     4. In the **Select a Provider vendor** list, select your IdP. 

If your IdP isn't listed, then select **Generic Identity Provider**.

     5. In **Select an authentication protocol** , select **OpenID Connect (OIDC)**.
     6. In the **Create a provider** section, do the following: 
        1. In **Name** , enter the name for the provider.
        2. In **Description** , enter the description for the provider.
        3. In **Issuer (URL)** , enter the issuer URI. The OIDC issuer URI must be in a valid URI format and start with `https`; for example, `https://example.com/oidc`.
        4. In **Client ID** , enter the OIDC client ID that is registered with your OIDC IdP; the ID must match the `aud` claim of the JWT that is issued by your IdP.
        5. To create a provider that is enabled, make sure **Enable provider** is on.
        6. Click **Continue**.
     7. In the **Share your provider information with IdP** section, copy the URL. In your IdP, configure this url as the redirect URI, which informs your IdP where to send the assertion token after logging in.
     8. Click **Continue**.
     9. In the **Configure OIDC Web Sign-in** section, do the following: 
        1. In the **Flow type** list, select **ID Token**.
        2. In the **Assertion claims behavior** list, **ID token** is selected.
        3. Optional: If you selected **Okta** as your IdP, add any extra OIDC scopes in the **Additional scopes beyond openid, profile, and email** field.
     10. Click **Continue**.
     11. In the **Configure provider** section, in **Detailed logging** , click the **Enable attribute value audit logging** toggle. 

Workforce Identity Federation _detailed audit logging_ logs information received from your IdP to Logging. Detailed audit logging can help you troubleshoot your workforce identity pool provider configuration. To learn how to troubleshoot attribute mapping errors with detailed audit logging, see [General attribute mapping errors](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#general-attribute-mapping-errors). To learn about Logging pricing, see [Google Cloud Observability pricing](https://docs.cloud.google.com/stackdriver/pricing#logs-costs).

To disable detailed audit logging for a workforce identity pool provider, leave the **Enable attribute value audit logging** toggle off when you create the provider. To disable detailed audit logging, you can also [update the provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#update-oidc-provider). 

     12. To create the provider, click **Submit**.

After the provider is created, you are redirected to the provider attributes page.

To configure attribute mappings and conditions, do the following:

     1. When prompted, sign in to your external IdP to validate the default attribute mappings.
     2. On the provider attributes page, view and edit the attribute mappings and conditions: 
        1. To add or edit attribute mappings, do the following: 
           1. Click **Add mapping** to add a new mapping, or edit the existing mappings.
           2. In the **Google _n_** field, where _n_ is a number, select a Google Cloud-supported key.
           3. In the corresponding **OIDC _n_** field, enter the IdP attribute name or a CEL expression. 
        2. To add an attribute condition, do the following: **Warning:** If your multi-tenant IdP has a single issuer URI, you must use [attribute conditions](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions) to ensure that access is restricted to the correct tenant. For more information, see [Use attribute conditions when federating with GitHub or other multi-tenant identity providers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#use-attribute-conditions-multitenant). 
           1. Click **Add condition**.
           2. In the **Attribute Conditions** field, enter a condition in [CEL format](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions); for example, `assertion.role == 'gcp-users'`. This example condition ensures that only users with the role `gcp-users` can sign in using this provider.
     3. To validate your mappings, click **Save and refetch token**.
     4. To complete the setup, click **Save and exit**.




#### Create a SAML workforce pool provider

  1. In your SAML IdP, register a new application for Google Cloud Workforce Identity Federation.

  2. Set the audience for SAML assertions. It is usually the `SP Entity ID` field in your IdP configuration. You must set it to the following URL:
         
         https://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID
         

  3. Set the redirect URL, also known as the Assertion Consumer Service (ACS) URL. To set the redirect URL, locate the redirect URL field in your SAML IdP, and do one of the following:

     * To set up browser-based sign-in through the Google Cloud console or another browser-based sign-in method, enter following URL:
           
           https://auth.cloud.google/signin-callback/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID
           

Replace the following:

       * `WORKFORCE_POOL_ID`: the workforce identity pool ID

       * `WORKFORCE_PROVIDER_ID`: the ID of the workforce identity pool provider that you create later in this document.

     * To set up programmatic sign-in through your IdP, enter the following URL:
           
           localhost
           

See [Set up user access to the console](https://docs.cloud.google.com/iam/docs/workforce-console-sso) for more details on configuring console sign-in.

  4. In Google Cloud, create a SAML workforce identity pool provider using your IdP's SAML metadata document. You can download the SAML metadata XML document from your IdP. The document must include at least the following:

     * A SAML entity ID for your IdP.
     * The single-sign-on URL for your IdP.
     * At least one signing public key. See Key requirements later in this guide for details on signing keys.



###  gcloud

To configure the SAML provider using the gcloud CLI, do the following:
    
    
      gcloud iam workforce-pools providers create-saml WORKFORCE_PROVIDER_ID \
          --workforce-pool=WORKFORCE_POOL_ID \
          --display-name="DISPLAY_NAME" \
          --description="DESCRIPTION" \
          --idp-metadata-path=METADATA_FILE_PATH \
          --attribute-mapping="ATTRIBUTE_MAPPING" \
          --attribute-condition="ATTRIBUTE_CONDITION" \
          --location=global
    

Replace the following:

  * `WORKFORCE_PROVIDER_ID`: The workforce identity pool provider ID.
  * `WORKFORCE_POOL_ID`: The workforce identity pool ID.
  * `DISPLAY_NAME` The display name for the provider; for example, `idp-eu-employees`.
  * `DESCRIPTION`: The description for the workforce identity pool provider; for example, `IdP for Partner Example Organization EU employees`.
  * `METADATA_FILE_PATH`: The path of the SAML metadata file.
  * `ATTRIBUTE_MAPPING`: The [attribute mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings); for example:
        
        google.subject=assertion.subject
        attribute.costcenter=assertion.attributes.costcenter[0]

This example maps the `assertion.subject` IdP attribute to `google.subject` and the `assertion.attributes.costcenter[0]` IdP attribute to `attribute.costcenter`. 
  * `ATTRIBUTE_CONDITION`: An [attribute condition](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions). For example, to limit the `ipaddr` attribute to a certain IP range you can set the condition `assertion.attributes.ipaddr.startsWith('98.11.12.')`. This example condition ensures that only users with an IP address that starts with `98.11.12.` can sign in using this workforce provider.




It can take a few minutes for the provider to begin accepting requests.

For SAML federation, you can use the following keywords in attribute mappings and conditions:

  * `assertion.subject`: a string equal to the `NameID` attribute in the SAML assertion.
  * `assertion.attributes.NAME`: a string list equal to the values of the like-named attributes in the SAML assertion.



### Optional: Accept encrypted SAML assertions from your IdP

To enable your SAML 2.0 IdP to produce encrypted SAML assertions that can be accepted by workforce identity federation, do the following: 

  * In workforce identity federation, do the following:
    * Create an asymmetric key pair for your workforce identity pool provider.
    * Download a certificate file that contains the public key.
    * Configure your SAML IdP to use the public key to encrypt SAML assertions it issues.
  * In your IdP, do the following:
    * Enable assertion encryption, also known as token encryption.
    * Upload the public key that you created in workforce identity federation. 
    * Confirm that your IdP produces encrypted SAML assertions.

Note that, even with SAML encryption provider keys configured, workforce identity federation can still process a plaintext assertion. 

#### Create workforce identity federation SAML assertion encryption keys

This section guides you through creating an asymmetric key pair that enables workforce identity federation to accept encrypted SAML assertions. 

Google Cloud uses the private key to decrypt the SAML assertions that your IdP issues. To create an asymmetric key pair for use with SAML encryption, run the following command. To learn more, see Supported SAML encryption algorithms. 
    
    
    gcloud iam workforce-pools providers keys create KEY_ID \
        --workforce-pool WORKFORCE_POOL_ID \
        --provider WORKFORCE_PROVIDER_ID \
        --location global \
        --use encryption \
        --spec KEY_SPECIFICATION

Replace the following: 

  * `KEY_ID`: a key name of your choice
  * `WORKFORCE_POOL_ID`: the pool ID
  * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID
  * `KEY_SPECIFICATION`: the key specification, which can be one of `rsa-2048`, `rsa-3072`, and `rsa-4096`. 



After the key pair is created, to download the public key into a certificate file, execute the following command. Only workforce identity federation has access to the private key. 
    
    
    gcloud iam workforce-pools providers keys describe KEY_ID \
        --workforce-pool WORKFORCE_POOL_ID \
        --provider WORKFORCE_PROVIDER_ID \
        --location global \
        --format "value(keyData.key)" \
        > CERTIFICATE_PATH

Replace the following: 

  * `KEY_ID`: the key name
  * `WORKFORCE_POOL_ID`: the pool ID
  * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID
  * `CERTIFICATE_PATH`: the path to write the certificate to—for example, `saml-certificate.cer` or `saml-certificate.pem`



#### Configure your SAML 2.0-compliant IdP to issue encrypted SAML assertions

Configure your SAML IdP to use the public certificate downloaded from the last step to encrypt the SAML assertions that it issues. Consult your IdP team for specific instructions. 

After you configure your IdP to encrypt SAML assertions, we recommend that you check to make sure that the assertions it generates are actually encrypted. Even with SAML assertion encryption configured, workforce identity federation can still process plaintext assertions. 

#### Delete workforce identity federation encryption keys

To delete SAML encryption keys run the following command: 
    
    
      gcloud iam workforce-pools providers keys delete KEY_ID \
          --workforce-pool WORKFORCE_POOL_ID \
          --provider WORKFORCE_PROVIDER_ID \
          --location global

Replace the following: 

  * `KEY_ID`: the key name
  * `WORKFORCE_POOL_ID`: the pool ID
  * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID



#### Supported SAML encryption algorithms

Workforce identity federation supports the following key transport algorithms:

  * <http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p>
  * [http://www.w3.org/2009/xmlenc11#rsa-oaep"](http://www.w3.org/2009/xmlenc11#rsa-oaep)
  * [http://www.w3.org/2001/04/xmlenc#rsa-1_5"](http://www.w3.org/2001/04/xmlenc#rsa-1_5)



Workforce identity federation supports the following block encryption algorithms:

  * <http://www.w3.org/2001/04/xmlenc#aes128-cbc>
  * <http://www.w3.org/2001/04/xmlenc#aes192-cbc>
  * <http://www.w3.org/2001/04/xmlenc#aes256-cbc>
  * <http://www.w3.org/2009/xmlenc11#aes128-gcm>
  * <http://www.w3.org/2009/xmlenc11#aes256-gcm>



#### SAML X.509 signing key requirements

The following key specifications apply to SAML X.509 signing keys:

  * An RSA public key that is wrapped in an [X.509 v3 certificate](https://tools.ietf.org/html/rfc5280).

  * Certificate validity requirements:

    * `notBefore`: a timestamp that is no more than 7 days in the future
    * `notAfter`: a timestamp that is no more than 25 years in the future
  * Recommended algorithms:

    * [RSAwithSHA256](https://www.w3.org/TR/xmldsig-core1/#sec-PKCS1) (supported key sizes (bits): 2048, 3072, 4096)
    * [ECDSAwithSHA256](https://www.w3.org/TR/xmldsig-core1/#sec-ECDSA)



A workforce identity pool provider can be configured with at most three signing keys at a given time. When multiple keys exist, Google Cloud iterates through them and attempts to use each non-expired key to fulfill a token exchange request.

As a security best practice, we strongly recommend that you don't reuse the same key pair with other services.

#### Key management

**Important:** To ensure that your workforce users' access isn't disrupted when your keys expire, we recommend that you regularly update your keys. The public signing keys used to validate SAML assertion signatures have an expiration date. After the expiration date, the keys can't be used for token exchanges.

To update your IdP's signing keys, do the following:

  1. Create a new asymmetric key pair and configure the SAML identity provider with the key pair. You initially mark it as inactive before activating it in a later step.

  2. Download a SAML metadata XML document from your IdP.

  3. Update the workforce identity pool provider resource using the SAML metadata document. When multiple keys exist, Google Cloud iterates through each non-expired key and attempts to use each one to fulfill a token exchange request.

To update the workforce identity pool provider with the SAML metadata, execute the following command.
         
         gcloud iam workforce-pools providers update-saml WORKFORCE_PROVIDER_ID \
             --workforce-pool=WORKFORCE_POOL_ID \
             --idp-metadata-path=SAML_METADATA_FILE_PATH \
             --location=global
         

Replace the following:

     * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID
     * `WORKFORCE_POOL_ID`: the workforce identity pool ID
     * `SAML_METADATA_FILE_PATH`: the path to the SAML metadata file
  4. Wait for the operation returned from the previous step to complete (the operation is marked as done), and then in your SAML IdP, activate the new signing key. The old signing key is marked as inactive. Assertions issued by your IdP are signed using the new key.




The following steps are optional, but we recommend that you perform them as a best practice:

  1. Delete the old, now inactive, signing key from your IdP.
  2. Download the SAML metadata XML document from your IdP.
  3. Update the workforce identity pool provider resource using the SAML metadata document. Google Cloud refuses assertions that are signed with the expired signing key. To update the document, execute the following command:
         
         gcloud iam workforce-pools providers update-saml WORKFORCE_PROVIDER_ID \
             --workforce-pool=WORKFORCE_POOL_ID \
             --idp-metadata-path=SAML_METADATA_FILE_PATH \
             --location=global
         

Replace the following:

     * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID
     * `WORKFORCE_POOL_ID`: the workforce identity pool ID
     * `SAML_METADATA_FILE_PATH`: the SAML metadata path



### Key deletion constraint

Google Cloud refuses assertions signed with a deleted key.

**Caution:** Accidentally deleting a key that is still in use can lead to outages. You can only update a workforce identity pool provider resource if the SAML metadata contains at least one non-expired signing key. This restriction is skipped if all existing signing keys are expired.

###  Console 

To configure the SAML provider using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Workforce Identity Pools** page: 

[Go to Workforce Identity Pools](https://console.cloud.google.com/iam-admin/workforce-identity-pools)

  2. In the **Workforce Identity Pools** table, select the pool for which you want to create the provider.
  3. In the **Providers** section, click **add Add Provider**.
  4. In the **Select a Provider vendor** list, select your IdP. 

If your IdP isn't listed, then select **Generic Identity Provider**.

  5. In **Select an authentication protocol** , select **SAML**.
  6. In the **Create a provider** section, do the following: 
     1. In **Name** , enter a name for the provider.
     2. Optional: In **Description** , enter a description for the provider.
     3. In **IDP metadata file (XML)** , select the metadata XML file that you generated earlier in this guide.
     4. To create a provider that is enabled, make sure **Enable provider** is on.
     5. Click **Continue**.
  7. In the **Share your provider information** section, copy the URLs. In your IdP, configure the first URL as the entity ID, which identifies your application to the IdP. Configure the other URL as the redirect URI, which informs your IdP where to send the assertion token after signing in.
  8. Click **Continue**.
  9. In the **Configure provider** section, in **Detailed logging** , click the **Enable attribute value audit logging** toggle. 

Workforce Identity Federation _detailed audit logging_ logs information received from your IdP to Logging. Detailed audit logging can help you troubleshoot your workforce identity pool provider configuration. To learn how to troubleshoot attribute mapping errors with detailed audit logging, see [General attribute mapping errors](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#general-attribute-mapping-errors). To learn about Logging pricing, see [Google Cloud Observability pricing](https://docs.cloud.google.com/stackdriver/pricing#logs-costs).

To disable detailed audit logging for a workforce identity pool provider, leave the **Enable attribute value audit logging** toggle off when you create the provider. To disable detailed audit logging, you can also [update the provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#update-oidc-provider). 

  10. To create the provider, click **Submit**.



After the provider is created, you are redirected to the provider attributes page.

To configure attribute mappings and conditions, do the following:

  1. When prompted, sign in to your external IdP to validate the default attribute mappings.
  2. On the provider attributes page, view and edit the attribute mappings and conditions: 
     1. To add or edit attribute mappings, do the following: 
        1. Click **Add mapping** to add a new mapping, or edit the existing mappings.
        2. In the **Google _n_** field, where _n_ is a number, select a Google Cloud supported key.
        3. In the corresponding **SAML _n_** field, enter the IdP attribute name or a CEL expression—for example: 
               
               google.subject=assertion.subject
               attribute.costcenter=assertion.attributes.costcenter[0]

This example maps the `assertion.subject` IdP attribute to `google.subject` and the `assertion.attributes.costcenter[0]` IdP attribute to `attribute.costcenter`. 
     2. To add an attribute condition, do the following: **Warning:** If your multi-tenant IdP has a single issuer URI, you must use [attribute conditions](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions) to ensure that access is restricted to the correct tenant. For more information, see [Use attribute conditions when federating with GitHub or other multi-tenant identity providers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#use-attribute-conditions-multitenant). 
        1. Click **Add condition**.
        2. In the **Attribute Conditions** field, enter a condition in [CEL format](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions)—for example, For example, to limit the `ipaddr` attribute to a certain IP range you can set the condition `assertion.attributes.ipaddr.startsWith('98.11.12.')`. This example condition ensures that only users with an IP address that starts with `98.11.12.` can sign in using this workforce provider..
  3. To validate your mappings, click **Save and refetch token**.
  4. To complete the setup, click **Save and exit**.



## Verify your provider configuration

Before testing the end-user sign-in flow, you can verify that your provider configuration is correct and that Google Cloud can exchange tokens with your IdP. 

The **Validate your provider attributes** page in the Google Cloud console includes an attributes viewer that lets you interactively test your configuration and debug Common Expression Language (CEL) expressions. You can use the attributes viewer to do the following:

  * View the raw attributes sent in the IdP assertion.
  * Verify that your attribute mappings and conditions correctly transform those attributes.
  * Debug complex CEL expressions in real time.



To verify your provider configuration, do the following:

  1. To enable the browser-based sign-in flow for Workforce Identity Federation, add `https://auth.cloud.google/signin-callback/locations/global/workforcePools/POOL_ID/providers/PROVIDER_ID` to your IdP's list of allowed redirect URIs.
  2. In the Google Cloud console, go to **Workforce Identity Pools**.

[Go to Workforce Identity Pools](https://console.cloud.google.com/iam-admin/workforce-identity-pools)
  3. From the list of pools, click the name of the pool you want to verify.
  4. In the **Workforce pool details** page, click the name of the IdP you want to verify. 
  5. In the **Provider Details** page, click **Debug IdP token**.
  6. In the **Sign in** dialog, sign in to your IdP as a test user.



The **Validate your provider attributes** page displays the mapped attributes and the result of your attribute condition. 

The **Mapped attributes from your IdP token** section displays how Google attributes, such as `google.subject`, are populated from your IdP's token based on your mapping configuration. An error icon appears if a mapping is incorrect. 

The **Attribute condition** section shows the boolean result of your condition. If the condition evaluates to `false`, the sign-in is blocked. 

To view the full assertion token, click **View full token**. This shows the raw JSON object from your IdP. Reference a top-level property in your mappings using the format `assertion.PROPERTY_NAME`. 

### Edit your provider configuration

To correct any errors, you can edit the configuration: 

  1. In the **Validate your provider attributes** page, click ** edit  Edit**. 
  2. Make the necessary changes.
  3. To start a new test and see the updated results, click **Save and refetch token**. 



## Workforce principal identifiers for allow policies

The following table shows the principal identifiers that you can use to grant roles to individual users and groups of users.

Identities | Identifier format  
---|---  
Single identity in a workforce identity pool |  `principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE`  
All workforce identities in a group |  `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/group/GROUP_ID`  
All workforce identities with a specific attribute value |  `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE`  
All identities in a workforce identity pool |  `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/*`  
  
For a complete list of principal identifiers, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

## Grant IAM roles to principals

You can grant roles to principals, such as single identities, groups of identities, or an entire pool.

To grant a role on a project to a principal, execute the following command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --role="ROLE" \
        --member="PRINCIPAL"
    

Replace the following:

  * `PROJECT_ID`: the project ID
  * `ROLE`: the role to grant
  * `PRINCIPAL`: the principal; see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers) for Workforce Identity Federation.



In the example that follows, the command grants the Storage Admin role (`roles/storage.admin`) to all identities within the group `GROUP_ID`:
    
    
    gcloud projects add-iam-policy-binding my-project \
        --role="roles/storage.admin" \
        --member="principalSet://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/group/GROUP_ID"
    

For more information about the principal format, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers) for Workforce Identity Federation.

## Delete users

Workforce Identity Federation creates user metadata and resources for federated user identities. If you choose to delete users in your IdP you must also explicitly delete these resources in Google Cloud. To do so, see [Delete Workforce Identity Federation users and their data](https://docs.cloud.google.com/iam/docs/workforce-delete-user-data).

To immediately terminate a user's active sessions, you can revoke their sessions. For more information, see [Revoke Workforce Identity Federation user sessions](https://docs.cloud.google.com/iam/docs/workforce-revoke-sessions). 

You might see resources continue to be associated with a user that was deleted. This is because deleting user metadata and resources requires a long-running operation. After you initiate a deletion of a user's identity, processes that the user initiated before the deletion can continue to run until the processes complete or are canceled.

## What's next

  * [Obtain short-lived credentials for Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials)
  * [Manage workforce identity pool providers](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers)
  * [Delete Workforce Identity Federation users and their data](https://docs.cloud.google.com/iam/docs/workforce-delete-user-data)
  * [Revoke Workforce Identity Federation user sessions](https://docs.cloud.google.com/iam/docs/workforce-revoke-sessions)
  * Learn which Google Cloud products [support Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services)
  * [Set up user access to console (federated)](https://docs.cloud.google.com/iam/docs/workforce-console-sso)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
