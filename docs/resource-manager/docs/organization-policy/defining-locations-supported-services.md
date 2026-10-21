---
url: https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services/
title: Services that support restricting resource locations \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:42:49.832904+00:00
---

# Services that support restricting resource locations  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Reference ](https://docs.cloud.google.com/organization-policy/apis)



Send feedback 

#  Services that support restricting resource locations Stay organized with collections  Save and categorize content based on your preferences. 

The resources used by each service are impacted by location in different ways. Before adding a [resource locations](https://docs.cloud.google.com/organization-policy/restrict-locations) constraint to your [organization policy](https://docs.cloud.google.com/organization-policy/overview), review the following sections to see how the resources you are applying the policy to will behave.

**Note:** Organization policies, including those with the resource locations constraint, are not retroactive. Adding the resource locations constraint to existing resources will not restrict their location, but might restrict automatic child resource creation or other functionality.

## Agent Anomaly Detection

The resource locations constraint is enforced only when you create an `AgentAnomalyDetectionScope` resource. You cannot change the location of an existing `AgentAnomalyDetectionScope` resource, and deleting this resource is exempt from the constraint. Because organization policy compliance isn't enforced retroactively, applying this constraint doesn't affect pre-existing resources.

Agent Anomaly Detection is available in the `us` multi-region only. For more information, see the [Agent Anomaly Detection overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-anomalies-overview).

## Agent Assist

Organization policy is enforced when you create a `conversation profile` or a `knowledge base` resource in Agent Assist. Both resources are regional.

Resource location constraints do not apply to the `global` location; resource creation is always allowed.

For a list of available locations and limitations, see the [Agent Assist regionalization and data residency](https://docs.cloud.google.com/agent-assist/docs/regionalization) page.

## Agent Identity API

Organization policy is enforced when you create an `authProvider` resource in Agent Identity API.

Resource location constraints apply to all supported regions. For a list of available regions, see [Agent Identity API locations](https://docs.cloud.google.com/iam/docs/agent-identity-locations).

## Agent Registry

Resource locations constraints apply to Agent Registry regional resources, such as `service`, `binding`, `skill`, and `skillRevision` resources. Organization policy compliance isn't retroactively enforced. This means that applying a resource locations constraint doesn't affect any pre-existing resources or updates to those resources.

For a list of available locations, see [Agent Registry locations](https://docs.cloud.google.com/agent-registry/locations).

## Agent Search

Resource locations constraints apply to all Agent Search resources. Organization policy compliance isn't retroactively enforced. This means that applying a resource locations constraint doesn't affect any pre-existing resources or updates to those resources.

For a list of available regions, see [Agent Search locations](https://docs.cloud.google.com/generative-ai-app-builder/docs/locations).

## AlloyDB for PostgreSQL

Organization policy is enforced when you create clusters, instances, and certain types of backups. The creation of on-demand backups is subject to the organization policy, while the creation of automated and continuous backups is exempted if enabled to prevent data loss.

AlloyDB for PostgreSQL only supports region locations. Constraints on multi-region locations and zone locations have no effect. However, constraints on value groups that contain regions do have an effect. For example, the value `asia` in an organization policy has no effect, but the value `in:asia-locations` does have an effect.

For a list of available locations, see [AlloyDB for PostgreSQL locations](https://docs.cloud.google.com/alloydb/docs/locations).

## Anti Money Laundering AI

Resource locations constraints apply to all Anti Money Laundering AI resources and are enforced at the time of resource creation.

For a list of available locations, see [AML AI locations](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations).

## API Gateway

Resource locations constraints are enforced when creating [gateways](https://docs.cloud.google.com/api-gateway/docs/reference/rest/v1/projects.locations.gateways/create), a regional resource. Other API Gateway resources, such as [APIs](https://docs.cloud.google.com/api-gateway/docs/reference/rest/v1/projects.locations.apis/create) and [API configs](https://docs.cloud.google.com/api-gateway/docs/reference/rest/v1/projects.locations.apis.configs/create), are global resources and are not subject to resource locations constraints.

For a list of supported locations for API Gateway, see [Choosing a Google Cloud region](https://docs.cloud.google.com/api-gateway/docs/deployment-model#choosing-region).

Learn more about how to set an organization policy with resource locations constraints in [Restricting resource locations](https://docs.cloud.google.com/organization-policy/restrict-locations).

## Apigee

Resource locations constraints are enforced when creating the following Apigee resources:

  * [Apigee Organization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/create)
  * [Apigee Instance](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances/create)
  * [Apigee Endpoint Attachments](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments/create)



For a list of available locations, see [Apigee locations](https://docs.cloud.google.com/apigee/docs/locations).

Learn more about how to set an organization policy with resource locations constraints in [Restricting resource locations](https://docs.cloud.google.com/organization-policy/restrict-locations).

## Apigee API hub

Resource locations constraints apply to all Apigee API hub resources. Organization policy compliance isn't retroactively enforced. This means that applying a resource locations constraint doesn't affect any pre-existing resources or updates to those resources.

For a list of available locations, see [Apigee API hub locations](https://docs.cloud.google.com/apigee/docs/apihub/locations).

## Apigee Integration API

The organization policy is enforced when you use the [Apigee Integration API](https://docs.cloud.google.com/apigee/docs/api-platform/integration/reference/rest) to create the following resources:

  * Integration
  * Authorization configuration (AuthConfig)
  * Certificate for AuthConfig
  * Integration version
  * SFDC (Salesforce) channel
  * SFDC (Salesforce) instance



The organization policy is also enforced when you run, schedule, or test an integration.

Apigee integrations are region specific. It means that an integration created in a specific region can access the resources only within that region.

For a list of available locations where you can create your integrations, see [Apigee locations](https://docs.cloud.google.com/apigee/docs/locations).

## App Engine

App Engine is a property of the `application` resource. The location property is enforced for all environments when you create an `application`. You can create only one App Engine `application` in each project. A Cloud Storage bucket is automatically created in the same location as the `application`. If you create an `application` with a broad location that doesn't comply with the organization policy, you will have to create a new project and App Engine `application`.

When you disable an `application`, it won't be served in the future, but replicated code and data will remain in locations the `application` was stored in. To completely erase this data, delete the parent project.

The App Engine flexible environment is built on top of Compute Engine. Auto-scaling instances can fail if any locations where scaling happens aren't in the list of allowed locations that are defined in the organization policy.

For a list of available locations, see [App Engine Locations](https://docs.cloud.google.com/appengine/docs/locations).

## App Hub

The organization policy is enforced when you create an application in App Hub. A regional application can only contain the resources of that region. Global applications aren't subject to the resource locations constraint and can contain both global and regional resources. For more information, see [Global and regional App Hub applications](https://docs.cloud.google.com/app-hub/docs/global-regional-applications).

For a list of available locations, see [App Hub locations](https://docs.cloud.google.com/app-hub/docs/locations).

## App Lifecycle Manager

When you use App Lifecycle Manager through Google Cloud console, the UI uses the `global` region to automate the replication of `Saas`, `UnitKind`, and `Release` resources to the available regions defined in your SaaS offering. The `global` region isn't subject to resource locations constraints. However, the replicated regional resources are subject to resource locations constraints.

`Unit` resources can only be created in the available regions defined in your SaaS offering and aren't propagated to the `global` region. The organization policy is enforced when creating or updating these resources.

**Note:** Resource replication isn't automated if you create or update App Lifecycle Manager resources using Google Cloud CLI.

For more information about regionalization, see the [App Lifecycle Manager overview](https://docs.cloud.google.com/saas-runtime/docs/overview#saas-locations).

For a list of available locations, see [App Lifecycle Manager locations](https://docs.cloud.google.com/saas-runtime/docs/locations).

## Application Design Center

Resource locations constraints apply when you create regional spaces, applications, and application templates in App Design Center.

Organization policy compliance isn't retroactively enforced, meaning that applying a resource locations constraint does not affect pre-existing spaces or resources. The `global` location is not subject to resource locations constraints.

For a list of available locations, see [App Design Center locations](https://docs.cloud.google.com/application-design-center/docs/locations).

## Application Integration API

The organization policy is enforced when you use the [Application Integration API](https://docs.cloud.google.com/application-integration/docs/reference/rest) to create the following resources:

  * [Integration](https://docs.cloud.google.com/application-integration/docs/reference/rest#rest-resource:-v1.projects.locations.integrations)
  * [Integration version](https://docs.cloud.google.com/application-integration/docs/reference/rest#rest-resource:-v1.projects.locations.integrations.versions)
  * [Execution](https://docs.cloud.google.com/application-integration/docs/reference/rest#rest-resource:-v1.projects.locations.integrations.executions)
  * [Suspension](https://docs.cloud.google.com/application-integration/docs/reference/rest#rest-resource:-v1.projects.locations.integrations.executions.suspensions)
  * [Authorization configuration (AuthConfig)](https://docs.cloud.google.com/application-integration/docs/reference/rest#rest-resource:-v1.projects.locations.authconfigs)
  * [SFDC (Salesforce) instance](https://docs.cloud.google.com/application-integration/docs/reference/rest#rest-resource:-v1.projects.locations.sfdcinstances)
  * [SFDC (Salesforce) channel](https://docs.cloud.google.com/application-integration/docs/reference/rest#rest-resource:-v1.projects.locations.sfdcinstances.sfdcchannels)



The organization policy is also enforced when you run, schedule, or test an integration.

Application Integration is _regional_ , which means that an integration created in a specific region can access the resources only within that region.

For a list of available locations, see [Application Integration locations](https://docs.cloud.google.com/application-integration/docs/locations).

### Limitations

The following Application Integration resources don't support the resource location constraints that you specify:

  * Email subject and email body of [Send Email task](https://docs.cloud.google.com/application-integration/docs/configure-send-email-task)
  * [Certificate for AuthConfig](https://docs.cloud.google.com/application-integration/docs/reference/rest#rest-resource:-v1.projects.locations.certificates)
  * [Build integrations with Gemini](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini)



## Artifact Registry

You can create repositories in a multi-region or region. Artifact Registry enforces organization policy when you create a repository.

Organization policy compliance isn't enforced retroactively. Artifacts can be added to any existing repository, even if the repository location is denied by the resource locations organization policy. To enforce a new resource locations organization policy on existing repositories, create new repositories after the organization policy is applied, and then migrate artifacts from old repositories to the new ones. You can use the [gcrane](https://github.com/google/go-containerregistry/tree/main/cmd/gcrane) tool to copy images between repositories.

For a list of available locations, see the [Artifact Registry documentation](https://docs.cloud.google.com/artifact-registry/docs/repo-locations).

## Audit Manager

When you run a new audit, the organization policy is enforced based on the region that you specified when creating the audit request. When the location of the audit is selected as global, it is not subjected to the resource locations constraint.

For a list of available regional locations, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations).

## Backup and DR Service

Organization policy is enforced when you create the following regional resource:

  * `BackupPlan`: the location of this resource determines the target region where all backup data is stored.



For more information, see [Backup and DR Service locations](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault).

## Backup for GKE

Organizational policy is enforced when you create either of the top-two regional resources:

  * `BackupPlan`: the location of this resource determines the target region where all backup data is stored for backups created below this plan. There may be multiple `BackupPlan` resources in a project.

  * `RestorePlan`: the location of this resource controls the allowable region of the target cluster into which data from a backup is restored. There may be multiple `RestorePlan` resources in a project.




For more information, see [Backup for GKE locations](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-locations).

## BigQuery

BigQuery `dataset` resources can be both regional and multi-regional. Organization policy compliance isn't enforced retroactively. To enforce a new resource locations constraint on an existing `dataset`, delete the `dataset` resource and create it again with the organization policy applied to the parent resource.

You can create `Database` resources within a `dataset` resource with a location that is denied by the resource locations organization policy. The location of the `dataset` resource doesn't dictate the location of the `database` resource. To enforce a new resource locations constraint on an existing `database`, delete the `database` resource and create it again with the organization policy applied to the parent resource.

For a list of available locations, see the BigQuery [Dataset Locations](https://docs.cloud.google.com/bigquery/docs/dataset-locations) page.

## BigQuery Data Transfer Service

The [`TransferConfig`](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs) resource can be both regional and multi-regional. Organization policy compliance isn't enforced retroactively. Organization policy is checked only when creating a `TransferConfig`. To enforce a new resource locations constraint on an existing `TransferConfig`, delete the `TransferConfig` resource and create it again with the organization policy applied to the parent resource.

For a list of available locations, see [BigQuery Data Transfer Service locations](https://docs.cloud.google.com/bigquery/docs/dts-introduction#supported_regions).

## BigQuery Migration Service

The [`MigrationWorkflow` resource](https://docs.cloud.google.com/bigquery/docs/reference/migration/rest/v2/projects.locations.workflows#resource:-migrationworkflow) describes the tasks and subtasks that constitute the migration workflow. They can be created by using the Google Cloud console or the API when running the [migration assessment](https://docs.cloud.google.com/bigquery/docs/migration-assessment) or SQL translation. The migration workflow must be created in the same location as the resources that it uses. For example, if your BigQuery dataset and the Cloud Storage bucket are in the `US` multi-region, then the migration workflow can be created in the `US` multi-region or the `us-west1` region.

Organization policy is checked only when creating a migration workflow, because it is an immutable resource.

For a list of available locations, see [BigQuery locations](https://docs.cloud.google.com/bigquery/docs/locations#supported_locations).

## BigQuery sharing

The organization policy is enforced when you create a [`DataExchange`](https://docs.cloud.google.com/bigquery/docs/reference/analytics-hub/rest/v1/projects.locations.dataExchanges) or a [`Listing`](https://docs.cloud.google.com/bigquery/docs/reference/analytics-hub/rest/v1/projects.locations.dataExchanges.listings). These resources can be regional or multi-regional. Organization policy compliance isn't enforced retroactively. To enforce a new resource locations constraint on an existing resource, you must delete and recreate the resource with the organization policy applied.

For a list of available locations, see [Introduction to BigQuery sharing](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#supported-regions).

## Bigtable

A Bigtable instance resource is a logical container of clusters. Each of these clusters is located in a zone. All data in an instance is replicated uniformly to all clusters that are contained in that instance. Organization policy is enforced when a cluster is created. You can't create new storage containers in a location that is denied by the organization policy. Existing instances and clusters will continue to operate even if they are in locations that are denied by a subsequent change to the organization policy.

You can manually remediate resources that violate a new organization policy, by deleting them and recreating them once the organization policy is put into place. For example, if you had a multi-cluster instance in which one cluster violated a new organization policy, you could delete it and then add a new cluster in a permitted zone.

For a list of available locations, see the [Bigtable Locations](https://docs.cloud.google.com/bigtable/docs/locations) page.

## Certificate Authority Service

CA Service resources such as certificate templates, certificate authority (CA) pools, and CAs can be created in any available location. These resources can't be moved after creation.

Certificate templates can be replicated using Google Cloud CLI commands. You can use gcloud CLI commands to create resources with the same name in another supported location. For more information, see [Creating certificate templates](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-template).

CAs can be cloned from existing CAs in the same CA pool. These new CAs are created in the same location as the CA from which they were cloned. For more information, see [Creating certificate authorities](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities).

For the list of available locations, see [CA Service locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).

## Certificate Manager

Except for [`CertificateMaps`](https://docs.cloud.google.com/certificate-manager/docs/maps) and [`CertificateMapEntries`](https://docs.cloud.google.com/certificate-manager/docs/map-entries), which can be global only, Certificate Manager resources can be created in any regional or global locations. However, you can't choose a zone for a resource. The organization policy is enforced at the time that you create the Certificate Manager resource.

For a list of available locations, see [Products available by location](https://cloud.google.com/about/locations).

## Cloud Asset Inventory

Cloud Asset Inventory feed resources are global resources and are not subject to resource locations constraints.

## Cloud Build

Organization policy is enforced when you create new regional Cloud Build resources. Although you can create resources in any region, Cloud Build ensures that you select a region approved by your organization. Organization policy is only enforced on newly created Cloud Build resources in a non-global region after you create the organization policy.

For a list of available regions, see the Cloud Build [locations](https://docs.cloud.google.com/build/docs/locations) page.

## Managed Service for Apache Airflow

**Note:** Managed Airflow supports location constraints on the region level. Location constraints on the zone level are not supported.

A Managed Airflow environment is a logical container for the resources listed below. During the environment creation process, you choose a location (region/zone) for the environment and the underlying resources are created based on the location selected.

  * Google Kubernetes Engine cluster

  * Cloud SQL instance

  * App Engine VM(s) running Airflow web server

  * Persistent Disks: Used by the Airflow Webserver and GKE cluster

  * Pub/Sub topics

  * Cloud Storage

  * Building and storing Airflow images with custom Python dependencies

    * When location restrictions are not specified, then depending on the configuration Composer might build Airflow images either within the GKE cluster or using Cloud Build. Read more about it in [Installing a Python dependency to a private IP environment](https://docs.cloud.google.com/composer/docs/how-to/using/installing-python-dependencies#install-private-ip). Depending on the Composer version, Airflow images might be stored in the selected region (using Artifact Registry) or multi-region to which the selected region belongs to (using Container Registry).

    * If location restrictions are specified, Managed Airflow builds Airflow images within the environment's GKE cluster and stores them in Artifact Registry repository in the selected region.

  * Cloud Monitoring: Stores metrics for environments and executed Airflow DAGs in the region you specify

    * Some metric labels may contain names of DAGs and Managed Airflow environments.
  * Cloud Logging: By default, Managed Airflow stores in Cloud Logging which is a global Google Cloud service. If you want to store Managed Airflow logs in a specific location, you must redirect logs to a Cloud Storage bucket in this location.




For a list of available locations, see [Managed Airflow Regions](https://cloud.google.com/about/locations).

[The Managed Airflow documentation](https://cloud.google.com/composer/docs/concepts/architecture) provides more information on the architectural details of Managed Airflow environments.

## Cloud Data Fusion

Organization policy is enforced when you create an instance. The instance is a regional resource that is created in the region that you specify.

When you create an instance with a customer-managed encryption key (CMEK), the key location must be the same as the instance location.

By default, Cloud Data Fusion creates ephemeral Managed Service for Apache Spark clusters in the same region as the instance for each pipeline. The location for these ephemeral clusters can be changed and isn't enforced by the resource locations organization policy. For static Managed Service for Apache Spark clusters, you can use any of the locations supported by Managed Service for Apache Spark and these locations aren't enforced by the resource locations organization policy.

For a list of available locations, see [Cloud Data Fusion supported regions](https://cloud.google.com/data-fusion/pricing#supported_regions).

## Cloud Deploy

The following are the Cloud Deploy resource types:

  * Delivery pipeline
  * Target
  * Release
  * Rollout
  * Job run



All Cloud Deploy resources are created in the same region where the delivery pipeline was created.

If you have an organization policy against using certain locations, you can't create any Cloud Deploy resources in that region (delivery pipeline, target, release, or rollout).

For a list of available locations for the Cloud Deploy service and its resources, see [About Cloud Deploy regions](https://docs.cloud.google.com/deploy/docs/regions).

## Cloud Domains

Cloud Domains registration resources are global resources and are not subject to resource locations constraints.

## Cloud Healthcare API

The organization policy is enforced when you create a `dataset` resource. `dataset` resources are either regional or multi-regional resources. Data store resources, such as FHIR store, or other lower-level resources, such as HL7v2 messages, can be added to any existing `dataset`, even if the `dataset` resource is in a location that is denied by the organization policy. To ensure that your resources are in compliance with the resource location constraint, create new `dataset` resources after the organization policy is applied, and then migrate data from old `dataset` resources to the new ones.

For a list of available locations, see [Cloud Healthcare API Regions](https://cloud.google.com/healthcare/docs/concepts/regions).

## Cloud Interconnect

A Cloud Interconnect attachment can be created in any region. However, you can't choose a zone. The organizational policy is enforced at the time that you create the Cloud Interconnect attachment.

For a list of available regions, see the Compute Engine [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) page.

## Cloud Intrusion Detection System

Organization policy is enforced when you create a Cloud IDS endpoint, which is a zonal resource. Organization policy compliance isn't enforced retroactively. Existing endpoints will continue to operate even if they are in locations that are denied by the organization policy. To enforce a new resource location constraint on an existing Cloud IDS endpoint, delete the instance and then create it again with the organization policy applied.

For a list of available locations, see [Products available by location](https://cloud.google.com/about/locations).

## Cloud Key Management Service

Cloud KMS resources can be created in regional, dual-regional, multi-regional, or global locations. The organization policy will be enforced at the time you create that resource.

For more information, see the Cloud KMS [locations](https://docs.cloud.google.com/kms/docs/locations) page.

## Cloud Load Balancing

Load balancers using the following products can be created in any regional location:

  * Regional external Application Load Balancer
  * Regional external proxy Network Load Balancer
  * Regional internal Application Load Balancer
  * Regional internal proxy Network Load Balancer
  * Regional external passthrough Network Load Balancer
  * Internal passthrough Network Load Balancer



However, you cannot choose a zone for these load balancers. The organizational policy is enforced at the time that you create the load balancing resource.

For a list of available regional locations, see the Compute Engine [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) page.

## Cloud Logging

Organization policy is enforced when you create new [log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries#about_log_buckets). While you can create a new bucket in any region or set its location to `global`, Logging ensures that you select a region approved by your organization. Organization policy is only enforced on newly created log buckets after you create your organization policy.

For a list of available regions, see the Cloud Logging [Locations](https://docs.cloud.google.com/logging/docs/region-support) page.

## Cloud NAT

A Cloud NAT gateway can be created in any regional location. However, you can't choose a zone for a Cloud NAT gateway. The organizational policy is enforced at the time that you create the Cloud NAT gateway.

For a list of available regional locations, see the Compute Engine [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) page.

## Cloud Next Generation Firewall Enterprise

Organization policy is enforced when you create a Cloud NGFW Enterprise endpoint, which is a zonal resource. Organization policy compliance isn't enforced retroactively. Existing endpoints will continue to operate even if they are in locations that are denied by the organization policy. To enforce a new resource location constraint on an existing Cloud NGFW Enterprise endpoint, delete the instance and then create it again with the organization policy applied.

For a list of available locations, see [Products available by location](https://cloud.google.com/about/locations).

## Cloud Next Generation Firewall Standard

A Cloud NGFW Standard regional network firewall policy can be created in any regional location. However, you can't choose a zone for a Cloud NGFW Standard regional network firewall policy. The organization policy is enforced at the time that you create the Cloud NGFW Standard regional network firewall policy.

For a list of available regional locations, see the Compute Engine [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) page.

## Cloud Router

A Cloud Router can be created in any regional location. However, you can't choose a zone for a Cloud Router. The organizational policy is enforced at the time that you create the Cloud Router.

For a list of available regional locations, see the Compute Engine [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) page.

## Cloud Run

Organization policy is enforced when you create a top-level resource, such as a `Service`. It is not enforced on any already existing resources or on updates to existing resources, even if those updates lead to the creation of a lower level resource, such as a `Revision`.

For a list of available regions, see the Cloud Run [locations](https://docs.cloud.google.com/run/docs/locations) page.

## Cloud Run functions

Organization policy is enforced when you create or update a Cloud Run function resource. It is not enforced on any already existing resources.

For a list of available regions, see [Cloud Run functions locations](https://docs.cloud.google.com/functions/docs/locations).

## Cloud Scheduler

Organization policy is enforced when you create or update a Cloud Scheduler `Job` resource. It isn't enforced on any already existing resources.

For a list of available regions, see [Cloud Scheduler locations](https://docs.cloud.google.com/scheduler/docs/locations).

## Cloud Service Mesh

Organization policy is enforced when you attempt to provision Cloud Service Mesh or create workloads for the mesh. Cloud Service Mesh does **not** enforce organization policies when workloads are registered to the mesh.

See relevant documentation for your specific service workloads:

  * Fleet
  * Compute Engine
  * GKE
  * Cloud Run
  * GKE Multi-Cloud



See the list of available regions for your Cloud Service Mesh computing infrastructure:

  * [Managed Control Plane using Istio APIs](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed#regions)
  * [Managed Control Plane using Google Cloud APIs](https://docs.cloud.google.com/service-mesh/docs/service-routing/features#supported-platforms)



## Cloud SQL

Organization policy is enforced when you create an instance. The instance is a regional resource that will create a zonal database, for which the resource location is not enforced. When you create read replicas or database clones, you locate the new resources in the same region as the original, so the resource locations organization policy isn't enforced.

For a list of available locations, see the Cloud SQL [Instance Locations](https://docs.cloud.google.com/sql/docs/mysql/instance-locations) page.

## Cloud Storage

Organization policy is enforced when you create a `bucket` resource. `Bucket` resources are regional or multi-regional. `Object` resources can be added to any existing `bucket` even if the `object` is in a location that is denied by the resource locations organization policy. To ensure that your resources are in compliance with the resource locations organization policy, create new `bucket` resources after the organization policy is applied, and then migrate data from old `bucket` resources to the new ones.

For a list of available locations, see the Cloud Storage [Bucket Locations](https://docs.cloud.google.com/storage/docs/bucket-locations) page.

## Cloud Tasks

Organization policy is enforced when you create a queue. It is not enforced on queues that were created before the organization policy was set, or on updates to such queues.

For a list of available locations, see [Products available by region](https://cloud.google.com/about/locations).

### Limitations

Limitations apply to the following regions:

  * `us-central1`
  * `us-central2` (private Google Cloud region)



When you have any of the regions mentioned earlier in your organization policy, you must include both `us-central1` and `us-central2`, even if you are not creating Cloud Tasks resources in these regions. You can include the region `us-central2` in your organization policy even if your organization doesn't use private regions.

## Cloud Trace

Trace data is stored in [observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/storage-overview#storage-model), which are subject to organization policies enforced by Google Cloud Observability at the time of creation. Organization policy compliance isn't enforced retroactively.

For more information, see the Google Cloud Observability section of this document.

## Cloud TPU

Cloud TPU resources (TPU nodes and TPU VMs) are zonal resources. This means you must select a specific zone within a Google Cloud region when creating a Cloud TPU resource.

The availability of specific Cloud TPU accelerator types (such as v3, v4, v5e, or v5p) varies by zone. Not all zones offer all types of TPUs. Organization policies that enforce resource location constraints are checked during the creation of Cloud TPU resources. If an organization policy restricts deployment in the chosen zone, the TPU resource creation is blocked.

For a list of available regions and zones where Cloud TPU is supported, see [Cloud TPU locations and zones](https://docs.cloud.google.com/tpu/docs/regions-zones).

## Cloud Translation - Advanced API (v3)

To ensure that your Cloud Translation resources are in compliance with the resource location constraint, specify a regional endpoint when creating the resource. The resource location constraint is enforced when you create a Cloud Translation resource.

For information about how to use regional endpoints, see [Specify a regional endpoint](https://docs.cloud.google.com/translate/docs/advanced/endpoints).

## Cloud VPN

A Cloud VPN gateway can be created in any regional location. However, you can't choose a zone for a Cloud VPN gateway. The organization policy is enforced at the time that you create the Cloud VPN gateway.

For a list of available regional locations, see the Compute Engine [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) page.

## Cloud Workstations

Organization policy is enforced when you create new regional resources such as workstation clusters, workstation configurations, and workstations. Creation of a workstation configuration might result in the creation of Compute Engine persistent disks and VMs, so you can create these resources only in zones that your organization policy allows.

For a list of available locations, see [Cloud Workstations locations](https://docs.cloud.google.com/workstations/docs/locations).

## Cluster Director

The organization policy is enforced when you create a cluster in Cluster Director.

Cluster Director clusters are regional resources. This means the location of the resource determines the target region where all data is processed and stored.

## Compute Engine

Compute Engine offers a variety of [resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources), and these can be global, regional, or zonal. Regional and zonal resources are subject to the resource location constraints. Global resources are not subject to the resource locations constraint, but some global resources use regional and zonal resources; those regional and zonal resources are subject to the resource locations constraint.

For example, an instance template is a global resource, but you might specify regional or zonal disks in an instance template. Those disks are subject to the resource locations constraints, so, in your instance template, you must specify disks in regions and zones that your org policy permits.

### Limitations

All Compute Engine resources support the resource location constraints that you specify, with the following exceptions.

  * Snapshots and images

    * When you create a snapshot or image, you must [specify a storage location](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#create_snapshots) in a permitted location, otherwise the creation of the snapshot or image might fail.
  * Managed instance groups

    * Some managed instance group (MIG) operations rely on the creation or recreation of VMs in permitted zones. These operations include: scaling out (manually or through autoscaling), autohealing, autoupdating, and proactive instance redistribution. For those operations to succeed, your MIGs must exist in locations that are allowed by your org's resource location constraint.

    * Create MIGs in permitted locations. For regional MIGs, [select zones](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#selectingzones) that are not location restricted.

    * If you have a pre-existing zonal or regional MIG, and later set a resource location constraint, MIG operations will fail if they violate the constraint. You must recreate the MIG in a permitted location.

  * Sole-tenant nodes

    * If you have a pre-existing node group and later set a resource location constraint, you can't scale out the group to add new hosts (manually or through autoscaling) if the group's location violates the constraint.



For a list of available locations, see the Compute Engine [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) page.

## Config Controller

Config Controller uses [Compute Engine regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones). Enforcement of the resource locations is handled at the level of the Compute Engine resource when you create the cluster. To scale a cluster by adding more instances these new additions must also be in an allowed location.

To create clusters with sufficient redundancy, use [value groups](https://docs.cloud.google.com/organization-policy/restrict-locations#value_groups) to control the locations that are restricted. If you set the locations manually, all zones in that region must be in the allowed list to have the same level of redundancy. Auto-scaling clusters can break if any of the locations in which scaling happens aren't in the list of allowed locations defined in the organization policy.

## Customer Experience Insights

The organization policy is enforced when you create a `conversation` in Customer Experience Insights. `conversation` resources are regional.

For a list of available locations, see the [Customer Experience Insights locations page](https://docs.cloud.google.com/contact-center/insights/docs/regionalization).

## Customer Experience Agent Studio

Organization policy is enforced when you create an agent application.

For a list of available locations, see the [Customer Experience Agent Studio Locations](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/reference/region) page.

## Database Migration Service

Organization policy is enforced when you create any of the following Database Migration Service resources:

  * [Migration Jobs](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs)
  * [Connection profiles](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles)
  * [Conversion Workspaces](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces)
  * [Private connections](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections)



The policy is enforced when the resource is created. Applying a resource locations constraint doesn't affect existing resources or updates to those resources.

## Data Lineage API

Organization policy is enforced when you create or update a `Process` using either the [CreateProcess](https://docs.cloud.google.com/data-catalog/docs/reference/data-lineage/rpc/google.cloud.datacatalog.lineage.v1#google.cloud.datacatalog.lineage.v1.Lineage.CreateProcess), [UpdateProcess](https://docs.cloud.google.com/data-catalog/docs/reference/data-lineage/rpc/google.cloud.datacatalog.lineage.v1#google.cloud.datacatalog.lineage.v1.Lineage.UpdateProcess), or [ProcessOpenLineageRunEvent](https://docs.cloud.google.com/data-catalog/docs/reference/data-lineage/rpc/google.cloud.datacatalog.lineage.v1#google.cloud.datacatalog.lineage.v1.Lineage.ProcessOpenLineageRunEvent) method.

Children resources (`Runs` or `Events`) can be updated or added to any existing `Process` even if the `Process` is in a location that is denied by the resource location organization policy. To ensure that all your resources are in compliance with the resource location organization policy, create new `Process` after the organization policy is applied.

**Note:** If you use the `ProcessOpenLineageRunEvent` method to update existing Lineage children resources, the policy will still be enforced. In case this is undesirable, use alternative API methods, such as `UpdateRun`, for which the policy is not enforced.

## Dataflow

The organization policy is enforced when you create a `job`. A `job` is a regional resource that uses both Cloud Storage and Compute Engine. You can configure Compute Engine workers to execute in a zone outside the region of the job by specifying the zone parameter. In this case, the Dataflow control plane will execute in the specified region, while data processing workers will execute in the specified zone. If you don't specify the zone of workers, the workers will be created within the region in which the `job` is configured to run.

If you don't specify the zone of the `job`, the location of the workers will be in one of the zones within the region in which the `job` is configured to run. Dataflow will select the zone based on the available capacity in the zone. All zones within the region of the `job` should be set as allowed values in the resource locations organization policy.

Auto-scaling clusters can break if any of the locations in which scaling happens aren't in the list of allowed locations defined in the organization policy.

For a list of available locations, see the Dataflow [Regional endpoints](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints) page.

## Dataform

Dataform resources are regional. When you create a Dataform repository, the repository and all its child resources are constrained to the region specified on repository creation.

For a list of available locations, see [Dataform locations](https://docs.cloud.google.com/dataform/docs/locations).

## Knowledge Catalog

The organization policy is enforced when you create any of the following Knowledge Catalog resources:

  * [Entry Groups](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.entryGroups)
  * [Entry Types](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.entryTypes)
  * [Aspect Types](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.aspectTypes)
  * [Data Scans](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.dataScans)
  * [Metadata Jobs](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.metadataJobs).



The policy is enforced when the resource is created. Applying a resource locations constraint doesn't affect existing resources or updates to those resources.

## Managed Service for Apache Spark

When you create a `cluster`, the organization policy is enforced based on the region you specify in the creation request. The location of a `job` is bound by the location of the `cluster` that is its parent when the `submit` method is called.

For a list of available locations, see the Managed Service for Apache Spark [Regional endpoints](https://docs.cloud.google.com/dataproc/docs/concepts/regional-endpoints) page.

## Dataproc Metastore

When you create a `service`, the organization policy is enforced based on the region you specify in the creation request. The location of `backups` and `metadataImports` are bound by the location of the `service` that is its parent when the `importMetadata` and `backupService` methods are called.

For a list of available locations, see the [Dataproc Metastore locations](https://docs.cloud.google.com/dataproc-metastore/docs/locations) page.

## Datastore

The Datastore `database` resources are directly dependent on the App Engine application in the parent project and its defined location. Disabling the App Engine application will block API access for the associated database. To delete replicated data from the physical locations, delete the project as described in the App Engine section.

For a list of available locations, see the [Datastore Locations](https://docs.cloud.google.com/datastore/docs/locations) page.

## Datastream

The organization policy is enforced when you create any of the following Datastream resources:

  * [Stream](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams)
  * [Connection profiles](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles)
  * [Private connections](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.privateConnections)



The policy is enforced when the resource is created. Applying a resource locations constraint doesn't affect existing resources or updates to those resources.

## Developer Connect

The organization policy is enforced when you create any of the following Developer Connect resources:

  * [Connection](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections)
  * [Git repository link](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks)



The policy is enforced when the resource is created. Applying a resource locations constraint doesn't affect existing resources or updates to those resources.

For a list of available locations, see [Developer Connect locations](https://docs.cloud.google.com/developer-connect/docs/locations).

## Dialogflow

Organization policy is enforced when you create an `agent` or a `location setting` resource in Dialogflow CX (Dialogflow ES doesn't enforce organization policy yet). Both `agent` resources and `location setting` resources are regional or multi-regional. Other Dialogflow resources, such as `intents` or `flows`, can be added to any existing `agent`, even if the `agent` resource is in a location that is denied by the organization policy. To ensure that your resources are in compliance with the resource location constraint, create new `agent` resources after the organization policy is applied, and then migrate data from the old `agent` resources to the new ones.

Resource location constraints do not apply to the `global` location; resource creation is always allowed.

For a list of available locations, see the [Dialogflow Locations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region) page.

## Document AI

Document AI resources are regional. When you create a `Processor` or `LabelerPool` resource, the resource location organization policy is enforced and restricts the regions in which new resources can be created or stored.

Organization policy compliance isn't enforced retroactively. New Document AI resources can be created under existing parent resources, even if the parent's resource location is denied by the resource locations organization policy. To enforce a new resource location constraint on an existing resource, delete the resource and create it again with the organization policy applied.

For a list of available locations, see the Document AI [Multi-regional support](https://docs.cloud.google.com/document-ai/docs/regions) page.

## Eventarc

Organization policy is enforced when you [create an Eventarc trigger](https://docs.cloud.google.com/eventarc/docs/targets). The policy is not enforced on already existing resources or on updates to existing resources. Triggers can be either a global or regional resource. Global resources are not subject to the resource locations constraint.

If the resource locations constraint is enforced, only regional triggers whose regions exactly match those applied in the resource locations constraint or are included in the [value group](https://docs.cloud.google.com/organization-policy/restrict-locations#value_groups) can be created. For example, if either `us-central1` or `us-locations` are in the list of allowed locations defined in the organization policy, you can create a `us-central1` trigger.

For a list of available locations, see [Eventarc locations](https://docs.cloud.google.com/eventarc/docs/locations).

## Filestore

Organization policy is enforced when you create a Filestore instance, which can be a zonal or regional resource. Organization policy compliance isn't enforced retroactively. Existing instances will continue to operate even if they are in locations that are denied by the organization policy. To enforce a new resource location constraint on an existing Filestore instance, delete the instance and then create it again with the organization policy applied.

For a list of available locations, see the [Filestore Regions and Zones](https://docs.cloud.google.com/filestore/docs/regions) page.

## Financial Research Agent

The `AnalystAgentPersona` resource is multi-regional. Organization policy compliance isn't enforced retroactively. Organization policy is checked only when creating an `AnalystAgentPersona`. To enforce a new resource locations constraint on an existing `AnalystAgentPersona`, delete the resource and create it again with the organization policy applied to the parent resource.

Available locations are `eu`, `us` and `global`.

## Firebase Data Connect

When you create a regional database, organization policies are enforced that produce a Firebase Data Connect database that contains service, schema, and connector information. In addition, this information maps to a corresponding Cloud SQL database that's located in the same region. The Cloud SQL database has its own organization policy.

For a list of available locations, see the [Firebase Data Connect Locations](https://firebase.google.com/docs/data-connect/manage-services-and-databases#available-locations) page.

## Firestore

The Firestore `database` resources are directly dependent on the App Engine application in the parent project and its defined location. Disabling the App Engine application will block API access for the associated database. To delete replicated data from the physical locations, delete the project as described in the App Engine section.

For a list of available locations, see the [Firestore Locations](https://docs.cloud.google.com/firestore/docs/locations) page.

## Fleet

Cloud Fleet `membership` resources only support region locations in [Compute Engine regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones). Enforcement of the resource locations is handled at the level of the `membership` resource when you register a cluster. Fleet memberships are supported in global and regional locations.

To create memberships with sufficient redundancy, use [value groups](https://docs.cloud.google.com/organization-policy/restrict-locations#value_groups) to control the regions that are restricted. Constraints on multi-region locations and zone locations have no effect on Fleet `membership`. However, constraints on value groups that contain regions do have an effect. For example, the value `asia` in an organization policy has no effect on Fleet membership, but the value `in:asia-locations` does have an effect.

## Gemini Enterprise Agent Platform

Resource locations constraints apply to all Gemini Enterprise Agent Platform resources. Organization policy compliance isn't retroactively enforced. This means that applying a resource locations constraint doesn't affect any pre-existing resources or updates to those resources. Resource location constraints don't apply to Model Garden publisher models because they aren't Google Cloud resources.

Agent Platform only supports region locations. Constraints on multi-region locations and zone locations have no effect on Agent Platform. However, constraints on [value groups](https://docs.cloud.google.com/organization-policy/restrict-locations#value_groups) that contain regions do have an effect. For example, the value `asia` in an organization policy has no effect on Agent Platform, but the value `in:asia-locations` does have an effect.

Learn more about [locations for machine learning services](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/locations).

### Limitations

Resource location restrictions are enforced in the following interfaces for Agent Platform:

  * `Agent Studio` (UI)



Resource location restrictions are not enforced in the following interfaces:

  * `Gen AI SDK for Python`
  * `Gen AI SDK for Go`
  * `Gen AI SDK for Node.js`
  * `Gen AI SDK for Java`
  * `Gen AI SDK for C#`
  * `REST API`



You can instead use the endpoint restriction constraint to block locations by defining a list of denied `aiplatform.googleapis.com` locational API endpoints.

For more information, see [Restrict endpoint usage](https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage).

For more information about this limitation, see the [Issue Tracker](https://issuetracker.google.com/404207829).

**Note:** The limitation affects all regions, but the issue tracker specifically mentions `EU`.

## GKE Multi-Cloud

The organization policy is enforced when you use the [GKE Multi-Cloud API](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs) to create the following clusters:

  * GKE on AWS
  * GKE on Azure
  * GKE attached clusters



For a list of available locations, see the following pages for each cluster platform.

  * [GKE on AWS regions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/gcp-managed-regions)
  * [GKE on Azure regions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/gcp-managed-regions)
  * [GKE attached clusters: EKS regions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/supported-regions)
  * [GKE attached clusters: AKS regions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/reference/supported-regions)
  * [GKE attached clusters: CNCF conformant clusters regions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/reference/supported-regions)



## Network Services API

When you create a Network Services API resource, the organization policy is enforced based on the region you specify in the creation request. The policy is not enforced on already existing resources. Global resources are not subject to the resource locations constraint.

## Google Cloud Armor

When you create a Cloud Armor security policy, the organization policy is enforced based on the region you specify in the creation request. The policy is not enforced on already existing resources. Global resources are not subject to the resource locations constraint.

For a list of available regional locations, see the Compute Engine [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) page.

## Google Cloud Contact Center as a Service

The `ContactCenter` resource is regional. Organization policy compliance isn't enforced retroactively. Organization policy is checked when creating a `ContactCenter`.

For a list of available locations, see [Google Cloud Contact Center as a Service locations](https://docs.cloud.google.com/contact-center/ccai-platform/docs/localities).

## Google Cloud Managed Lustre

The organization policy is enforced when you create an instance in Managed Lustre.

Managed Lustre instances are regional resources. This means the location of the resource determines the target region where all data is processed and stored.

For a list of available locations where you can create your instances, see [Supported Regions](https://docs.cloud.google.com/managed-lustre/docs/locations).

## Google Cloud Managed Service for Apache Kafka

The organization policy is enforced when you create a cluster in Managed Service for Apache Kafka.

Managed Service for Apache Kafka clusters are regional resources. This means the location of the resource determines the target region where all data is processed and stored.

For a list of available locations where you can create your clusters, see [Supported Regions](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/locations).

## Google Cloud NetApp Volumes

Organization policy is enforced when you create a NetApp Volumes storage pool or volume, which can be a regional resource. Organization policy compliance isn't enforced retroactively. Existing storage pools will continue to operate even if they are in locations that are denied by the organization policy. To enforce a new resource location constraint on an existing NetApp Volumes storage pool or volume, delete the resource and then create it again with the organization policy applied.

For a list of available locations, see the [NetApp Volumes locations](https://docs.cloud.google.com/netapp/volumes/docs/locations) page.

## Google Cloud Observability

Google Cloud Observability enforces organization policies when it creates an [observability bucket](https://docs.cloud.google.com/stackdriver/docs/observability/storage-overview#storage-model). Organization policy compliance isn't enforced retroactively. Existing observability buckets remain usable even if they are in locations that the organization policy denies.

When multiple locations are supported, you can set a specific location for new observability buckets. For more information, see [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets).

For a list of available locations, see [Observability buckets locations](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).

## Google Kubernetes Engine

Google Kubernetes Engine uses [Compute Engine regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones). Enforcement of the resource locations is handled at the level of the Compute Engine resource when you create the VM for a cluster. If you want to scale a cluster by adding more instances or adding another zone, these new additions must also be in an allowed location.

To create clusters with sufficient redundancy, use [value groups](https://docs.cloud.google.com/organization-policy/restrict-locations#value_groups) to control the locations that are restricted. If you set the locations manually, all zones in that region must be in the allowed list to have the same level of redundancy. Auto-scaling clusters can break if any of the locations in which scaling happens aren't in the list of allowed locations defined in the organization policy.

## Infrastructure Manager

Infrastructure Manager uses [these Google Cloud regions](https://docs.cloud.google.com/infrastructure-manager/docs/locations#regions) for creating Infra Manager [Deployments](https://docs.cloud.google.com/infrastructure-manager/docs/deployments-revisions#deployments).

Additionally, Infrastructure Manager uses [HCL](https://developer.hashicorp.com/terraform/language/syntax/configuration) as the configuration language to actuate resources using [Terraform](https://www.terraform.io/).

Resource location constraints are enforced for both Infra Manager [Deployment](https://docs.cloud.google.com/infrastructure-manager/docs/deployments-revisions#deployments) resources as well as the supported Google Cloud resources defined in HCL.

## Integration Connectors API

The organization policy is enforced when you use the [Integration Connectors API](https://docs.cloud.google.com/integration-connectors/docs/reference/rest) to create the following resources:

  * [Connection](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections)
  * [Endpoint Attachment](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.endpointAttachments)
  * [Event Subscription](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections.eventSubscriptions)



For a list of available locations, see [Integration Connectors locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

## Looker (Google Cloud core)

Looker (Google Cloud core) resources can be created in regional locations. The organization policy will be enforced at the time you create that resource.

For a list of available regions, see the [Create a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-create) page.

## Managed Service for Microsoft Active Directory

Organization policy is enforced when you create Managed Microsoft AD domains or update existing AD resources. Managed Microsoft AD requires the `global` location to be allowed. If the `global` location is not allowed, domain creation and resource updates will fail.

Learn how to [view and update the resource location constraint to `global`](https://docs.cloud.google.com/managed-microsoft-ad/docs/troubleshooting#resource_location_restriction_organization_policy).

## Memorystore for Memcached

The organization policy is enforced when you create an instance. The instance is a regional resource that creates one or more zonal caches depending on the number of nodes selected. When you add nodes using a scale-up operation, you locate the new resources in the same region as the original instance. The location organization policy is enforced during scale-up.

For a list of available locations, see the Memorystore for Memcached [Regions and Zones](https://docs.cloud.google.com/memorystore/docs/memcached/regions) page.

## Memorystore for Redis

Organization policy is enforced when you create an instance. The instance is a regional resource that will create one or more zonal caches depending on the selected instance tier. Basic tier instances deploy a single cache within a specified region and zone. Standard tier instances deploy a zonal cache and one or more zonal cache replicas which are located within the instance's region. When you create additional replicas, you locate the new resources in the same region as the original zonal cache. The location organization policy is enforced when creating additional replicas.

For a list of available locations, see the Memorystore for Redis [Regions and Zones](https://docs.cloud.google.com/memorystore/docs/redis/regions) page.

## Memorystore for Redis Cluster

Organization policy is enforced when you create an instance. The instance is a regional resource that will create one or more zonal caches depending on selected zone distribution mode. When you create additional replicas or shards, you locate the new resources in the same region as the original zonal cache. The location organization policy is enforced when creating additional replicas.

For a list of available locations, see the Memorystore for Redis Cluster [Locations](https://docs.cloud.google.com/memorystore/docs/cluster/locations) page.

## Memorystore for Valkey

Organization policy is enforced when you create an instance. The instance is a regional resource that will create one or more zonal caches depending on selected zone distribution mode. When you create additional replicas or shards, you locate the new resources in the same region as the original zonal cache. The location organization policy is enforced when creating additional replicas.

For a list of available locations, see the Memorystore for Valkey [Locations](https://docs.cloud.google.com/memorystore/docs/valkey/locations) page.

## Migrate to Virtual Machines

Organization policy is enforced when you create a Migrate to VMs resource. Migrate to VMs image and migration resources are all regional resources. The `TargetProject` resource, which contains the ID of the project that is used as the target project of the migration and import jobs, is a global resource.

## Model Armor

Organization policy is enforced when you create a `template` resource.

For a list of available locations, see the [Model Armor locations](https://docs.cloud.google.com/model-armor/locations) page.

## Network Connectivity Center

You can create Network Connectivity Center hub and VPC spoke resources globally. Hybrid spoke resources can be created in any regional location. Organization policy is enforced when you create the spoke resource.

For a list of available regional locations, see the Compute Engine [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) page.

NCC Gateway spoke resources can be created in regions that have the `GATEWAY_SPOKES` feature enabled. To see an updated list of supported regions, use the [`gcloud network-connectivity locations list`](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/locations) command.

## Network Intelligence Center - Connectivity Tests

Connectivity Tests resources can be created in the global location. The organization policy will be enforced at the time you create that resource.

## Parameter Manager

Resource locations constraints apply to all Parameter Manager resources.

Organization policies are enforced when you create a parameter. Existing parameters are not automatically moved if location constraints change.

For a list of available locations where you can create your parameters, see [Locations for Parameter Manager resources](https://docs.cloud.google.com/secret-manager/docs/locations#parameter_manager_locations).

## Persistent Disk

The organization policy is enforced when you create a `disk` resource, which can then be attached to virtual machines:

  * After you create a zonal `disk` resource, you can attach it to virtual machine instances in the same zone.
  * After you create a regional `disk` resource, you can attach it to virtual machine instances in one of the two zones the `disk` resides in.



Organization policy compliance isn't enforced retroactively. To enforce a new resource locations organization policy on existing `disk` resources, you need to delete the `disk` resources and then create them again with the organization policy applied to the parent resource.

For a list of available locations, see the Compute Engine [Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones) page.

## Pub/Sub

The resource locations organization policy affects the locations in which messages published to a `topic` can be persisted at rest. The organization policy is enforced when you publish messages to a `topic`. Note that a `topic` is still a global resource that is accessible from anywhere in the world to authorized clients.

Changes to the organization policy are not retroactive, and will not be applied to existing `topics`. If a new resource locations constraint denies a location where messages published to a `topic` are already stored, those messages will not be automatically moved.

For more information, see the Pub/Sub [Restricting Pub/Sub resource locations](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction) page.

## Pub/Sub Lite

The resource locations organization policy affects the locations in which a `topic` can be created, which determines where messages will be persisted. A `topic` is a zonal resource, but messages can be requested from any location, including outside of Google Cloud.

Changes to the organization policy are not retroactive, and will not be applied to existing `topics`. If a new resource locations constraint denies a location where messages published to a `topic` are already stored, those messages will not be automatically moved.

## Secret Manager

Secrets can have either an automatic replication policy or a user managed replication policy.

When using an automatic replication policy, payload data is replicated without restriction. Secret Manager requires the `global` location to be allowed when creating a secret with an automatic replication policy. If the `global` location is not allowed, secret creation will fail.

When using a user managed replication policy, payload data is replicated to a user-defined set of supported locations. Secret Manager requires all locations in the replication policy to be allowed when creating a secret with a user managed replication policy. If any of the locations in a secret's replication policy are not allowed, secret creation will fail.

The organization policy will be enforced at the time you create that secret.

For more information, see the Secret Manager [locations](https://docs.cloud.google.com/secret-manager/docs/locations) page.

## Secure Source Manager

Organization policy is enforced when you create new Secure Source Manager instances. Secure Source Manager ensures that you select a region approved by your organization. Organization policy is only enforced on newly created Secure Source Manager instances in a region after you create the organization policy.

For more information, see the [Secure Source Manager overview](https://docs.cloud.google.com/secure-source-manager/overview/overview) page.

## Secure Web Proxy

A Secure Web Proxy can be created in any regional location. However, you can't choose a zone for a Secure Web Proxy. The organizational policy is enforced at the time that you create the Secure Web Proxy.

For a list of available locations, see [Products available by location](https://cloud.google.com/about/locations).

## Sensitive Data Protection

Resource location constraints apply to all Sensitive Data Protection resources.

Changes to the organization policy are not retroactive and will not be applied to existing resources.

Learn more about [regions available for Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/locations).

## Serverless VPC Access

Organization policy is enforced when you create new Serverless VPC Access connector instances. Organization policy is only enforced on newly created Serverless VPC Access connector instances in a region after you create the organization policy.

For more information, see the Serverless VPC Access [Supported Regions](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access).

## Service Extensions

The following resources are regional:

  * [`WasmPlugin`](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/projects.locations.wasmPlugins)
  * [`WasmPluginVersion`](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/projects.locations.wasmPlugins.versions)



Organization policy is enforced when you create these resources.

## Spanner

Organization policy is enforced when you create an instance. Instances are either regional or multi-regional resources. If an instance is blocked by the resource locations organization policy, the only way to bring the resource into compliance is by deleting the instance. Instances that are blocked by the resource locations organization policy will still allow for reads, writes, and the creation of database resources.

For a list of available locations, see the Spanner [Instances](https://docs.cloud.google.com/spanner/docs/instances) page.

## Speech-to-Text

The resource locations organization policy affects the locations in which any Speech-to-Text resource can be created. It also affects the locations in which the `config` resource can be updated.

Speech-to-Text v1 is available in the `global`, `eu`, and `us` regions. Learn more about [Speech-to-Text v2 available regions](https://docs.cloud.google.com/speech-to-text/v2/docs/locations).

## Storage Transfer Service

Organization policy is enforced when you create a Storage Transfer Service job. Organization policy ensures compliance by allowing Storage Transfer Service jobs to be created only in allowed regions. If the Storage Transfer Service job's region is outside of organization policy constraints, the job won't be successfully created.

To learn how Storage Transfer Service chooses the region in which to run a Storage Transfer Service job, refer to [Location of Storage Transfer Service jobs](https://docs.cloud.google.com/storage-transfer/docs/known-limitations-transfer#locations).

## Live Stream API

The `input`, `channel`, `asset`, and `pool` resources are regional. You can specify a location when creating the resource. The organization policy is enforced at the time you create the resource.

For a list of available regions, see [Live Stream API locations](https://docs.cloud.google.com/livestream/docs/locations#regions).

## Transcoder API

`job` and `jobTemplate` resources are regional. You can specify a location when creating the resource. The organization policy is enforced at the time you create the resource.

For a list of available regions, see [Transcoder API locations](https://docs.cloud.google.com/transcoder/docs/locations#regions).

## Virtual Private Cloud

[Virtual Private Cloud (VPC) networks](https://docs.cloud.google.com/vpc/docs/vpc) are global virtual networks that contain regional virtual subnetworks (subnets). Resource location constraints don't apply to VPC networks, because they are global resources. Resource location constraints are enforced on subnetworks at the time of subnetwork creation. If you create an [auto mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges), subnetworks are created only in the regions that are allowed by the resource location constraint.

For a list of available regions, see the Compute Engine [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) page.

## Workflows

Organization policy is enforced when you [create a Workflows workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#create_a_workflow). The policy is not enforced on already existing resources or on updates to existing resources. Workflows are regional resources and are subject to the resource locations constraint.

If the resource locations constraint is enforced, only workflows whose regions exactly match those applied in the resource locations constraint or are included in the [value group](https://docs.cloud.google.com/organization-policy/restrict-locations#value_groups) can be created. For example, if either `us-central1` or `us-locations` are in the list of allowed locations defined in the organization policy, you can create a `us-central1` workflow.

For a list of available locations, see [Workflows locations](https://docs.cloud.google.com/workflows/docs/locations).

## Workload Manager

Organization policy is enforced when you create a Workload Manager [Evaluation](https://docs.cloud.google.com/workload-manager/docs/about-evaluations) or [Deployment](https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment) resource. Evaluations and Deployments are regional resources and are subject to the resource locations constraint.

For a list of available locations, see [supported locations](https://docs.cloud.google.com/workload-manager/docs/evaluate/locations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
