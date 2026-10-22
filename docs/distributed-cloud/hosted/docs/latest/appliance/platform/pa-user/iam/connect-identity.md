---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/connect-identity/
title: Connect an existing identity provider \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:58.517069+00:00
---

# Connect an existing identity provider  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/connect-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Connect an existing identity provider Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect Google Distributed Cloud (GDC) air-gapped appliance to your organization's existing identity provider (IdP). An IdP is a system that centrally manages and secures user identities, providing authentication services. Connecting to an existing IdP lets users access GDC using their organization's credentials, without needing to create or manage separate accounts within GDC. This process ensures a seamless and secure login experience. Since an IdP is a global resource, users can access GDC through the same IdP regardless of the zone they work in.

After the initial identity provider is set up and connected to an identity provider, you can connect additional existing identity providers using the GDC console.

You can connect to an existing identity provider using one of the following:

  * OpenID Connect (OIDC)
  * Security Assertion Markup Language (SAML)



## Before you begin

Before you connect to an existing identity provider, you must ensure the initial setup is complete, request the necessary permissions, and prepare your environment.

### Initial identity provider connection setup

A member of your organization's infrastructure operator group must configure the initial IdP connection before users can access GDC clusters or dashboards. They can do so by opening a ticket in the ticketing system and providing the required identity provider information.

### Request IAM roles

To create, read, update, and delete identity provider configurations, contact your Organization IAM Admin to request the **IdP Federation Admin** (`idp-federation-admin`) role.

Ensure that the initial admin you specify when connecting the identity provider has the **Organization IAM Admin** (`organization-iam-admin`) role.

### Prepare your environment

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * Install the `kubectl` CLI, as described in [Install components](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install#install-components).

  * [Generate a kubeconfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auth#get-kubeconfig) to configure `kubectl` access.




## Connect to an existing identity provider

To connect the identity provider, you must have a single client ID and secret from your identity provider. You can either connect to an existing OIDC or a SAML provider using the console.

### Connect to an existing OIDC provider

  1. Sign in to the GDC console. The following example shows the console after signing into an organization called `org-1`: ![Console welcome page with
quick access links to common tasks.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/images/login.png)
  2. In the navigation menu, click **Identity and Access > Identity**. ![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/images/identityAndAccess.png)
  3. Click **Setup New Identity Provider**. ![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/images/newIdentityProvider.png)
  4. In the **Configure identity provider** section, complete the following steps and click **Next** : ![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/images/selectIdentityProviderOIDC.png)

     1. In the **Identity provider** list, select **Open ID Connect (OIDC)**.
     2. Enter an **Identity provider name**.
     3. In the **Google Distributed Cloud URL** field, enter the URL you use to access GDC.
     4. In the **Issuer URI** field, enter the URL where authorization requests are sent to your identity provider. The Kubernetes API server uses this URL to discover public keys for verifying tokens. The URL must use HTTPS.
     5. In the **Client ID** field, enter the ID for the client application that makes authentication requests to the identity provider. 
        1. In the **Client secret** section, select **Configure client secret (Recommended)**.
        2. In the **Client secret** field, enter the client secret, which is a shared secret between your identity provider and GDC air-gapped appliance.
     6. Optional: In the **Prefix** field, enter a prefix. The prefix is the **Identity provider prefix** field, enter a prefix. The prefix is added to the beginning of user claims and group claims. Prefixes are used to distinguish between different identity provider configurations. For example, if you set a prefix of `myidp`, a user claim might be `myidpusername@example.com` and a group claim might be `myidpgroup@example.com`. The prefix must also be included when assigning role-based access control (RBAC) permissions to groups.

**Note:** GDC air-gapped appliance doesn't insert a separator between the prefix and the group name. Insert a separator such as - or : at the end of the prefix to increase readability. Otherwise `prefix` and `kiran@example.com` are identified as `prefixkiran@example.com`.
     7. Optional: In the **Encryption** section, select **Enable encrypted tokens**.

To enable encryption tokens, you must have the IdP Federation Admin role. Ask your Organization IAM Admin to grant you the IdP Federation Admin (`idp-federation-admin`) role.

        1. In the **Key ID** field, enter your key ID. The key ID is a public key of a JSON web encryption token (JWT). Your OIDC provider sets up and provisions a key ID.
        2. In the **Decryption key** field, enter the decryption key in PEM format. The decryption key is an asymmetric key that decrypts an encryption. Your OIDC provider sets up and provisions a decryption key. 
  5. In the **Configure attributes** section, complete the following steps and click **Next** : ![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/images/configureAttributesOIDC.png)

     1. In the **Certificate authority for OIDC provider** field, enter a base64-encoded PEM-encoded certificate for the identity provider. For more information, see <https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail>. 
        1. To create the string, encode the certificate, including headers, into `base64`.
        2. Include the resulting string in as a single line. Example: `LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tC...k1JSUN2RENDQWFT==`
     2. In the **Group claim** field, enter the name of the claim in the identity provider token that holds the user's group information.
     3. In the **User claim** field, enter the claim to identify each user. The default claim for many providers is `sub`. You can choose other claims, such as `email` or `name`, depending on the identity provider. Claims other than `email` are prefixed with the issuer URL to prevent naming clashes.
     4. Optional: If your identity provider uses GKE Identity Service, in the Custom attributes section, click **Add** and enter key-value pairs for additional claims about a user, such as their department or profile picture URL.
     5. If your identity provider requires additional scopes, in the **Scopes** field, enter the comma-separated scopes to send to the identity provider. For example, Microsoft Azure and Okta require the `offline_access` scope.
     6. In the **Extra parameters** section, enter any additional key-value pairs (comma-separated) required by your identity provider. If you are authorizing a group, pass in `resource=token-groups-claim`. If your authorization server prompts for consent for authentication with Microsoft Azure and Okta, set `prompt=consent`. For Cloud Identity, set `prompt=consent,access_type=offline`.
  6. In the **Specify initial admins** section, complete the following steps and click **Next** : ![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/images/specifyInitialAdmins.png)

     1. Choose whether to add individual users or groups as initial administrators.
     2. In the **Username or group alias** field, enter the user or group email address to access the organization. If you are the administrator, enter your email address for example `sally@example.com`. The prefix is added before the user name, such as `myidp-sally@example.com`.
  7. Review your selections and click **Setup**.




The new identity provider profile is available in the Identity profiles list.

### Connect to an existing SAML provider

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Identity and Access > Identity**.
  3. In the **Configure identity provider** section, complete the following steps and click **Next** : ![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/images/selectIdentityProviderSAML.png)

     1. In the **Identity provider** drop-down menu, select **Security Assertion Markup Language (SAML)**.
     2. Enter an **Identity provider name**.
     3. In the **Identity ID** field, enter the ID for the client application that makes authentication requests to the identity provider.
     4. In the **SSO URI** field, enter the URL to the single sign on endpoint of the provider. For example: `https://www.idp.com/saml/sso`.
     5. In the **Identity provider prefix** field, enter a prefix. The prefix is added to the beginning of user and group claims. Prefixes distinguish between different identity provider configurations. For example: If you set a prefix of `myidp`, a user claim might show as `myidpusername@example.com` and a group claim might show as `myidpgroup@example.com`. You must also include the prefix when assigning RBAC permissions to groups.

**Note:** GDC air-gapped appliance doesn't insert a separator between the prefix and the group name. Insert a separator such as **-** or **:** at the end of the prefix to increase readability. Otherwise `prefix` and `kiran@example.com` are identified as `prefixkiran@example.com`.
     6. Optional: In the **SAML Assertions** section, select **Enable encrypted SAML assertions**.

To enable encrypted SAML assertions, you must have the IdP Federation Admin role. Ask your Organization IAM Admin to grant you the IdP Federation Admin (`idp-federation-admin`) role.

        1. In the **Encryption certificate** field, enter your encryption certificate in PEM format. You receive your encryption certificate after generating the SAML provider.
        2. In the **Decryption key** field, enter your decryption key. You receive your decryption key after generating the SAML provider.
     7. Optional: In the **SAML Signed requests** section, check **Enable signed SAML requests**.

        1. In the **Signing certificate** field, enter your signing certificate in the PEM file format. Your SAML provider sets up and produces you a signing certificate.
        2. In the **Signing key** field, enter your signing key in the PEM file format. Your SAML provider sets up and produces you a signing key. 
  4. In the **Configure attributes** page, complete the following steps and click **Next** : ![](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/images/configureAttributesSAML.png)

     1. In the **IDP certificate** field, enter a base64-encoded PEM-encoded certificate for the identity provider. For more information, see <https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail>. 
        1. To create the string, encode the certificate, including headers, into `base64`.
        2. Include the resulting string in as a single line. For example: `LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tC...k1JSUN2RENDQWFT==`.
     2. Enter any additional certificates in the field **Additional IDP certificate**.
     3. In the **User attribute** field, enter the attribute to identify each user. The default attribute for many providers is `sub`. You can choose other attributes, such as `email` or `name`, depending on the identity provider. Attributes other than `email` are prefixed with the issuer URL to prevent naming clashes.
     4. In the **Group attribute** field, enter the name of the attribute in the identity provider token that holds the user's group information.
     5. Optional: If your identity provider uses GKE Identity Service, in the **Attribute mapping** area, click **Add** and enter key-value pairs for additional attributes about a user, such as their department or profile picture URL.
  5. In the **Specify initial admins** section, complete the following steps and click **Next** :

     1. Choose whether to add individual users or groups as initial administrators.
     2. In the **Username** field, enter the user or group email address to access the organization. If you are the administrator, enter your email address for example `kiran@example.com`. The prefix is added before the user name, such as `myidp-kiran@example.com`.
  6. In the **Review** page, check all the values of each identity configuration before continuing. Click **Back** to return to the previous pages and make necessary corrections. When you've configured all values to your specification, click **Setup**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
