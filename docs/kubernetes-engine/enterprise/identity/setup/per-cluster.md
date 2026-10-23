---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/per-cluster/
title: Set up fleet member clusters for OIDC authentication \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:17.394909+00:00
---

# Set up fleet member clusters for OIDC authentication  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/per-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Set up fleet member clusters for OIDC authentication Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how cluster administrators or application operators can configure clusters to support authentication using a third-party [OpenID Connect (OIDC)](https://openid.net/connect/) provider.

## Limitations

You must use a [cluster type that supports OIDC](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity#supported_cluster_types).

## Before you begin

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  4. After initializing the gcloud CLI, update it and install the required components: 
         
         gcloud components update
         gcloud components install kubectl

  5. Ensure that your platform administrator has given you all of the provider information that you need. For more information, see [Share the identity provider details](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider#share_the_identity_provider_details).
  6. To authenticate by using the Google Cloud console, register each cluster that you want to configure to your project fleet. For more information, see [Fleet creation overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#clusters_outside).
  7. To connect to an AWS or Azure cluster's control plane that is outside your current VPC network through a bastion host, make sure that you have created the bastion host and started an SSH tunnel at port `8118`. When you run `kubectl` commands in this document, prepend the commands with `HTTPS_PROXY=http://localhost:PORT`, where `PORT` is the port number that you used when you started the SSH tunnel.
  8. For GKE clusters on Google Cloud, [register the clusters to your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke).



## Configure clusters

To configure authentication to a cluster using OIDC, you add the following information to a Kubernetes [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) named ClientConfig:

  * Information about your identity provider, such as a client ID and a secret.
  * Information about the JSON Web Tokens (JWTs) that your identity provider uses for authentication.
  * Any additional scopes or parameters that are unique to your identity provider.



For more information about the information that you need from your platform administrator, or whoever manages identity in your organization, see [Share the identity provider details](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider#share_the_identity_provider_details).

The cluster uses the fields in the ClientConfig custom resource to interact with your identity provider. Every cluster has a ClientConfig named `default` in the `kube-public` namespace. The specific fields that you modify depend on your identity provider.

To edit the `default` ClientConfig, make sure you can connect to your cluster `kubectl`, and then run the following command:
    
    
    kubectl --kubeconfig=KUBECONFIG_PATH edit ClientConfigs default -n kube-public
    

Replace `KUBECONFIG_PATH` with the path to your cluster's kubeconfig file—for example `$HOME/.kube/config`.

A text editor loads your cluster's ClientConfig resource. Add the `spec.authentication.oidc` object as show in the following sample. Don't modify any default data that has already been written.
    
    
    apiVersion: authentication.gke.io/v2alpha1
    kind: ClientConfig
    metadata:
      name: default
      namespace: kube-public
    spec:
      **authentication :
      - name: NAME
        oidc:
          certificateAuthorityData: CERTIFICATE_AUTHORITY_DATA
          clientID: CLIENT_ID
          clientSecret: CLIENT_SECRET
          deployCloudConsoleProxy: PROXY_BOOLEAN
          extraParams: EXTRA_PARAMS
          groupsClaim: GROUPS_CLAIM
          groupPrefix: GROUP_PREFIX
          issuerURI: ISSUER_URI
          kubectlRedirectURI: KUBECTL_REDIRECT_URI
          scopes: SCOPES
          userClaim: USER_CLAIM
          userPrefix: USER_PREFIX
          enableAccessToken: ENABLE_ACCESS_TOKEN
        proxy: PROXY_URL**
    # Rest of the resource is managed by Google. DO NOT MODIFY.
    

For example, consider the following identity token fields:
    
    
    {
      'iss': 'https://server.example.com'
      'sub': 'u98523-4509823'
      'groupList': ['developers@example.corp', 'us-east1-cluster-admins@example.corp']
      # Multiple lines are omitted here
    }
    

In this example, `iss` is the identity provider URI, `sub` identifies the user, and `groupList` lists the security groups that the user belongs to. This example shows only a sample of the fields that the actual token might have.

For the preceding example token, you update the following fields in the `spec.authentication.oidc` object of the ClientConfig:
    
    
    issuerURI: 'https://server.example.com'
    userClaim: 'sub'
    groupsClaim: 'groupList'
    # Multiple lines are omitted here
    

You can add multiple OIDC, LDAP, and SAML identity provider configurations to the same ClientConfig. The cluster attempts to authenticate with each configuration in the order in which they are defined, and stops after the first successful authentication. The following example ClientConfig defines multiple identity providers in a specific order:
    
    
    apiVersion: authentication.gke.io/v2alpha1
    kind: ClientConfig
    metadata:
      name: default
      namespace: kube-public
    spec:
      authentication:
      - aws:
          region: us-west-2
        name: AWS Login
      - ldap:
      # Multiple lines are omitted here.
      - saml:
      # Multiple lines are omitted here.
      - azureAD:
      # Multiple lines are omitted here.
      - oidc:
        name: Okta OIDC
      # Multiple lines are omitted here.
      - oidc:
        name: Google OIDC
      # Multiple lines are omitted here.
    

### ClientConfig OIDC fields

The following table describes the fields of the ClientConfig `oidc` object. The fields that you need to add depend on your identity provider tokens and how your platform administrator configured the provider.

Field | Required | Description | Format  
---|---|---|---  
name | yes | The name you want to use to identify this configuration, typically the identity provider name. A configuration name must start with a letter followed by up to 39 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. | String  
certificateAuthorityData | No | If provided by your platform administrator, a PEM-encoded certificate string for the identity provider. Include the resulting string in `certificateAuthorityData` as a single line. | String  
clientID | Yes | The client ID from the identity provider. | String  
clientSecret | No | Shared secret between the OIDC client application and the OIDC provider. | String  
deployCloudConsoleProxy | No | Specifies whether a proxy is deployed that lets the Google Cloud console connect to an on-premises identity provider that is not publicly accessible over the internet. By default this is set to `false`. | Boolean  
extraParams | No |  Additional key=value parameters to send to the identity provider, specified as a comma-separated list—for example `prompt=consent,access_type=offline`.  | Comma-delimited list  
groupsClaim | No | The JWT claim (field name) that your provider uses to return an account's security groups. | String  
groupPrefix | No | The prefix you want to prepend to security group names to avoid clashes with existing names in your access control rules if you have configurations for multiple identity providers (typically the provider name). | String  
issuerURI | Yes | The URI where authorization requests are made to your identity provider. The URI must use HTTPS and should not end with a trailing slash. | URL String  
kubectlRedirectURI | Yes | The redirect URL and port used by the gcloud CLI and specified by your platform admin at registration, typically in the form `http://localhost:PORT/callback`. | URL String  
scopes | Yes | Additional scopes to send to the OpenID provider. For example, Microsoft Azure and Okta require the `offline_access` scope. | Comma-delimited list  
userClaim | No | The JWT claim (field name) that your provider uses to identify a user account. If you don't specify a value here, the default value is "sub", which is the user ID claim used by many providers. You can choose other claims, such as "email" or "name", depending on the OpenID provider. Claims other than "email" are prefixed with the issuer URL to prevent naming clashes. | String  
userPrefix | No | The prefix you want prepended to user claims to prevent clashes with existing names, if you don't want to use the default prefix. | String  
enableAccessToken | No | If enabled, the cluster can use the identity provider's userinfo endpoint to get groups information when a user logs in from the command line. This lets you use security groups for authorization if you have a provider (such as Okta) that provides group claims from this endpoint. If not set, this is considered to be `false`. | Boolean  
proxy | No | Proxy server address to use to connect to the identity provider, if applicable. You might need to set this if, for example, your cluster is in a private network and needs to connect to a public identity provider. For example: `http://user:password@10.10.10.10:8888`. | String  
  
After you edit your ClientConfig, save the file to update the ClientConfig for your cluster. If you make any syntax errors, you see a prompt to fix those errors and save the file.

### Provider-specific configurations

This section provides configuration guidance for some popular OIDC providers, including example configurations that you can copy and edit with your own details.

**Caution:** You must use either the standard OIDC or the Microsoft Entra ID (Advanced) method. Don't apply both. These configurations are mutually exclusive. Attempting to use both simultaneously causes the standard OIDC plugin to override the Microsoft Entra ID (Advanced) plugin, which leads to authentication failures for users with more than 200 group memberships.

### Microsoft Entra ID

This is the default configuration to set up a cluster for authentication with Microsoft Entra ID. Using this configuration lets the cluster get user and group membership information from Microsoft Entra ID, and lets you set up [Kubernetes role based access control (RBAC)](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access#optional_set_up_role-based_access_control_rbac) based on groups. However, using this configuration limits you to retrieving approximately 200 groups per user.

If you need to retrieve more than 200 groups per user, see the instructions for **Microsoft Entra ID (Advanced)**.
    
    
    # Multiple lines are omitted here.
    spec:
      authentication:
      - name: oidc-entraid
        oidc:
          clientID: CLIENT_ID
          clientSecret: CLIENT_SECRET
          cloudConsoleRedirectURI: https://console.cloud.google.com/kubernetes/oidc
          extraParams: prompt=consent, access_type=offline
          issuerURI: https://login.microsoftonline.com/TENANT_ID/v2.0
          kubectlRedirectURI: http://localhost:PORT/callback
          scopes: openid,email,offline_access
          userClaim: email
    # Multiple lines are omitted here. Do not modify any pre-filled data.
    

Replace the following:

  * CLIENT_ID: The client ID from Microsoft Entra ID.
  * CLIENT_SECRET: Shared secret between the OIDC client application and the OIDC provider.
  * TENANT_ID: The kind of Microsoft Entra ID account to be authenticated. Supported values are the tenant ID, or the tenant name for accounts belonging to a specific tenant. The tenant name is also known as the _primary domain_. For details on how to find these values, see [Find the Microsoft Entra tenant ID and primary domain name](https://learn.microsoft.com/en-us/partner-center/account-settings/find-ids-and-domain-names#find-the-microsoft-azure-ad-tenant-id-and-primary-domain-name).
  * PORT: The port number chosen for the redirect URL used by the gcloud CLI, specified by your platform administrator at registration.



### Microsoft Entra ID (Advanced)

This optional configuration for Microsoft Entra ID lets the cluster retrieve user and group information with no limit on the number of groups per user, using the Microsoft Graph API.

For information on platforms that support this configuration, see [Advanced setup for Microsoft Entra ID](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider#advancedsetupforAzureAD).

If you need to retrieve fewer than 200 groups per user, we recommend that you use the default configuration using an `oidc` anchor in your ClientConfig. For more information, see the instructions for **Microsoft Entra ID**.

All fields in the following example configuration are required.
    
    
    # Multiple lines are omitted here.
    spec:
      authentication:
      - name: NAME
        proxy: PROXY_URL
        azureAD:
          clientID: CLIENT_ID
          clientSecret: CLIENT_SECRET
          tenant: TENANT_ID
          kubectlRedirectURI: http://localhost:PORT/callback
          groupFormat: GROUP_FORMAT
          userClaim: USER_CLAIM
    # Multiple lines are omitted here. Do not modify any pre-filled data.
    

Replace the following:

  * NAME: The name you want to use to identify this configuration, typically the identity provider name. A configuration name must start with a letter followed by up to 39 lowercase letters, numbers, or hyphens, and cannot end with a hyphen.
  * PROXY_URL: Proxy server address to use to connect to the identity provider, if applicable. You might need to set this if, for example, your cluster is in a private network and needs to connect to a public identity provider. For example: `http://user:password@10.10.10.10:8888`.
  * CLIENT_ID: The client ID from Microsoft Entra ID.
  * CLIENT_SECRET: Shared secret between the OIDC client application and the OIDC provider.
  * TENANT: The kind of Microsoft Entra account to be authenticated. Supported values are the tenant ID, or the tenant name for accounts belonging to a specific tenant. The tenant name is also known as the _primary domain_. For details on how to find these values, see [Find the Microsoft Entra tenant ID and primary domain name](https://learn.microsoft.com/en-us/partner-center/account-settings/find-ids-and-domain-names#find-the-microsoft-azure-ad-tenant-id-and-primary-domain-name).
  * PORT: The port number chosen for the redirect URL used by the gcloud CLI, specified by your platform administrator at registration.
  * GROUP_FORMAT: The format in which you want to retrieve group information. This field can take values corresponding to `ID` or `NAME` of the user groups. Note that this setting is available only for clusters in bare metal Google Distributed Cloud deployments.
  * USER_CLAIM (Optional): The JWT claim (field name) that your provider uses to identify an account. If you don't specify a value here, the cluster uses a value in the order of "email", "preferred_username", or "sub" to fetch the user details. This attribute can be used from version 1.28.



### Okta

The following shows you how to set up authentication using both users and groups with Okta as your identity provider. This config lets the cluster retrieve user and group claims by using an access token and Okta's userinfo endpoint.

**Note:** While this configuration is for Okta, you can also retrieve user and group information from any other identity provider that supports a userinfo endpoint. In your config, specify `enableAccessToken: true` to use this feature.
    
    
    # Multiple lines are omitted here.
    spec:
      authentication:
      - name: okta
        oidc:
          clientID: CLIENT_ID
          clientSecret: CLIENT_SECRET
          cloudConsoleRedirectURI: https://console.cloud.google.com/kubernetes/oidc
          enableAccessToken: true
          extraParams: prompt=consent
          groupsClaim: groups
          issuerURI: https://OKTA_ISSUER_URI/
          kubectlRedirectURI: http://localhost:PORT/callback
          scopes: offline_access,email,profile,groups
          userClaim: email
    # Multiple lines are omitted here. Do not modify any pre-filled data.
    

#### Group access limits

For Okta users, the cluster can retrieve group information for users whose group names, if concatenated, have a length less than 170000 characters. This corresponds to a membership of approximately 650 groups given Okta's maximum group length. If the user is a member of too many groups, the authentication call fails.

## What's next?

After the configuration is applied, continue to [set up user access to clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
