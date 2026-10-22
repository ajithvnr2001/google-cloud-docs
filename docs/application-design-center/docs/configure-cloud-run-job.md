---
url: https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run-job/
title: Configure a Cloud Run job \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:36.412492+00:00
---

# Configure a Cloud Run job  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a Cloud Run job Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Run jobs let you run containerized, non-HTTP tasks, such as scheduled batch processing and data transformations, that execute to completion and exit. Application Design Center helps you configure these job components for your specific component connections and configuration parameters. The configuration parameters are listed in the [terraform-google-cloud-run/modules/job-exec](https://github.com/GoogleCloudPlatform/terraform-google-cloud-run/tree/main/modules/job-exec) Terraform module.

## Component connections

The following table includes the components that you can connect to a Cloud Run job component, and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Service account](https://docs.cloud.google.com/application-design-center/docs/configure-service-account) | 

  * The Cloud Run job uses the service account as a service identity.
  * The service account email is added to the Cloud Run job.

| [Configure service identity for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity)  
[Cloud SQL (MySQL)](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-sql-mysql) | 

  * The Cloud Run job can read and write data to the Cloud SQL (MySQL) instance.

| [Connect from Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run)  
[Cloud SQL (PostgreSQL)](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-sql-postgresql) | 

  * The Cloud Run job can read and write data to the Cloud SQL (PostgreSQL) instance.

| [Connect from Cloud Run](https://docs.cloud.google.com/sql/docs/postgres/connect-run)  
[Cloud Storage](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-storage) | 

  * The Cloud Run job can communicate with the Cloud Storage bucket.
  * The Cloud Storage bucket name is added to the Cloud Run job.

| [Connect to Google Cloud services](https://docs.cloud.google.com/run/docs/integrate/using-gcp-services)  
  
## Required configuration parameters

If your template includes a Cloud Run job, you must configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Project ID** | The project where you want to deploy the Cloud Run job. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
**Name** | [name](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs#Job.FIELDS.name) | [Cloud Run services](https://docs.cloud.google.com/run/docs/resource-model#services)  
**Region** | The Cloud Run service deployment location. | [Cloud Run locations](https://docs.cloud.google.com/run/docs/locations)  
**Image** | [image](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#FIELDS.image) | [Deploying container images](https://docs.cloud.google.com/run/docs/deploying)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
| **Create Service Account** | Create a new service account for the Cloud Run job. | [Configure service identity for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity)  
| **Service Account Project Roles** | Roles to grant to the newly created service account. Enable **Create Service Account** and don't provide input for **Service Account**. | [Configure service identity for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity)  
| **Exec** | Whether to execute the job after it's created. | [Execute jobs](https://docs.cloud.google.com/run/docs/execute/jobs)  
| **Service Account Email** | [serviceAccount](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs.executions.tasks#Task.FIELDS.service_account) | [Configure service identity for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity)  
| **Argument** | [args[]](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#FIELDS.args) | [Configure containers for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/containers)  
| **Container Command** | [command](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#FIELDS.command) | [Configure containers for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/containers)  
Env Vars | **Name** | [name](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#EnvVar.FIELDS.name) | [Environment variables for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/environment-variables)  
**Value** | [value](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#EnvVar.FIELDS.value) | [Environment variables for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/environment-variables)  
Env Secret Vars | **Name** | [EnvVarSource](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#envvarsource) | [Configure secrets for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/secrets)  
**Secret** | [secret](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#SecretKeySelector.FIELDS.secret) | [Configure secrets for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/secrets)  
**Version** | [version](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#SecretKeySelector.FIELDS.version) | [Configure secrets for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/secrets)  
| **Launch Stage** | [LaunchStage](https://docs.cloud.google.com/run/docs/reference/rest/v2/LaunchStage) | [Product launch stages](https://docs.cloud.google.com/products#product-launch-stages)  
Labels | **Key** | [labels](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs#Job.FIELDS.labels) | [Configure labels for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/labels)  
**Value** | [labels](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs#Job.FIELDS.labels) | [Configure labels for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/labels)  
| **Max Retries** | [maxRetries](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs.executions.tasks#Task.FIELDS.max_retries) | [Set maximum retries for jobs](https://docs.cloud.google.com/run/docs/configuring/max-retries)  
| **Parallelism** | [parallelism](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs.executions#Execution.FIELDS.parallelism) | [Set parallelism for jobs](https://docs.cloud.google.com/run/docs/configuring/parallelism)  
| **Task Count** | [taskCount](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs.executions#Execution.FIELDS.task_count) | [Override job configuration for a specific execution](https://docs.cloud.google.com/run/docs/execute/jobs#override-job-configuration)  
Volumes | **Name** | [name](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#FIELDS.name) | [Configure in-memory volume mounts for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/in-memory-volume-mounts)  
**Instances** | [instances[]](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#cloudsqlinstance) | [Connect from Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run#terraform)  
**Bucket** | [bucket](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#GCSVolumeSource.FIELDS.bucket) | [Configure Cloud Storage volume mounts for services](https://docs.cloud.google.com/run/docs/configuring/jobs/cloud-storage-volume-mounts)  
**Read Only** | [readOnly](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#GCSVolumeSource.FIELDS.read_only) | [Configure Cloud Storage volume mounts for services](https://docs.cloud.google.com/run/docs/configuring/jobs/cloud-storage-volume-mounts)  
**Mount Options** | [mountOptions[]](https://docs.cloud.google.com/run/docs/reference/rest/v2/Volume#GCSVolumeSource.FIELDS.mount_options) | [Configure Cloud Storage volume mounts for services](https://docs.cloud.google.com/run/docs/configuring/jobs/cloud-storage-volume-mounts)  
Volume Mounts | **Name** | [name](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#VolumeMount.FIELDS.name) | [Connect from Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run)  
**Mount Path** | [mountPath](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#VolumeMount.FIELDS.mount_path) | [Connect from Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run)  
Vpc Access | **Connector** | [connector](https://docs.cloud.google.com/run/docs/reference/rest/v2/VpcAccess#FIELDS.connector) | [VPC with connectors](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors)  
**Egress** | [egress](https://docs.cloud.google.com/run/docs/reference/rest/v2/VpcAccess#FIELDS.egress) | [Control egress service traffic](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#egress-service)  
Limits | **Cpu** | [limits](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#ResourceRequirements.FIELDS.limits) | [Configure CPU limits for jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/cpu)  
**Memory** | [limits](https://docs.cloud.google.com/run/docs/reference/rest/v2/Container#ResourceRequirements.FIELDS.limits) | [Configure memory limits for services](https://docs.cloud.google.com/run/docs/configuring/jobs/memory-limits)  
| **Timeout** | [timeout](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs.executions.tasks#Task.FIELDS.timeout) | [Set task timeout for jobs](https://docs.cloud.google.com/run/docs/configuring/task-timeout)  
| **Cloud Run Deletion Protection** | Prevents Terraform from destroying or recreating Cloud Run jobs and services. | [deletion_protection](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_job#deletion_protection-1)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
