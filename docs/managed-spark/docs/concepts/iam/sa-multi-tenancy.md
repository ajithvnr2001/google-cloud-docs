---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/iam/sa-multi-tenancy/
title: Create a multi-tenant cluster using service accounts \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:40.551099+00:00
---

# Create a multi-tenant cluster using service accounts  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/iam/sa-multi-tenancy/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Create a multi-tenant cluster using service accounts Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark service-account-based secure multi-tenancy lets you share a cluster with multiple users, with a set of user accounts mapped to service accounts when the cluster is created. Users can submit interactive workloads, such as Jupyter notebook, to kernels running on the multi-tenant cluster with isolated user environments.

When a user submits a job to the multi-tenant cluster:

  * The job runs as a specific OS user with a specific Kerberos principal.

  * The job accesses Google Cloud resources using a mapped service account.




This document shows you how to create a Managed Service for Apache Spark multi-tenant cluster, and then launch and connect a Jupyter notebook to a PySpark Kernel running on the cluster.

## Considerations and limitations

When you create a multi-tenant cluster:

  * The cluster is available only to Google Account users with mapped service accounts. Google groups can't be mapped. Unmapped users can't run jobs on the cluster.

  * [Kerberos](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/security) is enabled and configured on the cluster for secure intra-cluster communication. End user authentication through Kerberos is not supported.

  * Direct SSH access to the cluster and Compute Engine features, such as the ability to run startup scripts on cluster VMs, are blocked. Also, jobs cannot run with `sudo` privileges.

  * Managed Service for Apache Spark [Workflows](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/overview) are not supported.




## Create a multi-tenant cluster

You enable the multi-tenant feature when you [create a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster#creating_a_cloud_dataproc_cluster).

### Console

Create a cluster using the Google Cloud console, as follows:

  1. In the Google Cloud console, go to the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Optional components**. 
     1. Select the **Enable components in the UI** checkbox to enable component UIs, then select the checkbox for **Jupyter Kernel Gateway**.
     2. Click **Save**.
  4. Edit **Customization & Other**. 
     1. To allow adding or removing multi-tenant users without re-creating the cluster (see Update multi-tenant cluster users), in the **Cluster properties** section, click **\+ Add properties**.
     2. Add the following property: Prefix: `dataproc`, Key: `dataproc.dynamic.multi.tenancy.enabled`, Value: `true`

**Recommendation** : Since YARN consumes significant cluster resources for each notebook kernel running on a multi-tenant cluster, add Spark and YARN properties to increase resource allocation.

Example:

Prefix | Key | Value  
---|---|---  
spark | spark.driver.memory | 5g  
spark | spark.executor.memory | 5g  
spark | spark.executor.cores | 2  
capacity-scheduler | yarn.scheduler.capacity.maximum-am-resource-percent | 0.5  
     3. Click **Save**.
  5. Edit **Security**. 
     * Under **Project access** , select the checkbox for **Enables the cloud-platform scope for this cluster**.
     * Under **Secure Multi Tenancy** , select **Enable**.
     * Under **Multi-tenancy Mapping** , click **Add Multi-tenancy Mapping** to map user accounts to service accounts.
  6. Click **Save**.
  7. Confirm other settings, then click **Create cluster**.



### gcloud

Use the `gcloud dataproc clusters create command` with the [`--secure-multi-tenancy-user-mapping`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--secure-multi-tenancy-user-mapping) flag to specify a list of user account to service-account mappings.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --secure-multi-tenancy-user-mapping=USER_MAPPINGS: \
        --properties "dataproc:dataproc.dynamic.multi.tenancy.enabled=true" \
        --service-account=CLUSTER_SERVICE_ACCOUNT@iam.gserviceaccount.com \
        --scopes=https://www.googleapis.com/auth/iam \
        --optional-components=JUPYTER_KERNEL_GATEWAY \
        --enable-component-gateway \
        other args ...
    

Notes:

  * USER_MAPPINGS: Specify a comma-separated list that maps user accounts to service accounts. 
        
        --secure-multi-tenancy-user-mapping=UserA@my-company.com:SERVICE_ACCOUNT_FOR_USERA@iam.gserviceaccount.com,UserB@my-company.com:SERVICE_ACCOUNT_FOR_USERB@iam.gserviceaccount.com,UserC@my-company.com:SERVICE_ACCOUNT_FOR_USERC@iam.gserviceaccount.com
        

**Use a YAML mapping file:** Instead of using the `--secure-multi-tenancy-user-mapping` flag to specify the user account to service account mappings, you can use the [`--identity-config-file`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--identity-config-file) flag to specify a local or Cloud Storage YAML file that contains the mappings. 
        
        --identity-config-file=LOCAL_FILE or gs://BUCKET/FOLDER/FILENAME
        

Each line in the mapping file maps a user account to a service account. The first line contains the `user_service_account_mapping:` header. 
        
        user_service_account_mapping:
        UserA@my-company.com:SERVICE_ACCOUNT_FOR_USERA@iam.gserviceaccount.com
        UserB@my-company.com:SERVICE_ACCOUNT_FOR_USERB@iam.gserviceaccount.com
        UserC@my-company.com:SERVICE_ACCOUNT_FOR_USERC@iam.gserviceaccount.com
        

  * `--properties "dataproc:dataproc.dynamic.multi.tenancy.enabled=true"`: This property allows adding or removing multi-tenant cluster users without re-creating the cluster (see Update multi-tenant cluster users).

**Recommendation** : Since YARN consumes significant cluster resources for each notebook kernel running on a multi-tenant cluster, add Spark and YARN properties to increase resource allocation.

Example:
        
        --properties=" \
        spark:spark.driver.memory=5g,\
        spark:spark.executor.memory=5g,\
        spark:spark.executor.cores=200, \
        capacity-scheduler:yarn.scheduler.capacity.maximum-am-resource-percent=0.5"
        

  * CLUSTER_SERVICE_ACCOUNT (Optional): You can use the `--service-account flag` to specify a [custom VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#VM_service_account%22) for the cluster. If you omit this flag, the [default cluster VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#VM_service_account), `PROJECT_NUMBER-compute@developer.gserviceaccount.com`, is used. 

**Recommendation:** Use different cluster service accounts for different clusters to allow each cluster VM service account to impersonate only a limited group of mapped user service accounts.

  * `--scopes=https://www.googleapis.com/auth/iam` is necessary for the cluster service account to perform impersonation.

  * `--enable-component-gateway` and `--optional-components=JUPYTER_KERNEL_GATEWAY`: Enabling the [Managed Service for Apache Spark Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways) and the [Jupyter Kernel Gateway](https://jupyter-kernel-gateway.readthedocs.io/en/latest/) lets multiple users connect their Jupyter notebooks to the multi-tenant cluster.




### API

Use the [`SecurityConfig.IdentityConfig.userServiceAccountMapping field`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#IdentityConfig.FIELDS.user_service_account_mapping) to specify a list of user account to service account mappings.

## Grant Identity and Access Management permissions

To connect user notebooks to notebook kernels running on a multi-tenant cluster, mapped users, mapped service accounts, and the cluster VM service account must have IAM permissions needed to access resources.

### Mapped user permissions

Each mapped user must have the`dataproc.clusters.get` and `dataproc.clusters.use` permissions, which are needed for the user to access and connect to notebook kernels running on the multi-tenant cluster. You can grant the [**Managed Service for Apache Spark Editor** role (`roles/dataproc.editor`)](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#VM_service_account), which contains these permissions (see [Grant a single IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role)), or [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating) with these permissions.

### Mapped service account permissions

Each mapped service account must have permissions needed by the mapped user's notebook application, such as access to a Cloud Storage bucket or access to a BigQuery table (see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts)).

### VM service account permissions

The multi-tenant cluster [VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#vm-service-account) must have the `iam.serviceAccounts.getAccessToken` permission on each mapped service account. You can grant the [**Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator), which contains this permission (see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts)), or [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating) with this permission. See [Managed Service for Apache Spark VM service account](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/service-accounts#VM_service_account) for information on other VM service account roles.

## Connect Jupyter notebooks to a multi-tenant cluster kernel

Mapped multi-tenant cluster users can connect their Vertex AI Workbench or user-managed Jupyter notebook to the kernels installed on the multi-tenant cluster.

### Vertex AI notebook

To create and connect a Jupyter notebook to the multi-tenant cluster, do the following;

  1. [Create a Vertex AI Workbench instance](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/create#create).
  2. On the [Workbench](https://console.cloud.google.com/vertex-ai/workbench/instances) Instances tab, click the **Open JupyterLab** link for your instance.
  3. Under **Dataproc Cluster Notebooks** , click the **PySpark (YARN Cluster) on` MULTI_TENANCY_CLUSTER_NAME`** card to connect to and launch a new Jupyter PySpark notebook.



### User-managed notebook

To create and connect a user-managed Jupyter notebook to your Managed Service for Apache Spark multi-tenant cluster, follow the steps to [Install the JupyterLab extension](https://docs.cloud.google.com/managed-spark/docs/quickstarts/jupyterlab-sessions#install-jupyterlab-extension) on your user-managed VM.

## Update multi-tenant cluster users (Preview)

**Preview — This preview is available only with Managed Service for Apache Spark 2.3 or later image version clusters.**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you set the `dataproc:dataproc.dynamic.multi.tenancy.enabled` cluster property to `true` when you created a multi-tenant cluster, you can add, remove, or replace multi-tenant cluster users after cluster creation. 

### Add users

The following update command uses the `--add-user-mappings` flag to add two new user account to service account mappings to the secure multi-tenant cluster.
    
    
    gcloud dataproc clusters update CLUSTER_NAME \
        --region=REGION \
        --add-user-mappings=new-user1@my-company.com=SERVICE_ACCOUNT_FOR_NEW_USER1@iam.gserviceaccount.com,new-user2@my-company.com=SERVICE_ACCOUNT_FOR_NEW_USER2@iam.gserviceaccount.com
    

### Remove users

The following update command uses the `--remove-user-mappings` flag to remove two users from the multi-tenant cluster. The flag accepts the user accounts of the users to be removed.
    
    
    gcloud dataproc clusters update CLUSTER_NAME \
        --region=REGION \
        --remove-user-mappings=UserB@my-company.com,UserC@my-company.com
    

### Replace users

You can use the update command with the `--identity-config-file` flag to replace the existing set of users with a new set. This flag is useful to both add and remove users with one update command.
    
    
    gcloud dataproc clusters update CLUSTER_NAME \
        --region=REGION \
        --identity-config-file=identity-config.yaml
    

Notes:

  * `--identity-config-file`: Specify a local or Cloud Storage YAML file that contains the new user account to service account mappings. 
        
        --identity-config-file=LOCAL_FILE or gs://BUCKET/FOLDER/FILENAME
        

Each line in the mapping file maps a user account to a service account. The first line contains the `user_service_account_mapping:` header. 
        
        user_service_account_mapping:
        new-user1@my-company.com:SERVICE_ACCOUNT_FOR_NEW_USER1@iam.gserviceaccount.com
        new-user2@my-company.com:SERVICE_ACCOUNT_FOR_NEW_USER2@iam.gserviceaccount.com
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
