---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/grant-access-helm-oci/
title: Grant Config Sync access to your OCI image or Helm repository \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:20:20.499503+00:00
---

# Grant Config Sync access to your OCI image or Helm repository  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/grant-access-helm-oci/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Grant Config Sync access to your OCI image or Helm repository Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to authenticate Config Sync to your OCI image or Helm repository. Config Sync requires read-only access to your source of truth so it can read your configurations, apply them to your clusters, and keep them in sync.

## Choose an authentication method

The authentication method that you use depends on what is supported for your source type.

The following table summarizes the authentication methods you can use with Config Sync:

Method | Supported sources | Description | Limitations  
---|---|---|---  
**No authentication** | Git, OCI, Helm | No additional setup required. | Only works if your source of truth is public.  
**SSH key pair** | Git | Supported by most Git providers. | Requires key management. Not supported for OCI or Helm.  
**token** | Git, OCI, Helm | Supported by most Git providers. Good alternative if your organization doesn't permit the use of SSH keys. Supports username and password for OCI and Helm. | Requires token management. Tokens can expire.  
**Kubernetes service account** | OCI, Helm | Uses IAM to grant Artifact Registry access directly to a Kubernetes service account. Requires Workload Identity Federation for GKE to be enabled on your cluster. | Not supported for Git.  
**Google service account** | Git | Uses IAM, which avoids storing credentials in Kubernetes Secrets. Recommended for Secure Source Manager and Cloud Source Repositories. Requires Workload Identity Federation for GKE to be enabled on your cluster. | Requires configuration before and after installing Config Sync on your clusters. Not supported for repositories hosted outside of Secure Source Manager or Cloud Source Repositories.  
**GitHub App** | Git | Direct integration with GitHub. Allows fine-grained permissions. | Only supported for repositories hosted in GitHub.  
  
Config Sync also supports the following authentication methods; however, these methods are only recommended if you can't use one of the options listed in the preceding table:

  * **cookiefile:** might not be supported for all Git providers. Not supported for OCI or Helm.
  * **Compute Engine default service account (`gcenode`):** not recommended because this method only works if Workload Identity Federation for GKE is disabled. Supported for Git, OCI, and Helm.
  * **Google service account for Helm and OCI:** supported, but not recommended because the Kubernetes service account method requires less configuration.



## Before you begin

Before you grant Config Sync read-only access to your source of truth, complete the following tasks:

  * Prepare, or have access to, an OCI image or Helm repository where you store your configuration files that you want Config Sync to sync. For more information, see the following resources:

    * [Add configs to a source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/configs): conceptual information about configurations.
    * [GitOps best practices](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/gitops-best-practices): tips and general best practices for organizing and managing your repository.
    * [Use an unstructured repo](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/unstructured-repo): recommendations for using and organizing an unstructured repository.
  * Create, or have access to, a GKE cluster. Before creating a cluster, [review cluster configuration requirements and recommendations for Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/cluster-requirements).


**Important:** Protect any Secrets or sensitive information created as part of the steps on this page. For example, you can delete the file if you don't need it, or store it in a secure way.

## Grant access to an OCI image

This section describes how to grant Config Sync read-only access to OCI images by using a supported authentication method.

You must store OCI images in Artifact Registry to authenticate to Config Sync.

### Use a token

To use a token to grant Config Sync read-only access to your OCI repository, create a Secret that uses your OCI repository username and password:
    
    
    kubectl create secret generic SECRET_NAME \
          --namespace=config-management-system \
          --from-literal=username=USERNAME \
          --from-literal=password=PASSWORD
    

Replace the following:

  * `SECRET_NAME`: a name for your Secret.
  * `USERNAME`: your OCI repository username.
  * `PASSWORD`: your OCI repository password.



When you install Config Sync, use token (`token`) as the authentication type. You must also specify the Secret name in the `spec.oci.secretRef.name` field.

### Use a Kubernetes ServiceAccount

To authenticate with a Kubernetes ServiceAccount, your cluster must have [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) or [fleet Workload Identity Federation for GKE](https://docs.cloud.google.com/anthos/fleet-management/docs/use-workload-identity) enabled.

To grant Config Sync read-only access to your OCI image by using a Kubernetes ServiceAccount, complete the following steps:

  1. To get the permissions that you need to create a policy binding, ask your administrator to grant you the following IAM roles: 

     * Grant project-wide access: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the project 
     * Grant repository-specific access: [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`) on the repository 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  2. Grant the Artifact Registry Reader role (`roles/artifactregistry.reader`) on the project or repository to the Kubernetes ServiceAccount:

     * Grant project-wide permission if the same permissions apply to all repositories in the project.
           
           gcloud projects add-iam-policy-binding PROJECT_ID \
                --role=roles/artifactregistry.reader \
                --member="principal://iam.googleapis.com/projects/FLEET_HOST_PROJECT_NUMBER/locations/global/workloadIdentityPools/FLEET_HOST_PROJECT_ID.svc.id.goog/subject/ns/config-management-system/sa/KUBERNETES_SERVICEACCOUNT" \
                --condition=None
           

     * Grant repository-specific permission when you want service accounts to have different levels of access for each repository in your project.
           
           gcloud artifacts repositories add-iam-policy-binding REPOSITORY \
               --location=LOCATION \
               --role=roles/artifactregistry.reader \
               --member="principal://iam.googleapis.com/projects/FLEET_HOST_PROJECT_NUMBER/locations/global/workloadIdentityPools/FLEET_HOST_PROJECT_ID.svc.id.goog/subject/ns/config-management-system/sa/KUBERNETES_SERVICEACCOUNT" \
               --project=PROJECT_ID \
               --condition=None
           

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `FLEET_HOST_PROJECT_NUMBER`: if you use Workload Identity Federation for GKE, this value is the same as your project number. If you use fleet Workload Identity Federation for GKE, this value is the project number of the fleet that your cluster is registered to.
     * `FLEET_HOST_PROJECT_ID`: if you use Workload Identity Federation for GKE, this value is the same as the project ID. If you use fleet Workload Identity Federation for GKE, this value is the project ID of the fleet that your cluster is registered to.
     * `KUBERNETES_SERVICEACCOUNT`: the Kubernetes ServiceAccount for the reconciler. In most cases, the value is `root-reconciler` because Config Sync automatically creates a `RootSync` object named `root-sync` when installed with the Google Cloud console or the Google Cloud CLI. Otherwise, use `root-reconciler-ROOT_SYNC_NAME` as the value.
     * `REPOSITORY`: the ID of the repository.
     * `LOCATION`: the regional or multi-regional location of the repository.



When you install Config Sync, use Kubernetes ServiceAccount (`k8sserviceaccount`) as the authentication type.

### Use a Compute Engine default service account

As an alternative to a Google service account, if you don't have Workload Identity Federation for GKE enabled, you can use a Compute Engine service account to authenticate.

To use a Compute Engine default service account to grant Config Sync read-only access to your repository, grant the Compute Engine service account read permission to Artifact Registry:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
          --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
          --role=roles/artifactregistry.reader
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `PROJECT_NUMBER`: your project number.



When you install Config Sync, use Compute Engine service account (`gcenode`) as the authentication type.

## Grant access to a Helm repository

This section describes how to grant Config Sync read-only access to Helm charts stored in a repository.

**Caution:** Config Sync doesn't support configuring `helm` as the source type using the Google Cloud console or the Google Cloud CLI. You can configure your `RootSync` or `RepoSync` object to sync from a Helm repository using the [Kubernetes API](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories#kubernetes-api), or [declare it in another source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories#managed-control). For more information, see [Configuration for the Helm repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields#configuration_for_the_helm_repository).

### Use a token

To use a token to grant Config Sync read-only access to your Helm repository, create a Secret that uses your Helm repository username and password:
    
    
    kubectl create secret generic SECRET_NAME \
          --namespace=config-management-system \
          --from-literal=username=USERNAME \
          --from-literal=password=PASSWORD
    

Replace the following:

  * `SECRET_NAME`: a name for your Secret.
  * `USERNAME`: your Helm repository username.
  * `PASSWORD`: your Helm repository password.



When you install Config Sync, use token (`token`) as the authentication type. You must also specify the Secret name in the `spec.helm.secretRef.name` field.

### Use a Kubernetes ServiceAccount

To authenticate by using a Kubernetes ServiceAccount, you must meet the following requirements:

  * Your repository is in Artifact Registry.
  * Your cluster has [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) or [fleet Workload Identity Federation for GKE](https://docs.cloud.google.com/anthos/fleet-management/docs/use-workload-identity) enabled.



To use a Kubernetes ServiceAccount to grant Config Sync read-only access to your Helm repository, complete the following steps:

  1. To get the permissions that you need to create a policy binding, ask your administrator to grant you the following IAM roles: 

     * Grant project-wide access: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the project 
     * Grant repository-specific access: [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`) on the repository 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  2. Grant the Artifact Registry Reader role (`roles/artifactregistry.reader`) on the project or repository to the Kubernetes ServiceAccount:

     * Grant project-wide permission if the same permissions apply to all repositories in the project.
           
           gcloud projects add-iam-policy-binding PROJECT_ID \
                --role=roles/artifactregistry.reader \
                --member="principal://iam.googleapis.com/projects/FLEET_HOST_PROJECT_NUMBER/locations/global/workloadIdentityPools/FLEET_HOST_PROJECT_ID.svc.id.goog/subject/ns/config-management-system/sa/KUBERNETES_SERVICEACCOUNT" \
                --condition=None
           

     * Grant repository-specific permission when you want service accounts to have different levels of access for each repository in your project.
           
           gcloud artifacts repositories add-iam-policy-binding REPOSITORY \
               --location=LOCATION \
               --role=roles/artifactregistry.reader \
               --member="principal://iam.googleapis.com/projects/FLEET_HOST_PROJECT_NUMBER/locations/global/workloadIdentityPools/FLEET_HOST_PROJECT_ID.svc.id.goog/subject/ns/config-management-system/sa/KUBERNETES_SERVICEACCOUNT" \
               --project=PROJECT_ID \
               --condition=None
           

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `FLEET_HOST_PROJECT_NUMBER`: if you use Workload Identity Federation for GKE, this value is the same as your project number. If you use fleet Workload Identity Federation for GKE, this value is the project number of the fleet that your cluster is registered to.
     * `FLEET_HOST_PROJECT_ID`: if you use Workload Identity Federation for GKE, this value is the same as project ID. If you use fleet Workload Identity Federation for GKE, this value is the project ID of the fleet that your cluster is registered to.
     * `KUBERNETES_SERVICEACCOUNT`: the Kubernetes ServiceAccount for the reconciler. In most cases, the value is `root-reconciler` because Config Sync automatically creates a `RootSync` object named `root-sync` when installed with the Google Cloud console or the Google Cloud CLI. Otherwise, use `root-reconciler-ROOT_SYNC_NAME` as the value.
     * `REPOSITORY`: the ID of the repository.
     * `LOCATION`: the regional or multi-regional location of the repository.



When you install Config Sync, use Kubernetes ServiceAccount (`k8sserviceaccount`) as the authentication type.

### Use a Compute Engine default service account

As an alternative to a Google service account, if you don't have Workload Identity Federation for GKE enabled, you can use a Compute Engine service account to authenticate.

To use a Compute Engine default service account to grant Config Sync read-only access to your repository, grant the Compute Engine service account read permission to Artifact Registry:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
          --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
          --role=roles/artifactregistry.reader
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `PROJECT_NUMBER`: your project number.



When you install Config Sync, use Compute Engine service account (`gcenode`) as the authentication type.

## What's next

  * [Install Config Sync with default settings](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/install-default)
  * [Customize your Config Sync installation](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
