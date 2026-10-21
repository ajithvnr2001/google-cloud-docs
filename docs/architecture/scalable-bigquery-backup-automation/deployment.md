---
url: https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation/deployment/
title: Deploy scalable BigQuery backup automation \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:09.005622+00:00
---

# Deploy scalable BigQuery backup automation  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation/deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Deploy scalable BigQuery backup automation Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-09-17 UTC

This document describes how you deploy [Scalable BigQuery backup automation](https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation).

This document is intended for cloud architects, engineers, and data governance officers who want to define and automate data policies in their organizations. Experience with Terraform is helpful.

## Architecture

The following diagram shows the automated backup architecture:

![Architecture for the automated backup solution.](https://docs.cloud.google.com/static/architecture/images/bq-backup-manager-diagram.svg)![](https://docs.cloud.google.com/static/architecture/images/bq-backup-manager-diagram.svg)

Cloud Scheduler triggers the run. The dispatcher service, using BigQuery API, lists the in-scope tables. Through a Pub/Sub message, the dispatcher service submits one request for each table to the configurator service. The configurator service determines the backup policies for the tables, and then submits one request for each table to the relevant Cloud Run service. The Cloud Run service then submits a request to the BigQuery API and runs the backup operations. Pub/Sub triggers the tagger service, which logs the results and updates the backup state in the Cloud Storage metadata layer.

For details about the architecture, see [Scalable BigQuery backup automation](https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation#architecture).

## Objectives

  * Build Cloud Run services.
  * Configure Terraform variables.
  * Run the Terraform and manual deployment scripts.
  * Run the solution.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [BigQuery](https://cloud.google.com/bigquery/pricing)
  * [Pub/Sub](https://cloud.google.com/pubsub/pricing)
  * [Cloud Logging](https://cloud.google.com/logging/pricing)
  * [Cloud Run](https://cloud.google.com/run/pricing)
  * [Cloud Storage](https://cloud.google.com/storage/pricing)
  * [Cloud Scheduler](https://cloud.google.com/scheduler/pricing)
  * [Firestore in Datastore mode (Datastore)](https://cloud.google.com/datastore/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

If you're re-deploying the solution, you can skip this section (for example, after new commits).

In this section, you create one-time resources.

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. If you want to create a new Google Cloud project to use as the host project for the deployment, use the [`gcloud projects create`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/create) command:
         
         gcloud projects create PROJECT_ID
         

Replace PROJECT_ID with the ID of the project you want to create.

  3. Install Maven:

     1. Download [Maven](https://maven.apache.org/download.cgi).
     2. In Cloud Shell, add Maven to `PATH`:
            
            export PATH=/DOWNLOADED_MAVEN_DIR/bin:$PATH
            

  4. In Cloud Shell, clone the GitHub repository:
         
         git clone https://github.com/GoogleCloudPlatform/bq-backup-manager.git
         

  5. Set and export the following environment variables:
         
         export PROJECT_ID=PROJECT_ID
         export TF_SA=bq-backup-mgr-terraform
         export COMPUTE_REGION=COMPUTE_REGION
         export DATA_REGION=DATA_REGION
         export BUCKET_NAME=${PROJECT_ID}-bq-backup-mgr
         export BUCKET=gs://${BUCKET_NAME}
         export DOCKER_REPO_NAME=docker-repo
         export CONFIG=bq-backup-manager
         export ACCOUNT=ACCOUNT_EMAIL
         
         gcloud config configurations create $CONFIG
         gcloud config set project $PROJECT_ID
         gcloud config set account $ACCOUNT
         gcloud config set compute/region $COMPUTE_REGION
         
         gcloud auth login
         gcloud auth application-default login
         

Replace the following:

     * PROJECT_ID: the ID of the Google Cloud host project that you want to deploy the solution to.
     * COMPUTE_REGION: the Google Cloud [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) where you want to deploy compute resources like Cloud Run and Identity and Access Management (IAM).
     * DATA_REGION: the Google Cloud region you want to deploy data resources (such as buckets and datasets) to.
     * ACCOUNT_EMAIL: the user account email address.
  6. Enable the APIs:
         
         ./scripts/enable_gcp_apis.sh
         

The script enables the following APIs:

     * Cloud Resource Manager API
     * IAM API
     * Data Catalog API
     * Artifact Registry API
     * BigQuery API
     * Pub/Sub API
     * Cloud Storage API
     * Cloud Run Admin API
     * Cloud Build API
     * Service Usage API
     * App Engine Admin API
     * Serverless VPC Access API
     * Cloud DNS API
  7. Prepare the Terraform state bucket:
         
         gcloud storage buckets create $BUCKET --project=$PROJECT_ID --location=$COMPUTE_REGION --uniform-bucket-level-access
         

  8. Prepare the Terraform service account:
         
         ./scripts/prepare_terraform_service_account.sh
         

  9. To publish images that this solution uses, prepare a [Docker](https://docs.docker.com/guides/) repository:
         
         gcloud artifacts repositories create $DOCKER_REPO_NAME
           --repository-format=docker \
           --location=$COMPUTE_REGION \
           --description="Docker repository for backups"
         




## Deploy the infrastructure

Make sure that you've completed Before you begin at least once.

In this section, follow the steps to deploy or redeploy the latest codebase to the Google Cloud environment.

### Activate the gcloud CLI configuration

  * In Cloud Shell, activate and authenticate the gcloud CLI configuration:
        
        gcloud config configurations activate $CONFIG
        
        gcloud auth login
        gcloud auth application-default login
        




### Build Cloud Run services images

  * In Cloud Shell, build and deploy docker images to be used by the Cloud Run service:
        
        export DISPATCHER_IMAGE=${COMPUTE_REGION}-docker.pkg.dev/${PROJECT_ID}/${DOCKER_REPO_NAME}/bqsm-dispatcher-service:latest
        export CONFIGURATOR_IMAGE=${COMPUTE_REGION}-docker.pkg.dev/${PROJECT_ID}/${DOCKER_REPO_NAME}/bqsm-configurator-service:latest
        export SNAPSHOTER_BQ_IMAGE=${COMPUTE_REGION}-docker.pkg.dev/${PROJECT_ID}/${DOCKER_REPO_NAME}/bqsm-snapshoter-bq-service:latest
        export SNAPSHOTER_GCS_IMAGE=${COMPUTE_REGION}-docker.pkg.dev/${PROJECT_ID}/${DOCKER_REPO_NAME}/bqsm-snapshoter-gcs-service:latest
        export TAGGER_IMAGE=${COMPUTE_REGION}-docker.pkg.dev/${PROJECT_ID}/${DOCKER_REPO_NAME}/bqsm-tagger-service:latest
        
        ./scripts/deploy_services.sh
        




### Configure Terraform variables

This deployment uses Terraform for configurations and a deployment script.

  1. In Cloud Shell, create a new Terraform TFVARS file in which you can override the variables in this section:
         
         export VARS=FILENAME
         .tfvars
         

Replace FILENAME with the name of the variables file that you created (for example, `my-variables`). You can use the [`example-variables`](https://github.com/GoogleCloudPlatform/bq-backup-manager/blob/main/terraform/example-variables.text) file as a reference.

  2. In the TFVARS file, configure the project variables:
         
         project = "PROJECT_ID"
         compute_region = "COMPUTE_REGION"
         data_region = "DATA_REGION"
         

You can use the default values that are defined in the [variables.tf](https://github.com/GoogleCloudPlatform/bq-backup-manager/blob/main/terraform/variables.tf) file or change the values.

  3. Configure the Terraform service account, which you created and prepared earlier in Before you begin:
         
         terraform_service_account =
         "bq-backup-mgr-terraform@PROJECT_ID.iam.gserviceaccount.com"
         

Make sure that you use the full email address of the account that you created.

  4. Configure the Cloud Run services to use the container images that you built and deployed earlier:
         
         dispatcher_service_image     = "${COMPUTE_REGION}-docker.pkg.dev/${PROJECT_ID}/${DOCKER_REPO_NAME}/bqsm-dispatcher-service:latest"
         configurator_service_image   = "${COMPUTE_REGION}-docker.pkg.dev/${PROJECT_ID}/${DOCKER_REPO_NAME}/bqsm-configurator-service:latest"
         snapshoter_bq_service_image  = "${COMPUTE_REGION}-docker.pkg.dev/${PROJECT_ID}/${DOCKER_REPO_NAME}/bqsm-snapshoter-bq-service:latest"
         snapshoter_gcs_service_image = "${COMPUTE_REGION}-docker.pkg.dev/${PROJECT_ID}/${DOCKER_REPO_NAME}/bqsm-snapshoter-gcs-service:latest"
         tagger_service_image         = "${COMPUTE_REGION}-docker.pkg.dev/${PROJECT_ID}/${DOCKER_REPO_NAME}/bqsm-tagger-service:latest"
         

This script instructs Terraform to use these published images in the Cloud Run services, which Terraform creates later.

Terraform only links a Cloud Run service to an existing image. It doesn't build the images from the codebase, because that was completed in a previous step.

  5. In the `schedulers` variable, define at least one scheduler. The scheduler periodically lists and checks tables for required backups, based on their table-level backup cron schedules.
         
         {
         name    = "SCHEDULER_NAME"
         cron    = "SCHEDULER_CRON"
         payload = {
             is_force_run = FORCE_RUN
             is_dry_run   = DRY_RUN
         
             folders_include_list  = [FOLDERS_INCLUDED]
             projects_include_list = [PROJECTS_INCLUDED]
             projects_exclude_list = [PROJECTS_EXCLUDED]
             datasets_include_list =  [DATASETS_INCLUDED]
             datasets_exclude_list =  [DATASETS_EXCLUDED]
             tables_include_list   =  [TABLES_INCLUDED]
             tables_exclude_list   =  [TABLES_EXCLUDED]
             }
         }
         

Replace the following:

     * SCHEDULER_NAME: the display name of the Cloud Scheduler.
     * SCHEDULER_CRON: the frequency with which the scheduler checks whether a backup is due for the in-scope tables, based on their individual backup schedules. This can be any [unix-cron](https://man7.org/linux/man-pages/man5/crontab.5.html) compatible string. For example, `0 * * * *` is an hourly frequency.
     * FORCE_RUN: a boolean value. Set the value to `false` if you want the scheduler to use the tables' cron schedules. If set to `true`, all in-scope tables are backed up, regardless of their cron setting.
     * DRY_RUN: a boolean value. When set to `true`, no actual backup operations take place. Only log messages are generated. Use `true` when you want to test and debug the solution without incurring backup costs.
     * FOLDERS_INCLUDED: a list of numerical IDs for folders that contain BigQuery data (for example, `1234, 456`). When set, the solution backs up the tables in the specified folders, and ignores the `projects_include_list`, `datasets_include_list`, and `tables_include_list` field settings.
     * PROJECTS_INCLUDED: a list of project names (for example, `"project1", "project2"`). When set, the solution backs up the tables in the specified projects, and ignores the `datasets_include_list` and `tables_include_list` field settings. This setting is ignored if you set the `folders_include_list` field.
     * PROJECTS_EXCLUDED: a list of project names or regular expression (for example, `"project1", "regex:^test_"`). When set, the solution does _not_ take backups of the tables in the specified projects. You can use this setting in combination with the `folders_include_list` field.
     * DATASETS_INCLUDED: a list of datasets (for example, `"project1.dataset1", "project1.dataset2"`). When set, the solution backs up the tables in the specified datasets, and ignores the `tables_include_list` field setting. This setting is ignored if you set the `folders_include_list` or `projects_include_list` fields.
     * DATASETS_EXCLUDED: a list of datasets or regular expression (for example, `"project1.dataset1", "regex:.*\\_landing$"`). When set, the solution does _not_ take backups of the tables in the specified datasets. You can use this setting in combination with the `folders_include_list` or `projects_include_list` fields.
     * TABLES_INCLUDED: a list of tables (for example, `"project1.dataset1.table 1", "project1.dataset2.table2"`). When set, the solution backs up the specified tables. This setting is ignored if you set the `folders_include_list`, `projects_include_list`, or `datasets_include_list` fields.
     * TABLES_EXCLUDED: a list of tables or regular expression (for example, `"project1.dataset1.table 1", "regex:.*\_test"`). When set, the solution does _not_ take backups of the specified tables. You can use this setting in combination with the `folders_include_list`, `projects_include_list`, or `datasets_include_list` fields.

All exclusion lists accept regular expressions in the form `regex:REGULAR_EXPRESSION`.

If the fully qualified entry name (for example, `"project.dataset.table"`) matches any of the supplied regular expression, it's excluded from the backup scope.

The following are some common use cases:

     * Exclude all dataset names that end with `_landing`: `datasets_exclude_list = ["regex:.*\\_landing$"]`
     * Exclude all tables ending with `_test`, `_tst`, `_bkp`, or `_copy`: `tables_exclude_list = ["regex:.*\_(test|tst|bkp|copy)"]`



### Define fallback policies

On each run, the solution needs to determine the backup policy of each in-scope table. For more information about the types of policies, see [Backup policies](https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation#backup-policies). This section shows you how to define a fallback policy.

A fallback policy is defined with a `default_policy` variable and a set of exceptions or overrides on different levels (folder, project, dataset, and table). This approach provides granular flexibility without the need for an entry for each table.

There are additional sets of policy fields, depending on the backup method that you decide to use: BigQuery snapshots, exports to Cloud Storage, or both.

  1. In the TFVARS file, for the `default_policy` variable, set the following common fields for the default policy:
         
         fallback_policy = {
           "default_policy" : {
             "backup_cron" : "BACKUP_CRON"
             "backup_method" : "BACKUP_METHOD",
             "backup_time_travel_offset_days" : "OFFSET_DAYS",
             "backup_storage_project" : "BACKUP_STORAGE_PROJECT",
             "backup_operation_project" : "BACKUP_OPERATIONS_PROJECT",
         
         

Replace the following:

     * BACKUP_CRON: a cron expression to set the frequency with which a table is backed up (for example, for backups every 6 hours, specify `0 0 */6 * * *`). This must be a [Spring-Framework](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/scheduling/support/CronExpression.html) compatible cron expression.
     * BACKUP_METHOD: the method, which you specify as `BigQuery Snapshot`, `GCS Snapshot` (to use the export to Cloud Storage method), or `Both`. You need to provide the required fields for each chosen backup method, as shown later.
     * OFFSET_DAYS: the number of days in the past that determines the point in time from which to back up the tables. Values can be a number between 0 and 7.
     * BACKUP_STORAGE_PROJECT: the ID of the project where all snapshot and export operations are stored. This is the same project where the `bq_snapshot_storage_dataset` and `gcs_snapshot_storage_location` resides. Small deployments can use the host project, but large scale deployments should use a separate project.
     * BACKUP_OPERATIONS_PROJECT: an optional setting, where you specify the ID of the project where all snapshot and export operations run. Snapshot and export job [quotas and limits](https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation#limits) are applicable to this project. This can be the same value as `backup_storage_project`. If not set, the solution uses the source table's project.
  2. If you specified `BigQuery Snapshot` or `Both` as the `backup_method`, add the following fields after the common fields, in the `default_policy` variable:
         
         "bq_snapshot_expiration_days" : "SNAPSHOT_EXPIRATION",
           "bq_snapshot_storage_dataset" : "DATASET_NAME",
         

Replace the following:

     * SNAPSHOT_EXPIRATION: the number of days to keep each snapshot (for example, `15`).
     * DATASET_NAME: the name of the dataset to store snapshots in (for example, `backups`). The dataset must already exist in the project specified for `backup_storage_project`.
  3. If you specified `GCS Snapshot` (to use the export to Cloud Storage method) or `Both` as the `backup_method`, add the following fields to the `default_policy` variable:
         
         "gcs_snapshot_storage_location" : "STORAGE_BUCKET",
           "gcs_snapshot_format" : "FILE_FORMAT",
           "gcs_avro_use_logical_types" : AVRO_TYPE,
           "gcs_csv_delimiter" : "CSV_DELIMITER",
           "gcs_csv_export_header" : CSV_EXPORT_HEADER
         

Replace the following:

     * STORAGE_BUCKET: the Cloud Storage bucket in which to store the exported data, in the format `gs://bucket/path/`. For example, `gs://bucket1/backups/`.
     * FILE_FORMAT: the file format and compression used to export a BigQuery table to Cloud Storage. Available values are `CSV`, `CSV_GZIP`, `JSON`, `JSON_GZIP`, `AVRO`, `AVRO_DEFLATE`, `AVRO_SNAPPY`, `PARQUET`, `PARQUET_SNAPPY`, and `PARQUET_GZIP`.
     * AVRO_TYPE: a boolean value. If set to `false`, the BigQuery types are exported as strings. If set to `true`, the types are exported as their corresponding [Avro logical type](https://avro.apache.org/docs/1.10.2/spec.html#Logical+Types). This field is required when the `gcs_snapshot_format` is any Avro type format.
     * CSV_DELIMITER: the delimiter used for the exported CSV files, and the value can be any ISO-8859-1 single-byte character. You can use `\t` or `tab` to specify tab delimiters. This field is required when the `gcs_snapshot_format` is any CSV type format.
     * CSV_EXPORT_HEADER: a boolean value. If set to `true`, the column headers are exported to the CSV files. This field is required when the `gcs_snapshot_format` is any CSV type format.

For details and Avro type mapping, see the following table:

BigQuery Type | Avro Logical Type  
---|---  
`TIMESTAMP` | `timestamp-micros` (annotates Avro `LONG`)  
`DATE` | `date` (annotates Avro `INT`)  
`TIME` | `timestamp-micro` (annotates Avro `LONG`)  
`DATETIME` | `STRING` (custom named logical type `datetime`)  
  4. Add override variables for specific folders, projects, datasets, and tables:
         
         },
           "folder_overrides" : {
            "FOLDER_NUMBER" : {
            },
           },
         
           "project_overrides" : {
            "PROJECT_NAME" : {
            }
           },
         
           "dataset_overrides" : {
            "PROJECT_NAME.DATASET_NAME" : {
            }
           },
         
           "table_overrides" : {
            "PROJECT_NAME.DATASET_NAME.TABLE_NAME" : {
            }
           }
         }
         

Replace the following:

     * FOLDER_NUMBER: specify the folder for which you want to set override fields.
     * PROJECT_NAME: specify the project when you set override fields for a particular project, dataset, or table.
     * DATASET_NAME: specify the dataset when you set override fields for a particular dataset or table.
     * TABLE_NAME: specify the table for which you want to set override fields.

For each override entry, such as a specific project in the `project_overrides` variable, add the common fields and the required fields for the backup method that you specified earlier in `default_policy`.

If you don't want to set overrides for a particular level, set that variable to an empty map (for example, `project_overrides : {}`).

In the following example, override fields are set for a specific table that uses the BigQuery snapshot method:
    
    },
      "project_overrides" : {},
    
      "table_overrides" : {
       "example_project1.dataset1.table1" : {
        "backup_cron" : "0 0 */5 * * *", # every 5 hours each day
        "backup_method" : "BigQuery Snapshot",
        "backup_time_travel_offset_days" : "7",
        "backup_storage_project" : "project name",
        "backup_operation_project" : "project name",
        # bq settings
        "bq_snapshot_expiration_days" : "14",
        "bq_snapshot_storage_dataset" : "backups2"
        },
       }
    }
    




For a full example of a fallback policy, see the [`example-variables` file](https://github.com/GoogleCloudPlatform/bq-backup-manager/blob/4a8ef598530ccd534d7632b8ee690c808cbc169c/terraform/example-variables.text#L34).

### Configure additional backup operation projects

  * If you want to specify additional backup projects, such as those defined in external configurations (table-level backup policy) or the table source projects, configure the following variable:
        
        additional_backup_operation_projects = [ADDITIONAL_BACKUPS]
        

Replace ADDITIONAL_BACKUPS with a comma-separated list of project names (for example, `"project1", "project2"`). If you're using only the fallback backup policy without table-level external policies, you can set the value to an empty list.

If you don't add this field, any projects that are specified in the optional `backup_operation_project` field are automatically included as backup projects.




### Configure Terraform service account permissions

In the previous steps, you configured the backup projects where the backup operations run. Terraform needs to deploy resources to those backup projects.

The service account that Terraform uses must have the required permissions for these specified backup projects.

  * In Cloud Shell, grant the service account permissions for all of the projects where backup operations run:
        
        ./scripts/prepare_backup_operation_projects_for_terraform.sh BACKUP_OPERATIONS_PROJECT DATA_PROJECTS ADDITIONAL_BACKUPS
        

Replace the following:

    * BACKUP_OPERATIONS_PROJECT: any projects defined in the `backup_operation_project` fields in any of the fallback policies and table-level policies.
    * DATA_PROJECTS: if no `backup_operation_project` field is defined in a fallback or table-level policy, include the projects for those source tables.
    * ADDITIONAL_BACKUPS: any projects that are defined in the `additional_backup_operation_projects` Terraform variable.



### Run the deployment scripts

  1. In Cloud Shell, run the Terraform deployment script:
         
         cd terraform
         
         terraform init \
             -backend-config="bucket=${BUCKET_NAME}" \
             -backend-config="prefix=terraform-state" \
             -backend-config="impersonate_service_account=$TF_SA@$PROJECT_ID.iam.gserviceaccount.com"
         
         terraform plan -var-file=$VARS
         
         terraform apply -var-file=$VARS
         

  2. Add the time to live (TTL) policies for Firestore:
         
         gcloud firestore fields ttls update expires_at \
             --collection-group=project_folder_cache \
             --enable-ttl \
             --async \
             --project=$PROJECT_ID
         

The solution uses Datastore as a cache in some situations. To save costs and improve lookup performance, the TTL policy allows Firestore to automatically delete entries that are expired.




### Set up access to sources and destinations

  1. In Cloud Shell, set the following variables for the service accounts used by the solution:
         
         export SA_DISPATCHER_EMAIL=dispatcher@${PROJECT_ID}.iam.gserviceaccount.com
         export SA_CONFIGURATOR_EMAIL=configurator@${PROJECT_ID}.iam.gserviceaccount.com
         export SA_SNAPSHOTER_BQ_EMAIL=snapshoter-bq@${PROJECT_ID}.iam.gserviceaccount.com
         export SA_SNAPSHOTER_GCS_EMAIL=snapshoter-gcs@${PROJECT_ID}.iam.gserviceaccount.com
         export SA_TAGGER_EMAIL=tagger@${PROJECT_ID}.iam.gserviceaccount.com
         

If you've changed the default names in Terraform, update the service account emails.

  2. If you've set the `folders_include_list` field, and want to set the scope of the BigQuery scan to include certain folders, grant the required permissions on the folder level:
         
         ./scripts/prepare_data_folders.sh FOLDERS_INCLUDED
         

  3. To enable the application to execute the necessary tasks in different projects, grant the required permissions on each of these projects:
         
         ./scripts/prepare_data_projects.sh DATA_PROJECTS
         ./scripts/prepare_backup_storage_projects.sh BACKUP_STORAGE_PROJECT
         ./scripts/prepare_backup_operation_projects.sh BACKUP_OPERATIONS_PROJECT
         

Replace the following:

     * DATA_PROJECTS: the data projects (or source projects) that contain the source tables that you want to back up (for example, `project1 project2`). Include the following projects:

       * Projects that are specified in the inclusion lists in the Terraform variable `schedulers`.
       * If you want to back up tables in the host project, include the host project.
     * BACKUP_STORAGE_PROJECT: the backup storage projects (or destination projects) where the solution stores the backups (for example, `project1 project2`). You need to include the projects that are specified in the following fields:

       * The `backup_storage_project` fields in all of the fallback policies.
       * The `backup_storage_project` fields in all of the table-level policies.

Include backup storage projects that are used in multiple fields or that are used as both the source and destination project

     * BACKUP_OPERATIONS_PROJECT: the data operation projects where the solution runs the backup operations (for example, `project1 project2`). You need to include the projects that are specified in the following fields:

       * The `backup_operation_project` fields in all of the fallback policies.
       * All inclusion lists in the scope of the BigQuery scan (if you don't set the `backup_operation_project` field).
       * The `backup_operation_project` fields in all of the table-level policies.

Include backup operations projects that are used in multiple fields or that are used as both the source and destination project.

  4. For tables that use [column-level access control](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro#policy_tags), identify all policy tag taxonomies that are used by your tables (if any), and grant the solution's service accounts access to the table data:
         
         TAXONOMY="projects/TAXONOMY_PROJECT/locations/TAXONOMY_LOCATION/taxonomies/TAXONOMY_ID"
         
         gcloud data-catalog taxonomies add-iam-policy-binding \
         $TAXONOMY \
         --member="serviceAccount:${SA_SNAPSHOTER_BQ_EMAIL}" \
         --role='roles/datacatalog.categoryFineGrainedReader'
         
         gcloud data-catalog taxonomies add-iam-policy-binding \
         $TAXONOMY \
         --member="serviceAccount:${SA_SNAPSHOTER_GCS_EMAIL}" \
         --role='roles/datacatalog.categoryFineGrainedReader'
         

Replace the following:

     * TAXONOMY_PROJECT: the project ID in the policy tag taxonomy
     * TAXONOMY_LOCATION: the location specified in the policy tag taxonomy
     * TAXONOMY_ID: the taxonomy ID of the policy tag taxonomy
  5. Repeat the previous step for each policy tag taxonomy.




## Run the solution

After you deploy the solution, use the following sections to run and manage the solution.

### Set table-level backup policies

  * In Cloud Shell, create a table-level policy with the required fields, and then store the policy in the Cloud Storage bucket for policies:
        
        # Use the default backup policies bucket unless overwritten in the .tfvars
        export POLICIES_BUCKET=${PROJECT_ID}-bq-backup-manager-policies
        
        # set target table info
        export TABLE_PROJECT='TABLE_PROJECT'
        export TABLE_DATASET='TABLE_DATASET'
        export TABLE='TABLE_NAME'
        
        # Config Source must be 'MANUAL' when assigned this way
        export BACKUP_POLICY="{
        'config_source' : 'MANUAL',
        'backup_cron' : 'BACKUP_CRON',
        'backup_method' : 'BACKUP_METHOD',
        'backup_time_travel_offset_days' : 'OFFSET_DAYS',
        'backup_storage_project' : 'BACKUP_STORAGE_PROJECT',
        'backup_operation_project' : 'BACKUP_OPERATION_PROJECT',
        'gcs_snapshot_storage_location' : 'STORAGE_BUCKET',
        'gcs_snapshot_format' : 'FILE_FORMAT',
        'gcs_avro_use_logical_types' : 'AVRO_TYPE',
        'bq_snapshot_storage_dataset' : 'DATASET_NAME',
        'bq_snapshot_expiration_days' : 'SNAPSHOT_EXPIRATION'
        }"
        
        # File name MUST BE backup_policy.json
        echo $BACKUP_POLICY >> backup_policy.json
        
        gcloud storage cp backup_policy.json gs://${POLICIES_BUCKET}/policy/project=${TABLE_PROJECT}/dataset=${TABLE_DATASET}/table=${TABLE}/backup_policy.json
        

Replace the following:

    * TABLE_PROJECT: the project in which the table resides
    * TABLE_DATASET: the dataset of the table
    * TABLE_NAME: the name of the table



### Trigger backup operations

The Cloud Scheduler jobs that you configured earlier run automatically based on their cron expression.

You can also manually run the jobs in the Google Cloud console. For more information, see [Run your job](https://docs.cloud.google.com/scheduler/docs/schedule-run-cron-job#run-job).

### Monitor and report

With your host project (PROJECT_ID) selected, you can run the following queries in BigQuery Studio to get reports and information.

  * Get progress statistics of each run (including in-progress runs):
        
        SELECT * FROM `bq_backup_manager.v_run_summary_counts`
        

  * Get all fatal (non-retryable errors) for a single run:
        
        SELECT * FROM `bq_backup_manager.v_errors_non_retryable`
        WHERE run_id = 'RUN_ID'
        

Replace RUN_ID with the ID of the run.

  * Get all runs on a table and their execution information:
        
        SELECT * FROM `bq_backup_manager.v_errors_non_retryable`
        WHERE tablespec = 'project.dataset.table'
        

You can also specify a `grouped` version:
        
        SELECT * FROM `bq_backup_manager.v_audit_log_by_table_grouped`, UNNEST(runs) r
        WHERE r.run_has_retryable_error = FALSE
        

  * For debugging, you can get detailed request and response information for each service invocation:
        
        SELECT
        jsonPayload.unified_target_table AS tablespec,
        jsonPayload.unified_run_id AS run_id,
        jsonPayload.unified_tracking_id AS tracking_id,
        CAST(jsonPayload.unified_is_successful AS BOOL) AS configurator_is_successful,
        jsonPayload.unified_error AS configurator_error,
        CAST(jsonPayload.unified_is_retryable_error AS BOOL) AS configurator_is_retryable_error,
        CAST(JSON_VALUE(jsonPayload.unified_input_json, '$.isForceRun') AS BOOL) AS is_force_run,
        CAST(JSON_VALUE(jsonPayload.unified_output_json, '$.isBackupTime') AS BOOL) AS is_backup_time,
        JSON_VALUE(jsonPayload.unified_output_json, '$.backupPolicy.method') AS backup_method,
        CAST(JSON_VALUE(jsonPayload.unified_input_json, '$.isDryRun') AS BOOL) AS is_dry_run,
        jsonPayload.unified_input_json AS request_json,
        jsonPayload.unified_output_json AS response_json
        FROM `bq_backup_manager.run_googleapis_com_stdout`
        WHERE jsonPayload.global_app_log = 'UNIFIED_LOG'
        -- 1= dispatcher, 2= configurator, 3=bq snapshoter, -3=gcs snapshoter and 4=tagger
        AND jsonPayload.unified_component = "2"
        

  * Get the backup policies that are manually added or assigned by the system based on fallbacks:
        
        SELECT * FROM `bq_backup_manager.ext_backup_policies`
        




### Limitations

For more information about limits and quotas for each project that is specified in the `backup_operation_project` fields, see [Limits](https://docs.cloud.google.com/architecture/scalable-bigquery-backup-automation#limits).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this deployment, either delete the projects that contain the resources, or keep the projects and delete the individual resources.

### Delete the projects

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the new resources

As an alternative to deleting the projects, you can delete the resources created during this procedure.

  * In Cloud Shell, delete the Terraform resources:
        
        terraform destroy -var-file="${VARS}"
        

The command deletes almost all of the resources. Check to ensure that all the resources you want to delete are removed.




## What's next

  * Learn more about BigQuery: 
    * [BigQuery table snapshots](https://docs.cloud.google.com/bigquery/docs/table-snapshots-intro)
    * [BigQuery table exports to Cloud Storage](https://docs.cloud.google.com/bigquery/docs/exporting-data)
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Karim Wadie](https://www.linkedin.com/in/karimwadie) | Strategic Cloud Engineer

Other contributors: 

  * [Chris DeForeest](https://www.linkedin.com/in/chris-deforeest) | Site Reliability Engineer
  * [Eyal Ben Ivri](https://www.linkedin.com/in/eyalbenivri) | Cloud Solutions Architect
  * [Jason Davenport](https://www.linkedin.com/in/davenportjw) | Developer Advocate
  * [Jaliya Ekanayake](https://www.linkedin.com/in/jaliya) | Engineering Manager
  * [Muhammad Zain](https://www.linkedin.com/in/muhammad-zain-ul-islam-96a87994) | Strategic Cloud Engineer



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-09-17 UTC."],[],[]] 
