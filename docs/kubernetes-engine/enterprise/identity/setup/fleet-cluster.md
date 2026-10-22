---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet-cluster/
title: Set up fleet-level authentication management \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:29.901800+00:00
---

# Set up fleet-level authentication management  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Set up fleet-level authentication management Stay organized with collections  Save and categorize content based on your preferences. 

This document shows clusters administrators how to set up multiple clusters for authentication from third-party identity providers by using [fleets](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs). Google Cloud manages the configuration of clusters in a fleet, which results in a faster, less complex setup process than setting up individual clusters. For more information about the third-party provider authentication process, see [About authentication using third-party identities](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity).

## Before you begin

  1. Install and configure the Google Cloud CLI:

     1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

     2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

     3. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
            
            gcloud init

  2. After initializing the gcloud CLI, update it and install the required components: 
         
         gcloud components update
         gcloud components install kubectl

  3. In the gcloud CLI, select your fleet host project: 
         
         gcloud config set project FLEET_HOST_PROJECT_ID

Replace `FLEET_HOST_PROJECT_ID` with the project ID of your fleet host project. 


* Enable the required APIs:

  1. In the Google Cloud console, go to the project selector page:

[Go to project selector](https://console.cloud.google.com/projectselector2/)

  2. Select your fleet host project.

  3. Enable the GKE Hub and Kubernetes Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=gkehub.googleapis.com,container.googleapis.com&redirect=https%3A//console.cloud.google.com)



* Ensure that your platform administrator has given you all of the provider information that you need for your selected protocol. For more information, see the following documents:

  * [Configure OIDC providers to authenticate to clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider)
  * [Configure SAML providers to authenticate to clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/saml-provider)
  * [Configure LDAP providers to authenticate to clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider-ldap)



### Required roles

To get the permissions that you need to set up clusters at the fleet level, ask your administrator to grant you the [Fleet Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`) IAM role on the fleet host project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable the fleet-level identity service feature

The fleet-level identity service feature uses a controller to manage the configuration in each of the clusters in the fleet. You need to enable the fleet-level feature only in the fleet host project.

To enable the fleet-level feature, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **GKE Identity Service** page.

[Go to GKE Identity Service](https://console.cloud.google.com/kubernetes/identityservice)

  2. Click **Enable Identity Service**.




###  gcloud 

Enable the fleet-level identity service feature:
    
    
    gcloud container fleet identity-service enable
    

## Configure clusters

To configure your clusters, you must specify the following information:

  * Information about your identity provider, such as a client ID and a secret.
  * Information about the JSON Web Tokens (JWTs) that your identity provider uses for authentication.
  * Any additional scopes or parameters that are unique to your identity provider.



For more information about the information that you need from your platform administrator, or whoever manages identity in your organization, see the following documents:

  * [Configure OIDC providers to authenticate to clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider)
  * [Configure SAML providers to authenticate to clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/saml-provider)
  * [Configure LDAP providers to authenticate to clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider-ldap)



If you have existing cluster-level configurations for OIDC providers, applying a fleet-level configuration to the cluster overwrites all your existing authentication specifications. Additionally, if you have existing cluster-level configurations for providers that are not supported for fleet-level configuration, this setup will fail. You must remove the existing provider configuration to apply the fleet-level configuration.

To configure your clusters, follow these steps:

### Console

  1. Select clusters to configure:

     1. In the Google Cloud console, go to the **GKE Identity Service** page.

[Go to Feature Manager](https://console.cloud.google.com/kubernetes/identityservice)

     2. Select one or more checkboxes for the clusters that you want to configure. You can choose individual clusters, or specify that you want all clusters to be configured with the same identity configuration. If you have configured [fleet-level defaults](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet-cluster#configure-fleet), the configuration is reconciled back to the default.

     3. Click **Update Configuration**. The **Edit Identity Service Clusters Config** pane opens.

     4. In the **Identity Providers** section, choose how you want to configure the clusters. You can update an existing configuration, copy a configuration from a different cluster, or create a new configuration. To create a new configuration, click **Add an Identity Provider**. The **New Identity Provider** section appears.

  2. In the **New Identity Provider** section, set the provider details:

### OIDC

     1. Select **New Open ID Connect** to create a new OIDC configuration.
     2. Specify the name you want to use to identify this configuration in the **Provider name** field, typically the identity provider name. This name must start with a letter followed by up to 39 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. You cannot edit this name once you've created a configuration.
     3. Specify the client ID from the identity provider in the **Client ID** field.
     4. Specify the client secret that must be shared between the client application and the identity provider in the **Client Secret** field.
     5. Specify the URI where authorization requests are made to your identity provider in the **Issuer URL** field.
     6. Click **Next** to set the OIDC attributes.

### Azure AD

     1. Select **New Azure Active Directory** to create a new Azure AD configuration.
     2. Specify the name you want to use to identify this configuration in the **Provider name** field, typically the identity provider name. This name must start with a letter followed by up to 39 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. You cannot edit this name once you've created a configuration.
     3. Specify the client ID from the identity provider in the **Client ID** field.
     4. Specify the client secret that must be shared between the client application and the identity provider in the **Client Secret** field.
     5. Specify the tenant that is the Azure AD account to be authenticated in the **Tenant**.
     6. Click **Next** to set the Azure AD attributes.

### LDAP

     1. Select **LDAP** to create a new LDAP configuration.
     2. Specify the name you want to use to identify this configuration in the **Provider name** field, typically the identity provider name. This name must start with a letter followed by up to 39 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. You cannot edit this name once you've created a configuration.
     3. Click **Next**.
     4. Specify the hostname (mandatory), LDAP connection type, and base64-encoded CA certificate of the LDAP server.
     5. Click **Next** to configure the server.
     6. Specify the user's distinguished name, filter, login attribute, and identifier attribute.
     7. Click **Next** to set the user details.
     8. If you choose to use groups, specify the group's distinguished name, filter, and identifier attribute.
     9. Click **Next** to set the group details.
     10. Specify the service account username and password.
     11. Click **Done** to set the service account name.

  3. Click **Next**. The **Set attributes** section opens.

  4. Set the attributes for your identity provider. To view attributes for OIDC or Azure AD, select one of the following options:

### OIDC

     * **`kubectl` redirect URI**: The redirect URL and port used by the gcloud CLI and specified by your platform administrator at registration, typically in the form `http://localhost:PORT/callback`.
     * **Certificate Authority** (Optional): If provided by your platform administrator, a PEM-encoded certificate string for the identity provider.
     * **Group Claim** (Optional): The JWT claim (field name) that your provider uses to return an account's security groups.
     * **Group Prefix** (Optional): The prefix you want to prepend to security group names to avoid clashes with existing names in your access control rules if you have configurations for multiple identity providers (typically the provider name).
     * **Proxy** (Optional): Proxy server address to use to connect to the identity provider, if applicable. You might need to set this if, for example, your cluster is in a private network and needs to connect to a public identity provider. For example: `http://user:password@10.10.10.10:8888`.
     * **Scopes** (Optional): Any additional scopes required by your identity provider. Microsoft Azure and Okta require the `offline_access` scope. Click **Add scope** to add more scopes if necessary.
     * **User Claim** (Optional): The JWT claim (field name) that your provider uses to identify an account. If you don't specify a value here, the cluster uses "sub", which is the user ID claim used by many providers. You can choose other claims, such as "email" or "name", depending on the OpenID provider. Claims other than "email" are prefixed with the issuer URL to prevent naming clashes.
     * **User Prefix** (Optional): The prefix you want prepended to user claims to prevent clashes with existing names, if you don't want to use the default prefix.
     * **Extra Params** (Optional): Any extra parameters required for your configuration, specified as the parameter **Key** and **Value**. Click **Add param** to add more parameters if needed.
     * **Enable access token** (Optional): If enabled, it allows group support for OIDC providers such as Okta.
     * **Deploy Google Cloud console proxy** (Optional): If enabled, a proxy is deployed that lets the Google Cloud console connect to an on-premises identity provider that is not publicly accessible over the internet.

### Azure AD

     * **`kubectl` redirect URI**: The redirect URL and port used by the gcloud CLI and specified by your platform administrator at registration, typically in the form `http://localhost:PORT/callback`.
     * **User Claim** (Optional): The JWT claim (field name) that your provider uses to identify an account. If you don't specify a value here, the cluster uses a value in the order of "email", "preferred_username", or "sub" to fetch the user details.
     * **Proxy** (Optional): Proxy server address to use to connect to the identity provider, if applicable. You might need to set this if, for example, your cluster is in a private network and needs to connect to a public identity provider. For example: `http://user:password@10.10.10.10:8888`.

  5. Click **Done**.

  6. Optional: To add more providers to the configuration, click **Add an identity provider** and repeat the preceding steps.

  7. Click **Update configuration**.




This installs any required components if necessary and applies the client configuration on your selected clusters.

### gcloud

To use the gcloud CLI to configure the fleet, you create a Kubernetes [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) named ClientConfig with fields for all of the information that the cluster needs to interact with the identity provider. To create and use a ClientConfig, follow these steps:

  1. Create a ClientConfig specification in a file named `auth-config.yaml`. To view example configurations for OIDC, SAML, or LDAP, select one of the following options. For other identity provider configurations, see Provider-specific configurations.

### OIDC

The following example ClientConfig shows both an `oidc` configuration and an `azuread` configuration. For more information about when to use `oidc` or `azuread`, see Provider-specific configurations.
         
         apiVersion: authentication.gke.io/v2alpha1
         kind: ClientConfig
         metadata:
           name: default
           namespace: kube-public
         spec:
           authentication:
           - name: NAME
             proxy: PROXY_URL
             oidc:
               certificateAuthorityData: CERTIFICATE_STRING
               clientID: CLIENT_ID
               clientSecret: CLIENT_SECRET
               deployCloudConsoleProxy: PROXY_BOOLEAN
               extraParams: EXTRA_PARAMS
               groupsClaim: GROUPS_CLAIM
               groupPrefix: GROUP_PREFIX
               issuerURI: ISSUER_URI
               kubectlRedirectURI: http://localhost:PORT/callback
               scopes: SCOPES
               userClaim: USER_CLAIM
               userPrefix: USER_PREFIX
           - name: azure
             azureAD:
               clientID: CLIENT_ID
               clientSecret: CLIENT_SECRET
               tenant: TENANT_UUID
               kubectlRedirectURI: http://localhost:PORT/callback
               groupFormat: GROUP_FORMAT
               userClaim: USER_CLAIM
         

For more information about the fields in the `oidc` object, see [ClientConfig OIDC fields](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/per-cluster#clientconfig-oidc-fields).

### SAML

The following example ClientConfig shows a `saml` configuration:
         
         apiVersion: authentication.gke.io/v2alpha1
             kind: ClientConfig
             metadata:
               name: default
               namespace: kube-public
             spec:
               authentication:
               - name: NAME
                 saml:
                   idpEntityID: ENTITY_ID
                   idpSingleSignOnURI: SIGN_ON_URI
                   idpCertificateDataList: IDP_CA_CERT
                   userAttribute: USER_ATTRIBUTE
                   groupsAttribute: GROUPS_ATTRIBUTE
                   userPrefix: USER_PREFIX
                   groupPrefix: GROUP_PREFIX
                   attributeMapping:
                     ATTRIBUTE_KEY_1 : ATTRIBUTE_CEL_EXPRESSION_1
                     ATTRIBUTE_KEY_2 : ATTRIBUTE_CEL_EXPRESSION_2
                 certificateAuthorityData: CERTIFICATE_STRING
                 preferredAuthentication: PREFERRED_AUTHENTICATION
                 server: <>
         

For more information about these fields, see [ClientConfig SAML fields](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/saml-per-cluster#clientconfig-saml-fields).

### LDAP

The following example ClientConfig shows an `ldap` configuration:
         
         apiVersion: authentication.gke.io/v2alpha1
         kind: ClientConfig
         metadata:
           name: default
           namespace: kube-public
         spec:
           authentication:
           - name: ldap
             ldap:
               server:
                 host: HOST_NAME
                 connectionType: CONNECTION_TYPE
                 certificateAuthorityData: CERTIFICATE_AUTHORITY_DATA
               user:
                 baseDn: BASE_DN
                 loginAttribute: LOGIN_ATTRIBUTE
                 filter: FILTER
                 identifierAttribute: IDENTIFIER_ATTRIBUTE
               group:
                 baseDn: BASE_DN
                 filter: FILTER
                 identifierAttribute: IDENTIFIER_ATTRIBUTE
               serviceAccount:
                 simpleBindCredentials:
                   dn: DISTINGUISHED_NAME
                   password: PASSWORD
         

For more information about these fields, see [ClientConfig LDAP fields](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/ldap#clientconfig-ldap-fields).

You can add multiple identity provider configurations to the same ClientConfig. The cluster attempts to authenticate with each configuration in the order in which they are defined, and stops after the first successful authentication.

  2. Apply the ClientConfig to a cluster:
         
         gcloud container fleet identity-service apply \
             --membership=CLUSTER_NAME \
             --config=auth-config.yaml
         

Replace `CLUSTER_NAME` with your cluster's unique name within the fleet.




The cluster installs any required components and uses the ClientConfig that you created. The fleet-level controller manages the configuration for the cluster. Any local changes to the cluster configuration are reconciled by the controller to the fleet-level configuration.

For some cluster versions, applying your fleet-level configuration also by default adds an additional `authentication` configuration to your clusters. This lets the cluster retrieve Google Groups information for user accounts logging in with their [Google ID](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway). This configuration is applicable to clusters on Google Distributed Cloud (both [VMware](https://docs.cloud.google.com/vmware-engine/docs/overview) and [bare metal](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)). For more information about the Google Groups feature, see [Set up the connect gateway with Google Groups](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup-groups).

If you no longer want the fleet-level controller to manage your configuration, for example if you want to use a different authentication option or options, you can disable this feature by following the instructions in [Disabling fleet-level identity management](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/manage-fleet-clusters).

### Provider-specific configurations

This section provides configuration guidance for OIDC providers (such as Azure AD and Okta), including an example configuration that you can copy and edit with your own details.

### Azure AD

This is the default configuration to set up authentication with Azure AD. Using this configuration lets the cluster get user and group information from Azure AD, and lets you set up [Kubernetes role based access control (RBAC)](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access#optional_set_up_role-based_access_control_rbac) based on groups. However, using this configuration limits you to retrieving approximately 200 groups per user.

If you need to retrieve more than 200 groups per user, see the instructions for **Azure AD (Advanced)**.
    
    
    ...
    spec:
      authentication:
      - name: oidc-azuread
        oidc:
          clientID: CLIENT_ID
          clientSecret: CLIENT_SECRET
          cloudConsoleRedirectURI: https://console.cloud.google.com/kubernetes/oidc
          extraParams: prompt=consent, access_type=offline
          issuerURI: https://login.microsoftonline.com/TENANT_ID/v2.0
          kubectlRedirectURI: http://localhost:PORT/callback
          scopes: openid,email,offline_access
          userClaim: email
    
    # Rest of the resource is managed by Google. DO NOT MODIFY.
    ...
    

### Azure AD (Advanced)

This optional configuration for Azure AD lets the cluster retrieve user and group information with no limit on the number of groups per user, using the Microsoft Graph API. For information on platforms that support this configuration, see [Identity provider setup information](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider#microsoft-entra-id).

If you need to retrieve fewer than 200 groups per user, we recommend that you use the default configuration using an `oidc` anchor in your ClientConfig. For more information, see the instructions for **Azure AD**.

All fields in the example configuration are required.
    
    
    ...
    spec:
      authentication:
      - name: azure
        azureAD:
          clientID: CLIENT_ID
          clientSecret: CLIENT_SECRET
          tenant: TENANT_UUID
          kubectlRedirectURI: http://localhost:PORT/callback
          groupFormat: GROUP_FORMAT
          userClaim: USER_CLAIM
    
    # Rest of the resource is managed by Google. DO NOT MODIFY.
    ...
    

Replace GROUP_FORMAT with the format in which you want to retrieve group information. This field can take values corresponding to `ID` or `NAME` of the user groups. This setting is only available for clusters in Google Distributed Cloud (on-premises) deployments.

### Okta

The following shows you how to set up authentication using both users and groups with Okta as your identity provider. This config lets the cluster retrieve user and group claims by using an access token and Okta's userinfo endpoint.

**Note:** While this configuration is for Okta, you can also retrieve user and group information from any other identity provider that supports a userinfo endpoint. In your config, specify `enableAccessToken: true` to use this feature.
    
    
    ...
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
    
    # Rest of the resource is managed by Google. DO NOT MODIFY.
    ...
    

### Configure fleet-level defaults

You can specify a fleet-level default configuration for authentication. Using this setup, every new cluster that you [register to the fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation) automatically uses the authentication configuration you specify.

Existing fleet member clusters aren't automatically updated when you specify a fleet-level default configuration. You can optionally apply your default configuration to those clusters. For more information about managing fleet-level configuration, see [Manage fleet-level features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/manage-features).

After you set a fleet-level default, any local changes to the authentication configuration of individual clusters are overwritten when the fleet controller reconciles the cluster with the default configuration.

To configure a fleet-level default configuration, do the following:

  1. Create a ClientConfig in a file named `fleet-default.yaml`. For more information about how to create the file, see the gcloud CLI steps in the Configure clusters section.
  2. To apply the fleet-level default configuration, run one of the following commands:

     * If the fleet-level identity service feature isn't enabled, enable the feature and specify the fleet-level default configuration:
           
           gcloud container fleet identity-service enable --fleet-default-member-config=fleet-default.yaml

     * If the fleet-level identity service feature is enabled, apply the new fleet-level default configuration:
           
           gcloud container fleet identity-service apply --fleet-default-member-config=default-config.yaml

New clusters that you register to the fleet use this configuration by default. Existing fleet member clusters don't automatically inherit the new default configuration.

  3. To apply the default configuration to an existing fleet member cluster, run the following command:
         
         gcloud container fleet identity-service apply --origin=fleet --membership=CLUSTER_NAME




#### Remove the fleet-level default configuration

To remove the default configuration, run the following command:
    
    
    gcloud container fleet identity-service delete --fleet-default-member-config

New clusters that you register to the fleet don't automatically use an authentication configuration.

## Verify the identity service configuration

After you complete the fleet-level setup, you can verify if the clusters in your fleet have been successfully configured with the identity service configuration that you specified.

### Console

  1. In the Google Cloud console, go to the **Feature Manager** page.

[Go to Feature Manager](https://console.cloud.google.com/kubernetes/features/overview)

All enabled features are listed as **Enabled** in their panel.

  2. Click **DETAILS** in the **Identity Service** panel. A details panel displays the status of your registered clusters.




### gcloud

Run the following command:
    
    
    gcloud container fleet identity-service describe
    

## What's next

After you have configured the clusters, continue to [set up user access](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
