---
url: https://docs.cloud.google.com/logging/docs/api/v2/resource-list/
title: Monitored resources and services \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:16.651874+00:00
---

# Monitored resources and services  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/api/v2/resource-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Reference ](https://docs.cloud.google.com/logging/docs/apis)



Send feedback 

#  Monitored resources and services Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about the Google Cloud resource types and services that Cloud Logging uses. This information can help you understand [Google Cloud platform logs](https://docs.cloud.google.com/logging/docs/api/platform-logs), which are service-specific logs that can help you debug and troubleshoot issues as well as understand the Google Cloud services you're using.

If you use BindPlane to write your on-premise and hybrid cloud logs, then you can find these logs under the resource type `generic_node`.

## Monitored resource types

The following table lists all the Cloud Logging monitored resource types, their labels, and descriptive information. The information shown for each monitored resource type is defined in the [`MonitoredResourceDescriptor` object](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/monitoredResourceDescriptors/list#MonitoredResourceDescriptor). This table is regenerated frequently, and the timestamp is shown at the end of the table.

When writing log entries, `MonitoredResourceDescriptor.type` has to be one of the following types. You can't create your own monitored resource types; these are created by Google Cloud. For non-Google Cloud resources, we recommend you can use the generic types `generic_node` or `generic_task`.

The list of monitored resource types in Logging might not match [list of monitored resource types in Monitoring](https://docs.cloud.google.com/monitoring/api/resources).

Resource type  
Display name | Description  
Labels  
---|---  
`abuseevent.googleapis.com/Location`  
Abuse Event  |  A GCP resource container associated with an abuse event.   
`resource_container`: The GCP resource identifier associated with the abuse event.   
`location`: The location where the abuse event was observed.   
`aiplatform.googleapis.com/DeploymentResourcePool`  
Vertex AI Deployment Resource Pool  |  A Vertex AI Deployment Resource Pool.   
`resource_container`: The identifier of the GCP Project owning the Deployment Resource Pool.   
`location`: The region in which the service is running.   
`deployment_resource_pool_id`: The ID of the Deployment Resource Pool.   
`aiplatform.googleapis.com/Endpoint`  
Vertex AI Endpoint  |  A Vertex AI API Endpoint where Models are deployed into it.   
`resource_container`: The identifier of the GCP Project owning the Endpoint.   
`location`: The region in which the service is running.   
`endpoint_id`: The ID of the Endpoint.   
`aiplatform.googleapis.com/Featurestore`  
Vertex AI Feature Store  |  A Vertex AI Feature Store.   
`resource_container`: The identifier of the GCP Project owning the Featurestore.   
`location`: The region in which the service is running.   
`featurestore_id`: The ID of the Featurestore.   
`aiplatform.googleapis.com/Index`  
Matching Engine Index  |  An Index built through the cloud Matching Engine service.   
`resource_container`: The identifier of the GCP Project owning the Index.   
`location`: The region in which the service is running.   
`index_id`: The ID of the Index.   
`aiplatform.googleapis.com/IndexEndpoint`  
Matching Engine Index Endpoint  |  An Endpoint to which Matching Engine Indexes are deployed.   
`resource_container`: The identifier of the GCP Project owning the Index.   
`location`: The region in which the service is running.   
`index_endpoint_id`: The ID of the index endpoint.   
`aiplatform.googleapis.com/ModelMonitor`  
Vertex AI Model Monitor  |  A Vertex AI Model Monitor.   
`resource_container`: The identifier of the GCP Project owning the Model Monitor.   
`location`: The region in which the service is running.   
`model_monitor_id`: The identifier of the Model Monitor.   
`aiplatform.googleapis.com/OnlineEvaluator`  
Vertex AI Online Evaluator  |  A Vertex AI Online Evaluator.   
`resource_container`: The resource container of the Online Evaluator.   
`location`: The location of the Online Evaluator.   
`online_evaluator_id`: The ID of the Online Evaluator resource.   
`aiplatform.googleapis.com/PipelineJob`  
Vertex Pipelines Job  |  A Vertex Pipelines Job.   
`resource_container`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The region in which the service is running.   
`pipeline_job_id`: The ID of the PipelineJob.   
`aiplatform.googleapis.com/PublisherModel`  
Vertex AI Model Garden Publisher Model  |  A Vertex AI Model Garden Publisher Model.   
`resource_container`: The identifier of the GCP Project owning the Endpoint.   
`location`: The region in which the service is running.   
`publisher`: The publisher of the model.   
`model_user_id`: The resource ID of the PublisherModel.   
`model_version_id`: The version ID of the PublisherModel.   
`aiplatform.googleapis.com/ReasoningEngine`  
Vertex AI Reasoning Engine  |  A Vertex AI Reasoning Engine.   
`resource_container`: The identifier of the GCP Project owning the ReasoningEngine.   
`location`: The region in which the service is running.   
`reasoning_engine_id`: The numeric ID of the Reasoning Engine instance.   
`aiplatform.googleapis.com/ServerlessRayJob`  
Vertex AI Serverless Ray Job  |  A Vertex AI Serverless Ray Job.   
`resource_container`: The identifier of the GCP Project owning the Serverless Ray Job.   
`location`: The region in which the service is running.   
`job_id`: The ID of the Serverless Ray Job.   
`alloydb.googleapis.com/Cluster`  
AlloyDB cluster  |  Monitored resource representing an AlloyDB cluster.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud region in which the AlloyDB cluster is running.   
`cluster_id`: AlloyDB cluster identifier.   
`alloydb.googleapis.com/Instance`  
AlloyDB instance  |  Monitored resource representing an AlloyDB instance.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud region in which the AlloyDB instance is running.   
`cluster_id`: AlloyDB cluster identifier.   
`instance_id`: AlloyDB instance identifier.   
`anthos_l4lb`  
Anthos L4LB  |  An Anthos L4 load balancer instance.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The GCP region where to store metrics.   
`kind`: The kind of the load balancer.   
`group_name`: The name of the load balancer group.   
`hostname`: The hostname of the instance running LB.   
`api`  
Produced API  |  An API provided by the producer.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`service`: The API service name, such as "cloudsql.googleapis.com".   
`method`: The API method, such as "disks.list".   
`version`: The API version, such as "v1".   
`location`: The service specific notion of location. This can be the name of a zone, region, or "global".   
`apigateway.googleapis.com/Gateway`  
API Gateway  |  Fully managed API Gateway.   
`resource_container`: The identifier of the GCP Project owning the Gateway.   
`location`: The region in which the Gateway is running.   
`gateway_id`: The ID of the Gateway.   
`apigee.googleapis.com/Environment`  
Apigee environment  |  Monitored resource for Apigee environment.   
`resource_container`: The GCP project ID that writes to this monitored resource.   
`org`: An organization is a container for all the objects in an Apigee account.   
`env`: An environment is a runtime execution context for the proxies in an organization.   
`location`: Location where the Apigee infrastructure is provisioned.   
`apigee.googleapis.com/Instance`  
Apigee instance  |  Monitored resource for Apigee instance.   
`resource_container`: The GCP project ID that writes to this monitored resource.   
`org`: An organization is a container for all the objects in an Apigee account.   
`location`: Location of the Apigee Instance.   
`instance_id`: Instance ID of the Apigee application.   
`app_script_function`  
Apps Script Function  |  An Apps Script function.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`invocation_type`: The invocation type.   
`function_name`: The function name.   
`artifactregistry.googleapis.com/Project`  
Artifact Registry Project  |  A Cloud project in Artifact Registry.   
`resource_container`: The identifier of the GCP resource container associated with this resource, such as "my_project" or "organizations/5678".   
`location`: Location of resource.   
`artifactregistry.googleapis.com/Repository`  
Artifact Registry Repository  |  A repository in Artifact Registry.   
`resource_container`: The identifier of the GCP resource container associated with this resource, such as "my_project" or "organizations/5678".   
`location`: Location of resource.   
`repository_id`: The identifier of the Artifact Registry repository, such as "my_repository".   
`assistant_action`  
Google Assistant Action  |  An Action in a Google Assistant App.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`version_id`: Stringified version ID of the assistant agent.   
`action_id`: Action ID of the assistant agent.   
`assistant_action_project`  
Google Assistant Action Project  |  A project in a Google Assistant Action.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`audited_resource`  
Audited Resource  |  A Google Cloud resource that produces an audit log.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`service`: The name of the API service generating the audit log.   
`method`: The name of the API method generating the audit log.   
`authztoolkitcontrol.googleapis.com/TargetAssociation`  
AuthzToolkit TargetAssociation  |  A target association resource in AuthzToolkit.   
`resource_container`: The GCP container associated with the target association.   
`location`: The region that contains the target association.   
`target_association_id`: The target association id.   
`autoscaler`  
Autoscaler  |  An autoscaler for a single managed instance group.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The zone or region for the autoscaler.   
`autoscaler_id`: The identifier for the autoscaler.   
`autoscaler_name`: The name of the autoscaler.   
`instance_group_manager_id`: The identifier for the managed instance group scaled by the given autoscaler.   
`instance_group_manager_name`: The name of the managed instance group scaled by the givenautoscaler.   
`aws_alb_load_balancer`  
Amazon ALB Load Balancer  |  A load balancer in Amazon ALB.   
`project_id`: The identifier of the GCP project under which data is stored for the AWS account specified in the aws_account label, such as "my-project".   
`name`: The name of the load balancer.   
`region`: The AWS region for the load balancer. The format of this field is "aws:{region}", where supported values for {region} are listed at <http://docs.aws.amazon.com/general/latest/gr/rande.html>.   
`aws_account`: The AWS account number for the load balancer.   
`aws_cloudfront_distribution`  
Amazon CloudFront CDN  |  A CloudFront content distribution network.   
`project_id`: The identifier of the GCP project under which data is stored for the AWS account specified in the aws_account label, such as "my-project".   
`distribution_id`: The CloudFront distribution identifier assigned by AWS.   
`region`: The AWS region for the CloudFront distribution. The format of this field is "aws:{region}", where supported values for {region} are listed at <http://docs.aws.amazon.com/general/latest/gr/rande.html>.   
`aws_account`: The AWS account number for the CDN.   
`aws_ec2_instance`  
Amazon EC2 Instance  |  A VM instance in Amazon EC2.   
`project_id`: The identifier of the GCP project under which data is stored for the AWS account specified in the aws_account label, such as "my-project".   
`instance_id`: The VM instance identifier assigned by AWS.   
`aws_account`: The AWS account number under which the VM is running.   
`region`: The AWS region in which the VM is running. Supported AWS region values are listed by service at <http://docs.aws.amazon.com/general/latest/gr/rande.html>. The value supplied for this label must be prefixed with 'aws:' (for example, 'aws:us-east-1' is a valid value while 'us-east-1' is not).   
`aws_elasticache_cluster`  
Amazon Elasticache Cluster  |  A cache cluster in Amazon Elasticache.   
`project_id`: The identifier of the GCP project under which data is stored for the AWS account specified in the aws_account label, such as "my-project".   
`cluster_id`: The cluster identifier.   
`region`: The AWS region for the cluster. The format of this field is "aws:{region}", where supported values for {region} are listed at <http://docs.aws.amazon.com/general/latest/gr/rande.html>.   
`aws_account`: The AWS account number for the cluster.   
`aws_lambda_function`  
Amazon Lambda Function  |  A function in Amazon Lambda.   
`project_id`: The identifier of the GCP project under which data is stored for the AWS account specified in the aws_account label, such as "my-project".   
`function_name`: The function name.   
`region`: The AWS region for the function. The format of this field is "aws:{region}", where supported values for {region} are listed at <http://docs.aws.amazon.com/general/latest/gr/rande.html>.   
`aws_account`: The AWS account number for the function.   
`aws_rds_database`  
Amazon RDS Database  |  A database in Amazon Relational Database Service.   
`project_id`: The identifier of the GCP project under which data is stored for the AWS account specified in the aws_account label, such as "my-project".   
`name`: The database name.   
`region`: The AWS region for the database. The format of this field is "aws:{region}", where supported values for {region} are listed at <http://docs.aws.amazon.com/general/latest/gr/rande.html>.   
`aws_account`: The AWS account number for the database.   
`aws_s3_bucket`  
Amazon S3 Bucket  |  A bucket in Amazon S3.   
`project_id`: The identifier of the GCP project under which data is stored for the AWS account specified in the aws_account label, such as "my-project".   
`bucket_name`: The bucket name.   
`region`: The AWS region for the bucket. The format of this field is "aws:{region}", where supported values for {region} are listed at <http://docs.aws.amazon.com/general/latest/gr/rande.html>.   
`aws_account`: The AWS account number for the bucket.   
`aws_sqs_queue`  
Amazon SQS Queue  |  A queue in Amazon Simple Queue Service.   
`project_id`: The identifier of the GCP project under which data is stored for the AWS account specified in the aws_account label, such as "my-project".   
`queue`: The queue name.   
`region`: The AWS region for the queue. The format of this field is "aws:{region}", where supported values for {region} are listed at <http://docs.aws.amazon.com/general/latest/gr/rande.html>.   
`aws_account`: The AWS account number for the queue.   
`backupdr.googleapis.com/AutoProtectionPolicy`  
Auto Protection Policy  |  Represents a single Auto Protection Policy resource.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The GCP location.   
`auto_protection_policy_id`: The ID of the Auto Protection Policy.   
`backupdr.googleapis.com/AutoProtectionPolicyBinding`  
Auto Protection Policy Binding  |  Represents a single Auto Protection Policy Binding resource.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The GCP location.   
`auto_protection_policy_id`: The ID of the Auto Protection Policy.   
`binding_id`: The ID of the Auto Protection Policy Binding.   
`backupdr.googleapis.com/BackupDRProject`  
BackupDR Project  |  A BackupDR Project.   
`resource_container`: Backup and DR API enabled project.   
`location`: The GCP location.   
`backupdr.googleapis.com/BackupPlan`  
Backup Plan  |  Represents a single Backup Plan resource.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The GCP location.   
`backup_plan_id`: The ID of the Backup Plan.   
`backupdr.googleapis.com/BackupPlanAssociation`  
Backup Plan Association  |  Represents a single Backup Plan Association resource.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The GCP location.   
`backup_plan_association_id`: The ID of the Backup Plan Association.   
`backupdr.googleapis.com/BackupRecoveryAppliance`  
Backup Recovery Appliance  |  A Backup Recovery Appliance.   
`resource_container`: Backup and DR API enabled project.   
`location`: The GCP location.   
`backup_recovery_appliance_id`: The Backup recovery appliance Id.   
`management_server_id`: Name of the management server.   
`backupdr.googleapis.com/BackupVault`  
BackupVault  |  A specialized storage for Google Cloud Backup and DR backups.   
`resource_container`: The identifier of the GCP project on which the BackupDR API is enabled, such as "my-project".   
`location`: The GCP location.   
`backup_vault_id`: The BackupVault ID.   
`backupdr.googleapis.com/ManagementConsole`  
Management Console  |  A Backup and DR management console.   
`resource_container`: Backup and DR API enabled project.   
`location`: The GCP location.   
`management_server_id`: Name of the management server.   
`baremetalsolution.googleapis.com/Instance`  
Bare Metal Solution Instance  |  Bare Metal Solution Instance.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The GCP location where the instance resource resides.   
`instance_id`: The ID of the instance resource.   
`batch.googleapis.com/Job`  
Job  |  A Google Batch job managed by the Google Batch service.   
`resource_container`: The identifier of the GCP project associated with the job.   
`location`: The region where the job has been created.   
`job_id`: The identifier of the Job.   
`beyondcorp.googleapis.com/SecurityGateway`  
Security Gateway  |  Chrome Enterprise Premium Security Gateway.   
`resource_container`: The GCP container associated with the Security Gateway.   
`location`: The region that contains the Security Gateway.   
`security_gateway_id`: The Security Gateway ID.   
`bigquery.googleapis.com/ManagedRoutineInvocation`  
BigQuery Managed Routine Invocation  |  Logs and metrics from BigQuery Managed Routines.   
`resource_container`: The identifier of the GCP resource container associated with this resource, such as "my-project" or "organizations/123".   
`location`: The cloud location of the managed routine.   
`query_job_id`: The identifier of the BigQuery job that invoked the managed routine.   
`routine_project_id`: The project id of the invoked routine.   
`routine_dataset_id`: The dataset id of the invoked routine.   
`routine_id`: The id of the invoked routine.   
`bigquery.googleapis.com/SparkJob`  
BigQuery Spark Job  |  Logs and metrics from BigQuery Spark Jobs.   
`resource_container`: The identifier of the GCP resource container associated with this resource, such as "my-project" or "organizations/123".   
`location`: The Cloud location of the Spark job.   
`spark_job_id`: The ID of the Spark job.   
`bigquery_biengine_model`  
BigQuery BI Engine Model  |  BigQuery BI Engine Model.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The Google Cloud location of the resource.   
`model_id`: The identifier of the BI model.   
`bigquery_dataset`  
BigQuery Dataset  |  A dataset in BigQuery.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`dataset_id`: The name of the BigQuery dataset.   
`bigquery_dts_config`  
BigQuery DTS Config  |  A BigQuery Data Transfer Service configuration.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The Google Cloud location of the resource   
`config_id`: The id of the DTS configuration.   
`bigquery_project`  
BigQuery Project  |  BigQuery Project.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: Location of the resource.   
`bigquery_resource`  
BigQuery  |  A BigQuery resource.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`billing_account`  
Cloud Billing Account  |  A Cloud Billing Account.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`account_id`: The unique id of the billing account.   
`build`  
Cloud Build  |  A build in Cloud Build.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`build_id`: The unique id of the build.   
`build_trigger_id`: The unique id of the build trigger.   
`businessaicode.googleapis.com/BAICInstance`  
Business AI Code Instance  |  An instance resource that represents a Business AI Code configuration.   
`resource_container`: The identifier of the GCP container associated with this resource.   
`location`: The location of the resource.   
`certificatemanager.googleapis.com/Project`  
Certificate Manager project  |  Certificate Manager project.   
`resource_container`: The GCP container associated with the resource.   
`location`: GCP location.   
`chronicle.googleapis.com/Compliance`  
Chronicle Compliance  |  A Chronicle compliance object   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The physical location of the Chronicle instance.   
`instance_id`: The unique identifier for the Chronicle instance.   
`chronicle.googleapis.com/LogType`  
Chronicle Log Type  |  A Chronicle logtype object   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The physical location of the cluster that contains the logtype object.   
`log_type`: The name of the log type.   
`client_auth_config_brand`  
OAuth2 Brand  |  Consent screen data shown to users during three-legged OAuth2 flows.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`brand_id`: The unique id of the brand.   
`client_auth_config_client`  
OAuth2 Client  |  A client used in OAuth2 flows.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`client_id`: The unique id of the client.   
`cloud_composer_environment`  
Cloud Composer Environment  |  A Composer environment runs the managed Apache Airflow service.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The Cloud Composer location in which the environment is running.   
`environment_name`: The user-specified environment name.   
`cloud_dataproc_batch`  
Cloud Dataproc Batch  |  A Dataproc batch execution.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The Cloud Dataproc region to which the batch was submitted.   
`batch_id`: The user-specified batch id.   
`cloud_dataproc_cluster`  
Cloud Dataproc Cluster  |  A Dataproc cluster with separate cluster name and id labels.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`cluster_name`: The user-specified cluster name.   
`cluster_uuid`: The generated cluster id.   
`region`: The Cloud Dataproc region in which the cluster is running.   
`cloud_dataproc_job`  
Cloud Dataproc Job  |  A Dataproc job execution.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`region`: The Cloud Dataproc region to which the job was submitted.   
`job_id`: The user-specified job id.   
`job_uuid`: The generated job uuid.   
`cloud_dataproc_session`  
Cloud Dataproc Session  |  A Dataproc session execution.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The Cloud Dataproc region in which the session was created.   
`session_id`: The user-specified session id.   
`cloud_debugger_resource`  
Cloud Debugger  |  A Google Cloud Debugger resource.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`app`: The application to which the debugger is attached.   
`cloud_function`  
Cloud Function  |  A function in Google Cloud Functions.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`function_name`: The short function name.   
`region`: The region in which the function is running.   
`cloud_osconfig_patch_job`  
OS Patch Job  |  A Google Cloud OS Patch Job.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`patch_job_id`: Identifier of the job.   
`cloud_run_instance`  
Cloud Run Instance  |  An instance in Cloud Run.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`instance_name`: Name of the monitored instance.   
`location`: Region where the instance exists.   
`cloud_run_job`  
Cloud Run Job  |  A job in Cloud Run.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`job_name`: Name of the monitored job.   
`location`: Region where the job exists.   
`cloud_run_revision`  
Cloud Run Revision  |  A revision in Cloud Run.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`service_name`: Name of the service.   
`revision_name`: Name of the monitored revision.   
`location`: Region where the service is running.   
`configuration_name`: Name of the configuration which created the monitored revision.   
`cloud_run_worker_pool`  
Cloud Run Worker Pool  |  A worker pool in Cloud Run.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`worker_pool_name`: Name of the worker pool.   
`revision_name`: Name of the monitored revision.   
`location`: Region where the worker pool is running.   
`configuration_name`: Name of the configuration which created the monitored revision.   
`cloud_scheduler_job`  
Cloud Scheduler Job  |  A Cloud Scheduler Job.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The region of the job.   
`job_id`: Identifier of the job.   
`cloud_tasks_queue`  
Cloud Tasks Queue  |  A queue in Cloud Tasks.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`queue_id`: The name of the queue.   
`target_type`: The target type the queue is dispatching to.   
`location`: The zone or region where the application is running.   
`cloudaicompanion.googleapis.com/Instance`  
Gemini for Google Cloud Instance  |  An instance resource that represents a Gemini for Google Cloud configuration.   
`resource_container`: The identifier of the GCP container associated with this resource.   
`location`: The location of the resource.   
`instance_id`: The ID of the instance resource.   
`cloudcontrolspartner.googleapis.com/Location`  
Location  |  A Google Cloud Resource.   
`resource_container`: The identifier of the GCP container associated with the resource.   
`location`: The region in which the job is running.   
`clouddeploy.googleapis.com/DeliveryPipeline`  
Cloud Deploy Delivery Pipeline  |  A Cloud Deploy Delivery Pipeline.   
`resource_container`: The identifier of the Google Cloud project associated with this resource.   
`location`: The Google Cloud location where the resource resides.   
`pipeline_id`: ID of the delivery pipeline resource.   
`cloudkms_cryptokey`  
Cloud KMS CryptoKey  |  Cryptographic key in the KMS.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The region Crypto Key belongs to.   
`key_ring_id`: Key Ring the Crypto Key belongs to.   
`crypto_key_id`: Crypto Key Identifier.   
`cloudkms_cryptokeyversion`  
Cloud KMS CryptoKeyVersion  |  Version of a cryptographic key.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The region Crypto Key Version belongs to.   
`key_ring_id`: Key Ring the Crypto Key Version belongs to.   
`crypto_key_id`: Crypto Key the Crypto Key Version belongs to.   
`crypto_key_version_id`: Crypto Key Version Identifier.   
`cloudkms_keyring`  
Cloud KMS Key Ring  |  Collection of cryptographic keys.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The region Key Ring belongs to.   
`key_ring_id`: Key Ring Identifier.   
`cloudml_job`  
Cloud ML Job  |  A Google Cloud ML job.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`job_id`: An immutable identifier for a job.   
`region`: Cloud ML region.   
`cloudml_model_version`  
Cloud ML Model Version  |  A Google Cloud ML model version.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`model_id`: An immutable identifier for a model.   
`version_id`: An immutable identifier for a version.   
`region`: Cloud ML region.   
`cloudsql_database`  
Cloud SQL Database  |  A Cloud SQL instance.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`database_id`: The Google Cloud SQL instance name.   
`region`: The Google Cloud SQL region in which the database is running.   
`cloudvolumesgcp-api.netapp.com/CloudVolume`  
Monitored Resource for NetApp CVS  |  Monitored Resource for NetApp CVS.   
`resource_container`: Project information.   
`location`: Region/Zone information.   
`volume_id`: ID of the volume.   
`service_type`: Service type of the volume or replication relationship.   
`name`: Name of the volume or replication relationship.   
`compute.googleapis.com/Machine`  
Machine  |  A Compute Engine Machine ID   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`zone`: The zone of the GCP project associated with the machine.   
`machine_id`: The obfuscated ID of the machine   
`compute.googleapis.com/Reservation`  
Reservation  |  Monitored resource representing a reservation.   
`resource_container`: The GCP container (e.g. project number) associated with the reservation.   
`location`: The zone that contains the reservation.   
`reservation_id`: Reservation resource ID.   
`connectors.googleapis.com/Connection`  
Connectors  |  Monitored resource for Connectors.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: GCP region location of the connection.   
`connection`: The name of the connection.   
`consumed_api`  
Consumed API  |  An API used by customers.   
`project_id`: The identifier of the GCP project associated with this resource, such as 'my-project'.   
`service`: The API service name, such as 'cloudsql.googleapis.com'.   
`method`: The API method name, such as 'disks.list'.   
`version`: The API version, such as 'v1'.   
`location`: The service specific notion of location. This can be a name of a zone or region. If a service does not have any notion of zones then 'global' can be used.   
`credential_id`: The client credential ID, such as an API key ID or the OAuth client ID.   
`contactcenteraiplatform.googleapis.com/ContactCenter`  
CCAI Platform Contact Center  |  A CCAI Platform Contact Center instance.   
`resource_container`: Container of the current project.   
`resource_id`: The identifier of the Contact Center instance.   
`location`: The region in which the Contact Center is running.   
`container`  
GKE Container  |  A Google Kubernetes Engine (GKE) container instance.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`cluster_name`: An immutable name for the cluster the container is running in.   
`namespace_id`: Immutable ID of the cluster namespace the container is running in.   
`instance_id`: Immutable ID of the Compute Engine instance the container is running in.   
`pod_id`: Immutable ID of the pod the container is running in.   
`container_name`: Immutable name of the container.   
`zone`: The Compute Engine zone in which the instance is running.   
`container.googleapis.com/Cluster`  
Kubernetes Cluster Limits  |  Kubernetes Cluster.   
`resource_container`: Project or organization.   
`location`: Region or zone where the cluster was created.   
`cluster_name`: Cluster name.   
`container.googleapis.com/NodePool`  
GKE Node Pool  |  GKE Node Pool.   
`resource_container`: Project or organization.   
`location`: Region or zone where the cluster was created.   
`cluster_name`: Cluster name.   
`node_pool_name`: Node pool name.   
`contextawareaccess.googleapis.com/Location`  
Location  |  Access summary for risk based access levels.   
`resource_container`: The identifier of the Google Cloud organization associated with this resource.   
`location`: The location of the resource.   
`csr_repository`  
Cloud Source Repository  |  A repository in Google Cloud Source Repositories.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`name`: The name of the repository.   
`dataflow_step`  
Dataflow Step  |  A step in a Dataflow job.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`job_id`: The ID of the job.   
`step_id`: The ID of the step.   
`job_name`: The name of the job.   
`region`: The region in which the job is running.   
`dataform.googleapis.com/Repository`  
Dataform Repository  |  A Repository on Google Cloud Dataform.   
`resource_container`: The identifier of the GCP resource container associated with this resource, such as "my-project".   
`location`: The region in which the Repository is created.   
`repository_id`: The user-specified ID of the Repository.   
`datafusion.googleapis.com/InstanceV2`  
Cloud Data Fusion Instance  |  An instance of Cloud Data Fusion.   
`resource_container`: The ID of the customer project.   
`org_id`: The ID of the organization that the customer project belongs to.   
`location`: The zone/region that the instance is hosted in.   
`edition`: The edition of the instance.   
`is_private_ip_enabled`: Does the instance use private IP.   
`version`: The data plane version of the instance.   
`instance_id`: The instance ID.   
`namespace`: Name of the namespace.   
`datafusion.googleapis.com/InstanceV3`  
Cloud Data Fusion Instance  |  An instance of Cloud Data Fusion.   
`resource_container`: The ID of the customer project.   
`location`: The zone/region that the instance is hosted in.   
`edition`: The edition of the instance.   
`is_private_ip_enabled`: Does the instance use private IP.   
`version`: The data plane version of the instance.   
`instance_id`: The instance ID.   
`datafusion.googleapis.com/PipelineV2`  
Cloud Data Fusion Pipeline  |  A deployed Pipeline in a Cloud Data Fusion instance.   
`resource_container`: The ID of the customer project.   
`org_id`: The ID of the organization that the customer project belongs to.   
`location`: The zone/region that the instance is hosted in.   
`edition`: The edition of the instance.   
`is_private_ip_enabled`: Does the instance use private IP.   
`version`: The data plane version of the instance.   
`instance_id`: The instance ID.   
`namespace`: The namespace of the pipeline.   
`pipeline_id`: The Pipeline ID.   
`run_id`: The Run ID.   
`datamigration.googleapis.com/MigrationJob`  
Database migration service migration job  |  Database migration service migration job.   
`resource_container`: The resource container (project ID).   
`location`: The location.   
`migration_job_id`: The migration job ID.   
`dataplex.googleapis.com/Asset`  
Cloud Dataplex Asset  |  An Asset within a Cloud Dataplex Lake.   
`resource_container`: The identifier of GCP project associated with this resource.   
`location`: The GCP region associated with this resource.   
`lake_id`: The identifier of the Lake resource containing this resource.   
`zone_id`: The identifier of the Zone resource containing this resource.   
`asset_id`: The identifier of this Asset resource.   
`dataplex.googleapis.com/DataScan`  
Cloud Dataplex DataScan  |  A DataScan resource in Dataplex.   
`resource_container`: The identifier of GCP project associated with this resource.   
`location`: The GCP region associated with this resource.   
`datascan_id`: The identifier of this DataScan resource.   
`dataplex.googleapis.com/EntryLink`  
Cloud Dataplex Glossary Entry Link Resource  |  A Glossary Entry Link resource in Dataplex.   
`resource_container`: The identifier of GCP project associated with this resource.   
`location`: The cloud region that contains the resource.   
`entry_group_id`: The user-provided identifier for the entry group resource.   
`entry_link_id`: The user-provided identifier for the entry link resource.   
`dataplex.googleapis.com/EntryLinkType`  
Cloud Dataplex Entry Link Type Resource  |  An Entry Link Type resource in Dataplex.   
`resource_container`: The identifier of GCP project associated with this resource.   
`location`: The cloud region that contains the resource.   
`entry_link_type_id`: The user-provided identifier for the entry link type resource.   
`dataplex.googleapis.com/Environment`  
Cloud Dataplex Environment  |  An Environment within a Cloud Dataplex Lake.   
`resource_container`: The identifier of GCP project associated with this resource.   
`location`: The GCP region associated with this resource.   
`lake_id`: The identifier of the Lake resource containing this resource.   
`environment_id`: The identifier of this Environment resource.   
`dataplex.googleapis.com/Glossary`  
Cloud Dataplex Glossary Resource  |  A Glossary resource in Dataplex.   
`resource_container`: The identifier of GCP project associated with this resource.   
`location`: The cloud region that contains the resource.   
`glossary_id`: The user-provided identifier for the glossary resource.   
`dataplex.googleapis.com/GlossaryCategory`  
Cloud Dataplex Glossary Category Resource  |  A Glossary Category resource in Dataplex.   
`resource_container`: The identifier of GCP project associated with this resource.   
`location`: The cloud region that contains the resource.   
`glossary_id`: The user-provided identifier for the glossary resource.   
`glossary_category_id`: The user-provided identifier for the glossary category resource.   
`dataplex.googleapis.com/GlossaryTerm`  
Cloud Dataplex Glossary Term Resource  |  A Glossary Term resource in Dataplex.   
`resource_container`: The identifier of GCP project associated with this resource.   
`location`: The cloud region that contains the resource.   
`glossary_id`: The user-provided identifier for the glossary resource.   
`glossary_term_id`: The user-provided identifier for the glossary term resource.   
`dataplex.googleapis.com/GovernanceRule`  
Cloud Dataplex Governance Rule  |  A Governance rule resource in Dataplex.   
`resource_container`: The identifier of GCP project associated with this resource.   
`location`: The cloud region that contains the resource.   
`rule_id`: The user-provided identifier for the governance rule.   
`dataplex.googleapis.com/Lake`  
Cloud Dataplex Lake  |  A Cloud Dataplex Lake.   
`resource_container`: The identifier of GCP project associated with this resource.   
`location`: The GCP region associated with this resource.   
`lake_id`: The identifier of this Lake resource.   
`dataplex.googleapis.com/Project`  
Cloud Dataplex Project.  |  Cloud Dataplex Project.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The location of the resource.   
`dataplex.googleapis.com/Task`  
Cloud Dataplex Task  |  A Task within a Cloud Dataplex Lake.   
`resource_container`: The identifier of GCP project associated with this resource.   
`location`: The GCP region associated with this resource.   
`lake_id`: The identifier of the Lake resource containing this resource.   
`task_id`: The identifier of this Task resource.   
`dataplex.googleapis.com/Zone`  
Cloud Dataplex Zone  |  A Zone within a Cloud Dataplex Lake.   
`resource_container`: The identifier of GCP project associated with this resource.   
`location`: The GCP region associated with this resource.   
`lake_id`: The identifier of the Lake resource containing this resource.   
`zone_id`: The identifier of this Zone resource.   
`datastore_database`  
Cloud Datastore Database  |  A Cloud Datastore database.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`database_id`: The unique id of the database.   
`datastore_index`  
Cloud Datastore Index  |  A Cloud Datastore index.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`database_id`: The database the index belongs to.   
`index_id`: The unique id of the index.   
`datastream.googleapis.com/Stream`  
Datastream Stream  |  A Datastream stream.   
`resource_container`: The resource container (project ID).   
`location`: The location.   
`stream_id`: The stream ID.   
`dell_emc_cloud_onefs_cluster`  
Dell EMC Cloud OneFS Cluster  |  Multi-protocol access to files and directories on GCP, Isilon Cloud OneFS clusters with SMB for Windows, and NFS for UNIX file systems.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The Google Cloud location in which the cluster is running.   
`cluster_id`: Unique identifier of the cluster.   
`deployment`  
Deployment  |  A Deployment Manager deployment.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`name`: Name that uniquely identifies the deployment within a project.   
`deployment_manager_manifest`  
Deployment Manager Manifest  |  A Deployment Manager manifest which is used to specify the contents of a deployment.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`manifest_name`: Name that uniquely identifies the manifest within a project.   
`deployment_name`: Name of the deployment.   
`deployment_manager_operation`  
Deployment Manager Operation  |  A Deployment Manager operation.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`operation_name`: Name that uniquely identifies the operation within a project.   
`deployment_manager_resource`  
Deployment Manager Resource  |  Deployment Manager's record of Google Cloud Platform resources in a Deployment, such as a VM or a bucket.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`resource_name`: Name of the resource, unique within a deployment.   
`deployment_name`: Name of the deployment.   
`deployment_manager_type`  
Deployment Manager Type  |  A Deployment Manager type.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`name`: Name that uniquely identifies the type within a project.   
`dialogflow.googleapis.com/Location`  
Dialogflow Location  |  A Dialogflow Location (sometimes called Region).   
`resource_container`: The id of the GCP resource container associated with this resource.   
`location`: Location of resource.   
`discoveryengine.googleapis.com/Agent`  
Gemini Enterprise Agent  |  A specific Agent resource within Gemini Enterprise, mapping to discoveryengine.googleapis.com/Agent.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud location where the Agent is located.   
`assistant_id`: The unique identifier of the Assistant.   
`engine_id`: The unique identifier of the Engine.   
`agent_id`: The unique identifier of the Agent.   
`discoveryengine.googleapis.com/AgentToolInvocation`  
Gemini Enterprise Agent Tool Invocation  |  An Invocation of a specific Tool within the context of Gemini Enterprise Agent. This resource type is used for tracking tool-level metrics and latencies scoped to individual agents.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud location where the Tool is located.   
`assistant_id`: The unique identifier of the Assistant using the tool.   
`engine_id`: The unique identifier of the Engine where the tool is used.   
`agent_id`: The unique identifier of the Agent using the tool.   
`tool_id`: The unique identifier of the Tool.   
`discoveryengine.googleapis.com/DataConnector`  
Gemini Enterprise Data Connector  |  A specific Data Connector resource within Gemini Enterprise, mapping to discoveryengine.googleapis.com/DataConnector.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud location where the Data Connector is located.   
`connector_id`: The unique identifier of the Data Connector.   
`data_source`: Type of the Data Connector.   
`discoveryengine.googleapis.com/Engine`  
Gemini Enterprise Engine  |  A specific Engine (app) resource within Gemini Enterprise, mapping to discoveryengine.googleapis.com/Engine.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud location where the Engine is located.   
`collection_id`: The Collection the Engine belongs to (e.g. default_collection).   
`engine_id`: The unique identifier of the Engine.   
`dns_managed_zone`  
Managed DNS Zone  |  A ManagedZone in the Google Cloud DNS service.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`zone_name`: The name of the ManagedZone.   
`location`: The location field is provided for compatibility with other GCP services. Its value is always set to 'global'   
`dns_policy`  
Cloud DNS Policy  |  A Policy in the Google Cloud DNS service.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`policy_name`: The name of the Policy.   
`location`: The location field is provided for compatibility with other GCP services. Its value is always set to 'global'   
`dns_query`  
Cloud DNS Query  |  A DNS query to a private DNS handled by the Google Cloud DNS service.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`target_name`: The DNS name managed by Cloud DNS to be resolved (e.g. the zone name, policy name, internal domain name). External names will have the value "external"   
`location`: The GCP zone where the DNS request was received (e.g. us-east1, us-west1).   
`target_type`: The target of the resolution of the DNS query (e.g. public-zone, private-zone, external).   
`source_type`: Source of the query (e.g. gce-vm, internet).   
`dns_resource_record_set`  
Cloud DNS Resource Record Set  |  A ResourceRecordSet in the Google Cloud DNS service.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`name`: The name of the ResourceRecordSet.   
`type`: The type of the ResourceRecordSet.   
`location`: The GCP region where the ResourceRecordSet is located.   
`dns_response_policy`  
Cloud DNS Response Policy  |  A ResponsePolicy in the Google Cloud DNS service.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The GCP region where the ResponsePolicy is located.   
`response_policy_name`: The name of the ResponsePolicy.   
`dns_response_policy_rule`  
Cloud DNS Response Policy Rule  |  A ResponsePolicyRule in the Google Cloud DNS service.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The GCP region where the ResponsePolicyRule is located.   
`response_policy_name`: The name of the parent ResponsePolicy.   
`response_policy_rule_name`: The name of the ResponsePolicyRule.   
`edgecache.googleapis.com/EdgeCacheRouteRule`  
Edge Cache Route Rule  |  An Edge Cache route rule represents an Edge Cache Service's traffic as part of a Media Edge deployment.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: A GCP zone close to the proxy location. Please note that this may change over time.   
`service_name`: The name of the EdgeCacheService.   
`path_matcher_name`: The name of the PathMatcher that contains this route.   
`matched_path`: The matched URL prefix, full URL path, or path template.   
`route_type`: The type of the routed matched by the incoming request, one of [ORIGIN, URL_REDIRECT].   
`route_destination`: The URL of the origin this request is to be proxied to.   
`eventarc.googleapis.com/Enrollment`  
Eventarc Enrollment  |  An Enrollment represents a subscription for messages on a particular MessageBus.   
`resource_container`: The identifier of the GCP container associated with the resource.   
`location`: The location of the GCP project associated with the resource.   
`enrollment_id`: The ID of the Enrollment.   
`eventarc.googleapis.com/GoogleApiSource`  
Eventarc Google API Source  |  A GoogleApiSource represents a subscription of 1P events from a MessageBus.   
`resource_container`: The identifier of the GCP container associated with the resource.   
`location`: The location of the GCP project associated with the resource.   
`google_api_source_id`: The ID of the GoogleApiSource.   
`eventarc.googleapis.com/MessageBus`  
Eventarc Message Bus  |  MessageBus for the messages flowing through the system.   
`resource_container`: The identifier of the GCP container associated with the resource.   
`location`: The location of the GCP project associated with the resource.   
`message_bus_id`: The ID of the MessageBus.   
`eventarc.googleapis.com/Pipeline`  
Eventarc Pipeline  |  A Pipeline represents a destination for messages subscribed by an Enrollment.   
`resource_container`: The identifier of the GCP container associated with the resource.   
`location`: The location of the GCP project associated with the resource.   
`pipeline_id`: The ID of the Pipeline.   
`faulttesting.googleapis.com/Experiment`  
Fault Injection Experiment  |  Experiment associated with a template to inject faults.   
`resource_container`: The identifier of the GCP resource container associated with this resource (project_id), such as "my-project" or "organizations/123".   
`location`: The location in which the Fault Injection Experiment is present.   
`experiment_id`: The ID of the Experiment.   
`filestore_instance`  
Filestore Instance  |  A Filestore instance.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The physical location of the instance.   
`instance_name`: The name for the Filestore instance.   
`financialservices.googleapis.com/BacktestResult`  
Financial Services Backtest Result  |  A BacktestResult within the Financial Services API.   
`resource_container`: The identifier of the GCP container associated with this resource.   
`location`: The GCP location associated with this resource (e.g., us-central1).   
`instance_id`: The FinServ instance that contains this resource (e.g., test-instance).   
`backtest_result_id`: BacktestResult ID (e.g., test-backtest-result).   
`financialservices.googleapis.com/EngineConfig`  
Financial Services Engine Config  |  An EngineConfig within the Financial Services API.   
`resource_container`: The identifier of the GCP container associated with this resource.   
`location`: The GCP location associated with this resource (e.g., us-central1).   
`instance_id`: The FinServ instance that contains this resource (e.g., test-instance).   
`engine_config_id`: EngineConfig ID (e.g., test-engine-config).   
`financialservices.googleapis.com/Instance`  
Financial Services Instance  |  An Instance within the Financial Services API.   
`resource_container`: The identifier of the GCP container associated with this resource.   
`location`: The GCP location associated with this resource (e.g., us-central1).   
`instance_id`: Instance ID (e.g., test-instance).   
`financialservices.googleapis.com/PredictionResult`  
Financial Services Prediction Result  |  A PredictionResult within the Financial Services API.   
`resource_container`: The identifier of the GCP container associated with this resource.   
`location`: The GCP location associated with this resource (e.g., us-central1).   
`instance_id`: The FinServ instance that contains this resource (e.g., test-instance).   
`prediction_result_id`: PredictionResult ID (e.g., test-prediction-result).   
`firebase_auth`  
Firebase Auth Project  |  A Firebase Auth Project.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`firebase_domain`  
Firebase Hosting Site Domain  |  A domain from which a Firebase Hosting site is serving traffic.   
`project_id`: The identifier of the GCP project associated with this resource, such as 'my-project'.   
`site_name`: The name of a Firebase Hosting site, that is the subdomain in .web.app.   
`domain_name`: The default subdomain (on web.app or firebaseapp.com) or custom domain from which content was served.   
`firebase_namespace`  
Firebase Realtime Database  |  A Firebase Realtime Database.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`table_name`: The name of the database.   
`location`: The location of the database.   
`firebaseapphosting.googleapis.com/Backend`  
Firebase App Hosting Backend  |  A Firebase App Hosting Backend.   
`resource_container`: The GCP container (usually project ID) for the App Hosting Backend.   
`location`: The serving locality of the App Hosting Backend, such as "global" or "us-central1". For v1 backends, this will be "global".   
`backend_id`: An identifier for the App Hosting Backend within a project.   
`firebasecrashlytics.googleapis.com/App`  
Firebase Crashlytics App  |  A Firebase client using Crashlytics.   
`resource_container`: The Firebase project for the application.   
`location`: Location for Firebase Apps is global.   
`app_id`: A Firebase App ID.   
`firebaserules_release`  
Releases for Firebase Rules  |  Mapping of the ruleset to a release name.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`release_name`: Name of the release.   
`region`: The region in which the ruleset is on.   
`firebaserules_ruleset`  
Ruleset for Firebase Rules  |  Definition of the ruleset for firebase rules.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`ruleset_name`: Name of the ruleset.   
`region`: The region in which the ruleset is on.   
`firebasevertexai.googleapis.com/Model`  
Firebase AI Logic Model  |  A Model supported by Firebase AI Logic.   
`resource_container`: The GCP container associated with the model.   
`location`: The zone that served the model.   
`publisher_id`: The publisher ID of the model, such as "google".   
`model_id`: The model ID, such as "gemini-0.0-flash-002".   
`firebasevertexai.googleapis.com/PromptTemplate`  
Firebase AI Logic Server Prompt Template  |  A Firebase AI Logic Server Prompt Template.   
`resource_container`: The GCP container associated with the prompt template.   
`location`: The region that served the prompt template.   
`template_id`: The prompt template ID.   
`firestore.googleapis.com/Database`  
Firestore Database  |  A Firestore Database.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The location of the database.   
`database_id`: The database id.   
`fleetengine.googleapis.com/DeliveryFleet`  
Fleet Engine Last Mile Fleet Solution  |  A top-level resource for Fleet Engine Last Mile Fleet Solution metrics and logs.   
`resource_container`: The identifier of the GCP container associated with DeliveryFleet.   
`location`: The region in which the Fleet Engine instance is running.   
`fleetengine.googleapis.com/Fleet`  
Fleet Engine On Demand Rides and Deliveries  |  A top-level resource for Fleet Engine On Demand Rides and Deliveries metrics and logs.   
`resource_container`: The identifier of the GCP container associated with Fleet.   
`location`: The region in which the Fleet Engine instance is running.   
`folder`  
Google Folder  |  A Google Cloud Platform folder.   
`folder_id`: Numeric id of the folder.   
`gae_app`  
GAE Application  |  An application running in Google App Engine (GAE).   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`module_id`: The service/module name.   
`version_id`: The version name.   
`zone`: The GAE zone where the application is running.   
`gateway_scope`  
Gateway Scope  |  GatewayScope represents a set of Gateways with the same merged configs.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The location of the control plane   
`scope`: The name of the gateway_scope   
`gce_autoscaler`  
Autoscaler  |  A Google Compute Engine autoscaler.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`autoscaler_id`: Unique identifier of the autoscaler.   
`location`: Compute Engine zone or region where the autoscaler is running.   
`gce_backend_bucket`  
Backend Bucket  |  A Google Compute Engine backend bucket.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`backend_bucket_id`: Unique identifier of the backend bucket.   
`gce_backend_service`  
Cloud Load Balancing Backend Service  |  A Compute Engine backend service.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`backend_service_id`: Unique identifier of the backend service.   
`location`: Global or Compute Engine region containing the backend service   
`gce_client_ssl_policy`  
Client SSL Policy  |  A Google Compute Engine client SSL policy.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`client_ssl_policy_id`: Unique identifier of the client SSL policy.   
`gce_commitment`  
Committed Use Discount  |  A Google Compute Engine committed use discount.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`commitment_id`: Unique identifier of the committed use discount.   
`location`: Compute Engine region where the committed use discount is active.   
`gce_disk`  
Disk  |  A disk belonging to a Compute Engine instance.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`disk_id`: Unique identifier of the disk.   
`zone`: The Compute Engine zone where the disk resides.   
`gce_firewall_rule`  
Firewall Rule  |  A Google Compute Engine firewall rule.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`firewall_rule_id`: Unique identifier of the firewall rule.   
`gce_forwarding_rule`  
Forwarding Rule  |  A Google Compute Engine Forwarding Rule.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`forwarding_rule_id`: Unique identifier of the forewarding rule.   
`region`: Compute Engine region where the forwarding rule resides.   
`gce_ha_controller`  
HA Controller  |  A Google Compute Engine HA controller.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`ha_controller_id`: Unique identifier of the HA controller.   
`location`: Compute Engine region where the HA controller resides.   
`gce_health_check`  
Health Check  |  A Google Compute Engine health check.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`health_check_id`: Unique identifier of the health check.   
`gce_image`  
Image  |  A Google Compute Engine image resource.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`image_id`: Unique numerical identifier of the image.   
`gce_instance`  
VM Instance  |  A virtual machine instance hosted in Compute Engine.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`instance_id`: The numeric VM instance identifier assigned by Compute Engine.   
`zone`: The Compute Engine zone in which the VM is running.   
`gce_instance_group`  
Instance Group  |  A Google Compute Engine instance group resource.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`instance_group_id`: The unique numerical identifier of the instance group.   
`instance_group_name`: The unique user provided name of the instance group.   
`location`: Compute Engine zone containing the instance group.   
`gce_instance_group_manager`  
Instance Group Manager  |  A Google Compute Engine instance group manager resource.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`instance_group_manager_id`: The unique numerical identifier of the instance group manager.   
`instance_group_manager_name`: The unique user provided name of the instance group manager.   
`location`: Compute Engine zone or region where the instance group manager is located.   
`gce_instance_template`  
Instance Template  |  A Google Compute Engine instance template resource.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`instance_template_id`: The unique numerical identifier of the instance template.   
`instance_template_name`: The unique user provided name of the instance template.   
`gce_license`  
License  |  A Google Compute Engine license.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`license_id`: Unique identifier of the license.   
`gce_network`  
Network  |  A Google Compute Engine network.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`network_id`: Unique identifier of the network.   
`gce_network_endpoint_group`  
Network Endpoint Group  |  A Compute Engine network endpoint group resource.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`zone`: The name of the zone where the network endpoint group is located.   
`network_endpoint_group_id`: The ID of the network endpoint group.   
`gce_network_region`  
Network Region  |  A region of a Compute Engine network.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`network_id`: The ID of the Compute Engine network.   
`region`: The name of the network region.   
`gce_node_group`  
Node Group  |  A Compute Engine node group.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`node_group_id`: Unique identifier of the node group.   
`zone`: Zone of the node group.   
`gce_node_template`  
Node Template  |  A Compute Engine node template.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`node_template_id`: Unique identifier of the node template.   
`region`: Region of the node template.   
`gce_operation`  
Operation  |  A Google Compute Engine operation resource.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`operation_name`: The unique user provided name of the operation.   
`location`: Location of the resource.   
`gce_packet_mirroring`  
Packet Mirroring  |  A Google Compute Engine packet mirroring.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`packet_mirroring_id`: Unique identifier of the packet mirroring.   
`region`: Region of the packet mirroring.   
`gce_project`  
Project  |  A Google Compute Engine project resource.   
`project_id`: Compute Engine specific numeric identifier of the project resource.   
`gce_reserved_address`  
Reserved Address  |  A Google Compute Engine reserved address.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`reserved_address_id`: Unique identifier of the reserved address.   
`location`: Global or Compute Engine region containing the reserved address   
`gce_resource_policy`  
Resource Policy  |  A Compute Engine resource policy.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`resource_policy_id`: Unique identifier of the resource policy.   
`region`: Region of the resource policy.   
`gce_route`  
Route  |  A Google Compute Engine route.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`route_id`: Unique identifier of the route.   
`gce_router`  
Router  |  A Google Compute Engine router.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`router_id`: Unique identifier of the router.   
`region`: Region of the router.   
`gce_service_attachment`  
Service Attachment  |  A Private Service Connect Service Attachment.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`region`: The region where the service attachment resides.   
`service_attachment_id`: Unique identifier of the service attachment.   
`gce_snapshot`  
Snapshot  |  A Google Compute Engine snapshot.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`snapshot_id`: Unique identifier of the snapshot.   
`gce_ssl_certificate`  
SSL Certificate  |  A Google Compute Engine SSL certificate.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`ssl_certificate_id`: The unique numerical identifier of the SSL certificate.   
`ssl_certificate_name`: The unique user provided name of the SSL Certificate.   
`gce_subnetwork`  
Subnetwork  |  A Compute Engine subnetwork.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`subnetwork_id`: The unique numerical identifier of the subnetwork.   
`subnetwork_name`: The unique user provided name of the subnetwork.   
`location`: Location of the resource.   
`gce_target_http_instance`  
Target HTTP Instance  |  A Google Compute Engine target http instance.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`target_http_instance_id`: Unique identifier of the target http instance.   
`zone`: Compute Engine zone where the target http instance resides.   
`gce_target_http_proxy`  
Target HTTP Proxy  |  A Google Compute Engine target http proxy.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`target_http_proxy_id`: Unique identifier of the target http proxy.   
`gce_target_https_proxy`  
Target HTTPS Proxy  |  A Google Compute Engine target https proxy.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`target_https_proxy_id`: Unique identifier of the target https proxy.   
`gce_target_pool`  
Target Pool  |  A Google Compute Engine target pool.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`target_pool_id`: Unique identifier of the target pool.   
`zone`: Compute Engine zone where the pool resides.   
`gce_target_ssl_proxy`  
Target SSL Proxy  |  A Google Compute Engine target SSL proxy.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`target_ssl_proxy_id`: Unique identifier of the target ssl proxy.   
`gce_url_map`  
URL Map  |  A Google Compute Engine URL map.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`url_map_id`: Unique identifier of the url map.   
`gcs_bucket`  
GCS Bucket  |  A Google Cloud Storage (GCS) bucket.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`bucket_name`: An immutable name of the bucket.   
`location`: Location of the bucket.   
`geminidataanalytics.googleapis.com/Location`  
Gemini Data Analytics Location  |  A Gemini Data Analytics Location.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The location of the GCP project associated with this resource.   
`generic_node`  
Generic Node  |  A generic node identifies a machine or other computational resource for which no more specific resource type is applicable. The label values must uniquely identify the node.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The Google Cloud region or zone that determines where data about the resource is stored. For example, "us-east1-a".   
`namespace`: A namespace identifier, such as a cluster name.   
`node_id`: A unique identifier for the node within the namespace, such as a hostname or IP address.   
`generic_task`  
Generic Task  |  A generic task identifies an application process for which no more specific resource is applicable, such as a process scheduled by a custom orchestration system. The label values must uniquely identify the task.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The Google Cloud region or zone that determines where data about the resource is stored. For example, "us-east1-a".   
`namespace`: A namespace identifier, such as a cluster name.   
`job`: An identifier for a grouping of related tasks, such as the name of a microservice or distributed batch job.   
`task_id`: A unique identifier for the task within the namespace and job, such as a replica index identifying the task within the job.   
`genomics_dataset`  
Genomics Dataset  |  A dataset in the Google Genomics service.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`dataset_id`: Unique identifier of the dataset.   
`genomics_operation`  
Genomics Operation  |  A long running operation in the Google Genomics service.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`operation_id`: Unique identifier of the long running operation.   
`gke_cluster`  
GKE Cluster Operations  |  A Google Kubernetes Engine (GKE) Cluster. It contains events and audit logs about cluster operations.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`cluster_name`: The name of the GKE Cluster.   
`location`: The location in which the GKE Cluster is running.   
`gke_nodepool`  
GKE Node Pool Operations  |  A Google Kubernetes Engine (GKE) Node Pool. It contains audit logs about Node Pool operations.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`nodepool_name`: The name of the GKE Node Pool.   
`location`: The location in which the GKE Cluster is running.   
`cluster_name`: The name of the GKE Cluster to which this Node Pool belongs.   
`gkebackup.googleapis.com/BackupPlan`  
GKE Backup Plan  |  A backup plan provides configuration, location, and management functions for a sequence of backups.   
`resource_container`: The identifier of the Google Cloud container associated with the resource.   
`location`: The Google Cloud location where this backupPlan resides.   
`backup_plan_id`: The name of the backupPlan.   
`gkebackup.googleapis.com/RestorePlan`  
GKE Restore Plan  |  A restore plan defines the configuration of a series of restore operations to be performed against backups which belong to the specified backup plan.   
`resource_container`: The identifier of the Google Cloud container associated with the resource.   
`location`: The Google Cloud location where this restorePlan resides.   
`restore_plan_id`: The name of the restorePlan.   
`global`  
Global  |  A resource type used to indicate that a log is not associated with any specific resource.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`health.googleapis.com/Subscriber`  
Health API Subscriber  |  A subscriber of the Google Health API to receive data change notifications.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The location of the resource.   
`subscriber_id`: The identifier of the subscriber which is unique per GCP Project.   
`healthcare_pipeline_job`  
Healthcare Pipeline Job  |  A Cloud Healthcare Pipeline Job.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The Google Cloud location of the dataset that contains the Pipeline Job.   
`dataset_id`: The ID of the dataset.   
`pipeline_job_id`: The ID of the Pipeline Job.   
`http_external_regional_lb_rule`  
Regional External Application Load Balancer Rule  |  A resource descriptor for regional external Application Load Balancer behavior.   
`project_id`: The identifier of the Google Cloud project associated with this resource, such as 'my-project'.   
`network_name`: The name of the customer network in which the Load Balancer resides.   
`region`: The region under which the Load Balancer is defined.   
`url_map_name`: The name of the urlmap.   
`forwarding_rule_name`: The name of the forwarding rule.   
`target_proxy_name`: The name of the target HTTP/S proxy.   
`matched_url_path_rule`: The prefix of URL defined in urlmap tree. 'UNMATCHED' for the sink default rule.   
`backend_target_name`: The name of the backend target or service.   
`backend_target_type`: The type of the backend target. Can be 'BACKEND_SERVICE', or 'UNKNOWN' if the backend wasn't assigned.   
`backend_name`: The name of the backend group. Can be '' if the backend wasn't assigned.   
`backend_type`: The type of the backend group. Can be 'INSTANCE_GROUP', 'NETWORK_ENDPOINT_GROUP', or 'UNKNOWN' if the backend wasn't assigned.   
`backend_scope`: The scope of the backend group. Can be 'UNKNOWN' if the backend wasn't assigned.   
`backend_scope_type`: The type of the scope of the backend group. Can be 'ZONE', 'REGION', or 'UNKNOWN' in case the backend wasn't assigned.   
`http_load_balancer`  
Application Load Balancer  |  An Application Load Balancer Instance.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`forwarding_rule_name`: The name of the forwarding rule.   
`url_map_name`: The name of the urlmap.   
`target_proxy_name`: The name of the target proxy.   
`backend_service_name`: The name of the backend service.   
`zone`: The zone in which the load balancer is running.   
`iam.googleapis.com/WorkforcePoolProvider`  
Workforce Identity Pool Provider  |  A workforce identity pool provider.   
`resource_container`: The identifier of the Google Cloud organization associated with this resource.   
`location`: The location of the resource.   
`pool_id`: The ID of the provider's workforce pool parent resource.   
`provider_id`: The ID of the workforce pool provider resource.   
`iam_role`  
IAM Role  |  An IAM role.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`role_name`: The name of the IAM custom role; this labelappears only on custom roles.(e.g., roles/[CUSTOM_ROLE],organizations/123456/roles/[CUSTOM_ROLE],projects/myproject/roles/[CUSTOM_ROLE]).   
`identitytoolkit_project`  
Project  |  An Identity Toolkit project.   
`project_id`: The identifier of the GCP project associated with this resource.   
`identitytoolkit_tenant`  
Identity Toolkit Tenant  |  An Identity Toolkit tenant.   
`project_id`: The identifier of the GCP project associated with this resource.   
`tenant_name`: The name of the tenant.   
`ids.googleapis.com/Endpoint`  
IDS Endpoint  |  A Cloud IDS Endpoint.   
`resource_container`: The identifier of the GCP project owning the Endpoint.   
`location`: The zone of the IDS Endpoint.   
`id`: The ID of the Endpoint.   
`integrations.googleapis.com/IntegrationVersion`  
Integration Version  |  An integration version to be executed.   
`resource_container`: The project id.   
`location`: The location value.   
`product`: The product value.   
`integration`: The integration name.   
`version`: The version id of the integration.   
`interconnect`  
Interconnect  |  A physical connection to Google at a datacenter.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`interconnect`: The unique identifier of the interconnect.   
`interconnect_attachment`  
Interconnect Attachment  |  A VLAN attaching a cloud network to an Interconnect.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`attachment`: The unique identifier of the attachment.   
`interconnect`: The unique identifier of the interconnect that the attachment connects to.   
`region`: The cloud region that the attachment connects to.   
`interconnect_project`: The name of the project that owns interconnect that the attachment connects to.   
`internal_http_lb_rule`  
Internal Application Load Balancer Rule  |  A resource descriptor for internal Application Load Balancer behavior.   
`project_id`: The identifier of the Google Cloud project associated with this resource, such as 'my-project'.   
`network_name`: The name of the customer network in which the Load Balancer resides.   
`region`: The region under which the Load Balancer is defined.   
`url_map_name`: The name of the urlmap.   
`forwarding_rule_name`: The name of the forwarding rule.   
`target_proxy_name`: The name of the target HTTP(S) proxy.   
`matched_url_path_rule`: The prefix of URL defined in urlmap tree. 'UNMATCHED' for the sink default rule.   
`backend_target_name`: The name of the backend target or service.   
`backend_target_type`: The type of the backend target. Can be 'BACKEND_SERVICE', or 'UNKNOWN' if the backend wasn't assigned.   
`backend_name`: The name of the backend group. Can be '' if the backend wasn't assigned.   
`backend_type`: The type of the backend group. Can be 'INSTANCE_GROUP', 'NETWORK_ENDPOINT_GROUP', or 'UNKNOWN' if the backend wasn't assigned.   
`backend_scope`: The scope of the backend group. Can be 'UNKNOWN' if the backend wasn't assigned.   
`backend_scope_type`: The type of the scope of the backend group. Can be 'ZONE', 'REGION', or 'UNKNOWN' in case the backend wasn't assigned.   
`istio_control_plane`  
Istio Control Plane  |  An Istio Control Plane is an instance of a service that provides xDS and related functionality to a set of managed Istio proxies.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`mesh_uid`: Unique identifier for an Istio service mesh.   
`location`: The physical location in which the workload for the Control Plane is located.   
`revision`: Immutable revision of Istio managed by the Control Plane.   
`build_id`: Immutable build tag for the instance of the Control Plane.   
`owner`: Immutable name of the owner of the Control Plane.   
`k8s_cluster`  
Kubernetes Cluster  |  A Kubernetes cluster. It contains Kubernetes audit logs from the cluster.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The physical location of the cluster.   
`cluster_name`: The name of the cluster.   
`k8s_container`  
Kubernetes Container  |  A Kubernetes container instance.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The physical location of the cluster that contains the container.   
`cluster_name`: The name of the cluster that the container is running in.   
`namespace_name`: The name of the namespace that the container is running in.   
`pod_name`: The name of the pod that the container is running in.   
`container_name`: The name of the container.   
`k8s_control_plane_component`  
Kubernetes Control Plane Component  |  A Kubernetes Control Plane component.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The physical location of the cluster that contains the control plane component.   
`cluster_name`: The name of the cluster that the control plane component is running in.   
`component_name`: The name of the control plane component.   
`component_location`: The physical location where the control plane component is running.   
`k8s_node`  
Kubernetes Node  |  A Kubernetes node instance.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The physical location of the cluster that contains the node.   
`cluster_name`: The name of the cluster that the node is a part of.   
`node_name`: The name of the node.   
`k8s_pod`  
Kubernetes Pod  |  A Kubernetes pod instance.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The physical location of the cluster that contains the pod.   
`cluster_name`: The name of the cluster that the pod is running in.   
`namespace_name`: The name of the namespace that the pod is running in.   
`pod_name`: The name of the pod.   
`k8s_service`  
Kubernetes Service  |  A Kubernetes Service instance.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The physical location of the cluster that contains the service.   
`cluster_name`: The name of the cluster that the service is running in.   
`namespace_name`: The name of the namespace that the service is running in.   
`service_name`: The name of the service.   
`l4_proxy_rule`  
Proxy Network Load Balancer Rule  |  A resource descriptor for proxy Network Load Balancer behavior.   
`project_id`: The identifier of the Google Cloud project associated with this resource, such as 'my-project'.   
`network_name`: The name of the customer network in which the Load Balancer resides.   
`region`: The region under which the Load Balancer is defined.   
`load_balancing_scheme`: The load balancing scheme associated with the forwarding rule, one of [INTERNAL_MANAGED, EXTERNAL_MANAGED].   
`protocol`: The protocol associated with the traffic processed by the proxy, one of [TCP, UDP, SSL, UNKNOWN].   
`forwarding_rule_name`: The name of the forwarding rule.   
`target_proxy_name`: The name of the target proxy.   
`backend_target_name`: The name of the backend target or service.   
`backend_target_type`: The type of the backend target, one of ['BACKEND_SERVICE'; 'UNKNOWN' - if the backend wasn't assigned].   
`backend_name`: The name of the backend group. Can be '' if the backend wasn't assigned.   
`backend_type`: The type of the backend group, one of ['INSTANCE_GROUP'; 'NETWORK_ENDPOINT_GROUP'; 'UNKNOWN' - if the backend wasn't assigned].   
`backend_scope`: The scope of the backend group. Can be 'UNKNOWN' if the backend wasn't assigned.   
`backend_scope_type`: The type of the scope of the backend group, one of ['ZONE'; 'REGION'; 'UNKNOWN' - in case the backend wasn't assigned].   
`livestream.googleapis.com/Channel`  
Live Stream API Channel  |  A Live Stream API Channel.   
`resource_container`: The identifier of the GCP project associated with this channel resource.   
`location`: The GCP location where the channel resource resides.   
`channel_id`: ID of the channel resource.   
`loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule`  
External Passthrough Network Load Balancer Rule  |  A set of definitions for multi protocol network load balancing behavior.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`region`: The Google Cloud Platform region of the backend instance that connected to network load balancing forwarding rule.   
`backend_network_name`: The network name of the NIC of the instance that received the Net LB flow.   
`backend_target_type`: The type of the backend target that handled the connection.   
`backend_service_name`: The name of the backend service that handled the connection.   
`primary_target_pool`: The name of the primary target pool.   
`target_pool`: The name of the target pool.   
`forwarding_rule_name`: The name of the forwarding rule.   
`backend_group_name`: The name of the backend group that handled the connection.   
`backend_group_type`: The type of the backend group that handled the connection.   
`backend_group_scope`: The scope (zone or region) of the backend group that handled the connection.   
`backend_subnetwork_name`: The name of the subnetwork of the instance that handled the connection.   
`backend_zone`: The zone of the endpoint (VM instance) that handled the connection.   
`loadbalancing.googleapis.com/InternalNetworkLoadBalancerRule`  
Internal Passthrough Network Load Balancer Rule  |  A set of definitions for multi protocol internal load balancing behavior.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`region`: The Google Cloud Platform region of the backend instance that connected to network load balancing forwarding rule.   
`backend_network_name`: The network name of the NIC of the instance that received the Net LB flow.   
`backend_service_name`: The name of the backend service that handled the connection.   
`forwarding_rule_name`: The name of the forwarding rule.   
`backend_group_name`: The name of the backend group that handled the connection.   
`backend_group_type`: The type of the backend group that handled the connection.   
`backend_group_scope`: The scope (zone or region) of the backend group that handled the connection.   
`backend_subnetwork_name`: The name of the subnetwork of the instance that handled the connection.   
`logging_bucket`  
Logging Bucket  |  An export bucket in Cloud Logging.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`bucket_id`: The name of the log bucket.   
`location`: The location of the log bucket.   
`source_resource_container`: The source resource container (e.g. project, folder, organization) of the log entry that is destined for the log bucket. The format is "projects/project_id"   
`monitored_resource_type`: The type field of the monitored resource in the log entry that is destined for the log bucket.   
`logging_exclusion`  
Log Exclusion  |  An exclusion in Cloud Logging.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`name`: The unique name of the exclusion.   
`logging_log`  
Log stream  |  A Google Cloud Logging log.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`name`: Unique identifier of the log.   
`logging_sink`  
Logging export sink  |  An export sink in Cloud Logging.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`name`: The unique name of the sink.   
`destination`: The destination of the sink.   
`lustre.googleapis.com/Instance`  
Lustre instance  |  A Lustre Instance.   
`resource_container`: The identifier of the GCP consumer project associated with this resource, such as 'my-project'.   
`location`: The Google Cloud location in which the managed instance is running.   
`instance_id`: The ID of the managed instance.   
`managed_service`  
Managed Service  |  A service managed by Google Service Management.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`service_name`: The name of the service.   
`producer_project_id`: The id of the project which produces and owns this service.   
`managedflink.googleapis.com/Deployment`  
Managed Flink Deployment  |  A managed Flink cluster.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The location of the GCP project associated with this resource.   
`deployment_id`: The user-specified or system generated deployment identifier.   
`managedflink.googleapis.com/Job`  
Managed Flink Job  |  A job running on a deployment.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The location of the GCP project associated with this resource.   
`deployment_id`: The user-specified or system generated deployment identifier.   
`job_id`: The system-generated job identifier.   
`managedkafka.googleapis.com/Cluster`  
Apache Kafka Cluster  |  A Managed Kafka cluster.   
`resource_container`: The identifier of the project or container associated with this cluster.   
`location`: The region in which the cluster is created.   
`cluster_id`: The user-specified cluster id.   
`managedkafka.googleapis.com/ConnectCluster`  
Apache Kafka Connect Cluster  |  A Managed Kafka Connect cluster.   
`resource_container`: The identifier of the project or container associated with this cluster.   
`location`: The region in which the cluster is created.   
`cluster_id`: The user-specified cluster id.   
`managedkafka.googleapis.com/Location`  
Apache Kafka Location  |  A Managed Kafka location.   
`resource_container`: The identifier of the project or container associated with this location.   
`location`: The location in the API.   
`managedkafka.googleapis.com/SchemaRegistry`  
Apache Kafka Schema Registry  |  A Managed Kafka Schema Registry.   
`resource_container`: The identifier of the GCP project associated with this schema registry.   
`location`: The region in which the schema registry is created.   
`schema_registry_id`: The user-specified schema registry id.   
`memorystore.googleapis.com/Instance`  
Memorystore Instance  |  An instance hosted on Google Cloud Memorystore.   
`resource_container`: The identifier of the GCP consumer project associated with this resource, such as 'my-project'.   
`location`: The Google Cloud region in which the managed instance is running.   
`instance_id`: The ID of the managed instance.   
`instance_uid`: Identifier assigned by Google to uniquely distinguish an instance.   
`mesh`  
Mesh  |  A mesh serves as the "key" to deliver configuration to data plane proxy instances.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The location of the control plane   
`mesh`: The name of the mesh   
`metastore.googleapis.com/Federation`  
Dataproc Metastore Federation  |  A Dataproc Metastore Federation.   
`resource_container`: The ID of the customer project.   
`location`: The region that the federation is hosted in.   
`federation_id`: The federation ID.   
`metastore.googleapis.com/Service`  
Dataproc Metastore Service  |  A Dataproc Metastore Service.   
`resource_container`: The ID of the customer project.   
`location`: The region that the service is hosted in.   
`service_id`: The service ID.   
`metric`  
Metric Type  |  A Stackdriver Monitoring metric type.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`name`: The name of the metric type, such as "logging.googleapis.com/my-metric-name".   
`microsoft_ad_domain`  
Microsoft Active Directory Domain  |  A Microsoft Active Directory Domain hosted and managed by Google Cloud Platform   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`fqdn`: The fully qualified domain name of the Active Directory Domain   
`location`: The location where Active Directory Domain resources (like VMs, etc.) are present.   
`ml_job`  
Cloud ML Job  |  A Cloud Machine Learning job.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`job_id`: The job identifier.   
`task_name`: The task name.   
`mobilitybilling.googleapis.com/Project`  
Google Maps Platform - Mobility Billing  |  A top-level resource for Mobility Billing metrics and logs.   
`resource_container`: The identifier of the GCP container associated with this resource.   
`location`: The region in which the Mobility Billing instance is running.   
`modelarmor.googleapis.com/SanitizeOperation`  
Model Armor Sanitize Operation  |  A resource that represents the Model Armor sanitize operations.   
`resource_container`: The identifier of the GCP resource container associated with this resource, such as "my_project" or "organizations/5678".   
`location`: The GCP location.   
`template_id`: The template ID.   
`modelarmor.googleapis.com/Template`  
Model Armor Template  |  A resource that represents the Model Armor template operations.   
`resource_container`: The identifier of the GCP resource container associated with this resource, such as "my_project" or "organizations/5678".   
`location`: The GCP location.   
`template_id`: The template ID.   
`nat_gateway`  
Cloud NAT Gateway  |  A Cloud NAT Gateway.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`region`: The region where the NAT gateway is located.   
`router_id`: Identifier of the router under which the NAT gateway is defined.   
`gateway_name`: The name of the NAT gateway.   
`netapp.googleapis.com/StoragePool`  
Google Cloud NetApp Volumes StoragePool  |  Google Cloud NetApp Volumes StoragePool.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: StoragePool region/zone.   
`name`: Name of the storage pool.   
`netapp_cloud_volume`  
NetApp Cloud Volume  |  A specific volume in the NetApp Cloud Volumes service.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The Google Cloud location in which the NetApp Cloud Volume instance is running.   
`volume_id`: The ID of a NetApp Volume.   
`network_security_policy`  
Network Security Policy  |  A network security policy.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The region where the security policy resides. For global security policies this is "global".   
`policy_name`: The unique user provided name of the security policy.   
`networkactions.googleapis.com/WasmPluginVersion`  
Media CDN Wasm Plugin Version  |  A single immutable version of a Media CDN WasmPlugin (code + runtime config).   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The location of this service. Only 'global' is allowed.   
`plugin_name`: The name of the WasmPlugin.   
`plugin_version`: The name of the WasmPluginVersion.   
`networking.googleapis.com/Location`  
GCP Location  |  A GCP location: a specific zone or region, or "global".   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: Name of a GCP zone/region, or "global".   
`networkmanagement.googleapis.com/MonitoringPoint`  
Monitoring Point  |  A Monitoring Point in Cloud Network insights.   
`resource_container`: The identifier of the GCP resource container associated with this resource, such as "projects/123456789".   
`location`: The location of the Monitoring Point resource.   
`network_monitoring_provider_id`: Identifier of the network monitoring provider.   
`monitoring_point_id`: Identifier of the Monitoring Point.   
`networkmanagement.googleapis.com/NetworkPath`  
Network Path  |  A Network Path in Cloud Network insights.   
`resource_container`: The identifier of the GCP resource container associated with this resource, such as "projects/123456789".   
`location`: The location of the NetworkPath resource.   
`network_monitoring_provider_id`: Identifier of the network monitoring provider.   
`path_id`: Identifier of the network path.   
`networkmanagement.googleapis.com/WebPath`  
Web Path  |  A Web Path in Cloud Network insights.   
`resource_container`: The identifier of the GCP resource container associated with this resource, such as "projects/123456789".   
`location`: The location of the WebPath resource.   
`network_monitoring_provider_id`: Identifier of the network monitoring provider.   
`path_id`: Identifier of the web path.   
`networksecurity.googleapis.com/DnsThreatDetector`  
DNS Threat Detector  |  A GCP network and Cloud Region indicating the location where a DNS threat was detected.   
`resource_container`: The identifier of the GCP project for the threat event.   
`id`: ID of the DNS Threat Detector resource.   
`location`: The origin Cloud Region of the DNS query analyzed by Protective DNS.   
`networksecurity.googleapis.com/FirewallEndpoint`  
Firewall Endpoint  |  A Cloud Firewall Endpoint.   
`resource_container`: The identifier of the GCP organization or project owning the Firewall Endpoint.   
`location`: The zone of the Firewall Endpoint.   
`id`: The ID of the Firewall Endpoint.   
`networksecurity.googleapis.com/ProtectedEndpoint`  
Protected Network Endpoint  |  An endpoint (identified by IP) protected by Cloud Armor Managed Protection.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The region on which the protected endpoint resides, such as 'global' or 'us-central1'.   
`vip`: The virtual IP address of the protected endpoint. When multiple representations are possible, the IETF canonical representation (e.g., RFC 5952) is used.   
`networkservices.googleapis.com/Gateway`  
Gateway  |  A Gateway represents a single gateway resource.   
`resource_container`: The GCP container associated with the gateway.   
`location`: The region name in which the Gateway is defined.   
`network_name`: The name of the VPC network in which the Gateway was created.   
`gateway_type`: The type enum of the Gateway.   
`gateway_name`: The name of the Gateway resource.   
`networkservices.googleapis.com/MulticastDomain`  
Multicast Domain  |  A Cloud Multicast domain.   
`resource_container`: The project number of the multicast domain.   
`location`: Fixed to "global".   
`multicast_domain_id`: The user defined name of the multicast domain.   
`networkservices.googleapis.com/MulticastGroup`  
Multicast Group  |  Multicast Group.   
`resource_container`: The multicast administrator project number, prefixed by "projects/".   
`location`: Fixed to "global".   
`multicast_domain_id`: The user defined name of the multicast domain the group range is associated with.   
`multicast_group_range_id`: The user defined name of the multicast group range.   
`multicast_ip`: The IP address used in this multicast group.   
`networkservices.googleapis.com/WasmPluginVersion`  
Wasm Plugin Version  |  A single immutable version of a WasmPlugin (code + runtime config).   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The location of this service.   
`plugin_name`: The name of the WasmPlugin.   
`plugin_version`: The name of the WasmPluginVersion.   
`nodemanagement.googleapis.com/GoldkeyResource`  
Goldkey Resource  |  A Goldkey resource managed by the Builder stack.   
`resource_container`: The GCP project number owning the resource.   
`location`: The deployment location of the resource.   
`resource_id`: The unique ID of the resource.   
`resource_type`: Type of the resource.   
`oracledatabase.googleapis.com/AutonomousDatabase`  
Autonomous Database  |  Monitored resource representing a Autonomous Database.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud region in which the Autonomous database is running.   
`autonomous_database_id`: The identifier of the Autonomous database.   
`oracledatabase.googleapis.com/CloudExadataInfrastructure`  
Exadata Infrastructure  |  Monitored resource representing a Oracle Exadata infrastrucure.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud region in which the Exadata infrastrucure is running.   
`cloud_exadata_infrastructure_id`: The identifier of the CloudExadataInfrastructure resource.   
`oracledatabase.googleapis.com/CloudVmCluster`  
Cloud VM cluster  |  Monitored resource representing a Cloud VM Cluster in Oracle Exadata infrastrucure.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud region in which the cluster is running.   
`cloud_exadata_infrastructure_id`: The Cloud exadata infrastrucure id in which this cluster is hosted.   
`cloud_vm_cluster_id`: The identifier of the CloudVmCluster resource.   
`oracledatabase.googleapis.com/ContainerDatabase`  
Container Database  |  Monitored resource representing a Container Database in Cloud VM Cluster.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud region in which the cluster is running.   
`cloud_exadata_infrastructure_id`: The Cloud exadata infrastrucure id in which this cluster is hosted.   
`cloud_vm_cluster_id`: The identifier of the CloudVmCluster resource.   
`container_database_name`: Name of the ContainerDatabase.   
`oracledatabase.googleapis.com/DbSystem`  
Db System  |  Monitored resource representing a DbSystem.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud region in which the cluster is running.   
`db_system_id`: The identifier of the DbSystem resource.   
`oracledatabase.googleapis.com/DbSystemContainerDatabase`  
DbSystem Container Database  |  Monitored resource representing a DbSystem Container Database.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud region in which the cluster is running.   
`db_system_id`: The identifier of the CloudVmCluster resource.   
`container_database_name`: Name of the ContainerDatabase.   
`oracledatabase.googleapis.com/DbSystemPluggableDatabase`  
DbSystem Pluggable Database  |  Monitored resource representing a DbSystem Pluggable Database in a VM Cluster.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud region in which the cluster is running.   
`db_system_id`: The identifier of the CloudVmCluster resource.   
`container_database_name`: Name of the ContainerDatabase.   
`pluggable_database_name`: Name of the PluggableDatabase.   
`oracledatabase.googleapis.com/ExadbContainerDatabase`  
Exadb Container Database  |  Monitored resource representing a ExadbContainer Database in Cloud VM Cluster.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud region in which the cluster is running.   
`exadb_vm_cluster_id`: The identifier of the CloudVmCluster resource.   
`container_database_name`: Name of the ContainerDatabase.   
`oracledatabase.googleapis.com/ExadbPluggableDatabase`  
Exadb Pluggable Database  |  Monitored resource representing a Exadb Pluggable Database in a VM Cluster.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud region in which the cluster is running.   
`exadb_vm_cluster_id`: The identifier of the CloudVmCluster resource.   
`container_database_name`: Name of the ContainerDatabase.   
`pluggable_database_name`: Name of the PluggableDatabase.   
`oracledatabase.googleapis.com/ExadbVmCluster`  
ExaDB VM Cluster  |  Monitored resource representing an Exascale DB VM Cluster.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud region in which the cluster is running.   
`exadb_vm_cluster_id`: The identifier of the ExadbVmCluster resource.   
`oracledatabase.googleapis.com/ExascaleDbStorageVault`  
ExaDB Storage Vault  |  Monitored resource representing ExascaleDb Storage Vault.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud region in which the cluster is running.   
`exascale_db_storage_vault_id`: The identifier of the ExascaleDbStorageVault resource.   
`oracledatabase.googleapis.com/GoldengateDeployment`  
Goldengate Deployment  |  Monitored resource representing a Goldengate Deployment.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud region in which the deployment is running.   
`gg_deployment_id`: The identifier of the Goldengate Deployment resource.   
`oracledatabase.googleapis.com/PluggableDatabase`  
Pluggable Database  |  Monitored resource representing a Pluggable Database in a VM Cluster.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The Google Cloud region in which the cluster is running.   
`cloud_exadata_infrastructure_id`: The Cloud exadata infrastrucure id in which this cluster is hosted.   
`cloud_vm_cluster_id`: The identifier of the CloudVmCluster resource.   
`container_database_name`: Name of the ContainerDatabase.   
`pluggable_database_name`: Name of the PluggableDatabase.   
`organization`  
Google Organization  |  A Google Cloud Platform organization.   
`organization_id`: Numeric id of the organization.   
`produced_api`  
Produced API with consumer dimension  |  An API provided by the producer with consumer dimension.   
`project_id`: The identifier of the GCP project associated with this resource, such as 'my-project'.   
`service`: The API service name, such as 'cloudsql.googleapis.com'.   
`method`: The API method name, such as 'disks.list'.   
`version`: The API version, such as 'v1'.   
`location`: The service specific notion of location. This can be a name of a zone or region. If a service does not have any notion of zones then 'global' can be used.   
`consumer_id`: This is the ID of a consumer project that's made a request to the API, such as project number '412016889367'.   
`project`  
Google Project  |  A Google project.   
`project_id`: The identifier of the GCP project associated with this resource (e.g., my-project).   
`pubsub_snapshot`  
Cloud Pub/Sub Snapshot  |  A snapshot in Google Cloud Pub/Sub.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`snapshot_id`: The identifier of the snapshot, such as "my-snapshot".   
`pubsub_subscription`  
Cloud Pub/Sub Subscription  |  A subscription in Google Cloud Pub/Sub.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`subscription_id`: The identifier of the subscription, such as "my-subscription".   
`pubsub_topic`  
Cloud Pub/Sub Topic  |  A topic in Google Cloud Pub/Sub.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`topic_id`: The identifier of the topic, such as "my-topic".   
`recaptchaenterprise.googleapis.com/Key`  
reCAPTCHA Key  |  Monitoring resource for reCAPTCHA Key.   
`resource_container`: The ID of the GCP project associated with this reCAPTCHA Key.   
`location`: Location where the reCAPTCHA Key is provisioned.   
`key_id`: The ID for this Key.   
`recommender`  
Recommender  |  A Recommender represents a grouping of similar recommendations.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`recommender_id`: The name of the recommender.   
`location`: The location of the recommendation.   
`recommender_insight_type`  
InsightType  |  An InsightType represents a grouping of similar insights.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`insight_type_id`: The resource ID of the insight type.   
`location`: The location of the insight.   
`redis_instance`  
Cloud Memorystore Redis Instance  |  A Redis instance hosted on Google Cloud Memorystore.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`region`: The Google Cloud region in which the managed instance is running.   
`instance_id`: The ID of the managed instance.   
`node_id`: The ID of a Redis node within the managed instance.   
`remotebuild_instance`  
Remote Build Execution Instance  |  A specific instance for the Remote Build Execution service.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The Cloud zone of the instance.   
`instance_id`: The specific instance within the Remote Build Execution consumer project.   
`reported_errors`  
Reported Errors  |  Error data and metadata managed by Stackdriver Error Reporting   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`saasservicemgmt.googleapis.com/Rollout`  
App Lifecycle Manager Rollout  |  A Rollout of an App Lifecycle Manager Tenant.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The region in which this rollout occurred.   
`rollout_id`: ID associated with this rollout.   
`saasservicemgmt.googleapis.com/Unit`  
App Lifecycle Manager Unit  |  A Unit within an App Lifecycle Manager Tenant.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The location of the GCP project associated with this resource.   
`unit_id`: The ID of the Unit.   
`secretmanager.googleapis.com/Secret`  
Secret Manager Secret  |  A logical secret whose value and versions can be accessed.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: Location of secret metadata. Always global for v1.   
`secret_id`: The name given to this secret.   
`sensitiveaction.googleapis.com/Location`  
Location  |  A GCP resource container where a sensitive action was observed.   
`resource_container`: The GCP resource container where the sensitive action was observed.   
`location`: The location where the sensitive action was observed.   
`service_account`  
Service Account  |  A service account.   
`project_id`: The identifier of the GCP project associated with this resource (e.g., my-project).   
`email_id`: The service account email id, e.g. "account123@proj123.iam.gserviceaccount.com".   
`unique_id`: The unique id of the service account, e.g. "113948692397867021414".   
`service_config`  
Service Configuration  |  A specific service configuration.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`service_name`: The name of the service.   
`service_config_id`: The id of the service configuration.   
`service_rollout`  
Service Rollout  |  A resource type used to describe how a service configuration is deployed to backend systems.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`service_name`: The name of the service.   
`rollout_id`: The id of the service rollout.   
`servicedirectory_namespace`  
Service Directory Namespace  |  A namespace in the Service Directory service.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The cloud region of the Service Directory namespace.   
`namespace_name`: The name of the Service Directory namespace.   
`servicedirectory_service`  
Service Directory Service  |  A Service Directory service.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The cloud region of the Service Directory service.   
`namespace_name`: The name of the Service Directory namespace.   
`service_name`: The name of the Service Directory service.   
`servicehealth.googleapis.com/Artifact`  
Artifact  |  An Artifact in service health.   
`resource_container`: The GCP project number.   
`location`: The GCP location that serves the API for the given artifact.   
`artifact_id`: The artifact ID.   
`servicehealth.googleapis.com/Event`  
Event  |  An Event in service health.   
`resource_container`: The GCP project number.   
`location`: The GCP location that serves the API for the given event.   
`event_id`: The event ID.   
`serviceusage_service`  
Service  |  A service activated or deactivated by a consumer project.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`service_name`: The name of the service.   
`serviceuser_service`  
Service  |  A service activated or deactivated by a consumer project.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`service_name`: The name of the service.   
`spanner_instance`  
Cloud Spanner Instance  |  A Cloud Spanner instance.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`instance_id`: An immutable identifier for an instance.   
`location`: Cloud Spanner region.   
`instance_config`: Instance config for the instance.   
`storage.googleapis.com/Client`  
GCS Client  |  A Google Cloud Storage (GCS) client.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The location parsed from `cloud.region`.   
`cloud_platform`: The cloud platform on which the GCS client runs.   
`host_id`: The ID of the host (usually a VM) on which the GCS client runs.   
`instance_id`: An UUID auto-generated by the client for the identification purpose.   
`api`: The API used for communication. The available values are GRPC, JSON, and XML.   
`storage_transfer_job`  
Cloud Storage Transfer Job  |  A Google Cloud storage transfer job.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`job_id`: A unique name of the storage transfer job.   
`stream.googleapis.com/StreamInstance`  
Stream Instance  |  A service instance that streams a single source of Content. .   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The region of the runtime.   
`stream_instance_id`: The identifier of the stream instance.   
`tcp_ssl_proxy_rule`  
Global External Proxy Network Load Balancer Rule  |  A set of definitions for TCP/SSL proxy behavior.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`region`: The region on which TCP/SSL proxy is applied, such as 'global' or 'us-central1'. Various other objects are defined per that locality.   
`backend_target_name`: The name of the backend target ('backend service', equivalent to 'proxy name').   
`backend_target_type`: The type of the backend target. Can only be 'BACKEND_SERVICE' currently.   
`forwarding_rule_name`: The name of the forwarding rule.   
`target_proxy_name`: The name of the target TCP/SSL proxy.   
`backend_name`: The name of the backend group.   
`backend_type`: The type of the backend group. Can be 'INSTANCE_GROUP' or 'NETWORK_ENDPOINT_GROUP'.   
`backend_scope`: The scope (zone or region) of the backend group.   
`backend_scope_type`: The type of the scope of the backend group. Can be either 'ZONE' or 'REGION'.   
`testservice_matrix`  
Test Matrix  |  A Test Matrix in the Google Cloud Test Lab service.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`matrix_id`: Unique identifier of the matrix.   
`threat_detector`  
Threat Detector  |  A detector in the Threat Detection service.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`detector_name`: The specific detector that triggered the alert.   
`tpu_worker`  
TPU Worker  |  A TPU Worker executing Tensorflow work for a TPU Node.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`zone`: The Google Cloud zone in which the TPU Worker is running.   
`node_id`: The ID of the TPU Node.   
`worker_id`: The ID of a TPU Worker within the TPU Node.   
`transferappliance.googleapis.com/Appliance`  
Transfer Appliance  |  Transfer Appliance is a way for Google Cloud Customers to transfer data to GCS.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The region in which the appliance was provisioned in (e.g. us-central1).   
`appliance_id`: The unique id of the appliance.   
`uptime_url`  
Uptime Check URL  |  An Uptime Monitoring check against a custom URL.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`host`: The hostname or IP address of the check.   
`videostitcher.googleapis.com/Project`  
Video Stitcher API Project  |  A Video Stitcher API Project.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The GCP location where the project resource resides.   
`visionai.googleapis.com/Application`  
Application  |  A Vertex AI Vision application.   
`resource_container`: The identifier of the GCP project associated with this resource.   
`location`: The GCP location in which this application resides.   
`application_id`: The identifier of the application.   
`vmmigration.googleapis.com/MigratingVM`  
Migrate to Virtual Machines Migrating VM  |  A Migrate to Virtual Machines Migrating VM.   
`resource_container`: The identifier of the GCP project associated with this VM resource.   
`location`: The GCP location where the VM resource resides.   
`source`: The source where the VM resource resides.   
`vm`: The VM ID.   
`vmmigration.googleapis.com/Source`  
Migrate to Virtual Machines Source  |  A Migrate to Virtual Machines Source.   
`resource_container`: The identifier of the GCP project associated with this source resource.   
`location`: The GCP location where the source resource resides.   
`source`: The source ID.   
`vpc_access_connector`  
VPC Access Connector  |  A connector that can communicate with devices within a VPC.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`location`: The region the connector is located in.   
`connector_name`: The name of the connector.   
`vpc_flow_logs_config`  
VPC Flow Logs Config  |  A VPC Flow Logs configuration.   
`resource_container`: The identifier of the GCP resource container associated with this resource, such as \"projects/123\" or \"organizations/123\"   
`name`: The unique name of the configuration within a project or organization. This refers to the config name alone, not the entire config path.   
`location`: This is a global resource, so this field holds a static value of \"global\".   
`vpn_gateway`  
Cloud VPN Gateway  |  A Cloud VPN gateway.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`gateway_id`: The VPN Gateway ID.   
`region`: The region in which the VPN Gateway is running.   
`vpn_tunnel`  
Cloud VPN Tunnel  |  A Cloud VPN tunnel.   
`project_id`: The identifier of the GCP project associated with this resource, such as "my-project".   
`tunnel_id`: The unique numerical identifier of the VPN tunnel.   
`tunnel_name`: The unique user provided name of the VPN tunnel.   
`location`: Location of the Cloud VPN Tunnel.   
`workflows.googleapis.com/Workflow`  
Workflow  |  A Workflows specification of steps to execute.   
`resource_container`: The identifier of the GCP container associated with the resource.   
`location`: The region in which the workflow is deployed.   
`workflow_id`: The ID of the workflow.   
  
This list of monitored-resource types was last generated at 2026-10-22 02:17:28 UTC.

## Mappings for Logging-only resources

For log-based metrics to be ingested by Monitoring, the metrics must be mapped to a monitored-resource type supported by Monitoring. The mappings are also required to view corresponding logs from a Monitoring chart or alert.

In many cases, Logging and Monitoring use the same monitored-resource types. However, for certain monitored-resource types in Logging, there is no corresponding type in Monitoring. In these cases, the Logging resource types are mapped to an existing Monitoring type.

### Mappings to `global`

The following monitored-resource types in Logging map to the [`global`](https://docs.cloud.google.com/monitoring/api/resources#tag_global) type in Monitoring:

**Note:** The `global` monitored-resource type only contains the `project_id` label. Any labels in the Cloud Logging monitored-resource type are not available in the corresponding log-based metric.

  * `bigquery_resource`
  * `billing_account`
  * `client_auth_config_brand`
  * `client_auth_config_client`
  * `cloud_debugger_resource`
  * `cloudkms_cryptokey`
  * `cloudkms_cryptokeyversion`
  * `cloudkms_keyring`
  * `datastore_database`
  * `datastore_index`
  * `deployment`
  * `deployment_manager_manifest`
  * `deployment_manager_operation`
  * `deployment_manager_resource`
  * `deployment_manager_type`
  * `folder`
  * `gce_autoscaler`
  * `gce_backend_bucket`
  * `gce_backend_service`
  * `gce_client_ssl_policy`
  * `gce_commitment`
  * `gce_firewall_rule`
  * `gce_forwarding_rule`
  * `gce_health_check`
  * `gce_image`
  * `gce_instance_group`
  * `gce_instance_group_manager`
  * `gce_instance_template`
  * `gce_license`
  * `gce_network`
  * `gce_operation`
  * `gce_packet_mirroring`
  * `gce_project`
  * `gce_reserved_address`
  * `gce_route`
  * `gce_router`
  * `gce_snapshot`
  * `gce_ssl_certificate`
  * `gce_target_http_instance`
  * `gce_target_http_proxy`
  * `gce_target_https_proxy`
  * `gce_target_pool`
  * `gce_target_ssl_proxy`
  * `gce_url_map`
  * `genomics_dataset`
  * `genomics_operation`
  * `gke_cluster`
  * `gke_nodepool`
  * `iam_role`
  * `logging_log`
  * `managed_service`
  * `ml_job`
  * `organization`
  * `project`
  * `reported_errors`
  * `service_account`
  * `service_config`
  * `service_rollout`
  * `serviceusage_service`
  * `serviceuser_service`
  * `testservice_matrix`
  * `vpn_tunnel`
  * `firebaserules_ruleset`
  * `firebaserules_release`



### Mappings to other Cloud Monitoring resource types

The following monitored-resource types in Logging map to a resource type other than [`global`](https://docs.cloud.google.com/monitoring/api/resources#tag_global) in Monitoring:

Logging monitored-resource type | Monitoring monitored-resource type | Label mappings  
---|---|---  
[`dataflow_step`](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#tag_dataflow_step) | [`dataflow_job`](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job) | 

  * `project_id` maps to `project_id`.
  * `job_id` does not exist in Monitoring.
  * `step_id` does not exist in Monitoring.
  * `job_name` maps to `job_name`.
  * `region` maps to `region`.

  
[`container`](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#tag_container) **Note:** Both `container` and its Cloud Monitoring monitored-resource type `gke_container` are deprecated. Newer container logs use `k8s_container`. | [`gke_container`](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container) | Labels match exactly.  
[`http_load_balancer`](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#tag_http_load_balancer) | [`l7_lb_rule`](https://docs.cloud.google.com/monitoring/api/resources#tag_l7_lb_rule) **Note:** The `l7_lb_rule` monitored-resource type is only used by log-based metrics. Other load balancer system metrics use the monitored-resource type [`https_lb_rule`](https://docs.cloud.google.com/monitoring/api/resources#tag_https_lb_rule). | 

  * `project_id` maps to `project_id`.
  * `forwarding_rule_name` maps to `forwarding_rule_name`.
  * `url_map_name` maps to `url_map_name`.
  * `target_proxy_name` maps to `target_proxy_name`.
  * `backend_service_name` maps to `backend_name`.
  * `zone` does not exist in Monitoring.
  * All other labels are empty in Monitoring.

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
