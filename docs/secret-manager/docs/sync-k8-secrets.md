---
url: https://docs.cloud.google.com/secret-manager/docs/sync-k8-secrets/
title: Synchronize secrets to Kubernetes Secrets \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:45.106364+00:00
---

# Synchronize secrets to Kubernetes Secrets  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/sync-k8-secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/docs/overview)



Send feedback 

#  Synchronize secrets to Kubernetes Secrets Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to synchronize secrets stored in Secret Manager to Kubernetes Secrets within your Google Kubernetes Engine (GKE) clusters.

The synchronization process lets applications running on GKE access secrets from Secret Manager using standard Kubernetes methods, such as environment variables or volume mounts. This is useful for applications that are already designed to read secrets from the Kubernetes Secret object, rather than having to be updated to directly access Secret Manager.

Recommendation: The secret synchronization feature is an alternative to the [Secret Manager add-on](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component), which mounts secrets as in-memory files directly into your Pods. Use the Secret Manager add-on whenever your application supports it, because it is a more secure method to access secrets from Secret Manager in GKE.

## Before you begin

Complete the following prerequisites before you synchronize secrets:

  * Enable the Secret Manager and Google Kubernetes Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=secretmanager.googleapis.com,container.googleapis.com)

  * [Install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command.

  * Ensure you have a GKE cluster running. This feature requires GKE version 1.33 and later.

  * Ensure Workload Identity Federation for GKE is enabled on your GKE cluster. This is required for authentication. Workload Identity Federation for GKE is enabled by default on an Autopilot cluster.

  * Ensure you have the necessary Identity and Access Management permissions to manage GKE clusters and Secret Manager.




## Enable secret synchronization on a GKE cluster

Enable the secret synchronization feature when you create a new cluster or update an existing cluster. This feature is available on both Standard and Autopilot clusters.

### Enable secret synchronization on a new cluster

To create a new cluster with secret synchronization, use one of these gcloud CLI commands:

###  Standard cluster

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 

Enable secret synchronization without automatic rotation.
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --workload-pool=PROJECT_ID.svc.id.goog \
        --enable-secret-sync
    

Enable secret synchronization with automatic rotation. The default interval is 2 minutes.
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --workload-pool=PROJECT_ID.svc.id.goog \
        --enable-secret-sync \
        --enable-secret-sync-rotation
    

Enable secret synchronization with a custom rotation interval. The minimum interval is 1 minute.
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --workload-pool=PROJECT_ID.svc.id.goog \
        --enable-secret-sync \
        --enable-secret-sync-rotation \
        --secret-sync-rotation-interval=60s
    

Replace the following:

  * `CLUSTER_NAME`: the name of your GKE cluster
  * `CONTROL_PLANE_LOCATION`: the region or zone of your cluster control plane, such as `us-central1` or `us-east1-a`
  * `PROJECT_ID`: your Google Cloud project ID



###  Autopilot cluster

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 

Enable secret synchronization without automatic rotation.
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --enable-secret-sync
    

Enable secret synchronization with automatic rotation. The default interval is 2 minutes.
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --enable-secret-sync \
        --enable-secret-sync-rotation
    

Enable secret synchronization with a custom rotation interval. The minimum interval is 1 minute.
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --enable-secret-sync \
        --enable-secret-sync-rotation \
        --secret-sync-rotation-interval=60s
    

Replace the following:

  * `CLUSTER_NAME`: the name of your GKE cluster
  * `CONTROL_PLANE_LOCATION`: the region or zone of your cluster control plane, such as `us-central1` or `us-east1-a`



### Enable secret synchronization on an existing cluster

To update existing clusters with secret synchronization, use one of the following gcloud CLI commands:

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 

Enable secret synchronization on an existing cluster
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --enable-secret-sync
    

Enable rotation with a custom interval
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --enable-secret-sync-rotation \
        --secret-sync-rotation-interval=300s
    

Disable rotation
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --no-enable-secret-sync-rotation
    

Replace the following:

  * `CLUSTER_NAME`: the name of your GKE cluster
  * `CONTROL_PLANE_LOCATION`: the region or zone of your cluster control plane, such as `us-central1` or `us-east1-a`



## Configure secret synchronization

To synchronize secrets, complete the following steps:

  1. Create a [Kubernetes ServiceAccount](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) using the following command:
         
         kubectl create serviceaccount KSA_NAME --namespace NAMESPACE
         

Replace the following:

     * `KSA_NAME`: the name of your Kubernetes ServiceAccount
     * `NAMESPACE`: the Kubernetes namespace where you want to create the ServiceAccount
  2. Create an IAM allow policy that references the new Kubernetes ServiceAccount and grant the ServiceAccount permission to access the secret:

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
         
         gcloud secrets add-iam-policy-binding SECRET_NAME \
            --role=roles/secretmanager.secretAccessor \
            --member=principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KSA_NAME
         

Replace the following:

     * `SECRET_NAME`: the name of the secret in Secret Manager
     * `PROJECT_NUMBER`: your Google Cloud project number
     * `PROJECT_ID`: your Google Cloud project ID
     * `NAMESPACE`: the Kubernetes namespace
     * `KSA_NAME`: the name of your Kubernetes ServiceAccount

  3. Create a SecretProviderClass custom resource using a YAML manifest. The SecretProviderClass resource defines the specific secrets to retrieve Secret Manager, including their resource names and paths. The Secret Manager add-on also uses the SecretProviderClass resource to list the secrets to mount and the filename to mount them as.

Create a `spc.yaml` file with the following content:
         
         apiVersion: secrets-store.csi.x-k8s.io/v1
         kind: SecretProviderClass
         metadata:
           name: SECRET_PROVIDER_CLASS_NAME
           namespace: NAMESPACE
         spec:
           provider: gke
           parameters:
             secrets: |
               -   resourceName: "projects/SECRET_PROJECT_ID/secrets/SECRET_NAME_1/versions/SECRET_VERSION_1"
                   path: "FILENAME.txt"
               -   resourceName: "projects/SECRET_PROJECT_ID/secrets/SECRET_NAME_2/versions/SECRET_VERSION_2"
                   path: "FILENAME1.txt"
         

Replace the following:

     * `SECRET_PROVIDER_CLASS_NAME`: the name for your SecretProviderClass object.
     * `NAMESPACE`: the Kubernetes namespace where you are creating this resource.
     * `resourceName`: the complete resource identifier for the secret in Secret Manager. This must include the project ID, secret name, and version following the format: projects/SECRET_PROJECT_ID/secrets/SECRET_NAME/versions/SECRET_VERSION. 
       * `SECRET_PROJECT_ID`: the ID of the Google Cloud project where the secret is stored. This can be the same as the PROJECT_ID if the secret is stored in the same project as the GKE cluster.
       * `SECRET_NAME`: the secret name.
       * `SECRET_VERSION`: the secret version. The secret version must be in the same region as the cluster.
     * `path`: the local filename or alias that the secret value will be exposed as within the Kubernetes environment. It's the unique identifier that links a specific Secret Manager version to the local representation used by the cluster. When the secret is synced to a Kubernetes Secret using the SecretSync resource, this path is referenced by the `sourcePath` field to locate the secret value for syncing. You can map multiple secrets (defined by `resourceName`) to different path names within the same SecretProviderClass.
  4. To apply the manifest, run the following command:
         
         kubectl apply -f spc.yaml
         

  5. Create a SecretSync custom resource using a YAML manifest. This resource instructs the synchronization controller to create or update a Kubernetes Secret based on the contents defined in the SecretProviderClass.

Create a `secret-sync.yaml` file with the following content:
         
         apiVersion: secret-sync.gke.io/v1
         kind: SecretSync
         metadata:
           name: KUBERNETES_SECRET_NAME
           namespace: NAMESPACE
         spec:
           serviceAccountName: KSA_NAME
           secretProviderClassName: SECRET_PROVIDER_CLASS_NAME
           secretObject:
             type: KUBERNETES_SECRET_TYPE
             data:
               -   sourcePath: "FILENAME.txt"
                   targetKey: "TARGET_KEY1"
               -   sourcePath: "FILENAME1.txt"
                   targetKey: "TARGET_KEY2"
         

Replace the following:

     * `KUBERNETES_SECRET_NAME`: the name you want to give to the new Kubernetes Secret that will be created by the SecretSync resource.
     * `NAMESPACE`: the Kubernetes namespace where the new resource is created. It must be the same namespace as the SecretProviderClass.
     * `KSA_NAME`: the name of the Kubernetes ServiceAccount that the SecretSync controller uses to create and update the target Kubernetes Secret. This ServiceAccount must have the necessary permissions to access external secrets from Secret Manager.
     * `SECRET_PROVIDER_CLASS_NAME`: the name of the SecretProviderClass object that you created in the previous step. The SecretSync resource uses this to find the correct configuration for the secrets.
     * `KUBERNETES_SECRET_TYPE`: the type of Kubernetes Secret to be created, such as `Opaque`, `tls`, or `docker-registry`. This determines how Kubernetes handles the secret's data.
     * `sourcePath`: the local filename or alias (the value of the `path` field in the SecretProviderClass) that identifies the secret data to be retrieved. The SecretSync controller uses this `sourcePath` to request the specific secret content and convert it into a new Kubernetes Secret.
     * `targetKey`: the key that will be used in the `data` section of the new Kubernetes Secret being created. This defines how the secret content retrieved using the `sourcePath` is named and stored in the final Kubernetes Secret object. Using multiple entries in the data array lets you define multiple key-value pairs within the same target Secret.
  6. To apply the manifest, run the following command:
         
         kubectl apply -f secret-sync.yaml
         

The synchronization controller creates a Kubernetes Secret in the specified namespace. This secret contains the data mapped from Secret Manager.

  7. Verify that the Kubernetes Secret is created:
         
         kubectl get secret KUBERNETES_SECRET_NAME -n NAMESPACE -o yaml
         

Replace the following:

     * `KUBERNETES_SECRET_NAME`: the name of the new Kubernetes Secret
     * `NAMESPACE`: the Kubernetes namespace where the new Secret is created
  8. To troubleshoot a synchronization issue, use the following command:
         
         kubectl describe secretSync KUBERNETES_SECRET_NAME -n NAMESPACE
         

Replace the following:

     * `KUBERNETES_SECRET_NAME`: the name of the new Kubernetes Secret
     * `NAMESPACE`: the Kubernetes namespace where the new Secret should exist

**Note:** If you're using VPC Service Controls to restrict the Secret Manager API and encounter ingress violations when using this feature, your service perimeter might be preventing access to the Secret Manager API from a project that's not part of the perimeter. If you continue to experience issues, contact [Google Cloud Support](https://docs.cloud.google.com/support).

## Manage secret rotation

If you [enable the `--enable-secret-sync-rotation` flag](https://docs.cloud.google.com/secret-manager/docs/sync-k8-secrets#enable-secret-sync), on your cluster, the synchronization controller periodically checks Secret Manager for new versions of the secrets specified in the SecretProviderClass resource. The `--secret-sync-rotation-interval` flag determines how often the controller checks for updates.

If the controller detects a new secret version in Secret Manager, the controller updates the corresponding Kubernetes Secret. The controller compares hashes of the secret content to update secrets only when changes occur.

Applications using these secrets must detect and reload the updated secret values from the Kubernetes Secret. The application's design determines how this is handled.

## Disable secret synchronization

To disable secret synchronization, run the following gcloud CLI command:

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --no-enable-secret-sync
    

Replace the following:

  * `CLUSTER_NAME`: the name of your GKE cluster
  * `CONTROL_PLANE_LOCATION`: the region or zone of your cluster control plane, such as `us-central1` or `us-east1-a`



This command stops the synchronization controller. It doesn't delete any Kubernetes Secrets that have already been created. You must manually delete any synced Kubernetes Secrets if you no longer need them.

## Delete synced secrets

To delete a synced Kubernetes Secret, delete the `SecretSync` resource using the following command:
    
    
        kubectl delete secretsync KUBERNETES_SECRET_NAME --namespace NAMESPACE
    

Replace the following:

  * `KUBERNETES_SECRET_NAME`: the name of the Kubernetes Secret
  * `NAMESPACE`: the Kubernetes namespace where the Secret exists



## Migrate from the existing Secrets Store CSI Driver

If you're migrating from your existing installation of the [Secrets Store CSI Driver](https://github.com/kubernetes-sigs/secrets-store-csi-driver), follow these steps:

  1. Update the `provider` field in your SecretProviderClass from `gcp` to `gke`. The following example shows how to update the `provider` field:
         
         apiVersion: secrets-store.csi.x-k8s.io/v1
         kind: SecretProviderClass
         metadata:
           name: app-secrets-gke
         spec:
           provider: gke
           parameters:
             secrets: |
               -   resourceName: "projects/87654321/secrets/api-key-secret/versions/2"
                   path: "good1.txt"
         

  2. Create a SecretSync resource. Use the following sample configuration:
         
         apiVersion: secret-sync.gke.io/v1
         kind: SecretSync
         metadata:
           name: my-kube-secret
           namespace: NAMESPACE
         spec:
           serviceAccountName: KSA_NAME
           secretProviderClassName: my-app-secrets
           secretObject:
             type: Opaque # Or other Kubernetes Secret types
             data:
               -   sourcePath: "my-secret.txt"
                   targetKey: "USERNAME"
               -   sourcePath: "another-secret.txt"
                   targetKey: "PASSWORD"
         




## Security considerations

Secret Manager offers security features like [access control with IAM](https://docs.cloud.google.com/secret-manager/docs/access-control), [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/secret-manager/docs/cmek), and [audit logging](https://docs.cloud.google.com/secret-manager/docs/audit-logging). Secrets are encrypted at rest and in transit within Secret Manager. When you synchronize secrets to Kubernetes secrets, their security within the cluster depends on the configuration of your GKE cluster. Consider the following:

  * **Storage** : Kubernetes secrets are stored in etcd, which is GKE's primary datastore. By default, GKE encrypts data at rest. For enhanced security, [encrypt Kubernetes secrets at the application layer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets) by using a key that you manage in [Cloud Key Management Service(Cloud KMS)](https://docs.cloud.google.com/kms/docs). Encrypting secrets provides an additional layer of security for sensitive workloads.

  * **Access control** : GKE supports multiple options for managing access to resources within projects and its clusters using role-based access control (RBAC). Overly broad RBAC permissions can expose secrets to unintended workloads or users. Grant access following the principle of least privilege and regularly audit access to both Secret Manager and the Kubernetes secrets.

  * **Environment variables** : To improve security, mount Kubernetes secrets as volumes instead of using them as environment variables. This reduces the risk of accidental logging or exposure to other processes.




## What's next

  * Read the [Secret Manager GKE integration release notes](https://docs.cloud.google.com/secret-manager/docs/gke-release-notes).
  * Explore [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/).
  * Understand [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
