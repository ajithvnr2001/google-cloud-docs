---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/ldap/
title: Set up fleet member clusters for LDAP authentication \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:56.039253+00:00
---

# Set up fleet member clusters for LDAP authentication  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/ldap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Set up fleet member clusters for LDAP authentication Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how cluster administrators or application operators can configure Kubernetes clusters to support authentication from a third-party [Lightweight Directory Access Protocol (LDAP)](https://ldap.com/) provider, such as Microsoft Entra ID or Google LDAP. For more information, see [About authentication using third-party identities](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity).

## Limitations

You must use a [cluster type that supports LDAP](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity#supported_cluster_types).

## Before you begin

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  4. After initializing the gcloud CLI, update it and install the required components: 
         
         gcloud components update
         gcloud components install kubectl

  5. Ensure that your platform administrator has given you all of the provider information that you need. For more information, see [Configure LDAP providers to authenticate to clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider-ldap).



Throughout this setup, you might need to refer to the documentation for your LDAP server. The following administrator guides explain configuration for some popular LDAP providers, including where to find the information you need to log in to the LDAP server and configure your clusters:

  * [OpenLDAP](https://www.openldap.org/doc/)
  * [Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/architecture/auth-ldap)
  * [Microsoft Active Directory](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/active-directory-overview)
  * [Google LDAP](https://support.google.com/a/topic/9173976?ref_topic=9048334)



## Populate the LDAP service account secret

Your cluster needs a service account secret to authenticate to the LDAP server and retrieve user details. LDAP authentication supports the following mechanisms:

  * Basic authentication, where you use a username and password.
  * Client certificate authentication, where you use a client private key and client certificate.



You or your platform administrator should have this information about your provider from following [Configure LDAP providers to authenticate to clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider-ldap). To make the LDAP server login information available to the cluster, you need to create a [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/) that has the LDAP login details. The following examples show how to configure Secrets for both authentication types. The examples show the Secret being applied to the `anthos-identity-service` namespace.

This is an example of a basic authentication Secret configuration:
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: SERVICE_ACCOUNT_SECRET_NAME
      namespace: "anthos-identity-service"
    type: kubernetes.io/basic-auth     # Make sure the type is correct
    data:
      username: USERNAME  # Use a base64-encoded username
      password: PASSWORD  # Use a base64-encoded password

where, SERVICE_ACCOUNT_SECRET_NAME is the name you have chosen for this Secret. Replace the username and password values with the username and password you got in the previous step. USERNAME is a base64-encoded username PASSWORD is a base64-encoded password

This is an example of a client certificate Secret configuration:
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: SERVICE_ACCOUNT_SECRET_NAME
      namespace: anthos-identity-service
    type: kubernetes.io/tls            # Make sure the type is correct
    data:
      # the data is abbreviated in this example
      tls.crt: |
           MIIC2DCCAcCgAwIBAgIBATANBgkqh ...
      tls.key: |
           MIIEpgIBAAKCAQEA7yn3bRHQ5FHMQ ...

Replace SERVICE_ACCOUNT_SECRET_NAME with the name you have chosen for this Secret. Replace the TLS certificate and key values with the encoded certificate and key values you got in the previous step.

The examples show the secret being applied to the `anthos-identity-service` namespace. By default, system components have permission to read Secrets in this namespace. To use another namespace, change the metadata in the secret and then add a new RBAC policy to grant the permission to read Secrets in that namespace to the `default` ServiceAccount in the `anthos-identity-service` namespace, as follows:
    
    
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      namespace: NAMESPACE
      name: ais-secret-reader-role
    rules:
    - apiGroups: [""]
      resources: ["secrets"]
      verbs: ["get","list"]
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: ais-secret-reader-role-binding
      namespace: NAMESPACE
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: Role
      name: ais-secret-reader-role
    subjects:
    - kind: ServiceAccount
      name: default
      namespace: anthos-identity-service
    ---

## Configure the cluster

To configure authentication to a cluster using LDAP, you add the following information to a Kubernetes [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) named ClientConfig:

  * Information about the identity provider and the parameters it needs to return user information.
  * The name and namespace of the Secret that you created and applied in the previous, which allows the cluster to authenticate to the LDAP server.



To configure your cluster, edit the `default` ClientConfig in the `kube-public` namespace:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG -n kube-public edit clientconfig default
    

Replace `USER_CLUSTER_KUBECONFIG` with the path to the kubeconfig file for the cluster. If there are multiple contexts in the kubeconfig, the current context is used. You might need to reset the current context to the correct cluster before running the command.

The following shows the format for ClientConfig configuration:
    
    
    apiVersion: authentication.gke.io/v2alpha1
    kind: ClientConfig
    metadata:
      name: default
      namespace: kube-public
    spec:
      **authentication :
      - name: NAME
        ldap:
          certificateAuthorityData: CERTIFICATE_AUTHORITY_DATA
          connectionType: CONNECTION_TYPE
          host: HOST_NAME
          serviceAccountSecret:
            name: SERVICE_ACCOUNT_SECRET_NAME
            namespace: NAMESPACE
            type: SECRET_FORMAT
          user:
            baseDN: BASE_DN
            filter: FILTER
            identifierAttribute: IDENTIFIER_ATTRIBUTE
            loginAttribute: LOGIN_ATTRIBUTE
          group:
            baseDN: BASE_DN
            filter: FILTER
            identifierAttribute: IDENTIFIER_ATTRIBUTE**
    

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
    

### ClientConfig LDAP fields

The following table describes the fields of the ClientConfig `ldap` object. The fields that you need to add depend on your identity provider tokens and how your platform administrator configured the provider.

Field | Required | Description | Format  
---|---|---|---  
name  | yes  | A name to identify this LDAP configuration  | string   
host  | yes  | Hostname or IP address of the LDAP server. Port is optional and will default to 389, if unspecified. For example, `ldap.server.example.com` or `10.10.10.10:389`.  | string   
certificateAuthorityData  | Required for certain LDAP connection types  | Contains a Base64 encoded, PEM formatted certificate authority certificate for the LDAP server. This must be provided only for `ldaps` and `startTLS` connections.  | string   
connectionType  | yes  | LDAP connection type to use when connecting to the LDAP server. Defaults to `startTLS`. The `insecure` mode should only be used for development, since all communication with the server will be in plaintext.  | string   
serviceAccountSecret  |  |  |   
name  | yes  | Name of the Kubernetes Secret that stores the credentials for the LDAP service account.  | string   
namespace  | yes  | Namespace of the Kubernetes Secret which stores the credentials for the LDAP service account.  | string   
type  | yes  | Defines the format of the service account secret in order to support different kinds of secrets. If you specified `basic-auth` in your Secret configuration, this should be `basic`, otherwise it should be `tls`. If unspecified, defaults to `basic`.  | string   
user  |  |  |   
baseDN  | yes  | The location of the subtree in the LDAP directory to search for user entries.  | string   
filter  | no  | Optional filter to apply when searching for the user. This can be used to further restrict the user accounts that are allowed to login. If unspecified, defaults to `(objectClass=User)`.  | string   
identifierAttribute  | no  | Determines which attribute to use as the user's identity after they are authenticated. This is distinct from the loginAttribute field to allow users to login with a username, but then have their actual identifier be an email address or full Distinguished Name (DN). For example, setting loginAttribute to `sAMAccountName` and identifierAttribute to `userPrincipalName` would allow a user to login as `bsmith`, but actual RBAC policies for the user would be written as `bsmith@example.com`. Using `userPrincipalName` is recommended since this will be unique for each user. If unspecified, this defaults to `userPrincipalName`.  | string   
loginAttribute  | no  | The name of the attribute that matches against the input username. This is used to find the user in the LDAP database, for example `(<LoginAttribute>=<username>)` and is combined with the optional filter field. This defaults to `userPrincipalName`.  | string   
group (Optional field)  |  |  |   
baseDN  | yes  | The location of the subtree in the LDAP directory to search for group entries.  | string   
filter  | no  | Optional filter to be used when searching for groups a user belongs to. This can be used to explicitly match only certain groups in order to reduce the amount of groups returned for each user. This defaults to `(objectClass=Group)`.  | string   
identifierAttribute  | no  | The identifying name of each group a user belongs to. For example, if this is set to `distinguishedName` then RBACs and other group expectations should be written as full DNs. If unspecified, this defaults to `distinguishedName`.  | string   
  
## What's next?

After the configuration is applied, continue to [set up user access from external providers to clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
