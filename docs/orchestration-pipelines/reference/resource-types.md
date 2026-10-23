---
url: https://docs.cloud.google.com/orchestration-pipelines/reference/resource-types/
title: Orchestration Pipelines provisioned resource types reference \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:59.992090+00:00
---

# Orchestration Pipelines provisioned resource types reference  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/orchestration-pipelines/reference/resource-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Orchestration Pipelines ](https://docs.cloud.google.com/orchestration-pipelines)
  * [ Reference ](https://docs.cloud.google.com/orchestration-pipelines/apis)



Send feedback 

#  Orchestration Pipelines provisioned resource types reference Stay organized with collections  Save and categorize content based on your preferences. 

This page describes resource types that can be provisioned in Orchestration Pipelines.

For more information about provisioning resources, see [Provision resources](https://docs.cloud.google.com/orchestration-pipelines/provision-resources).

**Note:** You can get the latest list of available resource types by running the [`orchestration-pipelines resource-types list` command](https://docs.cloud.google.com/orchestration-pipelines/provision-resources#resource-types) in Google Cloud CLI.

## Resource types overview

Resource type | API reference | Description  
---|---|---  
artifactregistry.repository | [v1](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories) |  Artifact Registry repository configurations.  
bigquery.dataset | [v2](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets) |  BigQuery Dataset configurations. Definition handling:

  * `datasetReference`: automatically populated with project and dataset IDs. 

  
bigquery.routine | [v2](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines) |  BigQuery Routine configurations.  
bigquery.table | [v2](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables) |  BigQuery Table configurations. Definition handling:

  * `tableReference`: automatically populated with project, dataset, and table IDs. 

  
bigquerydatatransfer.transferConfig | [v1](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs) |  BigQuery Data Transfer Service configurations. Metadata:

  * `service_account_name`: authorization service account 

Definition handling:

  * `displayName`: used to find existing resource instead of exact ID match 

  
cloudkms.keyRing | [v1](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings) |  Cloud Key Management Service KeyRing resources.  
cloudkms.keyRing.cryptoKey | [v1](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys) |  Cloud Key Management Service CryptoKey resources. Parent resource type: `cloudkms.keyRing`.  
composer.environment | [v1](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments) |  Managed Service for Apache Airflow environment configurations.  
compute.address | [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses) |  Compute Engine Address resources. Special handling:

  * `updates`: in-place updates are supported only for labels 

  
compute.firewall | [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls) |  Compute Engine Firewall resources.  
compute.forwardingRule | [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules) |  Compute Engine Forwarding Rule resources. Special handling:

  * `portRange`: automatically normalized during comparison (for example, `80` becomes `80-80`) 

  
compute.instance | [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances) |  Compute Engine Instance resources. Special handling:

  * `zone`: derived from `metadata.location` if omitted 
  * `disks[].initializeParams`: ignored during comparison 

  
compute.instanceGroupManager | [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers) |  Compute Engine Instance Group Manager resources. Special handling:

  * `zone`: derived from `metadata.location` if omitted 

  
compute.instanceTemplate | [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates) |  Compute Engine Instance Template resources. Special handling:

  * `updates`: in-place updates are not supported 

  
compute.network | [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks) |  Compute Engine Network resources.  
compute.network.networkPeering | [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks) |  Compute Engine Network Peering resources. Special handling:

  * `lifecycle`: managed through parent Network peering methods (AddPeering, UpdatePeering) 

Parent resource type: `compute.network`.  
compute.route | [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes) |  Compute Engine Route resources. Special handling:

  * `updates`: in-place updates are not supported 

  
compute.router | [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers) |  Compute Engine Router resources.  
compute.subnetwork | [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetInstances) |  Compute Engine Target Instance resources. Special handling:

  * `updates`: in-place updates are not supported 

  
dataform.repository | [v1beta1](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories) |  Dataform Repository resources.  
dataform.repository.releaseConfig | [v1beta1](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.releaseConfigs) |  Dataform ReleaseConfig resources. Special handling:

  * `releaseCompilationResult`: setting to `auto` in definition triggers compilation after resource creation or update 

Parent resource type: `dataform.repository`.  
dataform.repository.workflowConfig | [v1beta1](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowConfigs) |  Compute Engine WorkflowConfig resources. Definition handling:

  * `releaseConfig`: accepts short ID of config within the same repository instead of full URI 

Parent resource type: `dataform.repository`.  
dataform.repository.workspace | [v1beta1](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces) |  Compute Engine Workspace resources. Parent resource type: `dataform.repository`.  
dataproc.autoscalingPolicy | [v1](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.autoscalingPolicies) |  Managed Service for Apache Spark Autoscaling Policies.  
dataproc.cluster | [v1](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.clusters) |  Managed Service for Apache Spark Cluster resources. Definition handling:

  * `config.autoDeleteTtl`: ignored during comparison 
  * `config.softwareConfig`: ignored during comparison 

  
dataproc.workflowTemplate | [v1](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.workflowTemplates) |  Managed Service for Apache Spark Workflow Templates. Definition handling:

  * `id`: automatically populated with the logical name of the resource. 

  
iam.serviceAccount | [v1](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts) |  IAM Service Accounts. Special handling:

  * `resource ID`: implicitly formatted as email address for API requests. For example, if resource ID is `example-account`, the project is `example-project`, then the resource's name is formatted as `example-account@example-project.iam.gserviceaccount.com`. 

  
iam.workloadIdentityPool | [v1](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools) |  IAM Workload Identity Pools.  
iam.workloadIdentityPoolProvider | [v1](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers) |  IAM Workload Identity Pool Providers.  
pubsub.schema | [v1](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.schemas) |  Pub/Sub Schema resources. Special handling:

  * `updates`: in-place updates aren't fully supported yet. 

  
pubsub.subscription | [v1](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions) |  Pub/Sub Subscription resources.  
pubsub.topic | [v1](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics) |  Pub/Sub Topic resources.  
secretmanager.secret | [v1](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets) |  Secret Manager Secret resources.  
sqladmin.instance | [v1beta4](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances) |  Cloud SQL Admin Instance resources.  
sqladmin.instance.database | [v1beta4](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/databases) |  Cloud SQL Admin Database resources. Parent resource type: `sqladmin.instance`.  
sqladmin.instance.user | [v1beta4](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/users) |  Cloud SQL Admin User resources. Parent resource type: `sqladmin.instance`.  
storage.bucket | [v1beta4](https://docs.cloud.google.com/storage/docs/reference/rest/v1/buckets) |  Cloud Storage Bucket resources.  
storage.bucket.notification | [v1](https://docs.cloud.google.com/storage/docs/reference/rest/v1/notifications) |  Cloud Storage Notification resources. Special handling:

  * `updates`: in-place updates are not supported by the API; resources must be recreated 
  * `dynamic ID resolution`: resource ID is resolved dynamically from matching topic in API list output 

Definition handling:

  * `topic`: prefix `//pubsub.[DOMAIN]/` is ignored during comparison against API state 

Parent resource type: `storage.bucket`.  
  
## Resource types

This section lists available resource types.

### artifactregistry.repository

Artifact Registry repository configurations.

API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories)



### bigquery.dataset

BigQuery Dataset configurations.

Definition handling:

  * `datasetReference`: automatically populated with project and dataset IDs. 



API documentation for the resource's definition:

  * [v2](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets)



### bigquery.routine

BigQuery Routine configurations.

API documentation for the resource's definition:

  * [v2](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines)



### bigquery.table

BigQuery Table configurations.

Definition handling:

  * `tableReference`: automatically populated with project, dataset, and table IDs. 



API documentation for the resource's definition:

  * [v2](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables)



### bigquerydatatransfer.transferConfig

BigQuery Data Transfer Service configurations.

Metadata:

  * `service_account_name`: authorization service account 



Definition handling:

  * `displayName`: used to find existing resource instead of exact ID match 



API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs)



### cloudkms.keyRing

Cloud Key Management Service KeyRing resources.

API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings)



### cloudkms.keyRing.cryptoKey

Cloud Key Management Service CryptoKey resources.

Parent resource:

  * cloudkms.keyRing.



API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys)



### composer.environment

Managed Service for Apache Airflow environment configurations.

API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments)



### compute.address

Compute Engine Address resources.

Special handling:

  * `updates`: in-place updates are supported only for labels 



API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses)



### compute.firewall

Compute Engine Firewall resources.

API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls)



### compute.forwardingRule

Compute Engine Forwarding Rule resources.

Special handling:

  * `portRange`: automatically normalized during comparison (for example, `80` becomes `80-80`) 



API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules)



### compute.instance

Compute Engine Instance resources.

Special handling:

  * `zone`: derived from `metadata.location` if omitted 
  * `disks[].initializeParams`: ignored during comparison 



API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances)



### compute.instanceGroupManager

Compute Engine Instance Group Manager resources.

Special handling:

  * `zone`: derived from `metadata.location` if omitted 



API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers)



### compute.instanceTemplate

Compute Engine Instance Template resources.

Special handling:

  * `updates`: in-place updates are not supported 



API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates)



### compute.network

Compute Engine Network resources.

API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks)



### compute.network.networkPeering

Compute Engine Network Peering resources.

Special handling:

  * `lifecycle`: managed through parent Network peering methods (AddPeering, UpdatePeering) 



Parent resource:

  * compute.network.



API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks)



### compute.route

Compute Engine Route resources.

Special handling:

  * `updates`: in-place updates are not supported 



API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes)



### compute.router

Compute Engine Router resources.

API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers)



### compute.subnetwork

Compute Engine Target Instance resources.

Special handling:

  * `updates`: in-place updates are not supported 



API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetInstances)



### dataform.repository

Dataform Repository resources.

API documentation for the resource's definition:

  * [v1beta1](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories)



### dataform.repository.releaseConfig

Dataform ReleaseConfig resources.

Special handling:

  * `releaseCompilationResult`: setting to `auto` in definition triggers compilation after resource creation or update 



Parent resource:

  * dataform.repository.



API documentation for the resource's definition:

  * [v1beta1](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.releaseConfigs)



### dataform.repository.workflowConfig

Compute Engine WorkflowConfig resources.

Definition handling:

  * `releaseConfig`: accepts short ID of config within the same repository instead of full URI 



Parent resource:

  * dataform.repository.



API documentation for the resource's definition:

  * [v1beta1](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowConfigs)



### dataform.repository.workspace

Compute Engine Workspace resources.

Parent resource:

  * dataform.repository.



API documentation for the resource's definition:

  * [v1beta1](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces)



### dataproc.autoscalingPolicy

Managed Service for Apache Spark Autoscaling Policies.

API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.autoscalingPolicies)



### dataproc.cluster

Managed Service for Apache Spark Cluster resources.

Definition handling:

  * `config.autoDeleteTtl`: ignored during comparison 
  * `config.softwareConfig`: ignored during comparison 



API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.clusters)



### dataproc.workflowTemplate

Managed Service for Apache Spark Workflow Templates.

Definition handling:

  * `id`: automatically populated with the logical name of the resource. 



API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.workflowTemplates)



### iam.serviceAccount

IAM Service Accounts.

Special handling:

  * `resource ID`: implicitly formatted as email address for API requests. For example, if resource ID is `example-account`, the project is `example-project`, then the resource's name is formatted as `example-account@example-project.iam.gserviceaccount.com`. 



API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts)



### iam.workloadIdentityPool

IAM Workload Identity Pools.

API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools)



### iam.workloadIdentityPoolProvider

IAM Workload Identity Pool Providers.

API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers)



### pubsub.schema

Pub/Sub Schema resources.

Special handling:

  * `updates`: in-place updates aren't fully supported yet. 



API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.schemas)



### pubsub.subscription

Pub/Sub Subscription resources.

API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions)



### pubsub.topic

Pub/Sub Topic resources.

API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics)



### secretmanager.secret

Secret Manager Secret resources.

API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets)



### sqladmin.instance

Cloud SQL Admin Instance resources.

API documentation for the resource's definition:

  * [v1beta4](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances)



### sqladmin.instance.database

Cloud SQL Admin Database resources.

Parent resource:

  * sqladmin.instance.



API documentation for the resource's definition:

  * [v1beta4](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/databases)



### sqladmin.instance.user

Cloud SQL Admin User resources.

Parent resource:

  * sqladmin.instance.



API documentation for the resource's definition:

  * [v1beta4](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/users)



### storage.bucket

Cloud Storage Bucket resources.

API documentation for the resource's definition:

  * [v1beta4](https://docs.cloud.google.com/storage/docs/reference/rest/v1/buckets)



### storage.bucket.notification

Cloud Storage Notification resources.

Special handling:

  * `updates`: in-place updates are not supported by the API; resources must be recreated 
  * `dynamic ID resolution`: resource ID is resolved dynamically from matching topic in API list output 



Definition handling:

  * `topic`: prefix `//pubsub.[DOMAIN]/` is ignored during comparison against API state 



Parent resource:

  * storage.bucket.



API documentation for the resource's definition:

  * [v1](https://docs.cloud.google.com/storage/docs/reference/rest/v1/notifications)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
