---
url: https://docs.cloud.google.com/monitoring/api/resources/
title: Monitored resource types \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:30.628974+00:00
---

# Monitored resource types  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Monitored resource types Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Monitoring supports the following monitored-resource types. This list differs from the [Cloud Logging list of monitored-resource types](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#resource-types).

## About the list

This list is regenerated frequently and time-stamped. The fields listed for each resource type are defined in the [`MonitoredResourceDescriptor` object](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors#MonitoredResourceDescriptor) type in the Monitoring API. For an introduction to monitored resources, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).

**Cloud Endpoints** : APIs managed by Cloud Endpoints write [ `serviceruntime`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-serviceruntime) metrics against the [`api`](https://docs.cloud.google.com/monitoring/api/resources#tag_api) monitored-resource type.

The following list was last generated at 2026-10-14 20:17:53 UTC.

## `abuseevent.googleapis.com/Location`

**Display name** : Abuse Event

**Description** : A GCP resource container associated with an abuse event.

**Labels** :

  * `resource_container`: The GCP resource identifier associated with the abuse event.
  * `location`: The location where the abuse event was observed.



## `accesscontextmanager.googleapis.com/AccessPolicyQuotaResource`

**Display name** : Access policy resource.

**Description** : Access policy resource.

**Labels** :

  * `resource_container`: The GCP container associated with the metric.
  * `location`: Location for the quota.
  * `access_policy`: The access policy custom dimension.



## `aiplatform.googleapis.com/DeploymentResourcePool`

**Display name** : Vertex AI Deployment Resource Pool

**Description** : A Vertex AI Deployment Resource Pool.

**Labels** :

  * `resource_container`: The identifier of the GCP Project owning the Deployment Resource Pool.
  * `location`: The region in which the service is running.
  * `deployment_resource_pool_id`: The ID of the Deployment Resource Pool.



## `aiplatform.googleapis.com/Endpoint`

**Display name** : Vertex AI Endpoint

**Description** : A Vertex AI API Endpoint where Models are deployed into it.

**Labels** :

  * `resource_container`: The identifier of the GCP Project owning the Endpoint.
  * `location`: The region in which the service is running.
  * `endpoint_id`: The ID of the Endpoint.



## `aiplatform.googleapis.com/FeatureOnlineStore`

**Display name** : Vertex AI Feature Online Store

**Description** : A Vertex AI Feature Online Store.

**Labels** :

  * `resource_container`: The identifier of the GCP Project owning the FeatureOnlineStore.
  * `location`: The region in which the service is running.
  * `feature_online_store_id`: The ID of the Feature Online Store.



## `aiplatform.googleapis.com/Featurestore`

**Display name** : Vertex AI Feature Store

**Description** : A Vertex AI Feature Store.

**Labels** :

  * `resource_container`: The identifier of the GCP Project owning the Featurestore.
  * `location`: The region in which the service is running.
  * `featurestore_id`: The ID of the Featurestore.



## `aiplatform.googleapis.com/Index`

**Display name** : Matching Engine Index

**Description** : An Index built through the cloud Matching Engine service.

**Labels** :

  * `resource_container`: The identifier of the GCP Project owning the Index.
  * `location`: The region in which the service is running.
  * `index_id`: The ID of the Index.



## `aiplatform.googleapis.com/IndexEndpoint`

**Display name** : Matching Engine Index Endpoint

**Description** : An Endpoint to which Matching Engine Indexes are deployed.

**Labels** :

  * `resource_container`: The identifier of the GCP Project owning the Index.
  * `location`: The region in which the service is running.
  * `index_endpoint_id`: The ID of the index endpoint.



## `aiplatform.googleapis.com/Location`

**Display name** : Location

**Description** : A Google Cloud Project and region where a job is running.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The region in which the service is running.



## `aiplatform.googleapis.com/Model`

**Display name** : Vertex AI Model

**Description** : A Vertex AI Model.

**Labels** :

  * `resource_container`: The identifier of the GCP Project owning the Model.
  * `location`: The region in which the service is running.
  * `model`: The identifier of the Model.



## `aiplatform.googleapis.com/ModelMonitor`

**Display name** : Vertex AI Model Monitor

**Description** : A Vertex AI Model Monitor.

**Labels** :

  * `resource_container`: The identifier of the GCP Project owning the Model Monitor.
  * `location`: The region in which the service is running.
  * `model_monitor_id`: The identifier of the Model Monitor.



## `aiplatform.googleapis.com/OnlineEvaluator`

**Display name** : Vertex AI Online Evaluator

**Description** : A Vertex AI Online Evaluator.

**Labels** :

  * `resource_container`: The resource container of the Online Evaluator.
  * `location`: The location of the Online Evaluator.
  * `online_evaluator_id`: The ID of the Online Evaluator resource.



## `aiplatform.googleapis.com/PipelineJob`

**Display name** : Vertex Pipelines Job

**Description** : A Vertex Pipelines Job.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The region in which the service is running.
  * `pipeline_job_id`: The ID of the PipelineJob.



## `aiplatform.googleapis.com/PublisherModel`

**Display name** : Vertex AI Model Garden Publisher Model

**Description** : A Vertex AI Model Garden Publisher Model.

**Labels** :

  * `resource_container`: The identifier of the GCP Project owning the Endpoint.
  * `location`: The region in which the service is running.
  * `publisher`: The publisher of the model.
  * `model_user_id`: The resource ID of the PublisherModel.
  * `model_version_id`: The version ID of the PublisherModel.



## `aiplatform.googleapis.com/ReasoningEngine`

**Display name** : Vertex AI Reasoning Engine

**Description** : A Vertex AI Reasoning Engine.

**Labels** :

  * `resource_container`: The identifier of the GCP Project owning the ReasoningEngine.
  * `location`: The region in which the service is running.
  * `reasoning_engine_id`: The numeric ID of the Reasoning Engine instance.



## `aiplatform.googleapis.com/SemanticGovernancePolicyEngine`

**Display name** : Semantic Governance Policy Engine

**Description** : Semantic Governance Policy Engine resource.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The region in which the service is running.



## `aiplatform.googleapis.com/ServerlessRayJob`

**Display name** : Vertex AI Serverless Ray Job

**Description** : A Vertex AI Serverless Ray Job.

**Labels** :

  * `resource_container`: The identifier of the GCP Project owning the Serverless Ray Job.
  * `location`: The region in which the service is running.
  * `job_id`: The ID of the Serverless Ray Job.



## `alloydb.googleapis.com/Cluster`

**Display name** : AlloyDB cluster

**Description** : Monitored resource representing an AlloyDB cluster.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the AlloyDB cluster is running.
  * `cluster_id`: AlloyDB cluster identifier.



## `alloydb.googleapis.com/Database`

**Display name** : AlloyDB database

**Description** : Monitored resource representing a database on AlloyDB instance.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the AlloyDB instance is running.
  * `cluster_id`: AlloyDB cluster identifier.
  * `instance_id`: AlloyDB instance identifier.
  * `database`: The name of database schema associated with the AlloyDB engine.



## `alloydb.googleapis.com/Instance`

**Display name** : AlloyDB instance

**Description** : Monitored resource representing an AlloyDB instance.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the AlloyDB instance is running.
  * `cluster_id`: AlloyDB cluster identifier.
  * `instance_id`: AlloyDB instance identifier.



## `alloydb.googleapis.com/InstanceNode`

**Display name** : AlloyDB node

**Description** : Monitored resource representing a physical node in AlloyDB instance.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the AlloyDB instance is running.
  * `cluster_id`: AlloyDB cluster identifier.
  * `instance_id`: AlloyDB instance identifier.
  * `node_id`: AlloyDB physical node identifier within the AlloyDB instance.



## `alloydb.googleapis.com/Location`

**Display name** : AlloyDB Location

**Description** : A location in the AlloyDB API.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource.
  * `location`: The location in the API.



## `alloydb.googleapis.com/NodeDatabase`

**Display name** : AlloyDB Node Database

**Description** : Monitored resource to capture database metrics reported by a specific AlloyDB node.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the AlloyDB instance is running.
  * `cluster_id`: AlloyDB cluster identifier.
  * `instance_id`: AlloyDB instance identifier.
  * `node_id`: AlloyDB physical node identifier within the AlloyDB instance.
  * `database`: The name of database schema associated with the AlloyDB engine.



## `anthos_l4lb`

**Display name** : Anthos L4LB

**Description** : An Anthos L4 load balancer instance.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The GCP region where to store metrics.
  * `kind`: The kind of the load balancer.
  * `group_name`: The name of the load balancer group.
  * `hostname`: The hostname of the instance running LB.



## `api`

**Display name** : Produced API

**Description** : An API provided by the producer.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `service`: The API service name, such as "cloudsql.googleapis.com".
  * `method`: The API method, such as "disks.list".
  * `version`: The API version, such as "v1".
  * `location`: The service specific notion of location. This can be the name of a zone, region, or "global".



## `apigateway.googleapis.com/Gateway`

**Display name** : API Gateway

**Description** : Fully managed API Gateway.

**Labels** :

  * `resource_container`: The identifier of the GCP Project owning the Gateway.
  * `location`: The region in which the Gateway is running.
  * `gateway_id`: The ID of the Gateway.



## `apigee.googleapis.com/APIHubDeployment`

**Display name** : API Hub Deployment

**Description** : Deployment for API Hub.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: Location of the deployment.
  * `gateway_type`: The type of the gateway the deployment belongs to.
  * `gateway_id`: The identifier of the gateway the deployment belongs to.
  * `deployment_id`: The identifier of the deployment that got assessed.



## `apigee.googleapis.com/Environment`

**Display name** : Apigee environment

**Description** : Monitored resource for Apigee environment.

**Labels** :

  * `resource_container`: The GCP project ID that writes to this monitored resource.
  * `org`: An organization is a container for all the objects in an Apigee account.
  * `env`: An environment is a runtime execution context for the proxies in an organization.
  * `location`: Location where the Apigee infrastructure is provisioned.



## `apigee.googleapis.com/EnvironmentInstance`

**Display name** : Apigee environment instance

**Description** : Monitored resource for Apigee instance attachment.

**Labels** :

  * `resource_container`: The GCP project ID that writes to this monitored resource.
  * `org`: An organization is a container for all the objects in an Apigee account.
  * `env`: An environment is a runtime execution context for the proxies in an organization.
  * `location`: Location of the Apigee Instance.
  * `instance_id`: ID of the Apigee instance.



## `apigee.googleapis.com/Instance`

**Display name** : Apigee instance

**Description** : Monitored resource for Apigee instance.

**Labels** :

  * `resource_container`: The GCP project ID that writes to this monitored resource.
  * `org`: An organization is a container for all the objects in an Apigee account.
  * `location`: Location of the Apigee Instance.
  * `instance_id`: Instance ID of the Apigee application.



## `apigee.googleapis.com/Proxy`

**Display name** : Apigee Proxy

**Description** : Monitored resource for Apigee API proxy.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "my-project".
  * `org`: The identifier for the Apigee organization.
  * `env`: The identifier for the Apigee environment.
  * `location`: Location where the Apigee runtime plane is provisioned.
  * `proxy_name`: The name of Apigee proxy deployed to the environment.



## `apigee.googleapis.com/ProxyV2`

**Display name** : Apigee proxy (v2)

**Description** : Monitored resource for Apigee API proxy (v2).

**Labels** :

  * `resource_container`: The GCP project ID that writes to this monitored resource.
  * `org`: An organization is a container for all the objects in an Apigee account.
  * `env`: An environment is a runtime execution context for the proxies in an organization.
  * `location`: Location where the Apigee infrastructure is provisioned.
  * `proxy_name`: A proxy is your interface to developers that want to use your backend services.
  * `runtime_version`: Version of the Apigee Runtime for the proxy.
  * `instance_id`: Instance ID of the Apigee application.



## `apigee.googleapis.com/SecurityAssessmentResult`

**Display name** : Apigee API Security Assessment Result

**Description** : Security assessment result for Apigee Advanced API Security Risk Assessment V2.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: Location of the resource, global always.
  * `org`: The identifier of the Apigee organization associated with this resource, such as "my-org".
  * `scope`: The identifier of the scope associated with the resource that got assessed. If an Apigee proxy was assessed, this would be the Apigee environment ID the proxy is deployed in.
  * `resource`: The identifier of the resource that got assessed. If an Apigee proxy was assessed, this would be the Apigee proxy ID.
  * `security_profile`: The identifier of the Apigee Risk Assessment V2 Security profile used to assess the resource, such as "google-default".



## `apigee.googleapis.com/SecurityDetectionRule`

**Display name** : Apigee API Security Detection Rule

**Description** : Apigee API Security abuse detection rule to detect unusual patterns in API traffic.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: Location of the resource, global always.
  * `org`: The identifier of the Apigee organization associated with this resource, such as "my-org".
  * `env`: The identifier of Apigee environment associated with this resource, such as "my-env".
  * `detection_rule`: Apigee API Security detection rule, such as "Flooder" or "Static Content Scraper".



## `apigee.googleapis.com/SecurityIncident`

**Display name** : Apigee API Security Incident

**Description** : A security incident is a group of events with similar patterns detected by Apigee Advanced API Security, which could represent an API attack.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: Location of the resource, global always.
  * `org`: The identifier of the Apigee organization associated with this resource, such as "my-org".
  * `env`: The identifier of Apigee environment associated with this resource, such as "my-env".
  * `incident_id`: Apigee API Security incident id.



## `apigee.googleapis.com/SecurityProfileEnvironmentAssociation`

**Display name** : Apigee API Security Profile Environment Association

**Description** : Apigee Advanced API Security profile attached to Apigee environment.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: Location of the resource, global always.
  * `org`: The identifier of the Apigee organization associated with this resource, such as "my-org".
  * `profile`: Apigee API Security profile name, such as "google-default".
  * `env`: The identifier of Apigee environment associated with this resource, such as "my-env".



## `apigee.googleapis.com/Target`

**Display name** : Apigee target

**Description** : Monitored resource for Apigee target with the host endpoint label.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "my-project".
  * `org`: The identifier for the Apigee organization.
  * `env`: The identifier for the Apigee environment.
  * `location`: Location where the Apigee runtime plane is provisioned.
  * `proxy_name`: The name of Apigee proxy deployed to the environment.
  * `endpoint`: Endpoint is represented by statically defined hostnames or target servers. For IP Addresses and dynamically-configured endpoints, data is aggregated and presented under the static string "IP Address" and "Dynamic Target" respectively.



## `apigee.googleapis.com/TargetV2`

**Display name** : Apigee target (v2)

**Description** : Monitored resource for Apigee target (v2) with the host endpoint label.

**Labels** :

  * `resource_container`: The GCP project ID that writes to this monitored resource.
  * `org`: An organization is a container for all the objects in an Apigee account.
  * `env`: An environment is a runtime execution context for the proxies in an organization.
  * `location`: Location where the Apigee infrastructure is provisioned.
  * `proxy_name`: A proxy is your interface to developers that want to use your backend services.
  * `type`: Type of target such as service callout.
  * `endpoint`: Target endpoint URL.
  * `runtime_version`: Version of the Apigee Runtime for the proxy.
  * `instance_id`: Instance ID of the Apigee application.



## `app_script_function`

**Display name** : Apps Script Function

**Description** : An Apps Script function.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `invocation_type`: The invocation type.
  * `function_name`: The function name.



## `apphub.googleapis.com/Application`

**Display name** : AppHub Application

**Description** : An Application in AppHub.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: Location for the quota.
  * `application_id`: The identifier of an Application in AppHub, such as "my-app".



## `apphub.googleapis.com/Location`

**Display name** : GCP Location

**Description** : A GCP location. A specific region, or global.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: Location for the resource.



## `artifactregistry.googleapis.com/Location`

**Display name** : Artifact Registry Location

**Description** : A location in Artifact Registry.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "my_project" or "organizations/5678".
  * `location`: Location of resource.



## `artifactregistry.googleapis.com/Project`

**Display name** : Artifact Registry Project

**Description** : A Cloud project in Artifact Registry.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "my_project" or "organizations/5678".
  * `location`: Location of resource.



## `artifactregistry.googleapis.com/Repository`

**Display name** : Artifact Registry Repository

**Description** : A repository in Artifact Registry.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "my_project" or "organizations/5678".
  * `location`: Location of resource.
  * `repository_id`: The identifier of the Artifact Registry repository, such as "my_repository".



## `assistant_action`

**Display name** : Google Assistant Action

**Description** : An Action in a Google Assistant App.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `version_id`: Stringified version ID of the assistant agent.
  * `action_id`: Action ID of the assistant agent.



## `assistant_action_project`

**Display name** : Google Assistant Action Project

**Description** : A project in a Google Assistant Action.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".



## `audited_resource`

**Display name** : Audited Resource

**Description** : A Google Cloud resource that produces an audit log.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `service`: The name of the API service generating the audit log.
  * `method`: The name of the API method generating the audit log.



## `autoscaler`

**Display name** : Autoscaler

**Description** : An autoscaler for a single managed instance group.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The zone or region for the autoscaler.
  * `autoscaler_id`: The identifier for the autoscaler.
  * `autoscaler_name`: The name of the autoscaler.
  * `instance_group_manager_id`: The identifier for the managed instance group scaled by the given autoscaler.
  * `instance_group_manager_name`: The name of the managed instance group scaled by the givenautoscaler.



## `aws_alb_load_balancer`

**Display name** : Amazon ALB Load Balancer

**Description** : A load balancer in Amazon ALB.

**Labels** :

  * `project_id`: The identifier of the GCP project under which data is stored for the AWS account specified in the aws_account label, such as "my-project".
  * `name`: The name of the load balancer.
  * `region`: The AWS region for the load balancer. The format of this field is "aws:{region}", where supported values for {region} are listed at <http://docs.aws.amazon.com/general/latest/gr/rande.html>. 
  * `aws_account`: The AWS account number for the load balancer.



## `aws_cloudfront_distribution`

**Display name** : Amazon CloudFront CDN

**Description** : A CloudFront content distribution network.

**Labels** :

  * `project_id`: The identifier of the GCP project under which data is stored for the AWS account specified in the aws_account label, such as "my-project".
  * `distribution_id`: The CloudFront distribution identifier assigned by AWS.
  * `region`: The AWS region for the CloudFront distribution. The format of this field is "aws:{region}", where supported values for {region} are listed at <http://docs.aws.amazon.com/general/latest/gr/rande.html>. 
  * `aws_account`: The AWS account number for the CDN.



## `aws_ec2_instance`

**Display name** : Amazon EC2 Instance

**Description** : A VM instance in Amazon EC2.

**Labels** :

  * `project_id`: The identifier of the GCP project under which data is stored for the AWS account specified in the aws_account label, such as "my-project".
  * `instance_id`: The VM instance identifier assigned by AWS.
  * `region`: The AWS region for the VM. The format of this field is "aws:{region}", where supported values for {region} are listed at <http://docs.aws.amazon.com/general/latest/gr/rande.html>. 
  * `aws_account`: The AWS account number for the VM.



## `aws_elasticache_cluster`

**Display name** : Amazon Elasticache Cluster

**Description** : A cache cluster in Amazon Elasticache.

**Labels** :

  * `project_id`: The identifier of the GCP project under which data is stored for the AWS account specified in the aws_account label, such as "my-project".
  * `cluster_id`: The cluster identifier.
  * `region`: The AWS region for the cluster. The format of this field is "aws:{region}", where supported values for {region} are listed at <http://docs.aws.amazon.com/general/latest/gr/rande.html>. 
  * `aws_account`: The AWS account number for the cluster.



## `aws_lambda_function`

**Display name** : Amazon Lambda Function

**Description** : A function in Amazon Lambda.

**Labels** :

  * `project_id`: The identifier of the GCP project under which data is stored for the AWS account specified in the aws_account label, such as "my-project".
  * `function_name`: The function name.
  * `region`: The AWS region for the function. The format of this field is "aws:{region}", where supported values for {region} are listed at <http://docs.aws.amazon.com/general/latest/gr/rande.html>. 
  * `aws_account`: The AWS account number for the function.



## `aws_rds_database`

**Display name** : Amazon RDS Database

**Description** : A database in Amazon Relational Database Service.

**Labels** :

  * `project_id`: The identifier of the GCP project under which data is stored for the AWS account specified in the aws_account label, such as "my-project".
  * `name`: The database name.
  * `region`: The AWS region for the database. The format of this field is "aws:{region}", where supported values for {region} are listed at <http://docs.aws.amazon.com/general/latest/gr/rande.html>. 
  * `aws_account`: The AWS account number for the database.



## `aws_s3_bucket`

**Display name** : Amazon S3 Bucket

**Description** : A bucket in Amazon S3.

**Labels** :

  * `project_id`: The identifier of the GCP project under which data is stored for the AWS account specified in the aws_account label, such as "my-project".
  * `bucket_name`: The bucket name.
  * `region`: The AWS region for the bucket. The format of this field is "aws:{region}", where supported values for {region} are listed at <http://docs.aws.amazon.com/general/latest/gr/rande.html>. 
  * `aws_account`: The AWS account number for the bucket.



## `aws_sqs_queue`

**Display name** : Amazon SQS Queue

**Description** : A queue in Amazon Simple Queue Service.

**Labels** :

  * `project_id`: The identifier of the GCP project under which data is stored for the AWS account specified in the aws_account label, such as "my-project".
  * `queue`: The queue name.
  * `region`: The AWS region for the queue. The format of this field is "aws:{region}", where supported values for {region} are listed at <http://docs.aws.amazon.com/general/latest/gr/rande.html>. 
  * `aws_account`: The AWS account number for the queue.



## `backupdr.googleapis.com/AutoProtectionPolicy`

**Display name** : Auto Protection Policy

**Description** : Represents a single Auto Protection Policy resource.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The GCP location.
  * `auto_protection_policy_id`: The ID of the Auto Protection Policy.



## `backupdr.googleapis.com/AutoProtectionPolicyBinding`

**Display name** : Auto Protection Policy Binding

**Description** : Represents a single Auto Protection Policy Binding resource.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The GCP location.
  * `auto_protection_policy_id`: The ID of the Auto Protection Policy.
  * `binding_id`: The ID of the Auto Protection Policy Binding.



## `backupdr.googleapis.com/BackupDRProject`

**Display name** : BackupDR Project

**Description** : A BackupDR Project.

**Labels** :

  * `resource_container`: Backup and DR API enabled project.
  * `location`: The GCP location.



## `backupdr.googleapis.com/BackupPlan`

**Display name** : Backup Plan

**Description** : Represents a single Backup Plan resource.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The GCP location.
  * `backup_plan_id`: The ID of the Backup Plan.



## `backupdr.googleapis.com/BackupPlanAssociation`

**Display name** : Backup Plan Association

**Description** : Represents a single Backup Plan Association resource.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The GCP location.
  * `backup_plan_association_id`: The ID of the Backup Plan Association.



## `backupdr.googleapis.com/BackupRecoveryAppliance`

**Display name** : Backup Recovery Appliance

**Description** : A Backup Recovery Appliance.

**Labels** :

  * `resource_container`: Backup and DR API enabled project.
  * `location`: The GCP location.
  * `backup_recovery_appliance_id`: The Backup recovery appliance Id.
  * `management_server_id`: Name of the management server.



## `backupdr.googleapis.com/BackupVault`

**Display name** : BackupVault

**Description** : A specialized storage for Google Cloud Backup and DR backups.

**Labels** :

  * `resource_container`: The identifier of the GCP project on which the BackupDR API is enabled, such as "my-project".
  * `location`: The GCP location.
  * `backup_vault_id`: The BackupVault ID.



## `backupdr.googleapis.com/ManagementConsole`

**Display name** : Management Console

**Description** : A Backup and DR management console.

**Labels** :

  * `resource_container`: Backup and DR API enabled project.
  * `location`: The GCP location.
  * `management_server_id`: Name of the management server.



## `baremetalsolution.googleapis.com/Instance`

**Display name** : Bare Metal Solution Instance

**Description** : Bare Metal Solution Instance.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The GCP location where the instance resource resides.
  * `instance_id`: The ID of the instance resource.



## `baremetalsolution.googleapis.com/Lun`

**Display name** : Bare Metal Solution Lun

**Description** : Bare Metal Solution Lun.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The GCP location where the volume resource resides.
  * `volume_id`: The ID of the volume resource.
  * `lun_id`: The ID of the lun resource.



## `baremetalsolution.googleapis.com/Volume`

**Display name** : Bare Metal Solution Volume

**Description** : Bare Metal Solution Volume.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The GCP location where the volume resource resides.
  * `volume_id`: The ID of the volume resource.



## `batch.googleapis.com/Job`

**Display name** : Job

**Description** : A Google Batch job managed by the Google Batch service.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with the job.
  * `location`: The region where the job has been created.
  * `job_id`: The identifier of the Job.



## `beyondcorp.googleapis.com/SecurityGateway`

**Display name** : Security Gateway

**Description** : Chrome Enterprise Premium Security Gateway.

**Labels** :

  * `resource_container`: The GCP container associated with the Security Gateway.
  * `location`: The region that contains the Security Gateway.
  * `security_gateway_id`: The Security Gateway ID.



## `bigquery.googleapis.com/ContinuousJob`

**Display name** : BigQuery Continuous Job

**Description** : Metrics from BigQuery Continuous Jobs.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "my-project" or "organizations/123".
  * `location`: The Cloud location of the continuous job.
  * `job_id`: The ID of the continuous job.



## `bigquery.googleapis.com/ManagedRoutineInvocation`

**Display name** : BigQuery Managed Routine Invocation

**Description** : Logs and metrics from BigQuery Managed Routines.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "my-project" or "organizations/123".
  * `location`: The cloud location of the managed routine.
  * `query_job_id`: The identifier of the BigQuery job that invoked the managed routine.
  * `routine_project_id`: The project id of the invoked routine.
  * `routine_dataset_id`: The dataset id of the invoked routine.
  * `routine_id`: The id of the invoked routine.



## `bigquery.googleapis.com/SparkJob`

**Display name** : BigQuery Spark Job

**Description** : Logs and metrics from BigQuery Spark Jobs.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "my-project" or "organizations/123".
  * `location`: The Cloud location of the Spark job.
  * `spark_job_id`: The ID of the Spark job.



## `bigquery_biengine_model`

**Display name** : BigQuery BI Engine Model

**Description** : BigQuery BI Engine Model.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The Google Cloud location of the resource.
  * `model_id`: The identifier of the BI model.



## `bigquery_dataset`

**Display name** : BigQuery Dataset

**Description** : A dataset in BigQuery.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `dataset_id`: The name of the BigQuery dataset.



## `bigquery_dts_config`

**Display name** : BigQuery DTS Config

**Description** : A BigQuery Data Transfer Service configuration.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The Google Cloud location of the resource
  * `config_id`: The id of the DTS configuration.



## `bigquery_project`

**Display name** : BigQuery Project

**Description** : BigQuery Project.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: Location of the resource.



## `bigquerystorage.googleapis.com/DataflowWrite`

**Display name** : BigQuery Storage Write API metrics for Dataflow jobs.

**Description** : BigQuery Storage Write API metrics for Dataflow jobs.

**Labels** :

  * `resource_container`: The identifier of the GCP project/folder/org associated with this resource. This is the project that runs the Dataflow job.
  * `location`: The BigQuery region in which the Storage API server locates.
  * `job_name`: The name of the Dataflow job this worker belongs to.
  * `job_id`: The id of the dataflow job the worker belongs to.
  * `worker_id`: The ID of the worker, unique for this job_id.
  * `destination_project`: The project of BigQuery destination table of the Dataflow job.



## `bigtable_backup`

**Display name** : Cloud Bigtable Backup

**Description** : A backup in Google Cloud Bigtable.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `instance`: The identifier for the instance.
  * `cluster`: The identifier for the cluster.
  * `backup`: The identifier for the backup.
  * `zone`: The zone of the backup.



## `bigtable_cluster`

**Display name** : Cloud Bigtable Cluster

**Description** : A cluster in Google Cloud Bigtable.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `instance`: The identifier for the instance.
  * `cluster`: The identifier for the cluster.
  * `zone`: The zone of the cluster.



## `bigtable_materialized_view`

**Display name** : Cloud Bigtable Materialized View

**Description** : A Materialized View in Google Cloud Bigtable.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `instance`: The identifier for the instance.
  * `cluster`: The identifier for the cluster.
  * `materialized_view`: The name of the materialized view.
  * `zone`: The zone of the materialized view.



## `bigtable_table`

**Display name** : Cloud Bigtable Table

**Description** : A table in Google Cloud Bigtable.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `instance`: The identifier for the instance.
  * `cluster`: The identifier for the cluster.
  * `table`: The name of the table.
  * `zone`: The zone of the table.



## `billingbudgets.googleapis.com/Location`

**Display name** : A location in the external budget API.

**Description** : A location in the external budget API.

**Labels** :

  * `resource_container`: The identity of the GCP resource container associated with this resource.
  * `location`: Location of resource.



## `blockchainaccelerator.googleapis.com/BlockchainNode`

**Display name** : Blockchain Node

**Description** : A Blockchain Node.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the GCP project associated with this resource.
  * `blockchain_protocol`: The blockchain protocol on which Blockchain Validator runs.
  * `blockchain_network`: Network type for the Blockchain.
  * `node_type`: Type of the Blockchain Node - Sentry, validator, core, etc.



## `blockchainnodeengine.googleapis.com/BlockchainNode`

**Display name** : Blockchain Node

**Description** : A blockchain node.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource, such as \"my-project\".
  * `location`: The Google Cloud region in which the blockchain node instance is running.
  * `blockchain_node_id`: The identifier of the blockchain node.



## `build`

**Display name** : Cloud Build

**Description** : A build in Cloud Build.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `build_id`: The unique id of the build.
  * `build_trigger_id`: The unique id of the build trigger.



## `businessaicode.googleapis.com/BAICInstance`

**Display name** : Business AI Code Instance

**Description** : An instance resource that represents a Business AI Code configuration.

**Labels** :

  * `resource_container`: The identifier of the GCP container associated with this resource.
  * `location`: The location of the resource.



## `certificatemanager.googleapis.com/CertificateMap`

**Display name** : Certificate Map

**Description** : Certificate Map instance.

**Labels** :

  * `resource_container`: The GCP container associated with the resource.
  * `location`: GCP location.
  * `certificate_map_id`: ID of Certificate Map.



## `certificatemanager.googleapis.com/Project`

**Display name** : Certificate Manager project

**Description** : Certificate Manager project.

**Labels** :

  * `resource_container`: The GCP container associated with the resource.
  * `location`: GCP location.



## `chronicle.googleapis.com/Collector`

**Display name** : Chronicle Collector

**Description** : A Chronicle collector object

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The physical location of the cluster that contains the collector object.
  * `collector_id`: The id of the collector.
  * `log_type`: The name of the log type.



## `chronicle.googleapis.com/Compliance`

**Display name** : Chronicle Compliance

**Description** : A Chronicle compliance object

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The physical location of the Chronicle instance.
  * `instance_id`: The unique identifier for the Chronicle instance.



## `chronicle.googleapis.com/LogType`

**Display name** : Chronicle Log Type

**Description** : A Chronicle logtype object

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The physical location of the cluster that contains the logtype object.
  * `log_type`: The name of the log type.



## `cloud_composer_environment`

**Display name** : Cloud Composer Environment

**Description** : A Composer environment runs the managed Apache Airflow service.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The Cloud Composer location in which the environment is running.
  * `environment_name`: The user-specified environment name.



## `cloud_composer_workflow`

**Display name** : Cloud Composer Workflow

**Description** : A Composer workflow runs a managed Apache Airflow workflow.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The Cloud Composer location in which the workflow is running.
  * `workflow_name`: The user-specified workflow name.



## `cloud_composer_workload`

**Display name** : Cloud Composer Workload

**Description** : A Composer workload runs the managed Apache Airflow workload.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The Cloud Composer location in which the environment is running.
  * `environment_name`: The user-specified environment name.
  * `workload_name`: The name of a workload.
  * `type`: The type of a workload.



## `cloud_dataproc_batch`

**Display name** : Cloud Dataproc Batch

**Description** : A Dataproc batch execution.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The Cloud Dataproc region to which the batch was submitted.
  * `batch_id`: The user-specified batch id.



## `cloud_dataproc_cluster`

**Display name** : Cloud Dataproc Cluster

**Description** : A Dataproc cluster with separate cluster name and id labels.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `cluster_name`: The user-specified cluster name.
  * `cluster_uuid`: The generated cluster id.
  * `region`: The Cloud Dataproc region in which the cluster is running.



## `cloud_dataproc_job`

**Display name** : Cloud Dataproc Job

**Description** : A Dataproc job execution.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `region`: The Cloud Dataproc region to which the job was submitted.
  * `job_id`: The user-specified job id.
  * `job_uuid`: The generated job uuid.



## `cloud_dataproc_session`

**Display name** : Cloud Dataproc Session

**Description** : A Dataproc session execution.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The Cloud Dataproc region in which the session was created.
  * `session_id`: The user-specified session id.



## `cloud_dlp_project`

**Display name** : Cloud Data Loss Prevention Project

**Description** : A Cloud Data Loss Prevention project.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The Google Cloud location where the operation is running.



## `cloud_function`

**Display name** : Cloud Function

**Description** : A function in Google Cloud Functions.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `function_name`: The short function name.
  * `region`: The region in which the function is running.



## `cloud_osconfig_patch_job`

**Display name** : OS Patch Job

**Description** : A Google Cloud OS Patch Job.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `patch_job_id`: Identifier of the job.



## `cloud_run_instance`

**Display name** : Cloud Run Instance

**Description** : An instance in Cloud Run.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `instance_name`: Name of the monitored instance.
  * `location`: Region where the instance exists.



## `cloud_run_job`

**Display name** : Cloud Run Job

**Description** : A job in Cloud Run.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `job_name`: Name of the monitored job.
  * `location`: Region where the job exists.



## `cloud_run_revision`

**Display name** : Cloud Run Revision

**Description** : A revision in Cloud Run.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `service_name`: Name of the service.
  * `revision_name`: Name of the monitored revision.
  * `location`: Region where the service is running.
  * `configuration_name`: Name of the configuration which created the monitored revision.



## `cloud_run_worker_pool`

**Display name** : Cloud Run Worker Pool

**Description** : A worker pool in Cloud Run.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `worker_pool_name`: Name of the worker pool.
  * `revision_name`: Name of the monitored revision.
  * `location`: Region where the worker pool is running.
  * `configuration_name`: Name of the configuration which created the monitored revision.



## `cloud_scheduler_job`

**Display name** : Cloud Scheduler Job

**Description** : A Cloud Scheduler Job.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The region of the job.
  * `job_id`: Identifier of the job.



## `cloud_tasks_queue`

**Display name** : Cloud Tasks Queue

**Description** : A queue in Cloud Tasks.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `queue_id`: The name of the queue.
  * `target_type`: The target type the queue is dispatching to.
  * `location`: The zone or region where the application is running.



## `cloudaicompanion.googleapis.com/Instance`

**Display name** : Gemini for Google Cloud Instance

**Description** : An instance resource that represents a Gemini for Google Cloud configuration.

**Labels** :

  * `resource_container`: The identifier of the GCP container associated with this resource.
  * `location`: The location of the resource.
  * `instance_id`: The ID of the instance resource.



## `cloudbuild.googleapis.com/Location`

**Display name** : Cloud Build Location

**Description** : A location in the Cloud Build API.

**Labels** :

  * `resource_container`: The identified of the GCP resource container associated with this resource, such as "my_project" or "organizations/5678".
  * `location`: Location of resource.



## `cloudcontrolspartner.googleapis.com/Location`

**Display name** : Location

**Description** : A Google Cloud Resource.

**Labels** :

  * `resource_container`: The identifier of the GCP container associated with the resource.
  * `location`: The region in which the job is running.



## `clouddeploy.googleapis.com/DeliveryPipeline`

**Display name** : Cloud Deploy Delivery Pipeline

**Description** : A Cloud Deploy Delivery Pipeline.

**Labels** :

  * `resource_container`: The identifier of the Google Cloud project associated with this resource.
  * `location`: The Google Cloud location where the resource resides.
  * `pipeline_id`: ID of the delivery pipeline resource.



## `cloudkms.googleapis.com/Project`

**Display name** : KMS project

**Description** : KMS project.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the resource.



## `cloudml_job`

**Display name** : Cloud ML Job

**Description** : A Google Cloud ML job.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `job_id`: An immutable identifier for a job.
  * `region`: Cloud ML region.



## `cloudml_model_version`

**Display name** : Cloud ML Model Version

**Description** : A Google Cloud ML model version.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `model_id`: An immutable identifier for a model.
  * `version_id`: An immutable identifier for a version.
  * `region`: Cloud ML region.



## `cloudsql.googleapis.com/InstanceClient`

**Display name** : Cloud SQL Instance Client

**Description** : A client connection to a Cloud SQL instance.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `resource_id`: The Cloud SQL instance identifier in the format of [project_name:instance_name].
  * `client_uid`: A unique identifier for the particular connector client.
  * `application_name`: The name of the application using the connector.
  * `region`: The GCP region in which the Cloud SQL instance is running.
  * `client_region`: The client region when the application is hosting on GCP, unknown if not on GCP.
  * `compute_platform`: Where the application is running, detected by the client based on runtime environment heuristics. string [cloud_build, cloud_run, appengine, gke, gce, unknown].
  * `connector_type`: Cloud SQL Connector type [java, go, python, nodejs].
  * `connector_version`: Cloud SQL Connector version.
  * `database_engine_type`: Database engine type [MySQL, PostgreSQL, SQL Server].



## `cloudsql_database`

**Display name** : Cloud SQL Database

**Description** : A Cloud SQL instance.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `database_id`: The Google Cloud SQL instance name.
  * `region`: The Google Cloud SQL region in which the database is running.



## `cloudsql_instance_database`

**Display name** : Cloud SQL Instance Database

**Description** : A database on a Cloud SQL instance.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: A GCP region or zone that this service agent is running in.
  * `resource_id`: The instance ID of the database.
  * `database`: The name of the database.



## `cloudtrace.googleapis.com/CloudtraceProject`

**Display name** : Cloud Trace

**Description** : Cloud trace resource, e.g. project.

**Labels** :

  * `resource_container`: The identifier of the GCP container associated with the resource.
  * `location`: The location that the Cloud Trace service recording the metrics is running.



## `cloudvolumesgcp-api.netapp.com/CloudVolume`

**Display name** : Monitored Resource for NetApp CVS

**Description** : Monitored Resource for NetApp CVS.

**Labels** :

  * `resource_container`: Project information.
  * `location`: Region/Zone information.
  * `volume_id`: ID of the volume.
  * `service_type`: Service type of the volume or replication relationship.
  * `name`: Name of the volume or replication relationship.



## `cloudvolumesgcp-api.netapp.com/CloudVolumePool`

**Display name** : Monitored Resource for NetApp CVS storage pool

**Description** : Monitored Resource for NetApp CVS storage pool.

**Labels** :

  * `resource_container`: Project information.
  * `pool_id`: ID of the storage pool.
  * `location`: Region/zone of the storage pool.



## `compute.googleapis.com/AcceleratorSlice`

**Display name** : AcceleratorSlice

**Description** : An Accelerator Slice

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `zone`: The zone of the GCP project associated with the accelerator slice.
  * `slice_id`: The obfuscated locus id of the slice.



## `compute.googleapis.com/FirewallPolicy`

**Display name** : Firewall policy

**Description** : Firewall policy.

**Labels** :

  * `resource_container`: The identifier of the GCP container (i.e. project or organization) associated with the firewall policy.
  * `location`: Location of the firewall policy.
  * `firewall_policy_id`: Firewall policy resource ID.



## `compute.googleapis.com/Interconnect`

**Display name** : Interconnect

**Description** : Interconnect.

**Labels** :

  * `resource_container`: The identifier of the GCP container (i.e. project) associated with the Interconnect.
  * `location`: Location of the Interconnect.
  * `interconnect_id`: Interconnect resource ID.



## `compute.googleapis.com/Location`

**Display name** : Compute Location

**Description** : A location in the Compute API.

**Labels** :

  * `resource_container`: The identifier of the GCP container (i.e. project) associated with the Compute Location.
  * `location`: Location of resource.



## `compute.googleapis.com/Machine`

**Display name** : Machine

**Description** : A Compute Engine Machine ID

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `zone`: The zone of the GCP project associated with the machine.
  * `machine_id`: The obfuscated ID of the machine



## `compute.googleapis.com/MrdmaNic`

**Display name** : MrdmaNic

**Description** : Collection of metrics for CX NICs.

**Labels** :

  * `resource_container`: The GCP project associated with the instance running the daemon.
  * `location`: The zone that the daemon is running in.
  * `instance_id`: The numerical ID of the GCE instance.



## `compute.googleapis.com/NetworkPathQuotasResource`

**Display name** : Network Path Quotas Resource

**Description** : Network Path Quotas Resource.

**Labels** :

  * `resource_container`: The GCP container associated with the metric.
  * `location`: Location for the quota.
  * `network_path_id`: The network path custom dimension.



## `compute.googleapis.com/OperationType`

**Display name** : Operation Type

**Description** : Operation Type.

**Labels** :

  * `resource_container`: The identifier of the GCP container (i.e. project) associated with the operation.
  * `location`: Location of the operation.
  * `operation_type`: Operation type.



## `compute.googleapis.com/PrivateServiceConnectEndpoint`

**Display name** : Private Service Connect Endpoint

**Description** : A Private Service Connect Service Endpoint.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `region`: The region where the service endpoint resides.
  * `psc_connection_id`: Unique identifier of the service endpoint.



## `compute.googleapis.com/Reservation`

**Display name** : Reservation

**Description** : Monitored resource representing a reservation.

**Labels** :

  * `resource_container`: The GCP container (e.g. project number) associated with the reservation.
  * `location`: The zone that contains the reservation.
  * `reservation_id`: Reservation resource ID.



## `compute.googleapis.com/ResourcePolicy`

**Display name** : Resource Policy

**Description** : Resource Policy.

**Labels** :

  * `resource_container`: The identifier of the GCP container (i.e. project) associated with the Resource Policy.
  * `location`: Location of the Resource Policy.
  * `resource_policy_id`: Resource Policy resource ID.



## `compute.googleapis.com/StoragePool`

**Display name** : Storage Pool

**Description** : Monitored resource representing a storage pool.

**Labels** :

  * `resource_container`: The GCP container (e.g. project number) associated with the storage pool.
  * `location`: The location that contains the storage pool.
  * `storage_pool_id`: Numerical resource ID of the storage pool.



## `compute.googleapis.com/VpcNetwork`

**Display name** : VPC Network

**Description** : VPC Network.

**Labels** :

  * `resource_container`: The identifier of the GCP container (i.e. project) associated with the VPC Network.
  * `location`: Location of the VPC Network, global always.
  * `network_id`: VPC Network resource ID.



## `compute.googleapis.com/Workload`

**Display name** : Workload

**Description** : A workload ID

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The zone of the GCP project associated with the instance.
  * `workload_id`: ID of monitored workload.
  * `replica_id`: ID of workload replica for this metric.



## `compute.googleapis.com/WorkloadProcess`

**Display name** : Workload Process

**Description** : A Workload Process ID

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The zone of the GCP project associated with the instance.
  * `workload_id`: ID of monitored workload.
  * `replica_id`: ID of workload replica for this metric.
  * `process_id`: Process identifier within the workload. Typically this is the process global rank.



## `connectors.googleapis.com/Connection`

**Display name** : Connectors

**Description** : Monitored resource for Connectors.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: GCP region location of the connection.
  * `connection`: The name of the connection.



## `consumed_api`

**Display name** : Consumed API

**Description** : An API used by customers.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as 'my-project'.
  * `service`: The API service name, such as 'cloudsql.googleapis.com'.
  * `method`: The API method name, such as 'disks.list'.
  * `version`: The API version, such as 'v1'.
  * `location`: The service specific notion of location. This can be a name of a zone or region. If a service does not have any notion of zones then 'global' can be used.
  * `credential_id`: The client credential ID, such as an API key ID or the OAuth client ID.



## `consumed_mcp_api`

**Display name** : Consumed MCP Method

**Description** : An MCP method used by customers.

**Labels** :

  * `resource_container`: The identifier of the GCP container associated with the resource, such as 'my-project' for GCP project.
  * `service`: Service that provides MCP tools, such as 'pubsub.googleapis.com'.
  * `method`: MCP method, such as 'tool/list', 'resource/list' or 'prompts/list'.
  * `primitive`: Name of the MCP primitive defined at https://modelcontextprotocol.io/docs/learn/architecture#primitives. Values can be tool, resource or prompts name, such as 'list_topics'.
  * `version`: The MCP tool version, such as 'v1'.
  * `location`: The service specific notion of location. This can be a name of a zone or region. If a service does not have any notion of zones then 'global' can be used.



## `consumer_quota`

**Display name** : Consumer Quota

**Description** : Quota used by consumers.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `service`: The name of the used service, such as "cloudsql.googleapis.com".
  * `location`: The location where the quota are consumed. It is a region for regional quota, or a zone for zonal quota, or "global" otherwise.



## `contactcenteraiplatform.googleapis.com/ContactCenter`

**Display name** : CCAI Platform Contact Center

**Description** : A CCAI Platform Contact Center instance.

**Labels** :

  * `resource_container`: Container of the current project.
  * `resource_id`: The identifier of the Contact Center instance.
  * `location`: The region in which the Contact Center is running.



## `contactcenterinsights.googleapis.com/Environment`

**Display name** : Contact Center AI Insights environment

**Description** : Contact Center AI Insights environment.

**Labels** :

  * `resource_container`: GCP project ID containing the resources for CCAI Insights.
  * `location`: Region where CCAI Insights is provisioned.



## `container.googleapis.com/Cluster`

**Display name** : Kubernetes Cluster Limits

**Description** : Kubernetes Cluster.

**Labels** :

  * `resource_container`: Project or organization.
  * `location`: Region or zone where the cluster was created.
  * `cluster_name`: Cluster name.



## `container.googleapis.com/NodePool`

**Display name** : GKE Node Pool

**Description** : GKE Node Pool.

**Labels** :

  * `resource_container`: Project or organization.
  * `location`: Region or zone where the cluster was created.
  * `cluster_name`: Cluster name.
  * `node_pool_name`: Node pool name.



## `contextawareaccess.googleapis.com/Location`

**Display name** : Location

**Description** : Access summary for risk based access levels.

**Labels** :

  * `resource_container`: The identifier of the Google Cloud organization associated with this resource.
  * `location`: The location of the resource.



## `csr_repository`

**Display name** : Cloud Source Repository

**Description** : A repository in Google Cloud Source Repositories.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `name`: The name of the repository.



## `databasecenter.googleapis.com/Resource`

**Display name** : Database Resource

**Description** : A database resource.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "my-project" or "organizations/123". The resource container must be in the format "projects/", or "organizations/". For more information, see https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy.
  * `location`: The location of the resource.
  * `resource_type`: The type of the resource.
  * `full_resource_name`: The full resource name of the resource.



## `dataflow.googleapis.com/Project`

**Display name** : Dataflow Project

**Description** : A project level monitored resource for Dataflow.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The location where Dataflow jobs are running.



## `dataflow_job`

**Display name** : Dataflow Job

**Description** : A Dataflow job.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `job_name`: The name of the job.
  * `region`: The region for the job.



## `dataflow_worker`

**Display name** : Dataflow worker

**Description** : A Dataflow worker.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The geographic location this worker is running in.
  * `job_name`: The name of the Dataflow job this worker belongs to.
  * `job_id`: Unique id of this instance of the dataflow job.
  * `worker_type`: A string identifying the type of worker/component producing this metric
  * `worker_id`: The ID of the worker, unique for this job_id and worker_type



## `dataform.googleapis.com/Repository`

**Display name** : Dataform Repository

**Description** : A Repository on Google Cloud Dataform.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "my-project".
  * `location`: The region in which the Repository is created.
  * `repository_id`: The user-specified ID of the Repository.



## `datafusion.googleapis.com/InstanceV2`

**Display name** : Cloud Data Fusion Instance

**Description** : An instance of Cloud Data Fusion.

**Labels** :

  * `resource_container`: The ID of the customer project.
  * `org_id`: The ID of the organization that the customer project belongs to.
  * `location`: The zone/region that the instance is hosted in.
  * `edition`: The edition of the instance.
  * `is_private_ip_enabled`: Does the instance use private IP.
  * `version`: The data plane version of the instance.
  * `instance_id`: The instance ID.
  * `namespace`: Name of the namespace.



## `datafusion.googleapis.com/InstanceV3`

**Display name** : Cloud Data Fusion Instance

**Description** : An instance of Cloud Data Fusion.

**Labels** :

  * `resource_container`: The ID of the customer project.
  * `location`: The zone/region that the instance is hosted in.
  * `edition`: The edition of the instance.
  * `is_private_ip_enabled`: Does the instance use private IP.
  * `version`: The data plane version of the instance.
  * `instance_id`: The instance ID.



## `datafusion.googleapis.com/PipelineV2`

**Display name** : Cloud Data Fusion Pipeline

**Description** : A deployed Pipeline in a Cloud Data Fusion instance.

**Labels** :

  * `resource_container`: The ID of the customer project.
  * `org_id`: The ID of the organization that the customer project belongs to.
  * `location`: The zone/region that the instance is hosted in.
  * `edition`: The edition of the instance.
  * `is_private_ip_enabled`: Does the instance use private IP.
  * `version`: The data plane version of the instance.
  * `instance_id`: The instance ID.
  * `namespace`: The namespace of the pipeline.
  * `pipeline_id`: The Pipeline ID.
  * `run_id`: The Run ID.



## `datamigration.googleapis.com/MigrationJob`

**Display name** : Database migration service migration job

**Description** : Database migration service migration job.

**Labels** :

  * `resource_container`: The resource container (project ID).
  * `location`: The location.
  * `migration_job_id`: The migration job ID.



## `dataplex.googleapis.com/Asset`

**Display name** : Cloud Dataplex Asset

**Description** : An Asset within a Cloud Dataplex Lake.

**Labels** :

  * `resource_container`: The identifier of GCP project associated with this resource.
  * `location`: The GCP region associated with this resource.
  * `lake_id`: The identifier of the Lake resource containing this resource.
  * `zone_id`: The identifier of the Zone resource containing this resource.
  * `asset_id`: The identifier of this Asset resource.



## `dataplex.googleapis.com/DataScan`

**Display name** : Cloud Dataplex DataScan

**Description** : A DataScan resource in Dataplex.

**Labels** :

  * `resource_container`: The identifier of GCP project associated with this resource.
  * `location`: The GCP region associated with this resource.
  * `datascan_id`: The identifier of this DataScan resource.



## `dataplex.googleapis.com/EntryLink`

**Display name** : Cloud Dataplex Glossary Entry Link Resource

**Description** : A Glossary Entry Link resource in Dataplex.

**Labels** :

  * `resource_container`: The identifier of GCP project associated with this resource.
  * `location`: The cloud region that contains the resource.
  * `entry_group_id`: The user-provided identifier for the entry group resource.
  * `entry_link_id`: The user-provided identifier for the entry link resource.



## `dataplex.googleapis.com/EntryLinkType`

**Display name** : Cloud Dataplex Entry Link Type Resource

**Description** : An Entry Link Type resource in Dataplex.

**Labels** :

  * `resource_container`: The identifier of GCP project associated with this resource.
  * `location`: The cloud region that contains the resource.
  * `entry_link_type_id`: The user-provided identifier for the entry link type resource.



## `dataplex.googleapis.com/Environment`

**Display name** : Cloud Dataplex Environment

**Description** : An Environment within a Cloud Dataplex Lake.

**Labels** :

  * `resource_container`: The identifier of GCP project associated with this resource.
  * `location`: The GCP region associated with this resource.
  * `lake_id`: The identifier of the Lake resource containing this resource.
  * `environment_id`: The identifier of this Environment resource.



## `dataplex.googleapis.com/Glossary`

**Display name** : Cloud Dataplex Glossary Resource

**Description** : A Glossary resource in Dataplex.

**Labels** :

  * `resource_container`: The identifier of GCP project associated with this resource.
  * `location`: The cloud region that contains the resource.
  * `glossary_id`: The user-provided identifier for the glossary resource.



## `dataplex.googleapis.com/GlossaryCategory`

**Display name** : Cloud Dataplex Glossary Category Resource

**Description** : A Glossary Category resource in Dataplex.

**Labels** :

  * `resource_container`: The identifier of GCP project associated with this resource.
  * `location`: The cloud region that contains the resource.
  * `glossary_id`: The user-provided identifier for the glossary resource.
  * `glossary_category_id`: The user-provided identifier for the glossary category resource.



## `dataplex.googleapis.com/GlossaryTerm`

**Display name** : Cloud Dataplex Glossary Term Resource

**Description** : A Glossary Term resource in Dataplex.

**Labels** :

  * `resource_container`: The identifier of GCP project associated with this resource.
  * `location`: The cloud region that contains the resource.
  * `glossary_id`: The user-provided identifier for the glossary resource.
  * `glossary_term_id`: The user-provided identifier for the glossary term resource.



## `dataplex.googleapis.com/GovernanceRule`

**Display name** : Cloud Dataplex Governance Rule

**Description** : A Governance rule resource in Dataplex.

**Labels** :

  * `resource_container`: The identifier of GCP project associated with this resource.
  * `location`: The cloud region that contains the resource.
  * `rule_id`: The user-provided identifier for the governance rule.



## `dataplex.googleapis.com/Lake`

**Display name** : Cloud Dataplex Lake

**Description** : A Cloud Dataplex Lake.

**Labels** :

  * `resource_container`: The identifier of GCP project associated with this resource.
  * `location`: The GCP region associated with this resource.
  * `lake_id`: The identifier of this Lake resource.



## `dataplex.googleapis.com/Project`

**Display name** : Cloud Dataplex Project.

**Description** : Cloud Dataplex Project.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the resource.



## `dataplex.googleapis.com/Task`

**Display name** : Cloud Dataplex Task

**Description** : A Task within a Cloud Dataplex Lake.

**Labels** :

  * `resource_container`: The identifier of GCP project associated with this resource.
  * `location`: The GCP region associated with this resource.
  * `lake_id`: The identifier of the Lake resource containing this resource.
  * `task_id`: The identifier of this Task resource.



## `dataplex.googleapis.com/Zone`

**Display name** : Cloud Dataplex Zone

**Description** : A Zone within a Cloud Dataplex Lake.

**Labels** :

  * `resource_container`: The identifier of GCP project associated with this resource.
  * `location`: The GCP region associated with this resource.
  * `lake_id`: The identifier of the Lake resource containing this resource.
  * `zone_id`: The identifier of this Zone resource.



## `datastore_request`

**Display name** : Datastore Request

**Description** : A request to Datastore from your App Engine application.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `module_id`: The module of the App Engine application that made this request.
  * `version_id`: The major version id of the App Engine application that made this request.



## `datastream.googleapis.com/Stream`

**Display name** : Datastream Stream

**Description** : A Datastream stream.

**Labels** :

  * `resource_container`: The resource container (project ID).
  * `location`: The location.
  * `stream_id`: The stream ID.



## `datastream.googleapis.com/StreamObject`

**Display name** : Datastream Stream Object

**Description** : A Datastream stream object.

**Labels** :

  * `resource_container`: The resource container (project ID).
  * `location`: The location.
  * `stream_id`: The stream ID.
  * `object_name`: The object name.



## `dell_emc_cloud_onefs_cluster`

**Display name** : Dell EMC Cloud OneFS Cluster

**Description** : Multi-protocol access to files and directories on GCP, Isilon Cloud OneFS clusters with SMB for Windows, and NFS for UNIX file systems.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The Google Cloud location in which the cluster is running.
  * `cluster_id`: Unique identifier of the cluster.



## `deprecated_resource`

**Display name** : Reserved

**Description** : Reserved.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `param1`: Reserved.
  * `param2`: Reserved.
  * `param3`: Reserved.
  * `param4`: Reserved.
  * `location`: Reserved.



## `dialogflow.googleapis.com/Location`

**Display name** : Dialogflow Location

**Description** : A Dialogflow Location (sometimes called Region).

**Labels** :

  * `resource_container`: The id of the GCP resource container associated with this resource.
  * `location`: Location of resource.



## `discoveryengine.googleapis.com/Agent`

**Display name** : Gemini Enterprise Agent

**Description** : A specific Agent resource within Gemini Enterprise, mapping to discoveryengine.googleapis.com/Agent.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud location where the Agent is located.
  * `assistant_id`: The unique identifier of the Assistant.
  * `engine_id`: The unique identifier of the Engine.
  * `agent_id`: The unique identifier of the Agent.



## `discoveryengine.googleapis.com/AgentToolInvocation`

**Display name** : Gemini Enterprise Agent Tool Invocation

**Description** : An Invocation of a specific Tool within the context of Gemini Enterprise Agent. This resource type is used for tracking tool-level metrics and latencies scoped to individual agents.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud location where the Tool is located.
  * `assistant_id`: The unique identifier of the Assistant using the tool.
  * `engine_id`: The unique identifier of the Engine where the tool is used.
  * `agent_id`: The unique identifier of the Agent using the tool.
  * `tool_id`: The unique identifier of the Tool.



## `discoveryengine.googleapis.com/DataConnector`

**Display name** : Gemini Enterprise Data Connector

**Description** : A specific Data Connector resource within Gemini Enterprise, mapping to discoveryengine.googleapis.com/DataConnector.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud location where the Data Connector is located.
  * `connector_id`: The unique identifier of the Data Connector.
  * `data_source`: Type of the Data Connector.



## `discoveryengine.googleapis.com/Engine`

**Display name** : Gemini Enterprise Engine

**Description** : A specific Engine (app) resource within Gemini Enterprise, mapping to discoveryengine.googleapis.com/Engine.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud location where the Engine is located.
  * `collection_id`: The Collection the Engine belongs to (e.g. default_collection).
  * `engine_id`: The unique identifier of the Engine.



## `discoveryengine.googleapis.com/LocalizedUser`

**Display name** : Monitored Resource for Localized Quota

**Description** : A monitored resource representing a user within a specific location, used for tracking and enforcing per-user quotas.

**Labels** :

  * `resource_container`: The GCP container associated with the metric.
  * `location`: Location for the quota.
  * `ge_user`: User who is assigned the quota.



## `discoveryengine.googleapis.com/Location`

**Display name** : Discovery Engine Location

**Description** : A Location in the discoveryengine API.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "my_project" or "organizations/5678".
  * `location`: Location of resource.



## `displayvideo.googleapis.com/Advertiser`

**Display name** : Display & Video 360 Advertiser.

**Description** : A single advertiser in Display & Video 360 (DV360).

**Labels** :

  * `resource_container`: The GCP container associated with the metric.
  * `location`: Location for the quota.
  * `advertiser_id`: The Advertiser ID custom dimension.



## `dns_managed_zone`

**Display name** : Managed DNS Zone

**Description** : A ManagedZone in the Google Cloud DNS service.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `zone_name`: The name of the ManagedZone.
  * `location`: The location field is provided for compatibility with other GCP services. Its value is always set to 'global'



## `dns_policy`

**Display name** : Cloud DNS Policy

**Description** : A Policy in the Google Cloud DNS service.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `policy_name`: The name of the Policy.
  * `location`: The location field is provided for compatibility with other GCP services. Its value is always set to 'global'



## `dns_query`

**Display name** : Cloud DNS Query

**Description** : A DNS query to a private DNS handled by the Google Cloud DNS service.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `target_name`: The DNS name managed by Cloud DNS to be resolved (e.g. the zone name, policy name, internal domain name). External names will have the value "external"
  * `location`: The GCP zone where the DNS request was received (e.g. us-east1, us-west1).
  * `target_type`: The target of the resolution of the DNS query (e.g. public-zone, private-zone, external).
  * `source_type`: Source of the query (e.g. gce-vm, internet).



## `dns_resource_record_set`

**Display name** : Cloud DNS Resource Record Set

**Description** : A ResourceRecordSet in the Google Cloud DNS service.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `name`: The name of the ResourceRecordSet.
  * `type`: The type of the ResourceRecordSet.
  * `location`: The GCP region where the ResourceRecordSet is located.



## `dns_response_policy`

**Display name** : Cloud DNS Response Policy

**Description** : A ResponsePolicy in the Google Cloud DNS service.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The GCP region where the ResponsePolicy is located.
  * `response_policy_name`: The name of the ResponsePolicy.



## `dns_response_policy_rule`

**Display name** : Cloud DNS Response Policy Rule

**Description** : A ResponsePolicyRule in the Google Cloud DNS service.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The GCP region where the ResponsePolicyRule is located.
  * `response_policy_name`: The name of the parent ResponsePolicy.
  * `response_policy_rule_name`: The name of the ResponsePolicyRule.



## `earthengine.googleapis.com/Project`

**Display name** : Earth Engine Cloud Project

**Description** : An Earth Engine Cloud Project.

**Labels** :

  * `resource_container`: The GCP project ID, such as "my-project".
  * `location`: The GCP location of the project.



## `edgecache.googleapis.com/EdgeCacheRouteRule`

**Display name** : Edge Cache Route Rule

**Description** : An Edge Cache route rule represents an Edge Cache Service's traffic as part of a Media Edge deployment.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: A GCP zone close to the proxy location. Please note that this may change over time.
  * `service_name`: The name of the EdgeCacheService.
  * `path_matcher_name`: The name of the PathMatcher that contains this route.
  * `matched_path`: The matched URL prefix, full URL path, or path template.
  * `route_type`: The type of the routed matched by the incoming request, one of [ORIGIN, URL_REDIRECT].
  * `route_destination`: The URL of the origin this request is to be proxied to.



## `edgecontainer.googleapis.com/EdgeCluster`

**Display name** : Cluster

**Description** : An Edge Container kubernetes cluster.

**Labels** :

  * `resource_container`: The identifier of the cluster GCP project associated with this resource.
  * `location`: The GCP location in which region this cluster resides.
  * `cluster_name`: The user given identifier of the cluster.



## `edgecontainer.googleapis.com/EdgeZone`

**Display name** : EdgeZone

**Description** : An Edge Container edge zone.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The GCP location that the edge zone is parented to.
  * `edge_zone`: The identifier of the edge zone.



## `edgecontainer.googleapis.com/Machine`

**Display name** : Machine

**Description** : An Edge Container machine.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The GCP location in which the Rack resides.
  * `machine_id`: The identifier of the machine.



## `edgecontainer.googleapis.com/Node`

**Display name** : Node

**Description** : An Edge Container cluster node.

**Labels** :

  * `resource_container`: The identifier of the cluster GCP project associated with this resource.
  * `location`: The GCP location in which region this cluster resides.
  * `cluster_name`: The user given identifier of the cluster the node runs in.
  * `node_name`: Automatically assigned identifier of the cluster node.
  * `machine_name`: The name of the machine the node runs on.



## `edgecontainer.googleapis.com/Rack`

**Display name** : Rack

**Description** : An Edge Container rack.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The GCP location in which the Rack resides.
  * `rack_id`: The identifier of the rack.



## `eventarc.googleapis.com/Location`

**Display name** : Eventarc Location

**Description** : A localized count in the Eventarc API.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "my-project" or "organizations/123".
  * `location`: The location of the service.



## `faulttesting.googleapis.com/Experiment`

**Display name** : Fault Injection Experiment

**Description** : Experiment associated with a template to inject faults.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource (project_id), such as "my-project" or "organizations/123".
  * `location`: The location in which the Fault Injection Experiment is present.
  * `experiment_id`: The ID of the Experiment.



## `filestore_instance`

**Display name** : Filestore Instance

**Description** : A Filestore instance.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The physical location of the instance.
  * `instance_name`: The name for the Filestore instance.



## `financialservices.googleapis.com/BacktestResult`

**Display name** : Financial Services Backtest Result

**Description** : A BacktestResult within the Financial Services API.

**Labels** :

  * `resource_container`: The identifier of the GCP container associated with this resource.
  * `location`: The GCP location associated with this resource (e.g., us-central1).
  * `instance_id`: The FinServ instance that contains this resource (e.g., test-instance).
  * `backtest_result_id`: BacktestResult ID (e.g., test-backtest-result).



## `financialservices.googleapis.com/EngineConfig`

**Display name** : Financial Services Engine Config

**Description** : An EngineConfig within the Financial Services API.

**Labels** :

  * `resource_container`: The identifier of the GCP container associated with this resource.
  * `location`: The GCP location associated with this resource (e.g., us-central1).
  * `instance_id`: The FinServ instance that contains this resource (e.g., test-instance).
  * `engine_config_id`: EngineConfig ID (e.g., test-engine-config).



## `financialservices.googleapis.com/Instance`

**Display name** : Financial Services Instance

**Description** : An Instance within the Financial Services API.

**Labels** :

  * `resource_container`: The identifier of the GCP container associated with this resource.
  * `location`: The GCP location associated with this resource (e.g., us-central1).
  * `instance_id`: Instance ID (e.g., test-instance).



## `financialservices.googleapis.com/PredictionResult`

**Display name** : Financial Services Prediction Result

**Description** : A PredictionResult within the Financial Services API.

**Labels** :

  * `resource_container`: The identifier of the GCP container associated with this resource.
  * `location`: The GCP location associated with this resource (e.g., us-central1).
  * `instance_id`: The FinServ instance that contains this resource (e.g., test-instance).
  * `prediction_result_id`: PredictionResult ID (e.g., test-prediction-result).



## `firebase_auth`

**Display name** : Firebase Auth Project

**Description** : A Firebase Auth Project.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".



## `firebase_domain`

**Display name** : Firebase Hosting Site Domain

**Description** : A domain from which a Firebase Hosting site is serving traffic.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as 'my-project'.
  * `site_name`: The name of a Firebase Hosting site, that is the subdomain in .web.app.
  * `domain_name`: The default subdomain (on web.app or firebaseapp.com) or custom domain from which content was served.



## `firebase_namespace`

**Display name** : Firebase Realtime Database

**Description** : A Firebase Realtime Database.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `table_name`: The name of the database.
  * `location`: The location of the database.



## `firebaseappcheck.googleapis.com/Instance`

**Display name** : Firebase App Check Instance

**Description** : Monitored resource for Firebase App Check instances.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: Location where Firebase App Check is provisioned (always set to "global").
  * `app_id`: Firebase Application ID. If the application cannot be identified from a request, the value "UNKNOWN" is used.
  * `service_id`: The service reporting Firebase App Check metrics.



## `firebaseappcheck.googleapis.com/Resource`

**Display name** : Firebase App Check Resource

**Description** : Monitored resource for Firebase App Check target resources.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: Location where Firebase App Check is provisioned (always set to "global").
  * `service_id`: The service reporting Firebase App Check metrics.
  * `target_resource`: The resource for which Firebase App Check was verified.



## `firebaseappcheck.googleapis.com/Service`

**Display name** : Firebase App Check Service

**Description** : Monitored resource for Firebase App Check services.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: Location where Firebase App Check is provisioned (always set to "global").
  * `service_id`: The service reporting Firebase App Check metrics.



## `firebaseapphosting.googleapis.com/Backend`

**Display name** : Firebase App Hosting Backend

**Description** : A Firebase App Hosting Backend.

**Labels** :

  * `resource_container`: The GCP container (usually project ID) for the App Hosting Backend.
  * `location`: The serving locality of the App Hosting Backend, such as "global" or "us-central1". For v1 backends, this will be "global".
  * `backend_id`: An identifier for the App Hosting Backend within a project.



## `firebasecrashlytics.googleapis.com/App`

**Display name** : Firebase Crashlytics App

**Description** : A Firebase client using Crashlytics.

**Labels** :

  * `resource_container`: The Firebase project for the application.
  * `location`: Location for Firebase Apps is global.
  * `app_id`: A Firebase App ID.



## `firebasedataconnect.googleapis.com/Connector`

**Display name** : Firebase SQL Connect Connector

**Description** : A Firebase SQL Connect Connector.

**Labels** :

  * `resource_container`: The GCP container associated with the connector.
  * `location`: The GCP region that contains the connector.
  * `service_id`: The Firebase SQL Connect service ID.
  * `connector_id`: The Firebase SQL Connect connector ID. For arbitrary operations executed via GraphqlService, connector_id is inferred from RPC name, e.g., (executeGraphql), (executeGraphqlRead), (introspectGraphql).



## `firebasedataconnect.googleapis.com/Service`

**Display name** : Firebase SQL Connect Service

**Description** : A Firebase SQL Connect Service.

**Labels** :

  * `resource_container`: The GCP container associated with the service.
  * `location`: The GCP region that contains the service.
  * `service_id`: The service ID.



## `firebaseextensions.googleapis.com/ExtensionVersion`

**Display name** : Firebase Extension Version

**Description** : A published version of a Firebase extension.

**Labels** :

  * `resource_container`: The GCP project number used to publish the extension.
  * `location`: Location of the published Firebase extension version (always set to "global").
  * `publisher`: The publisher of the published extension.
  * `extension`: The name of the published extension.
  * `version`: The version of the published extension.



## `firebaseremoteconfig.googleapis.com/Project`

**Display name** : Remote Config Project

**Description** : Firebase Remote Config Project.

**Labels** :

  * `resource_container`: The GCP container associated with the project.
  * `location`: The location of the project.



## `firebasevertexai.googleapis.com/Model`

**Display name** : Firebase AI Logic Model

**Description** : A Model supported by Firebase AI Logic.

**Labels** :

  * `resource_container`: The GCP container associated with the model.
  * `location`: The zone that served the model.
  * `publisher_id`: The publisher ID of the model, such as "google".
  * `model_id`: The model ID, such as "gemini-0.0-flash-002".



## `firebasevertexai.googleapis.com/PromptTemplate`

**Display name** : Firebase AI Logic Server Prompt Template

**Description** : A Firebase AI Logic Server Prompt Template.

**Labels** :

  * `resource_container`: The GCP container associated with the prompt template.
  * `location`: The region that served the prompt template.
  * `template_id`: The prompt template ID.



## `firestore.googleapis.com/Database`

**Display name** : Firestore Database

**Description** : A Firestore Database.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the database.
  * `database_id`: The database id.



## `firestore_instance`

**Display name** : Firestore Instance

**Description** : An instance of the Cloud Firestore database.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".



## `fleetengine.googleapis.com/DeliveryFleet`

**Display name** : Fleet Engine Last Mile Fleet Solution

**Description** : A top-level resource for Fleet Engine Last Mile Fleet Solution metrics and logs.

**Labels** :

  * `resource_container`: The identifier of the GCP container associated with DeliveryFleet.
  * `location`: The region in which the Fleet Engine instance is running.



## `fleetengine.googleapis.com/Fleet`

**Display name** : Fleet Engine On Demand Rides and Deliveries

**Description** : A top-level resource for Fleet Engine On Demand Rides and Deliveries metrics and logs.

**Labels** :

  * `resource_container`: The identifier of the GCP container associated with Fleet.
  * `location`: The region in which the Fleet Engine instance is running.



## `fpnv.googleapis.com/Project`

**Display name** : Firebase PNV Project

**Description** : A Firebase project using the Firebase PNV service.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the GCP project, always 'global'.



## `gae_app`

**Display name** : GAE Application

**Description** : An application running in Google App Engine (GAE).

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `module_id`: The service/module name.
  * `version_id`: The version name.
  * `zone`: The GAE zone where the application is running.



## `gae_instance`

**Display name** : GAE Instance

**Description** : A single instance of a Google App Engine (GAE) version.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `module_id`: The service/module name.
  * `version_id`: The version name.
  * `instance_id`: The instance id.
  * `location`: App Engine's external notion of location.



## `gateway_scope`

**Display name** : Gateway Scope

**Description** : GatewayScope represents a set of Gateways with the same merged configs.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The location of the control plane
  * `scope`: The name of the gateway_scope



## `gce_backend_service`

**Display name** : Cloud Load Balancing Backend Service

**Description** : A Compute Engine backend service.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `backend_service_id`: Unique identifier of the backend service.
  * `location`: Global or Compute Engine region containing the backend service



## `gce_disk`

**Display name** : Disk

**Description** : A disk belonging to a Compute Engine instance.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `disk_id`: Unique identifier of the disk.
  * `zone`: The Compute Engine zone where the disk resides.



## `gce_forwarding_rule`

**Display name** : Forwarding Rule

**Description** : A Google Compute Engine Forwarding Rule.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `region`: The region where the forwarding rule resides.
  * `forwarding_rule_id`: Unique identifier of the forwarding rule.



## `gce_instance`

**Display name** : VM Instance

**Description** : A virtual machine instance hosted in Compute Engine.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `instance_id`: The numeric VM instance identifier assigned by Compute Engine.
  * `zone`: The Compute Engine zone in which the VM is running.



## `gce_network`

**Display name** : Network

**Description** : A Compute Engine network.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `network_id`: Unique identifier of the network.



## `gce_network_endpoint_group`

**Display name** : Network Endpoint Group

**Description** : A Compute Engine network endpoint group resource.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `zone`: The name of the zone where the network endpoint group is located.
  * `network_endpoint_group_id`: The ID of the network endpoint group.



## `gce_network_region`

**Display name** : Network Region

**Description** : A region of a Compute Engine network.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `network_id`: The ID of the Compute Engine network.
  * `region`: The name of the network region.



## `gce_node_group`

**Display name** : Node Group

**Description** : A Compute Engine node group.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `node_group_id`: Unique identifier of the node group.
  * `zone`: Zone of the node group.



## `gce_node_template`

**Display name** : Node Template

**Description** : A Compute Engine node template.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `node_template_id`: Unique identifier of the node template.
  * `region`: Region of the node template.



## `gce_resource_policy`

**Display name** : Resource Policy

**Description** : A Compute Engine resource policy.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `resource_policy_id`: Unique identifier of the resource policy.
  * `region`: Region of the resource policy.



## `gce_router`

**Display name** : Cloud Router

**Description** : A Cloud Router instance.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `router_id`: The router identifier.
  * `region`: The region where the router instance is located.



## `gce_service_attachment`

**Display name** : Service Attachment

**Description** : A Private Service Connect Service Attachment.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `region`: The region where the service attachment resides.
  * `service_attachment_id`: Unique identifier of the service attachment.



## `gce_subnetwork`

**Display name** : Subnetwork

**Description** : A Compute Engine subnetwork.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `subnetwork_id`: The unique numerical identifier of the subnetwork.
  * `subnetwork_name`: The unique user provided name of the subnetwork.
  * `location`: Location of the resource.



## `gce_zone_network_health`

**Display name** : Zone Network Health

**Description** : Data concerning the networking related health of a Compute Engine zone

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `zone`: The Compute Engine zone being monitored.
  * `region`: The Compute Engine region the zone belongs to.



## `gcs_bucket`

**Display name** : GCS Bucket

**Description** : A Google Cloud Storage (GCS) bucket.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `bucket_name`: An immutable name of the bucket.
  * `location`: Location of the bucket.



## `geminidataanalytics.googleapis.com/Agent`

**Display name** : Data Cloud Agent

**Description** : A Data Cloud Agent.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the GCP project associated with this resource.
  * `agent_id`: The DataAgent ID (e.g., GDA Agent ID).



## `geminidataanalytics.googleapis.com/Location`

**Display name** : Gemini Data Analytics Location

**Description** : A Gemini Data Analytics Location.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the GCP project associated with this resource.



## `geminidataanalytics.googleapis.com/User`

**Display name** : Data Cloud User

**Description** : A Data Cloud User.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the GCP project associated with this resource.
  * `user_id`: The Data Cloud User ID.



## `generativelanguage.googleapis.com/Location`

**Display name** : Location

**Description** : Location.

**Labels** :

  * `resource_container`: The id of the GCP resource container associated with this resource.
  * `location`: Location of resource.



## `generic_node`

**Display name** : Generic Node

**Description** : A generic node identifies a machine or other computational resource for which no more specific resource type is applicable. The label values must uniquely identify the node.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The Google Cloud region or zone that determines where data about the resource is stored. For example, "us-east1-a".
  * `namespace`: A namespace identifier, such as a cluster name.
  * `node_id`: A unique identifier for the node within the namespace, such as a hostname or IP address.



## `generic_task`

**Display name** : Generic Task

**Description** : A generic task identifies an application process for which no more specific resource is applicable, such as a process scheduled by a custom orchestration system. The label values must uniquely identify the task.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The Google Cloud region or zone that determines where data about the resource is stored. For example, "us-east1-a".
  * `namespace`: A namespace identifier, such as a cluster name.
  * `job`: An identifier for a grouping of related tasks, such as the name of a microservice or distributed batch job.
  * `task_id`: A unique identifier for the task within the namespace and job, such as a replica index identifying the task within the job.



## `gke_container`

**Display name** : GKE Container

**Description** : A Google Kubernetes Engine (GKE) container instance.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `cluster_name`: The name for the cluster the container is running in.
  * `namespace_id`: The identifier for the cluster namespace the container is running in.
  * `instance_id`: The identifier for the Compute Engine instance the container is running in.
  * `pod_id`: The identifier for the pod the container is running in.
  * `container_name`: The name of the container.
  * `zone`: The zone for the instance.



## `gkebackup.googleapis.com/BackupPlan`

**Display name** : GKE Backup Plan

**Description** : A backup plan provides configuration, location, and management functions for a sequence of backups.

**Labels** :

  * `resource_container`: The identifier of the Google Cloud container associated with the resource.
  * `location`: The Google Cloud location where this backupPlan resides.
  * `backup_plan_id`: The name of the backupPlan.



## `gkebackup.googleapis.com/RestorePlan`

**Display name** : GKE Restore Plan

**Description** : A restore plan defines the configuration of a series of restore operations to be performed against backups which belong to the specified backup plan.

**Labels** :

  * `resource_container`: The identifier of the Google Cloud container associated with the resource.
  * `location`: The Google Cloud location where this restorePlan resides.
  * `restore_plan_id`: The name of the restorePlan.



## `global`

**Display name** : Global

**Description** : A resource type that is not associated with any specific resource.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".



## `google_service_gce_client`

**Display name** : Google Service VM Client

**Description** : A set of definitions for Compute Engine to Google-Service behavior.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `zone`: The zone of the instance.
  * `instance_id`: The VM instance id.
  * `instance_name`: The name of the virtual machine.
  * `region`: The region of the instance.
  * `resource_type`: Possible values GCE_VM/OTHER. GCE_VM mean the that traffic was oriented from a Compute Engine VM where OTHER mean the traffic comes from VPN/INTERCONNECT or other location type



## `health.googleapis.com/Subscriber`

**Display name** : Health API Subscriber

**Description** : A subscriber of the Google Health API to receive data change notifications.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the resource.
  * `subscriber_id`: The identifier of the subscriber which is unique per GCP Project.



## `healthcare_pipeline_job`

**Display name** : Healthcare Pipeline Job

**Description** : A Cloud Healthcare Pipeline Job.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The Google Cloud location of the dataset that contains the Pipeline Job.
  * `dataset_id`: The ID of the dataset.
  * `pipeline_job_id`: The ID of the Pipeline Job.



## `http_external_regional_lb_rule`

**Display name** : Regional External Application Load Balancer Rule

**Description** : A resource descriptor for regional external Application Load Balancer behavior.

**Labels** :

  * `project_id`: The identifier of the Google Cloud project associated with this resource, such as 'my-project'.
  * `network_name`: The name of the customer network in which the Load Balancer resides.
  * `region`: The region under which the Load Balancer is defined.
  * `url_map_name`: The name of the urlmap.
  * `forwarding_rule_name`: The name of the forwarding rule.
  * `target_proxy_name`: The name of the target HTTP/S proxy.
  * `matched_url_path_rule`: The prefix of URL defined in urlmap tree. 'UNMATCHED' for the sink default rule.
  * `backend_target_name`: The name of the backend target or service.
  * `backend_target_type`: The type of the backend target. Can be 'BACKEND_SERVICE', or 'UNKNOWN' if the backend wasn't assigned.
  * `backend_name`: The name of the backend group. Can be '' if the backend wasn't assigned.
  * `backend_type`: The type of the backend group. Can be 'INSTANCE_GROUP', 'NETWORK_ENDPOINT_GROUP', or 'UNKNOWN' if the backend wasn't assigned.
  * `backend_scope`: The scope of the backend group. Can be 'UNKNOWN' if the backend wasn't assigned.
  * `backend_scope_type`: The type of the scope of the backend group. Can be 'ZONE', 'REGION', or 'UNKNOWN' in case the backend wasn't assigned.



## `https_lb_rule`

**Display name** : Global External Application Load Balancer Rule

**Description** : A set of definitions for HTTP/S load balancing behavior.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `region`: The region on which HTTP/S Load Balancer is applied, such as 'global' or 'us-central1'. Various other objects are defined per that locality.
  * `url_map_name`: The name of the urlmap.
  * `forwarding_rule_name`: The name of the forwarding rule.
  * `target_proxy_name`: The name of the target HTTP/S proxy.
  * `matched_url_path_rule`: The prefix of URL defined in urlmap tree. 'UNMATCHED' for the sink default rule.
  * `backend_target_name`: The name of the backend target - service or bucket.
  * `backend_target_type`: The type of the backend target. Can be either 'BACKEND_SERVICE' or 'BACKEND_BUCKET'.
  * `backend_name`: The name of the backend group. Can be a special value if the backend wasn't assigned.
  * `backend_type`: The type of the backend group. Can be 'INSTANCE_GROUP', 'NETWORK_ENDPOINT_GROUP', or a special value if the backend wasn't assigned.
  * `backend_scope`: The scope (zone-name or region-name) of the backend group. Can be a special value if the backend wasn't assigned. Can be empty if there is no response from the backend.
  * `backend_scope_type`: The type of the scope of the backend group. Can be 'ZONE', 'REGION' or other special value in case the backend wasn't assigned.



## `hypercomputecluster.googleapis.com/Cluster`

**Display name** : Cluster

**Description** : A Cluster Director Cluster.

**Labels** :

  * `resource_container`: The project ID of the cluster.
  * `location`: The location of the cluster.
  * `cluster_id`: The ID of the cluster.



## `iam.googleapis.com/Location`

**Display name** : AccessPolicy Parent

**Description** : The parent of the AccessPolicy.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with the AccessPolicy, such as "my-project" or "organizations/123".
  * `location`: The location of the AccessPolicy.



## `iam.googleapis.com/WorkforcePoolProvider`

**Display name** : Workforce Identity Pool Provider

**Description** : A workforce identity pool provider.

**Labels** :

  * `resource_container`: The identifier of the Google Cloud organization associated with this resource.
  * `location`: The location of the resource.
  * `pool_id`: The ID of the provider's workforce pool parent resource.
  * `provider_id`: The ID of the workforce pool provider resource.



## `iam.googleapis.com/WorkloadIdentityPoolProvider`

**Display name** : Workload Identity Pool Provider

**Description** : A workload identity pool provider.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource, such as 'my-project'.
  * `location`: The location of the resource.
  * `pool_id`: The ID of the provider's workload identity pool parent resource.
  * `provider_id`: The ID of the workload identity pool provider resource.



## `iam_service_account`

**Display name** : IAM Service Account

**Description** : An IAM Service Account.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as 'my-project'.
  * `unique_id`: The unique_id of the service account.



## `identitytoolkit_project`

**Display name** : Project

**Description** : An Identity Toolkit project.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource.



## `identitytoolkit_tenant`

**Display name** : Identity Toolkit Tenant

**Description** : An Identity Toolkit tenant.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource.
  * `tenant_name`: The name of the tenant.



## `ids.googleapis.com/Endpoint`

**Display name** : IDS Endpoint

**Description** : A Cloud IDS Endpoint.

**Labels** :

  * `resource_container`: The identifier of the GCP project owning the Endpoint.
  * `location`: The zone of the IDS Endpoint.
  * `id`: The ID of the Endpoint.



## `instance_group`

**Display name** : Instance Group

**Description** : A group of VM instances.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The zone or region of the instance group.
  * `instance_group_id`: The identifier of the instance group.
  * `instance_group_name`: The name of the instance group.



## `integrations.googleapis.com/IntegrationVersion`

**Display name** : Integration Version

**Description** : An integration version to be executed.

**Labels** :

  * `resource_container`: The project id.
  * `location`: The location value.
  * `product`: The product value.
  * `integration`: The integration name.
  * `version`: The version id of the integration.



## `interconnect`

**Display name** : Interconnect

**Description** : A physical connection to Google at a datacenter.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `interconnect`: The unique identifier of the interconnect.



## `interconnect_attachment`

**Display name** : Interconnect Attachment

**Description** : A VLAN attaching a cloud network to an Interconnect.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `attachment`: The unique identifier of the attachment.
  * `interconnect`: The unique identifier of the interconnect that the attachment connects to.
  * `region`: The cloud region that the attachment connects to.
  * `interconnect_project`: The name of the project that owns interconnect that the attachment connects to.



## `internal_http_lb_rule`

**Display name** : Internal Application Load Balancer Rule

**Description** : A resource descriptor for internal Application Load Balancer behavior.

**Labels** :

  * `project_id`: The identifier of the Google Cloud project associated with this resource, such as 'my-project'.
  * `network_name`: The name of the customer network in which the Load Balancer resides.
  * `region`: The region under which the Load Balancer is defined.
  * `url_map_name`: The name of the urlmap.
  * `forwarding_rule_name`: The name of the forwarding rule.
  * `target_proxy_name`: The name of the target HTTP(S) proxy.
  * `matched_url_path_rule`: The prefix of URL defined in urlmap tree. 'UNMATCHED' for the sink default rule.
  * `backend_target_name`: The name of the backend target or service.
  * `backend_target_type`: The type of the backend target. Can be 'BACKEND_SERVICE', or 'UNKNOWN' if the backend wasn't assigned.
  * `backend_name`: The name of the backend group. Can be '' if the backend wasn't assigned.
  * `backend_type`: The type of the backend group. Can be 'INSTANCE_GROUP', 'NETWORK_ENDPOINT_GROUP', or 'UNKNOWN' if the backend wasn't assigned.
  * `backend_scope`: The scope of the backend group. Can be 'UNKNOWN' if the backend wasn't assigned.
  * `backend_scope_type`: The type of the scope of the backend group. Can be 'ZONE', 'REGION', or 'UNKNOWN' in case the backend wasn't assigned.



## `internal_tcp_lb_rule`

**Display name** : Internal Passthrough TCP Network Load Balancer Rule

**Description** : A set of definitions for internal TCP load balancing behavior.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `region`: The region of the backend target.
  * `network_name`: The name of the virtual network.
  * `backend_target_type`: The type of the backend target that handled the connection. Currently it's 'BACKEND_SERVICE'.
  * `backend_target_name`: The name of the backend target that handled the connection (equivalent to 'load_balancer_name').
  * `load_balancer_name`: The name of the load balancer.
  * `forwarding_rule_name`: The name of the forwarding rule.
  * `backend_name`: The name of the backend group that handled the connection.
  * `backend_type`: The type of the backend group that handled the connection. Can be 'INSTANCE_GROUP' or 'NETWORK_ENDPOINT_GROUP'.
  * `backend_scope`: The scope (zone or region) of the backend group that handled the connection.
  * `backend_scope_type`: The type of the scope of the backend group that handled the connection. Can be either 'ZONE' or 'REGION'.
  * `backend_subnetwork_name`: The name of the subnetwork of the backend.



## `internal_udp_lb_rule`

**Display name** : Internal Passthrough UDP Network Load Balancer Rule

**Description** : A set of definitions for internal UDP load balancing behavior.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `region`: The region of the backend target.
  * `network_name`: The name of the virtual network.
  * `backend_target_type`: The type of the backend target that handled the connection. Currently it's 'BACKEND_SERVICE'.
  * `backend_target_name`: The name of the backend target that handled the connection (equivalent to 'load_balancer_name').
  * `load_balancer_name`: The name of the load balancer.
  * `forwarding_rule_name`: The name of the forwarding rule.
  * `backend_name`: The name of the backend group that handled the connection.
  * `backend_type`: The type of the backend group that handled the connection. Can be 'INSTANCE_GROUP' or 'NETWORK_ENDPOINT_GROUP'.
  * `backend_scope`: The scope (zone or region) of the backend group that handled the connection.
  * `backend_scope_type`: The type of the scope of the backend group that handled the connection. Can be either 'ZONE' or 'REGION'.
  * `backend_subnetwork_name`: The name of the subnetwork of the backend.



## `istio_canonical_service`

**Display name** : Istio Canonical Service

**Description** : An Istio Canonical Service represents a group of related workloads (example: Kubernetes Deployment) that communicate with other workload groups in an Istio service mesh.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `mesh_uid`: Unique identifier for an Istio service mesh.
  * `namespace_name`: The name of the namespace that the service is running in.
  * `canonical_service_name`: The name of the canonical service.
  * `location`: The physical location of the workload instance that is running the service.
  * `revision`: Immutable version of the service. This may be a semantic versioning level version or git SHA or similar.



## `istio_control_plane`

**Display name** : Istio Control Plane

**Description** : An Istio Control Plane is an instance of a service that provides xDS and related functionality to a set of managed Istio proxies.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `mesh_uid`: Unique identifier for an Istio service mesh.
  * `location`: The physical location in which the workload for the Control Plane is located.
  * `revision`: Immutable revision of Istio managed by the Control Plane.
  * `build_id`: Immutable build tag for the instance of the Control Plane.
  * `owner`: Immutable name of the owner of the Control Plane.



## `k8s_cluster`

**Display name** : Kubernetes Cluster

**Description** : A Kubernetes cluster. It contains Kubernetes audit logs from the cluster.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The physical location of the cluster.
  * `cluster_name`: The name of the cluster.



## `k8s_container`

**Display name** : Kubernetes Container

**Description** : A Kubernetes container instance.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The physical location of the cluster that contains the container.
  * `cluster_name`: The name of the cluster that the container is running in.
  * `namespace_name`: The name of the namespace that the container is running in.
  * `pod_name`: The name of the pod that the container is running in.
  * `container_name`: The name of the container.



## `k8s_control_plane_component`

**Display name** : Kubernetes Control Plane Component

**Description** : A Kubernetes Control Plane component.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The physical location of the cluster that contains the control plane component.
  * `cluster_name`: The name of the cluster that the control plane component is running in.
  * `component_name`: The name of the control plane component.
  * `component_location`: The physical location where the control plane component is running.



## `k8s_entity`

**Display name** : Kubernetes Entity

**Description** : A Kubernetes entity.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The physical location of the cluster that contains the nodepool.
  * `cluster_name`: The name of the cluster that the nodepool is in.
  * `entity_type`: The type of the entity.
  * `entity_namespace`: The namespace of the entity.
  * `entity_name`: The name of the entity.
  * `entity_uid`: The uid of the entity.



## `k8s_node`

**Display name** : Kubernetes Node

**Description** : A Kubernetes node instance.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The physical location of the cluster that contains the node.
  * `cluster_name`: The name of the cluster that the node is a part of.
  * `node_name`: The name of the node.



## `k8s_node_pool`

**Display name** : Kubernetes Nodepool

**Description** : A Kubernetes nodepool instance.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The physical location of the cluster that contains the nodepool.
  * `cluster_name`: The name of the cluster that the nodepool is in.
  * `node_pool_name`: The name of the nodepool.



## `k8s_pod`

**Display name** : Kubernetes Pod

**Description** : A Kubernetes pod instance.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The physical location of the cluster that contains the pod.
  * `cluster_name`: The name of the cluster that the pod is running in.
  * `namespace_name`: The name of the namespace that the pod is running in.
  * `pod_name`: The name of the pod.



## `k8s_scale`

**Display name** : Kubernetes Scale

**Description** : A Kubernetes object that can be targeted by Kubernetes autoscalers.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The physical location of the cluster that contains the scaled object.
  * `cluster_name`: The name of the cluster that the scaled object is in.
  * `namespace_name`: The name of the namespace that the scaled object is in.
  * `controller_api_group_name`: The name of the api group of the scaled object, such as "core".
  * `controller_kind`: The kind of the scaled object, such as "Deployment".
  * `controller_name`: The name of the scaled object.



## `k8s_service`

**Display name** : Kubernetes Service

**Description** : A Kubernetes Service instance.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The physical location of the cluster that contains the service.
  * `cluster_name`: The name of the cluster that the service is running in.
  * `namespace_name`: The name of the namespace that the service is running in.
  * `service_name`: The name of the service.



## `knative_broker`

**Display name** : Cloud Run for Anthos Broker

**Description** : A Knative broker in Cloud Run for Anthos.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: Location where the broker is running.
  * `cluster_name`: Name of the GKE cluster.
  * `namespace_name`: Name of the namespace.
  * `broker_name`: Name of the broker.



## `knative_revision`

**Display name** : Cloud Run for Anthos Revision

**Description** : A Knative revision in Cloud Run for Anthos.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `service_name`: Name of the service.
  * `revision_name`: Name of the monitored revision.
  * `location`: Location where the service is running.
  * `configuration_name`: Name of the configuration which created the monitored revision.
  * `cluster_name`: Name of the GKE cluster.
  * `namespace_name`: Name of the namespace.



## `knative_trigger`

**Display name** : Cloud Run for Anthos Trigger

**Description** : A Knative trigger in Cloud Run for Anthos.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: Location where the broker is running.
  * `cluster_name`: Name of the GKE cluster.
  * `namespace_name`: Name of the namespace.
  * `broker_name`: Name of the broker the trigger is associated with.
  * `trigger_name`: Name of the trigger.



## `l4_proxy_rule`

**Display name** : Proxy Network Load Balancer Rule

**Description** : A resource descriptor for proxy Network Load Balancer behavior.

**Labels** :

  * `project_id`: The identifier of the Google Cloud project associated with this resource, such as 'my-project'.
  * `network_name`: The name of the customer network in which the Load Balancer resides.
  * `region`: The region under which the Load Balancer is defined.
  * `load_balancing_scheme`: The load balancing scheme associated with the forwarding rule, one of [INTERNAL_MANAGED, EXTERNAL_MANAGED].
  * `protocol`: The protocol associated with the traffic processed by the proxy, one of [TCP, UDP, SSL, UNKNOWN].
  * `forwarding_rule_name`: The name of the forwarding rule.
  * `target_proxy_name`: The name of the target proxy.
  * `backend_target_name`: The name of the backend target or service.
  * `backend_target_type`: The type of the backend target, one of ['BACKEND_SERVICE'; 'UNKNOWN' - if the backend wasn't assigned].
  * `backend_name`: The name of the backend group. Can be '' if the backend wasn't assigned.
  * `backend_type`: The type of the backend group, one of ['INSTANCE_GROUP'; 'NETWORK_ENDPOINT_GROUP'; 'UNKNOWN' - if the backend wasn't assigned].
  * `backend_scope`: The scope of the backend group. Can be 'UNKNOWN' if the backend wasn't assigned.
  * `backend_scope_type`: The type of the scope of the backend group, one of ['ZONE'; 'REGION'; 'UNKNOWN' - in case the backend wasn't assigned].



## `l7_lb_rule`

**Display name** : Application Load Balancer Rule (Logs-based Metrics)

**Description** : A set of definitions for HTTP load balancing behavior used for logs-based metrics.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `forwarding_rule_name`: The name of the forwarding rule.
  * `target_proxy_name`: The name of the target proxy.
  * `target_proxy_type`: The type of the target proxy.
  * `url_map_name`: The name of the urlmap.
  * `matched_url_path_rule`: The prefix of URL defined in urlmap tree.
  * `backend_name`: The name of the backend.
  * `backend_type`: The type of the backend.
  * `instance_group_name`: The name of the instance group.
  * `backend_zone`: The zone of the instance group.



## `livestream.googleapis.com/Channel`

**Display name** : Live Stream API Channel

**Description** : A Live Stream API Channel.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this channel resource.
  * `location`: The GCP location where the channel resource resides.
  * `channel_id`: ID of the channel resource.



## `load_balancer_backend`

**Display name** : Load Balancer Backend

**Description** : A backend group of the load balancer.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `backend_service_name`: The user-specified backend service name.
  * `location`: Global or the region containing the backend service.
  * `backend_group_project_id`: The numeric project number of the backend group. This is to support cross-project NEG backends. Normally this is identical to the backend service project number.
  * `backend_group_name`: The user-specified backend group name.
  * `backend_group_type`: The type of the backend group. Can be INSTANCE_GROUP or NETWORK_ENDPOINT_GROUP.
  * `backend_group_location`: The zone of the backend group, for regional backend groups this will be the region.



## `loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule`

**Display name** : External Passthrough Network Load Balancer Rule

**Description** : A set of definitions for multi protocol network load balancing behavior.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `region`: The Google Cloud Platform region of the backend instance that connected to network load balancing forwarding rule.
  * `backend_network_name`: The network name of the NIC of the instance that received the Net LB flow.
  * `backend_target_type`: The type of the backend target that handled the connection.
  * `backend_service_name`: The name of the backend service that handled the connection.
  * `primary_target_pool`: The name of the primary target pool.
  * `target_pool`: The name of the target pool.
  * `forwarding_rule_name`: The name of the forwarding rule.
  * `backend_group_name`: The name of the backend group that handled the connection.
  * `backend_group_type`: The type of the backend group that handled the connection.
  * `backend_group_scope`: The scope (zone or region) of the backend group that handled the connection.
  * `backend_subnetwork_name`: The name of the subnetwork of the instance that handled the connection.
  * `backend_zone`: The zone of the endpoint (VM instance) that handled the connection.



## `loadbalancing.googleapis.com/InternalNetworkLoadBalancerRule`

**Display name** : Internal Passthrough Network Load Balancer Rule

**Description** : A set of definitions for multi protocol internal load balancing behavior.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `region`: The Google Cloud Platform region of the backend instance that connected to network load balancing forwarding rule.
  * `backend_network_name`: The network name of the NIC of the instance that received the Net LB flow.
  * `backend_service_name`: The name of the backend service that handled the connection.
  * `forwarding_rule_name`: The name of the forwarding rule.
  * `backend_group_name`: The name of the backend group that handled the connection.
  * `backend_group_type`: The type of the backend group that handled the connection.
  * `backend_group_scope`: The scope (zone or region) of the backend group that handled the connection.
  * `backend_subnetwork_name`: The name of the subnetwork of the instance that handled the connection.



## `logging_bucket`

**Display name** : Logging Bucket

**Description** : An export bucket in Cloud Logging.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `bucket_id`: The name of the log bucket.
  * `location`: The location of the log bucket.
  * `source_resource_container`: The source resource container (e.g. project, folder, organization) of the log entry that is destined for the log bucket. The format is "projects/project_id"
  * `monitored_resource_type`: The type field of the monitored resource in the log entry that is destined for the log bucket.



## `logging_exclusion`

**Display name** : Log Exclusion

**Description** : An exclusion in Cloud Logging.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `name`: The unique name of the exclusion.



## `logging_sink`

**Display name** : Logging export sink

**Description** : An export sink in Cloud Logging.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `name`: The unique name of the sink.
  * `destination`: The destination of the sink.



## `lustre.googleapis.com/Instance`

**Display name** : Lustre instance

**Description** : A Lustre Instance.

**Labels** :

  * `resource_container`: The identifier of the GCP consumer project associated with this resource, such as 'my-project'.
  * `location`: The Google Cloud location in which the managed instance is running.
  * `instance_id`: The ID of the managed instance.



## `lustre.googleapis.com/Job`

**Display name** : Lustre client job

**Description** : A Lustre client job.

**Labels** :

  * `resource_container`: The identifier of the GCP consumer project associated with this resource, such as 'my-project'.
  * `location`: The Google Cloud location in which the managed instance is running.
  * `instance_id`: The ID of the managed instance.
  * `job_id`: The string representation of the remote process running on the client.



## `lustre.googleapis.com/Location`

**Display name** : Lustre location

**Description** : A Lustre Location.

**Labels** :

  * `resource_container`: The identifier of the GCP consumer project associated with this resource, such as 'my-project'.
  * `location`: The Google Cloud location in which the managed instance is running.



## `lustre.googleapis.com/QuotaEntity`

**Display name** : Lustre Quota Entity

**Description** : A specific entity (user, group, or project) on a Lustre target for which quota is tracked within a Lustre instance.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud location in which the instance is running.
  * `instance_id`: The ID of the Lustre instance.
  * `id`: The identifier for the accounting_type type (e.g., UID, GID).



## `managedflink.googleapis.com/Deployment`

**Display name** : Managed Flink Deployment

**Description** : A managed Flink cluster.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the GCP project associated with this resource.
  * `deployment_id`: The user-specified or system generated deployment identifier.



## `managedflink.googleapis.com/Job`

**Display name** : Managed Flink Job

**Description** : A job running on a deployment.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the GCP project associated with this resource.
  * `deployment_id`: The user-specified or system generated deployment identifier.
  * `job_id`: The system-generated job identifier.



## `managedflink.googleapis.com/Operator`

**Display name** : Managed Flink Operator

**Description** : A Flink operator.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the GCP project associated with this resource.
  * `deployment_id`: The user-specified or system generated deployment identifier.
  * `job_id`: The system-generated job identifier.
  * `operator_id`: The system-generated operator identifier.



## `managedflink.googleapis.com/Vertex`

**Display name** : Managed Flink Vertex

**Description** : A Flink vertex.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the GCP project associated with this resource.
  * `deployment_id`: The user-specified or system generated deployment identifier.
  * `job_id`: The system-generated job identifier.
  * `vertex_id`: The system-generated vertex identifier.



## `managedkafka.googleapis.com/Cluster`

**Display name** : Apache Kafka Cluster

**Description** : A Managed Kafka cluster.

**Labels** :

  * `resource_container`: The identifier of the project or container associated with this cluster.
  * `location`: The region in which the cluster is created.
  * `cluster_id`: The user-specified cluster id.



## `managedkafka.googleapis.com/ConnectCluster`

**Display name** : Apache Kafka Connect Cluster

**Description** : A Managed Kafka Connect cluster.

**Labels** :

  * `resource_container`: The identifier of the project or container associated with this cluster.
  * `location`: The region in which the cluster is created.
  * `cluster_id`: The user-specified cluster id.



## `managedkafka.googleapis.com/Connector`

**Display name** : Apache Kafka Connect Connector

**Description** : A Managed Kafka Connect Connector.

**Labels** :

  * `resource_container`: The identifier of the project or container associated with this cluster.
  * `location`: The region in which the cluster is created.
  * `cluster_id`: The user-specified cluster id.
  * `connector_id`: The user-specified connector id.



## `managedkafka.googleapis.com/Location`

**Display name** : Apache Kafka Location

**Description** : A Managed Kafka location.

**Labels** :

  * `resource_container`: The identifier of the project or container associated with this location.
  * `location`: The location in the API.



## `managedkafka.googleapis.com/SchemaRegistry`

**Display name** : Apache Kafka Schema Registry

**Description** : A Managed Kafka Schema Registry.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this schema registry.
  * `location`: The region in which the schema registry is created.
  * `schema_registry_id`: The user-specified schema registry id.



## `managedkafka.googleapis.com/Topic`

**Display name** : Apache Kafka Topic

**Description** : A Kafka topic.

**Labels** :

  * `resource_container`: The identifier of the project or container associated with this topic.
  * `location`: The region in which the topic is created.
  * `cluster_id`: The user-specified cluster id to which the topic belongs.
  * `topic_id`: The user-specified topic id.



## `managedkafka.googleapis.com/TopicPartition`

**Display name** : Apache Kafka Topic Partition

**Description** : A Kafka topic partition.

**Labels** :

  * `resource_container`: The identifier of the project or container associated with this partition.
  * `location`: The region in which the partition is created.
  * `cluster_id`: The user-specified cluster id to which the partition belongs.
  * `topic_id`: The user-specified topic id to which the partition belongs.
  * `partition_index`: The index of the partition.



## `managedkafka.googleapis.com/TopicPartitionConsumerGroup`

**Display name** : Apache Kafka Topic Partition Consumer Group

**Description** : A Kafka consumer group along with the topic partition from which it is consuming.

**Labels** :

  * `resource_container`: The identifier of the project or container associated with this topic partition consumer group.
  * `location`: The region in which the partition and consumer group are created.
  * `cluster_id`: The user-specified cluster id to which the partition and consumer group belong.
  * `topic_id`: The user-specified topic id to which the partition belongs.
  * `partition_index`: The index of the partition.
  * `consumer_group_id`: The user-specified consumer group id.



## `maps.googleapis.com/Api`

**Display name** : Google Maps API

**Description** : Google Maps API availability and latency.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `service`: The Google Maps API in use.
  * `version`: The version of the service that handled the request.
  * `location`: The Google Cloud region where the request was processed (e.g. us-east1, us-west1-a).
  * `method`: The Google Maps API method in use.
  * `credential_id`: The credential ID (API key or project number) used to call the Maps API.



## `memcache_node`

**Display name** : Memorystore Memcached Node

**Description** : A node of a Memorystore Memcached instance.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: Google Cloud zone where the Memcached node is located
  * `instance_id`: Customer given identifier unique among Memcached instances in the region that this node belongs to.
  * `node_id`: Name of this Memcached node which is unique within a single Memcached instance.



## `memorystore.googleapis.com/Instance`

**Display name** : Memorystore Instance

**Description** : An instance hosted on Google Cloud Memorystore.

**Labels** :

  * `resource_container`: The identifier of the GCP consumer project associated with this resource, such as 'my-project'.
  * `location`: The Google Cloud region in which the managed instance is running.
  * `instance_id`: The ID of the managed instance.
  * `instance_uid`: Identifier assigned by Google to uniquely distinguish an instance.



## `memorystore.googleapis.com/InstanceNode`

**Display name** : Memorystore Instance Node

**Description** : An Instance node hosted on Google Cloud Memorystore.

**Labels** :

  * `resource_container`: The identifier of the GCP consumer project associated with this resource, such as 'my-project'.
  * `location`: The Google Cloud zone in which the managed cluster node is running.
  * `instance_id`: The ID of the managed instance.
  * `instance_uid`: Identifier assigned by Google to uniquely distinguish an instance.
  * `node_id`: Identifier assigned by Valkey to uniquely distinguish a node.
  * `shard_id`: Identifier assigned by Valkey to uniquely distinguish a shard.



## `mesh`

**Display name** : Mesh

**Description** : A mesh serves as the "key" to deliver configuration to data plane proxy instances.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The location of the control plane
  * `mesh`: The name of the mesh



## `metastore.googleapis.com/Federation`

**Display name** : Dataproc Metastore Federation

**Description** : A Dataproc Metastore Federation.

**Labels** :

  * `resource_container`: The ID of the customer project.
  * `location`: The region that the federation is hosted in.
  * `federation_id`: The federation ID.



## `metastore.googleapis.com/Service`

**Display name** : Dataproc Metastore Service

**Description** : A Dataproc Metastore Service.

**Labels** :

  * `resource_container`: The ID of the customer project.
  * `location`: The region that the service is hosted in.
  * `service_id`: The service ID.



## `metric`

**Display name** : Metric Type

**Description** : A Stackdriver Monitoring metric type.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `name`: The name of the metric type, such as "logging.googleapis.com/my-metric-name".



## `microsoft_ad_domain`

**Display name** : Microsoft Active Directory Domain

**Description** : A Microsoft Active Directory Domain hosted and managed by Google Cloud Platform

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `fqdn`: The fully qualified domain name of the Active Directory Domain
  * `location`: The location where Active Directory Domain resources (like VMs, etc.) are present.



## `modelarmor.googleapis.com/SanitizeOperation`

**Display name** : Model Armor Sanitize Operation

**Description** : A resource that represents the Model Armor sanitize operations.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "my_project" or "organizations/5678".
  * `location`: The GCP location.
  * `template_id`: The template ID.



## `modelarmor.googleapis.com/Template`

**Display name** : Model Armor Template

**Description** : A resource that represents the Model Armor template operations.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "my_project" or "organizations/5678".
  * `location`: The GCP location.
  * `template_id`: The template ID.



## `monitoring.googleapis.com/MetricIngestionAttribution`

**Display name** : Metric Ingestion Attribution

**Description** : Attribution for metric ingestion.

**Labels** :

  * `resource_container`: The identifier of the GCP project to which the metric is written, such as 'my-project'.
  * `location`: The location of the resource that the metric ingestion was associated with, unless it was 'global', in which case this will be the cloud region where the metric was received.
  * `attribution_dimension`: The dimension used for attribution reporting. It is not recommended that aggregations are performed across dimensions because a single metric point can be recorded with multiple dimensions which could cause double counting. Currently only "namespace" and "cluster" are supported.
  * `attribution_id`: The attribution id of the source of the metric write.



## `monitoring.googleapis.com/MetricStatistics`

**Display name** : (DEPRECATED) Metric Statistics

**Description** : Information about a user-written metric in Cloud Monitoring. This resource is deprecated. Please refer to https://cloud.google.com/monitoring/docs/metrics-management#diagnostics and https://cloud.google.com/monitoring/docs/metrics-management#view-summary for how monitor the ingestion of metrics.

**Labels** :

  * `resource_container`: The identifier of the GCP project to which the metric is written, such as 'my-project'.
  * `location`: The cloud region where the metric was received.
  * `metric_type`: The metric type.



## `nat_gateway`

**Display name** : Cloud NAT Gateway

**Description** : A Cloud NAT Gateway.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `region`: The region where the NAT gateway is located.
  * `router_id`: Identifier of the router under which the NAT gateway is defined.
  * `gateway_name`: The name of the NAT gateway.



## `netapp.googleapis.com/Replication`

**Display name** : Google Cloud NetApp Volumes Replication

**Description** : Google Cloud NetApp Volumes Replication.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: Replication source region/zone.
  * `name`: Name of the replication relationship.



## `netapp.googleapis.com/StoragePool`

**Display name** : Google Cloud NetApp Volumes StoragePool

**Description** : Google Cloud NetApp Volumes StoragePool.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: StoragePool region/zone.
  * `name`: Name of the storage pool.



## `netapp.googleapis.com/Volume`

**Display name** : Google Cloud NetApp Volumes Volume

**Description** : Google Cloud NetApp Volumes Volume.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: Volume region/zone.
  * `name`: Name of the volume.



## `netapp_cloud_volume`

**Display name** : NetApp Cloud Volume

**Description** : A specific volume in the NetApp Cloud Volumes service.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The Google Cloud location in which the NetApp Cloud Volume instance is running.
  * `volume_id`: The ID of a NetApp Volume.



## `network_security_policy`

**Display name** : Network Security Policy

**Description** : A network security policy.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The region where the security policy resides. For global security policies this is "global".
  * `policy_name`: The unique user provided name of the security policy.



## `networkactions.googleapis.com/Extension`

**Display name** : Media CDN Service Extension

**Description** : Extension represents a Service Extensions resource in Media CDN.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the Service Extensions resource.
  * `resource_name`: The name of the Service Extensions resource.
  * `resource_type`: The type of Service Extensions resource according to the API. Only CdnEdgeExtensio is supported for now.
  * `attachment_scope`: Defines the scope this extension is being applied to. Only EdgeCacheService is supported for now.



## `networkactions.googleapis.com/WasmPluginVersion`

**Display name** : Media CDN Wasm Plugin Version

**Description** : A single immutable version of a Media CDN WasmPlugin (code + runtime config).

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of this service. Only 'global' is allowed.
  * `plugin_name`: The name of the WasmPlugin.
  * `plugin_version`: The name of the WasmPluginVersion.



## `networkconnectivity.googleapis.com/Group`

**Display name** : Network Connectivity Group

**Description** : A group associated with a Network Connectivity hub.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this group.
  * `location`: The identifier of the location that this group is in.
  * `hub_id`: The identifier of the hub that is associated with this group.
  * `group_id`: The identifier of this group.



## `networkconnectivity.googleapis.com/Hub`

**Display name** : Network Connectivity Hub

**Description** : A Network Connectivity hub.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container that this hub is in.
  * `location`: The identifier of the location that this hub is in.
  * `hub_id`: The identifier of this hub.



## `networkconnectivity.googleapis.com/RouteTable`

**Display name** : Network Connectivity Route Table

**Description** : A route table associated with a Network Connectivity hub.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this route table.
  * `location`: The identifier of the location that this route table is in.
  * `hub_id`: The identifier of the hub that is associated with this route table.
  * `route_table_id`: The identifier of this route table.



## `networkconnectivity.googleapis.com/Spoke`

**Display name** : Spoke

**Description** : A Network Connectivity Center Spoke resource.

**Labels** :

  * `resource_container`: The identifier of the GCP project owning the NCC spoke.
  * `location`: The location of the NCC spoke.
  * `id`: The user-specified identifier of the NCC spoke.



## `networkconnectivity.googleapis.com/Transport`

**Display name** : Transport

**Description** : A Partner CCI Transport resource.

**Labels** :

  * `resource_container`: The identifier of the GCP project owning the transport.
  * `location`: The location of the transport.
  * `id`: The user-specified identifier of the transport.



## `networking.googleapis.com/Location`

**Display name** : GCP Location

**Description** : A GCP location: a specific zone or region, or "global".

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: Name of a GCP zone/region, or "global".



## `networkmanagement.googleapis.com/MonitoringPoint`

**Display name** : Monitoring Point

**Description** : A Monitoring Point in Cloud Network insights.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "projects/123456789".
  * `location`: The location of the Monitoring Point resource.
  * `network_monitoring_provider_id`: Identifier of the network monitoring provider.
  * `monitoring_point_id`: Identifier of the Monitoring Point.



## `networkmanagement.googleapis.com/NetworkMonitoringProvider`

**Display name** : Network Monitoring Provider

**Description** : A Network Monitoring Provider in Cloud Network insights.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "projects/123456789".
  * `location`: The location of the NetworkMonitoringProvider resource.
  * `network_monitoring_provider_id`: Identifier of the network monitoring provider.



## `networkmanagement.googleapis.com/NetworkPath`

**Display name** : Network Path

**Description** : A Network Path in Cloud Network insights.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "projects/123456789".
  * `location`: The location of the NetworkPath resource.
  * `network_monitoring_provider_id`: Identifier of the network monitoring provider.
  * `path_id`: Identifier of the network path.



## `networkmanagement.googleapis.com/WebPath`

**Display name** : Web Path

**Description** : A Web Path in Cloud Network insights.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "projects/123456789".
  * `location`: The location of the WebPath resource.
  * `network_monitoring_provider_id`: Identifier of the network monitoring provider.
  * `path_id`: Identifier of the web path.



## `networksecurity.googleapis.com/DnsThreatDetector`

**Display name** : DNS Threat Detector

**Description** : A GCP network and Cloud Region indicating the location where a DNS threat was detected.

**Labels** :

  * `resource_container`: The identifier of the GCP project for the threat event.
  * `id`: ID of the DNS Threat Detector resource.
  * `location`: The origin Cloud Region of the DNS query analyzed by Protective DNS.



## `networksecurity.googleapis.com/FirewallEndpoint`

**Display name** : Firewall Endpoint

**Description** : A Cloud Firewall Endpoint.

**Labels** :

  * `resource_container`: The identifier of the GCP organization or project owning the Firewall Endpoint.
  * `location`: The zone of the Firewall Endpoint.
  * `id`: The ID of the Firewall Endpoint.



## `networksecurity.googleapis.com/Location`

**Display name** : Network Security Location

**Description** : A location in the Network Security API.

**Labels** :

  * `resource_container`: The identitifier of the GCP resource container associated with this resource, such as "my_project" or "organizations/5678".
  * `location`: Location of resource.



## `networksecurity.googleapis.com/MirroringEndpointNetwork`

**Display name** : Mirroring endpoint network

**Description** : A pairing of a mirroring endpoint and a mirrored network associated to it.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with the mirroring endpoint.
  * `location`: The location of the GCP container associated with the mirroring endpoint.
  * `endpoint_id`: Endpoint resource ID.
  * `network_container`: The identifier of the GCP container associated with the network.
  * `network_location`: The location of the GCP container associated with the network.
  * `network_id`: Network resource ID.



## `networksecurity.googleapis.com/PartnerSSEGateway`

**Display name** : Partner SSE Gateway

**Description** : A Cloud Partner SSE Gateway resource.

**Labels** :

  * `resource_container`: The identifier of the GCP project owning the SSE Gateway.
  * `location`: The region of the Partner SSE Gateway.
  * `id`: The ID of the Partner SSE Gateway.
  * `vni`: The virtual network identifier of the Partner SSE Gateway.



## `networksecurity.googleapis.com/ProtectedEndpoint`

**Display name** : Protected Network Endpoint

**Description** : An endpoint (identified by IP) protected by Cloud Armor Managed Protection.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The region on which the protected endpoint resides, such as 'global' or 'us-central1'. 
  * `vip`: The virtual IP address of the protected endpoint. When multiple representations are possible, the IETF canonical representation (e.g., RFC 5952) is used. 



## `networksecurity.googleapis.com/RegionalNetworkSecurityPolicy`

**Display name** : Regional Network Security Policy

**Description** : A regional network security policy.

**Labels** :

  * `resource_container`: The GCP project associated with this resource.
  * `location`: The GCP location that contains this security policy.
  * `policy_name`: The user provided name of this security policy.



## `networksecurity.googleapis.com/SSEGateway`

**Display name** : SSE Gateway

**Description** : DEPRECATED: This monitored resource has been replaced by networkconnectivity.googleapis.com/Spoke.

**Labels** :

  * `resource_container`: The identifier of the GCP project owning the SSE Gateway.
  * `location`: The region of the SSE Gateway.
  * `id`: The ID of the SSE Gateway.



## `networkservices.googleapis.com/Extension`

**Display name** : Service Extensions

**Description** : Extension represents a Service Extensions resource.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the Service Extensions resource.
  * `resource_name`: The name of the Service Extensions resource.
  * `resource_type`: The type of Service Extensions resource according to the API (e.g. LbTrafficExtension).
  * `attachment_scope`: Defines the scope this extension is being applied to.



## `networkservices.googleapis.com/Gateway`

**Display name** : Gateway

**Description** : A Gateway represents a single gateway resource.

**Labels** :

  * `resource_container`: The GCP container associated with the gateway.
  * `location`: The region name in which the Gateway is defined.
  * `network_name`: The name of the VPC network in which the Gateway was created.
  * `gateway_type`: The type enum of the Gateway.
  * `gateway_name`: The name of the Gateway resource.



## `networkservices.googleapis.com/Location`

**Display name** : Network Services Location

**Description** : A location in the Network Services API.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource.
  * `location`: Location of resource.



## `networkservices.googleapis.com/MulticastDomain`

**Display name** : Multicast Domain

**Description** : A Cloud Multicast domain.

**Labels** :

  * `resource_container`: The project number of the multicast domain.
  * `location`: Fixed to "global".
  * `multicast_domain_id`: The user defined name of the multicast domain.



## `networkservices.googleapis.com/MulticastGroup`

**Display name** : Multicast Group

**Description** : Multicast Group.

**Labels** :

  * `resource_container`: The multicast administrator project number, prefixed by "projects/".
  * `location`: Fixed to "global".
  * `multicast_domain_id`: The user defined name of the multicast domain the group range is associated with.
  * `multicast_group_range_id`: The user defined name of the multicast group range.
  * `multicast_ip`: The IP address used in this multicast group.



## `networkservices.googleapis.com/WasmPluginVersion`

**Display name** : Wasm Plugin Version

**Description** : A single immutable version of a WasmPlugin (code + runtime config).

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of this service.
  * `plugin_name`: The name of the WasmPlugin.
  * `plugin_version`: The name of the WasmPluginVersion.



## `nodemanagement.googleapis.com/GoldkeyResource`

**Display name** : Goldkey Resource

**Description** : A Goldkey resource managed by the Builder stack.

**Labels** :

  * `resource_container`: The GCP project number owning the resource.
  * `location`: The deployment location of the resource.
  * `resource_id`: The unique ID of the resource.
  * `resource_type`: Type of the resource.



## `oracledatabase.googleapis.com/AutonomousDatabase`

**Display name** : Autonomous Database

**Description** : Monitored resource representing a Autonomous Database.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the Autonomous database is running.
  * `autonomous_database_id`: The identifier of the Autonomous database.



## `oracledatabase.googleapis.com/CloudExadataInfrastructure`

**Display name** : Exadata Infrastructure

**Description** : Monitored resource representing a Oracle Exadata infrastrucure.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the Exadata infrastrucure is running.
  * `cloud_exadata_infrastructure_id`: The identifier of the CloudExadataInfrastructure resource.



## `oracledatabase.googleapis.com/CloudVmCluster`

**Display name** : Cloud VM cluster

**Description** : Monitored resource representing a Cloud VM Cluster in Oracle Exadata infrastrucure.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the cluster is running.
  * `cloud_exadata_infrastructure_id`: The Cloud exadata infrastrucure id in which this cluster is hosted.
  * `cloud_vm_cluster_id`: The identifier of the CloudVmCluster resource.



## `oracledatabase.googleapis.com/ContainerDatabase`

**Display name** : Container Database

**Description** : Monitored resource representing a Container Database in Cloud VM Cluster.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the cluster is running.
  * `cloud_exadata_infrastructure_id`: The Cloud exadata infrastrucure id in which this cluster is hosted.
  * `cloud_vm_cluster_id`: The identifier of the CloudVmCluster resource.
  * `container_database_name`: Name of the ContainerDatabase.



## `oracledatabase.googleapis.com/DbSystem`

**Display name** : Db System

**Description** : Monitored resource representing a DbSystem.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the cluster is running.
  * `db_system_id`: The identifier of the DbSystem resource.



## `oracledatabase.googleapis.com/DbSystemContainerDatabase`

**Display name** : DbSystem Container Database

**Description** : Monitored resource representing a DbSystem Container Database.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the cluster is running.
  * `db_system_id`: The identifier of the CloudVmCluster resource.
  * `container_database_name`: Name of the ContainerDatabase.



## `oracledatabase.googleapis.com/DbSystemPluggableDatabase`

**Display name** : DbSystem Pluggable Database

**Description** : Monitored resource representing a DbSystem Pluggable Database in a VM Cluster.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the cluster is running.
  * `db_system_id`: The identifier of the CloudVmCluster resource.
  * `container_database_name`: Name of the ContainerDatabase.
  * `pluggable_database_name`: Name of the PluggableDatabase.



## `oracledatabase.googleapis.com/ExadbContainerDatabase`

**Display name** : Exadb Container Database

**Description** : Monitored resource representing a ExadbContainer Database in Cloud VM Cluster.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the cluster is running.
  * `exadb_vm_cluster_id`: The identifier of the CloudVmCluster resource.
  * `container_database_name`: Name of the ContainerDatabase.



## `oracledatabase.googleapis.com/ExadbPluggableDatabase`

**Display name** : Exadb Pluggable Database

**Description** : Monitored resource representing a Exadb Pluggable Database in a VM Cluster.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the cluster is running.
  * `exadb_vm_cluster_id`: The identifier of the CloudVmCluster resource.
  * `container_database_name`: Name of the ContainerDatabase.
  * `pluggable_database_name`: Name of the PluggableDatabase.



## `oracledatabase.googleapis.com/ExadbVmCluster`

**Display name** : ExaDB VM Cluster

**Description** : Monitored resource representing an Exascale DB VM Cluster.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the cluster is running.
  * `exadb_vm_cluster_id`: The identifier of the ExadbVmCluster resource.



## `oracledatabase.googleapis.com/ExascaleDbStorageVault`

**Display name** : ExaDB Storage Vault

**Description** : Monitored resource representing ExascaleDb Storage Vault.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the cluster is running.
  * `exascale_db_storage_vault_id`: The identifier of the ExascaleDbStorageVault resource.



## `oracledatabase.googleapis.com/GoldengateDeployment`

**Display name** : Goldengate Deployment

**Description** : Monitored resource representing a Goldengate Deployment.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the deployment is running.
  * `gg_deployment_id`: The identifier of the Goldengate Deployment resource.



## `oracledatabase.googleapis.com/PluggableDatabase`

**Display name** : Pluggable Database

**Description** : Monitored resource representing a Pluggable Database in a VM Cluster.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The Google Cloud region in which the cluster is running.
  * `cloud_exadata_infrastructure_id`: The Cloud exadata infrastrucure id in which this cluster is hosted.
  * `cloud_vm_cluster_id`: The identifier of the CloudVmCluster resource.
  * `container_database_name`: Name of the ContainerDatabase.
  * `pluggable_database_name`: Name of the PluggableDatabase.



## `osconfig.googleapis.com/PatchJob`

**Display name** : Patch Job

**Description** : A patch job ran by VM Manager.

**Labels** :

  * `resource_container`: The GCP project associated with the patch job.
  * `location`: The location that contains the patch job.
  * `id`: Id uniquely identifying the patch job.



## `parallelstore.googleapis.com/Instance`

**Display name** : Parallelstore Instance

**Description** : A Parallelstore instance.

**Labels** :

  * `resource_container`: The GCP container associated with the instance.
  * `location`: The physical location of the instance, a zone.
  * `instance_id`: The name of the Parallelstore instance.



## `privateca.googleapis.com/CertificateAuthority`

**Display name** : Certificate Authority

**Description** : A managed Certificate Authority.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The Cloud region where the Certificate Authority is located.
  * `ca_pool_id`: The Certificate Authority Pool ID.
  * `certificate_authority_id`: The Certificate Authority ID.



## `processor_version`

**Display name** : Cloud Document AI Processor Version

**Description** : Cloud Document AI Processor Version

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The Google Cloud location where the ProcessorVersion is located.
  * `processor_type`: The type of the processor. For example, "CUSTOM_EXTRACTION_PROCESSOR".
  * `processor_id`: The ID of the processor.
  * `processor_version_id`: The ID of the processor version.



## `produced_api`

**Display name** : Produced API with consumer dimension

**Description** : An API provided by the producer with consumer dimension.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as 'my-project'.
  * `service`: The API service name, such as 'cloudsql.googleapis.com'.
  * `method`: The API method name, such as 'disks.list'.
  * `version`: The API version, such as 'v1'.
  * `location`: The service specific notion of location. This can be a name of a zone or region. If a service does not have any notion of zones then 'global' can be used.
  * `consumer_id`: This is the ID of a consumer project that's made a request to the API, such as project number '412016889367'.



## `producer_quota`

**Display name** : Producer Quota

**Description** : Quota provided by the service producer.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `service`: The name of the service, such as "cloudsql.googleapis.com".
  * `location`: The location where the quota are consumed. It is a region for regional quota, or a zone for zonal quota, or "global" otherwise.
  * `consumer_resource_node`: The resource node consuming quota. For projects, it is the project number. For other resource nodes like folders and organzations, it must have type prefix, such as "organizations/12345".



## `prometheus_target`

**Display name** : Prometheus Target

**Description** : A Prometheus Target identifies a target monitored by Google Cloud Managed Service for Prometheus.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The Google Cloud region or zone that determines where data about the resource is stored. For example, "us-east1-a".
  * `cluster`: The GKE cluster or related concept.
  * `namespace`: The GKE namespace or related concept.
  * `job`: The job label of the Prometheus target.
  * `instance`: The instance label of the Prometheus target.



## `pubsub_snapshot`

**Display name** : Cloud Pub/Sub Snapshot

**Description** : A snapshot in Google Cloud Pub/Sub.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `snapshot_id`: The identifier of the snapshot, such as "my-snapshot".



## `pubsub_subscription`

**Display name** : Cloud Pub/Sub Subscription

**Description** : A subscription in Google Cloud Pub/Sub.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `subscription_id`: The identifier of the subscription, such as "my-subscription".



## `pubsub_topic`

**Display name** : Cloud Pub/Sub Topic

**Description** : A topic in Google Cloud Pub/Sub.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `topic_id`: The identifier of the topic, such as "my-topic".



## `pubsublite_reservation`

**Display name** : Pub/Sub Lite Reservation

**Description** : A reservation in Google Pub/Sub Lite.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `reservation_id`: The identifier of the reservation, such as "my-reservation".
  * `location`: The GCP region where the reservation resides, such as "us-east1" or "us-west1".



## `pubsublite_subscription_partition`

**Display name** : Pub/Sub Lite Subscription Partition

**Description** : A subscription partition in Google Pub/Sub Lite.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `subscription_id`: The identifier of the subscription, such as "my-subscription".
  * `partition`: The partition within the subscription's topic.
  * `location`: The GCP zone where the subscription's topic resides, such as "us-east1-a" or "us-west1-a".



## `pubsublite_topic_partition`

**Display name** : Pub/Sub Lite Topic Partition

**Description** : A topic partition in Google Pub/Sub Lite.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `topic_id`: The identifier of the topic, such as "my-topic".
  * `partition`: The partition within the topic.
  * `location`: The GCP zone where the topic resides, such as "us-east1-a" or "us-west1-a".



## `recaptchaenterprise.googleapis.com/Key`

**Display name** : reCAPTCHA Key

**Description** : Monitoring resource for reCAPTCHA Key.

**Labels** :

  * `resource_container`: The ID of the GCP project associated with this reCAPTCHA Key.
  * `location`: Location where the reCAPTCHA Key is provisioned.
  * `key_id`: The ID for this Key.



## `recommendationengine.googleapis.com/EventStore`

**Display name** : Recommendation Event Store

**Description** : Recommendation event store resource.

**Labels** :

  * `resource_container`: The identifier of the GCP container associated with the resource.
  * `location`: Location of the event store.
  * `catalog_id`: The id of catalog associated with the event store.
  * `event_store_id`: The id of event store.



## `recommender`

**Display name** : Recommender

**Description** : A Recommender represents a grouping of similar recommendations.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `recommender_id`: The name of the recommender.
  * `location`: The location of the recommendation.



## `recommender_insight_type`

**Display name** : InsightType

**Description** : An InsightType represents a grouping of similar insights.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `insight_type_id`: The resource ID of the insight type.
  * `location`: The location of the insight.



## `redis.googleapis.com/Cluster`

**Display name** : Cloud Memorystore Redis Cluster

**Description** : A Redis cluster hosted on Google Cloud Memorystore.

**Labels** :

  * `resource_container`: The identifier of the GCP consumer project associated with this resource, such as 'my-project'.
  * `location`: The Google Cloud region in which the managed cluster is running.
  * `cluster_id`: The ID of the managed cluster.
  * `cluster_uid`: Identifier assigned by Google to uniquely distinguish a cluster.



## `redis.googleapis.com/ClusterNode`

**Display name** : Cloud Memorystore Redis Cluster Node

**Description** : A Redis cluster node hosted on Google Cloud Memorystore.

**Labels** :

  * `resource_container`: The identifier of the GCP consumer project associated with this resource, such as 'my-project'.
  * `location`: The Google Cloud zone in which the managed cluster node is running.
  * `cluster_id`: The ID of the managed cluster.
  * `cluster_uid`: Identifier assigned by Google to uniquely distinguish a cluster.
  * `node_id`: Identifier assigned by Redis to uniquely distinguish a node.
  * `shard_id`: Identifier assigned by Redis to uniquely distinguish a shard.



## `redis_instance`

**Display name** : Cloud Memorystore Redis Instance

**Description** : A Redis instance hosted on Google Cloud Memorystore.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `region`: The Google Cloud region in which the managed instance is running.
  * `instance_id`: The ID of the managed instance.
  * `node_id`: The ID of a Redis node within the managed instance.



## `retail.googleapis.com/Catalog`

**Display name** : Retail Catalog Store

**Description** : Retail catalog store resource.

**Labels** :

  * `resource_container`: The identifier of the GCP container associated with the resource.
  * `location`: Location of the catalog store.
  * `catalog_id`: The id of the catalog store.



## `saasservicemgmt.googleapis.com/Rollout`

**Display name** : App Lifecycle Manager Rollout

**Description** : A Rollout of an App Lifecycle Manager Tenant.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The region in which this rollout occurred.
  * `rollout_id`: ID associated with this rollout.



## `saasservicemgmt.googleapis.com/Unit`

**Display name** : App Lifecycle Manager Unit

**Description** : A Unit within an App Lifecycle Manager Tenant.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the GCP project associated with this resource.
  * `unit_id`: The ID of the Unit.



## `saasservicemgmt.googleapis.com/UnitKind`

**Display name** : App Lifecycle Manager Unit Kind

**Description** : A Unit Kind within an App Lifecycle Manager Tenant.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the GCP project associated with this resource.
  * `unit_kind_id`: The ID of the Unit Kind.



## `secretmanager.googleapis.com/Secret`

**Display name** : Secret Manager Secret

**Description** : A logical secret whose value and versions can be accessed.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: Location of secret metadata. Always global for v1.
  * `secret_id`: The name given to this secret.



## `securesourcemanager.googleapis.com/Location`

**Display name** : Secure Source Manager Location

**Description** : A location in the Secure Source Manager API.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource.
  * `location`: Location of the resource.



## `sensitiveaction.googleapis.com/Location`

**Display name** : Location

**Description** : A GCP resource container where a sensitive action was observed.

**Labels** :

  * `resource_container`: The GCP resource container where the sensitive action was observed.
  * `location`: The location where the sensitive action was observed.



## `servicedirectory_namespace`

**Display name** : Service Directory Namespace

**Description** : A namespace in the Service Directory service.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The cloud region of the Service Directory namespace.
  * `namespace_name`: The name of the Service Directory namespace.



## `servicedirectory_service`

**Display name** : Service Directory Service

**Description** : A Service Directory service.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The cloud region of the Service Directory service.
  * `namespace_name`: The name of the Service Directory namespace.
  * `service_name`: The name of the Service Directory service.



## `servicehealth.googleapis.com/Artifact`

**Display name** : Artifact

**Description** : An Artifact in service health.

**Labels** :

  * `resource_container`: The GCP project number.
  * `location`: The GCP location that serves the API for the given artifact.
  * `artifact_id`: The artifact ID.



## `servicehealth.googleapis.com/Event`

**Display name** : Event

**Description** : An Event in service health.

**Labels** :

  * `resource_container`: The GCP project number.
  * `location`: The GCP location that serves the API for the given event.
  * `event_id`: The event ID.



## `spanner.googleapis.com/Instance`

**Display name** : Cloud spanner instance resource

**Description** : Cloud spanner instance resource.

**Labels** :

  * `resource_container`: The GCP container associated with the metric.
  * `location`: Location of the instance.
  * `instance`: Cloud spanner instance.



## `spanner_instance`

**Display name** : Cloud Spanner Instance

**Description** : A Cloud Spanner instance.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `instance_id`: An immutable identifier for an instance.
  * `location`: Cloud Spanner region.
  * `instance_config`: Instance config for the instance.



## `storage.googleapis.com/Client`

**Display name** : GCS Client

**Description** : A Google Cloud Storage (GCS) client.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The location parsed from `cloud.region`.
  * `cloud_platform`: The cloud platform on which the GCS client runs.
  * `host_id`: The ID of the host (usually a VM) on which the GCS client runs.
  * `instance_id`: An UUID auto-generated by the client for the identification purpose.
  * `api`: The API used for communication. The available values are GRPC, JSON, and XML.



## `storage.googleapis.com/Project`

**Display name** : GCS Project

**Description** : GCS Project.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource, such as \"my-project\".
  * `location`: The location where the quota is consumed. It is a region for regional quota, or a zone for zonal quota, or \"global\" otherwise.



## `storage.googleapis.com/Storage`

**Display name** : Cloud Storage

**Description** : storage.googleapis.com/Storage target schema.

**Labels** :

  * `resource_container`: The monitored resource container. Usually a project.
  * `location`: The location of the resource.
  * `bucket_name`: The bucket name associated with the resource.



## `storage_transfer_job`

**Display name** : Cloud Storage Transfer Job

**Description** : A Google Cloud storage transfer job.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `job_id`: A unique name of the storage transfer job.



## `storagebatchoperations.googleapis.com/Location`

**Display name** : Storage Batch Operations Location

**Description** : The location where the batch operation is running in.

**Labels** :

  * `resource_container`: The project number that owns the batch operation.
  * `location`: The location where the batch operation is running in.



## `stream.googleapis.com/StreamInstance`

**Display name** : Stream Instance

**Description** : A service instance that streams a single source of Content. .

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The region of the runtime.
  * `stream_instance_id`: The identifier of the stream instance.



## `tcp_lb_rule`

**Display name** : External Passthrough TCP Network Load Balancer Rule

**Description** : A set of definitions for network TCP load balancing behavior.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `load_balancer_name`: The name of the load balancer.
  * `region`: The Google Cloud Platform region of the backends instance that connected to network load balancing forwarding rule.
  * `network_name`: The network from which the instance that connected to network load balancing sends traffic.
  * `backend_target_type`: The type of the backend target that handled the connection.
  * `backend_target_name`: The name of the backend target that handled the connection.
  * `forwarding_rule_name`: The name of the forwarding rule.
  * `forwarding_rule_network_tier`: The network tier of the forwarding rule.
  * `backend_name`: The name of the backend that handled the connection.
  * `backend_type`: The type of the backend that handled the connection.
  * `backend_scope`: The scope (zone or region) of the backend group that handled the connection.
  * `backend_scope_type`: The type of the scope of the backend group that handled the connection. Can be either 'ZONE' or 'REGION'.
  * `backend_failover_configuration`: The configured state of the backend group or the target pool that handled the connection.
  * `backend_subnetwork_name`: The name of the subnetwork of the instance that handled the connection.
  * `endpoint_zone`: The zone of the endpoint (VM instance) that handled the connection.



## `tcp_ssl_proxy_rule`

**Display name** : Global External Proxy Network Load Balancer Rule

**Description** : A set of definitions for TCP/SSL proxy behavior.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `region`: The region on which TCP/SSL proxy is applied, such as 'global' or 'us-central1'. Various other objects are defined per that locality.
  * `backend_target_name`: The name of the backend target ('backend service', equivalent to 'proxy name').
  * `backend_target_type`: The type of the backend target. Can only be 'BACKEND_SERVICE' currently.
  * `forwarding_rule_name`: The name of the forwarding rule.
  * `target_proxy_name`: The name of the target TCP/SSL proxy.
  * `backend_name`: The name of the backend group.
  * `backend_type`: The type of the backend group. Can be 'INSTANCE_GROUP' or 'NETWORK_ENDPOINT_GROUP'.
  * `backend_scope`: The scope (zone or region) of the backend group.
  * `backend_scope_type`: The type of the scope of the backend group. Can be either 'ZONE' or 'REGION'.



## `telcoautomation.googleapis.com/OrchestrationCluster`

**Display name** : OrchestrationCluster

**Description** : A TNA OrchestrationCluster.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the resource inside the project.
  * `orchestration_cluster_id`: User-provided unique identifier within a project & region.



## `threat_detector`

**Display name** : Threat Detector

**Description** : A detector in the Threat Detection service.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `detector_name`: The specific detector that triggered the alert.



## `tpu.googleapis.com/GceTpuWorker`

**Display name** : GCE TPU Worker

**Description** : A single TPU GCE worker VM.

**Labels** :

  * `resource_container`: The GCP project number.
  * `location`: The GCP location.
  * `worker_id`: The GCE VM instance ID.



## `tpu_worker`

**Display name** : TPU Worker

**Description** : A TPU Worker executing Tensorflow work for a TPU Node.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `zone`: The Google Cloud zone in which the TPU Worker is running.
  * `node_id`: The ID of the TPU Node.
  * `worker_id`: The ID of a TPU Worker within the TPU Node.



## `transfer_service_agent`

**Display name** : Transfer Service Agent

**Description** : An instance of the agent application that Transfer Service uses to transfer data into Google Cloud.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `agent_pool`: The identifier of the agent pool associated with this resource.
  * `agent_id`: The unique identifier of the agent within the agent pool.



## `transferappliance.googleapis.com/Appliance`

**Display name** : Transfer Appliance

**Description** : Transfer Appliance is a way for Google Cloud Customers to transfer data to GCS.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The region in which the appliance was provisioned in (e.g. us-central1).
  * `appliance_id`: The unique id of the appliance.



## `translationhub.googleapis.com/Portal`

**Display name** : Translation Hub Portal

**Description** : A Portal (resource) in the Translation Hub API.

**Labels** :

  * `resource_container`: The identifier of the GCP resource container associated with this resource, such as "my-project".
  * `location`: The location of the usage.



## `udp_lb_rule`

**Display name** : External Passthrough UDP Network Load Balancer Rule

**Description** : A set of definitions for network UDP load balancing behavior.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `load_balancer_name`: The name of the load balancer.
  * `region`: The Google Cloud Platform region of the backends instance that connected to network load balancing forwarding rule.
  * `network_name`: The network from which the instance that connected to network load balancing sends traffic.
  * `backend_target_type`: The type of the backend target that handled the connection.
  * `backend_target_name`: The name of the backend target that handled the connection.
  * `forwarding_rule_name`: The name of the forwarding rule.
  * `forwarding_rule_network_tier`: The network tier of the forwarding rule.
  * `backend_name`: The name of the backend that handled the connection.
  * `backend_type`: The type of the backend that handled the connection.
  * `backend_scope`: The scope (zone or region) of the backend group that handled the connection.
  * `backend_scope_type`: The type of the scope of the backend group that handled the connection. Can be either 'ZONE' or 'REGION'.
  * `backend_failover_configuration`: The configured state of the backend group or the target pool that handled the connection.
  * `backend_subnetwork_name`: The name of the subnetwork of the instance that handled the connection.
  * `endpoint_zone`: The zone of the endpoint (VM instance) that handled the connection.



## `uptime_url`

**Display name** : Uptime Check URL

**Description** : An Uptime Monitoring check against a custom URL.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `host`: The hostname or IP address of the check.



## `vectorsearch.googleapis.com/Collection`

**Display name** : Vector Search Collection

**Description** : Monitored resource representing a Vector Search Collection.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the GCP project associated with this resource.
  * `collection`: The ID of the Collection.



## `vectorsearch.googleapis.com/Index`

**Display name** : Vector Search Index

**Description** : Monitored resource representing a Vector Search Index.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The location of the GCP project associated with this resource.
  * `collection_id`: The ID of the Collection.
  * `index_id`: The ID of the Index.



## `videostitcher.googleapis.com/Project`

**Display name** : Video Stitcher API Project

**Description** : A Video Stitcher API Project.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The GCP location where the project resource resides.



## `visionai.googleapis.com/Application`

**Display name** : Application

**Description** : A Vertex AI Vision application.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The GCP location in which this application resides.
  * `application_id`: The identifier of the application.



## `visionai.googleapis.com/Instance`

**Display name** : Application instance

**Description** : A Vertex AI Vision application instance.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The GCP location in which this application instance resides.
  * `application_id`: The identifier of the application which this instance is associated with.
  * `instance_id`: The identifier of the instance.



## `visionai.googleapis.com/Stream`

**Display name** : Stream

**Description** : A Vertex AI Vision stream.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this resource.
  * `location`: The GCP location in which this stream resides.
  * `cluster_id`: The identifier of the cluster in which this stream resides.
  * `stream_id`: The identifier of the stream.



## `vmmigration.googleapis.com/MigratingVM`

**Display name** : Migrate to Virtual Machines Migrating VM

**Description** : A Migrate to Virtual Machines Migrating VM.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this VM resource.
  * `location`: The GCP location where the VM resource resides.
  * `source`: The source where the VM resource resides.
  * `vm`: The VM ID.



## `vmmigration.googleapis.com/Source`

**Display name** : Migrate to Virtual Machines Source

**Description** : A Migrate to Virtual Machines Source.

**Labels** :

  * `resource_container`: The identifier of the GCP project associated with this source resource.
  * `location`: The GCP location where the source resource resides.
  * `source`: The source ID.



## `vmwareengine.googleapis.com/VmwareEngineNetwork`

**Display name** : Vmware Engine Network

**Description** : A VMWare Engine Network.

**Labels** :

  * `resource_container`: The GCP container associated with the Vmware Engine Network.
  * `location`: The location (global) that contains the Vmware Engine Network.
  * `vmware_engine_network_name`: The name of the Vmware Engine Network in a given project.



## `vpc_access_connector`

**Display name** : VPC Access Connector

**Description** : A connector that can communicate with devices within a VPC.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `location`: The region the connector is located in.
  * `connector_name`: The name of the connector.



## `vpn_gateway`

**Display name** : Cloud VPN Gateway

**Description** : A Cloud VPN gateway.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `gateway_id`: The VPN Gateway ID.
  * `region`: The region in which the VPN Gateway is running.



## `vpn_tunnel`

**Display name** : Cloud VPN Tunnel

**Description** : A Cloud VPN Tunnel.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `region`: The region in which the VPN Tunnel is activly running.
  * `tunnel_id`: The VPN Tunnel ID.



## `wire_endpoint`

**Display name** : Interconnect Wire Endpoint

**Description** : Logical endpoint of an Interconnect pseudowire.

**Labels** :

  * `project_id`: The identifier of the GCP project associated with this resource, such as "my-project".
  * `cross_site_network`: The user-provided name of the parent cross site network resource.
  * `wire_group`: The user-provided name of the wire group resource container.
  * `src_city`: The Interconnect city, a.k.a. the metropolitan area designator, for the wire endpoint source.
  * `src_interconnect_project`: The Interconnect city, a.k.a. the metropolitan area designator, for the wire endpoint source.
  * `src_interconnect`: The interconnect name for the wire endpoint source.
  * `src_vlan`: The interconnect VLAN interface for the wire endpoint source.
  * `dst_city`: The Interconnect city, a.k.a. the metropolitan area designator, for the wire endpoint destination.
  * `dst_interconnect_project`: The Interconnect city, a.k.a. the metropolitan area designator, for the wire endpoint destination.
  * `dst_interconnect`: The interconnect name for the wire endpoint destination.
  * `dst_vlan`: The interconnect VLAN interface for the wire endpoint destination.



## `workflows.googleapis.com/Workflow`

**Display name** : Workflow

**Description** : A Workflows specification of steps to execute.

**Labels** :

  * `resource_container`: The identifier of the GCP container associated with the resource.
  * `location`: The region in which the workflow is deployed.
  * `workflow_id`: The ID of the workflow.



Generated at 2026-10-14 20:17:53 UTC.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
