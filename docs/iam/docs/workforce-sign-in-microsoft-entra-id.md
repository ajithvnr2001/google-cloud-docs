---
url: https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id/
title: Configure Workforce Identity Federation with Microsoft Entra ID and sign in users \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:13.168374+00:00
---

# Configure Workforce Identity Federation with Microsoft Entra ID and sign in users  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Configure Workforce Identity Federation with Microsoft Entra ID and sign in users Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to configure Workforce Identity Federation with the Microsoft Entra ID identity provider (IdP) and manage access to Google Cloud. Federated users can then access Google Cloud services that [support Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services). You can use either the OIDC protocol or SAML 2.0 protocol to federate identities.

**Important:** Using the instructions in this guide, you can map up to 150 groups from Microsoft Entra ID to Google Cloud. If you want to map up to 400 groups from Microsoft Entra ID to Google Cloud, see [Configure Workforce Identity Federation with Microsoft Entra ID and a large number of groups](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id-scalable-groups). The group limits apply to identity federation using OIDC protocol (implicit and code flow) and SAML 2.0 protocol.

## Before you begin

  1. Make sure that you have a Google Cloud organization set up.
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. In Microsoft Entra ID, make sure that ID tokens are enabled for implicit flow. For more information, see [Enable ID token implicit grant](https://learn.microsoft.com/en-us/azure/active-directory-b2c/tutorial-register-applications#enable-id-token-implicit-grant). 
  4. For sign-in, your IdP must provide signed authentication information: OIDC IdPs must provide a JWT, and SAML IdP responses must be signed. 
  5. To receive important information about changes to your organization or Google Cloud products, you must provide [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts). For more information, see the [Workforce Identity Federation overview](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#essential-contacts).



## Costs

Workforce Identity Federation is available as a no-cost feature. However, Workforce Identity Federation detailed audit logging uses Cloud Logging. To learn about Logging pricing, see [Google Cloud Observability pricing](https://docs.cloud.google.com/stackdriver/pricing#logs-costs). 

## Required roles

To get the permissions that you need to configure Workforce Identity Federation, ask your administrator to grant you the [IAM Workforce Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workforcePoolAdmin) (`roles/iam.workforcePoolAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If you're configuring permissions in a development or test environment—but not a production environment—you can grant the IAM Owner (`roles/owner`) basic role, which also includes permissions for Workforce Identity Federation.

## Create a Microsoft Entra ID application

This section shows you how to create a Microsoft Entra ID application using the Microsoft Entra admin center. Alternatively, you can update your existing application. For additional details, see [Establish applications in the Microsoft Entra ID ecosystem](https://learn.microsoft.com/en-us/entra/architecture/establish-applications). 

Workforce identity pools support federation using both OIDC and SAML protocols. 

### OIDC

To create a Microsoft Entra ID application registration that uses the OIDC protocol, do the following:

  1. Sign in to the Microsoft Entra admin center.

  2. Go to **Entra ID** > **App registrations**.

  3. To begin configuring the application registration, do the following:

     1. Click **New registration**.

     2. Enter a name for your application.

     3. In **Supported account types** , select an option.

     4. In the **Redirect URI** section, in the **Select a platform** drop-down list, select **Web**.

     5. In the text field, enter a redirect URL. Your users are redirected to this URL after they successfully sign in. If you are configuring access to the [console (federated)](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#console-federated), use the following URL format:
            
            https://auth.cloud.google/signin-callback/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID
            

Replace the following:

        * `WORKFORCE_POOL_ID`: a workforce identity pool ID that you use when creating the workforce identity pool later in this document—for example, `entra-id-oidc-pool`.
        * `WORKFORCE_PROVIDER_ID`: a workforce identity pool provider ID that you use when creating the workforce identity pool provider later in this document—for example, `entra-id-oidc-pool-provider`.

For information on formatting the ID, see the [Query parameters](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/create#query-parameters) section in the API documentation.

     6. To create the application registration, click **Register**.

     7. To use the example attribute mapping that is provided later in this document, you must create a custom `department` attribute. 




Recommended: As a [security best practice](https://docs.cloud.google.com/iam/docs/using-iam-securely), we recommend that you configure a group claim by doing the following:

  1. Go to your Microsoft Entra ID application registration.

  2. Click **Token configuration**.

  3. Click **Add groups claim**.

  4. Select the group types to return. For more details, refer to [Configuring groups optional claims](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims#configuring-groups-optional-claims).




### SAML

To create a Microsoft Entra ID application registration that uses the SAML protocol, do the following:

  1. Sign in to the Microsoft Entra admin center.

  2. Go to **Entra ID** > **Enterprise applications**.

  3. To begin configuring the enterprise application, do the following:

     1. Click **New application** > **Create your own application**.

     2. In the **Create your own application** pane that appears, enter a name for your application.

     3. Click **Create**.

     4. Go to **Single sign-on** > **SAML**.

     5. Update the **Basic SAML Configuration** as follows:

        1. In the **Identifier (Entity ID)** field, enter the following value:
               
               https://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID
               

Replace the following:

           * `WORKFORCE_POOL_ID`: a workforce identity pool ID that you use when creating the workforce identity pool later in this document—for example, `entra-id-saml-pool`.
           * `WORKFORCE_PROVIDER_ID`: a workforce identity pool provider ID that you use when creating the workforce identity pool provider later in this document—for example, `entra-id-saml-pool-provider`.

For information on formatting the ID, see the [Query parameters](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/create#query-parameters) section in the API documentation.

        2. In the **Reply URL (Assertion Consumer Service URL)** field, enter a redirect URL. Your users are redirected to this URL after they successfully sign in. If you are configuring access to the [console (federated)](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#console-federated), use the following URL format:
               
               https://auth.cloud.google/signin-callback/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID
               

Replace the following:

           * `WORKFORCE_POOL_ID`: the workforce identity pool ID.
           * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID.
        3. To enable IdP-initiated sign-on, set the **Relay State** field to the following value:
               
               https://console.cloud.google/
               

        4. To save the SAML application configuration, click **Save**.

     6. To use the example attribute mapping that is provided later in this document, you must create a custom `department` attribute. 

  4. [Assign users or groups to the application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/assign-user-or-group-access-portal).




Recommended: As a [security best practice](https://docs.cloud.google.com/iam/docs/using-iam-securely), we recommend that you configure a group claim by doing the following:

  1. Go to your Microsoft Entra ID application.

  2. Click **Single sign-on**.

  3. In the **Attributes & Claims** section, click **Edit**.

  4. Click **Add a group claim**.

  5. Select the group type to return. For more details, refer to [Add group claims to tokens for SAML applications using SSO configuration](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-fed-group-claims#add-group-claims-to-tokens-for-saml-applications-using-sso-configuration).




## Create a workforce identity pool

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

## Create the Microsoft Entra ID workforce identity pool provider

This section describes how to create a [workforce identity pool provider](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-identity-pool-providers) to enable your IdP users to access Google Cloud. You can configure the provider to use either the OIDC or SAML protocol.

### Create an OIDC workforce identity pool provider

To create a workforce identity pool provider for your Microsoft Entra ID application integration, using the OIDC protocol, do the following:

  1. To get the issuer URI for your Microsoft Entra ID application, do the following: 

     1. Go to the **Overview** page of your Microsoft Entra ID application registration.
     2. Click **Endpoints**.
     3. Find the **OpenID Connect metadata document** endpoint. The issuer URI is the OpenID Connect metadata document URI, omitting the trailing `/.well-known/openid-configuration`.

For example, if the OpenID Connect metadata document URI is `https://login.microsoftonline.com/d41ad248-019e-49e5-b3de-4bdfe1fapple/v2.0/.well-known/openid-configuration`, the issuer URI is `https://login.microsoftonline.com/d41ad248-019e-49e5-b3de-4bdfe1fapple/v2.0/`. Alternatively, you can copy the **OpenID Connect metadata document** URL, open it in a browser tab, and copy the value of `issuer` from the JSON response.

  2. To get the client ID for your Microsoft Entra ID application, do the following:

     1. Go to the **Overview** page of your Microsoft Entra ID application registration.
     2. In **Application (client) ID** , copy the value.
  3. To create an OIDC workforce identity pool provider for web-based sign-in, do the following:

### gcloud

To create a provider that supports the OIDC protocol, do the following:

### Code flow

To create an OIDC provider that uses [authorization code flow](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#oidc-flow-types) for web-based sign-in, do the following:

     1. In your Microsoft Entra ID application, to get your client secret, do the following:

        1. Go to your Microsoft Entra ID app registration.

        2. In **Certificates & secrets**, click the **Client secrets** tab.

        3. To add a client secret, click **\+ New client secret**.

        4. In the **Add a client secret** dialog, enter information, as needed.

        5. To create the client secret, click **Add**.

        6. In the **Client secrets** tab, find your new client secret.

        7. In the **Value** column for your new client secret, click _content_copy_ **Copy**.

     2. To create the provider, run the following command:
            
            gcloud iam workforce-pools providers create-oidc WORKFORCE_PROVIDER_ID \
                --workforce-pool=WORKFORCE_POOL_ID \
                --display-name="DISPLAY_NAME" \
                --description="DESCRIPTION" \
                --issuer-uri="ISSUER_URI" \
                --client-id="OIDC_CLIENT_ID" \  
                --client-secret-value="OIDC_CLIENT_SECRET" \  
                --vendor-type="entra-id" \
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
        * `ATTRIBUTE_MAPPING`: An [attribute mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings). For Microsoft Entra ID with OIDC authentication, we recommend the following attribute mappings: 
              
              google.subject=assertion.oid,
              google.groups=assertion.groups,
              google.display_name=assertion.preferred_username
              

This example maps the IdP attributes `assertion.oid`, `assertion.groups`, and `assertion.preferred_username` to the Google Cloud attributes `google.subject`, `google.groups`, and `google.display_name`, respectively. 

        * `ATTRIBUTE_CONDITION`: An [attribute condition](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions); for example, to limit the `ipaddr` attribute to a certain IP range you can set the condition `assertion.ipaddr.startsWith('98.11.12.')` . **Warning:** If your multi-tenant IdP has a single issuer URI, you must use [attribute conditions](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions) to ensure that access is restricted to the correct tenant. For more information, see [Use attribute conditions when federating with GitHub or other multi-tenant identity providers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#use-attribute-conditions-multitenant). 
        * `JWK_JSON_PATH`: An optional path to a [locally uploaded OIDC JWKs](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#json-web-keys). If this parameter isn't supplied, Google Cloud instead uses your IdP's `/.well-known/openid-configuration` path to source the JWKs containing the public keys. For more information about locally uploaded OIDC JWKs, see [manage OIDC JWKs](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#manage-oidc-keys). **Note:** Local OIDC JWKs can be uploaded through [implicit flow or code flow](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#oidc-flow-types), but can only be used in [programmatic flow](https://docs.cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials), in which you directly call the STS `/token` endpoint with a credential from the third-party IdP to exchange for a Google Cloud access token for your workforce pool. You can't use local OIDC JWKs when signing in to the console (federated). 
        * Workforce Identity Federation _detailed audit logging_ logs information received from your IdP to Logging. Detailed audit logging can help you troubleshoot your workforce identity pool provider configuration. To learn how to troubleshoot attribute mapping errors with detailed audit logging, see [General attribute mapping errors](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#general-attribute-mapping-errors). To learn about Logging pricing, see [Google Cloud Observability pricing](https://docs.cloud.google.com/stackdriver/pricing#logs-costs).

To disable detailed audit logging for a workforce identity pool provider, omit the `--detailed-audit-logging` flag when you run `gcloud iam workforce-pools providers create`. To disable detailed audit logging, you can also [update the provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#update-oidc-provider). 

The `--web-sso-assertion-claims-behavior` flag controls how OIDC claims are included in the `assertion` object used for attribute mappings and attribute conditions. For the authorization code flow (`--web-sso-response-type="code"`), you can set this flag to one of the following values: 

        * `merge-user-info-over-id-token-claims`: Merges claims from the OIDC `UserInfo` endpoint with claims from the ID token. If both contain the same claim name, the `UserInfo` claim value takes precedence. Use this value when your IdP returns additional user attributes or group claims from the `UserInfo` endpoint. 
        * `only-id-token-claims`: Includes only claims from the ID token. Use this value when all claims required for your attribute mappings and conditions are already present in the ID token. 
In the command response, POOL_RESOURCE_NAME is the name of the pool; for example, `locations/global/workforcePools/enterprise-example-organization-employees`.

### Implicit flow

To create an OIDC provider that uses the [implicit flow](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#oidc-flow-types) for web sign-in, do the following:

     1. To enable the ID token in your Microsoft Entra ID application, do the following:

        1. Go to your Microsoft Entra ID application registration.
        2. In **Authentication** , select the **ID token** checkbox.
        3. Click **Save**.
     2. To create the provider, run the following command:
            
            gcloud iam workforce-pools providers create-oidc WORKFORCE_PROVIDER_ID \
                --workforce-pool=WORKFORCE_POOL_ID \
                --display-name="DISPLAY_NAME" \
                --description="DESCRIPTION" \
                --issuer-uri="ISSUER_URI" \
                --client-id="OIDC_CLIENT_ID" \  
                --vendor-type="entra-id" \
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
        * `ATTRIBUTE_MAPPING`: An [attribute mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings). For Microsoft Entra ID with OIDC authentication, we recommend the following attribute mappings: 
              
              google.subject=assertion.oid,
              google.groups=assertion.groups,
              google.display_name=assertion.preferred_username
              

This example maps the IdP attributes `assertion.oid`, `assertion.groups`, and `assertion.preferred_username` to the Google Cloud attributes `google.subject`, `google.groups`, and `google.display_name`, respectively. 

        * `ATTRIBUTE_CONDITION`: An [attribute condition](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions); for example, to limit the `ipaddr` attribute to a certain IP range you can set the condition `assertion.ipaddr.startsWith('98.11.12.')` . **Warning:** If your multi-tenant IdP has a single issuer URI, you must use [attribute conditions](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions) to ensure that access is restricted to the correct tenant. For more information, see [Use attribute conditions when federating with GitHub or other multi-tenant identity providers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#use-attribute-conditions-multitenant). 
        * `JWK_JSON_PATH`: An optional path to a [locally uploaded OIDC JWKs](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#json-web-keys). If this parameter isn't supplied, Google Cloud instead uses your IdP's `/.well-known/openid-configuration` path to source the JWKs containing the public keys. For more information about locally uploaded OIDC JWKs, see [manage OIDC JWKs](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#manage-oidc-keys). **Note:** Local OIDC JWKs can be uploaded through [implicit flow or code flow](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#oidc-flow-types), but can only be used in [programmatic flow](https://docs.cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials), in which you directly call the STS `/token` endpoint with a credential from the third-party IdP to exchange for a Google Cloud access token for your workforce pool. You can't use local OIDC JWKs when signing in to the console (federated). 
        * Workforce Identity Federation _detailed audit logging_ logs information received from your IdP to Logging. Detailed audit logging can help you troubleshoot your workforce identity pool provider configuration. To learn how to troubleshoot attribute mapping errors with detailed audit logging, see [General attribute mapping errors](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#general-attribute-mapping-errors). To learn about Logging pricing, see [Google Cloud Observability pricing](https://docs.cloud.google.com/stackdriver/pricing#logs-costs).

To disable detailed audit logging for a workforce identity pool provider, omit the `--detailed-audit-logging` flag when you run `gcloud iam workforce-pools providers create`. To disable detailed audit logging, you can also [update the provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#update-oidc-provider). 

For the implicit flow (`--web-sso-response-type="id-token"`), you must set the `--web-sso-assertion-claims-behavior` flag to `only-id-token-claims`, which includes only claims from the ID token in the `assertion` object. The implicit flow doesn't support the `merge-user-info-over-id-token-claims` value. 

In the command response, POOL_RESOURCE_NAME is the name of the pool; for example, `locations/global/workforcePools/enterprise-example-organization-employees`.

### Console

### Code flow

To create an OIDC provider that uses [authorization code flow](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#oidc-flow-types) for web-based sign-in, do the following:

     1. To get the Microsoft Entra ID client secret, do the following:

        1. Go to your Microsoft Entra ID app registration.

        2. In **Certificates & secrets**, click the **Client secrets** tab.

        3. To add a client secret, click **\+ New client secret**.

        4. In the **Add a client secret** dialog, enter information, as needed.

        5. To create the client secret, click **Add**.

        6. In the **Client secrets** tab, find your new client secret.

        7. In the **Value** column for your new client secret, click _content_copy_ **Copy**.

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
           3. In the corresponding **OIDC _n_** field, enter the IdP attribute name or a CEL expression. For Microsoft Entra ID with OIDC authentication, we recommend the following attribute mappings: 
                  
                  google.subject=assertion.oid,
                  google.groups=assertion.groups,
                  google.display_name=assertion.preferred_username
                  

This example maps the IdP attributes `assertion.oid`, `assertion.groups`, and `assertion.preferred_username` to the Google Cloud attributes `google.subject`, `google.groups`, and `google.display_name`, respectively. 

        2. To increase the number of groups, do the following: 
           1. Click **Enable** for extra attributes.
           2. In the subtask that opens, enter the following details: 
              1. In the **Extra Attributes Issuer URI** field, enter the issuer URL.
              2. In the **Extra Attributes Client ID** field, enter the client ID.
              3. In the **Extra Attributes Client Secret** field, enter the client secret.
              4. In the **Extra Attributes Type** list, select an attribute type for extra attributes.
              5. In the **Extra Attributes Filter** field, enter a filter expression to be used when querying the Microsoft Graph API for groups.
              6. Click **Enable**.

After you enable extra attributes, you can click **Edit** to reopen the subtask and edit the details, or click **Disable** to turn off extra attributes.

        3. To add an attribute condition, do the following: **Warning:** If your multi-tenant IdP has a single issuer URI, you must use [attribute conditions](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions) to ensure that access is restricted to the correct tenant. For more information, see [Use attribute conditions when federating with GitHub or other multi-tenant identity providers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#use-attribute-conditions-multitenant). 
           1. Click **Add condition**.
           2. In the **Attribute Conditions** field, enter a condition in [CEL format](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions); for example, to limit the `ipaddr` attribute to a certain IP range you can set the condition `assertion.ipaddr.startsWith('98.11.12.')` .
     3. To validate your mappings, click **Save and refetch token**.
     4. To complete the setup, click **Save and exit**.

### Implicit flow

To create an OIDC provider that uses [implicit flow](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#oidc-flow-types) for web-based sign-in, do the following:

     1. To enable the ID token in your Microsoft Entra ID application, do the following:

        1. Go to your Microsoft Entra ID application registration.
        2. In **Authentication** , select the **ID token** checkbox.
        3. Click **Save**.

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
           3. In the corresponding **OIDC _n_** field, enter the IdP attribute name or a CEL expression. For Microsoft Entra ID with OIDC authentication, we recommend the following attribute mappings: 
                  
                  google.subject=assertion.oid,
                  google.groups=assertion.groups,
                  google.display_name=assertion.preferred_username
                  

This example maps the IdP attributes `assertion.oid`, `assertion.groups`, and `assertion.preferred_username` to the Google Cloud attributes `google.subject`, `google.groups`, and `google.display_name`, respectively. 

        2. To increase the number of groups, do the following: 
           1. Click **Enable** for extra attributes.
           2. In the subtask that opens, enter the details: 
              1. In the **Extra Attributes Issuer URI** field, enter the issuer URL.
              2. In the **Extra Attributes Client ID** field, enter the client ID.
              3. In the **Extra Attributes Client Secret** field, enter the client secret.
              4. In the **Extra Attributes Type** list, select an attribute type for extra attributes.
              5. In the **Extra Attributes Filter** field, enter a filter expression to be used when querying the Microsoft Graph API for groups.
              6. Click **Enable**.

After you enable extra attributes, you can click **Edit** to reopen the subtask and edit the details, or click **Disable** to turn off extra attributes.

        3. To add an attribute condition, do the following: **Warning:** If your multi-tenant IdP has a single issuer URI, you must use [attribute conditions](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions) to ensure that access is restricted to the correct tenant. For more information, see [Use attribute conditions when federating with GitHub or other multi-tenant identity providers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#use-attribute-conditions-multitenant). 
           1. Click **Add condition**.
           2. In the **Attribute Conditions** field, enter a condition in [CEL format](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions); for example, to limit the `ipaddr` attribute to a certain IP range you can set the condition `assertion.ipaddr.startsWith('98.11.12.')` .
     3. To validate your mappings, click **Save and refetch token**.
     4. To complete the setup, click **Save and exit**.




### Create a SAML 2.0 workforce identity pool provider

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



### gcloud

To save the SAML metadata for your Microsoft Entra ID application and create the provider, do the following:

  1. Go to your Microsoft Entra ID application.
  2. Click **Single sign-on**.
  3. In the **SAML Certificates** section, download the **Federation Metadata XML**.
  4. Save the metadata as a local XML file.



To create the SAML workforce identity pool provider, run the following command:
    
    
    gcloud iam workforce-pools providers create-saml WORKFORCE_PROVIDER_ID \
        --workforce-pool="WORKFORCE_POOL_ID" \
        --display-name="DISPLAY_NAME" \
        --description="DESCRIPTION" \
        --idp-metadata-path="XML_METADATA_PATH" \
        --attribute-mapping="ATTRIBUTE_MAPPING" \
        --attribute-condition="ATTRIBUTE_CONDITION" \
        --vendor-type="entra-id" \
        --detailed-audit-logging \
        --location=global
    

Replace the following:

  * `WORKFORCE_PROVIDER_ID`: A provider ID.
  * `WORKFORCE_POOL_ID`: The workforce identity pool ID.
  * `DISPLAY_NAME`: A display name.
  * `DESCRIPTION`: A description.
  * `XML_METADATA_PATH`: The path to the XML-formatted metadata file with configuration metadata for the SAML identity provider.
  * `ATTRIBUTE_MAPPING`: The [attribute mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings)— for example:
        
        google.subject=assertion.attributes['http://schemas.microsoft.com/identity/claims/objectidentifier'],
        attribute.costcenter=assertion.attributes.costcenter[0]

This example maps the `assertion.attributes['http://schemas.microsoft.com/identity/claims/objectidentifier']` IdP attribute to `google.subject` and the `assertion.attributes.costcenter[0]` IdP attribute to `attribute.costcenter`. 

For more information, see [Attribute mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mapping).

  * `ATTRIBUTE_CONDITION`: An optional [attribute condition](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions). For example, to limit the `ipaddr` attribute to a certain IP range you can set the condition `assertion.attributes.ipaddr.startsWith('98.11.12.')`. This example condition ensures that only users with an IP address that starts with `98.11.12.` can sign in using this workforce provider.




  * Workforce Identity Federation _detailed audit logging_ logs information received from your IdP to Logging. Detailed audit logging can help you troubleshoot your workforce identity pool provider configuration. To learn how to troubleshoot attribute mapping errors with detailed audit logging, see [General attribute mapping errors](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#general-attribute-mapping-errors). To learn about Logging pricing, see [Google Cloud Observability pricing](https://docs.cloud.google.com/stackdriver/pricing#logs-costs).

To disable detailed audit logging for a workforce identity pool provider, omit the `--detailed-audit-logging` flag when you run `gcloud iam workforce-pools providers create`. To disable detailed audit logging, you can also [update the provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#update-oidc-provider). 




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

To configure Microsoft Entra ID to encrypt SAML tokens, see <a href="https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/howto-saml-token-encryption?tabs=azure-portal"

> Configure Azure Active Directory SAML token encryption. 
> 
> After you configure your IdP to encrypt SAML assertions, we recommend that you check to make sure that the assertions it generates are actually encrypted. Even with SAML assertion encryption configured, workforce identity federation can still process plaintext assertions. 
> 
> #### Delete workforce identity federation encryption keys
> 
> To delete SAML encryption keys run the following command: 
>     
>     
>       gcloud iam workforce-pools providers keys delete KEY_ID \
>           --workforce-pool WORKFORCE_POOL_ID \
>           --provider WORKFORCE_PROVIDER_ID \
>           --location global
> 
> Replace the following: 
> 
>   * `KEY_ID`: the key name
>   * `WORKFORCE_POOL_ID`: the pool ID
>   * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID
> 

> 
> #### Supported SAML encryption algorithms
> 
> Workforce identity federation supports the following key transport algorithms:
> 
>   * <http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p>
>   * [http://www.w3.org/2009/xmlenc11#rsa-oaep"](http://www.w3.org/2009/xmlenc11#rsa-oaep)
>   * [http://www.w3.org/2001/04/xmlenc#rsa-1_5"](http://www.w3.org/2001/04/xmlenc#rsa-1_5)
> 

> 
> Workforce identity federation supports the following block encryption algorithms:
> 
>   * <http://www.w3.org/2001/04/xmlenc#aes128-cbc>
>   * <http://www.w3.org/2001/04/xmlenc#aes192-cbc>
>   * <http://www.w3.org/2001/04/xmlenc#aes256-cbc>
>   * <http://www.w3.org/2009/xmlenc11#aes128-gcm>
>   * <http://www.w3.org/2009/xmlenc11#aes256-gcm>
> 


### Console

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
               
               google.subject=assertion.attributes['http://schemas.microsoft.com/identity/claims/objectidentifier'],
               attribute.costcenter=assertion.attributes.costcenter[0]

This example maps the `assertion.attributes['http://schemas.microsoft.com/identity/claims/objectidentifier']` IdP attribute to `google.subject` and the `assertion.attributes.costcenter[0]` IdP attribute to `attribute.costcenter`. 

     2. To increase the number of groups, do the following: 
        1. Click **Enable** for extra attributes.
        2. In the subtask that opens, enter the details: 
           1. In the **Extra Attributes Issuer URI** field, enter the issuer URL.
           2. In the **Extra Attributes Client ID** field, enter the client ID.
           3. In the **Extra Attributes Client Secret** field, enter the client secret.
           4. In the **Extra Attributes Type** list, select an attribute type for extra attributes.
           5. In the **Extra Attributes Filter** field, enter a filter expression to be used when querying the Microsoft Graph API for groups.
           6. Click **Enable**.

After you enable extra attributes, you can click **Edit** to reopen the subtask and edit the details, or click **Disable** to turn off extra attributes.

     3. To add an attribute condition, do the following: **Warning:** If your multi-tenant IdP has a single issuer URI, you must use [attribute conditions](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions) to ensure that access is restricted to the correct tenant. For more information, see [Use attribute conditions when federating with GitHub or other multi-tenant identity providers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#use-attribute-conditions-multitenant). 
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



## Manage access to Google Cloud resources

This section provides an example that shows you how to manage access to Google Cloud resources by Workforce Identity Federation users.

In this example, you grant an Identity and Access Management (IAM) role on a sample project. Users can then sign in and use this project to access Google Cloud products.

**Note:** The sample project used here can be different from the project you used to set up Workforce Identity Federation.

You can manage IAM roles for single identities, a group of identities, or an entire pool. For more information, see [Workforce principal identifiers for allow policies](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#representing-workforce-users).

### Using mapped groups

To grant the Storage Admin role (`roles/storage.admin`) to all identities within the group `GROUP_ID` for project `TEST_PROJECT_ID`, run the following command:
    
    
    gcloud projects add-iam-policy-binding TEST_PROJECT_ID \
        --role="roles/storage.admin" \
        --member="principalSet://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/group/GROUP_ID"
    

Replace the following:

  * `TEST_PROJECT_ID`: the test project ID
  * `WORKFORCE_POOL_ID`: the workforce identity pool ID
  * `GROUP_ID`: a group in the mapped `google.groups` claim.



### For single identity 

To grant the Storage Admin (`roles/storage.admin`) role to a single identity for project `TEST_PROJECT_ID`, run the following command:
    
    
    gcloud projects add-iam-policy-binding TEST_PROJECT_ID \
        --role="roles/storage.admin" \
        --member="principal://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/subject/SUBJECT_VALUE"
    

Replace the following:

  * `TEST_PROJECT_ID`: the test project ID
  * `WORKFORCE_POOL_ID`: the workforce identity pool ID
  * `SUBJECT_VALUE`: the user identity



### Using mapped department attribute

To grant the Storage Admin role (`roles/storage.admin`) to all identities within a specific department for project `TEST_PROJECT_ID`, run the following command:
    
    
    gcloud projects add-iam-policy-binding TEST_PROJECT_ID \
        --role="roles/storage.admin" \
        --member="principalSet://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/attribute.department/DEPARTMENT_VALUE"
    

Replace the following:

  * `TEST_PROJECT_ID`: the test project ID
  * `WORKFORCE_POOL_ID`: the workforce identity pool ID
  * `DEPARTMENT_VALUE`: the mapped `attribute.department` value



## Sign in and test access

In this section, you sign in as a workforce identity pool user and test that you have access to Google Cloud resources.

### Sign in

This section shows you how to sign in as a federated user and access Google Cloud resources.

###  Console (federated) sign-in 

To sign in to the Google Cloud Workforce Identity Federation console, also known as the console (federated), do the following:

  1. Go to the console (federated) sign-in page.

[Go to console (federated)](https://auth.cloud.google/signin?continueUrl=https://console.cloud.google/)

  2. Enter the provider name, which is formatted as follows: 
         
         locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID

If prompted, enter user credentials in Microsoft Entra ID.

If you start an IdP-initiated sign-on, use the following for the relay URL: `https://console.cloud.google/`.




###  gcloud CLI browser-based sign-in 

To sign in to gcloud CLI using a browser-based sign-in flow, do the following:

**Create a configuration file**

Run the following command to create a login configuration file:

### Linux and macOS
    
    
    gcloud iam workforce-pools create-login-config \
        locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID \
        --output-file=LOGIN_CONFIG_PATH

### Windows (PowerShell)
    
    
    gcloud iam workforce-pools create-login-config `
        locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID `
        --output-file=LOGIN_CONFIG_PATH

**Note:** You can optionally activate the login configuration file as the default for the gcloud CLI by adding the [ `--activate`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-login-config#--activate) flag. You can then run `gcloud auth login` to authorize the gcloud CLI without specifying the login configuration file path each time. 

Replace the following:

  * `WORKFORCE_POOL_ID`: The Workforce Identity Federation pool ID.
  * `WORKFORCE_PROVIDER_ID`: The Workforce Identity Federation provider ID.
  * `LOGIN_CONFIG_PATH`: The path to write the login configuration file to. For example, `login-config.json`. 



The login configuration file contains the endpoints used by the gcloud CLI to enable the browser-based authentication flow and set the audience to the IdP that was configured in the workforce identity pool provider. The file doesn't contain confidential information. 

The login configuration file content looks similar to the following:
    
    
    {
      "universe_domain": "googleapis.com",
      "universe_cloud_web_domain": "cloud.google",
      "type": "external_account_authorized_user_login_config",
      "audience": "//iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID",
      "auth_url": "https://auth.cloud.google/authorize",
      "token_url": "https://sts.googleapis.com/v1/oauthtoken",
      "token_info_url": "https://sts.googleapis.com/v1/introspect"
    }

**Caution:** We recommend that you first ensure that the contents of this file are correct and then safeguard the file—for example, by making it read-only and restricting access with an ACL. The file isn't validated; a malicious actor with write access to this file can change the endpoints and intercept credentials. 

**Sign in using browser-based authentication**

Point to the login configuration file with an environment variable, a property in the active gcloud CLI configuration, or use it directly with the `gcloud auth login` command: 

### Environment variable

To use the login configuration file with an environment variable, complete the following instructions: 

  1. Set the `CLOUDSDK_AUTH_LOGIN_CONFIG_FILE` environment variable to the path of the login configuration file. 
  2. Run the following command:
         
         gcloud auth login

  3. The gcloud CLI references the environment variable to find the login configuration file, and then starts the authentication process. Follow the browser-based flow to authenticate and authorize the gcloud CLI to access resources on your behalf for future commands. 



To stop using the login configuration file for `gcloud auth login` commands, clear the `CLOUDSDK_AUTH_LOGIN_CONFIG_FILE` environment variable. 

### gcloud CLI configuration

To use the login configuration file with a gcloud CLI configuration property, complete the following instructions: 

  1. Set the active gcloud CLI configuration's `auth/login_config_file` property to the login configuration file's path with the following command: 
         
         gcloud config set auth/login_config_file LOGIN_CONFIG_PATH

  2. Run the following command:
         
         gcloud auth login

  3. The gcloud CLI references the configuration property to find the login configuration file, and then starts the authentication process. Follow the browser-based flow to authenticate and authorize the gcloud CLI to access resources on your behalf for future commands. 



To stop using the login configuration file for `gcloud auth login` commands, unset the property with the following command: 
    
    
    gcloud config unset auth/login_config_file

### gcloud auth login

To use the login configuration file directly with the `gcloud auth login` command, complete the following instructions: 

  * If you used the `--activate` flag when you created the login configuration file, run the following command: 
        
        gcloud auth login

  * If you didn't use the `--activate` flag when you created the login configuration file, run the following command: 

### Linux and macOS
        
        gcloud auth login \
            --login-config=LOGIN_CONFIG_PATH

### Windows (PowerShell)
        
        gcloud auth login `
            --login-config=LOGIN_CONFIG_PATH

Replace LOGIN_CONFIG_PATH with the path of your login configuration file. 




The [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command stores access credentials in your home directory. The authenticated principal becomes the active principal in your active gcloud CLI configuration. Unless overridden, the gcloud CLI uses these stored credentials to access Google Cloud. 

**Caution** : Any user with access to your file system can use the stored access credentials created by `gcloud auth login`. To reduce the consequences of a system being compromised, strictly separate human and workload use, and don't use `gcloud auth login` for automated workloads on remote systems with persistent storage. Where possible, use a secret manager in combination with environment variables instead. 

For more guidance on hardening remote systems, see [ Best practices for protecting developer credentials](https://docs.cloud.google.com/docs/security/bps-for-protecting-developer-credentials). 

###  gcloud CLI headless sign-in 

To sign in to Microsoft Entra ID with the gcloud CLI, do the following:

### OIDC

  1. Follow the steps in [Send the sign-in request](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-implicit-grant-flow#send-the-sign-in-request). Sign the user into your application with Microsoft Entra ID using OIDC.

  2. Copy the ID token from the `id_token` parameter of the redirect URL and save it to a file in a secure location on your local machine. In a later step, you set PATH_TO_OIDC_ID_TOKEN to the path to this file.

  3. Generate a configuration file similar to the example later in this step by running the following command:
         
         gcloud iam workforce-pools create-cred-config \
             locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID \
             --subject-token-type=urn:ietf:params:oauth:token-type:id_token \
             --credential-source-file=PATH_TO_OIDC_ID_TOKEN \
             --workforce-pool-user-project=WORKFORCE_POOL_USER_PROJECT \
             --output-file=config.json
         

Replace the following:

     * `WORKFORCE_POOL_ID`: the workforce identity pool ID.
     * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID.
     * `PATH_TO_OIDC_ID_TOKEN`: the path to the file location where the IdP token is stored.
     * `WORKFORCE_POOL_USER_PROJECT`: the project number or ID used for quota and billing. The principal must have `serviceusage.services.use` permission on this project.

When the command completes, the following config file is created by Microsoft Entra ID:
    
    {
      "type": "external_account",
      "audience": "//iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID",
      "subject_token_type": "urn:ietf:params:oauth:token-type:id_token",
      "token_url": "https://sts.googleapis.com/v1/token",
      "workforce_pool_user_project": "WORKFORCE_POOL_USER_PROJECT",
      "credential_source": {
        "file": "PATH_TO_OIDC_CREDENTIALS"
      }
    }
    

  4. Open the gcloud CLI and run the following command:
         
         gcloud auth login --cred-file=PATH_TO_OIDC_CREDENTIALS
         

Replace PATH_TO_OIDC_CREDENTIALS with the path to the output file from a previous step.

The gcloud CLI transparently posts your credentials to the Security Token Service endpoint. In the endpoint, it is exchanged for temporary Google Cloud access tokens.

You can now run gcloud CLI commands to Google Cloud.




### SAML

  1. Sign in a user to your Microsoft Entra ID application and get the SAML response.

  2. Save the SAML response returned by Microsoft Entra ID in a secure location on your local machine, then store the path as follows:
         
         SAML_ASSERTION_PATH=SAML_ASSERTION_PATH
         

  3. To generate a credential configuration file, run the following command:
         
         gcloud iam workforce-pools create-cred-config \
             locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID \
             --subject-token-type=urn:ietf:params:oauth:token-type:saml2 \
             --credential-source-file=SAML_ASSERTION_PATH  \
             --workforce-pool-user-project=PROJECT_ID  \
             --output-file=config.json
         

Replace the following:

     * `WORKFORCE_PROVIDER_ID`: the ID of the workforce identity pool provider that you created earlier in this guide
     * `WORKFORCE_POOL_ID`: the ID of the workforce identity pool that you created earlier in this guide
     * `SAML_ASSERTION_PATH`: the path of the SAML assertion file
     * `PROJECT_ID`: the project ID

The configuration file that is generated looks similar to the following:
    
    {
       "type": "external_account",
       "audience": "//iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID",
       "subject_token_type": "urn:ietf:params:oauth:token-type:saml2",
       "token_url": "https://sts.googleapis.com/v1/token",
       "credential_source": {
         "file": "SAML_ASSERTION_PATH"
       },
       "workforce_pool_user_project": "PROJECT_ID"
    }
    

  4. To login to the gcloud CLI using Workforce Identity Federation token exchange, run the following command:
         
         gcloud auth login --cred-file=config.json
         

The gcloud CLI then transparently exchanges your Microsoft Entra ID credentials for temporary Google Cloud access tokens. The access tokens let you access Google Cloud.

You see output similar to the following:
         
         Authenticated with external account user credentials for:
         [principal://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/subject/USER_ID].

  5. To list the credentialed accounts and your active account, run the following command:
         
         gcloud auth list
         




### Test Access

You now have access to the Google Cloud products that support Workforce Identity Federation and to which you are granted access. Earlier in this document, you granted the Storage Admin role (`roles/storage.admin`) to all of the identities within the group identifier that you specified in the `gcloud projects add-iam-policy-binding` for project `TEST_PROJECT_ID`.

You can now test that you have access by listing Cloud Storage buckets.

###  Console (federated) 

To test that you have access using the console (federated), do the following:

  * Go to the Cloud Storage page.

[Go to Cloud Storage](https://console.cloud.google.com/storage)

  * Verify that you can see a list of existing buckets for the `TEST_PROJECT_ID`.




###  gcloud CLI 

To test that you have access using the gcloud CLI, you can list Cloud Storage buckets and objects for the project that you have access to. To do this, run the following command. The principal must have the `serviceusage.services.use` permission on the specified project.
    
    
    gcloud storage ls --project="TEST_PROJECT_ID"
    

## Delete users

Workforce Identity Federation creates user metadata and resources for federated user identities. If you choose to delete users in your IdP you must also explicitly delete these resources in Google Cloud. To do so, see [Delete Workforce Identity Federation users and their data](https://docs.cloud.google.com/iam/docs/workforce-delete-user-data).

To immediately terminate a user's active sessions, you can revoke their sessions. For more information, see [Revoke Workforce Identity Federation user sessions](https://docs.cloud.google.com/iam/docs/workforce-revoke-sessions). 

You might see resources continue to be associated with a user that was deleted. This is because deleting user metadata and resources requires a long-running operation. After you initiate a deletion of a user's identity, processes that the user initiated before the deletion can continue to run until the processes complete or are canceled.

## What's next

  * [Configure SCIM in Microsoft Entra ID](https://docs.cloud.google.com/iam/docs/configure-scim-ms-entra)
  * [Delete Workforce Identity Federation users and their data](https://docs.cloud.google.com/iam/docs/workforce-delete-user-data)
  * [Revoke Workforce Identity Federation user sessions](https://docs.cloud.google.com/iam/docs/workforce-revoke-sessions)
  * Learn which Google Cloud products [support Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services)
  * [Set up user access to console (federated)](https://docs.cloud.google.com/iam/docs/workforce-console-sso)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
