---
url: https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers/
title: Configure Workload Identity Federation with other identity providers \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:03.481979+00:00
---

# Configure Workload Identity Federation with other identity providers  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Configure Workload Identity Federation with other identity providers Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to use Workload Identity Federation with other identity providers (IdPs). 

To authenticate to Google Cloud, you can let the workload exchange its environment-specific credentials for short-lived Google Cloud credentials by using Workload Identity Federation.

Workloads that run outside of Google Cloud might have access to existing, environment-specific credentials, for example:

  * A workload might be able to obtain an OpenID Connect (OIDC) assertion token from an IdP.

  * A workload might be able to obtain a SAML assertion token from an identity provider (IdP).




Using Workload Identity Federation can help you [reduce the number of credentials that require rotation](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#reduce-number-of-credentials).

The following sections describe how you can use Workload Identity Federation with IdPs that support either OpenID Connect (OIDC) or SAML authentication protocols.

**Note:** If your workloads run on AWS or Azure, see [Configure Workload Identity Federation with AWS or Azure](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds) instead. If you're using Active Directory Federation Services (AD FS) as IdP, see [Configure Workload Identity Federation with Active Directory](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-active-directory). If you've configured AWS with [outbound identity federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound_getting_started.html), continue with the following OIDC instructions on this page.

## Prepare your external IdP

You need to perform these steps once for each IdP.

Before you begin, verify that your external IdP meets the following requirements:

###  OIDC 

  * The IdP supports OpenID Connect 1.0.

  * The IdP has an issuer URI.

  * Google Cloud can access a [JSON web key set (JWKS)](https://www.rfc-editor.org/info/rfc7517) that contains [JSON web keys (JWKs)](https://www.rfc-editor.org/info/rfc7517). The JWKs are used to validate OIDC assertion tokens. You can provide access to the JWKS through one of the following methods:

    * Google Cloud downloads [OIDC metadata](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata) from the IdP, through a publicly available, well-known, internet-accessible discovery URL. Within the metadata, the JWKS URL must be secured with SSL and TLS. The JWKS URL must start with `https://`. Google Cloud doesn't support JWKS URLs that are secured with self-signed certificates.

Google Cloud uses these endpoint URLs to download your IdP's JSON web keys (JWKs) and uses these keys to validate tokens. Google Cloud doesn't limit the number of keys that it can download.

    * You can upload an OIDC JWKS file directly to Google Cloud when you create or update the OIDC workload identity pool provider. To do this, you use the `--jwk-json-path` to provide a path to your JWKS file. You can use this method when the IdP's OIDC metadata endpoint URL isn't publicly accessible. A maximum of 8 keys can be uploaded to Google Cloud. As a best practice, we recommend that you rotate your JWKS keys regularly by updating the JWKS file.

  * If you're federating workloads from AWS using [AWS Outbound Identity Federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound.html), AWS acts as your OIDC IdP. To prepare your AWS environment, follow these steps:

    1. Enable outbound identity federation in your AWS account settings to generate your unique OIDC issuer URL.

    2. Ensure your AWS workloads (such as EC2 instance profiles or ECS task roles) have the required AWS IAM policy granting permission to get JSON Web Tokens (JWTs).




###  SAML 

  * The IdP supports SAML 2.0.

  * The IdP provides a [SAML SP metadata document](https://docs.oasis-open.org/security/saml/v2.0/saml-metadata-2.0-os.pdf) that describes the SAML service provider configuration and contains the IdP's signing certificate.

Google Cloud uses this certificate to validate SAML assertions and responses.

  * The IdP signing certificate must contain either an ECDSA or RSA key that is within an [X.509 v3 certificate](https://tools.ietf.org/html/rfc5280).

  * Recommended signing algorithms include the following:

    * [ECDSAwithSHA256](https://www.w3.org/TR/xmldsig-core1/#sec-ECDSA)
    * [RSAwithSHA256](https://www.w3.org/TR/xmldsig-core1/#sec-PKCS1) with supported key sizes of 2048, 3072, and 4096 bits.
  * The signing certificate must meet the following validity requirements:

    * `notBefore`: a timestamp that is no more than 7 days in the future
    * `notAfter`: a timestamp that is no more than 25 years in the future



You can configure a SAML workload identity pool provider with at most three SAML signing certificates at a given time. This limitation doesn't apply to other workload identity pool provider types, like OIDC and X.509. When multiple certificates exist, Google Cloud iterates through them and attempts to use each non-expired certificate to fulfill a token exchange request.

As a security best practice, we strongly recommend that you don't reuse the same key pair with other services.

If your IdP meets these criteria, do the following:

###  OIDC 

Configure your IdP so that your workload can obtain ID tokens that meet the following criteria:

  * Tokens are signed using the `RS256` or `ES256` algorithm.
  * Tokens contain an `aud` claim with the following value:
        
        https://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID
        

Replace the following:

    * `PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of the Google Cloud project that you use to create a workload identity pool.
    * `POOL_ID`: an ID of your choice that identifies the workload identity pool. You must use the same ID when creating the workload identity pool later.
    * `WORKLOAD_PROVIDER_ID`: an ID of your choice that identifies the workload identity pool provider. You must use the same ID when creating the workload identity pool provider later.

Alternatively, you can configure the workload identity pool provider to expect a custom audience.

  * Tokens contain an `exp` claim that is in the future and an `iat` claim that is in the past.

The value of `exp` must be greater than the value of `iat` by at most 24 hours.




Typically, it's best to use ID tokens when performing a token exchange, because ID tokens reflect the user's identity. If you decide to use access tokens instead, make sure that access tokens meet the following additional requirements:

  * Access tokens are [JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token)-formatted.
  * Access tokens contain an `ISSUER` claim so that the URL `ISSUER/.well-known/openid-configuration` points to the IdP's OIDC metadata endpoint.

  * To upload local JWK keys, see [Manage OIDC JWKs](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#manage-oidc-keys). 


**Note:** Workload Identity Federation doesn't support opaque tokens or [token introspection](https://datatracker.ietf.org/doc/html/rfc7662).

###  SAML 

Configure your IdP so that SAML assertions contain elements that meet the following criteria:

  * an `Issuer` element that is set to the Entity ID configured in the workload identity pool provider. The issuer format must be omitted or set to `urn:oasis:names:tc:SAML:2.0:nameid-format:entity`.
  * a `Subject` element with: 
    * a `NameID` element.
    * exactly one `SubjectConfirmation` element with `Method` set to `urn:oasis:names:tc:SAML:2.0:cm:bearer`.
    * a `SubjectConfirmationData` element with `NotOnOrAfter` set to a timestamp that occurs in the future and no `NotBefore` value.
  * a `Conditions` element with:

    * `NotBefore` omitted or in the past.
    * `NotOnOrAfter` omitted or in the future.
    * An `Audience` that is formatted as follows:
          
          https://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID
          

Replace the following:

      * `PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of the Google Cloud project that you use to create workload identity pool.
      * `POOL_ID`: an ID of your choice that identifies the workload identity pool. You must use the same ID when creating the workload identity pool later.
      * `WORKLOAD_PROVIDER_ID`: an ID of your choice that identifies the workload identity pool provider. You must use the same ID when creating the workload identity pool provider later.
  * at least one `AuthnStatement` element.

  * a `SessionNotOnOrAfter` element with a timestamp that occurs in the future. Alternatively, omit the element.




For SAML assertions that are enclosed in a SAML response, the SAML response must contain:

  * exactly one assertion that meets the SAML assertion criteria that is described earlier in this section.
  * an `IssueInstant` attribute with a value less than 1 hour in the past.
  * the StatusCode `urn:oasis:names:tc:SAML:2.0:status:Success`.



Either the SAML assertion, the response, or both must be signed.

## Configure Workload Identity Federation

You only need to perform these steps once for each IdP. You can then use the same workload identity pool and provider for multiple workloads and across multiple Google Cloud projects.

To start configuring Workload Identity Federation, do the following:

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

It's best to [ use a dedicated project to manage workload identity pools and providers](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#dedicated-project). 
  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

Enable the IAM, Resource Manager, Service Account Credentials, and Security Token Service APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,cloudresourcemanager.googleapis.com,iamcredentials.googleapis.com,sts.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Manage self-uploaded OIDC JWKs (Optional)

This section shows you how to manage self-uploaded OIDC JWKs in workload identity pool OIDC providers.

#### Create a provider and upload OIDC JWKs

To create OIDC JWKs, see [JWT, JWS, JWE, JWK, and JWA Implementations](https://openid.net/developers/jwt/).

To upload an OIDC JWK file when you create a workload identity pool provider, run the [gcloud iam workload-identity-pools providers create-oidc](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/create-oidc) command with `--jwk-json-path="JWK_JSON_PATH"`. Replace `JWK_JSON_PATH` with the path to the JWKs JSON file.

This operation creates uploaded keys with the ones in the file.

#### Update OIDC JWKs

To update OIDC JWKs, run the [gcloud iam workload-identity-pools providers update-oidc](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/update-oidc) command with `--jwk-json-path="JWK_JSON_PATH"`. Replace `JWK_JSON_PATH` with the path to the JWKs JSON file.

This operation replaces any existing uploaded keys with the ones in the file. You cannot restore the replaced keys.

#### Delete all uploaded OIDC JWKs

To delete all of the uploaded OIDC JWKs and return to using the issuer URI to fetch the keys, run the [gcloud iam workload-identity-pools providers update-oidc](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/update-oidc) command with `--jwk-json-path="JWK_JSON_PATH"`. Replace `JWK_JSON_PATH` with the path to an empty file. Use the `--issuer-uri` flag to set the issuer URI.

This operation deletes all of your existing uploaded keys with the ones in the file. You cannot restore the deleted keys.

### Define an attribute mapping and condition

The OIDC tokens or SAML assertions issued by your IdP might contain multiple attributes, and you must decide which attribute you want to use as subject identifier (`google.subject`) in Google Cloud.

Optionally, you can [map additional attributes](https://docs.cloud.google.com/iam/docs/workload-identity-federation#mapping). You can then refer to these attributes when granting access to resources.

###  OIDC 

Your attribute mappings can use the claims embedded in the ID token or access token issued by the external IdP.

You must map one of these claims to `google.subject` to uniquely identify the user. To protect against spoofing threats, choose a claim with a unique value that can't be changed.

Many IdPs populate the `sub` claim with a unique and immutable ID. For these IdPs, consider mapping the `sub` claim to `google.subject`:
    
    
    google.subject=assertion.sub
    

Avoid using a claim like `email` for this purpose. Email addresses can typically be reassigned or changed, so they don't uniquely and permanently identify a user.

###  SAML 

Your attribute mappings can use the `<Subject>` and `<Attribute>` elements embedded in the assertion issued by the external IdP. SAML attributes can be referred to using the following keywords:

  * `assertion.subject` contains the `NameID` of the authenticated user found in the `<Subject>` element.
  * `assertion.attributes['ATTRIBUTE_NAME']` contains a list of values for the like-named `<Attribute>`.



You must map one of these claims to `google.subject` to uniquely identify the user. To protect against spoofing threats, choose a claim with a unique value that can't be changed.

Many IdPs populate the `NameId` with a unique and immutable ID. For these IdPs, consider mapping the `NameId` attribute to `google.subject`:
    
    
    google.subject=assertion.subject
    

Avoid using an attribute like `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` for this purpose. Email addresses can typically be reassigned or changed, so they don't uniquely and permanently identify a user.

Optionally, define an [attribute condition](https://docs.cloud.google.com/iam/docs/workload-identity-federation#conditions). Attribute conditions are CEL expressions that can check assertion attributes and target attributes. If the attribute condition evaluates to `true` for a given credential, the credential is accepted. Otherwise, the credential is rejected.

###  OIDC 

You can use an attribute condition to restrict which users can use Workload Identity Federation to obtain short-lived Google Cloud tokens.

For example, the following condition restricts access to tokens that contain a custom `service_account` claim with a value `true`:
    
    
    assertion.service_account==true
    

###  SAML 

You can use an attribute condition to restrict which users can use Workload Identity Federation to obtain short-lived Google Cloud tokens.

For example, the following condition restricts access to assertions that contain a custom `https://example.com/SAML/Attributes/AllowGcpFederation` attribute with a value `true`:
    
    
    assertion.attributes['https://example.com/SAML/Attributes/AllowGcpFederation'][0]=='true'
    

### Create the workload identity pool and provider

#### Required roles

To get the permissions that you need to configure Workload Identity Federation, ask your administrator to grant you the following IAM roles on the project: 

  * [Workload Identity Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityPoolAdmin) (`roles/iam.workloadIdentityPoolAdmin`)
  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Alternatively, the IAM Owner (`roles/owner`) basic role also includes permissions to configure identity federation. You should not grant basic roles in a production environment, but you can grant them in a development or test environment. 

You now have collected all the information that you need to create a workload identity pool and provider:

###  Console 

  1. In the Google Cloud console, go to the **New workload provider and pool** page.

[Go to New workload provider and pool](https://console.cloud.google.com/iam-admin/workload-identity-pools/create)

  2. Under **Create an identity pool** , enter the following:

     * **Name** : Name for the pool. The name is also used as the pool ID. You can't change the pool ID later.
     * **Description** : Text that describes the purpose of the pool.
  3. Click **Continue**.

  4. Configure provider settings as follows:

###  OIDC 

     * In **Select a provider** , select **OpenID Connect (OIDC)**.
     * In **Provider name** , enter a name for the provider. The name is also used as the provider ID. You can't change the provider ID after the provider is created.
     * In **Issuer URL** , enter the issuer URL of your IdP. The URL must start with `https://`
     * Optional: In **JWK file (JSON)** , choose a JWK file to upload. If this field is not supplied, Google Cloud attempts to fetch a JWK from the issuer.
     * **Allowed audiences** : Expected audience of ID tokens.

###  SAML 

     * In **Select a provider** , select **SAML**.
     * In **Provider name** , enter a name for the provider. The name is also used as the provider ID. You can't change the provider ID after the provider is created.
     * In **IDP Metadata file (XML)** , upload the SAML metadata XML document that is provided by your IdP.

  5. Click **Continue**.

  6. Under **Configure provider attributes** , add the attribute mappings that you identified earlier in this guide.

  7. Under **Attribute conditions** , enter the attribute condition that you identified earlier in this guide. Leave the field blank if you don't have an attribute condition.

  8. To create the workload identity pool and provider, click **Save**.




###  gcloud 

  1. To create a new workload identity pool, execute the following command:
         
         gcloud iam workload-identity-pools create POOL_ID \
             --location="global" \
             --description="DESCRIPTION" \
             --display-name="DISPLAY_NAME"
         

Replace the following:

     * `POOL_ID`: the unique ID for the pool.
     * `DISPLAY_NAME`: the name of the pool.
     * `DESCRIPTION`: a description of the pool that you choose. This description appears when you grant access to pool identities.
  2. To add a workload identity pool provider, do the following:

###  OIDC 

To add an OIDC workload identity pool provider, execute the following command:
         
         gcloud iam workload-identity-pools providers create-oidc WORKLOAD_PROVIDER_ID \
             --location="global" \
             --workload-identity-pool="POOL_ID" \
             --issuer-uri="ISSUER" \
             --allowed-audiences="AUDIENCE" \
             --attribute-mapping="MAPPINGS" \
             --attribute-condition="CONDITIONS"
             --jwk-json-path="JWK_JSON_PATH"
         

Replace the following:

     * `WORKLOAD_PROVIDER_ID`: A unique workload identity pool provider ID of your choice.
     * `POOL_ID`: The workload identity pool ID that you created earlier.
     * `ISSUER`: An issuer URI as it is defined in the OIDC metadata.
     * `AUDIENCE`: The expected audience of ID tokens, which, for many providers, matches the client ID.
     * `MAPPINGS`: A comma-separated list of attribute mappings that you created earlier in this guide.
     * `CONDITIONS`: An optional attribute condition that you created earlier in this guide. Remove the parameter if you don't have an attribute condition.
     * `JWK_JSON_PATH`: An optional path to a [locally uploaded OIDC JWKs](https://docs.cloud.google.com/iam/docs/workload-identity-federation#oidc-credential-security). If this parameter isn't supplied, Google Cloud instead uses your IdP's `/.well-known/openid-configuration` path to source the JWKs containing the public keys.

###  SAML 

To add a SAML workload identity pool provider, execute the following command:
    
    gcloud iam workload-identity-pools providers create-saml WORKLOAD_PROVIDER_ID \
        --location="global" \
        --workload-identity-pool="POOL_ID" \
        --idp-metadata-path="IDP_METADATA_PATH" \
        --attribute-mapping="MAPPINGS" \
        --attribute-condition="CONDITIONS"
    

Replace the following:

     * `POOL_ID`: the ID of the pool
     * `IDP_METADATA_PATH`: the local path to the SAML IdP's metadata document
     * `MAPPINGS`: a comma-separated list of attribute mappings that you created earlier in this guide
     * `CONDITIONS`: Optional: the attribute condition that you created earlier in this guide

The prefix `gcp-` is reserved and can't be used in a workforce identity pool or workforce identity pool provider ID.

### Optional: Accept encrypted SAML assertions from your IdP

To enable your SAML 2.0 IdP to produce encrypted SAML assertions that can be accepted by workload identity federation, do the following: 

     * In workload identity federation, do the following:
       * Create an asymmetric key pair for your workload identity pool provider.
       * Download a certificate file that contains the public key.
       * Configure your SAML IdP to use the public key to encrypt SAML assertions it issues.
     * In your IdP, do the following:
       * Enable assertion encryption, also known as token encryption.
       * Upload the public key that you created in workload identity federation. 
       * Confirm that your IdP produces encrypted SAML assertions.
Note that, even with SAML encryption provider keys configured, workload identity federation can still process a plaintext assertion. 

#### Create workload identity federation SAML assertion encryption keys

This section guides you through creating an asymmetric key pair that enables workload identity federation to accept encrypted SAML assertions. 

Google Cloud uses the private key to decrypt the SAML assertions that your IdP issues. To create an asymmetric key pair for use with SAML encryption, run the following command. To learn more, see Supported SAML encryption algorithms. 
    
    gcloud iam workload-identity-pools providers keys create KEY_ID \
        --workload-identity-pool WORKLOAD_POOL_ID \
        --provider WORKLOAD_PROVIDER_ID \
        --location global \
        --use encryption \
        --spec KEY_SPECIFICATION

Replace the following: 

     * `KEY_ID`: a key name of your choice
     * `WORKLOAD_POOL_ID`: the pool ID
     * `WORKLOAD_PROVIDER_ID`: the workforce identity pool provider ID
     * `KEY_SPECIFICATION`: the key specification, which can be one of `rsa-2048`, `rsa-3072`, and `rsa-4096`. 

After the key pair is created, to download the public key into a certificate file, execute the following command. Only workload identity federation has access to the private key. 
    
    gcloud iam workload-identity-pools providers keys describe KEY_ID \
        --workload-identity-pool WORKLOAD_POOL_ID \
        --provider WORKLOAD_PROVIDER_ID \
        --location global \
        --format "value(keyData.key)" \
        > CERTIFICATE_PATH

Replace the following: 

     * `KEY_ID`: the key name
     * `WORKLOAD_POOL_ID`: the pool ID
     * `WORKLOAD_PROVIDER_ID`: the workforce identity pool provider ID
     * `CERTIFICATE_PATH`: the path to write the certificate to—for example, `saml-certificate.cer` or `saml-certificate.pem`

#### Configure your SAML 2.0-compliant IdP to issue encrypted SAML assertions

Configure your SAML IdP to use the public certificate downloaded from the last step to encrypt the SAML assertions that it issues. Consult your IdP team for specific instructions. 

After you configure your IdP to encrypt SAML assertions, we recommend that you check to make sure that the assertions it generates are actually encrypted. Even with SAML assertion encryption configured, workload identity federation can still process plaintext assertions. 

#### Delete workload identity federation encryption keys

To delete SAML encryption keys run the following command: 
    
    gcloud iam workload-identity-pools providers keys delete KEY_ID \
          --workload-identity-pool WORKLOAD_POOL_ID \
          --provider WORKLOAD_PROVIDER_ID \
          --location global

Replace the following: 

     * `KEY_ID`: the key name
     * `WORKLOAD_POOL_ID`: the pool ID
     * `WORKLOAD_PROVIDER_ID`: the workforce identity pool provider ID

#### Supported SAML encryption algorithms

Workload identity federation supports the following key transport algorithms:

     * <http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p>
     * [http://www.w3.org/2009/xmlenc11#rsa-oaep"](http://www.w3.org/2009/xmlenc11#rsa-oaep)
     * [http://www.w3.org/2001/04/xmlenc#rsa-1_5"](http://www.w3.org/2001/04/xmlenc#rsa-1_5)

Workload identity federation supports the following block encryption algorithms:

     * <http://www.w3.org/2001/04/xmlenc#aes128-cbc>
     * <http://www.w3.org/2001/04/xmlenc#aes192-cbc>
     * <http://www.w3.org/2001/04/xmlenc#aes256-cbc>
     * <http://www.w3.org/2009/xmlenc11#aes128-gcm>
     * <http://www.w3.org/2009/xmlenc11#aes256-gcm>




## Authenticate a workload

You must perform these steps once for each workload.

### Allow your external workload to access Google Cloud resources

To provide your workload with access to Google Cloud resources, we recommend that you grant direct resource access to the principal. In this case, the principal is the federated user. Some Google Cloud products have [Google Cloud API limitations](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services). If your workload calls an API endpoint that has a limitation, you can instead use service account impersonation. In this case, the principal is the Google Cloud service account, which acts as the identity. You grant access to the service account on the resource.

### Direct resource access

You can grant access to a federated identity directly on resources by using the Google Cloud console or the gcloud CLI.

### Console

To use the Google Cloud console to grant IAM roles directly on a resource, you must go to the resource's page, and then grant the role. The following example shows you how to go to the Cloud Storage page and grant the role Storage Object Viewer (`roles/storage.objectViewer`) to a federated identity directly on a Cloud Storage bucket.

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket for which you want to grant the role.

  3. Select the **Permissions** tab near the top of the page.

  4. Click the _add_box_ **Grant access** button.

The **Add principals** dialog appears.

  5. In the **New principals** field, enter one or more identities that need access to your bucket.

###  By subject 
         
         principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT
         

Replace the following:

     * `PROJECT_NUMBER`: the project number
     * `POOL_ID`: the workload pool ID
     * `SUBJECT`: the individual subject mapped from your IdP—for example, `administrator@example.com`

###  By group 
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP
    

Replace the following:

     * `PROJECT_NUMBER`: the project number
     * `WORKLOAD_POOL_ID`: the workload pool ID
     * `GROUP`: the group mapped from your IdP—for example: `administrator-group@example.com`

###  By attribute 
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE
    

Replace the following:

     * `PROJECT_NUMBER`: the project number
     * `WORKLOAD_POOL_ID`: the workload pool ID
     * `ATTRIBUTE_NAME`: one of the attributes that was mapped from your IdP
     * `ATTRIBUTE_VALUE`: the value of the attribute

  6. Select a role (or roles) from the **Select a role** drop-down menu. The roles you select appear in the pane with a short description of the permissions they grant.

  7. Click **Save**.




###  gcloud 

To use the gcloud CLI to grant IAM roles on a resource in a project, do the following:

  1. Obtain the project number of the project in which the resource is defined.
         
         gcloud projects describe $(gcloud config get-value core/project) --format=value\(projectNumber\)
         

  2. Grant access to the resource.

To use the gcloud CLI to grant the role Storage Object Viewer (`roles/storage.objectViewer`) to external identities that meet certain criteria, run the following command. 

### By subject
         
         gcloud storage buckets add-iam-policy-binding BUCKET_ID \
             --role=roles/storage.objectViewer \
             --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT"

### By group
         
         gcloud storage buckets add-iam-policy-binding BUCKET_ID \
             --role=roles/storage.objectViewer \
             --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP"

### By attribute
         
         gcloud storage buckets add-iam-policy-binding BUCKET_ID \
             --role=roles/storage.objectViewer \
             --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE"

Replace the following:

     * `BUCKET_ID`: the bucket on which to grant access
     * `PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). of the project that contains the workload identity pool
     * `POOL_ID`: the pool ID of the workload identity pool
     * `SUBJECT`: the expected value for the attribute that you've mapped to `google.subject`
     * `GROUP`: the expected value for the attribute that you've mapped to `google.groups`
     * `ATTRIBUTE_NAME`: the name of a custom attribute in your attribute mapping
     * `ATTRIBUTE_VALUE`: the value of the custom attribute in your attribute mapping

You can grant roles on any Google Cloud resource that supports IAM allow policies.

**Note:** You must use the project number, not the project ID, in the member identifier.



### Service account impersonation

  1. To create a service account for the external workload, do the following:

     1. Enable the IAM, Security Token Service, and Service Account Credentials APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,sts.googleapis.com,iamcredentials.googleapis.com&redirect=https%3A//console.cloud.google.com)

     2. [Create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) that represents the workload. We recommend that you [use a dedicated service account for each workload](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#use-dedicated-service-accounts). The service account doesn't need to be in the same project as the workload identity pool, but you must refer to the project that contains the service account.

     3. [Grant the service account access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to resources that you want external identities to access.

  2. To let the federated identity impersonate the service account, do the following:




### Console

To use the Google Cloud console to grant IAM roles to a federated identity with service account, do the following:

### Service Account in the same project

  1. To grant access using service account impersonation for a service account in the same project, do the following:

     1. Go to the **Workload Identity Pools** page.

[Go to Workload Identity Pools](https://console.cloud.google.com/iam-admin/workload-identity-pools)

     2. Select **Grant access**.

     3. In the **Grant access to service account** dialog, select **Grant access using Service Account impersonation**.

     4. In the **Service accounts** list, select the service account for the external identities to impersonate, and do the following:

     5. To choose which identities in the pool can impersonate the service account, perform one of the following actions:

        * To allow only specific identities of the workload identity pool to impersonate the service account, select **Only identities matching the filter**.

        * In the **Attribute name** list, select the attribute that you want to filter on.

        * In the **Attribute value** field, enter the expected value of the attribute; for example, if you use an attribute mapping `google.subject=assertion.sub`, set **Attribute** name to `subject` and **Attribute value** to the value of the `sub` claim in tokens that are issued by your external identity provider.

     6. To save the configuration, click **Save** and then **Dismiss**.




### Service account in a different project

**Note:** Service accounts from different projects won't appear in the "CONNECTED SERVICE ACCOUNTS" section of your **Workload Identity Pool**.

  1. To grant access using service account impersonation for a service account in a different project, do the following:

     1. Go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

     2. Select the service account that you want to impersonate.

     3. Click **Manage access**.

     4. Click **Add principal**.

     5. In the **New principal** field, enter one of the following [principal identifiers](https://docs.cloud.google.com/iam/docs/workload-identity-federation#principal-types) for the identities in your pool that will impersonate the service account.

###  By subject 
            
            principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT
            

Replace the following:

        * `PROJECT_NUMBER`: the project number
        * `POOL_ID`: the workload pool ID
        * `SUBJECT`: the individual subject mapped from your IdP—for example, `administrator@example.com`

###  By group 
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP
    

Replace the following:

        * `PROJECT_NUMBER`: the project number
        * `WORKLOAD_POOL_ID`: the workload pool ID
        * `GROUP`: the group mapped from your IdP—for example: `administrator-group@example.com`

###  By attribute 
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE
    

Replace the following:

        * `PROJECT_NUMBER`: the project number
        * `WORKLOAD_POOL_ID`: the workload pool ID
        * `ATTRIBUTE_NAME`: one of the attributes that was mapped from your IdP
        * `ATTRIBUTE_VALUE`: the value of the attribute

### By pool
    
    principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/*
    

Replace the following:

        * `PROJECT_NUMBER`: the project number
        * `WORKLOAD_POOL_ID`: the workload pool ID

     6. In **Select a role** , select the Workload Identity User role (`roles/iam.workloadIdentityUser`).

     7. To save the configuration, click **Save**.




### gcloud

To grant the Workload Identity User role (`roles/iam.workloadIdentityUser`) to a federated principal or principal set, run the following command. To learn more about Workload Identity Federation principal identifiers, see [Principal types](https://docs.cloud.google.com/iam/docs/workload-identity-federation#principal-types). 

### By subject
    
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_EMAIL \
        --role=roles/iam.workloadIdentityUser \
        --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT"

### By group
    
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_EMAIL \
        --role=roles/iam.workloadIdentityUser \
        --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP"

### By attribute
    
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_EMAIL \
        --role=roles/iam.workloadIdentityUser \
        --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE"

Replace the following:

  * `SERVICE_ACCOUNT_EMAIL`: the email address of the service account
  * `PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). of the project that contains the workload identity pool
  * `POOL_ID`: the pool ID of the workload identity pool
  * `SUBJECT`: the expected value for the attribute that you've mapped to `google.subject`
  * `GROUP`: the expected value for the attribute that you've mapped to `google.groups`
  * `ATTRIBUTE_NAME`: the name of a custom attribute in your attribute mapping
  * `ATTRIBUTE_VALUE`: the value of the custom attribute in your attribute mapping

**Note:** You must use the project number, not the project ID, in the member identifier.

### Download a credential configuration

This section describes how to download the credential configuration using the Google Cloud console.

To let your workload access client libraries, you must first download and configure [application default credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) by doing the following: 

  1. In the Google Cloud console, go to the **Workload Identity Pools** page.

[Go to Workload Identity Pools](https://console.cloud.google.com/iam-admin/workload-identity-pools)
  2. In the table, select your pool to go the pool's detail page.

  3. Click **Grant access**.

  4. Select **Grant access using federated identities (Recommended)**. 

  5. To download the Application Default Credential (ADC) so that your workload can access client libraries, do the following: 

     1. Click **Download config**.

     2. In the **Configure your application** dialog, do the following:

        1. In the **Provider** drop-down list, select your provider. 

        2. In **OIDC token path** or **SAML assertion path** , enter the path where the token or assertion is located. 

In the **Format type** drop-down list, select the format. 

     3. Click **Download configuration** , and note the path where you saved the file. 




### Create a credential configuration

The [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries), the gcloud CLI, and Terraform, can automatically obtain external credentials, and use these credentials to access Google Cloud. To let libraries and tools complete this process, you have to provide a credential configuration file. This file defines the following:

  * Where to obtain external credentials from
  * Which workload identity pool and provider to use
  * Which service account to impersonate, if you use service account impersonation



The Cloud Client Libraries obtain external credentials from a local file, an HTTP URL, by running a local executable:

  * **Executable-sourced credentials** : The libraries launch an executable whenever they need a new credential. If the executable succeeds in obtaining a new external credential, it must write a JSON document to `STDOUT` that looks like the following:

###  OIDC 
        
        {
          "version": 1,
          "success": true,
          "token_type": "urn:ietf:params:oauth:token-type:id_token",
          "id_token": "HEADER.PAYLOAD.SIGNATURE",
          "expiration_time": 1620499962
        }
        

If the executable fails to obtain a new credential, it must write a JSON document to `STDOUT` that looks like the following:
        
        {
          "version": 1,
          "success": false,
          "code": "401",
          "message": "Caller not authorized."
        }
        

The JSON documents use the following fields:

    * `version`: The version of the JSON output. Only version 1 is supported.
    * `success`: The status of the response.

When `true`, the response must contain the fields `id_token` and `token_type`. The executable must exit with exit code 0.

When `false`, the response must contain the fields `code` and `message` and exit with a non-zero value.

    * `token_type`: The token type of the external credential. Supported values are

      * `urn:ietf:params:oauth:token-type:id_token`
      * `urn:ietf:params:oauth:token-type:jwt`
    * `id_token`: The external credential.

    * `expiration_time`: The OIDC token expiration time in seconds (Unix epoch time). This field is only required when an output file has been specified in the credential configuration.

    * `code`: The error code string.

    * `message`: The error message.

###  SAML 
    
    {
      "version": 1,
      "success": true,
      "token_type": "urn:ietf:params:oauth:token-type:saml2",
      "saml_response": "...",
      "expiration_time": 1620499962
    }
    

If the executable fails to obtain a new credential, it must write a JSON document to `STDOUT` that looks like the following:
    
    {
      "version": 1,
      "success": false,
      "code": "401",
      "message": "Caller not authorized."
    }
    

The JSON documents use the following fields:

    * `version`: The version of the JSON output. Only version 1 is supported.
    * `success`: The status of the response.

When `true`, the response must contain the fields `id_token` and `token_type`. The executable must exit with exit code 0.

When `false`, the response must contain the fields `code` and `message` and exit with a non-zero value.

    * `token_type`: The token type of the external credential. Must be `urn:ietf:params:oauth:token-type:saml2`.

    * `saml_response`: The SAML response or base64-encoded SAML assertion.

    * `expiration_time`: The assertion expiration time in seconds (Unix epoch time). This field is only required when an output file has been specified in the credential configuration.

    * `code`: The error code string.

    * `message`: The error message.

When launching the executable, client libraries set the following environment variables:

    * `GOOGLE_EXTERNAL_ACCOUNT_AUDIENCE`: Audience from the credential configuration. Always present.
    * `GOOGLE_EXTERNAL_ACCOUNT_TOKEN_TYPE`: Expected subject token type. Always present.
    * `GOOGLE_EXTERNAL_ACCOUNT_IMPERSONATED_EMAIL`: Service account email. Only present when service account impersonation is used.
    * `GOOGLE_EXTERNAL_ACCOUNT_OUTPUT_FILE`: Output file location from the credential configuration. Only present when specified in the credential configuration.

To use executable-sourced credentials, you must set the environment variable `GOOGLE_EXTERNAL_ACCOUNT_ALLOW_EXECUTABLES` to `1`.

  * **File-sourced credentials** : The libraries read the external credential from a local plain text or JSON file. For example:

###  JSON 
        
        {
          "mytoken": "ey...
        }
        

###  Text 
        
        ey...
        

The external credential can be:

    * an OIDC token
    * a SAML response
    * a base64-encoded SAML assertion

You must periodically update the file so that it always contains a valid credential. For example, if the OIDC token or SAML assertion is valid for one hour, you must refresh the file at least once every hour.

  * **URL-sourced credentials** : The libraries perform a `GET` request to an HTTP endpoint whenever they need a new credential. The endpoint must return a plain text or JSON response that is equivalent to the format used by file-sourced credentials.


**Note:** Unlike a [service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys), a credential configuration file doesn't contain a private key and doesn't need to be kept confidential. Details about the credential configuration file are available at <https://google.aip.dev/auth/4117>.

To create a credential configuration file, do the following:

###  Executable-sourced credentials 
    
    
    gcloud iam workload-identity-pools create-cred-config \
        projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
        --service-account=SERVICE_ACCOUNT_EMAIL \
        --service-account-token-lifetime-seconds=SERVICE_ACCOUNT_TOKEN_LIFETIME \
        --sts-location=REGION \
        --output-file=FILEPATH.json \
        --executable-command=EXECUTABLE_COMMAND \
        --executable-timeout-millis=EXECUTABLE_TIMEOUT \
        --executable-output-file=EXECUTABLE_OUTPUT_FILE

Replace the following:

  * `PROJECT_NUMBER`: The project number of the project that contains the workload identity pool.
  * `POOL_ID`: The ID of the workload identity pool.
  * `WORKLOAD_PROVIDER_ID`: The ID of the workload identity pool provider.
  * `SERVICE_ACCOUNT_EMAIL`: If you use service account impersonation, replace with the email address of the service account. Omit this flag if you don't use service account impersonation.
  * `SERVICE_ACCOUNT_TOKEN_LIFETIME`: If you use service account impersonation, replace with the lifetime of the service account access token, in seconds; this defaults to one hour when not provided. Omit this flag if you don't use service account impersonation. To specify a lifetime longer than one hour, you must configure the `constraints/iam.allowServiceAccountCredentialLifetimeExtension` [organizational policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).
  * `REGION`: Optional. Specify the region of the [regional Security Token Service endpoints](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#sts-regional-endpoints), if they are available.
  * `FILEPATH`: The file to save the configuration to.
  * `EXECUTABLE_COMMAND`: The full command, including arguments, to run to retrieve the OIDC ID token—for example, `--executable-command="/path/to/command --foo=bar"`.
  * `EXECUTABLE_TIMEOUT`: The optional duration in milliseconds to wait for the executable to run (defaults to 30s).
  * `EXECUTABLE_OUTPUT_FILE`: A path that points to the 3PI credentials generated by the executable. This is useful for caching the credentials. By specifying this path, the Auth libraries will first check for its existence before running the executable.



###  File-sourced credentials 
    
    
    gcloud iam workload-identity-pools create-cred-config \
        projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
        --service-account=SERVICE_ACCOUNT_EMAIL \
        --service-account-token-lifetime-seconds=SERVICE_ACCOUNT_TOKEN_LIFETIME \
        --sts-location=REGION \
        --output-file=FILEPATH.json \
        --credential-source-file=TOKEN_FILEPATH \
        --credential-source-type=SOURCE_TYPE \
        --credential-source-field-name=FIELD_NAME

Replace the following:

  * `PROJECT_NUMBER`: The project number of the project that contains the workload identity pool.
  * `POOL_ID`: The ID of the workload identity pool.
  * `WORKLOAD_PROVIDER_ID`: The ID of the workload identity pool provider.
  * `SERVICE_ACCOUNT_EMAIL`: If you use service account impersonation, replace with the email address of the service account. Omit this flag if you don't use service account impersonation.
  * `SERVICE_ACCOUNT_TOKEN_LIFETIME`: If you use service account impersonation, replace with the lifetime of the service account access token, in seconds; this defaults to one hour when not provided. Omit this flag if you don't use service account impersonation. To specify a lifetime longer than one hour, you must configure the `constraints/iam.allowServiceAccountCredentialLifetimeExtension` [organizational policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).
  * `REGION`: Optional. Specify the region of the [regional Security Token Service endpoints](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#sts-regional-endpoints), if they are available.
  * `FILEPATH`: The file to save the configuration to.
  * `TOKEN_FILEPATH`: The path where OIDC ID tokens are stored.
  * `SOURCE_TYPE`: The format of the OIDC ID token file, set to `text` (default) or `json`.
  * `FIELD_NAME`: The field in the text file that contains the token (if `SOURCE_TYPE` is `json`).



###  URL-sourced credentials 
    
    
    gcloud iam workload-identity-pools create-cred-config \
        projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/WORKLOAD_PROVIDER_ID \
        --service-account=SERVICE_ACCOUNT_EMAIL \
        --service-account-token-lifetime-seconds=SERVICE_ACCOUNT_TOKEN_LIFETIME \
        --sts-location=REGION \
        --output-file=FILEPATH.json \
        --credential-source-url="TOKEN_URL" \
        --credential-source-headers="KEY_1=VALUE_1,KEY_2=VALUE_2" \
        --credential-source-type=SOURCE_TYPE \
        --credential-source-field-name=FIELD_NAME

Replace the following:

  * `PROJECT_NUMBER`: Project number of the project that contains the workload identity pool.
  * `POOL_ID`: ID of the workload identity pool.
  * `WORKLOAD_PROVIDER_ID`: ID of the workload identity pool provider
  * `SERVICE_ACCOUNT_EMAIL`: If you use service account impersonation, replace with the mail address of the service account. Omit this flag if you don't use service account impersonation.
  * `SERVICE_ACCOUNT_TOKEN_LIFETIME`: If you use service account impersonation, replace with the lifetime of the service account access token, in seconds; this defaults to one hour when not provided. Omit this flag if you don't use service account impersonation. To specify a lifetime longer than one hour, you must configure the `constraints/iam.allowServiceAccountCredentialLifetimeExtension` [organizational policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).
  * `REGION`: Optional. Specify the region of the [regional Security Token Service endpoints](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation#sts-regional-endpoints), if they are available.
  * `FILEPATH`: File to save the configuration to.
  * `TOKEN_URL`: URL to retrieve OIDC ID token from
  * `KEY_n`, `VALUE_n`: Custom headers to include in HTTP request to `TOKEN_URL`
  * `SOURCE_TYPE`: Format of the OIDC ID token file, set to `text` (default) or `json`
  * `FIELD_NAME`: Field in the text file that contains the token (if `SOURCE_TYPE` is `json`)



### Use the credential configuration to access Google Cloud

To let tools and client libraries use your credential configuration, do the following:

  1. Initialize an environment variable `GOOGLE_APPLICATION_CREDENTIALS` and point it to the credential configuration file:

#### Bash
         
         export GOOGLE_APPLICATION_CREDENTIALS=`pwd`/FILEPATH.json
           

where `FILEPATH` is the relative path to the credential configuration file. 

#### PowerShell
         
         $env:GOOGLE_APPLICATION_CREDENTIALS = Resolve-Path 'FILEPATH.json'
           

where `FILEPATH` is the relative path to the credential configuration file. 

  2. Use a client library or tool that supports Workload Identity Federation and can [find credentials automatically](https://docs.cloud.google.com/docs/authentication/application-default-credentials):

###  C++ 

The [Google Cloud Client Libraries for C++](https://docs.cloud.google.com/cpp/docs) support Workload Identity Federation since version [v2.6.0](https://github.com/googleapis/google-cloud-cpp/releases/tag/v2.6.0). To use Workload Identity Federation, you must build the client libraries with version 1.36.0 or later of gRPC.

###  Go 

Client libraries for Go support Workload Identity Federation if they use version v0.0.0-20210218202405-ba52d332ba99 or later of the `golang.org/x/oauth2` module.

To check which version of this module your client library uses, run the following commands:
         
         cd $GOPATH/src/cloud.google.com/go
         go list -m golang.org/x/oauth2
         

###  Java 

Client libraries for Java support Workload Identity Federation if they use version 0.24.0 or later of the [`com.google.auth:google-auth-library-oauth2-http` artifact](https://search.maven.org/artifact/com.google.auth/google-auth-library-oauth2-http).

To check which version of this artifact your client library uses, run the following Maven command in your application directory:
         
         mvn dependency:list -DincludeArtifactIds=google-auth-library-oauth2-http
         

###  Node.js 

Client libraries for Node.js support Workload Identity Federation if they use version 7.0.2 or later of the [`google-auth-library` package](https://github.com/googleapis/google-auth-library-nodejs).

To check which version of this package your client library uses, run the following command in your application directory:
         
         npm list google-auth-library
         

When you create a `GoogleAuth` object, you can specify a project ID, or you can allow `GoogleAuth` to find the project ID automatically. To find the project ID automatically, the service account in the configuration file must have the Browser role (`roles/browser`), or a role with equivalent permissions, on your project. For details, see the [`README` for the `google-auth-library` package](https://github.com/googleapis/google-auth-library-nodejs#using-external-identities).

###  Python 

Client libraries for Python support Workload Identity Federation if they use version 1.27.0 or later of the [`google-auth` package](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth).

To check which version of this package your client library uses, run the following command in the environment where the package is installed:
         
         pip show google-auth
         

To specify a project ID for the authentication client, you can set the `GOOGLE_CLOUD_PROJECT` environment variable, or you can allow the client to find the project ID automatically. To find the project ID automatically, the service account in the configuration file must have the Browser role (`roles/browser`), or a role with equivalent permissions, on your project. For details, see the [user guide for the `google-auth` package](https://github.com/googleapis/google-cloud-python/blob/main/packages/google-auth/docs/user-guide.rst#using-external-identities).

###  gcloud 

To authenticate using Workload Identity Federation, use the [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command:
         
         gcloud auth login --cred-file=FILEPATH.json
         

Replace `FILEPATH` with the path to the credential configuration file.

Support for Workload Identity Federation in gcloud CLI is available in [version 363.0.0 and later versions of the gcloud CLI](https://docs.cloud.google.com/sdk/docs/components#updating_components).

###  Terraform 

The [Google Cloud provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs) supports Workload Identity Federation if you use version 3.61.0 or later:
         
         terraform {
           required_providers {
             google = {
               source  = "hashicorp/google"
               version = "~> 3.61.0"
             }
           }
         }
         

###  bq 

To authenticate using Workload Identity Federation, use the [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command, as follows:
         
         gcloud auth login --cred-file=FILEPATH.json
         

Replace `FILEPATH` with the path to the credential configuration file.

Support for Workload Identity Federation in bq is available in [version 390.0.0 and later versions of the gcloud CLI](https://docs.cloud.google.com/sdk/docs/components#updating_components).




## What's next

  * Read more about [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation).
  * Learn about [best practices for using Workload Identity Federation](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation).
  * See how you can [manage workload identity pools and providers](https://docs.cloud.google.com/iam/docs/manage-workload-identity-pools-providers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
