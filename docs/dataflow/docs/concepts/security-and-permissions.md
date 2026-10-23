---
url: https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions/
title: Dataflow security and permissions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:54.139034+00:00
---

# Dataflow security and permissions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Dataflow security and permissions Stay organized with collections  Save and categorize content based on your preferences. 

You can run Dataflow pipelines locally or on managed Google Cloud resources by using the Dataflow runner. Whether running pipelines locally or in the cloud, your pipeline and its workers use a permissions system to maintain secure access to pipeline files and resources. Dataflow permissions are assigned according to the role that's used to access pipeline resources. This document explains the following concepts:

  * Upgrading Dataflow VMs
  * Roles and permissions required for running local and Google Cloud pipelines
  * Roles and permissions required for accessing pipeline resources
  * Types of data used in a Dataflow service and in data security



## Before you begin

Read about Google Cloud project identifiers in the [Google Cloud overview](https://docs.cloud.google.com/docs/overview#projects). These identifiers include the project name, project ID, and project number.

## Upgrade and patch Dataflow VMs

Dataflow uses [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/concepts/security). The security processes of Container-Optimized OS also apply to Dataflow. For more details on how Google secures and hardens these VMs, see [Worker VM security and hardening](https://docs.cloud.google.com/dataflow/docs/guides/worker-vm-hardening).

Batch pipelines are time-bound and don't require maintenance. When a new batch pipeline starts, the latest Dataflow image is used.

For streaming pipelines, if a security patch is immediately required, Google Cloud notifies you by using [security bulletins](https://cloud.google.com/support/bulletins). For streaming pipelines, we recommend that you use the [`--update` option](https://docs.cloud.google.com/dataflow/docs/guides/updating-a-pipeline) to restart your job with the latest Dataflow image.

Dataflow container images are available in the [Google Cloud console](https://console.cloud.google.com/artifacts?project=cloud-dataflow).

### Container image security

Dataflow uses container images for the runtime environment of pipeline user code. By default, a prebuilt Apache Beam image is used. You can also provide a [custom container](https://docs.cloud.google.com/dataflow/docs/guides/using-custom-containers).

Google hardens and patches the operating system of base images used by the Dataflow-owned images. Google promptly makes any patches to these images available. All Dataflow production resources, including the Beam images provided by default, are automatically and regularly scanned for vulnerabilities. Any identified issues in Google-owned containers are addressed under a defined service-level objective (SLO). Issues in Beam containers are addressed by the Beam community. As part of Dataflow's [shared responsibility model](https://docs.cloud.google.com/dataflow/docs/resources/shared-responsibility#customers_responsibilities), to manage security issues responsively, we recommend that you use custom container images.

While the Container-Optimized OS images that Dataflow uses are CIS Level 1 compliant, achieving overall compliance is a [shared responsibility](https://docs.cloud.google.com/dataflow/docs/resources/shared-responsibility). The VM instances on which these containers run reside within the customer's project. Customers are responsible for scanning their own project resources. You can use [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/compliance-management) to scan your resources for compliance and vulnerabilities.

## Runtime environment

For the runtime environment of pipeline user code, Dataflow uses a prebuilt [Apache Beam image](https://hub.docker.com/search?q=apache%2Fbeam&type=image), or a [custom container](https://docs.cloud.google.com/dataflow/docs/guides/using-custom-containers) if one was provided.

The user for container execution is selected by the Dataflow service. Dataflow doesn't let you run custom SDK container images or custom template container images for Flex Templates as a non-root user.

Unlike other environments (such as Google Kubernetes Engine (GKE)) where containers run on shared nodes, Dataflow worker VMs aren't shared across pipelines. Pipeline resources are allocated on a per-job basis. There's no cross-pipeline sharing of VMs and other resources.

The runtime environment lifecycle is tied to the pipeline lifecycle. It's started at pipeline start, and stopped at pipeline termination. The runtime environment might be restarted one or more times during pipeline execution.

## Security and permissions for local pipelines

When you run locally, your Apache Beam pipeline runs as the Google Cloud account that you [configured with the Google Cloud CLI executable](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). Locally run Apache Beam SDK operations and your Google Cloud account have access to the same files and resources.

To list the Google Cloud account that you selected as your default, run the `gcloud config list` command.

Local pipelines can output data to local destinations, such as local files, or to cloud destinations, such as Cloud Storage or BigQuery. If your locally run pipeline writes files to cloud-based resources such as Cloud Storage, it uses your Google Cloud account credentials and the Google Cloud project that you configured as the Google Cloud CLI default. For instructions about how to authenticate with your Google Cloud account credentials, see the tutorial for the language you're using: [Java](https://docs.cloud.google.com/dataflow/docs/guides/create-pipeline-java), [Python](https://docs.cloud.google.com/dataflow/docs/guides/create-pipeline-python), or [Go](https://docs.cloud.google.com/dataflow/docs/guides/create-pipeline-go).

## Security and permissions for pipelines on Google Cloud

When you run your pipeline, Dataflow uses two service accounts to manage security and permissions:

  * **The Dataflow service account.** The Dataflow service uses the Dataflow service account as part of the job creation request, such as to check project quota and to create worker instances on your behalf. Dataflow also uses the Dataflow service account during job execution to manage the job. This account is also known as the Dataflow service agent.

  * **The worker service account.** Worker instances use the worker service account to access input and output resources after you submit your job. By default, workers use the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) associated with your project as the worker service account. As a best practice, we recommend that you specify a user-managed service account instead of using the default worker service account.




To impersonate the service account when you run a pipeline, the account that launches the pipeline needs the `iam.serviceAccounts.actAs` permission. This permission is included in the Service Account User role (`roles/iam.serviceAccountUser`). Impersonating a service account lets you temporarily adopt its identity and permissions to perform tasks requiring different access levels, while still avoiding the risks associated with persistent keys. For more information, see [Use service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation).

Depending on other project permissions, your user account might also need the `roles/dataflow.developer` role. If you are a project owner or editor, you already have the permissions contained by the `roles/dataflow.developer` role.

### Best practices

  * When possible, for the worker service account, specify a user-managed service account instead of using the default worker service account.
  * When giving permissions on resources, grant the role that contains the minimum required permissions for the task. You can [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) that includes only the required permissions.
  * When granting roles to access resources, use the lowest possible resource level. For example, instead of granting the `roles/bigquery.dataEditor` role on a project or folder, grant the role on the BigQuery table.
  * Create a bucket owned by your project to use as the staging bucket for Dataflow. The default bucket permissions allow Dataflow to use the bucket to stage the executable files of the pipeline.



### Dataflow service account

All projects that have used the resource `Dataflow Job` have a _Dataflow Service Account_ , also known as the Dataflow [service agent](https://docs.cloud.google.com/iam/docs/service-agents), which has the following email:
    
    
    service-PROJECT_NUMBER@dataflow-service-producer-prod.iam.gserviceaccount.com
    

This service account is created and managed by Google and assigned to your project automatically upon first usage of the resource `Dataflow Job`.

As part of running Dataflow pipelines, Dataflow manipulates resources on your behalf. For example, it creates additional VMs. When you run your pipeline with Dataflow, this service account is used.

This account is assigned the Dataflow Service Agent role on the project. It has the necessary permissions to run a Dataflow job in the project, including starting Compute Engine workers. This account is used exclusively by Dataflow and is specific to your project.

You can review the roles assigned to the Dataflow service account in the Google Cloud console or the Google Cloud CLI.

### Console

  1. Go to the **Roles** page.

[Go to Roles](https://console.cloud.google.com/iam-admin/roles)

  2. If applicable, select your project.

  3. In the list, click the title **Cloud Dataflow Service Agent**. A page opens that lists the permissions assigned to the Dataflow service account.




### gcloud CLI

View the permissions of the Dataflow service account:
    
    
    gcloud iam roles describe roles/dataflow.serviceAgent
    

Because Google Cloud services expect to have read and write access to the project and its resources, it's recommended that you don't change the default permissions automatically established for your project. If a Dataflow service account loses permissions to a project, Dataflow cannot launch VMs or perform other management tasks.

If you remove the permissions for the service account from the Identity and Access Management (IAM) policy, the account remains present, because it's owned by the Dataflow service.

### Worker service account

Compute Engine instances execute Apache Beam SDK operations in the cloud. These workers use the worker service account of your project to access the files and other resources associated with the pipeline. The worker service account is used as the identity for all worker VMs, and all requests that originate from the VM use the worker service account. This service account is also used to interact with resources such as Cloud Storage buckets and Pub/Sub topics.

**Note:** Service account permissions are project-specific. If you need to run a similar job in a different project, you must configure appropriate service accounts and permissions within that new project. Dataflow jobs cannot be migrated between projects. To move a job, recreate it in the new project. For more information, see [Migrate pipeline jobs to another Google Cloud project](https://docs.cloud.google.com/dataflow/docs/guides/migrate-your-jobs).

  * For the worker service account to be able to run a job, it must have the `roles/dataflow.worker` role.
  * For the worker service account to be able to create or examine a job, it must have the `roles/dataflow.admin` role.



In addition, when your Apache Beam pipelines access Google Cloud resources, you need to grant the required roles to your Dataflow project's worker service account. The worker service account needs to be able to access the resources while running the Dataflow job. For example, if your job writes to BigQuery, your service account must also have at least the `roles/bigquery.dataEditor` role on the BigQuery table. Examples of resources include:

  * Cloud Storage buckets
  * BigQuery datasets
  * Pub/Sub topics and subscriptions
  * Firestore datasets



#### Default worker service account

By default, workers use the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) of your project as the worker service account. This service account has the following email:
    
    
    PROJECT_NUMBER-compute@developer.gserviceaccount.com
    

This service account is automatically created when you enable the Compute Engine API for your project from the [API Library](https://console.cloud.google.com/project/_/apiui/apis/library) in the Google Cloud console.

Although you can use the Compute Engine default service account as the Dataflow worker service account, we recommend that you create a dedicated Dataflow worker service account that has only the roles and permissions that you need.

Depending on your organization policy configuration, the default service account might automatically be granted the [Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) on your project. We strongly recommend that you disable the automatic role grant by [ enforcing the `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants). If you created your organization after May 3, 2024, this constraint is enforced by default. 

If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Note:** In the past, Dataflow users were able to deploy applications that authenticated as the Compute Engine default service account, even if they didn't have permission to impersonate the Compute Engine default service account. This legacy behavior still affects some organizations. For more information, see [Requiring impersonation permissions when attaching service accounts to resources](https://docs.cloud.google.com/iam/docs/service-accounts-actas).

#### Specify a user-managed worker service account

If you want to create and use resources with fine-grained access control, you can create a user-managed service account. Use this account as the worker service account.

  1. If you don't have a user-managed service account, [create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account).

  2. Set the required IAM roles for your service account.

     * For the worker service account to be able to run a job, it must have the `roles/dataflow.worker` role.
     * For the worker service account to be able to create or examine a job, it must have the `roles/dataflow.admin` role.
     * Alternately, create a custom IAM role with the required permissions. For a list of the required permissions, see [Roles](https://docs.cloud.google.com/dataflow/docs/concepts/access-control#roles).
  3. Your service account might need additional roles to use Google Cloud resources as required by your job, such as BigQuery, Pub/Sub, or Cloud Storage. For example, if your job reads from BigQuery, your service account must also have at least the `roles/bigquery.dataViewer` role on the BigQuery table.

  4. Ensure that your user-managed service account has read and write access to the staging and temporary locations specified in the Dataflow job.

  5. To launch the pipeline, your user account must have the `iam.serviceAccounts.actAs` permission to impersonate the worker service account.

  6. In the project that contains the user-managed worker service account, the Dataflow Service Account (`service-PROJECT_NUMBER@dataflow-service-producer-prod.iam.gserviceaccount.com`) and the [Compute Engine Service Agent](https://docs.cloud.google.com/compute/docs/access/service-accounts#compute_engine_service_account) (`service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com`) must have the following roles. PROJECT_NUMBER is the ID of the project that your Dataflow job runs in. Both of these accounts are service agents.

     * [Service Account Token Creator role](https://docs.cloud.google.com/iam/docs/service-accounts#token-creator-role) (`iam.serviceAccountTokenCreator`)
     * [Service Account User role](https://docs.cloud.google.com/iam/docs/service-accounts#user-role) (`iam.serviceAccountUser`)

Assume that the Dataflow job is running in project A and that the worker service account is hosted in project B, make sure that the service agents from project A have the `iam.serviceAccountTokenCreator` and `iam.serviceAccountUser` roles in project B. In the project that your Dataflow job runs in, the accounts have these roles by default. To grant these roles, follow the steps in the [Grant a single role](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#grant-single-role) section in the Manage access to service accounts page.

  7. When the user-managed worker service account and the job are in different projects, ensure that the `iam.disableCrossProjectServiceAccountUsage` boolean constraint is not enforced for the project that owns the user-managed service account. For more information, see [Enable service accounts to be attached across projects](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project).

  8. When you run your pipeline job, specify your service account.

### Java

Use the `--serviceAccount` option and specify your service account when you run your pipeline job from the command line: `--serviceAccount=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`

Use the `--service-account-email` option and specify your service account when you run your pipeline job as a Flex template: `--service-account-email=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`

### Python

Use the `--service_account_email` option and specify your service account when you run your pipeline job: `--service_account_email=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`

### Go

Use the `--service_account_email` option and specify your service account when you run your pipeline job: `--service_account_email=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`




The user-managed service account can be in the same project as your job, or in a different project. If the service account and the job are in different projects, you must [configure the service account](https://docs.cloud.google.com/iam/docs/attach-service-accounts#attaching-different-project) before you run the job.

### Add roles

To add roles in your project, follow these steps.

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select your project.

  3. In the row containing your user account, click edit **Edit principal** , and then click add **Add another role**.

  4. In the drop-down list, select the role **Service Account User**.

  5. In the row containing your worker service account, click edit **Edit principal** , and then click add **Add another role**.

  6. In the drop-down list, select the role **Dataflow Worker**.

  7. If your worker service account needs the Dataflow Admin role, repeat for the **Dataflow Admin**.

  8. Repeat for any roles required by resources used in your job, and then click **Save**.

For more information about granting roles, see [Grant an IAM role by using the console](https://docs.cloud.google.com/iam/docs/grant-role-console).




### gcloud CLI

  1. Grant the `roles/iam.serviceAccountUser` role to your user account. Run the following command:
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:EMAIL_ADDRESS --role=roles/iam.serviceAccountUser
         

     * Replace `PROJECT_ID` with your project ID.
     * Replace `EMAIL_ADDRESS` with the email address for the user account.
  2. Grant roles to your worker service account. Run the following command for the `roles/dataflow.worker` IAM role and for any roles required by resources used in your job. If your worker service account needs the Dataflow Admin role, repeat for the `roles/dataflow.admin` IAM role. This example uses the Compute Engine default service account, but we recommend using a user-managed service account.
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" --role=SERVICE_ACCOUNT_ROLE
         

     * Replace `PROJECT_ID` with your project ID.
     * Replace `PROJECT_NUMBER` with your project number. To find your project number, see [Identify projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) or use the [`gcloud projects describe`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe) command.
     * Replace `SERVICE_ACCOUNT_ROLE` with each individual role.



## Access Google Cloud resources

Your Apache Beam pipelines can access Google Cloud resources, either in the same Google Cloud project or in other projects. These resources include:

  * Artifact Registry repositories
  * Cloud Storage buckets
  * BigQuery datasets
  * Pub/Sub topics and subscriptions
  * Firestore datasets



To ensure that your Apache Beam pipeline can access these resources, you need to use the resources' respective access control mechanisms to explicitly grant access to your Dataflow project worker service account.

If you use Assured Workloads features with Dataflow, such as [EU Regions and Support with Sovereignty Controls](https://docs.cloud.google.com/assured-workloads/docs/concept-platform-controls#eu-sovereignty-controls), all Cloud Storage, BigQuery, Pub/Sub, I/O connectors, and other resources that your pipeline accesses must be located in your organization's [Assured Workloads project or folder](https://docs.cloud.google.com/assured-workloads/docs/eu-sovereign-controls-restrictions-limitations).

If you're using a user-managed worker service account or accessing resources in other projects, then additional action might be needed. The following examples assume that the Compute Engine default service account is used, but you can also use a user-managed worker service account.

### Access Artifact Registry repositories

When you [use custom containers with Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/using-custom-containers), you might upload artifacts to an Artifact Registry repository.

To use Artifact Registry with Dataflow, you must grant at least [Artifact Registry Writer access](https://docs.cloud.google.com/artifact-registry/docs/access-control#permissions) (`role/artifactregistry.writer`) to the worker service account that runs the Dataflow job.

All repository content is encrypted using either Google-owned and Google-managed encryption keys or customer-managed encryption keys. Artifact Registry uses Google-owned and Google-managed encryption keys by default and no configuration is required for this option.

### Access Cloud Storage buckets

To grant your Dataflow project access to a Cloud Storage bucket, make the bucket accessible to your Dataflow project worker service account. At a minimum, your service account needs read and write permissions to both the bucket and its contents. You can use [IAM permissions for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) to grant the required access.

To give your worker service account the necessary permissions to read from and write to a bucket, use the [`gcloud storage buckets add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding) command. This command adds your Dataflow project service account to a [bucket-level policy](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add).
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" --role=SERVICE_ACCOUNT_ROLE
    

Replace the following:

  * BUCKET_NAME: the name of your Cloud Storage bucket
  * PROJECT_NUMBER: your Dataflow project number. To find your project number, see [Identify projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) or use the [`gcloud projects describe`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe) command.
  * SERVICE_ACCOUNT_ROLE: the IAM role, for example `storage.objectViewer`



To retrieve a list of the Cloud Storage buckets in a Google Cloud project, use the [`gcloud storage buckets list`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/list) command:
    
    
    gcloud storage buckets list --project= PROJECT_ID
    

Replace PROJECT_ID with the ID of the project.

Unless you're restricted by organizational policies that limit resource sharing, you can access a bucket that resides in a different project than your Dataflow pipeline. For more information about domain restrictions, see [Restricting identities by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains).

If you don't have a bucket, [create a new bucket](https://docs.cloud.google.com/storage/docs/creating-buckets). Then, give your worker service account the necessary permissions to read from and write to the bucket.

You can also set bucket permissions from the Google Cloud console. For more information, see [Setting bucket permissions](https://docs.cloud.google.com/storage/docs/cloud-console#_bucketpermission).

Cloud Storage offers two systems for granting users access to your buckets and objects: IAM and Access Control Lists (ACLs). In most cases, IAM is the recommended method for controlling access to your resources. 

  * IAM controls permissioning throughout Google Cloud and lets you grant permissions at the bucket and project levels. For a list of IAM roles that are associated with Cloud Storage and the permissions that are contained in each role, see [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles). If you need more control over permissions, [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

  * If you [use ACLs to control access](https://docs.cloud.google.com/storage/docs/access-control), ensure that your worker service account permissions are consistent with your IAM settings. Due to the inconsistency between IAM and ACL policies, the Cloud Storage bucket might become inaccessible to your Dataflow jobs when the Cloud Storage bucket is migrated from fine-grained access to uniform bucket-level access. For more information, see [Common error guidance](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#staged-package-inaccessible).




### Access BigQuery datasets

You can use the `BigQueryIO` API to access BigQuery datasets, either in the same project where you're using Dataflow or in a different project. For the BigQuery source and sink to operate properly, the following two accounts must have access to any BigQuery datasets that your Dataflow job reads from or writes to: 

  * The Google Cloud account that you use to run the Dataflow job
  * The worker service account that runs the Dataflow job



You might need to configure BigQuery to explicitly grant access to these accounts. See [BigQuery Access Control](https://docs.cloud.google.com/bigquery/access-control) for more information on granting access to BigQuery datasets using either the [BigQuery page](https://docs.cloud.google.com/bigquery/bigquery-web-ui) or the [BigQuery API](https://docs.cloud.google.com/bigquery/docs/reference/v2/datasets/update).

Among the required BigQuery permissions, the `bigquery.datasets.get` IAM permission is required by the pipeline to access a BigQuery dataset. Typically, most BigQuery IAM roles include the `bigquery.datasets.get` permission, but the `roles/bigquery.jobUser` role is an exception.

### Access Pub/Sub topics and subscriptions

To access a Pub/Sub topic or subscription, use the [Identity and Access Management](https://docs.cloud.google.com/pubsub/access_control) features of Pub/Sub to set up permissions for the worker service account.

Permissions from the following [Pub/Sub roles](https://docs.cloud.google.com/pubsub/docs/access-control#roles) are relevant: 

  * `roles/pubsub.subscriber` is **required** to consume data.
  * `roles/pubsub.editor` is **required** to create a Pub/Sub subscription.
  * `roles/pubsub.viewer` is **recommended** so that Dataflow can query the configurations of topics and subscriptions. This configuration has two benefits: 
    * Dataflow can check for [unsupported settings](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-with-cloud-pubsub#unsupported-features "Unsupported Settings") on subscriptions that might not work as expected. 
    * If the subscription does not use the default [ack deadline](https://docs.cloud.google.com/pubsub/docs/subscriber "Ack Deadline") of 10 seconds, performance improves. Dataflow repeatedly extends the ack deadline for a message while it's being processed by the pipeline. Without `pubsub.viewer` permissions, Dataflow is unable to query the ack deadline, and therefore must assume a default deadline. This configuration causes Dataflow to issue more [modifyAckDeadline](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/modifyAckDeadline) requests than necessary. 
    * If VPC Service Controls is enabled on the project that owns the subscription or topic, IP address-based ingress rules don't allow Dataflow to query the configurations. In this case, an ingress rule based on the worker service account is required.



For more information and some code examples that demonstrate how to use the Identity and Access Management features of Pub/Sub, see [Sample use case: cross-project communication](https://docs.cloud.google.com/pubsub/access_control#sample_use_case_cross-project_communication).

### Access Firestore

To access a Firestore database (in Native mode or Datastore mode), add your Dataflow worker service account (for example, `PROJECT_NUMBER-compute@developer.gserviceaccount.com`) as editor of the project that owns the database, or use a more restrictive [Datastore role](https://docs.cloud.google.com/datastore/docs/access/iam#iam_roles) like `roles/datastore.viewer`. Also, enable the Firestore API in both projects from the [API Library](https://console.cloud.google.com/project/_/apiui/apis/library) in the Google Cloud console. 

### Access images for projects with a trusted image policy

If you have a [trusted image policy](https://docs.cloud.google.com/compute/docs/images/restricting-image-access) set up for your project and your boot image is located in another project, ensure that the trusted image policy is configured to have access to the image. For example, if you're running a templated Dataflow job, ensure that the policy file includes access to the `dataflow-service-producer-prod` project. This Google Cloud project contains the images for template jobs.

### Access Google-provided templates with principal access boundary policies

If your organization uses [principal access boundary (PAB) policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies), principals (such as users or service accounts) might be blocked from viewing and running Google-provided templates. In this case, try one of the following solutions:

  * Update the principal access boundary policy to allow access to the Google-managed project that hosts the Google-provided templates. Add the `dataflow-templates` project (or project number `473832897378`) to the principal access boundary policy as an allowed resource:
        
        //cloudresourcemanager.googleapis.com/projects/dataflow-templates
        

For instructions on updating principal access boundary policies, see [Edit principal access boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies-edit).

  * Exempt specific principals in the policy binding. If only specific user accounts or service accounts need to run Google-provided templates, use [condition expressions in the principal access boundary policy binding](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#conditions) to exempt those principals from the policy.

  * Run the template from your own project. Use the open source template code from the [DataflowTemplates GitHub repository](https://github.com/GoogleCloudPlatform/DataflowTemplates) to build and stage the template within your own project. For an example, see [Build and run an example Flex Template](https://docs.cloud.google.com/dataflow/docs/guides/templates/using-flex-templates).




To see symptoms that point to a principal access boundary policy issue, see [Error loading template list in the Google Cloud console](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-templates#error-loading-templates) and [Permission denied when loading a template file](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-templates#permission-denied-template-file) in the template troubleshooting documentation.

## Dataflow security best practices

Securing a Dataflow pipeline requires protecting data at the following three main levels:

  1. Network and infrastructure security
  2. Identity and Access Management (IAM)
  3. Data protection and encryption



Dataflow runs on managed, autoscaling virtual machines (workers). As a result, configuring these elements correctly helps to ensure that your data isn't exposed and remains secure during processing.

### Network and infrastructure security

By default, Dataflow workers are assigned public IP addresses to access the internet and Google APIs. In a secure environment, you should restrict this access.

  * **Disable public IPs:** Run your Dataflow workers without public IP addresses by passing the parameter `--usePublicIps=false`.
  * **Configure Private Google Access:** When public IPs are disabled, your workers must still communicate with Google APIs (such as Cloud Storage, BigQuery, or Pub/Sub). Enable **Private Google Access** on your VPC subnet so workers can route traffic to Google services internally.
  * **Use Shared VPCs and VPC Service Controls (VPC-SC):**
    * Place your Dataflow pipelines inside a security perimeter using VPC Service Controls. This mitigates data exfiltration risks by ensuring data can't be copied to resources outside the perimeter, even by users with valid credentials.
    * Use dedicated subnets with strict firewall rules, allowing traffic only to necessary resources (such as your database or Kafka cluster) and explicitly disable SSH.



### IAM

The principle of least privilege is critical. By default, Dataflow attempts to use the Compute Engine default service account, which often has broad Editor permissions.

  * **Use a user-managed worker service account:** Create a dedicated, non-privileged service account specifically for your Dataflow workers and pass it during pipeline submission. For example:
        
        --serviceAccount=YOUR_SERVICE_ACCOUNT@YOUR_PROJECT_ID.iam.gserviceaccount.com
        

After the service account is created, only assign minimal roles to it:

    * The worker service account needs the `roles/dataflow.worker` role.
    * Only grant specific read or write access to the exact resources the pipeline touches. For example, grant `roles/storage.objectViewer` on your input Cloud Storage bucket, and `roles/bigquery.dataEditor` on your specific target BigQuery table (rather than project-wide roles).
  * **Separate controller versus worker permissions:** The developer or CI/CD pipeline submitting the job needs the `roles/dataflow.admin` and `roles/iam.serviceAccountUser` (or `iam.serviceAccounts.actAs` permission) to trigger the pipeline. However, the actual worker VMs only need runtime execution permissions (`roles/dataflow.worker`).




### Data protection and encryption

While Google Cloud encrypts all data in transit and at rest by default, highly regulated industries often require additional control over encryption keys.

  * **Implement Customer-Managed Encryption Keys (CMEK):** Use Cloud Key Management Service to generate and manage your own keys. Pass your key to Dataflow using the `--dataflowKmsKey` flag. Dataflow uses this key to encrypt: 
    * Persistent disks attached to the worker VMs.
    * Shuffle state data for batch pipelines.
    * Streaming Engine state for streaming pipelines.
  * **Secure your secrets:** Never hardcode passwords, API keys, or database credentials in your Apache Beam code or pipeline options. Access them dynamically during the `Setup` or `StartBundle` phases of your pipeline using Secret Manager.
  * **Deploy dead-letter queues (DLQ):** Avoid logging raw, unparsed elements when an error occurs, as they might contain Personally Identifiable Information (PII) or secrets. Instead, catch processing exceptions and route failed elements to an encrypted "dead-letter" Cloud Storage bucket or Pub/Sub topic for isolated, secure inspection.



### Pipeline code and vulnerability scanning

Security also applies to the software supply chain of your Apache Beam code.

  * **Container image scanning:** If you use custom container images for your Dataflow workers (using the `--sdkContainerImage` flag), store them in Artifact Registry and enable automatic vulnerability scanning.
  * **Keep images updated:** For streaming pipelines that run continuously, regularly update your pipeline to use the latest Apache Beam SDK releases. Google regularly hardens and patches the underlying operating system base images used by Dataflow.



### Quick security checklist

Use the following table to identify a security goal and how to achieve it.

Goal | Security parameter or tool | Purpose  
---|---|---  
Key ownership | `--dataflowKmsKey` | Encrypts pipeline state and worker disks using Cloud KMS.  
Least privilege access | `--serviceAccount` | Executes workers under a restricted identity.  
No internet exposure | `--usePublicIps=false` | Prevents workers from being assigned public IPs.  
Prevent exfiltration | VPC Service Controls (VPC-SC) | Restricts data movement outside your trust boundary.  
Secure API access | Private Google Access | Lets workers reach Cloud Storage and BigQuery privately.  
Secure credentials | Secret Manager | Dynamically pulls passwords and keys at runtime.  
Secure Cloud Storage buckets | Least privilege permissions | Restrict permissions on Cloud Storage buckets used by Dataflow.  
  
## Data access and security

The Dataflow service works with two kinds of data:

  * **End-user data.** This data is processed by a Dataflow pipeline. A typical pipeline reads data from one or more sources, implements transformations of the data, and writes the results to one or more sinks. All the sources and sinks are storage services that are not directly managed by Dataflow.

  * **Operational data.** This data includes all the metadata that is required for managing a Dataflow pipeline. This data includes both user-provided metadata such as a job name or pipeline options and also system-generated metadata such as a job ID.




The Dataflow service uses several security mechanisms to keep your data secure and private. These mechanisms apply to the following scenarios:

  * Submitting a pipeline to the service
  * Evaluating a pipeline
  * Requesting access to telemetry and metrics during and after a pipeline execution
  * Using a Dataflow service such as Shuffle or Streaming Engine



### Data locality

**Note:** We recommend that you **always** specify a region when you run a pipeline.

All of the core data processing for Dataflow happens in the region that is specified in the pipeline code. If a region is not specified, the default region `us-central1` is used. If you specify that option in the pipeline code, the pipeline job can optionally read and write from sources and sinks in other regions. However, the actual data processing occurs only in the region that is specified to run the Dataflow VMs.

Pipeline logic is evaluated on individual worker VM instances. You can specify the zone where these instances and the private network that they communicate over are located. Ancillary computations for the platform depend on metadata such as Cloud Storage locations or file sizes.

Dataflow is a regional service. For more information about data locality and regions, see [Dataflow regions](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints#data_locality).

### Data in a pipeline submission

The IAM permissions for your Google Cloud project control access to the Dataflow service. Any principals who are given editor or owner rights to your project can submit pipelines to the service. To submit pipelines, you must authenticate by using the Google Cloud CLI. After you authenticate, your pipelines are submitted using the HTTPS protocol. For instructions about how to authenticate with your Google Cloud account credentials, see the quickstart for the language that you're using.

### Data in a pipeline evaluation

As part of evaluating a pipeline, temporary data might be generated and stored locally in the worker VM instances or in Cloud Storage. Temporary data is encrypted at rest and does not persist after a pipeline evaluation concludes. Such data can also be stored in the Shuffle service or Streaming Engine service (if you have opted for the service) in the same region specified in the Dataflow pipeline.

### Java

By default, Compute Engine VMs are deleted when the Dataflow job completes, regardless of whether the job succeeds or fails. Consequently, the associated [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks), and any intermediate data that might be stored on it, is deleted. The intermediate data stored in Cloud Storage can be found in sublocations of the Cloud Storage path that you provide as your `--stagingLocation` or `--tempLocation`. If you're writing output to a Cloud Storage file, temporary files might be created in the output location before the `write` operation is finalized.

### Python

By default, Compute Engine VMs are deleted when the Dataflow job completes, regardless of whether the job succeeds or fails. Consequently, the associated [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks), and any intermediate data that might be stored on it, is deleted. The intermediate data stored in Cloud Storage can be found in sublocations of the Cloud Storage path that you provide as your `--staging_location` or `--temp_location`. If you're writing output to a Cloud Storage file, temporary files might be created in the output location before the `write` operation is finalized.

### Go

By default, Compute Engine VMs are deleted when the Dataflow job completes, regardless of whether the job succeeds or fails. Consequently, the associated [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks), and any intermediate data that might be stored on it, is deleted. The intermediate data stored in Cloud Storage can be found in sublocations of the Cloud Storage path that you provide as your `--staging_location` or `--temp_location`. If you're writing output to a Cloud Storage file, temporary files might be created in the output location before the `write` operation is finalized.

### Data in pipeline logs and telemetry

Information stored in [Cloud Logging](https://docs.cloud.google.com/logging/docs/region-support) is primarily generated by the code in your Dataflow program. The Dataflow service might also generate warning and error data in Cloud Logging, but this data is the only intermediate data that the service adds to logs. Cloud Logging is a global service.

Telemetry data and associated metrics are encrypted at rest, and access to this data is controlled by your Google Cloud project's read permissions.

### Data in Dataflow services

If you use Dataflow Shuffle or Dataflow Streaming for your pipeline, don't specify the zone pipeline options. Instead, specify the region and set the value to one of the regions where Shuffle or Streaming is available. Dataflow auto-selects the zone in the region that you specify. The end-user data in transit stays within the worker VMs and in the same zone. These Dataflow jobs can still read and write to sources and sinks that are outside the VM zone. The data in transit can also be sent to Dataflow Shuffle or Dataflow Streaming services. However, the data always remains in the region specified in the pipeline code.

### Recommended practice

We recommend that you use the security mechanisms available in the underlying cloud resources of your pipeline. These mechanisms include the data security capabilities of data sources and sinks such as BigQuery and Cloud Storage. It's also best not to mix different trust levels in a single project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
