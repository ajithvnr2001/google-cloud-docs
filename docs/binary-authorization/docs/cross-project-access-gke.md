---
url: https://docs.cloud.google.com/binary-authorization/docs/cross-project-access-gke/
title: Configure cross-project access in GKE \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:10.523936+00:00
---

# Configure cross-project access in GKE  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/cross-project-access-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Configure cross-project access in GKE Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to give Binary Authorization access to policies and container images that exist in different Google Cloud projects than your current project. For example, if you deploy images in your Google Kubernetes Engine (GKE) cluster from an Artifact Registry or Container Registry ([Deprecated](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation)) repository that's owned by a different project, you'll need to give the Binary Authorization service in your project access to the image metadata in the source repository.

## Terminology

This document uses the following terms:

  * **Service agent:** A Google Cloud-managed service account. Binary Authorization uses a service agent to interact with your Google Cloud resources, like GKE clusters.
  * **Policy project:** The Google Cloud project that contains your Binary Authorization policy.
  * **Cluster project:** The Google Cloud project that contains your GKE cluster.
  * **Artifact project:** The Google Cloud project that contains your Artifact Registry or Container Registry ([Deprecated](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation)) repository.



## Scenarios that require cross-project access

You must grant cross-project permissions in situations like the following:

  * Your policy project is different than your cluster project.
  * Your cluster project is different than your artifact project.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Binary Authorization API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable binaryauthorization.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Binary Authorization API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable binaryauthorization.googleapis.com




## Cluster project different than the policy project

Grant the Binary Authorization service agent in the cluster project the [Binary Authorization Policy Evaluator](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEvaluator) (`roles/binaryauthorization.policyEvaluator`) role on the policy project.
    
    
    gcloud projects add-iam-policy-binding POLICY_PROJECT_ID \
      --member="serviceAccount:service-$(gcloud projects describe CLUSTER_PROJECT_ID --format='value(projectNumber)')@gcp-sa-binaryauthorization.iam.gserviceaccount.com" \
      --role=roles/binaryauthorization.policyEvaluator

Replace the following: 

  * `POLICY_PROJECT_ID`: the ID of the project that contains your policy.
  * `CLUSTER_PROJECT_ID`: the project ID of the cluster.



## Cluster project different than the artifact project

Grant the Binary Authorization service agent in the cluster project the [Artifact Registry Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) role on the artifact project.
    
    
    gcloud projects add-iam-policy-binding ARTIFACT_PROJECT_ID \
        --member="serviceAccount:service-$(gcloud projects describe CLUSTER_PROJECT_ID --format='value(projectNumber)')@gcp-sa-binaryauthorization.iam.gserviceaccount.com" \
        --role=roles/artifactregistry.reader

Replace the following: 

  * `ARTIFACT_PROJECT_ID`: the ID of the project that contains your Artifact Registry repository. **Note:** If you use Container Registry, you can use the [Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) role, but we recommend that you migrate to Artifact Registry. Container Registry is deprecated. For migration instructions, see [Transition from Container Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/transition-from-gcr).
  * `CLUSTER_PROJECT_ID`: the project ID that runs your GKE clusters.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
