---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/service-accounts-serverless/
title: Managed Service for Apache Spark service accounts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:25.336231+00:00
---

# Managed Service for Apache Spark service accounts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/service-accounts-serverless/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark service accounts Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark batch workloads and interactive sessions run either with end user or service account credentials. When service account credentials are used, the service account used to run batch workloads or interactive sessions depends on the batch or session runtime version.

## Pre-3.0 runtime service accounts

Spark runtime versions prior to `3.0` with service account credentials use the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) or a user-specified custom service account to submit a batch workload or create an interactive session.

## 3.0+ runtime service accounts

Spark runtime versions `3.0` and later with service account credentials use a user-specified custom service account to submit a batch workload or create an interactive session.

Managed Service for Apache Spark 3.0 and later runtimes create the [Dataproc Resource Manager Node Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#google-cloud-dataproc-resource-manager-node-service-agent) service account, `service-project-number@gcp-sa-dataprocrmnode.iam.gserviceaccount.com`, with the **Dataproc Resource Manager Node Service Agent** role in a Managed Service for Apache Spark user Google Cloud project. This service account performs the following system operations on Managed Service for Apache Spark resources located in the project where a workload is created:

  * Cloud Logging and Cloud Monitoring
  * Managed Service for Apache Spark Resource Manager Node basic operations such as `get`, `heartbeat` and `mintOAuthToken`



## View and manage IAM service account roles

To view and manage roles granted to the batch workload or session service account, do the following:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/dataproc/interactive)'

  2. Click **Include Google-provided role grants**.

  3. View the roles listed for the batch workload or session default or custom service default or custom service account.

The following image shows the required **Managed Service for Apache Spark Worker** role listed for the Compute Engine default service account, `project_number-compute@developer.gserviceaccount.com`, which Managed Service for Apache Spark uses by default as the workload or session service account.

![Dataproc Worker role for Compute Engine default service account in IAM console](https://docs.cloud.google.com/static/managed-spark/docs/images/iam-vm-service-account-role-in-console.png)The Managed Service for Apache Spark Worker role assigned to the Compute Engine default service account on the IAM section of the Google Cloud console.
  4. You can click the pencil icon displayed on the service account row to [grant or remove service account roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#multiple-roles-console).




## How to use a cross-project service account

You can submit a batch workload that uses a service account from a project that is different than the batch workload project (the project where the batch is submitted). In this section, the project where the service account is located is called the `service account project`, and the project where the batch is submitted is called the `batch project`.

**Why use a cross-project service account to run a batch workload?** One possible reason is if the service account in the other project has been assigned [IAM roles](https://docs.cloud.google.com/iam/docs) roles that provide fine-grained access to the resources in that project.

### Setup steps

The examples in this sections apply to submitting a batch workload that is executed with a runtime version prior to `3.0`.

  1. In the service account project:

     1. [Enable service accounts to be attached across projects](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project).

     2. Enable the Dataproc API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com)

     3. Grant to your email account (the user who is creating the cluster) the [Service Account User](https://docs.cloud.google.com/iam/docs/service-accounts#user-role) role on either the service account project or, for more granular control, the service account in the service account project.

For more information, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to grant roles at the project level and [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts) grant roles at the service account level.

**gcloud CLI examples:**

The following sample command grants to the user the Service Account User role at the project level:
            
            gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
                --member=USER_EMAIL \
                --role="roles/iam.serviceAccountUser"
            

Notes:

        * `USER_EMAIL`: Provide your user account email address, in the format: `user:user-name@example.com`.

The following sample command grants to the user the Service Account User role at the service account level:
    
    gcloud iam service-accounts add-iam-policy-binding VM_SERVICE_ACCOUNT_EMAIL \
        --member=USER_EMAIL \
        --role="roles/iam.serviceAccountUser"
    

Notes:

        * `USER_EMAIL`: Provide your user account email address, in the format: `user:user-name@example.com`.
     4. Grant the service account the [Managed Service for Apache Spark Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) role on the batch project.

**gcloud CLI example:**
            
            gcloud projects add-iam-policy-binding BATCH_PROJECT_ID \
                --member=serviceAccount:SERVICE_ACCOUNT_NAME@SERVICE_ACCOUNT_PROJECT_ID.iam.gserviceaccount.com \
                --role="roles/dataproc.worker"
            

  2. In the batch project:

     1. Grant the [Managed Service for Apache Spark service agent service account](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#service_agent_control_plane_identity) the [Service Account User](https://docs.cloud.google.com/iam/docs/service-accounts#user-role) and the [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/service-accounts#token-creator-role) roles on either the service account project or, for more granular control, the service account in the service account project. By doing this, you allow the Managed Service for Apache Spark service agent service account in the batch project to create tokens for the service account in the service account project.

For more information, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to grant roles at the project level and [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts) grant roles at the service account level.

**gcloud CLI examples:**

The following commands grant the Managed Service for Apache Spark service agent service account in the batch project the Service Account User and Service Account Token Creator roles at the project level:
            
            gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
                --member=serviceAccount:service-BATCH_PROJECT_NUMBER@dataproc-accounts.iam.gserviceaccount.com \
                --role="roles/iam.serviceAccountUser"
            
            
            gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
                --member=serviceAccount:service-BATCH_PROJECT_NUMBER@dataproc-accounts.iam.gserviceaccount.com \
                --role="roles/iam.serviceAccountTokenCreator"
            

The following sample commands grant the Managed Service for Apache Spark Service Agent service account in the batch project the Service Account User and Service Account Token Creator roles at the service account level:
            
            gcloud iam service-accounts add-iam-policy-binding VM_SERVICE_ACCOUNT_EMAIL \
                --member=serviceAccount:service-BATCH_PROJECT_NUMBER@dataproc-accounts.iam.gserviceaccount.com \
                --role="roles/iam.serviceAccountUser"
            
            
            gcloud iam service-accounts add-iam-policy-binding VM_SERVICE_ACCOUNT_EMAIL \
                --member=serviceAccount:service-BATCH_PROJECT_NUMBER@dataproc-accounts.iam.gserviceaccount.com \
                --role="roles/iam.serviceAccountTokenCreator"
            

     2. Grant the [Compute Engine Service Agent service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#compute_engine_service_account) in the batch project the [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/service-accounts#token-creator-role) role on either the service account project or, for more granular control, the service account in the service account project. By doing this, you grant the Compute Agent Service Agent service account in the batch project the ability to create tokens for the service account in the service account project.

For more information, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to grant roles at the project level and [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts) grant roles at the service account level.

**gcloud CLI examples:**

The following sample command grants the Compute Engine Service Agent service account in the batch project the Service Account Token Creator role at the project level:
            
            gcloud projects add-iam-policy-binding SERVICE_ACCOUNT_PROJECT_ID \
                --member=serviceAccount:service-BATCH_PROJECT_NUMBER@compute-system.iam.gserviceaccount.com \
                --role="roles/iam.serviceAccountTokenCreator"
            

The following sample command grants the Compute Engine Service Agent service account in the cluster project the Service Account Token Creator role at the service account level:
            
            gcloud iam service-accounts add-iam-policy-binding VM_SERVICE_ACCOUNT_EMAIL \
                --member=serviceAccount:service-BATCH_PROJECT_NUMBER@compute-system.iam.gserviceaccount.com \
                --role="roles/iam.serviceAccountTokenCreator"
            




### Submit the batch workload

After you complete the setup steps, you can [submit a batch workload](https://docs.cloud.google.com/managed-spark/docs/quickstarts/spark-batch#submit_a_spark_batch_workload). Make sure to specify the service account in the service account project as the service account to use for the batch workload.

## Troubleshoot permission-based failures

Incorrect or insufficient permissions for the service account used by your batch workload or session can lead to batch or session creation failures that report a "Driver compute node failed to initialize for batch in 600 seconds" error message. This error indicates that the Spark driver couldn't start within the allotted timeout period, often due to a lack of necessary access to Google Cloud resources.

To troubleshoot this issue, verify your service account has the following minimum roles or permissions:

  * **Managed Service for Apache Spark Worker** role (`roles/dataproc.worker`): This role grants the necessary permissions for Managed Service for Apache Spark to manage and execute Spark workloads and sessions.
  * **Storage Object Viewer** (`roles/storage.objectViewer`), **Storage Object Creator** (`roles/storage.objectCreator`), or **Storage Object Admin** (`roles/storage.admin`): If your Spark application reads from or writes to Cloud Storage buckets, the service account needs appropriate permissions to access the buckets. For example, if your input data is in a Cloud Storage bucket, **`Storage Object Viewer`** is required. If your application writes output to a Cloud Storage bucket, **`Storage Object Creator`** or **`Storage Object Admin`** is needed.
  * **BigQuery Data Editor** (`roles/bigquery.dataEditor`) or **BigQuery Data Viewer** (`roles/bigquery.dataViewer`): If your Spark application interacts with BigQuery, verify the service account has the appropriate [BigQuery roles](https://docs.cloud.google.com/bigquery/docs/access-control).
  * **Cloud Logging permissions:** The service account needs permissions to write logs to Cloud Logging for effective debugging. Typically, the **`Logging Writer`** role (`roles/logging.logWriter`) is sufficient.



### Common permission or access-related failures

  * Missing `dataproc.worker` role: Without this core role, the Managed Service for Apache Spark infrastructure cannot properly provision and manage the driver node.

  * Insufficient Cloud Storage permissions: If your Spark application attempts to read input data from or write output to a Cloud Storage bucket without the necessary service account permissions, the driver can fail to initialize because it lacks access to critical resources.

  * Network or firewall issues: VPC Service Controls or firewall rules can inadvertently block service account access to Google Cloud APIs or resources.




To verify and update service account permissions:

  1. Go to the [**IAM & Admin** > **IAM**](https://console.cloud.google.com/am-admin/iam) page in the Google Cloud console.
  2. Locate the service account used for your batch workloads or sessions.
  3. Verify the necessary roles are assigned. If not, add them.



For a list of Managed Service for Apache Spark roles and permissions, see [Managed Service for Apache Spark permissions and IAM roles](https://docs.cloud.google.com/managed-spark/docs/concepts/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
