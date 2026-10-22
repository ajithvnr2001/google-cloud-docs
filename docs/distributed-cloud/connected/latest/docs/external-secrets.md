---
url: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/external-secrets/
title: Use External Secrets Operator \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:06.320380+00:00
---

# Use External Secrets Operator  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/external-secrets/

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
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/overview)



Send feedback 

#  Use External Secrets Operator Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use [External Secrets Operator (ESO)](https://external-secrets.io/latest) to synchronize secrets from Secret Manager to your Google Distributed Cloud connected clusters.

External Secrets Operator is an open-source Kubernetes operator that integrates external secret management systems. The operator reads information from external APIs and automatically injects the values into a Kubernetes secret.

## Prerequisites

Before you can use External Secrets Operator, you need to do the following:

  * Create a functional Distributed Cloud connected cluster.
  * Verify that the following APIs are enabled in your Google Cloud project. For information about enabling APIs, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling): 
    * `secretmanager.googleapis.com`
    * `iamcredentials.googleapis.com`
  * Ensure that you have the following command line tools installed:

    * The latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), which includes `gcloud`, the command line tool for interacting with Google Cloud.
    * [`kubectl`](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#install-kubectl)

If you're using Cloud Shell as your shell environment for interacting with Google Cloud, these tools are installed for you.

  * Ensure that you have [initialized](https://docs.cloud.google.com/sdk/docs/install-sdk#initializing_the) the gcloud CLI for use with your project.

  * Enable [Workload Identity Federation on the cluster](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/wi-cluster-auth). The Workload Identity Pool is automatically available and follows the format `PROJECT_ID.svc.id.goog`.

  * Install External Secrets Operator on your cluster. For installation instructions, see the [External Secrets Operator documentation](https://external-secrets.io/). We recommend installing the operator in a dedicated namespace, such as `external-secrets`. Don't install it in system-managed namespaces such as `kube-system` or `gke-system`.




Distributed Cloud connected clusters are automatically registered to a Fleet in the project where they are created.

## Authentication

External Secrets Operator requires authentication to access Secret Manager. Distributed Cloud connected uses Fleet Workload Identity Federation to allow workloads to authenticate to Google Cloud APIs.

To configure authentication for External Secrets Operator:

  1. Set up the trust relationship between your cluster and Google Cloud by following the instructions in [Workload Identity Cluster Authentication](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/wi-cluster-auth).
  2. Grant the Secret Manager Secret Accessor role (`roles/secretmanager.secretAccessor`) on the secret to the Kubernetes ServiceAccount that External Secrets Operator uses:
         
         gcloud secrets add-iam-policy-binding SECRET_NAME \
             --project=PROJECT_ID \
             --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/OPERATOR_NAMESPACE/sa/KUBERNETES_SERVICEACCOUNT" \
             --role="roles/secretmanager.secretAccessor" \
             --condition=None
         

Replace the following values:

     * `SECRET_NAME`: the name of the secret in Secret Manager
     * `PROJECT_ID`: your Google Cloud project ID
     * `PROJECT_NUMBER`: your numerical Google Cloud project number
     * `OPERATOR_NAMESPACE`: the namespace where you installed the operator
     * `KUBERNETES_SERVICEACCOUNT`: the name of the Kubernetes ServiceAccount used by the operator
  3. Configure the External Secrets Operator Pod to use Workload Identity Federation and provide the credential configuration file to the operator Pod by following the [Configure the workload](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/wi-cluster-auth#configure-workload) instructions.




## Create ESO resources to synchronize secrets

After you configure authentication, you can create External Secrets Operator resources to synchronize secrets.

### Create a `SecretStore`

A `SecretStore` specifies how to access the external secret management system. You can create `SecretStore` resources in the same namespace as External Secrets Operator or in application namespaces. For more information, see [SecretStore](https://external-secrets.io/latest/api/secretstore/) in the Kubernetes documentation.

  1. Create a file named `secret-store.yaml` with the following content:
         
         apiVersion: external-secrets.io/v1
         kind: SecretStore
         metadata:
           name: gcp-store
           namespace: NAMESPACE
         spec:
           provider:
             gcpsm:
               projectID: PROJECT_ID
         

Replace the following values:

     * `NAMESPACE`: the namespace where you want to create the `SecretStore`
     * `PROJECT_ID`: your Google Cloud project ID where secrets are stored
  2. Use the [kubectl apply](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/) command to apply the manifest:
         
         kubectl apply -f secret-store.yaml
         




### Create a `ClusterSecretStore`

A `ClusterSecretStore` is a cluster-scoped resource that `ExternalSecret` resources can use in any namespace. For more information, see [ClusterSecretStore](https://external-secrets.io/latest/api/clustersecretstore/) in the Kubernetes documentation.

  1. Create a file named `cluster-secret-store.yaml` with the following content:
         
         apiVersion: external-secrets.io/v1
         kind: ClusterSecretStore
         metadata:
           name: gcp-cluster-store
         spec:
           provider:
             gcpsm:
               projectID: PROJECT_ID
         

Replace `PROJECT_ID` with your Google Cloud project ID where secrets are stored.

  2. Apply the manifest:
         
         kubectl apply -f cluster-secret-store.yaml
         




### Create an `ExternalSecret`

An `ExternalSecret` declares what data to fetch and where to store it in the cluster. Create `ExternalSecret` resources in the namespace where the application Pods consume the resulting Kubernetes Secret. For more information, see [ExternalSecret](https://external-secrets.io/latest/api/externalsecret/) in the Kubernetes documentation.

  1. Create a file named `external-secret.yaml` with the following content:
         
         apiVersion: external-secrets.io/v1
         kind: ExternalSecret
         metadata:
           name: EXTERNAL_SECRET
           namespace: NAMESPACE
         spec:
           refreshInterval: 1h
           secretStoreRef:
             kind: SecretStore
             name: gcp-store
           target:
             name: K8S_SECRET_NAME
             creationPolicy: Owner
           data:
           - secretKey: K8S_SECRET_KEY
             remoteRef:
               key: SECRET_NAME
         

Replace the following values:

     * `EXTERNAL_SECRET`: the name of the `ExternalSecret` resource.
     * `NAMESPACE`: the namespace where you created the `SecretStore`.
     * `K8S_SECRET_NAME`: the name of the Kubernetes Secret to be created by ESO.
     * `K8S_SECRET_KEY`: the key in the Kubernetes Secret data.
     * `SECRET_NAME`: the name of the secret in Google Cloud Secret Manager.

If you use a `ClusterSecretStore`, set `kind: ClusterSecretStore`, and update the `name` in `secretStoreRef`.

  2. Apply the manifest:
         
         kubectl apply -f external-secret.yaml
         




### Synchronize multiple keys from a JSON secret

If your secret in Secret Manager contains a JSON string, you can extract all keys as individual entries in the Kubernetes secret.

  1. Create a file named `external-secret-json.yaml` with the following content:
         
         apiVersion: external-secrets.io/v1
         kind: ExternalSecret
         metadata:
           name: EXTERNAL_SECRET
           namespace: NAMESPACE
         spec:
           refreshInterval: 1h
           secretStoreRef:
             kind: SecretStore
             name: gcp-store
           target:
             name: K8S_SECRET_NAME
             creationPolicy: Owner
           dataFrom:
           - extract:
               key: SECRET_NAME
         

  2. Apply the manifest:
         
         kubectl apply -f external-secret-json.yaml
         




Each key-value pair in the JSON secret is mapped to a key-value pair in the resulting Kubernetes secret.

## Troubleshooting

If your secrets don't synchronize, use the following steps to troubleshoot:

  1. Use the [kubectl get](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/) command to check the status of the `ExternalSecret` resource:
         
         kubectl get externalsecret EXTERNAL_SECRET -n NAMESPACE -o yaml
         

Examine the `status` section for any error messages or failed conditions.

  2. Use the [kubectl logs](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_logs/) command to check the logs of the External Secrets Operator controller Pod:
         
         kubectl logs -l app.kubernetes.io/name=external-secrets -n OPERATOR_NAMESPACE
         

  3. Verify that the Kubernetes ServiceAccount used by the operator has the Secret Manager Secret Accessor role (`roles/secretmanager.secretAccessor`) and that Workload Identity Federation is correctly configured on the operator Pod. For more information, see [Workload Identity Federation on the cluster](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/wi-cluster-auth).




## What's next

  * [Security best practices](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/security)
  * [Manage services](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/services)
  * [Troubleshooting](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
