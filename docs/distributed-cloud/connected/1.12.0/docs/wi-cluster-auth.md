---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/wi-cluster-auth/
title: Workload Identity Cluster Authentication \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:57.085321+00:00
---

# Workload Identity Cluster Authentication  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/wi-cluster-auth/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/overview)



Send feedback 

#  Workload Identity Cluster Authentication Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up and use Workload Identity Cluster Authentication for Google Distributed Cloud connected, version 1.12.0. Instead of service account keys, Workload Identity Cluster Authentication uses short-lived tokens and Workload Identity Federation to allow your workloads to access Google Cloud resources securely. The short-lived credentials are OAuth 2.0 access tokens. By default, the access tokens expire after 1 hour.

With Workload Identity Cluster Authentication, your workloads can use their own Kubernetes identity to access Google Cloud resources directly or impersonate a Google service account.

Workload Identity Cluster Authentication provides two main benefits over using service account keys:

  * **Improved security** : Service account keys are a security risk if not managed correctly. OAuth 2.0 tokens and Workload Identity Federation are considered best practice alternatives to service account keys. For more information about service account tokens, see [Short-lived service account credentials](https://docs.cloud.google.com/iam/docs/service-account-creds#short-lived-credentials). For more information about Workload Identity Federation, see [ Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation).

  * **Reduced maintenance** : Service account keys require more maintenance. Regularly rotating and securing these keys can create an administrative burden.




This page is for Admins and architects and Operators who set up, monitor, and manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Cluster management

This guide covers Workload Identity Federation for your applications. Cluster-level Workload Identity Federation is automatically managed for Distributed Cloud connected clusters.

Distributed Cloud connected clusters are created and managed by Google through the [Distributed Cloud Edge Container API](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/apis), either by using the [`gcloud edge-cloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create) command or in the Google Cloud console.

Distributed Cloud connected clusters are automatically registered to a Fleet in the project that they're created in. You don't need to do any manual fleet registration. The Workload Identity Federation Pool is automatically available and follows the format `PROJECT_ID.svc.id.goog`.

## Before you begin

  * Before you can set up Workload Identity Federation, verify that the following APIs in your Google Cloud project are enabled. For information about enabling APIs, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling):

    * `iam.googleapis.com`
    * `sts.googleapis.com`
    * `iamcredentials.googleapis.com`
    * `gkehub.googleapis.com`
  * Ensure that you have the following command line tools installed:

    * The latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), which includes `gcloud`, the command line tool for interacting with Google Cloud.
    * [`kubectl`](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#install-kubectl)

If you're using Cloud Shell as your shell environment for interacting with Google Cloud, these tools are installed for you.

  * Ensure that you have [initialized](https://docs.cloud.google.com/sdk/docs/install-sdk#initializing_the) the gcloud CLI for use with your project.

  * Make sure that you have the following IAM roles on the project. These roles are required to perform the setup:

    * Owner (`roles/owner`) or
    * IAM Security Admin (`roles/iam.securityAdmin`) and Service Account Admin (`roles/iam.serviceAccountAdmin`)



In the following sections, you create service accounts and grant roles needed for Workload Identity Cluster Authentication.

### Recommended: Workload Identity Federation direct resource access

With Workload Identity Federation direct resource access, you use Workload Identity Federation to grant an IAM role to a Kubernetes ServiceAccount so that it can directly access Google Cloud resources.

Identity | Purpose | Roles  
---|---|---  
Kubernetes ServiceAccount |  The Kubernetes identity that your workload uses. Grant this identity the roles needed to access the required Google Cloud resources. This example grants the `roles/storage.objectViewer` role and the `roles/logging.admin` role.  |  `roles/storage.objectViewer`  
`roles/logging.admin`  
  
  
### Alternative: IAM service account impersonation

Alternatively, you can configure configure your Kubernetes ServiceAccount to use IAM service account impersonation.

Service account | Purpose | Roles  
---|---|---  
Google service account |  The Google service account that your in-cluster workload impersonates. Grant this service account the roles needed to access the required Google Cloud resources.  |  Depends on the resources being accessed.   
Kubernetes ServiceAccount |  Grant this identity the ability to impersonate the Google service account. This grant uses the role `roles/iam.workloadIdentityUser`.  |  `roles/iam.workloadIdentityUser`  
  
## Set up service accounts

The following sections contain instructions to create the required Kubernetes ServiceAccount and to grant it the necessary roles for Workload Identity Cluster Authentication using either Workload Identity Federation direct resource access or Google service account impersonation.

### Create a Kubernetes ServiceAccount

In your cluster, use the [kubectl create](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/) command to create a Kubernetes ServiceAccount for your pods. You can also use any existing ServiceAccount, including the default `ServiceAccount` in the namespace.
    
    
    kubectl create serviceaccount KSA_NAME --namespace NAMESPACE
    

Replace the following values:

  * `KSA_NAME`: a name for your Kubernetes ServiceAccount

  * `NAMESPACE`: the namespace for your cluster




### Use Workload Identity Federation to grant direct resource access

To grant Identity and Access Management roles directly to your Kubernetes ServiceAccount identity, follow these steps.

  1. Use the [gcloud projects describe](https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe) command to find your numerical project number:
         
         gcloud projects describe PROJECT_ID --format="value(projectNumber)"
         

Replace `PROJECT_ID` with the ID of your project.

  2. Use the [gcloud projects add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command to grant the required roles to the Kubernetes identity principal:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="principal://iam.gserviceaccount.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KSA_NAME" \
             --role=roles/storage.objectViewer
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="principal://iam.gserviceaccount.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KSA_NAME" \
             --role=roles/logging.admin
         

Replace the following values:

     * `PROJECT_NUMBER`: your numerical project number
     * `NAMESPACE`: the namespace for your cluster
     * `KSA_NAME`: the name for your Kubernetes ServiceAccount



### Alternative: Use IAM service account impersonation to grant access

If you prefer to have your workloads impersonate a Google service account, follow these steps.

  1. Use the [gcloud iam service-accounts create](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/create) command to create a Google service account:
         
         gcloud iam service-accounts create my-app-sa \
             --project=PROJECT_ID
         

Replace `PROJECT_ID` with the ID of your project.

  2. Use the [gcloud projects add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command to crant the Google service account the required roles:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member=serviceAccount:my-app-sa@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/storage.objectViewer
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member=serviceAccount:my-app-sa@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/logging.admin
         

  3. Use the [gcloud iam service-accounts add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding) command to grant the Kubernetes ServiceAccount the ability to impersonate the Google service account:
         
         gcloud iam service-accounts add-iam-policy-binding my-app-sa@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/iam.workloadIdentityUser \
             --member="serviceAccount:PROJECT_ID.svc.id.goog[NAMESPACE/KSA_NAME]"
         

Replace the following values:

     * `NAMESPACE`: the namespace for your cluster
     * `KSA_NAME`: the name for your Kubernetes ServiceAccount
  4. Use the [kubectl annotate](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_annotate/) command to annotate the Kubernetes ServiceAccount to link it to the Google service account:
         
         kubectl annotate serviceaccount \
             --namespace NAMESPACE KSA_NAME \
             iam.gke.io/gcp-service-account=my-app-sa@PROJECT_ID.iam.gserviceaccount.com
         




## Configure the workload

Update the Pod specification to use the Kubernetes ServiceAccount and mount the projected token volume. Because Distributed Cloud connected clusters are outside of Google Cloud, you must also provide a credential configuration file and set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to that file. Google Cloud client libraries within the pod use these to exchange the Kubernetes token for a Google Cloud access token through the Security Token Service API.

  1. Generate the `credential-configuration.json` file. Choose the command based on whether you're using Workload Identity Federation direct resource access or using IAM service account impersonation.

**Workload Identity Federation direct resource access**

Use the [gcloud iam workload-identity-pools create-cred-config](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create-cred-config) command:
         
         gcloud iam workload-identity-pools create-cred-config \
             projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/providers/attestor \
             --credential-source-file=/var/run/secrets/tokens/gcp-ksa/token \
             --credential-source-type=text \
             --output-file=credential-configuration.json
         

**Use IAM service account impersonation to grant access**

Use the [gcloud iam workload-identity-pools create-cred-config](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/create-cred-config) command:
         
         gcloud iam workload-identity-pools create-cred-config \
             projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/providers/attestor \
             --service-account=my-app-sa@PROJECT_ID.iam.gserviceaccount.com \
             --credential-source-file=/var/run/secrets/tokens/gcp-ksa/token \
             --credential-source-type=text \
             --output-file=credential-configuration.json
         

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can find the project number by running `gcloud projects describe PROJECT_ID --format="value(projectNumber)"`.

  2. Use the [`kubectl create configmap`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_configmap/) command to create a Kubernetes `ConfigMap` to store the configuration file:
         
         kubectl create configmap CREDENTIAL_CONFIG_MAP \
             --namespace NAMESPACE \
             --from-file=credential-configuration.json
         

Replace the following values:

     * `CREDENTIAL_CONFIG_MAP`: a name for your `ConfigMap`, which contains your credential configuration file

     * `NAMESPACE`: the namespace for your cluster

  3. Update your Pod specification with the following YAML content:
         
         spec:
           serviceAccountName: KSA_NAME
           containers:
           - name: MY_CONTAINER
             image: MY_IMAGE
             env:
             - name: GOOGLE_APPLICATION_CREDENTIALS
               value: /var/run/secrets/tokens/gcp-creds/credential-configuration.json
             volumeMounts:
             - mountPath: /var/run/secrets/tokens/gcp-ksa
               name: gcp-ksa
             - mountPath: /var/run/secrets/tokens/gcp-creds
               name: gcp-creds
               readOnly: true
           volumes:
           - name: gcp-ksa
             projected:
               defaultMode: 0420
               sources:
               - serviceAccountToken:
                   path: token
                   audience: PROJECT_ID.svc.id.goog
                   expirationSeconds: 3600
           - name: gcp-creds
             configMap:
               name: CREDENTIAL_CONFIG_MAP
         

Replace the following values:

     * `KSA_NAME`: a name for your Kubernetes ServiceAccount

     * `MY_CONTAINER`: the name of your container

     * `MY_IMAGE`: the name of your image




## Limitations

The following features and capabilities aren't supported when you use Workload Identity Federation for Distributed Cloud connected:

  * Using a proxy server for the token exchange process



For information about using Workload Identity Federation with VPC Service Controls, see [Configure VPC Service Controls integration](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/deploy#vpc-sc-integration).

## What's next

  * [Deploy workloads on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/deploy)
  * [Manage services](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/services)
  * [Apply security best practices](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/security)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
