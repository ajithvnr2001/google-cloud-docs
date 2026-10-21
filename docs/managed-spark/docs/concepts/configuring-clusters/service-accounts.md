---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts/
title: Managed Service for Apache Spark service accounts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:37.009514+00:00
---

# Managed Service for Apache Spark service accounts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark service accounts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes service accounts and VM access scopes and how they are used with Managed Service for Apache Spark.

**Security requirement beginning August 3, 2020:** Managed Service for Apache Spark users are required to have [service account `ActAs` permission](https://docs.cloud.google.com/iam/docs/service-accounts-actas) to deploy Managed Service for Apache Spark resources, such as creating clusters and submitting jobs. The [**Service Account User**](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) role contains this permission. See [Roles for service account authentication](https://docs.cloud.google.com/iam/docs/service-account-permissions) for information about required Managed Service for Apache Spark roles.

**Opt-in for existing Managed Service for Apache Spark users:** Existing Managed Service for Apache Spark users as of August 3, 2020 can opt in to this security requirement (see [Securing Managed Service for Apache Spark, Dataflow, and Cloud Data Fusion](https://docs.cloud.google.com/iam/docs/service-accounts-actas#dataproc-dataflow-datafusion)).

## What are service accounts?

A [service account](https://docs.cloud.google.com/compute/docs/access/service-accounts) is a special account that can be used by services and applications running on a Compute Engine virtual machine (VM) instance to interact with other Google Cloud APIs. Applications can use service account credentials to authorize themselves to a set of APIs and perform actions on the VM within the permissions granted to the service account.

**Use your identity instead of a VM service account.** See [Managed Service for Apache Spark Personal Cluster Authentication](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/personal-auth) to run interactive workloads on a cluster as your [ user identity](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#api_user_user_identity).

## Managed Service for Apache Spark cluster service accounts

The following service accounts must have the permissions necessary to perform Managed Service for Apache Spark actions in the project where your cluster is located.

### Managed Service for Apache Spark VM service account

The VMs in a Managed Service for Apache Spark cluster use a service account for Managed Service for Apache Spark [data plane operations](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#vm_service_account_data_plane_identity). The [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), `project_number-compute@developer.gserviceaccount.com`, is used as the VM service account unless you [specify a custom service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#create_a_cluster_with_a_custom_vm_service_account) when you create a cluster. The VM service account must have the [Managed Service for Apache Spark Worker](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#dataproc.worker) role, which includes the permissions required for Managed Service for Apache Spark data plane operations. For more information, see [Managed Service for Apache Spark roles](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#dataproc-roles).

**Note:** For successful Managed Service for Apache Spark cluster operation, the [Managed Service for Apache Spark VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#VM_service_account) must have access the Managed Service for Apache Spark [staging and temp buckets](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket). If you modify default VM service account IAM permissions or specify a [custom VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#create_a_cluster_with_a_custom_vm_service_account) for your cluster, you must grant the VM service account the `storage.*` IAM permissions included in the [`roles/dataproc.worker`](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) role. Also see [IAM permissions for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-permissions) and [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

#### View VM service account roles

To view the roles granted to the Managed Service for Apache Spark VM service account, do the following:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/dataproc/interactive)

  2. Click **Include Google-provided role grants**.

  3. View the roles listed for the VM service account. The following image shows the required **Dataproc Worker** role listed for the Compute Engine default service account (`project_number-compute@developer.gserviceaccount.com`) that Managed Service for Apache Spark uses by default as the VM service account.

![](https://docs.cloud.google.com/static/managed-spark/docs/images/iam-vm-service-account-role-in-console.png)
  4. You can click the pencil icon displayed on the service account row to [grant or remove service account roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#multiple-roles-console).




### Managed Service for Apache Spark Service Agent service account

Managed Service for Apache Spark creates the [Service Agent service account](https://docs.cloud.google.com/managed-spark/docs/guides/principals#service_agent_control_plane_identity), `service-project_number@dataproc-accounts.iam.gserviceaccount.com`, and grants the service account the [Managed Service for Apache Spark Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) role in a Google Cloud project. This service account performs [Managed Service for Apache Spark control plane](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#service_agent_control_plane_identity) operations, such as the creation, update, and deletion of cluster VMs. You can't replace this service account with a custom VM service account when you create a cluster.

To view Managed Service for Apache Spark service agent roles on a project, click "Include Google-provided role grants" on the [Identity and Access Management](https://console.cloud.google.com/iam-admin/iam) page in the Google Cloud console. **Note:** The Managed Service for Apache Spark service agent service account is not be listed on the IAM page if it does not have any roles on the project.

#### Role grant to Service Agent service account in a Shared VPC network

If a Managed Service for Apache Spark cluster uses a Shared VPC network, a Shared VPC Admin must grant the [**Managed Service for Apache Spark Service Agent service account**](https://docs.cloud.google.com/managed-spark/docs/guides/principals#service_agent_control_plane_identity) the role of [Network User](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) for the Shared VPC host project. For more information, see the following:

  * [Create a cluster that uses a VPC network in another project](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/network#create-a-cluster-that-uses-a-vpc-network-in-another-project)
  * [Shared VPC documentation: configuring service accounts as Service Project Admins](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#sa-as-spa)



## Create a cluster with a custom VM service account

When you create a cluster, you can specify a custom [VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#vm_service_account_data_plane_identity) that your cluster will use for Managed Service for Apache Spark data plane operations instead of the default VM service account (you can't change the VM service account after the cluster is created). Using a VM service account with assigned [IAM roles](https://docs.cloud.google.com/iam/docs) lets you provide your cluster with fine-grained access to project resources.

**Objective:** This section shows you how to specify a custom VM service account when you create a cluster. See Create a cluster with a custom VM service account from another project to specify a VM service account from a different project.

### Preliminary steps

  1. [Create the custom VM service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account) within the project where the cluster will be created.

  2. Grant the custom VM service account the [Managed Service for Apache Spark Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) role on the project and any additional roles needed by your jobs, such as the BigQuery [Reader and Writer](https://docs.cloud.google.com/bigquery/docs/access-control-basic-roles#dataset-basic-roles) roles (see [Managed Service for Apache Spark roles](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#dataproc-roles)).

**gcloud CLI example:**

     * The following sample command grants the custom VM service account in the cluster project the Dataproc Worker role at the project level:
    
    gcloud projects add-iam-policy-binding CLUSTER_PROJECT_ID \
        --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
        --role="roles/dataproc.worker"
     

     * **Consider a custom role:** Instead of granting service account the predefined Dataproc Worker role (`roles/dataproc.worker`), you can grant the service account a custom role that contains Worker role permissions but limits the [`storage.objects.*`](https://docs.cloud.google.com/storage/docs/access-control/iam-permissions#object_permissions) permissions. 
       * The custom role must at least grant the VM service account `storage.objects.create`, `storage.objects.get`, and `storage.objects.update` permissions on the objects in the [Managed Service for Apache Spark staging and temp buckets](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket) and on any additional buckets needed by jobs that will run on the cluster.



### Create the cluster

  * Create the cluster in your project.



### Google Cloud console

Setting a Managed Service for Apache Spark VM service account in the console is not supported. To set the `cloud-platform` access scope on cluster VMs when you create the cluster:

  1. Open the [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Security**.
  4. In the panel that opens, under **Project access** , select the checkbox for **Enables the cloud-platform scope for this cluster**.



### gcloud CLI

Use the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command to create a cluster with the custom VM service account.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
        --scopes=SCOPE

Replace the following:

  * CLUSTER_NAME: The cluster name, which must be unique within a project. The name must start with a lowercase letter, and can contain up to 51 lowercase letters, numbers, and hyphens. It cannot end with a hyphen. The name of a deleted cluster can be reused.
  * REGION: The [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the cluster will be located.
  * SERVICE_ACCOUNT_NAME: The service account name.
  * PROJECT_ID: The Google Cloud project ID of the project containing your VM service account. This will be the ID of the project where your cluster will be created or the ID of another project if you are creating a cluster with a custom VM service account in another project. 
  * SCOPE: [Access scope(s)](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#dataproc_vm_access_scopes) for cluster VM instances (for example, `https://www.googleapis.com/auth/cloud-platform`).



### REST API

When completing the [`GceClusterConfig`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#GceClusterConfig) as part of the [`clusters.create`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) API request, set the following fields:

  * [`serviceAccount`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#GceClusterConfig.FIELDS.service_account): The service account will be located in the project where your cluster will be created unless you are using a VM service account from a different project.
  * [`serviceAccountScopes`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#GceClusterConfig.FIELDS.service_account_scopes): Specify the [access scope(s)](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#dataproc_vm_access_scopes) for cluster VM instances (for example, `https://www.googleapis.com/auth/cloud-platform`).



## Create a cluster with a custom VM service account from another project

When you create a cluster, you can specify a custom [VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#vm_service_account_data_plane_identity) that your cluster will use for Managed Service for Apache Spark data plane operations instead of using the default VM service account (you can't specify a custom VM service account after the cluster is created). Using a custom VM service account with assigned [IAM roles](https://docs.cloud.google.com/iam/docs) allows you to provide your cluster with fine-grained access to project resources.

**Objective:** This section shows you how to specify a custom VM service account for your cluster from a project that is different from the project where your cluster will be created. We refer to this project as the "service account project" to distinguish it from the project where your cluster will be created (the "cluster project"). See Create a cluster with a custom VM service account to use a custom VM service account from the project where the cluster will be created .

### Preliminary steps

  1. In the service account project (the project where the custom VM service account is located):

     1. [Enable service accounts to be attached across projects](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project).

     2. Enable the Dataproc API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com)

  2. Grant to your email account (the user who is creating the cluster) the [Service Account User](https://docs.cloud.google.com/iam/docs/service-accounts#user-role) role on either the service account project or, for more granular control, the custom VM service account in the service account project.

**For more information:** See [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to grant roles at the project level and [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts) grant roles at the service account level.

**gcloud CLI examples:**

     * The following sample command grants to the user the Service Account User role at the project level:
    
    gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
        --member=USER_EMAIL \
        --role="roles/iam.serviceAccountUser"
    

Notes: `USER_EMAIL`: Provide your user account email address, in the format: `user:user-name@example.com`.

     * The following sample command grants to the user the Service Account User role at the service account level:
    
    gcloud iam service-accounts add-iam-policy-binding VM_SERVICE_ACCOUNT_EMAIL \
        --member=USER_EMAIL \
        --role="roles/iam.serviceAccountUser"
    

Notes: `USER_EMAIL`: Provide your user account email address, in the format: `user:user-name@example.com`.

  3. Grant the custom VM service account the [Managed Service for Apache Spark Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) role on the cluster project.

**gcloud CLI example:**
         
         gcloud projects add-iam-policy-binding CLUSTER_PROJECT_ID \
             --member=serviceAccount:SERVICE_ACCOUNT_NAME@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com \
             --role="roles/dataproc.worker"
          

  4. Grant the Managed Service for Apache Spark Service Agent service account in the cluster project the [Service Account User](https://docs.cloud.google.com/iam/docs/service-accounts#user-role) and the [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/service-accounts#token-creator-role) roles on either the service account project or, for more granular control, the custom VM service account in the service account project. By doing this, you allow the Dataproc service agent service account in the cluster project to create tokens for the custom Dataproc VM service account in the service account project.

**For more information:** See [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to grant roles at the project level and [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts) grant roles at the service account level.

**gcloud CLI examples:**

     * The following sample commands grant the Managed Service for Apache Spark Service Agent service account in the cluster project the Service Account User and Service Account Token Creator roles at the project level:
    
    gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
        --member=serviceAccount:service-CLUSTER_PROJECT_NUMBER@dataproc-accounts.iam.gserviceaccount.com \
        --role="roles/iam.serviceAccountUser"
     
    
    gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
        --member=serviceAccount:service-CLUSTER_PROJECT_NUMBER@dataproc-accounts.iam.gserviceaccount.com \
        --role="roles/iam.serviceAccountTokenCreator"
    

     * The following sample commands grant the Managed Service for Apache Spark Service Agent service account in the cluster project the Service Account User and Service Account Token Creator roles at the VM service account level:
    
    gcloud iam service-accounts add-iam-policy-binding VM_SERVICE_ACCOUNT_EMAIL \
        --member=serviceAccount:service-CLUSTER_PROJECT_NUMBER@dataproc-accounts.iam.gserviceaccount.com \
        --role="roles/iam.serviceAccountUser"
     
    
    gcloud iam service-accounts add-iam-policy-binding VM_SERVICE_ACCOUNT_EMAIL \
        --member=serviceAccount:service-CLUSTER_PROJECT_NUMBER@dataproc-accounts.iam.gserviceaccount.com \
        --role="roles/iam.serviceAccountTokenCreator"
    

**Note:** Note: In clusters created with Managed Service for Apache Spark image versions prior to 2.0.58, 2.1.4, or 2.2.1 (released in 2023), you must also grant the [Google APIs Service Agent service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#google_apis_service_agent) (`PROJECT_NUMBER@cloudservices.gserviceaccount.com`) in the cluster project the [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/service-accounts#token-creator-role) role on either the service account project or the custom VM service account in the service account project.
  5. Grant the [Compute Engine Service Agent service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#compute_engine_service_account) in the cluster project the [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/service-accounts#token-creator-role) role on either the service account project or, for more granular control, the custom VM service account in the service account project. By doing this, you grant the Compute Agent Service Agent service account in the cluster project the ability to create tokens for the custom Dataproc VM service account in the service account project.

**For more information:** See [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to grant roles at the project level and [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts) grant roles at the service account level.

**gcloud CLI examples:**

     * The following sample command grants the Compute Engine Service Agent service account in the cluster project the Service Account Token Creator role at the project level:
    
    gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
        --member=serviceAccount:service-CLUSTER_PROJECT_NUMBER@compute-system.iam.gserviceaccount.com \
        --role="roles/iam.serviceAccountTokenCreator"
     

     * The following sample command grants the Compute Engine Service Agent service account in the cluster project the Service Account Token Creator role at the VM service account level:
    
    gcloud iam service-accounts add-iam-policy-binding VM_SERVICE_ACCOUNT_EMAIL \
        --member=serviceAccount:service-CLUSTER_PROJECT_NUMBER@compute-system.iam.gserviceaccount.com \
        --role="roles/iam.serviceAccountTokenCreator"
     




### Create the cluster

  * Create the cluster in your project.



## What's next

  * [Service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts)
  * [Managed Service for Apache Spark permissions and IAM roles](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam)
  * [Managed Service for Apache Spark principals and roles](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals)
  * [Managed Service for Apache Spark Service Account Based Secure Multi-tenancy](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/sa-multi-tenancy)
  * [Managed Service for Apache Spark Personal Cluster Authentication](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/personal-auth)
  * [Managed Service for Apache Spark Granular IAM](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/granular-iam)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
