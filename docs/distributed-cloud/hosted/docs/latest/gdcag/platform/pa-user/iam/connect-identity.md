---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/connect-identity/
title: Connect to an identity provider \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:37.624564+00:00
---

# Connect to an identity provider  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/connect-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Connect to an identity provider Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect Google Distributed Cloud (GDC) air-gapped to your organization's existing identity provider (IdP). An IdP is a system that centrally manages and secures user identities, providing authentication services. Connecting to an existing IdP lets users access GDC using their organization's credentials, without needing to create or manage separate accounts within GDC. This process ensures a seamless and secure login experience. Since an IdP is a global resource, users can access GDC through the same IdP regardless of the zone they work in.

This page is for audiences within the platform administrator group, such as IT admins or security engineers, who want to connect to an IdP. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

You can connect to an existing identity provider using one of the following:

  * OpenID Connect (OIDC)
  * Security Assertion Markup Language (SAML)



## Before you begin

Before you connect to an existing identity provider, you must ensure the initial setup is complete, request the necessary permissions, and prepare your environment.

### Initial identity provider connection setup

A member of your organization's infrastructure operator group must configure the initial IdP connection before users can access GDC clusters or dashboards.

They can do so by opening a ticket in the ticketing system and providing the required identity provider information. For more information, see [Connect the customer identity provider to the organization](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/infrastructure/io-operations-30/configure-org-pa#connect-customer-idp-to-org).

### Request IAM roles

To create, read, update, and delete identity provider configurations, contact your Organization IAM Admin to request the **IdP Federation Admin** (`idp-federation-admin`) role.

Ensure that the initial admin you specify when connecting the identity provider has the **Organization IAM Admin** (`organization-iam-admin`) role.

### Prepare your environment

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).

  * [Generate a kubeconfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#get-kubeconfig) to configure `kubectl` access.




## Connect to an existing identity provider

To connect the identity provider, you must have a single client ID and secret from your identity provider. You can either connect to an existing OIDC or a SAML provider.

### Connect to an existing OIDC provider

To connect to an existing OIDC provider, complete the following steps:

### Console

  1. Sign in to the GDC console. The following example shows the console after signing into an organization called `org-1`: ![Console welcome page with quick access links to common tasks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/images/login.png)
  2. In the navigation menu, click **Identity and Access > Identity**.
  3. Click **Add Identity Provider**.
  4. In the **Configure identity provider** section, complete the following steps:

     1. In the **Identity provider** drop-down menu, select **Open ID Connect (OIDC)**.
     2. Enter an **Identity provider name**.
     3. In the **Issuer URI** field, enter the URL where authorization requests are sent to your identity provider. The Kubernetes API server uses this URL to discover public keys for verifying tokens. The URL must use HTTPS.
     4. In the **Client ID** field, enter the ID for the client application that makes authentication requests to the identity provider.
     5. In the **Client Secret** field, enter the client secret, which is a shared secret between your identity provider and Distributed Cloud.
     6. Optional: In the **Identity provider prefix** field, enter a prefix. The prefix is added to the beginning of user claims and group claims. Prefixes are used to distinguish between different identity provider configurations. For example, if you set a prefix of `myidp`, a user claim might be `myidp-username@example.com` and a group claim might be `myidp-group@example.com`. The prefix must also be included when assigning role-based access control (RBAC) permissions to groups.

**Note:** Distributed Cloud doesn't insert a separator between the prefix and the group name. Insert a separator such as `-` or `:` at the end of the prefix to increase readability. Otherwise, `prefix` and `kiran@example.com` are identified as `prefixkiran@example.com`.
     7. Optional: In the **Encryption** section, select **Enable encryption tokens**.

To enable encryption tokens, ask your Organization IAM Admin to grant you the IdP Federation Admin (`idp-federation-admin`) role.

        1. In the **Key ID** field, enter your key ID. The key ID identifies the public key of a JSON web encryption (JWE) token. Your OIDC provider sets up and provisions a key ID.
        2. In the **Decryption key** field, enter the decryption key in PEM format. The decryption key is an asymmetric key used to decrypt tokens. Your OIDC provider sets up and provisions a decryption key.
     8. Click **Next**.

  5. In the **Configure attributes** section, complete the following steps:

     1. In the **Certificate authority for OIDC provider** field, enter a base64-encoded PEM-encoded certificate for the identity provider. For more information, see [Privacy-Enhanced Mail](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail) on Wikipedia. 
        1. To create the string, encode the certificate, including headers, into `base64`.
        2. Include the resulting string as a single line. Example: `LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tC...k1JSUN2RENDQWFT==`
     2. In the **Group Claim** field, enter the name of the claim in the identity provider token that holds the user's group information.
     3. In the **User Claim** field, enter the claim to identify each user. The default claim for many providers is `sub`. You can choose other claims, such as `email` or `name`, depending on the identity provider. Claims other than `email` are prefixed with the issuer URL to prevent naming clashes. 
     4. Optional: In the **Custom attributes** section, click **Add Pair** and enter key-value pairs for additional claims about a user, such as their department or profile picture URL.
     5. If your identity provider requires additional scopes, in the **Scopes** field, enter the comma-separated scopes to send to the identity provider.
     6. In the **Extra parameters** section, enter any additional key-value pairs (comma-separated) required by your identity provider. If you are authorizing a group, pass in `resource=token-groups-claim`.
     7. Click **Next**. 
  6. In the **Specify initial admins** section, complete the following steps:

     1. Choose whether to add individual users or groups as initial administrators.
     2. In the **Username or group alias** field, enter the user or group email address to access the organization. If you are the administrator, enter your email address, for example `kiran@example.com`. The prefix is added before the username, such as `myidp-kiran@example.com`.
     3. Click **Next**.
  7. Review your selections and click **Setup**.




The new identity provider profile is available in the Identity profiles list.

### API

To connect your identity provider to your organization, create the global `IdentityProviderConfig` custom resource.

  1. Create an `IdentityProviderConfig` custom resource YAML file, such as `pa-idp-oidc.yaml`:
         
         apiVersion: iam.global.gdc.goog/v1
         kind: IdentityProviderConfig
         metadata:
           name: pa-idp-oidc
           namespace: platform
         spec:
           oidc:
             certificateAuthorityData: "IDP_BASE64_ENCODED_CERTIFICATE"
             clientID: IDP_CLIENT_ID
             clientSecret: IDP_CLIENT_SECRET
             groupPrefix: IDP_GROUP_PREFIX
             groupsClaim: IDP_GROUP_CLAIM
             issuerURI: IDP_ISSUER_URI
             scopes: openid,email,profile
             userClaim: IDP_USER_CLAIM
             userPrefix: IDP_USER_PREFIX
         

Replace the following variables:

     * `IDP_BASE64_ENCODED_CERTIFICATE`: the base64-encoded certificate for the IdP.
     * `IDP_CLIENT_ID`: the client ID for the IdP.
     * `IDP_CLIENT_SECRET`: the client secret for the IdP.
     * `IDP_GROUP_PREFIX`: the prefix for groups in the IdP.
     * `IDP_GROUP_CLAIM`: the name of the claim in the IdP token that groups information.
     * `IDP_ISSUER_URI`: the issuer URI for the IdP.
     * `IDP_USER_CLAIM`: the name of the claim in the IdP token for the user.
     * `IDP_USER_PREFIX`: the prefix for the user IdP.
  2. Apply the `IdentityProviderConfig` custom resource to the global API server:
         
         kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG apply -f pa-idp-oidc.yaml
         

Replace the `GLOBAL_API_SERVER_KUBECONFIG` variable with the path to the kubeconfig file for the global API server.




### Connect to an existing SAML provider

To connect to an existing SAML provider, complete the following steps:

### Console

  1. Sign in to the GDC console. The following example shows the console after signing into an organization called `org-1`: ![Console welcome page with quick access links to common tasks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/images/login.png)
  2. In the navigation menu, click **Identity and Access > Identity**.
  3. Click **Add Identity Provider**.
  4. In the **Configure identity provider** section, complete the following steps:

     1. In the **Identity provider** drop-down menu, select **Security Assertion Markup Language (SAML)**.
     2. Enter an **Identity provider name**.
     3. In the **Identity ID** field, enter the ID for the client application that makes authentication requests to the identity provider.
     4. In the **SSO URI** field, enter the URL to the single sign-on endpoint of the provider. For example: `https://www.idp.com/saml/sso`.
     5. In the **Identity provider prefix** field, enter a prefix. The prefix is added to the beginning of user and group claims. Prefixes distinguish between different identity provider configurations. For example: If you set a prefix of `myidp`, a user claim might show as `myidp-username@example.com` and a group claim might show as `myidp-group@example.com`. You must also include the prefix when assigning RBAC permissions to groups.

**Note:** Distributed Cloud doesn't insert a separator between the prefix and the group name. Insert a separator such as `-` or `:` at the end of the prefix to increase readability. Otherwise `prefix` and `kiran@example.com` are identified as `prefixkiran@example.com`.
     6. For enhanced security, configure your SAML provider to issue assertions with a lifespan of 5 to 10 minutes. This setting is configurable within your SAML provider's settings.

     7. Optional: In the **SAML Assertions** section, select **Enable encryption SAML assertions**.

To enable encrypted SAML assertions, ask your Organization IAM Admin to grant you the IdP Federation Admin (`idp-federation-admin`) role.

        1. In the **Encryption assertion certificate** field, enter your encryption certificate in PEM format. You obtain your encryption certificate from your SAML provider.
        2. In the **Encryption assertion key** field, enter your private key. You receive your decryption key after generating the SAML provider.
     8. Optional: In the **SAML Signed Requests** section, select **Enable signed SAML requests**.

        1. In the **Signing certificate** field, enter your signing certificate in the PEM file format. Your SAML provider issues a signing certificate.
        2. In the **Signing key** field, enter your signing key in the PEM file format. Your SAML provider sets up and produces you a signing key.
     9. Click **Next**.

  5. In the **Configure attributes** page, complete the following steps:

     1. In the **IDP certificate** field, enter a base64-encoded PEM-encoded certificate for the identity provider. For more information, see [Privacy-Enhanced Mail](https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail) on Wikipedia. 
        1. To create the string, encode the certificate, including headers, into `base64`.
        2. Include the resulting string in as a single line. For example: `LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tC...k1JSUN2RENDQWFT==`.
     2. Enter any additional certificates in the **Additional IDP certificate** field.
     3. In the **User attribute** field, enter the attribute to identify each user. The default attribute for many providers is `sub`. You can choose other attributes, such as `email` or `name`, depending on the identity provider. Attributes other than `email` are prefixed with the issuer URL to prevent naming clashes.
     4. In the **Group attribute** field, enter the name of the attribute in the identity provider token that holds the user's group information. 
     5. Optional: In the **Attribute mapping** section, click **Add Pair** and enter key-value pairs for additional attributes about a user, such as their department or profile picture URL.
     6. Click **Next**. 
  6. In the **Specify initial admins** section, complete the following steps:

     1. Choose whether to add individual users or groups as initial administrators.
     2. In the **Username or group alias** field, enter the user or group email address to access the organization. If you are the administrator, enter your email address, for example `kiran@example.com`. The prefix is added before the username, such as `myidp-kiran@example.com`.
     3. Click **Next**.
  7. In the **Review** page, check all the values of each identity configuration before continuing.

Click **Back** to return to the previous pages and make necessary corrections.

  8. Click **Setup**.




The new identity provider profile is available in the Identity profiles list.

### API

To connect your identity provider to your organization, create the global `IdentityProviderConfig` custom resource.

  1. Create an `IdentityProviderConfig` custom resource YAML file, such as `pa-idp-saml.yaml`:
         
         apiVersion: iam.global.gdc.goog/v1
         kind: IdentityProviderConfig
         metadata:
           name: pa-idp-saml
           namespace: platform
         spec:
           saml:
             groupPrefix: IDP_GROUP_PREFIX
             groupsAttribute: IDP_GROUP_ATTRIBUTE
             idpCertificateDataList:
             - "IDP_BASE64_ENCODED_CERTIFICATE"
             idpEntityID: IDP_SAML_ENTITY_ID
             idpSingleSignOnURI: IDP_SAML_SSO_URI
             userAttribute: IDP_USER_ATTRIBUTE
             userPrefix: IDP_USER_PREFIX
         

Replace the following variables:

     * `IDP_GROUP_PREFIX`: the prefix for groups in the IdP.
     * `IDP_GROUP_ATTRIBUTE`: the attribute for groups in the IdP.
     * `IDP_BASE64_ENCODED_CERTIFICATE`: the base64-encoded certificate for the IdP.
     * `IDP_SAML_ENTITY_ID`: the URL or URI for uniquely identifying the IdP.
     * `IDP_SAML_SSO_URI`: the issuer URI for the IdP.
     * `IDP_USER_ATTRIBUTE`: the attribute for the IdP user, such as an email.
     * `IDP_USER_PREFIX`: the name of the claim in the IdP token for the user.
  2. Apply the `IdentityProviderConfig` custom resource to the global API server:
         
         kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG apply -f pa-idp-saml.yaml
         

Replace the `GLOBAL_API_SERVER_KUBECONFIG` variable with the path to the kubeconfig file for the global API server.




## Delete an existing identity provider

Delete an existing identity provider using the GDC console:

  1. Sign in to the GDC console.
  2. In the project selector, select the organization in which you want to delete the identity provider.
  3. In the navigation menu, click **Identity and Access > Identity**.
  4. Check the box next to the name of one or more identity providers.

A message appears with the number of identity providers you selected and a **Delete** button.

  5. Click **Delete**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
