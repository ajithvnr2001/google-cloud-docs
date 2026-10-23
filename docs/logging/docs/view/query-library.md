---
url: https://docs.cloud.google.com/logging/docs/view/query-library/
title: Sample queries \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:02.408943+00:00
---

# Sample queries  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/view/query-library/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Sample queries Stay organized with collections  Save and categorize content based on your preferences. 

This document provides you with suggested queries to make it easier to find important logs using the Logs Explorer in the Google Cloud console. The listed queries are written in the [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language), and they can be used in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries), the [Logging API](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list), or the [command-line interface](https://docs.cloud.google.com/logging/docs/api/gcloud-logging#v2_api_commands).

The Logs Explorer uses Boolean expressions to specify a subset of all the log entries in your project. You can use these queries to choose log entries from specific logs or log services, or that satisfy conditions on metadata or user-defined fields.

## Before you begin

Ensure that you have the correct Identity and Access Management permissions or roles for building queries using the Logs Explorer. For details on the necessary IAM permissions, see [Permissions for the Google Cloud console](https://docs.cloud.google.com/logging/docs/access-control#console_permissions).

## Get started

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select the appropriate Google Cloud project or other Google Cloud resource for which you want to view logs.




## Use the sample queries

To apply a query from the following tables, click the _content_copy_ **Content Copy** icon for the expression, and then paste the copied expression into the Logs Explorer query-editor field.

The following screenshot illustrates the query pane:

![The query editor is showing where to enter a query](https://docs.cloud.google.com/static/logging/docs/images/query-pane-2.png)

If you don't see the query-editor field, enable **Show query**.

After you review your query expression, click **Run query**. Logs that match your query are listed under **Query results**.

Some of the queries listed later on this page include variables that you should replace with valid values. For example, when a query includes `logName`, then the PROJECT_ID you supply must refer to the selected Google Cloud project; otherwise, the query won't work.

Note the following:

  * If you have a query with a timestamp, then the [time-range selector](https://docs.cloud.google.com/logging/docs/view/building-queries#time-range) is disabled, and the query uses the timestamp expression as its time-range restriction. If a query doesn't use a timestamp expression, then the query uses the time-range selector as its time-range restriction.

  * The length of a query can't exceed 20,000 characters.

  * The [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language) is case-insensitive, with the exception of regular expressions.

  * You can use the `log_id` function for queries with a `log_name` expression. For example, the expression `log_name="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fdata_access"` is the same as `log_id("cloudaudit.googleapis.com/data_access")`. For more information about the `log_id` function, see [Logging query language: Functions](https://docs.cloud.google.com/logging/docs/view/logging-query-language#functions).




For instructions about querying in the Google Cloud console, see [Build queries in the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries).

The following sections group queries by Google Cloud services.

## App Engine queries

Query/filter name | Expression  
---|---  
App Engine logs from New Year's Eve (in UTC time) | 
    
    
    resource.type="gae_app" AND
    severity>=ERROR AND
    timestamp>="2018-12-31T00:00:00Z" AND timestamp<="2019-01-01T00:00:00Z"   
  
App Engine request logs with server errors | 
    
    
    resource.type="gae_app" AND
    log_id("appengine.googleapis.com/request_log") AND
    httpRequest.status>=500   
  
Sampled HTTP error logs | 
    
    
    resource.type="gae_app" AND
    protoPayload.status >= 400 AND
    sample(insertId, 0.1)   
  
Search for App Engine trace ID | 
    
    
    resource.type="gae_app" AND
    trace="projects/PROJECT_ID/traces/TRACE_ID"   
  
App Engine logs | 
    
    
    resource.type="gae_app" AND
    resource.labels.module_id="MODULE_ID" AND
    resource.labels.version_id="VERSION_ID"   
  
Recent App Engine deployments | 
    
    
    resource.type="gae_app" AND
    protoPayload.@type="type.googleapis.com/google.cloud.audit.AuditLog" AND
    protoPayload.serviceName="appengine.googleapis.com"   
  
## API enable and disable queries

Query/filter name | Expression  
---|---  
Audit API enable logs  | 
    
    
    protoPayload.methodName="google.api.serviceusage.v1.ServiceUsage.EnableService"  
  
Audit API disable logs  | 
    
    
    protoPayload.methodName="google.api.serviceusage.v1.ServiceUsage.DisableService"  
  
## BigQuery queries

Query/filter name | Expression  
---|---  
BigQuery audit logs | 
    
    
    resource.type=("bigquery_dataset" OR "bigquery_project") AND
    logName:"cloudaudit.googleapis.com"   
  
BigQuery audit logs for a project | 
    
    
    resource.type="bigquery_project" AND
    logName:"cloudaudit.googleapis.com"   
  
BigQuery audit logs for a dataset | 
    
    
    resource.type="bigquery_dataset" AND
    logName:"cloudaudit.googleapis.com"   
  
BigQuery audit logs for BI Engine Model | 
    
    
    resource.type="bigquery_biengine_model" AND
    logName:"cloudaudit.googleapis.com"   
  
BigQuery audit logs for a Data Transfer Service Run. | 
    
    
    resource.type="bigquery_dts_run" AND
    logName:"cloudaudit.googleapis.com"   
  
BigQuery audit logs for a Data Transfer Service configuration. | 
    
    
    resource.type="bigquery_dts_config" AND
    logName:"cloudaudit.googleapis.com"   
  
BigQuery data transfer service jobs  | 
    
    
    resource.type="bigquery_project" AND
    protoPayload.requestMetadata.callerSuppliedUserAgent=
    "BigQuery Data Transfer Service" AND
    protoPayload.methodName=("google.cloud.bigquery.v2.JobService.InsertJob" OR
    "google.cloud.bigquery.v2.JobService.Query")   
  
BigQuery transfer run logs | 
    
    
    resource.type="bigquery_dts_config" AND
    labels.run_id="RUN_ID" AND
    resource.labels.config_id="CONFIG_ID"   
  
BigQuery dataset updates  | 
    
    
    resource.type="bigquery_dataset" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName=
    "google.cloud.bigquery.v2.DatasetService.UpdateDataset"   
  
BigQuery jobs completed  | 
    
    
    resource.type="bigquery_project" AND
    log_id("cloudaudit.googleapis.com/data_access") AND
    protoPayload.methodName=("google.cloud.bigquery.v2.JobService.InsertJob"
    OR "google.cloud.bigquery.v2.JobService.Query")   
  
BigQuery large queries  | 
    
    
    resource.type="bigquery_project" AND
    protoPayload.metadata.jobChange.job.jobStats.queryStats.totalBilledBytes
    > 1073741824   
  
BigQuery quota exceeded  | 
    
    
    resource.type=("bigquery_dataset" OR "bigquery_project")
    AND
    protoPayload.status.code=8 AND
    severity>=WARNING   
  
BigQuery query started  | 
    
    
    resource.type="bigquery_project" AND
    protoPayload.metadata.jobInsertion.reason:*  
  
BigQuery concurrent load/extract jobs | 
    
    
    resource.type="bigquery_resource" AND
    protoPayload.methodName="jobservice.insert" AND
    protoPayload.serviceData.jobInsertRequest.resource.jobConfiguration.query.query:
    "extract"  
  
BigQuery audit logs for Row Access Policy | 
    
    
    protoPayload.methodName="jobservice.insert" AND
    protoPayload.serviceData.jobInsertRequest.resource.jobConfiguration.query.query:"ROW ACCESS POLICY"  
  
## Dataflow queries

Query/filter name | Expression  
---|---  
Errors and warnings in Dataflow workers  | 
    
    
    resource.type="dataflow_step" AND
    log_id("dataflow.googleapis.com/worker") AND
    severity>=WARNING   
  
## Managed Service for Apache Spark queries

Query/filter name | Expression  
---|---  
Dataproc Apache Hadoop logs  | 
    
    
    resource.type="cloud_dataproc_cluster" AND
    jsonPayload.class:"org.apache.hadoop.mapreduce"   
  
## Cloud Deployment Manager

Query/filter name | Expression  
---|---  
Deployment Manager errors  | 
    
    
    resource.type="deployment" AND
    severity>=ERROR   
  
## Cloud Run functions queries

Query/filter name | Expression  
---|---  
Cloud function errors  | 
    
    
    resource.type="cloud_function" AND
    log_id("cloudfunctions.googleapis.com/cloud-functions") AND
    severity>=ERROR   
  
## Cloud Monitoring queries

Query/filter name | Expression |  Show all notification channel  
errors  | 
    
    
    resource.type="stackdriver_notification_channel" AND
    severity>=ERROR   
  
---|---  
Show notification channel  
errors due to throttling  | 
    
    
    resource.type="stackdriver_notification_channel" AND
    severity>=ERROR AND
    jsonPayload.summary="Notification delivery throttled."  
  
Show logs written by  
the uptime resource | 
    
    
    resource.type="uptime_url"  
  
Show requests received from  
the uptime-check service | 
    
    
    "GoogleStackdriverMonitoring-UptimeChecks"  
  
## Cloud Run queries

Query/filter name | Expression  
---|---  
Cloud Run logs for a specific job  | 
    
    
    resource.type="cloud_run_job" AND
    resource.labels.job_name="JOB_NAME"  
  
Cloud Run logs for a specific revision and service  | 
    
    
    resource.type="cloud_run_revision" AND
    resource.labels.service_name="SERVICE_NAME"  
  
## Cloud Source Repositories queries

Query/filter name | Expression  
---|---  
Cloud Source Repository logs  | 
    
    
    resource.type="csr_repository" AND
    resource.labels.name="REPOSITORY_NAME"  
  
## Spanner queries

Query/filter name | Expression  
---|---  
Cloud Spanner logs for a specific spanner instance  | 
    
    
    resource.type="spanner_instance" AND
    resource.labels.instance_id="SPANNER_INSTANCE"  
  
## Cloud SQL queries

Query/filter name | Expression  
---|---  
Cloud SQL audit logs  | 
    
    
    resource.type="cloudsql_database" AND
    resource.labels.database_id="DATABASE_ID" AND
    log_id("cloudaudit.googleapis.com/activity")  
  
Cloud SQL MySQL error logs  | 
    
    
    resource.type="cloudsql_database" AND
    log_id("cloudsql.googleapis.com/mysql.err")  
  
Cloud SQL MySQL-based databases  | 
    
    
    resource.type="cloudsql_database" AND
    resource.labels.database_id="DATABASE_ID" AND
    log_id("cloudsql.googleapis.com/mysql")  
  
Cloud SQL Postgres-based databases  | 
    
    
    resource.type="cloudsql_database" AND
    resource.labels.database_id="DATABASE_ID" AND
    log_id("cloudsql.googleapis.com/postgres.log")  
  
Cloud SQL SQL Server error logs  | 
    
    
    resource.type="cloudsql_database" AND
    log_id("cloudsql.googleapis.com/sqlserver.err")  
  
Cloud SQL SQL Server-based databases  | 
    
    
    resource.type="cloudsql_database" AND
    resource.labels.database_id="DATABASE_ID" AND
    log_id("cloudsql.googleapis.com/sqlagent.out")  
  
## Cloud Storage queries

Query/filter name | Expression  
---|---  
GCS bucket logs  | 
    
    
    resource.type="gcs_bucket" AND
    resource.labels.bucket_name="BUCKET_NAME"  
  
GCS bucket audit logs  | 
    
    
    resource.type="gcs_bucket" AND
    logName:"cloudaudit.googleapis.com"   
  
GCS bucket creation logs  | 
    
    
    resource.type="gcs_bucket" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName="storage.buckets.create"   
  
GCS bucket deletion logs  | 
    
    
    resource.type="gcs_bucket" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName="storage.buckets.delete"   
  
## Cloud Tasks queries

Query/filter name | Expression  
---|---  
Cloud Tasks queue logs  | 
    
    
    resource.type="cloud_tasks_queue" AND
    resource.labels.queue_id="QUEUE_ID"  
  
## Compute Engine queries

Query/filter name | Expression  
---|---  
Compute Engine Admin Activity logs  | 
    
    
    resource.type="gce_instance" AND
    log_id("cloudaudit.googleapis.com/activity")  
  
Compute Engine firewall rule deletion  | 
    
    
    resource.type="gce_firewall_rule" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName:"firewalls.delete"   
  
Compute Engine VM syslogs  | 
    
    
    resource.type="gce_instance" AND
    log_id("syslog")   
  
Compute Engine VM authlogs  | 
    
    
    resource.type="gce_instance" AND
    log_id("authlog")   
  
Compute Engine Host Error  | 
    
    
    resource.type="gce_instance"
    protoPayload.serviceName="compute.googleapis.com"
    (protoPayload.methodName:"compute.instances.hostError"
    OR
    operation.producer:"compute.instances.hostError")
    log_id("cloudaudit.googleapis.com/system_event")
    resource.labels.instance_id="INSTANCE_ID"
     severity=INFO
          
  
Compute Engine Host Memory Alert  | 
    
    
    resource.type="gce_instance" AND
    protoPayload.serviceName="compute.googleapis.com" AND
    (jsonPayload.methodName:"compute.instances.host_event_notify"
    OR
    operation.producer:"compute.instances.host_event_notify") AND
    log_id("cloudaudit.googleapis.com/host_event_notify") AND
    resource.labels.instance_id="INSTANCE_ID" AND
    severity=CRITICAL
          
  
Compute Engine Host Migrated  | 
    
    
    resource.type="gce_instance"
    protoPayload.serviceName="compute.googleapis.com"
    (protoPayload.methodName:
    "compute.instances.migrateOnHostMaintenance"
    OR
    operation.producer:
    "compute.instances.migrateOnHostMaintenance")
    log_id("cloudaudit.googleapis.com/system_event")
    resource.labels.instance_id="INSTANCE_ID"
    severity=INFO   
  
Compute Engine VM Terminated/Preempted  | 
    
    
    resource.type="gce_instance"
    protoPayload.methodName=~"compute\.instances\.(guestTerminate|preempted)"
    log_id("cloudaudit.googleapis.com/system_event")
    resource.labels.instance_id="INSTANCE_ID"   
  
Compute Engine VM terminated due to Scratch Disk Creation Failure  | 
    
    
    resource.type="gce_instance"
    protoPayload.serviceName="compute.googleapis.com"
    (protoPayload.methodName="compute.instances.scratchDiskCreationFailed"
    OR
    operation.producer:
    "compute.instances.scratchDiskCreationFailed")
    log_id("cloudaudit.googleapis.com/system_event")
    resource.labels.instance_id="INSTANCE_ID"
    severity=INFO   
  
Compute Engine VM Instance Created  | 
    
    
    resource.type="gce_instance"
    protoPayload.methodName:"compute.instances.insert"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.request.name="INSTANCE_NAME"   
  
Compute Engine VM Instance Deleted with Name | 
    
    
    resource.type="gce_instance"
    protoPayload.methodName:"compute.instances.delete"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.resourceName:"INSTANCE_NAME"   
  
Compute Engine VM Instance Deleted with ID | 
    
    
    resource.type="gce_instance"
    protoPayload.methodName:"compute.instances.delete"
    log_id("cloudaudit.googleapis.com/activity")
    resource.labels.instance_id="INSTANCE_ID"   
  
Compute Engine VM Instance Restarted  | 
    
    
    resource.type="gce_instance"
    protoPayload.methodName=~"compute\.instances\.(
    stop|reset|automaticRestart|guestTerminate|
    instanceManagerHaltForRestart)"
    (log_id("cloudaudit.googleapis.com/activity")
    OR log_id("cloudaudit.googleapis.com/system_event"))
    resource.labels.instance_id="INSTANCE_ID"   
  
Compute Engine Shielded VM Boot Integrity Failure  | 
    
    
    resource.type="gce_instance"
    log_id("compute.googleapis.com/shielded_vm_integrity")
    jsonPayload.earlyBootReportEvent.policyEvaluationPassed="false"
    resource.labels.instance_id="INSTANCE_ID"   
  
Compute Engine VM instance stopped by Guest OS  | 
    
    
    resource.type="gce_instance"
    protoPayload.serviceName="compute.googleapis.com"
    (protoPayload.methodName:"compute.instances.guestTerminate" OR
    operation.producer:"compute.instances.guestTerminate")
    log_id("cloudaudit.googleapis.com/system_event")
    resource.labels.instance_id="INSTANCE_ID"
    severity=INFO   
  
Compute Engine Shielded VM boot file was blocked  | 
    
    
    resource.type="gce_instance"
    log_id("serialconsole.googleapis.com/serial_port_1_output")
    textPayload:"Security Violation"
    resource.labels.instance_id="INSTANCE_ID"   
  
Persistent Disk Created  | 
    
    
    resource.type="gce_disk" AND
    protoPayload.methodName:"compute.disks.insert" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.resourceName: "PERSISTENT_DISK_NAME"  
  
Nodes added in Sole Tenant Node  | 
    
    
    resource.type="gce_node_group"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.methodName=~("compute.nodeGroups.addNodes"
    OR "compute.nodeGroups.insert")
    resource.labels.node_group_id="NODE_GROUP_ID"
    severity=INFO  
  
Autoscale events in Sole Tenant Node  | 
    
    
    resource.type="gce_node_group"
    log_id("cloudaudit.googleapis.com/system_event")
    protoPayload.methodName=~("compute.nodeGroups.deleteNodes"
    OR "compute.nodeGroups.addNodes")
    resource.labels.node_group_id="NODE_GROUP_ID"  
  
Manual Snapshot Taken  | 
    
    
    resource.type="gce_snapshot"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.methodName:"compute.snapshots.insert"
    protoPayload.resourceName:"SNAPSHOT_NAME"  
  
Scheduled Snapshot Taken | 
    
    
    resource.type="gce_disk"
    log_id("cloudaudit.googleapis.com/system_event")
    protoPayload.methodName="ScheduledSnapshots"
    protoPayload.response.operationType="createSnapshot"
    protoPayload.response.targetLink="PERSISTENT_DISK_NAME"  
  
Snapshot Schedule Created  | 
    
    
    resource.type="gce_resource_policy"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.methodName:"compute.resourcePolicies.insert"
    protoPayload.request.name="SCHEDULE_NAME"  
  
Snapshot Schedule Attached  | 
    
    
    resource.type="gce_disk"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.methodName:"compute.disks.addResourcePolicies"
    protoPayload.request.resourcePolicys:"SCHEDULE_NAME"
    protoPayload.resourceName:"PERSISTENT_DISK_NAME"  
  
Quota Exceeded  | 
    
    
    resource.type="gce_instance"
    protoPayload.methodName:"compute.instances.insert"
    protoPayload.status.message:"QUOTA_EXCEEDED"
    severity=ERROR  
  
Query unhealthy instances in instance group | 
    
    
    resource.type="gce_instance_group"
    resource.labels.instance_group_name="INSTANCE_GROUP_NAME"
    jsonPayload.healthCheckProbeResult.healthState="UNHEALTHY"  
  
Query instance group members within a time frame in UTC time format | 
    
    
    resource.type="gce_instance_group_manager"
    resource.labels.instance_group_manager_name="INSTANCE_GROUP_NAME"
    jsonPayload.@type=
    "type.googleapis.com/compute.InstanceGroupManagerEvent"
    jsonPayload.instanceHealthStateChange.detailedHealthState="HEALTHY"
    timestamp >= START_TIME timestamp <= END_TIME   
  
Instances added to Instance Group  | 
    
    
    resource.type="gce_instance_group"
    protoPayload.methodName:"compute.instanceGroups.addInstances"
    log_id("cloudaudit.googleapis.com/activity")
    resource.labels.instance_group_name="INSTANCE_GROUP_NAME"  
  
Instances removed from Instance Group  | 
    
    
    resource.type="gce_instance_group"
    protoPayload.methodName:"compute.instanceGroups.removeInstances"
    log_id("cloudaudit.googleapis.com/activity")
    resource.labels.instance_group_name="INSTANCE_GROUP_NAME"  
  
Instance template set or updated | 
    
    
    resource.type="gce_instance_group_manager"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.methodName=
    "v1.compute.instanceGroupManagers.setInstanceTemplate"
    resource.labels.instance_group_manager_name="INSTANCE_GROUP_MANAGER"  
  
Firewall rule deleted  | 
    
    
    resource.type="gce_firewall_rule"
    log_id("cloudaudit.googleapis.com/activity")
    protoPayload.methodName:"firewalls.delete"  
  
Firewall logs  | 
    
    
    resource.type="gce_subnetwork"
    log_id("compute.googleapis.com/firewall")
    jsonPayload.instance.vm_name="INSTANCE_NAME"  
  
## Google Cloud Observability queries

Query/filter name | Expression  
---|---  
Log sink activities  | 
    
    
    resource.type="logging_sink" AND
    log_id("cloudaudit.googleapis.com/activity")  
  
Log-based metric create or update activities  | 
    
    
    resource.type="metric" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName:(UpdateLogMetric OR CreateLogMetric)  
  
Uptime URL checks for a host  | 
    
    
    resource.type="uptime_url" AND
    resource.labels.host="URL"  
  
## Identity and Access Management queries

Query/filter name | Expression  
---|---  
Service account creation logs  | 
    
    
    resource.type="service_account" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName="google.iam.admin.v1.CreateServiceAccount"   
  
Service account creation key logs  | 
    
    
    resource.type="service_account" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName="google.iam.admin.v1.CreateServiceAccountKey"   
  
Set access control policy logs  | 
    
    
    resource.type="project" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName="SetIamPolicy"   
  
External principal granted access to organization  | 
    
    
    resource.type="project" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.@type="type.googleapis.com/google.cloud.audit.AuditLog" AND
    protoPayload.request.@type:"IamPolicy" AND
    protoPayload.serviceData.policyDelta.bindingDeltas.member:* AND
    NOT protoPayload.serviceData.policyDelta.bindingDeltas.member:"@DOMAIN_NAME.com"   
  
Resource creation, modification, or deletion | 
    
    
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName:("create" OR "delete" OR "update")  
  
Role granted to principal | 
    
    
    log_id("cloudaudit.googleapis.com/activity") AND
    resource.type="project" AND
    protoPayload.serviceName="cloudresourcemanager.googleapis.com" AND
    protoPayload.methodName="SetIamPolicy" AND
    protoPayload.serviceData.policyDelta.bindingDeltas.action="Add" AND
    protoPayload.serviceData.policyDelta.bindingDeltas.member:"EMAIL_ID"   
  
Role removed from principal  | 
    
    
    log_id("cloudaudit.googleapis.com/activity") AND
    resource.type="project" AND
    protoPayload.serviceName="cloudresourcemanager.googleapis.com" AND
    protoPayload.methodName="SetIamPolicy" AND
    protoPayload.serviceData.policyDelta.bindingDeltas.action="Remove" AND
    protoPayload.serviceData.policyDelta.bindingDeltas.member:"EMAIL_ID"   
  
Permission updated in a custom role  | 
    
    
    log_id("cloudaudit.googleapis.com/activity") AND
    resource.type="iam_role" AND
    protoPayload.serviceName="iam.googleapis.com" AND
    protoPayload.methodName:"UpdateRole" AND
    resource.labels.role_name:"ROLE_ID"   
  
## Kubernetes-related queries

For an overview and examples of Admin Activity audit log queries, see those provided on the [GKE Audit logging page](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging). 

#### Cluster-level queries

Query/filter name | Expression  
---|---  
Google Kubernetes Engine cluster operations  | 
    
    
    resource.type="gke_cluster" AND
    log_id("cloudaudit.googleapis.com/activity")  
  
Google Kubernetes Engine cluster creation | 
    
    
    resource.type="gke_cluster" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName="google.container.v1.ClusterManager.CreateCluster"
            
  
Kubernetes cluster deployment | 
    
    
    resource.type="k8s_cluster" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName:"deployments"
            
  
Kubernetes cluster authentication failure | 
    
    
    resource.type="k8s_cluster" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.authenticationInfo.principalEmail="system:anonymous"
            
  
Kubernetes cluster operations and events in `us-central1-b` | 
    
    
    resource.type="k8s_cluster" AND
    resource.labels.location="us-central1-b"
            
  
Kubernetes pod requests from users | 
    
    
    resource.type="k8s_cluster" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName:"io.k8s.core.v1.pods" AND
    protoPayload.authenticationInfo.principalEmail="USER_EMAIL"
            
  
Kubernetes events | 
    
    
    resource.type="k8s_cluster" AND
    log_id("events")
            
  
Kubernetes Endpoints update | 
    
    
    resource.type="k8s_cluster" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.request.kind="Endpoints"
            
  
Kubernetes control plane logs | 
    
    
    resource.type="k8s_cluster" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.serviceName="k8s.io"
            
  
Kubernetes Engine control plane logs | 
    
    
    resource.type="k8s_cluster" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.serviceName="container.googleapis.com"
            
  
Pod deletion | 
    
    
    resource.type="k8s_cluster" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName=~"io\.k8s\.core\.v1\.pods\.(create|delete)"
            
  
Kubernetes pod audit logs from control plane | 
    
    
    resource.type="k8s_cluster" AND
    resource.labels.location="CLUSTER_LOCATION" AND
    resource.labels.cluster_name="CLUSTER_NAME" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.resourceName="core/v1/namespaces/POD_NAMESPACE/pods/POD_NAME
            
  
Kubernetes pod evictions | 
    
    
    resource.type="k8s_cluster" AND
    resource.labels.location="CLUSTER_LOCATION" AND
    resource.labels.cluster_name="CLUSTER_NAME" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName="io.k8s.core.v1.pods.eviction.create"
            
  
Kubernetes node audit logs from the control plane | 
    
    
    resource.type="k8s_cluster" AND
    resource.labels.location="CLUSTER_LOCATION" AND
    resource.labels.cluster_name="CLUSTER_NAME" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.methodName:"io.k8s.core.v1.nodes"
            
  
Kubernetes cluster control plane for Addon Manager Activity | 
    
    
    resource.type="k8s_cluster" AND
    resource.labels.location="CLUSTER_LOCATION" AND
    resource.labels.cluster_name="CLUSTER_NAME" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.authenticationInfo.principalEmail="system:addon-manager"
            
  
Kubernetes control plane errors (excluding `Conflict`, which is normal) | 
    
    
    resource.type="k8s_cluster" AND
    resource.labels.location="CLUSTER_LOCATION" AND
    resource.labels.cluster_name="CLUSTER_NAME" AND
    log_id("cloudaudit.googleapis.com/activity") AND
    protoPayload.status.message!="Conflict" AND
    protoPayload.status.code!=0
            
  
Ingress Controller events | 
    
    
    resource.type="k8s_cluster" AND
    resource.labels.location="CLUSTER_LOCATION" AND
    resource.labels.cluster_name="CLUSTER_NAME" AND
    log_id("events") AND
    jsonPayload.source.component="loadbalancer-controller"
            
  
Service Controller events (kube-controller-manager) | 
    
    
    resource.type="k8s_cluster" AND
    resource.labels.location="CLUSTER_LOCATION" AND
    resource.labels.cluster_name="CLUSTER_NAME" AND
    log_id("events") AND
    jsonPayload.source.component="service-controller"
            
  
Cluster Autoscaler events | 
    
    
    resource.type="k8s_cluster" AND
    resource.labels.location="CLUSTER_LOCATION" AND
    resource.labels.cluster_name="CLUSTER_NAME" AND
    log_id("events") AND
    jsonPayload.source.component="cluster-autoscaler"
            
  
#### Pod-level queries

Filter name | Expression  
---|---  
Query pod during creation | 
    
    
    resource.type="k8s_pod" AND
    resource.labels.pod_name="POD_NAME" AND
    log_id("events")
            
  
Query pod terminated due to resource pressure | 
    
    
    resource.type="k8s_pod" AND
            log_id("events") AND
            jsonPayload.reason="Evicted"
            
  
Scheduler events | 
    
    
    resource.type="k8s_pod" AND
    resource.labels.location="CLUSTER_LOCATION" AND
    resource.labels.cluster_name="CLUSTER_NAME" AND
    log_id("events") AND
    jsonPayload.source.component="default-scheduler"
            
  
Scheduler events (preemptions) | 
    
    
    resource.type="k8s_pod" AND
    resource.labels.location="CLUSTER_LOCATION" AND
    resource.labels.cluster_name="CLUSTER_NAME" AND
    log_id("events") AND
    jsonPayload.source.component="default-scheduler" AND
    jsonPayload.reason="Preempted"
            
  
#### Node-level queries

Filter name | Expression  
---|---  
Node events | 
    
    
    resource.type="k8s_node" AND
    log_id("events")
            
  
Looking at Kube-proxy logs | 
    
    
    resource.type="k8s_node" AND
    log_id("kube-proxy")
            
  
Looking at dockerd logs | 
    
    
    resource.type="k8s_node" AND
    log_id("container-runtime")
            
  
Looking at kubelet errors or failures | 
    
    
    resource.type="k8s_node" AND
    log_id("kubelet") AND
    jsonPayload.MESSAGE:("error" OR "fail")
            
  
Looking at node logs for GKE system logs | 
    
    
    resource.type = "k8s_node"
    logName:( "logs/container-runtime" OR
    "logs/docker" OR
    "logs/kube-container-runtime-monitor" OR
    "logs/kube-logrotate" OR
    "logs/kube-node-configuration" OR
    "logs/kube-node-installation" OR
    "logs/kubelet" OR
    "logs/kubelet-monitor" OR
    "logs/node-journal" OR
    "logs/node-problem-detector")
            
  
#### Namespace queries

Filter name | Expression  
---|---  
Container and pod logs for GKE system logs | 
    
    
    resource.type = ("k8s_container" OR "k8s_pod")
    resource.labels.namespace_name = (
    "cnrm-system" OR
    "config-management-system" OR
    "gatekeeper-system" OR
    "gke-connect" OR
    "gke-system" OR
    "istio-system" OR
    "knative-serving" OR
    "monitoring-system" OR
    "kube-system")
            
  
#### Container queries

Filter name | Expression  
---|---  
Stdout container logs across all pods and containers in a cluster | 
    
    
    resource.type="k8s_container" AND
    log_id("stdout")
            
  
Container error logs across all pods and containers in a cluster | 
    
    
    resource.type="k8s_container" AND
    log_id("stderr") AND
    severity=ERROR
            
  
Container error logs for a pod with a specific name | 
    
    
    resource.type="k8s_container" AND
    resource.labels.pod_name="POD_NAME" AND
    severity=ERROR
            
  
Container error logs for a specific container in a specific pod | 
    
    
    resource.type="k8s_container" AND
    resource.labels.pod_name="POD_NAME" AND
    resource.labels.container_name="server" AND
    severity=ERROR
            
  
Container error logs for a specific namespace and container | 
    
    
    resource.type="k8s_container" AND
    resource.labels.namespace_name="istio-system" AND
    resource.labels.container_name="egressgateway" AND
    severity=ERROR
            
  
Container logs for a pod with a specific label | 
    
    
    resource.type="k8s_container" AND
    labels."k8s-pod/app"="loadgenerator" AND
    severity=ERROR
            
  
Container error logs for pods running on a specific node | 
    
    
    resource.type="k8s_container" AND
    labels."compute.googleapis.com/resource_name"="NODE_NAME" AND
    severity=ERROR
            
  
Container logs for a pod with a label generated using skaffold | 
    
    
    resource.type="k8s_container" AND
    labels."k8s-pod/app"="loadgenerator" AND
    labels."k8s-pod/skaffold_dev/run-id"="SKAFFOLD_RUN_ID"
    severity=ERROR
            
  
Container error logs for a specific pod containing a `POST` in the textPayload | 
    
    
    resource.type="k8s_container" AND
    resource.labels.pod_name="POD_NAME" AND
    textPayload:"POST" AND
    severity=ERROR
            
  
Container error logs for a specific pod containing a `GET` in the structured JSON | 
    
    
    resource.type="k8s_container" AND
    resource.labels.pod_name="POD_NAME" AND
    jsonPayload."http.req.method"="GET" AND
    severity=ERROR
            
  
Container errors logs in the kube-system namespace | 
    
    
    resource.type="k8s_container" AND
    resource.labels.namespace_name="kube-system" AND
    severity=ERROR
            
  
Container error in the container insights log | 
    
    
    resource.type="k8s_container" AND
    log_id("clouderrorreporting.googleapis.com/insights")
            
  
Kubernetes container logs | 
    
    
    resource.type="k8s_container" AND
    resource.labels.container_name="CONTAINER_NAME"
            
  
#### Control plane queries

Note: GKE control plane logs must be enabled. Filter name | Expression  
---|---  
Kubernetes API server logs | 
    
    
    resource.type="k8s_control_plane_component"
    resource.labels.component_name="apiserver"
    resource.labels.location="CLUSTER_LOCATION"
    resource.labels.cluster_name="CLUSTER_NAME"
            
  
Kubernetes Scheduler logs | 
    
    
    resource.type="k8s_control_plane_component"
    resource.labels.component_name="scheduler"
    resource.labels.location="CLUSTER_LOCATION"
    resource.labels.cluster_name="CLUSTER_NAME"
            
  
Kubernetes Controller Manager logs | 
    
    
    resource.type="k8s_control_plane_component"
    resource.labels.component_name="controller-manager"
    resource.labels.location="CLUSTER_LOCATION"
    resource.labels.cluster_name="CLUSTER_NAME"
            
  
#### TPU workload queries

Note: GKE system and workload logging must be enabled. Filter name | Expression  
---|---  
Stdout container logs across all TPU nodes with the same prefix  | 
    
    
    resource.type="k8s_container" AND
    labels."compute.googleapis.com/resource_name"=~"TPU_NODE_PREFIX.*" AND
    log_id("stdout")
            
  
Container error logs across all TPU nodes with the same prefix  | 
    
    
    resource.type="k8s_container" AND
    labels."compute.googleapis.com/resource_name"=~"TPU_NODE_PREFIX.*" AND
    log_id("stderr") AND
    severity=ERROR
            
  
Stdout container logs from the same GKE Job  | 
    
    
    resource.type="k8s_container" AND
    labels."k8s-pod/batch.kubernetes.io/job-name" = "JOB_NAME" AND
    log_id("stdout")
            
  
Container error logs from the same GKE Job  | 
    
    
    resource.type="k8s_container" AND
    labels."k8s-pod/batch.kubernetes.io/job-name"="JOB_NAME" AND
    log_id("stderr") AND
    severity=ERROR
            
  
Stdout container logs from the same GKE JobSet  | 
    
    
    resource.type="k8s_container" AND
    labels."k8s-pod/jobset_sigs_k8s_io/jobset-name"="JOBSET_NAME" AND
    log_id("stdout")
            
  
Container error logs from the same GKE JobSet  | 
    
    
    resource.type="k8s_container" AND
    labels."k8s-pod/jobset_sigs_k8s_io/jobset-name"="JOBSET_NAME" AND
    log_id("stderr") AND
    severity=ERROR
            
  
## Third-party application queries

**Caution:** As of September 28, 2026, the legacy Logging agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/logging/docs/agent/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

The following queries use the [default log IDs](https://docs.cloud.google.com/logging/docs/agent/default-logs) for logs collected by the [legacy Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging). If you are collecting logs by using the [Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent), then the log names might be configured differently. For more information about the Ops Agent and application logs, see [Collect logs from third-party applications](https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party).

Query/filter name | Expression  
---|---  
Apache logs  | 
    
    
    resource.type="gce_instance" AND
    (logName:"/apache-access" OR logName:"/apache-error")  
  
Cassandra logs  | 
    
    
    resource.type="gce_instance" AND
    log_id("cassandra")  
  
Chef logs  | 
    
    
    resource.type="gce_instance" AND
    logName:"projects/PROJECT_ID/logs/chef-"  
  
Gitlab logs  | 
    
    
    resource.type="gce_instance"
    logName:"projects/PROJECT_ID/logs/gitlab-"   
  
Jenkins logs  | 
    
    
    resource.type="gce_instance" AND
    log_id("jenkins")  
  
Jetty logs  | 
    
    
    resource.type="gce_instance" AND
    logName:"projects/PROJECT_ID/logs/jetty-"  
  
Joomla logs  | 
    
    
    resource.type="gce_instance" AND
    log_id("joomla")  
  
Linux syslogs  | 
    
    
    resource.type="gce_instance" AND
    log_id("syslog")  
  
Magneto logs  | 
    
    
    resource.type="gce_instance" AND
    logName:"projects/PROJECT_ID/logs/magneto-"  
  
Mediawiki logs  | 
    
    
    resource.type="gce_instance" AND
    log_id("mediawiki")  
  
memcached logs  | 
    
    
    resource.type="gce_instance" AND
    log_id("memcached")  
  
MongoDB logs  | 
    
    
    resource.type="gce_instance" AND
    log_id("mongodb")  
  
MySQL logs  | 
    
    
    resource.type="gce_instance" AND
    log_id("mysql")  
  
Nginx logs  | 
    
    
    resource.type="gce_instance" AND
    logName:"projects/PROJECT_ID/logs/nginx-"  
  
PostgreSQL logs  | 
    
    
    resource.type="gce_instance" AND
    log_id("postgresql")  
  
Puppet logs  | 
    
    
    resource.type="gce_instance" AND
    logName:"projects/PROJECT_ID/logs/puppet-"  
  
RabbitMQ logs  | 
    
    
    resource.type="gce_instance" AND
    logName:"projects/PROJECT_ID/logs/rabbitmq-"  
  
Redmine logs  | 
    
    
    resource.type="gce_instance" AND
    log_id("redmine")  
  
Salt logs  | 
    
    
    resource.type="gce_instance" AND
    logName:"projects/PROJECT_ID/logs/salt-"  
  
Slow MySQL queries  | 
    
    
    resource.type="gce_instance" AND
    log_id("mysql-slow")  
  
Solr logs  | 
    
    
    resource.type="gce_instance" AND
    log_id("solr")  
  
SugarCRM logs  | 
    
    
    resource.type="gce_instance" AND
    log_id("sugarcrm")  
  
Tomcat logs  | 
    
    
    resource.type="gce_instance" AND
    log_id("tomcat")  
  
Zookeeper logs  | 
    
    
    resource.type="gce_instance" AND
    log_id("zookeeper")  
  
## Networking queries

Query/filter name | Expression  
---|---  
Firewall- all logs  | 
    
    
    resource.type="gce_subnetwork" AND
    log_id("compute.googleapis.com/firewall")  
  
Firewall logs for a given country | 
    
    
    resource.type="gce_subnetwork" AND
    log_id("compute.googleapis.com/firewall") AND
    jsonPayload.remote_location.country=COUNTRY_ISO_ALPHA_3  
  
Firewall logs from a VM | 
    
    
    resource.type="gce_subnetwork" AND
    log_id("compute.googleapis.com/firewall") AND
    jsonPayload.instance.vm_name="INSTANCE_NAME"  
  
Firewall subnet logs  | 
    
    
    resource.type="gce_subnetwork" AND
    log_id("compute.googleapis.com/firewall") AND
    resource.labels.subnetwork_name="SUBNET_NAME"  
  
Compute Engine subnetwork traffic logs to a subnet | 
    
    
    resource.type="gce_subnetwork" AND
    ip_in_net(jsonPayload.connection.dest_ip, "SUBNET_IP")  
  
VPC Flow logs  | 
    
    
    resource.type="gce_subnetwork" AND
    log_id("compute.googleapis.com/vpc_flows")  
  
VPC Flow logs for specific port and protocol  | 
    
    
    resource.type="gce_subnetwork" AND
    log_id("compute.googleapis.com/vpc_flows") AND
    jsonPayload.connection.src_port="PORT_ID" AND
    jsonPayload.connection.protocol="PROTOCOL"  
  
VPC Flow logs for specific subnet  | 
    
    
    resource.type="gce_subnetwork" AND
    log_id("compute.googleapis.com/vpc_flows") AND
    resource.labels.subnetwork_name="SUBNET_NAME"  
  
VPC Flow logs for specific subnet prefix | 
    
    
    resource.type="gce_subnetwork" AND
    log_id("compute.googleapis.com/vpc_flows") AND
    ip_in_net(jsonPayload.connection.dest_ip, "SUBNET_IP")  
  
VPC Flow logs for a specific VM | 
    
    
    resource.type="gce_subnetwork" AND
    log_id("compute.googleapis.com/vpc_flows") AND
    jsonPayload.src_instance.vm_name="VM_NAME"  
  
VPN gateway logs  | 
    
    
    resource.type="vpn_gateway" AND
    resource.labels.gateway_id="GATEWAY_ID"  
  
HTTP Load Balancer 5xx errors  | 
    
    
    resource.type="http_load_balancer" AND
    httpRequest.status>=500  
  
HTTP Load Balancer requests to PHPMyAdmin  | 
    
    
    resource.type="http_load_balancer" AND
    httpRequest.request_url:"phpmyadmin"  
  
## Security queries

Query/filter name | Expression  
---|---  
Audit logs—all  | 
    
    
    logName:"cloudaudit.googleapis.com"  
  
Audit logs- Access Transparency (AXT)  | 
    
    
    log_id("cloudaudit.googleapis.com/access_transparency")  
  
Audit logs- Admin Activity  | 
    
    
    log_id("cloudaudit.googleapis.com/activity")  
  
Audit logs- Data Access  | 
    
    
    log_id("cloudaudit.googleapis.com/data_access")  
  
Audit logs- System Event  | 
    
    
    log_id("cloudaudit.googleapis.com/system_event")  
  
## Security Command Center queries

Use the following queries to find Security Command Center audit logs and inspect or filter requests that are generated by Security Command Center services, including the vulnerability scanner for External Exposure, such as from the `TsunamiSecurityScanner` user agent. For more information, see [Identify scanner traffic in your logs](https://docs.cloud.google.com/security-command-center/docs/detect-external-exposure#identify-scanner-traffic) and [Troubleshooting Security Command Center](https://docs.cloud.google.com/security-command-center/docs/troubleshooting#tsunami-scanner-403).

Query/filter name | Expression  
---|---  
Security Command Center vulnerability scanner requests  | 
    
    
    httpRequest.userAgent="TsunamiSecurityScanner"  
  
Security Command Center scanner requests blocked by access controls (`HTTP 403`)  | 
    
    
    httpRequest.userAgent="TsunamiSecurityScanner" AND
    httpRequest.status=403  
  
Exclude Security Command Center vulnerability scanner requests  | 
    
    
    NOT httpRequest.userAgent="TsunamiSecurityScanner"  
  
Security Command Center Admin Activity audit logs  | 
    
    
    protoPayload.serviceName="securitycenter.googleapis.com" AND
    log_id("cloudaudit.googleapis.com/activity")  
  
All Security Command Center audit logs  | 
    
    
    protoPayload.serviceName="securitycenter.googleapis.com"  
  
## Troubleshooting

For instructions about troubleshooting common issues when using the Logs Explorer, see [Using the Logs Explorer: Troubleshooting](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#troubleshooting).

## What's next

For more information about the query syntax, which you can use to customize these queries, see [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).

For more information about querying in the Google Cloud console, see [Build queries by using the Logging query language](https://docs.cloud.google.com/logging/docs/view/building-queries).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
