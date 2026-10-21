---
url: https://docs.cloud.google.com/knowledge-catalog/docs/import-using-workflows-custom-source/
title: Import metadata from a custom source using Workflows \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:29.749061+00:00
---

# Import metadata from a custom source using Workflows  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/import-using-workflows-custom-source/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Import metadata from a custom source using Workflows Stay organized with collections  Save and categorize content based on your preferences. 

A managed connectivity pipeline in Workflows lets you extract and import metadata from custom third-party data sources into Knowledge Catalog (formerly Dataplex Universal Catalog). You can run the pipeline on demand or on a recurring schedule to keep your catalog synchronized so that you can discover, search, and govern your external assets.

For more information about managed connectivity, see [Managed connectivity overview](https://docs.cloud.google.com/knowledge-catalog/docs/managed-connectivity-overview).

## Before you begin

Before you import metadata, complete the tasks in this section.

### Build a connector

A connector extracts the metadata from your data source and generates a metadata import file that can be imported by Knowledge Catalog. The connector is an Artifact Registry image that can be run on Managed Service for Apache Spark.

  * Build a custom connector that extracts metadata from your third-party source.

For an example connector that you can use as a reference template to build your own connector, see [Develop a custom connector for metadata import](https://docs.cloud.google.com/knowledge-catalog/docs/develop-custom-connector).




### Configure Google Cloud resources

  1. Enable the Workflows, Dataproc, Cloud Storage, Dataplex, Secret Manager, Artifact Registry, and Cloud Scheduler APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=workflows.googleapis.com,dataproc.googleapis.com,storage.googleapis.com,dataplex.googleapis.com,secretmanager.googleapis.com,artifactregistry.googleapis.com,cloudscheduler.googleapis.com)

If you don't plan to run the pipeline on a schedule, you don't need to enable the Cloud Scheduler API.

  2. [Create secrets in Secret Manager](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) to store the credentials for your third-party data source.

  3. [Configure your Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/network) to run Managed Service for Apache Spark workloads.

  4. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) to store the metadata import files.

  5. Create the following Knowledge Catalog resources:

     1. [Create custom aspect types](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#create-aspect-type) for the entries that you want to import.

     2. [Create custom entry types](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#create-entry-type) for the entries that you want to import.




### Required roles

A service account represents the identity of a workflow and determines what permissions the workflow has and which Google Cloud resources it can access. You need a service account for Workflows (to run the pipeline) and for Managed Service for Apache Spark (to run the connector).

You can use the Compute Engine default service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`), or [create your own service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) (or accounts) to run the managed connectivity pipeline.

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select the project that you want to import metadata into.

  3. Click person_add **Grant Access** , and then enter the service account's email address.

  4. Assign the following roles to the service account:

     * **Logs Writer**
     * **Dataplex Entry Group Owner**
     * **Dataplex Metadata Job Owner**
     * **Dataplex Catalog Editor**
     * **Dataproc Editor**
     * **Dataproc Worker**
     * **Secret Manager Secret Accessor** \- on the secret that stores the credentials for your data source
     * **Storage Object User** \- on the Cloud Storage bucket
     * **Artifact Registry Reader** \- on the Artifact Registry repository that contains the connector image
     * **Service Account User** \- if you use different service accounts, grant the service account running Workflows this role on the service account running the Managed Service for Apache Spark batch jobs
     * **Workflows Invoker** \- if you want to schedule the pipeline
  5. Save your changes.




###  gcloud 

  1. Grant roles to the service account. Run the following commands:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_ID" \
             --role=roles/logging.logWriter
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_ID" \
             --role=roles/dataplex.entryGroupOwner
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_ID" \
             --role=roles/dataplex.metadataJobOwner
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_ID" \
             --role=roles/dataplex.catalogEditor
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_ID" \
             --role=roles/dataproc.editor
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_ID" \
             --role=roles/dataproc.worker
         

Replace the following:

     * `PROJECT_ID`: the name of the target Google Cloud project to import the metadata into. 
     * `SERVICE_ACCOUNT_ID`: the service account, such as `my-service-account@my-project.iam.gserviceaccount.com`.
  2. Grant the service account the following roles on the resource level:
         
         gcloud secrets add-iam-policy-binding SECRET_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_ID" \
             --role=roles/secretmanager.secretaccessor
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:SERVICE_ACCOUNT_ID" \
             --role=roles/storage.objectUser \
             --condition=resource.name.startsWith('projects/_/buckets/BUCKET_ID')
         gcloud artifacts repositories add-iam-policy-binding REPOSITORY \
             --location=REPOSITORY_LOCATION \
             --member=SERVICE_ACCOUNT_ID} \
             --role=roles/artifactregistry.reader
         

Replace the following:

     * `SECRET_ID`: the ID of the secret that stores the credentials for your data source. It uses the format `projects/PROJECT_ID/secrets/SECRET_ID`.
     * `BUCKET_ID`: the name of the Cloud Storage bucket.
     * `REPOSITORY`: the Artifact Registry repository that contains the connector image.
     * `REPOSITORY_LOCATION`: the Google Cloud location where the repository is hosted.
  3. Grant the service account running Workflows the `roles/iam.serviceAccountUser` role on the service account running the Managed Service for Apache Spark batch jobs. You must grant this role even if you use the same service account for both Workflows and Managed Service for Apache Spark.
         
         gcloud iam service-accounts add-iam-policy-binding \
             serviceAccount:SERVICE_ACCOUNT_ID \
             --member='SERVICE_ACCOUNT_ID' \
             --role='roles/iam.serviceAccountUser'
         

If you use different service accounts, the value for the `--member` flag is the service account running the Managed Service for Apache Spark batch jobs.

  4. If you want to schedule the pipeline, grant the service account the following role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
          --member="SERVICE_ACCOUNT_ID" \
          --role=roles/workflows.invoker
         




## Import metadata

To import metadata, create and then execute a workflow that runs the managed connectivity pipeline. This pipeline extracts metadata from your custom data source, creates the necessary [entry groups](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#entry-groups), and imports the metadata into Knowledge Catalog. You can also create a schedule for running the pipeline.

### Console

  1. [Create the workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow). Provide the following information:

     * **Service account** : the service account that you configured in the Required roles section of this document. 
     * **Encryption** : select **Google-managed encryption key**.

**Note:** Customer-managed encryption keys (CMEK) aren't propagated to Knowledge Catalog and Managed Service for Apache Spark jobs for end-to-end encryption.
     * **Define workflow** : provide the following definition file:
           
           main:
             params: [args]
             steps:
               - init:
                   assign:
                   - WORKFLOW_ID: ${"metadataworkflow-" + sys.get_env("GOOGLE_CLOUD_WORKFLOW_EXECUTION_ID")}
                   - NETWORK_URI: ${default(map.get(args, "NETWORK_URI"), "")}
                   - SUBNETWORK_URI: ${default(map.get(args, "SUBNETWORK_URI"), "")}
                   - NETWORK_TAGS: ${default(map.get(args, "NETWORK_TAGS"), [])}
           
               - check_networking:
                   switch:
                     - condition: ${NETWORK_URI != "" and SUBNETWORK_URI != ""}
                       raise: "Error: cannot set both network_uri and subnetwork_uri. Please select one."
                     - condition: ${NETWORK_URI == "" and SUBNETWORK_URI == ""}
                       steps:
                        - submit_extract_job_with_default_network_uri:
                             assign:
                               - NETWORK_TYPE: "networkUri"
                               - NETWORKING: ${"projects/" + args.TARGET_PROJECT_ID + "/global/networks/default"}  
                     - condition: ${NETWORK_URI != ""}
                       steps:
                         - submit_extract_job_with_network_uri:
                             assign:
                               - NETWORKING: ${NETWORK_URI}
                               - NETWORK_TYPE: "networkUri"
                     - condition: ${SUBNETWORK_URI != ""}
                       steps:
                         - submit_extract_job_with_subnetwork_uri:
                             assign:
                               - NETWORKING: ${SUBNETWORK_URI}
                               - NETWORK_TYPE: "subnetworkUri"
                   next: check_create_target_entry_group
           
               - check_create_target_entry_group:
                   switch:
                     - condition: ${args.CREATE_TARGET_ENTRY_GROUP == true}
                       next: create_target_entry_group
                     - condition: ${args.CREATE_TARGET_ENTRY_GROUP == false}
                       next: prepare_pyspark_job_body
           
               - create_target_entry_group:
                   call: http.post
                   args:
                     url: ${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/entryGroups?entry_group_id=" + args.TARGET_ENTRY_GROUP_ID}
                     auth:
                       type: OAuth2
                       scopes: "https://www.googleapis.com/auth/cloud-platform"
                   next: prepare_pyspark_job_body
           
               - prepare_pyspark_job_body:
                   assign:
                     - pyspark_batch_body:
                         mainPythonFileUri: file:///main.py
                         args:
                           - ${"--target_project_id=" + args.TARGET_PROJECT_ID}
                           - ${"--target_location_id=" + args.CLOUD_REGION}
                           - ${"--target_entry_group_id=" + args.TARGET_ENTRY_GROUP_ID}
                           - ${"--output_bucket=" + args.CLOUD_STORAGE_BUCKET_ID}
                           - ${"--output_folder=" + WORKFLOW_ID}
                           - ${args.ADDITIONAL_CONNECTOR_ARGS}
                   next: add_jar_file_uri_if_present
           
               - add_jar_file_uri_if_present:
                   switch:
                     - condition: ${args.JAR_FILE_URI != "" and args.JAR_FILE_URI != null}
                       assign:
                         - pyspark_batch_body.jarFileUris : ${args.JAR_FILE_URI}
                   next: generate_extract_job_link
           
               - generate_extract_job_link:
                   call: sys.log
                   args:
                       data: ${"https://console.cloud.google.com/dataproc/batches/" + args.CLOUD_REGION + "/" + WORKFLOW_ID + "/monitoring?project=" + args.TARGET_PROJECT_ID}
                       severity: "INFO"
                   next: submit_pyspark_extract_job
           
               - submit_pyspark_extract_job:
                   call: http.post
                   args:
                     url: ${"https://dataproc.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/batches"}
                     auth:
                       type: OAuth2
                       scopes: "https://www.googleapis.com/auth/cloud-platform"
                     headers:
                       Content-Type: "application/json"
                     query:
                       batchId: ${WORKFLOW_ID}
                     body:
                       pysparkBatch: ${pyspark_batch_body}
                       runtimeConfig:
                           containerImage: ${args.CUSTOM_CONTAINER_IMAGE}
                       environmentConfig:
                           executionConfig:
                               serviceAccount: ${args.SERVICE_ACCOUNT}
                               stagingBucket: ${args.CLOUD_STORAGE_BUCKET_ID}
                               ${NETWORK_TYPE}: ${NETWORKING}
                               networkTags: ${NETWORK_TAGS}
                   result: RESPONSE_MESSAGE
                   next: check_pyspark_extract_job
           
               - check_pyspark_extract_job:
                   call: http.get
                   args:
                     url: ${"https://dataproc.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/batches/" + WORKFLOW_ID}
                     auth:
                       type: OAuth2
                       scopes: "https://www.googleapis.com/auth/cloud-platform"
                   result: PYSPARK_EXTRACT_JOB_STATUS
                   next: check_pyspark_extract_job_done
           
               - check_pyspark_extract_job_done:
                   switch:
                     - condition: ${PYSPARK_EXTRACT_JOB_STATUS.body.state == "SUCCEEDED"}
                       next: generate_import_logs_link
                     - condition: ${PYSPARK_EXTRACT_JOB_STATUS.body.state == "CANCELLED"}
                       raise: ${PYSPARK_EXTRACT_JOB_STATUS}
                     - condition: ${PYSPARK_EXTRACT_JOB_STATUS.body.state == "FAILED"}
                       raise: ${PYSPARK_EXTRACT_JOB_STATUS}
                   next: pyspark_extract_job_wait
           
               - pyspark_extract_job_wait:
                   call: sys.sleep
                   args:
                     seconds: 30
                   next: check_pyspark_extract_job
           
               - generate_import_logs_link:
                   call: sys.log
                   args:
                       data: ${"https://console.cloud.google.com/logs/query?project=" + args.TARGET_PROJECT_ID + "&query=resource.type%3D%22dataplex.googleapis.com%2FMetadataJob%22+AND+resource.labels.location%3D%22" + args.CLOUD_REGION + "%22+AND+resource.labels.metadata_job_id%3D%22" + WORKFLOW_ID + "%22"}
                       severity: "INFO"
                   next: submit_import_job
           
               - submit_import_job:
                   call: http.post
                   args:
                     url: ${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/metadataJobs?metadata_job_id=" + WORKFLOW_ID}
                     auth:
                       type: OAuth2
                       scopes: "https://www.googleapis.com/auth/cloud-platform"
                     body:
                       type: IMPORT
                       import_spec:
                         source_storage_uri: ${"gs://" + args.CLOUD_STORAGE_BUCKET_ID + "/" + WORKFLOW_ID + "/"}
                         entry_sync_mode: FULL
                         aspect_sync_mode: INCREMENTAL
                         log_level: ${default(map.get(args, "IMPORT_JOB_LOG_LEVEL"), "INFO")}
                         scope:
                           entry_groups: 
                             - ${"projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/entryGroups/" + args.TARGET_ENTRY_GROUP_ID}
                           entry_types: ${args.IMPORT_JOB_SCOPE_ENTRY_TYPES}
                           aspect_types: ${args.IMPORT_JOB_SCOPE_ASPECT_TYPES}
                   result: IMPORT_JOB_RESPONSE
                   next: get_job_start_time
           
               - get_job_start_time:
                   assign:
                     - importJobStartTime: ${sys.now()}
                   next: import_job_startup_wait
           
               - import_job_startup_wait:
                   call: sys.sleep
                   args:
                     seconds: 30
                   next: initial_get_import_job
           
               - initial_get_import_job:
                   call: http.get
                   args:
                     url: ${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/metadataJobs/" + WORKFLOW_ID}
                     auth:
                       type: OAuth2
                       scopes: "https://www.googleapis.com/auth/cloud-platform"
                   result: IMPORT_JOB_STATUS
                   next: check_import_job_status_available
           
               - check_import_job_status_available:
                   switch:
                     - condition: ${sys.now() - importJobStartTime > 300}  # 5 minutes = 300 seconds
                       next: kill_import_job
                     - condition: ${"status" in IMPORT_JOB_STATUS.body}
                       next: check_import_job_done
                   next: import_job_status_wait
           
               - import_job_status_wait:
                   call: sys.sleep
                   args:
                     seconds: 30
                   next: check_import_job_status_available
           
               - check_import_job_done:
                   switch:
                     - condition: ${IMPORT_JOB_STATUS.body.status.state == "SUCCEEDED"}
                       next: the_end
                     - condition: ${IMPORT_JOB_STATUS.body.status.state == "CANCELLED"}
                       raise: ${IMPORT_JOB_STATUS}
                     - condition: ${IMPORT_JOB_STATUS.body.status.state == "SUCCEEDED_WITH_ERRORS"}
                       raise: ${IMPORT_JOB_STATUS}
                     - condition: ${IMPORT_JOB_STATUS.body.status.state == "FAILED"}
                       raise: ${IMPORT_JOB_STATUS}
                     - condition: ${sys.now() - importJobStartTime > 43200}  # 12 hours = 43200 seconds
                       next: kill_import_job
                   next: import_job_wait
           
               - get_import_job:
                   call: http.get
                   args:
                     url: ${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/metadataJobs/" + WORKFLOW_ID}
                     auth:
                       type: OAuth2
                       scopes: "https://www.googleapis.com/auth/cloud-platform"
                   result: IMPORT_JOB_STATUS
                   next: check_import_job_done
           
               - import_job_wait:
                   call: sys.sleep
                   args:
                     seconds: 30
                   next: get_import_job
           
               - kill_import_job:
                   call: http.post
                   args:
                     url: ${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/metadataJobs/" + WORKFLOW_ID + ":cancel"}
                     auth:
                       type: OAuth2
                       scopes: "https://www.googleapis.com/auth/cloud-platform"
                   next: get_killed_import_job
           
               - get_killed_import_job:
                   call: http.get
                   args:
                     url: ${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/metadataJobs/" + WORKFLOW_ID}
                     auth:
                       type: OAuth2
                       scopes: "https://www.googleapis.com/auth/cloud-platform"
                   result: KILLED_IMPORT_JOB_STATUS
                   next: killed
           
               - killed:
                   raise: ${KILLED_IMPORT_JOB_STATUS}
           
               - the_end:
                   return: ${IMPORT_JOB_STATUS}
           

  2. To run the pipeline on demand, [execute the workflow](https://docs.cloud.google.com/workflows/docs/executing-workflow).

Provide the following runtime arguments:
         
         {
             "TARGET_PROJECT_ID": "PROJECT_ID",
             "CLOUD_REGION": "LOCATION_ID",
             "TARGET_ENTRY_GROUP_ID": "ENTRY_GROUP_ID",
             "CREATE_TARGET_ENTRY_GROUP": CREATE_ENTRY_GROUP_BOOLEAN,
             "CLOUD_STORAGE_BUCKET_ID": "BUCKET_ID",
             "SERVICE_ACCOUNT": "SERVICE_ACCOUNT_ID",
             "ADDITIONAL_CONNECTOR_ARGS": [ADDITIONAL_CONNECTOR_ARGUMENTS],
             "CUSTOM_CONTAINER_IMAGE": "CONTAINER_IMAGE",
             "IMPORT_JOB_SCOPE_ENTRY_TYPES": [ENTRY_TYPES],
             "IMPORT_JOB_SCOPE_ASPECT_TYPES": [ASPECT_TYPES],
             "IMPORT_JOB_LOG_LEVEL": "INFO",
             "JAR_FILE_URI": "",
             "NETWORK_TAGS": [],
             "NETWORK_URI": "",
             "SUBNETWORK_URI": ""
          }
         

Replace the following:

     * `PROJECT_ID`: the name of the target Google Cloud project to import the metadata into. 
     * `LOCATION_ID`: the target Google Cloud location where the Managed Service for Apache Spark and metadata import jobs will run, and metadata will be imported into. 
     * `ENTRY_GROUP_ID`: the ID of the entry group to import metadata into. The entry group ID can contain lowercase letters, numbers, and hyphens. 

The full resource name of this entry group is `projects/PROJECT_ID/locations/LOCATION_ID/entryGroups/ENTRY_GROUP_ID`. 

     * `CREATE_ENTRY_GROUP_BOOLEAN`: if you want the pipeline to create the entry group if it doesn't already exist in your project, set this value to `true`. 
     * `BUCKET_ID`: the name of the Cloud Storage bucket to store the metadata import file that is generated by the connector. Each workflow execution creates a new folder. 
     * `SERVICE_ACCOUNT_ID`: the service account that you configured in the Required roles section of this document. The service account runs the connector in Managed Service for Apache Spark.
     * `ADDITIONAL_CONNECTOR_ARGUMENTS`: a list of additional arguments to pass to the connector. For examples, see [Develop a custom connector for metadata import](https://docs.cloud.google.com/knowledge-catalog/docs/develop-custom-connector). Enclose each argument in double quotation marks, and separate the arguments with commas.
     * `CONTAINER_IMAGE`: the custom container image of the connector hosted in Artifact Registry. 
     * `ENTRY_TYPES`: a list of entry types that are in scope for import, in the format `projects/PROJECT_ID/locations/LOCATION_ID/entryTypes/ENTRY_TYPE_ID`. The `LOCATION_ID` must be either the same Google Cloud location that you import metadata into, or `global`. 
     * `ASPECT_TYPES`: a list of aspect types that are in scope for import, in the format `projects/PROJECT_ID/locations/LOCATION_ID/aspectTypes/ASPECT_TYPE_ID`. The `LOCATION_ID` must be either the same Google Cloud location that you import metadata into, or `global`. 
     * Optional: for the `NETWORK_TAGS` argument, provide a list of network tags. 
     * Optional: For the `NETWORK_URI` argument, provide the URI of the VPC network that connects to the data source. If you provide a network, omit the subnetwork argument. 
     * Optional: For the `SUBNETWORK_URI` argument, provide the URI of the subnetwork that connects to the data source. If you provide a subnet, omit the network argument. 

Depending on the amount of metadata that you import, the pipeline might take several minutes or longer to run. For more information about how to view the progress, see [Access workflow execution results](https://docs.cloud.google.com/workflows/docs/access-execution-results).

After the pipeline has finished running, you can [search for the imported metadata in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets).

  3. Optional: If you want to run the pipeline on a schedule, [create a schedule](https://docs.cloud.google.com/workflows/docs/schedule-workflow) by using Cloud Scheduler. Provide the following information:

     * **Frequency** : a Unix-cron expression that defines the schedule to run the pipeline.
     * **Workflow argument** : the runtime arguments for the connector, as described in the previous step.
     * **Service account** : the service account. The service account manages the scheduler.



###  gcloud 

  1. Save the following workload definition as a YAML file:
         
         main:
           params: [args]
           steps:
             - init:
                 assign:
                 - WORKFLOW_ID: ${"metadataworkflow-" + sys.get_env("GOOGLE_CLOUD_WORKFLOW_EXECUTION_ID")}
                 - NETWORK_URI: ${default(map.get(args, "NETWORK_URI"), "")}
                 - SUBNETWORK_URI: ${default(map.get(args, "SUBNETWORK_URI"), "")}
                 - NETWORK_TAGS: ${default(map.get(args, "NETWORK_TAGS"), [])}
         
             - check_networking:
                 switch:
                   - condition: ${NETWORK_URI != "" and SUBNETWORK_URI != ""}
                     raise: "Error: cannot set both network_uri and subnetwork_uri. Please select one."
                   - condition: ${NETWORK_URI == "" and SUBNETWORK_URI == ""}
                     steps:
                      - submit_extract_job_with_default_network_uri:
                           assign:
                             - NETWORK_TYPE: "networkUri"
                             - NETWORKING: ${"projects/" + args.TARGET_PROJECT_ID + "/global/networks/default"}  
                   - condition: ${NETWORK_URI != ""}
                     steps:
                       - submit_extract_job_with_network_uri:
                           assign:
                             - NETWORKING: ${NETWORK_URI}
                             - NETWORK_TYPE: "networkUri"
                   - condition: ${SUBNETWORK_URI != ""}
                     steps:
                       - submit_extract_job_with_subnetwork_uri:
                           assign:
                             - NETWORKING: ${SUBNETWORK_URI}
                             - NETWORK_TYPE: "subnetworkUri"
                 next: check_create_target_entry_group
         
             - check_create_target_entry_group:
                 switch:
                   - condition: ${args.CREATE_TARGET_ENTRY_GROUP == true}
                     next: create_target_entry_group
                   - condition: ${args.CREATE_TARGET_ENTRY_GROUP == false}
                     next: prepare_pyspark_job_body
         
             - create_target_entry_group:
                 call: http.post
                 args:
                   url: ${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/entryGroups?entry_group_id=" + args.TARGET_ENTRY_GROUP_ID}
                   auth:
                     type: OAuth2
                     scopes: "https://www.googleapis.com/auth/cloud-platform"
                 next: prepare_pyspark_job_body
         
             - prepare_pyspark_job_body:
                 assign:
                   - pyspark_batch_body:
                       mainPythonFileUri: file:///main.py
                       args:
                         - ${"--target_project_id=" + args.TARGET_PROJECT_ID}
                         - ${"--target_location_id=" + args.CLOUD_REGION}
                         - ${"--target_entry_group_id=" + args.TARGET_ENTRY_GROUP_ID}
                         - ${"--output_bucket=" + args.CLOUD_STORAGE_BUCKET_ID}
                         - ${"--output_folder=" + WORKFLOW_ID}
                         - ${args.ADDITIONAL_CONNECTOR_ARGS}
                 next: add_jar_file_uri_if_present
         
             - add_jar_file_uri_if_present:
                 switch:
                   - condition: ${args.JAR_FILE_URI != "" and args.JAR_FILE_URI != null}
                     assign:
                       - pyspark_batch_body.jarFileUris : ${args.JAR_FILE_URI}
                 next: generate_extract_job_link
         
             - generate_extract_job_link:
                 call: sys.log
                 args:
                     data: ${"https://console.cloud.google.com/dataproc/batches/" + args.CLOUD_REGION + "/" + WORKFLOW_ID + "/monitoring?project=" + args.TARGET_PROJECT_ID}
                     severity: "INFO"
                 next: submit_pyspark_extract_job
         
             - submit_pyspark_extract_job:
                 call: http.post
                 args:
                   url: ${"https://dataproc.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/batches"}
                   auth:
                     type: OAuth2
                     scopes: "https://www.googleapis.com/auth/cloud-platform"
                   headers:
                     Content-Type: "application/json"
                   query:
                     batchId: ${WORKFLOW_ID}
                   body:
                     pysparkBatch: ${pyspark_batch_body}
                     runtimeConfig:
                         containerImage: ${args.CUSTOM_CONTAINER_IMAGE}
                     environmentConfig:
                         executionConfig:
                             serviceAccount: ${args.SERVICE_ACCOUNT}
                             stagingBucket: ${args.CLOUD_STORAGE_BUCKET_ID}
                             ${NETWORK_TYPE}: ${NETWORKING}
                             networkTags: ${NETWORK_TAGS}
                 result: RESPONSE_MESSAGE
                 next: check_pyspark_extract_job
         
             - check_pyspark_extract_job:
                 call: http.get
                 args:
                   url: ${"https://dataproc.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/batches/" + WORKFLOW_ID}
                   auth:
                     type: OAuth2
                     scopes: "https://www.googleapis.com/auth/cloud-platform"
                 result: PYSPARK_EXTRACT_JOB_STATUS
                 next: check_pyspark_extract_job_done
         
             - check_pyspark_extract_job_done:
                 switch:
                   - condition: ${PYSPARK_EXTRACT_JOB_STATUS.body.state == "SUCCEEDED"}
                     next: generate_import_logs_link
                   - condition: ${PYSPARK_EXTRACT_JOB_STATUS.body.state == "CANCELLED"}
                     raise: ${PYSPARK_EXTRACT_JOB_STATUS}
                   - condition: ${PYSPARK_EXTRACT_JOB_STATUS.body.state == "FAILED"}
                     raise: ${PYSPARK_EXTRACT_JOB_STATUS}
                 next: pyspark_extract_job_wait
         
             - pyspark_extract_job_wait:
                 call: sys.sleep
                 args:
                   seconds: 30
                 next: check_pyspark_extract_job
         
             - generate_import_logs_link:
                 call: sys.log
                 args:
                     data: ${"https://console.cloud.google.com/logs/query?project=" + args.TARGET_PROJECT_ID + "&query=resource.type%3D%22dataplex.googleapis.com%2FMetadataJob%22+AND+resource.labels.location%3D%22" + args.CLOUD_REGION + "%22+AND+resource.labels.metadata_job_id%3D%22" + WORKFLOW_ID + "%22"}
                     severity: "INFO"
                 next: submit_import_job
         
             - submit_import_job:
                 call: http.post
                 args:
                   url: ${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/metadataJobs?metadata_job_id=" + WORKFLOW_ID}
                   auth:
                     type: OAuth2
                     scopes: "https://www.googleapis.com/auth/cloud-platform"
                   body:
                     type: IMPORT
                     import_spec:
                       source_storage_uri: ${"gs://" + args.CLOUD_STORAGE_BUCKET_ID + "/" + WORKFLOW_ID + "/"}
                       entry_sync_mode: FULL
                       aspect_sync_mode: INCREMENTAL
                       log_level: ${default(map.get(args, "IMPORT_JOB_LOG_LEVEL"), "INFO")}
                       scope:
                         entry_groups: 
                           - ${"projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/entryGroups/" + args.TARGET_ENTRY_GROUP_ID}
                         entry_types: ${args.IMPORT_JOB_SCOPE_ENTRY_TYPES}
                         aspect_types: ${args.IMPORT_JOB_SCOPE_ASPECT_TYPES}
                 result: IMPORT_JOB_RESPONSE
                 next: get_job_start_time
         
             - get_job_start_time:
                 assign:
                   - importJobStartTime: ${sys.now()}
                 next: import_job_startup_wait
         
             - import_job_startup_wait:
                 call: sys.sleep
                 args:
                   seconds: 30
                 next: initial_get_import_job
         
             - initial_get_import_job:
                 call: http.get
                 args:
                   url: ${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/metadataJobs/" + WORKFLOW_ID}
                   auth:
                     type: OAuth2
                     scopes: "https://www.googleapis.com/auth/cloud-platform"
                 result: IMPORT_JOB_STATUS
                 next: check_import_job_status_available
         
             - check_import_job_status_available:
                 switch:
                   - condition: ${sys.now() - importJobStartTime > 300}  # 5 minutes = 300 seconds
                     next: kill_import_job
                   - condition: ${"status" in IMPORT_JOB_STATUS.body}
                     next: check_import_job_done
                 next: import_job_status_wait
         
             - import_job_status_wait:
                 call: sys.sleep
                 args:
                   seconds: 30
                 next: check_import_job_status_available
         
             - check_import_job_done:
                 switch:
                   - condition: ${IMPORT_JOB_STATUS.body.status.state == "SUCCEEDED"}
                     next: the_end
                   - condition: ${IMPORT_JOB_STATUS.body.status.state == "CANCELLED"}
                     raise: ${IMPORT_JOB_STATUS}
                   - condition: ${IMPORT_JOB_STATUS.body.status.state == "SUCCEEDED_WITH_ERRORS"}
                     raise: ${IMPORT_JOB_STATUS}
                   - condition: ${IMPORT_JOB_STATUS.body.status.state == "FAILED"}
                     raise: ${IMPORT_JOB_STATUS}
                   - condition: ${sys.now() - importJobStartTime > 43200}  # 12 hours = 43200 seconds
                     next: kill_import_job
                 next: import_job_wait
         
             - get_import_job:
                 call: http.get
                 args:
                   url: ${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/metadataJobs/" + WORKFLOW_ID}
                   auth:
                     type: OAuth2
                     scopes: "https://www.googleapis.com/auth/cloud-platform"
                 result: IMPORT_JOB_STATUS
                 next: check_import_job_done
         
             - import_job_wait:
                 call: sys.sleep
                 args:
                   seconds: 30
                 next: get_import_job
         
             - kill_import_job:
                 call: http.post
                 args:
                   url: ${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/metadataJobs/" + WORKFLOW_ID + ":cancel"}
                   auth:
                     type: OAuth2
                     scopes: "https://www.googleapis.com/auth/cloud-platform"
                 next: get_killed_import_job
         
             - get_killed_import_job:
                 call: http.get
                 args:
                   url: ${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/metadataJobs/" + WORKFLOW_ID}
                   auth:
                     type: OAuth2
                     scopes: "https://www.googleapis.com/auth/cloud-platform"
                 result: KILLED_IMPORT_JOB_STATUS
                 next: killed
         
             - killed:
                 raise: ${KILLED_IMPORT_JOB_STATUS}
         
             - the_end:
                 return: ${IMPORT_JOB_STATUS}
         

  2. Define Bash variables, [create the workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow), and optionally [create a schedule](https://docs.cloud.google.com/workflows/docs/schedule-workflow) for running the pipeline:
         
         # Define Bash variables (replace with your actual values)
         project_id="PROJECT_ID"
         region="LOCATION_ID"
         service_account="SERVICE_ACCOUNT_ID"
         workflow_source="WORKFLOW_DEFINITION_FILE.yaml"
         workflow_name="WORKFLOW_NAME"
         workflow_args='WORKFLOW_ARGUMENTS'
         
         # Create Workflows resource
         gcloud workflows deploy ${workflow_name} \
           --project=${project_id} \
           --location=${region} \
           --source=${workflow_source} \
           --service-account=${service_account}
         
         # Create Cloud Scheduler job
         gcloud scheduler jobs create http ${workflow_name}-scheduler \
           --project=${project_id} \
           --location=${region} \
           --schedule="CRON_SCHEDULE_EXPRESSION" \
           --time-zone="UTC" \
           --uri="https://workflowexecutions.googleapis.com/v1/projects/${project_id}/locations/${region}/workflows/${workflow_name}/executions" \
           --http-method="POST" \
           --oauth-service-account-email=${service_account} \
           --headers="Content-Type=application/json" \
           --message-body='{"argument": ${workflow_args}}'
         

Replace the following:

     * `PROJECT_ID`: the name of the target Google Cloud project to import the metadata into. 
     * `LOCATION_ID`: the target Google Cloud location where the Managed Service for Apache Spark and metadata import jobs will run, and metadata will be imported into. 
     * `SERVICE_ACCOUNT_ID`: the service account that you configured in the Required roles section of this document. 
     * `WORKFLOW_DEFINITION_FILE`: the path to the workflow definition YAML file.
     * `WORKFLOW_NAME`: the name of the workflow.
     * `WORKFLOW_ARGUMENTS`: the runtime arguments to pass to the connector. The arguments are in JSON format:
           
           {
               "TARGET_PROJECT_ID": "PROJECT_ID",
               "CLOUD_REGION": "LOCATION_ID",
               "TARGET_ENTRY_GROUP_ID": "ENTRY_GROUP_ID",
               "CREATE_TARGET_ENTRY_GROUP": CREATE_ENTRY_GROUP_BOOLEAN,
               "CLOUD_STORAGE_BUCKET_ID": "BUCKET_ID",
               "SERVICE_ACCOUNT": "SERVICE_ACCOUNT_ID",
               "ADDITIONAL_CONNECTOR_ARGS": [ADDITIONAL_CONNECTOR_ARGUMENTS],
               "CUSTOM_CONTAINER_IMAGE": "CONTAINER_IMAGE",
               "IMPORT_JOB_SCOPE_ENTRY_TYPES": [ENTRY_TYPES],
               "IMPORT_JOB_SCOPE_ASPECT_TYPES": [ASPECT_TYPES],
               "IMPORT_JOB_LOG_LEVEL": "INFO",
               "JAR_FILE_URI": "",
               "NETWORK_TAGS": [],
               "NETWORK_URI": "",
               "SUBNETWORK_URI": ""
            }
           

For Cloud Scheduler, the double quotation marks inside the quoted string are escaped using backslashes (\\). For example: `--message-body="{\"argument\": \"{\\\"key\\\": \\\"value\\\"}\"}"`.

Replace the following:

       * `ENTRY_GROUP_ID`: the ID of the entry group to import metadata into. The entry group ID can contain lowercase letters, numbers, and hyphens. 

The full resource name of this entry group is `projects/PROJECT_ID/locations/LOCATION_ID/entryGroups/ENTRY_GROUP_ID`. 

       * `CREATE_ENTRY_GROUP_BOOLEAN`: if you want the pipeline to create the entry group if it doesn't already exist in your project, set this value to `true`. 
       * `BUCKET_ID`: the name of the Cloud Storage bucket to store the metadata import file that is generated by the connector. Each workflow execution creates a new folder. 
       * `ADDITIONAL_CONNECTOR_ARGUMENTS`: a list of additional arguments to pass to the connector. For examples, see [Develop a custom connector for metadata import](https://docs.cloud.google.com/knowledge-catalog/docs/develop-custom-connector). 
       * `CONTAINER_IMAGE`: the custom container image of the connector hosted in Artifact Registry. 
       * `ENTRY_TYPES`: a list of entry types that are in scope for import, in the format `projects/PROJECT_ID/locations/LOCATION_ID/entryTypes/ENTRY_TYPE_ID`. The `LOCATION_ID` must be either the same Google Cloud location that you import metadata into, or `global`. 
       * `ASPECT_TYPES`: a list of aspect types that are in scope for import, in the format `projects/PROJECT_ID/locations/LOCATION_ID/aspectTypes/ASPECT_TYPE_ID`. The `LOCATION_ID` must be either the same Google Cloud location that you import metadata into, or `global`. 
       * Optional: for the `NETWORK_TAGS` argument, provide a list of network tags. 
       * Optional: For the `NETWORK_URI` argument, provide the URI of the VPC network that connects to the data source. If you provide a network, omit the subnetwork argument. 
       * Optional: For the `SUBNETWORK_URI` argument, provide the URI of the subnetwork that connects to the data source. If you provide a subnet, omit the network argument. 
     * `CRON_SCHEDULE_EXPRESSION`: a cron expression that defines the schedule to run the pipeline. For example, to run the schedule at midnight every day, use the expression `0 0 * * *`. 

  3. To run the pipeline on demand, [execute the workflow](https://docs.cloud.google.com/workflows/docs/executing-workflow):
         
         workflow_name="WORKFLOW_NAME"
         workflow_args='WORKFLOW_ARGUMENTS'
         
         gcloud workflows run "${workflow_name}" --project=${project_id} --location=${location} --data '${workflow_args}'
         

The workflow arguments are in JSON format, but not escaped.

Depending on the amount of metadata that you import, the workflow might take several minutes or longer to run. For more information about how to view the progress, see [Access workflow execution results](https://docs.cloud.google.com/workflows/docs/access-execution-results).

After the pipeline has finished running, you can [search for the imported metadata in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets).




### Terraform

  1. Clone the [`cloud-dataplex` repository](https://github.com/GoogleCloudPlatform/cloud-dataplex).

The repository includes the following Terraform files:

     * [`main.tf`](https://github.com/GoogleCloudPlatform/cloud-dataplex/blob/main/managed-connectivity/cloud-workflows/byo-connector/terraform/main.tf): defines the Google Cloud resources to create.
     * [`variables.tf`](https://github.com/GoogleCloudPlatform/cloud-dataplex/blob/main/managed-connectivity/cloud-workflows/byo-connector/terraform/variables.tf): declares the variables.
     * [`byo-connector.tfvars`](https://github.com/GoogleCloudPlatform/cloud-dataplex/blob/main/managed-connectivity/cloud-workflows/byo-connector/terraform/byo-connector.tfvars): defines the variables for your managed connectivity pipeline.
  2. Edit the `.tfvars` file to replace the placeholders with the information for your connector.
         
         project_id                      = "PROJECT_ID"
         region                          = "LOCATION_ID"
         service_account                 = "SERVICE_ACCOUNT_ID"
         cron_schedule                   = "CRON_SCHEDULE_EXPRESSION"
         workflow_args                   = {"TARGET_PROJECT_ID": "PROJECT_ID", "CLOUD_REGION": "LOCATION_ID", "TARGET_ENTRY_GROUP_ID": "ENTRY_GROUP_ID", "CREATE_TARGET_ENTRY_GROUP": CREATE_ENTRY_GROUP_BOOLEAN, "CLOUD_STORAGE_BUCKET_ID": "BUCKET_ID", "SERVICE_ACCOUNT": "SERVICE_ACCOUNT_ID", "ADDITIONAL_CONNECTOR_ARGS": [ADDITIONAL_CONNECTOR_ARGUMENTS], "CUSTOM_CONTAINER_IMAGE": "CONTAINER_IMAGE", "IMPORT_JOB_SCOPE_ENTRY_TYPES": [ENTRY_TYPES], "IMPORT_JOB_SCOPE_ASPECT_TYPES": [ASPECT_TYPES], "IMPORT_JOB_LOG_LEVEL": "INFO", "NETWORK_TAGS": [], "NETWORK_URI": "", "SUBNETWORK_URI": ""}
         
         
         workflow_source                 = <<EOF
         main:
           params: [args]
           steps:
             - init:
                 assign:
                 - WORKFLOW_ID: $${"metadataworkflow-" + sys.get_env("GOOGLE_CLOUD_WORKFLOW_EXECUTION_ID")}
                 - NETWORK_URI: $${default(map.get(args, "NETWORK_URI"), "")}
                 - SUBNETWORK_URI: $${default(map.get(args, "SUBNETWORK_URI"), "")}
                 - NETWORK_TAGS: $${default(map.get(args, "NETWORK_TAGS"), [])}
         
             - check_networking:
                 switch:
                   - condition: $${NETWORK_URI != "" and SUBNETWORK_URI != ""}
                     raise: "Error: cannot set both network_uri and subnetwork_uri. Please select one."
                   - condition: $${NETWORK_URI != ""}
                     steps:
                       - submit_extract_job_with_network_uri:
                           assign:
                             - NETWORKING: $${NETWORK_URI}
                             - NETWORK_TYPE: "networkUri"
                   - condition: $${SUBNETWORK_URI != ""}
                     steps:
                       - submit_extract_job_with_subnetwork_uri:
                           assign:
                             - NETWORKING: $${SUBNETWORK_URI}
                             - NETWORK_TYPE: "subnetworkUri"
                 next: set_default_networking
         
             - set_default_networking:
                 assign:
                   - NETWORK_TYPE: "networkUri"
                   - NETWORKING: $${"projects/" + args.TARGET_PROJECT_ID + "/global/networks/default"}
                 next: check_create_target_entry_group
         
             - check_create_target_entry_group:
                 switch:
                   - condition: $${args.CREATE_TARGET_ENTRY_GROUP == true}
                     next: create_target_entry_group
                   - condition: $${args.CREATE_TARGET_ENTRY_GROUP == false}
                     next: generate_extract_job_link
         
             - create_target_entry_group:
                 call: http.post
                 args:
                   url: $${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/entryGroups?entry_group_id=" + args.TARGET_ENTRY_GROUP_ID}
                   auth:
                     type: OAuth2
                     scopes: "https://www.googleapis.com/auth/cloud-platform"
                 next: generate_extract_job_link
         
             - generate_extract_job_link:
                 call: sys.log
                 args:
                     data: $${"https://console.cloud.google.com/dataproc/batches/" + args.CLOUD_REGION + "/" + WORKFLOW_ID + "/monitoring?project=" + args.TARGET_PROJECT_ID}
                     severity: "INFO"
                 next: submit_pyspark_extract_job
         
             - submit_pyspark_extract_job:
                 call: http.post
                 args:
                   url: $${"https://dataproc.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/batches"}
                   auth:
                     type: OAuth2
                     scopes: "https://www.googleapis.com/auth/cloud-platform"
                   headers:
                     Content-Type: "application/json"
                   query:
                     batchId: $${WORKFLOW_ID}
                   body:
                     pysparkBatch:
                       mainPythonFileUri: file:///main.py
                       args:
                         - $${"--target_project_id=" + args.TARGET_PROJECT_ID}
                         - $${"--target_location_id=" + args.CLOUD_REGION}
                         - $${"--target_entry_group_id=" + args.TARGET_ENTRY_GROUP_ID}
                         - $${"--output_bucket=" + args.CLOUD_STORAGE_BUCKET_ID}
                         - $${"--output_folder=" + WORKFLOW_ID}
                         - $${args.ADDITIONAL_CONNECTOR_ARGS}
                     runtimeConfig:
                         containerImage: $${args.CUSTOM_CONTAINER_IMAGE}
                     environmentConfig:
                         executionConfig:
                             serviceAccount: $${args.SERVICE_ACCOUNT}
                             stagingBucket: $${args.CLOUD_STORAGE_BUCKET_ID}
                             $${NETWORK_TYPE}: $${NETWORKING}
                             networkTags: $${NETWORK_TAGS}
                 result: RESPONSE_MESSAGE
                 next: check_pyspark_extract_job
         
             - check_pyspark_extract_job:
                 call: http.get
                 args:
                   url: $${"https://dataproc.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/batches/" + WORKFLOW_ID}
                   auth:
                     type: OAuth2
                     scopes: "https://www.googleapis.com/auth/cloud-platform"
                 result: PYSPARK_EXTRACT_JOB_STATUS
                 next: check_pyspark_extract_job_done
         
             - check_pyspark_extract_job_done:
                 switch:
                   - condition: $${PYSPARK_EXTRACT_JOB_STATUS.body.state == "SUCCEEDED"}
                     next: generate_import_logs_link
                   - condition: $${PYSPARK_EXTRACT_JOB_STATUS.body.state == "CANCELLED"}
                     raise: $${PYSPARK_EXTRACT_JOB_STATUS}
                   - condition: $${PYSPARK_EXTRACT_JOB_STATUS.body.state == "FAILED"}
                     raise: $${PYSPARK_EXTRACT_JOB_STATUS}
                 next: pyspark_extract_job_wait
         
             - pyspark_extract_job_wait:
                 call: sys.sleep
                 args:
                   seconds: 30
                 next: check_pyspark_extract_job
         
             - generate_import_logs_link:
                 call: sys.log
                 args:
                     data: $${"https://console.cloud.google.com/logs/query?project=" + args.TARGET_PROJECT_ID + "&query=resource.type%3D%22dataplex.googleapis.com%2FMetadataJob%22+AND+resource.labels.location%3D%22" + args.CLOUD_REGION + "%22+AND+resource.labels.metadata_job_id%3D%22" + WORKFLOW_ID + "%22"}
                     severity: "INFO"
                 next: submit_import_job
         
             - submit_import_job:
                 call: http.post
                 args:
                   url: $${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/metadataJobs?metadata_job_id=" + WORKFLOW_ID}
                   auth:
                     type: OAuth2
                     scopes: "https://www.googleapis.com/auth/cloud-platform"
                   body:
                     type: IMPORT
                     import_spec:
                       source_storage_uri: $${"gs://" + args.CLOUD_STORAGE_BUCKET_ID + "/" + WORKFLOW_ID + "/"}
                       entry_sync_mode: FULL
                       aspect_sync_mode: INCREMENTAL
                       log_level: $${default(map.get(args, "IMPORT_JOB_LOG_LEVEL"), "INFO")}
                       scope:
                         entry_groups: 
                           - $${"projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/entryGroups/" + args.TARGET_ENTRY_GROUP_ID}
                         entry_types: $${args.IMPORT_JOB_SCOPE_ENTRY_TYPES}
                         aspect_types: $${args.IMPORT_JOB_SCOPE_ASPECT_TYPES}
                 result: IMPORT_JOB_RESPONSE
                 next: get_job_start_time
         
             - get_job_start_time:
                 assign:
                   - importJobStartTime: $${sys.now()}
                 next: import_job_startup_wait
         
             - import_job_startup_wait:
                 call: sys.sleep
                 args:
                   seconds: 30
                 next: initial_get_import_job
         
             - initial_get_import_job:
                 call: http.get
                 args:
                   url: $${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/metadataJobs/" + WORKFLOW_ID}
                   auth:
                     type: OAuth2
                     scopes: "https://www.googleapis.com/auth/cloud-platform"
                 result: IMPORT_JOB_STATUS
                 next: check_import_job_status_available
         
             - check_import_job_status_available:
                 switch:
                   - condition: $${sys.now() - importJobStartTime > 300}  # 5 minutes = 300 seconds
                     next: kill_import_job
                   - condition: $${"status" in IMPORT_JOB_STATUS.body}
                     next: check_import_job_done
                 next: import_job_status_wait
         
             - import_job_status_wait:
                 call: sys.sleep
                 args:
                   seconds: 30
                 next: check_import_job_status_available
         
             - check_import_job_done:
                 switch:
                   - condition: $${IMPORT_JOB_STATUS.body.status.state == "SUCCEEDED"}
                     next: the_end
                   - condition: $${IMPORT_JOB_STATUS.body.status.state == "CANCELLED"}
                     raise: $${IMPORT_JOB_STATUS}
                   - condition: $${IMPORT_JOB_STATUS.body.status.state == "SUCCEEDED_WITH_ERRORS"}
                     raise: $${IMPORT_JOB_STATUS}
                   - condition: $${IMPORT_JOB_STATUS.body.status.state == "FAILED"}
                     raise: $${IMPORT_JOB_STATUS}
                   - condition: $${sys.now() - importJobStartTime > 43200}  # 12 hours = 43200 seconds
                     next: kill_import_job
                 next: import_job_wait
         
             - get_import_job:
                 call: http.get
                 args:
                   url: $${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/metadataJobs/" + WORKFLOW_ID}
                   auth:
                     type: OAuth2
                     scopes: "https://www.googleapis.com/auth/cloud-platform"
                 result: IMPORT_JOB_STATUS
                 next: check_import_job_done
         
             - import_job_wait:
                 call: sys.sleep
                 args:
                   seconds: 30
                 next: get_import_job
         
             - kill_import_job:
                 call: http.post
                 args:
                   url: $${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/metadataJobs/" + WORKFLOW_ID + ":cancel"}
                   auth:
                     type: OAuth2
                     scopes: "https://www.googleapis.com/auth/cloud-platform"
                 next: get_killed_import_job
         
             - get_killed_import_job:
                 call: http.get
                 args:
                   url: $${"https://dataplex.googleapis.com/v1/projects/" + args.TARGET_PROJECT_ID + "/locations/" + args.CLOUD_REGION + "/metadataJobs/" + WORKFLOW_ID}
                   auth:
                     type: OAuth2
                     scopes: "https://www.googleapis.com/auth/cloud-platform"
                 result: KILLED_IMPORT_JOB_STATUS
                 next: killed
         
             - killed:
                 raise: $${KILLED_IMPORT_JOB_STATUS}
         
             - the_end:
                 return: $${IMPORT_JOB_STATUS}
         EOF
         

Replace the following:

     * `PROJECT_ID`: the name of the target Google Cloud project to import the metadata into. 
     * `LOCATION_ID`: the target Google Cloud location where the Managed Service for Apache Spark and metadata import jobs will run, and metadata will be imported into. 
     * `SERVICE_ACCOUNT_ID`: the service account that you configured in the Required roles section of this document. 
     * `CRON_SCHEDULE_EXPRESSION`: a cron expression that defines the schedule to run the pipeline. For example, to run the schedule at midnight every day, use the expression `0 0 * * *`. 
     * `ENTRY_GROUP_ID`: the ID of the entry group to import metadata into. The entry group ID can contain lowercase letters, numbers, and hyphens. 

The full resource name of this entry group is `projects/PROJECT_ID/locations/LOCATION_ID/entryGroups/ENTRY_GROUP_ID`. 

     * `CREATE_ENTRY_GROUP_BOOLEAN`: if you want the pipeline to create the entry group if it doesn't already exist in your project, set this value to `true`. 
     * `BUCKET_ID`: the name of the Cloud Storage bucket to store the metadata import file that is generated by the connector. Each workflow execution creates a new folder. 
     * `ADDITIONAL_CONNECTOR_ARGUMENTS`: a list of additional arguments to pass to the connector. For examples, see [Develop a custom connector for metadata import](https://docs.cloud.google.com/knowledge-catalog/docs/develop-custom-connector). Enclose each argument in double quotation marks, and separate the arguments with commas.
     * `CONTAINER_IMAGE`: the custom container image of the connector hosted in Artifact Registry. 
     * `ENTRY_TYPES`: a list of entry types that are in scope for import, in the format `projects/PROJECT_ID/locations/LOCATION_ID/entryTypes/ENTRY_TYPE_ID`. The `LOCATION_ID` must be either the same Google Cloud location that you import metadata into, or `global`. 
     * `ASPECT_TYPES`: a list of aspect types that are in scope for import, in the format `projects/PROJECT_ID/locations/LOCATION_ID/aspectTypes/ASPECT_TYPE_ID`. The `LOCATION_ID` must be either the same Google Cloud location that you import metadata into, or `global`. 
     * Optional: for the `NETWORK_TAGS` argument, provide a list of network tags. 
     * Optional: For the `NETWORK_URI` argument, provide the URI of the VPC network that connects to the data source. If you provide a network, omit the subnetwork argument. 
     * Optional: For the `SUBNETWORK_URI` argument, provide the URI of the subnetwork that connects to the data source. If you provide a subnet, omit the network argument. 
  3. Initialize Terraform:
         
         terraform init
         

  4. Validate Terraform with your `.tfvars` file:
         
         terraform plan --var-file=CONNECTOR_VARIABLES_FILE.tfvars
         

Replace `CONNECTOR_VARIABLES_FILE` with the name of your variable definitions file.

  5. Deploy Terraform with your `.tfvars` file:
         
         terraform apply --var-file=CONNECTOR_VARIABLES_FILE.tfvars
         

Terraform creates a workflow and a Cloud Scheduler job in the specified project. Workflows runs the pipeline at the schedule that you specify.

Depending on the amount of metadata that you import, the workflow might take several minutes or longer to run. For more information about how to view the progress, see [Access workflow execution results](https://docs.cloud.google.com/workflows/docs/access-execution-results).

After the pipeline has finished running, you can [search for the imported metadata in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets).




## View job logs

Use Cloud Logging to view logs for a managed connectivity pipeline. The log payload includes a link to the logs for the Managed Service for Apache Spark batch job and the metadata import job, as relevant. For more information, see [View workflow logs](https://docs.cloud.google.com/workflows/docs/log-workflow#viewing-logs).

## Troubleshooting

Use the following troubleshooting suggestions:

  * Configure the import job log level for the metadata job to [use debug-level logging](https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata#troubleshoot-logs) instead of info-level logging.
  * Review the logs for the Managed Service for Apache Spark batch job (for connector runs) and the metadata import job. For more information, see [Query Managed Service for Apache Spark logs](https://docs.cloud.google.com/dataproc-serverless/docs/guides/monitor-troubleshoot-batches#query-dataproc-serverless-for-spark-logs) and [Query metadata job logs](https://docs.cloud.google.com/knowledge-catalog/docs/logging#access-metadata-job-logs).
  * If an entry can't be imported using the pipeline and the error message doesn't provide enough information, try creating a custom entry with the same details, in a test entry group. For more information, see [Create a custom entry](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#create-custom-entry).



## What's next

  * [About metadata management in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview)
  * [Develop a custom connector for metadata import](https://docs.cloud.google.com/knowledge-catalog/docs/develop-custom-connector)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
