---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/oidc-adfs/
title: Authenticating with OIDC and AD FS \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:11:16.696896+00:00
---

# Authenticating with OIDC and AD FS  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/oidc-adfs/

**Version 1.7**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.7 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/overview)



Send feedback 

#  Authenticating with OIDC and AD FS Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to configure Google Distributed Cloud to use [OpenID Connect (OIDC)](https://developers.google.com/identity/protocols/OpenIDConnect) with [Active Directory Federation Services (AD FS)](https://docs.microsoft.com/windows-server/identity/active-directory-federation-services) for authentication to user clusters. This page covers the process in general to help you understand how to configure an AD FS server as your OpenID provider with Active Directory as the user database.

For an overview of the Google Distributed Cloud authentication flow, see [Authentication](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/concepts/authentication). To learn how to configure OIDC with other OpenID providers, see the following resources:

  * [Authenticating with OpenID Connect (OIDC)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/oidc)
  * [Authenticating with OIDC and Google](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/oidc-google)



Google Distributed Cloud supports OIDC as one of the authentication mechanisms for interacting with a user cluster's Kubernetes API server. With OIDC, you can manage access to Kubernetes clusters by using the standard procedures in your organization for creating, enabling, and disabling user accounts.

There are two ways that users can authorize their accounts:

  * Use the Google Cloud CLI to initiate the OIDC flow and obtain user authorization through a browser-based consent page.

  * Use the Google Cloud console to initiate the OIDC authentication flow.




## Before you begin

  * This topic assumes that you are familiar with the following authentication and OpenID concepts:

    * [OAuth 2.0](https://oauth.net/2/)
    * [OpenID Connect](https://openid.net/connect/)
    * [scopes](https://openid.net/specs/openid-connect-core-1_0.html#ScopeClaims)
    * [claims](https://openid.net/specs/openid-connect-core-1_0.html#IDToken)
  * You must have an existing AD FS server and Active Directory user database to complete the steps in this section.

  * OIDC is supported only in AD FS version 2016 and later.

  * You should be aware of the following behaviors in AD FS:

    * In AD FS versions prior to 5.0, the `Token-Groups Qualified Names` LDAP attribute in your Active Directory database is mapped to the `groups` claim. In 5.0 and later, the attribute is `Token-Groups Qualified by Domain name`.

    * The AD FS server returns tokens that include the user's ID, the issuer ID, the `openid` claim and `groups` claim. The `groups` (`Group` in 5.0) claim lists the security groups in which the user belongs.

  * Headless systems are unsupported. A browser-based authentication flow is used to prompt you for consent and authorize your user account.

  * To authenticate through the Google Cloud console, each cluster that you want to configure for OIDC authentication must be [registered with Google Cloud](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster).




## Personas

This topic refers to three personas:

  * **Organization administrator.** This person chooses an OpenID provider and registers client applications with the provider.

  * **Cluster administrator.** This person creates one or more user clusters and creates authentication configuration files for developers who use the clusters.

  * **Developer.** This person runs workloads on one or more clusters and uses OIDC to authenticate.




## Creating redirect URLs

This section is for organization administrators.

You must create redirect URLs for both the gcloud CLI and Google Cloud console that the OpenID provider can use to return ID tokens.

### gcloud CLI redirect URL

Google Cloud CLI is installed on each developer's local machine and includes the gcloud CLI. You can specify a port number greater than 1024 to use for the redirect URL:
    
    
    http://localhost:PORT/callback
    

Replace `PORT` with your port number.

When you configure your AD FS server, specify `http://localhost:PORT/callback` as one of your redirect URLs.

### Google Cloud console redirect URL

The redirect URL for the Google Cloud console is:
    
    
    https://console.cloud.google.com/kubernetes/oidc

When you configure your AD FS server, specify `https://console.cloud.google.com/kubernetes/oidc` as one of your redirect URLs.

## Configuring AD FS

This section is for organization administrators.

Use a set of AD FS management wizards to configure your AD FS server and Active Directory user database:

  1. Open the AD FS management pane.

  2. Select **Application Groups** > **Actions** > **Add an Application Group**.

  3. Select **Server Application**. Enter a name and description of your choice. Click **Next**.

  4. Enter your two redirect URLs. You are given a client ID. This is how the AD FS server identifies the gcloud CLI and the Google Cloud console. Save the client ID for later.

  5. Select **Generate a shared secret**. The gcloud CLI and the Google Cloud console use this secret to authenticate to the AD FS server. Save the secret for later.




### Configuring security groups (optional)

This section is for organization administrators.

  1. In AD FS management, select **Relying party trusts** > **Add a new relying party trust**.

  2. Select **Claims aware** , and click **Start**.

  3. Select **Enter data about relying party manually**.

  4. Enter a display name.

  5. Skip the next two steps.

  6. Enter a Relying party trust identifier. Suggestion: `token-groups-claim`.

  7. For **Access control policy** , select **Permit everyone**. This means that all users share their security group information with the gcloud CLI and the Google Cloud console.

  8. Click **Finish**.




### Mapping LDAP attributes to claim names

This section is for organization administrators.

  1. In AD FS management, select **Relying party trusts** > **Edit claim issuance policy**.

  2. Select **Send LDAP Attributes as Claims** , and click **Next**.

  3. For **Claim rule name** , enter `groups`.

  4. For **Attribute store** , select **Active Directory**.

  5. In the table, for **LDAP Attribute** , select:

     * AD FS version 5.0 and later: **Token-Groups Qualified by Domain name**
     * AD FS versions before 5.0: **Token Groups - Qualified Names**
  6. For **Outgoing Claim Type** , select:

     * AD FS version 5.0 and later: **Group**
     * AD FS versions before 5.0: **groups**
  7. Click **Finish** , and click **Apply**.




### Registering the gcloud CLI and Google Cloud console with AD FS

This section is for organization administrators.

Open a PowerShell window in Administrator mode, and enter this command:
    
    
    Grant-AdfsApplicationPermission `
         -ClientRoleIdentifier "CLIENT_ID" `
         -ServerRoleIdentifier SERVER_ROLE_IDENTIFIER `
         -ScopeName "allatclaims", "openid"
    

Replace the following:

  * `CLIENT_ID`: the client ID that you obtained previously

  * `SERVER_ROLE_IDENTIFIER`: the claim identifier that you entered previously; the suggested identifier was `token-groups-claim`




## Configuring `oidc` on Google Distributed Cloud clusters

This section is for cluster administrators.

To configure OIDC authentication, you need to configure your user cluster's ClientConfig CRD with authentication details for a cluster. To do this, edit the KRM default object of type `clientconfig` in the `kube-public` namespace.
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG -n kube-public edit clientconfig default
    

Details from the ClientConfig CRD are used to configure OIDC for both the Google Cloud console and the Authentication plugin for GKE Enterprise. The configuration includes the following OIDC information:
    
    
    authentication:
      - name: NAME_STRING
        oidc:
          certificateAuthorityData: CERTIFICATE_STRING
          clientID: CLIENT_ID
          clientSecret: CLIENT_SECRET
          cloudConsoleRedirectURI: "https://console.cloud.google.com/kubernetes/oidc"
          deployCloudConsoleProxy: PROXY_BOOLEAN
          extraParams: EXTRA_PARAMS
          groupsClaim: GROUPS_CLAIM
          groupPrefix: GROUP_PREFIX
          issuerURI: ISSUER_URI
          kubectlRedirectURI: KUBECTL_REDIRECT_URI
          scopes: SCOPES
          userClaim: USER_CLAIM
          userPrefix: USER_PREFIX
        proxy: PROXY_URL
    

The following table describes the fields of the ClientConfig CRD `oidc` object.

Field | Required | Description | Format  
---|---|---|---  
name | yes | The name of the OIDC configuration to create. | String  
certificateAuthorityData | No | A `base64`-encoded [ PEM-encoded certificate](https://wikipedia.org/wiki/Privacy-Enhanced_Mail) for the OIDC provider. To create the string, encode the certificate, including headers, into `base64`. Include the resulting string in `certificateAuthorityData` as a single line.Example:  
`certificateAuthorityData: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tC...k1JSUN2RENDQWFT==` | String  
clientID | Yes | ID for the client application that makes authentication requests to the OpenID provider. | String  
clientSecret | No | Shared secret between the OIDC client application and the OIDC provider. | String  
extraParams | No |  Additional key-value parameters to send to the OpenID provider. If you are authorizing a group, pass in `resource=token-groups-claim`. If your authorization server prompts for consent for authentication with Microsoft Azure and Okta, set `extraParams` to `prompt=consent`. For Cloud Identity, set `extraParams` to `prompt=consent,access_type=offline`.  | Comma-delimited list  
groupsClaim | No | [JWT](https://tools.ietf.org/html/rfc7519) claim that the provider uses to return your security groups. | String  
groupPrefix | No | Prefix prepended to group claims to prevent clashes with existing names. For example, if you have two groups named `foobar`, add a prefix `gid-`. The resulting group is `gid-foobar`. | String  
issuerURI | Yes | URL where authorization requests are sent to your OpenID, such as `https://example.com/adfs`. The Kubernetes API server uses this URL to discover public keys for verifying tokens. The URI must use HTTPS. | URL String  
cloudConsoleRedirectURI | Yes | The redirect URL that `Google Cloud console` uses for authorization. The value should be `https://console.cloud.google.com/kubernetes/oidc`. | URL String  
kubectlRedirectURI | Yes | The redirect URL that `kubectl` uses for authorization. | URL String  
scopes | Yes | Additional scopes to send to the OpenID provider. Microsoft Azure and Okta require the `offline_access` scope. | Comma-delimited list  
userClaim | Yes | JWT claim to use as the username. You can choose other claims, such as email or name, depending on the OpenID provider. However, claims other than email are prefixed with the issuer URL to prevent naming clashes. | String  
userPrefix | No | Prefix prepended to username claims to prevent clashes with existing names. If you do not provide this field, and `userClaim` is a value other than `email`, the prefix defaults to `issuerurl#`. You can use the value `-` to disable all prefixing. | String  
proxy | No | Proxy server to use for the `auth` method, if applicable. For example: `http://user:password@10.10.10.10:8888`.`` | String  
  
### Example: Authorizing users and groups

Many providers encode user-identifying properties, such as email and user IDs, in a token. However, these properties have implicit risks for authentication policies:

  * User IDs can make policies difficult to read and audit.

  * Emails can create both an availability risk (if a user changes their primary email) and potentially a security risk (if an email can be re-assigned).




Therefore, it's a best practice to use group policies because a group ID can be both persistent and easier to audit.

Suppose that your provider creates identity tokens that include the following fields:
    
    
    {
      'iss': 'https://server.example.com'
      'sub': 'u98523-4509823'
      'groupList': ['developers@example.corp', 'us-east1-cluster-admins@example.corp']
      ...
    }
    

Given this token format, you would populate your configuration file's `oidc` specification like the following:
    
    
    issuerURL: 'https://server.example.com'
    username: 'sub'
    usernamePrefix: 'uid-'
    group: 'groupList'
    groupPrefix: 'gid-'
    extraParams: 'resource=token-groups-claim'
    ...
    

After you create the user cluster, you could then use Kubernetes role-based access control (RBAC) to grant privileged access to the authenticated users. For example, you could create a `ClusterRole` that grants its users read-only access to the cluster's Secrets, and create a `ClusterRoleBinding` resource to bind the role to the authenticated group:

### ClusterRole
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: secret-reader
    rules:
    - apiGroups: [""]
      # The resource type for which access is granted
      resources: ["secrets"]
      # The permissions granted by the ClusterRole
      verbs: ["get", "watch", "list"]

### ClusterRoleBinding
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: read-secrets-admins
    subjects:
      # Allows anyone in the "us-east1-cluster-admins" group to
      # read Secrets in any namespace within this cluster.
    - kind: Group
      name: gid-us-east1-cluster-admins # Name is case sensitive
      apiGroup: rbac.authorization.k8s.io
      # Allows this specific user to read Secrets in any
      # namespace within this cluster
    - kind: User
      name: uid-u98523-4509823
      apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: ClusterRole
      name: secret-reader
      apiGroup: rbac.authorization.k8s.io

Note that the Kubernetes API server treats a backslash as an escape character. Therefore, if the name of the user or group contains a double backslash (`\\`), the API server will read it as a single `\` when parsing the field value. To ensure that the API server correctly interprets a `\\` in a text field, you must replace it with `\\\\`. For example, the Kubernetes API server will parse

`"unique_name": "EXAMPLE\\\\cluster-developer"` as

`"unique_name": "EXAMPLE\\cluster-developer"`.

## Creating and distributing the authentication configuration file

This section is for cluster administrators.

After you create a user cluster, you create an authentication configuration file for that cluster. You can configure multiple clusters in a single authentication configuration file. You must provide each authentication configuration file to the users who want to authenticate with each of those clusters.

### Creating the authentication configuration file

To create the authentication configuration file in the current directory, run the following `gkectl` command:
    
    
    gkectl create-login-config --kubeconfig USER_CLUSTER_KUBECONFIG

Replace `USER_CLUSTER_KUBECONFIG` with the path of your user cluster's `kubeconfig` file. When you ran `gkectl create cluster` to create your user cluster, your [`kubeconfig` file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig) was created.

Result: Your authentication configuration file, named `kubectl-anthos-config.yaml`, is created in the current directory.

### Adding multiple clusters to the authentication configuration file

You can store the authentication configuration details for multiple clusters within a single authentication configuration file.

You can use the following command to merge additional user cluster authentication details into an existing authentication configuration file. Given an existing authentication configuration file, you can either merge or combine additional user cluster authentication details:

  * Merge the additional user cluster authentication details into that existing authentication configuration file.
  * Combine the additional user cluster authentication details into a new file.



For example, you might need to manage both the `anthos-config-1cluster.yaml` and `anthos-config-3clusters.yaml` authentication configuration files to accommodate the access needs of the multiple user groups in your organization.

To add additional user clusters to your existing authentication configuration file:

  1. Ensure that each cluster has a unique name. If your clusters have the same names, you cannot combine them into the same authentication configuration file. Note that after a cluster is created, that cluster cannot be renamed.

  2. Run the following `gkectl` command to merge or combine configuration details:
         
         gkectl create-login-config --kubeconfig USER_CLUSTER_KUBECONFIG \
         --merge-from IN_AUTH_CONFIG_FILE --output OUT_AUTH_CONFIG_FILE

Replace the following:

     * `USER_CLUSTER_KUBECONFIG` specifies the `kubeconfig` file of the user cluster that you want to add.

     * `IN_AUTH_CONFIG_FILE` specifies the path of the existing authentication configuration file that you want to merge with the additional cluster information.

     * `OUT_AUTH_CONFIG_FILE` specifies the path of the file where you want to store the merged authentication configuration:

       * Specify the same file as `IN_AUTH_CONFIG_FILE` to merge the additional cluster information into that existing file.
       * Specify a new path and filename to combine the authentication configuration details into a new file.



### Distributing the authentication configuration file

To enable your users to authenticate against your user clusters, you must provide them with access to one or more of the authentication configuration files that you created. Note that the following steps use the default file name and the location that are expected by the gcloud CLI. For information about using alternate file names and locations, see Custom configuration.

Consider distributing the authentication configuration files by:

  * Hosting the file at an accessible URL. If you include the `--login-config` flag in the `gcloud anthos auth login` command, the gcloud CLI obtains the authentication configuration file from that location.

Consider hosting the file on a secure host. See the `--login-config-cert` flag of the gcloud CLI for more information about using PEM certificates for secure HTTPS access.

  * Manually providing the file to each user. After users download the file, you must instruct them about how to store the file in the default location and with the default filename that the gcloud CLI expects.

For example, users can run the following commands to store the authentication configuration file with the default `kubectl-anthos-config.yaml` filename and in the default location:

### Linux
        
        mkdir -p  $HOME/.config/google/anthos/
        cp AUTH_CONFIG_FILE $HOME/.config/google/anthos/kubectl-anthos-config.yaml

where `AUTH_CONFIG_FILE` is the name of your authentication configuration file. For example `kubectl-anthos-config.yaml`.

### macOS
        
        mkdir -p  $HOME/Library/Preferences/google/anthos/
        cp AUTH_CONFIG_FILE $HOME/Library/Preferences/google/anthos/kubectl-anthos-config.yaml

where `AUTH_CONFIG_FILE` is the name of your authentication configuration file. For example `kubectl-anthos-config.yaml`.

### Windows
        
        md "%APPDATA%\google\anthos"
        copy AUTH_CONFIG_FILE "%APPDATA%\google\anthos\kubectl-anthos-config.yaml"

where `AUTH_CONFIG_FILE` is the name of your authentication configuration file. For example `kubectl-anthos-config.yaml`.

  * Using your internal tools to push the authentication configuration file onto each user's machine. For example, you could use your tooling to push files using the default `kubectl-anthos-config.yaml` filename into their default locations on each user's machine:

### Linux
        
        $HOME/.config/google/anthos/kubectl-anthos-config.yaml

### macOS
        
        $HOME/Library/Preferences/google/anthos/kubectl-anthos-config.yaml

### Windows
        
        %APPDATA%\google\anthos\kubectl-anthos-config.yaml




### Custom configuration

The gcloud CLI expects the authentication configuration file to be stored in the default location and with the default filename `kubectl-anthos-config.yaml` as mentioned in the prior section. However, you have the option to rename or store your authentication configuration file in an alternate location. If the file's name and location differ from the default, you must append the `--login-config` flag to each command that you run when you authenticate with the cluster. The extra command flag passes in the custom path and filename. To learn more about the command flag, see Authenticating through the gcloud CLI.

## Installing the gcloud CLI

This section is for both cluster administrators and developers.

Each developer or user who needs to authenticate with a cluster, must install Google Cloud CLI on their own machine. The Anthos authentication commands have been integrated into the gcloud CLI as the `anthos-auth` [component](https://docs.cloud.google.com/sdk/docs/components).

  * If you have an old version of "Anthos Plugin for Kubectl", you must uninstall that plugin before installing the gcloud CLI and `anthos-auth` component.

  * If you have an existing version of the gcloud CLI, install the latest version and the `anthos-auth` component.




### Removing old plugins

You must uninstall the old plugin before you can use the `anthos-auth` component of gcloud CLI. You can check whether one of the past `kubectl` based plugins exists on your machine by running the following command:
    
    
    kubectl anthos version

  * If the command responds with `Error: unknown command "anthos" for "kubectl"`, no plugin was found and you can skip to the next section.

  * If a `1.0beta` version of the plugin was found, you must locate the plugin binary and delete it. Run the following command to list the location and then use that location to remove the binary from your machine:
        
        kubectl plugin list




### Installing gcloud CLI and the gcloud CLI

To install the gcloud CLI you must first first install gcloud CLI:

**Important:** Using gcloud CLI with Google Distributed Cloud does not require you to have a Google account. If you have an account, sign in is optional but you do not need to run the `gcloud init` command.

  1. [Install gcloud CLI](https://docs.cloud.google.com/sdk/docs/install) but skip the `gcloud init` command.

  2. Run the following commands to install the `anthos-auth` component:
         
         gcloud components update
         gcloud components install anthos-auth

  3. Verify that the gcloud CLI was installed successfully by running either of the following commands:
         
         gcloud anthos auth
         gcloud anthos auth login

Result: Each command should respond with details about the required arguments and available options.




## Obtaining the authentication configuration file

This section is for developers.

Your administrator is responsible for creating your authentication configuration file and then providing it to you. For more details, see Distributing the authentication configuration file.

By default, the gcloud CLI uses a default filename and storage location for your authentication configuration file. If you were manually provided the file and need to save it on your machine, use the defaults to simplify your `gcloud` authentication commands.

Use the following commands to copy the authentication configuration file to the default location:

### Linux
    
    
    mkdir -p  $HOME/.config/google/anthos/
    cp AUTH_CONFIG_FILE $HOME/.config/google/anthos/kubectl-anthos-config.yaml

where `AUTH_CONFIG_FILE` is the name of your authentication configuration file. For example `kubectl-anthos-config.yaml`.

### macOS
    
    
    mkdir -p  $HOME/Library/Preferences/google/anthos/
    cp AUTH_CONFIG_FILE $HOME/Library/Preferences/google/anthos/kubectl-anthos-config.yaml

where `AUTH_CONFIG_FILE` is the name of your authentication configuration file. For example `kubectl-anthos-config.yaml`.

### Windows
    
    
    md "%APPDATA%\google\anthos"
    copy AUTH_CONFIG_FILE "%APPDATA%\google\anthos\kubectl-anthos-config.yaml"

where `AUTH_CONFIG_FILE` is the name of your authentication configuration file. For example `kubectl-anthos-config.yaml`.

If you choose to use a different filename or location, you have the option to include the `--login-config` flag with each of your authentication requests. See the following section for details about using the `gcloud anthos auth login` command.

## Authenticating with user clusters

This section is for developers.

Now that gcloud CLI is installed on your machine and the authentication configuration file has been provided to you by your administrator, you can use either the gcloud CLI or the Google Cloud console to authenticate with your clusters.

### Authenticating through the gcloud CLI

Run `gcloud` commands to authenticate with your clusters:

  1. Run the `gcloud anthos auth login` command to initiate the authentication flow:
         
         gcloud anthos auth login \
          --cluster CLUSTER_NAME \
          --user USER_NAME \
          --login-config AUTH_CONFIG_FILE_PATH \
          --login-config-cert CA_CERT_PEM_FILE \
          --kubeconfig USER_CLUSTER_KUBECONFIG

where:

     * `CLUSTER_NAME` (optional) specifies the name of your user cluster. If this flag is omitted, you are prompted to choose from the user clusters that are specified in your authentication configuration file.

     * `USER_NAME` (optional) specifies the username for the credentials stored in the `kubeconfig` file. The default value is ``CLUSTER_NAME`-anthos-default-user`.

     * `AUTH_CONFIG_FILE_PATH` (optional) specifies the custom path or URL to where your authentication configuration file is stored or hosted. You can omit this parameter, if the file is in the default location. Example: `--login-config /path/to/custom/authentication-config.yaml`

     * `CA_CERT_PEM_FILE` (optional) specifies the path to a PEM certificate file from your CA. If your authentication configuration file is hosted securely, you can use an HTTPS connection to access the file. Example: `--login-config-cert my-cert.pem`

     * `USER_CLUSTER_KUBECONFIG` (optional) specifies the custom path to your user cluster's `kubeconfig` file. The OIDC ID tokens that are returned by your OpenID provider are stored in the `kubeconfig` file.

Use this flag if your `kubeconfig` file resides in a location other than the [default](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig). If this flag is omitted, a new `kubeconfig` file is created in the default location. Example: `--kubeconfig /path/to/custom.kubeconfig`

**Examples** :

     * Authenticate to specific cluster:
           
           gcloud anthos auth login --cluster my-production-cluster
           

     * Use a prompt to select which cluster to authenticate with:
           
           gcloud anthos auth login
           

Result:
           
           Please use the --cluster flag to specify a cluster from the list below:
           Source: $HOME/.config/google/anthos/kubectl-anthos-config.yaml
           1. Cluster: test-cluster ServerIP: https://192.168.0.1:6443
           2. Cluster: test-cluster-2 ServerIP: https://192.168.0.2:6443
           3. Cluster: my-production-cluster ServerIP: https://192.168.0.3:6443
           

     * Use a hosted authentication configuration file:
           
           gcloud anthos auth login \
            --cluster my-production-cluster \
            --login-config HTTPS://my-secure-server/kubectl-anthos-config.yaml \
            --login-config-cert my-cert.pem
           

  2. Enter your credentials in the browser-based consent screen that opens.

  3. Verify that authentication was successful by running one of the `kubectl` commands to retrieve details about your cluster. For example:
         
         kubectl get nodes --kubeconfig USER_CLUSTER_KUBECONFIG




Result: Your `kubeconfig` file now contains an ID token that your `kubectl` commands will use to authenticate with the Kubernetes API server on your user cluster.

### Using SSH to authenticate from a remote machine

Suppose you want to SSH into a remote machine and authenticate to a user cluster from the remote machine. To do this, your authentication configuration file must be on the remote machine, and you must be able to reach your Open ID provider from your local machine.

On your local machine, run the following command:
    
    
    ssh USER_NAME@REMOTE_MACHINE -L LOCAL_PORT:localhost:REMOTE_PORT
    

where:

  * `USER_NAME` and `REMOTE_MACHINE` are the standard values used to log in with SSH.

  * `LOCAL_PORT` is an open port of your choice on your local machine that you will use to access the remote machine.

  * `REMOTE_PORT` is the port you configured for your OIDC redirect URL. You can find this in the `kubectlRedirectURI` field of your authentication configuration file.




In your SSH shell, run the following command to initiate authentication:
    
    
    gcloud anthos auth login --login-config AUTH_CONFIG_FILE
    

where `AUTH_CONFIG_FILE` is the path of your authentication configuration file on the remote machine.

On your local machine, in a browser, go to http://localhost:`LOCAL_PORT`/login and complete the OIDC login flow.

Now the kubeconfig file on your remote machine has the token that you need to access the user cluster.

In your SSH shell, verify that you have access to the user cluster:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get nodes
    

### Authenticating through the Google Cloud console

Initiate the authentication flow from the Kubernetes clusters page in the Google Cloud console:

  1. Open the Google Cloud console:

[Visit the Kubernetes clusters page](https://console.cloud.google.com/kubernetes/list)

  2. Locate your Google Distributed Cloud cluster in the list and then click **Login**.

  3. Select **Authenticate with the Identity Provider configured for the cluster** , and then click **LOGIN**.

You are redirected to your identity provider, where you might need to log in or consent to the Google Cloud console accessing your account. Then you are redirected back to the **Kubernetes clusters** page in the Google Cloud console.




## Troubleshooting your OIDC configuration

Review the following behaviors and errors to help resolve your OIDC issues:

Invalid configuration
    If Google Cloud console cannot read the OIDC configuration from your cluster, the **LOGIN** button will be disabled.
Invalid provider configuration
    If your identity provider configuration is invalid, you will see an error screen from your identity provider after you click **LOGIN**. Follow the provider-specific instructions to correctly configure the provider or your cluster.
Invalid permissions
    If you complete the authentication flow, but still don't see the details of the cluster, make sure you granted the correct RBAC permissions to the account that you used with OIDC. Note that this might be a different account from the one you use to access Google Cloud console.
`Error: missing 'RefreshToken' field in 'OAuth2Token' in credentials struct`
    You might get this error if the authorization server prompts for consent, but the required authentication parameter wasn't provided. Provide the `prompt=consent` parameter to Google Distributed Cloud configuration file's `oidc: extraparams` field, and regenerate the client authentication file with the `--extra-params prompt=consent` flag.

## What's next

  * Learn more about [scopes and claims](https://developer.okta.com/blog/2017/07/25/oidc-primer-part-1#key-concepts-scopes-claims-and-response-types).

  * Learn about [custom claims in ID tokens](https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/development/custom-id-tokens-in-ad-fs).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
