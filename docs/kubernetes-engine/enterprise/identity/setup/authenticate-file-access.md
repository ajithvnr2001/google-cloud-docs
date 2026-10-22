---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/authenticate-file-access/
title: Log in using a configuration file \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:31.688282+00:00
---

# Log in using a configuration file  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/authenticate-file-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Log in using a configuration file Stay organized with collections  Save and categorize content based on your preferences. 

You can log in to configured clusters from the command line using a username and password from a third party identity provider. Follow the instructions in this page if your cluster administrator has chosen to share a login configuration file for you to use when authenticating with gcloud CLI. For more information on accessing clusters, see [Choose an access method to log in to clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/accessing). This document applies only to [supported cluster types](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity#supported_cluster_types).

## Login workflow

The following is the workflow that you can use to access configured clusters using a login configuration file. The exact flow depends on the type of identity provider used.

### OIDC workflow

With OIDC providers, a cluster administrator registers a client application for the identity provider and sets up each cluster. They can add fine-grained access control using [Kubernetes role-based access control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/), if required.

You can log in to clusters in the following ways:

#### Command line access

  1. Authenticate: Run the `gcloud anthos auth login` command and enter your OIDC login credentials. This retrieves an identity token from the provider.
  2. Update Kubeconfig: The retrieved token is automatically added to your kubeconfig file.
  3. Access cluster: Use `kubectl` to interact with your cluster. The cluster validates your token and authorize access.



#### Google Cloud console access

  1. Initiate login: When you log in from the Google Cloud console, you are redirected to the identity provider's login page.
  2. Authenticate: Enter your credentials and successfully log in.
  3. Access cluster: Return to the Google Cloud console to view and manage your cluster resources.



### LDAP workflow

With LDAP providers, a cluster administrator sets up each cluster, which includes the LDAP client credentials. Cluster administrators can add fine-grained access control using [Kubernetes role-based access control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/), if required.

**Command line access**

  1. Initiate login: Run the `gcloud anthos auth login` command and enter your LDAP login credentials.
  2. Token generation: the cluster queries the LDAP server, retrieves your user attributes, and packages these attributes into a short-lived token (STS). Your LDAP credentials are not stored locally.
  3. Kubeconfig update: The STS token is automatically added to your `kubeconfig` file.
  4. Cluster access: Use `kubectl` to interact with your cluster. The cluster validates your token and authorize access. By default, the token expires after one hour, requiring the user to log in again.



To authenticate to clusters from the command line, you need to run `gcloud` authentication commands, using a login configuration file provided by your cluster administrator.

## Get the configuration file

The gcloud CLI assumes a default filename and location on your local machine for your authentication configuration file. Your administrator might copy the file to your machine for you. If you are manually provided the file and need to save it on your machine yourself, use the defaults to simplify your `gcloud` authentication commands.

Use the following commands to copy the authentication configuration file to the default location:

### Linux
    
    
    mkdir -p  $HOME/.config/google/anthos/
    cp [AUTH_CONFIG_FILE] $HOME/.config/google/anthos/kubectl-anthos-config.yaml

where [AUTH_CONFIG_FILE] is the name of your authentication configuration file. For example `kubectl-anthos-config.yaml`.

### macOS
    
    
    mkdir -p  $HOME/Library/Preferences/google/anthos/
    cp [AUTH_CONFIG_FILE] $HOME/Library/Preferences/google/anthos/kubectl-anthos-config.yaml

where [AUTH_CONFIG_FILE] is the name of your authentication configuration file. For example `kubectl-anthos-config.yaml`.

### Windows
    
    
    md "%APPDATA%\google\anthos"
    copy [AUTH_CONFIG_FILE] "%APPDATA%\google\anthos\kubectl-anthos-config.yaml"

where [AUTH_CONFIG_FILE] is the name of your authentication configuration file. For example `kubectl-anthos-config.yaml`.

If you or your administrator choose to use a different filename or location (for example, if your administrator is providing the file at a secure URL), you can specify this using the `--login-config` flag with each of your authentication requests. See the following section for more details.

## Authenticate to the cluster

Run `gcloud` commands to authenticate with your clusters:

  1. Run the `gcloud anthos auth login` command to initiate the authentication flow:
         
         gcloud anthos auth login \
          --cluster [CLUSTER_NAME] \
          --user [USER_NAME] \
          --login-config [AUTH_CONFIG_FILE_PATH] \
          --login-config-cert [CA_CERT_PEM_FILE] \
          --kubeconfig [CLUSTER_KUBECONFIG]

Replace the following:

     * [CLUSTER_NAME] (optional) specifies the name of your cluster. If this flag is omitted, you are prompted to choose from the clusters that are specified in your authentication configuration file.

     * [USER_NAME] (optional) specifies the username for the credentials stored in the `kubeconfig` file. The default value is `[CLUSTER_NAME]-anthos-default-user`.

     * [AUTH_CONFIG_FILE_PATH] (optional) specifies the custom path or URL to where your authentication configuration file is stored or hosted. You can omit this parameter, if the file is in the default location. Example: `--login-config /path/to/custom/authentication-config.yaml`

     * [CA_CERT_PEM_FILE] (optional) specifies the path to a PEM certificate file from your CA. If your authentication configuration file is hosted securely, you can use an HTTPS connection to access the file. Example: `--login-config-cert my-cert.pem`

     * [CLUSTER_KUBECONFIG] (optional) specifies the custom path to your cluster's `kubeconfig` file. The OIDC ID tokens that are returned by your OpenID provider are stored in the `kubeconfig` file.

Use this flag if your `kubeconfig` file resides in a location other than the [default](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig). If this flag is omitted, authentication tokens are added to the `kubeconfig` file in the default location. Example: `--kubeconfig /path/to/custom.kubeconfig`

**Examples** :

     * Authenticate to specific cluster:
           
           gcloud anthos auth login --cluster my-production-cluster
           

     * Use a prompt to select which cluster to authenticate with:
           
           gcloud anthos auth login
           

Result:
           
           Please use the --cluster flag to specify a cluster from the list below:
           Source: $HOME/.config/google/anthos/kubectl-anthos-config.yaml
           1. Cluster: projects/1000000000000/locations/global/memberships/gke-gcp-cluster ServerIP: https://104.198.180.50:440
           2. Cluster: projects/1000000000000/locations/global/memberships/gke-baremetal-cluster ServerIP: https://104.198.180.51:440
           3. Cluster: projects/1000000000000/locations/global/memberships/gke-onprem-cluster ServerIP: https://104.198.180.52:440
           4. Cluster: projects/1000000000000/locations/global/memberships/gke-aws-cluster ServerIP: https://104.198.180.53:440
           

     * Use a hosted authentication configuration file:
           
           gcloud anthos auth login \
            --cluster my-production-cluster \
            --login-config HTTPS://my-secure-server/kubectl-anthos-config.yaml \
            --login-config-cert my-cert.pem
           

     * Use a prompt to select an authentication option. For more information, see Choose an authentication method.

  2. Enter your credentials in the browser-based consent screen that opens. If this succeeds, your `kubeconfig` file should now contain an ID token that your `kubectl` commands will use to authenticate with the Kubernetes API server on your cluster.

  3. Verify that authentication was successful by running one of the `kubectl` commands to access a resource on your cluster. For example, if you have access to the "nodes" resource on the cluster (this access is configured by your cluster administrator), you should be able to run the following command and view the cluster's nodes:
         
         kubectl get nodes --kubeconfig [CLUSTER_KUBECONFIG]




For troubleshooting information related to user access, see [Troubleshoot user access issues](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access-troubleshooting).

## Choose an authentication method

If your cluster administrator has configured multiple identity providers for your cluster (for example, an OIDC provider and an LDAP server), and has not configured a default provider for your cluster, you are prompted at login to select an authentication option, as in the following example:
    
    
    gcloud anthos auth login
    
    Please select your preferred authentication option for cluster [gke-onprem-ldap]
    [1] LDAP Server
    [2] OIDC
    [3] cancel
    
    Please enter your numeric choice:
    
    1
    
    Setting Preferred Authentication option to [LDAP Server]
    

Enter a numeric choice, then continue to log in as described in Authenticate to the cluster above.

Your chosen authentication option is saved until either your cluster administrator changes the default provider for this cluster, or you change it yourself. To change your preferred authentication option, use the `--set-preferred-authentication` flag.
    
    
    gcloud anthos auth login --set-preferred-authentication
    

You should see a result like the following example, letting you choose a new preferred authentication option:
    
    
    Your current authentication method is [1] AD Server. Please select your preferred authentication option for cluster [gke-onprem-ldap]
    [1] LDAP Server
    [2] OIDC
    [3] cancel
    
    Please enter your numeric choice:
    
    2
    
    Setting Preferred Authentication option to [OIDC]
    

## Use SSH to authenticate from a remote machine

To connect to a remote machine and authenticate to a cluster with SSH, your authentication configuration file must be on the remote machine, and you must be able to reach your OpenID provider from your local machine.

On your local machine, run the following command:
    
    
    ssh [USER_NAME]@[REMOTE_MACHINE] -L [LOCAL_PORT]:localhost:[REMOTE_PORT]
    

Replace the following:

  * [USER_NAME] and [REMOTE_MACHINE] are the standard values used to log in with SSH.

  * [LOCAL_PORT] is an open port of your choice on your local machine that you will use to access the remote machine.

  * [REMOTE_PORT] is the port you configured for your OIDC redirect URL. You can find this in the `kubectlRedirectURI` field of your authentication configuration file.




In your SSH shell, run the following command to initiate authentication:
    
    
    gcloud anthos auth login --login-config [AUTH_CONFIG_FILE]
    

where [AUTH_CONFIG_FILE] is the path of your authentication configuration file on the remote machine.

On your local machine, in a browser, go to http://localhost:[LOCAL_PORT]/login and complete the OIDC login flow.

Now the kubeconfig file on your remote machine has the token that you need to access the cluster.

In your SSH shell, verify that you have access to the cluster:
    
    
    kubectl --kubeconfig [CLUSTER_KUBECONFIG] get nodes
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
