---
url: https://docs.cloud.google.com/kubernetes-engine/security/configure-node-service-accounts/
title: Configure GKE node service accounts \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:08.278124+00:00
---

# Configure GKE node service accounts  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/security/configure-node-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Configure GKE node service accounts Stay organized with collections  Save and categorize content based on your preferences. 

Your Google Kubernetes Engine (GKE) nodes use Identity and Access Management (IAM) service accounts for tasks like logging and pulling container images for workloads. This document shows platform administrators and security engineers how to grant roles to service accounts for specific use cases and how to create custom service accounts instead of using a default service account. For more information, see [Node service accounts](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#node-service-accounts). 

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Required roles

To get the permissions that you need to manage IAM service accounts and roles, ask your administrator to grant you the following IAM roles: 

  * [Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`) on the cluster project
  * Configure service accounts in a separate project: [Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`) on the service account project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Grant the minimum required role for GKE

GKE uses IAM service accounts that are attached to your nodes to run system tasks like logging and monitoring. At a minimum, these _node service accounts_ must have the [Kubernetes Engine Default Node Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAccount) (`roles/container.defaultNodeServiceAccount`) role on your project. By default, GKE uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), which is automatically created in your project, as the node service account. 

If your organization enforces the [`iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants), the default Compute Engine service account in your project might not automatically get the required permissions for GKE. 

**Note** : If your organization was created on or after May 3, 2024, this constraint is enforced by default. 

The following sections show you how to grant the `roles/container.defaultNodeServiceAccount` role to the default Compute Engine service account or to a new custom service account that you create.

**Best practice** : 

Create a custom service account for your nodes instead of using the default Compute Engine service account.

### Configure the default Compute Engine service account

To grant the `roles/container.defaultNodeServiceAccount` role to the Compute Engine default service account, complete the following steps:

### Console

  1. Go to the **Welcome** page: 

[Go to Welcome](https://console.cloud.google.com/welcome)

  2. In the **Project number** field, click content_copy **Copy to clipboard**.
  3. Go to the **IAM** page: 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  4. Click person_add **Grant access**.
  5. In the **New principals** field, specify the following value: 
         
         PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with the project number that you copied. 
  6. In the **Select a role** menu, select the **Kubernetes Engine Default Node Service Account** role.
  7. Click **Save**.



### gcloud

  1. Find your Google Cloud project number: 
         
         gcloud projects describe PROJECT_ID \
             --format="value(projectNumber)"

Replace `PROJECT_ID` with your project ID.

The output is similar to the following:
         
         12345678901
         

  2. Grant the `roles/container.defaultNodeServiceAccount` role to the Compute Engine default service account: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
             --role="roles/container.defaultNodeServiceAccount"

Replace `PROJECT_NUMBER` with the project number from the previous step.




### Configure a custom node service account

To create a custom service account and grant it the required role for GKE, complete the following steps:

### Console

  1. Go to the **Service accounts** page: 

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click add **Create service account**.
  3. Enter a name for the service account. The **Service account ID** field automatically generates a unique ID for the service account based on the name.
  4. Click **Create and continue**.
  5. In the **Select a role** menu, select the **Kubernetes Engine Default Node Service Account** role.
  6. Click **Done**.



### gcloud

  1. Create the service account: 
         
         gcloud iam service-accounts create SA_NAME

Replace`SA_NAME` with a unique name that identifies the service account.

  2. Grant the [Kubernetes Engine Default Node Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAccount) (`roles/container.defaultNodeServiceAccount`) role to the service account: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SA_NAME@PROJECT_ID.iam.gserviceaccount.com" \
             --role=roles/container.defaultNodeServiceAccount

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `SA_NAME`: the name of the service account that you created.



### Terraform

Create an IAM service account and grant it the `roles/container.defaultNodeServiceAccount` role on the project:
    
    
    resource "google_service_account" "default" {
      account_id   = "gke-node-service-account"
      display_name = "GKE node service account"
    }
    
    data "google_project" "project" {
    }
    
    resource "google_project_iam_member" "default" {
      project = data.google_project.project.project_id
      role    = "roles/container.defaultNodeServiceAccount"
      member  = "serviceAccount:${google_service_account.default.email}"
    }

### Config Connector

**Note:** This step requires [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview). Follow the [installation instructions](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall) to install Config Connector on your cluster.

  1. To create the service account, download the following resource as `service-account.yaml`: 
         
         apiVersion: iam.cnrm.cloud.google.com/v1beta1
         kind: IAMServiceAccount
         metadata:
           name: [SA_NAME]
         spec:
           displayName: [DISPLAY_NAME]

Replace the following:

     * `[SA_NAME]`: the name of the new service account.
     * `[DISPLAY_NAME]`: a display name for the service account.
  2. Create the service account: 
         
         kubectl apply -f service-account.yaml

  3. Apply the `roles/logging.logWriter` role to the service account: 
     1. Download the following resource as `policy-logging.yaml`. 
            
            apiVersion: iam.cnrm.cloud.google.com/v1beta1
            kind: IAMPolicyMember
            metadata:
              name: policy-logging
            spec:
              member: serviceAccount:[SA_NAME]@[PROJECT_ID].iam.gserviceaccount.com
              role: roles/logging.logWriter
              resourceRef:
                kind: Project
                name: [PROJECT_ID]

Replace the following:

        * `[SA_NAME]`: the name of the service account.
        * `[PROJECT_ID]`: your Google Cloud project ID.
     2. Apply the role to the service account: 
            
            kubectl apply -f policy-logging.yaml

  4. Apply the `roles/monitoring.metricWriter` role to the service account: 
     1. Download the following resource as `policy-metrics-writer.yaml`. Replace `[SA_NAME]` and `[PROJECT_ID]` with your own information. 
            
            apiVersion: iam.cnrm.cloud.google.com/v1beta1
            kind: IAMPolicyMember
            metadata:
              name: policy-metrics-writer
            spec:
              member: serviceAccount:[SA_NAME]@[PROJECT_ID].iam.gserviceaccount.com
              role: roles/monitoring.metricWriter
              resourceRef:
                kind: Project
                name: [PROJECT_ID]

Replace the following:

        * `[SA_NAME]`: the name of the service account.
        * `[PROJECT_ID]`: your Google Cloud project ID.
     2. Apply the role to the service account: 
            
            kubectl apply -f policy-metrics-writer.yaml

  5. Apply the `roles/monitoring.viewer` role to the service account: 
     1. Download the following resource as `policy-monitoring.yaml`. 
            
            apiVersion: iam.cnrm.cloud.google.com/v1beta1
            kind: IAMPolicyMember
            metadata:
              name: policy-monitoring
            spec:
              member: serviceAccount:[SA_NAME]@[PROJECT_ID].iam.gserviceaccount.com
              role: roles/monitoring.viewer
              resourceRef:
                kind: Project
                name: [PROJECT_ID]

Replace the following:

        * `[SA_NAME]`: the name of the service account.
        * `[PROJECT_ID]`: your Google Cloud project ID.
     2. Apply the role to the service account: 
            
            kubectl apply -f policy-monitoring.yaml

  6. Apply the `roles/autoscaling.metricsWriter` role to the service account: 
     1. Download the following resource as `policy-autoscaling-metrics-writer.yaml`. 
            
            apiVersion: iam.cnrm.cloud.google.com/v1beta1
            kind: IAMPolicyMember
            metadata:
              name: policy-autoscaling-metrics-writer
            spec:
              member: serviceAccount:[SA_NAME]@[PROJECT_ID].iam.gserviceaccount.com
              role: roles/autoscaling.metricsWriter
              resourceRef:
                kind: Project
                name: [PROJECT_ID]

Replace the following:

        * `[SA_NAME]`: the name of the service account.
        * `[PROJECT_ID]`: your Google Cloud project ID.
     2. Apply the role to the service account: 
            
            kubectl apply -f policy-autoscaling-metrics-writer.yaml




You can also use this service account for resources in other projects. For instructions, see [Enabling service account impersonation across projects](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project).

## Allow principals to attach custom service accounts

You can attach a custom service account when you create a cluster or a node pool. To let a principal (such as a platform administrator) use a custom service account to create GKE resources, grant the [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) role on the custom service account to that principal. To grant this role, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Service accounts** page:

[Go to Service accounts](https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts?supportedpurview=project)

In the resource selector, choose the project that contains your custom service account.

  2. Select the checkbox for the custom service account that you created to use with GKE nodes.

  3. Click person_add **Manage access**. The **Manage Access** pane opens.

  4. Click person_add **Add principal**. The **Grant access** pane opens.

  5. In the **New principals** field, specify the principal, such as an administrator group.

  6. In the **Select a role** drop-down menu, select the **Service Account User** role.

  7. Click **Save**. The **Grant access** pane closes.

  8. Close the **Manage Access** pane.




###  gcloud 

Grant the `roles/iam.serviceAccountUser` role:
    
    
    gcloud iam service-accounts add-iam-policy-binding \
        SA_NAME@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com \
        --member=PRINCIPAL \
        --role=roles/iam.serviceAccountUser
    

Replace the following:

  * `SA_NAME`: the name of the custom service account.
  * `SERVICE_ACCOUNT_PROJECT_ID`: the project ID that contains the custom service account.
  * `PRINCIPAL`: the [principal identifier](https://docs.cloud.google.com/iam/docs/principal-identifiers), such as `user:baklavainthebalkans@example.com`.



### Config Connector

**Note:** This step requires [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview). Follow the [installation instructions](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall) to install Config Connector on your cluster.

Apply the `iam.serviceAccountUser` role to your service account. Download the following resource as `policy-service-account-user.yaml`. Replace `[SA_NAME]` and `[PROJECT_ID]` with your own information. 
    
    
    apiVersion: iam.cnrm.cloud.google.com/v1beta1
    kind: IAMPolicyMember
    metadata:
      name: policy-service-account-user
    spec:
      member: serviceAccount:[SA_NAME]@[PROJECT_ID].iam.gserviceaccount.com
      role: roles/iam.serviceAccountUser
      resourceRef:
        kind: Project
        name: [PROJECT_ID]
    
    
    kubectl apply -f policy-service-account-user.yaml

After you grant the role on the service account, those principals can use that service account to create clusters and node pools. For more information, see the following documents:

  * [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster)
  * [Creating a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster)
  * [Add a node pool to a Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#add)



### Configure service account usage across projects

If your node service account isn't in the same project as your cluster, service agents in the cluster project need additional permissions on the service account. For more information, see [Node service accounts and project service agents](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#service-accounts-and-agents).

To grant the required roles on node service accounts that aren't in your cluster project, follow these steps:

  1. To enable cross-project service account attachment, [update your organization policies](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project).
  2. To grant the required roles on the custom service account to the service agents in your cluster project, select one of the following options:

###  Console 

     1. In the Google Cloud console, go to the **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts?supportedpurview=project)

     2. Select the checkbox for the custom service account that you created to use with GKE nodes.

     3. Click person_add **Manage access**. The **Manage Access** pane opens.

     4. Grant the Service Account Token Creator role to the Compute Engine service agent in your cluster project:

        1. In the **Manage Access** pane, click person_add **Add principal**. The **Grant access** pane opens.
        2. In the **New principals** field, specify the email address of the Compute Engine service agent in your cluster project:
               
               service-CLUSTER_PROJECT_NUMBER@compute-system.iam.gserviceaccount.com
               

Replace `CLUSTER_PROJECT_NUMBER` with the project number of your cluster project.

        3. In the **Select a role** menu, select the **Service Account Token Creator** role.

        4. Click **Save**. The **Grant access** pane closes.

     5. Grant the Service Account User role to the GKE service agent in your cluster project:

        1. In the **Manage Access** pane, click person_add **Add principal**. The **Grant access** pane opens.
        2. In the **New principals** field, specify the email address of the GKE service agent in your cluster project:
               
               service-CLUSTER_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com
               

        3. In the **Select a role** menu, select the **Service Account User** role.

        4. Click **Save**. The **Grant access** pane closes.

     6. Close the **Manage Access** pane.

###  gcloud 

     1. Get the project number of your cluster project:
            
            gcloud projects describe CLUSTER_PROJECT_ID \
                --format='value(projectNumber)'
            

Replace `CLUSTER_PROJECT_ID` with the project ID of your cluster project.

The output is similar to `123456789`.

     2. Grant the `roles/iam.serviceAccountTokenCreator` role on the custom service account to the Compute Engine service agent in your cluster project:
            
            gcloud iam service-accounts add-iam-policy-binding \
                SA_NAME@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com \
                --member=serviceAccount:service-CLUSTER_PROJECT_NUMBER@compute-system.iam.gserviceaccount.com \
                --role=roles/iam.serviceAccountTokenCreator
            

Replace the following:

        * `SA_NAME`: the name of the custom service account.
        * `SERVICE_ACCOUNT_PROJECT_ID`: the project ID of the project that contains your custom service account.
        * `CLUSTER_PROJECT_NUMBER`: the project number of your cluster project.
     3. Grant the `roles/iam.serviceAccountUser` role on the custom service account to the GKE service agent in your cluster project:
            
            gcloud iam service-accounts add-iam-policy-binding \
                SA_NAME@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com \
                --member=serviceAccount:service-CLUSTER_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com \
                --role=roles/iam.serviceAccountUser
            




## Allow image pulls from private repositories

If you have images in private Artifact Registry repositories, you must give your node service account access to those repositories. Even if you use the default Compute Engine service account, you might need to give the service account access to your repository if the repository is in another project.

**Note:** The steps in this section give access to the repository only to your node service account. The workloads in your cluster don't get this access. To give your GKE workloads access to Google Cloud resources, use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

To pull private images from Artifact Registry, grant the [Artifact Registry Reader role](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) on the repository to your node service account.

###  Console 

  1. In the Google Cloud console, go to the **Repositories** page.

[Go to Repositories](https://console.cloud.google.com/projectselector2/artifacts?supportedpurview=project)

  2. Select the checkbox for your repository.

  3. Click **Show info panel**. The repository information pane opens.

  4. In the **Permissions** tab, click person_add **Add principal**. The **Grant access** pane opens.

  5. In the **New principals** field, specify the [email address of your node service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#node-service-accounts).

  6. Click **Select a role** to open the role selection dialog.

  7. Select the **Artifact Registry Reader** role.

  8. Click **Save**.




###  gcloud 

Grant the `roles/artifactregistry.reader` role on the repository:
    
    
    gcloud artifacts repositories add-iam-policy-binding REPOSITORY_NAME \
        --member=serviceAccount:SERVICE_ACCOUNT_EMAIL \
        --project=REPOSITORY_PROJECT_ID \
        --role=roles/artifactregistry.reader
    

Replace the following:

  * `REPOSITORY_NAME`: the name of the Artifact Registry repository.
  * `SERVICE_ACCOUNT_EMAIL`: the [email address of your node service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#node-service-accounts).
  * `REPOSITORY_PROJECT_ID`: the project ID of the project that contains your repository.



### Config Connector

**Note:** This step requires [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview). Follow the [installation instructions](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall) to install Config Connector on your cluster.

**Note:** These steps assume that you use Config Connector to manage your Artifact Registry repository. If your repository doesn't exist as a Config Connector resource, these steps won't work.

  1. Save the following manifest as `policy-artifact-registry-reader.yaml`:
         
         apiVersion: iam.cnrm.cloud.google.com/v1beta1
         kind: IAMPolicyMember
         metadata:
           name: policy-artifact-registry-reader
         spec:
           member: serviceAccount:"SA_NAME"@"PROJECT_ID".iam.gserviceaccount.com
           role: roles/artifactregistry.reader
           resourceRef:
             apiVersion: artifactregistry.cnrm.cloud.google.com/v1beta1
             kind: ArtifactRegistryRepository
             name: "REPOSITORY_NAME"

Replace the following:

     * SA_NAME: the name of your IAM service account.
     * PROJECT_ID: your Google Cloud project ID.
     * REPOSITORY_NAME: the name of your Artifact Registry repository.
  2. Grant the Artifact Registry Reader role to the service account:
         
         kubectl apply -f policy-artifact-registry-reader.yaml
         




## What's next

  * [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster)
  * [Create a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster)
  * [Add a node pool to a Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#add)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
