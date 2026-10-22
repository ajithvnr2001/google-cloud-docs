---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/saml-per-cluster/
title: Set up fleet member clusters for SAML authentication \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:42.479700+00:00
---

# Set up fleet member clusters for SAML authentication  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/saml-per-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Set up fleet member clusters for SAML authentication Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how cluster administrators or application operators can configure Kubernetes clusters to support authentication from a third-party [Security Assertion Markup Language (SAML)](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html) provider. For more information, see [About authentication using third-party identities](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity).

## Limitations

You must use a [cluster type that supports SAML](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity#supported_cluster_types).

## Before you begin

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  4. After initializing the gcloud CLI, update it and install the required components: 
         
         gcloud components update
         gcloud components install kubectl

  5. Ensure that your platform administrator has given you all of the provider information that you need. For more information, see [Share provider details](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/saml-provider#share_provider_details).



## Configure the cluster

To configure a cluster for authentication using SAML, you configure a Kubernetes [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) named ClientConfig with information about the identity provider and the parameters that the provider needs to return user information.

To edit the `default` ClientConfig, make sure you can connect to your cluster `kubectl`, and then run the following command:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG -n kube-public edit clientconfig default
    

Replace `KUBECONFIG_PATH` with the path to your cluster's kubeconfig file—for example `$HOME/.kube/config`.

A text editor loads your cluster's ClientConfig resource. Add the `spec.authentication.saml` object as shown in the following sample. Don't modify any default data that has already been written.
    
    
    apiVersion: authentication.gke.io/v2alpha1
    kind: ClientConfig
    metadata:
      name: default
      namespace: kube-public
    spec:
      **authentication :
      - name: NAME
        saml:
          attributeMapping:
            ATTRIBUTE_KEY_1: ATTRIBUTE_CEL_EXPRESSION_1
            ATTRIBUTE_KEY_2: ATTRIBUTE_CEL_EXPRESSION_2
          groupsAttribute: GROUPS_ATTRIBUTE
          groupPrefix: GROUP_PREFIX
          idpEntityID: ENTITY_ID
          idpSingleSignOnURI: SIGN_ON_URI
          idpCertificateDataList: IDP_CA_CERT
          userAttribute: USER_ATTRIBUTE
          userPrefix: USER_PREFIX
        certificateAuthorityData: CERTIFICATE_AUTHORITY_DATA
        preferredAuthentication: PREFERRED_AUTHENTICATION
        server: <>**
    # Rest of the resource is managed by Google. DO NOT MODIFY.
    ...
    

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
    

### ClientConfig SAML fields

The following table describes the fields of the ClientConfig `saml` object. The fields that you need to add depend on your identity provider tokens and how your platform administrator configured the provider.

Field | Required | Description | Format  
---|---|---|---  
name | Yes | The name you want to use to identify this configuration, typically the identity provider name. A configuration name must start with a letter followed by up to 39 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. | String  
idpEntityID | Yes | The SAML entity ID for the SAML provider, specified in a URI format. For example: `https://www.idp.com/saml`. | URL String  
idpSingleSignOnURI | yes | The SAML provider SSO endpoint, specified in a URI format. For example: `https://www.idp.com/saml/sso`. | URL String  
idpCertificateDataList | Yes | Corresponds to the identity provider certificates used to verify the SAML response. These certificates must be standard base64 encoded and PEM formatted. Only a maximum of two certificates are supported to facilitate identity provider certificate rotation. | String  
userAttribute | No | Name of the attribute in the SAML response that holds the username. | String  
groupsAttribute | No | Name of the attribute in the SAML response that holds the user's group information. | String  
userPrefix | No | The prefix you want to prepend to user claims to prevent clashes with existing names, if you don't want to use the default prefix. | String  
groupPrefix | No | The prefix you want to prepend to security group names. This is to avoid clashes with existing names in your access control rules if you have configurations for multiple identity providers (typically the provider name). | String  
attributeMapping | No | The mapping of additional user attributes. | String  
certificateAuthorityData | No | If provided by your platform administrator, this is a PEM-encoded certificate string for the identity provider. Include the resulting string in `certificateAuthorityData` as a single line. | String  
preferredAuthentication | No | Name of the preferred authentication method configured in the cluster. | String  
  
After you complete your ClientConfig, save the file, which updates the ClientConfig on your cluster. If you've made any syntax errors, you are prompted to re-edit the configuration to fix them.

## What's next?

After the configuration is applied, continue to [set up user access to clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
