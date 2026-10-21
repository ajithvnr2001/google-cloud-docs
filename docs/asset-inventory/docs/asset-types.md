---
url: https://docs.cloud.google.com/asset-inventory/docs/asset-types/
title: Asset types \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:02.603921+00:00
---

# Asset types  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/asset-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Asset types Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the supported asset types in Cloud Asset Inventory. These include resource types, policy types, and runtime information types.

You can use these asset types with the following Cloud Asset Inventory operations:

  * [Export to BigQuery](https://docs.cloud.google.com/asset-inventory/docs/export-bigquery)

  * [Export to Cloud Storage](https://docs.cloud.google.com/asset-inventory/docs/export-cloud-storage)

  * [List assets](https://docs.cloud.google.com/asset-inventory/docs/list-assets)

  * [Monitor asset changes with Pub/Sub](https://docs.cloud.google.com/asset-inventory/docs/monitor-asset-changes)

  * [Query assets with SQL](https://docs.cloud.google.com/asset-inventory/docs/query-assets-with-sql)

  * [Search for resources](https://docs.cloud.google.com/asset-inventory/docs/search-resources)

  * [Search resources for IAM allow policies](https://docs.cloud.google.com/asset-inventory/docs/search-allow-policies)




You might also need to make use of [asset names](https://docs.cloud.google.com/asset-inventory/docs/asset-names) associated with these asset types when working with Cloud Asset Inventory.

Unless otherwise specified, all resource types are available in the export, list, monitor, search, and analysis APIs. Effective tags are supported only in the search APIs.

## Resource types

Cloud Asset Inventory provides eventual consistency on current data and best-effort consistency on historical data. While rare, it's possible that Cloud Asset Inventory can miss some data updates. To learn more, see [Cloud Asset Inventory's consistency model](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#consistency-model).

Unless noted in the following table, data is synchronized once every few hours. If a sync fails, data freshness is delayed until the next successful sync.

Cloud Asset Inventory uses the following asset types for the `RESOURCE` [content type](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types).

Service | Asset type  
---|---  
**Access Approval** |  [API reference](https://accessapproval.googleapis.com/$discovery/rest?version=v1)

  * [ ` accessapproval.googleapis.com/AccessApprovalSettings ` ](https://docs.cloud.google.com/assured-workloads/access-approval/docs/reference/rest/v1/AccessApprovalSettings) Not available in the analysis APIs. 

  
**Access Policy (Access Context Manager)** To retrieve all access policies in the export, list, and monitor APIs:

  * **REST** : Set the `contentType` to `ACCESS_POLICY`.
  * **gcloud CLI** : Set the `--content-type` flag to `access-policy`.

| 

  * [ ` accesscontextmanager.googleapis.com/AuthorizedOrgsDesc ` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.authorizedOrgsDescs) Not available in the analysis APIs. 
  * [ ` identity.accesscontextmanager.googleapis.com/AccessLevel ` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels)
  * [ ` identity.accesscontextmanager.googleapis.com/AccessPolicy ` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies)
  * [ ` identity.accesscontextmanager.googleapis.com/ServicePerimeter ` ](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters)

  
**Agent Identity API** |  [API reference](https://agentidentity.googleapis.com/$discovery/rest?version=v1)

  * [ ` agentidentity.googleapis.com/AuthProvider ` ](https://docs.cloud.google.com/iam/docs/reference/agentidentity/rest/v1/projects.locations.authProviders) Not available in the analysis APIs. 

  
**AI Commerce Search API** |  [API reference](https://retail.googleapis.com/$discovery/rest?version=v2)

  * [ ` retail.googleapis.com/Catalog ` ](https://docs.cloud.google.com/retail/docs/reference/rest/v2/projects.locations.catalogs)

  
**AlloyDB for PostgreSQL** |  [API reference](https://alloydb.googleapis.com/$discovery/rest?version=v1)

  * [ ` alloydb.googleapis.com/Backup ` ](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.backups) Not available in the analysis APIs. 
  * [ ` alloydb.googleapis.com/Cluster ` ](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters) Not available in the analysis APIs. 
  * [ ` alloydb.googleapis.com/Instance ` ](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances) Not available in the analysis APIs. 

  
**API Gateway** |  [API reference](https://apigateway.googleapis.com/$discovery/rest?version=v1)

  * [ ` apigateway.googleapis.com/Api ` ](https://docs.cloud.google.com/api-gateway/docs/reference/rest/v1/projects.locations.apis)
  * [ ` apigateway.googleapis.com/ApiConfig ` ](https://docs.cloud.google.com/api-gateway/docs/reference/rest/v1/projects.locations.apis.configs)
  * [ ` apigateway.googleapis.com/Gateway ` ](https://docs.cloud.google.com/api-gateway/docs/reference/rest/v1/projects.locations.gateways)

  
**API keys** The `location` field might not be populated for API keys assets. |  [API reference](https://apikeys.googleapis.com/$discovery/rest?version=v2)

  * [ ` apikeys.googleapis.com/Key ` ](https://docs.cloud.google.com/api-keys/docs/reference/rest/v2/keys)

  
**Apigee** |  [API reference](https://apigee.googleapis.com/$discovery/rest?version=v1)

  * [ ` apigee.googleapis.com/ApiProxy ` ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` apigee.googleapis.com/ApiProxyRevision ` ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` apigee.googleapis.com/Environment ` ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` apigee.googleapis.com/Instance ` ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances) Effective tags aren't supported. 
  * [ ` apigee.googleapis.com/Organization ` ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations) Effective tags aren't supported. 
  * [ ` apigee.googleapis.com/SecurityAction ` ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.securityActions) Not available in the analysis APIs. 
  * [ ` apigee.googleapis.com/SecurityMonitoringCondition ` ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityMonitoringConditions) Not available in the analysis APIs. 
  * [ ` apigee.googleapis.com/SecurityProfileV2 ` ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityProfilesV2) Not available in the analysis APIs. 

  
**Apigee API hub** |  [API reference](https://apihub.googleapis.com/$discovery/rest?version=v1)

  * [ ` apihub.googleapis.com/ApiHubInstance ` ](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apiHubInstances)

  
**App Design Center** |  [API reference](https://designcenter.googleapis.com/$discovery/rest)

  * [ ` designcenter.googleapis.com/Application ` ](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications) Effective tags aren't supported. 
  * [ ` designcenter.googleapis.com/ApplicationTemplateRevision ` ](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.revisions) Effective tags aren't supported. 
  * [ ` designcenter.googleapis.com/Component ` ](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components) Effective tags aren't supported. 
  * [ ` designcenter.googleapis.com/Connection ` ](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components.connections) Effective tags aren't supported. 
  * [ ` designcenter.googleapis.com/SharedTemplate ` ](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.sharedTemplates) Effective tags aren't supported. 
  * [ ` designcenter.googleapis.com/SharedTemplateRevision ` ](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.sharedTemplates.revisions) Effective tags aren't supported. 

  
**App Engine** The `location` field might not be populated for App Engine assets. |  [API reference](https://appengine.googleapis.com/$discovery/rest?version=v1)

  * [ ` appengine.googleapis.com/Application ` ](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps) Searchable attributes:
    * ` defaultBucket `
    * ` defaultHostname `
  * [ ` appengine.googleapis.com/Service ` ](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services)
  * [ ` appengine.googleapis.com/Version ` ](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions) Searchable attributes:
    * ` versionUrl `

  
**App Hub** |  [API reference](https://apphub.googleapis.com/$discovery/rest?version=v1)

  * [ ` apphub.googleapis.com/Application ` ](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/projects.locations.applications) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` apphub.googleapis.com/Service ` ](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/projects.locations.applications.services) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` apphub.googleapis.com/ServiceProjectAttachment ` ](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/projects.locations.serviceProjectAttachments) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` apphub.googleapis.com/Workload ` ](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/projects.locations.applications.workloads) Effective tags aren't supported. Not available in the analysis APIs. 

  
**App Lifecycle Manager** |  [API reference](https://saasservicemgmt.googleapis.com/$discovery/rest?version=v1)

  * [ ` saasservicemgmt.googleapis.com/Release ` ](https://docs.cloud.google.com/saas-runtime/docs/reference/rest/v1/projects.locations.releases) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` saasservicemgmt.googleapis.com/Rollout ` ](https://docs.cloud.google.com/saas-runtime/docs/reference/rest/v1/projects.locations.rollouts) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` saasservicemgmt.googleapis.com/RolloutKind ` ](https://docs.cloud.google.com/saas-runtime/docs/reference/rest/v1/projects.locations.rolloutKinds) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` saasservicemgmt.googleapis.com/Saas ` ](https://docs.cloud.google.com/saas-runtime/docs/reference/rest/v1/projects.locations.saas) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` saasservicemgmt.googleapis.com/Tenant ` ](https://docs.cloud.google.com/saas-runtime/docs/reference/rest/v1/projects.locations.tenants) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` saasservicemgmt.googleapis.com/Unit ` ](https://docs.cloud.google.com/saas-runtime/docs/reference/rest/v1/projects.locations.units) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` saasservicemgmt.googleapis.com/UnitKind ` ](https://docs.cloud.google.com/saas-runtime/docs/reference/rest/v1/projects.locations.unitKinds) Effective tags aren't supported. Not available in the analysis APIs. 

  
**Application Integration** |  [API reference](https://integrations.googleapis.com/$discovery/rest?version=v1)

  * [ ` integrations.googleapis.com/AuthConfig ` ](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.authConfigs) Not available in the analysis APIs. 
  * [ ` integrations.googleapis.com/Certificate ` ](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.certificates) Not available in the analysis APIs. 
  * [ ` integrations.googleapis.com/Execution ` ](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.executions) Not available in the analysis APIs. 
  * [ ` integrations.googleapis.com/Integration ` ](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations) Not available in the analysis APIs. 
  * [ ` integrations.googleapis.com/IntegrationVersion ` ](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions) Not available in the analysis APIs. 
  * [ ` integrations.googleapis.com/SfdcChannel ` ](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.sfdcInstances.sfdcChannels) Not available in the analysis APIs. 
  * [ ` integrations.googleapis.com/SfdcInstance ` ](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.sfdcInstances) Not available in the analysis APIs. 
  * [ ` integrations.googleapis.com/Suspension ` ](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.executions.suspensions) Not available in the analysis APIs. 

  
**Artifact Registry** |  [API reference](https://artifactregistry.googleapis.com/$discovery/rest?version=v1)

  * [ ` artifactregistry.googleapis.com/DockerImage ` ](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.dockerImages)
  * [ ` artifactregistry.googleapis.com/MavenArtifact ` ](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.mavenArtifacts) Not available in the analysis APIs. 
  * [ ` artifactregistry.googleapis.com/NpmPackage ` ](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.npmPackages) Not available in the analysis APIs. 
  * [ ` artifactregistry.googleapis.com/PythonPackage ` ](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.pythonPackages) Not available in the analysis APIs. 
  * [ ` artifactregistry.googleapis.com/Repository ` ](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories)
  * [ ` artifactregistry.googleapis.com/Rule ` ](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.rules) Not available in the analysis APIs. 

  
**Assured Workloads** |  [API reference](https://assuredworkloads.googleapis.com/$discovery/rest?version=v1)

  * [ ` assuredworkloads.googleapis.com/Workload ` ](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads)

  
**Backup and DR Service** |  [API reference](https://backupdr.googleapis.com/$discovery/rest?version=v1)

  * [ ` backupdr.googleapis.com/Backup ` ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.backupVaults.dataSources.backups) Not available in the analysis APIs. 
  * [ ` backupdr.googleapis.com/BackupPlan ` ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.backupPlans) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` backupdr.googleapis.com/BackupPlanAssociation ` ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.backupPlanAssociations) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` backupdr.googleapis.com/BackupPlanRevision ` ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.backupPlans.revisions) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` backupdr.googleapis.com/BackupVault ` ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.backupVaults) Not available in the analysis APIs. 
  * [ ` backupdr.googleapis.com/DataSource ` ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.backupVaults.dataSources) Not available in the analysis APIs. 
  * [ ` backupdr.googleapis.com/DataSourceReference ` ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.dataSourceReferences) Not available in the analysis APIs. 
  * [ ` backupdr.googleapis.com/ManagementServer ` ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/projects.locations.managementServers) Effective tags aren't supported. 

  
**Backup for GKE** |  [API reference](https://gkebackup.googleapis.com/$discovery/rest?version=v1)

  * [ ` gkebackup.googleapis.com/Backup ` ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups)
  * [ ` gkebackup.googleapis.com/BackupPlan ` ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans)
  * [ ` gkebackup.googleapis.com/Restore ` ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores)
  * [ ` gkebackup.googleapis.com/RestorePlan ` ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans)
  * [ ` gkebackup.googleapis.com/VolumeBackup ` ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups)
  * [ ` gkebackup.googleapis.com/VolumeRestore ` ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores.volumeRestores)

  
**Batch** |  [API reference](https://batch.googleapis.com/$discovery/rest?version=v1)

  * [ ` batch.googleapis.com/Job ` ](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs) Not available in the analysis APIs. 

  
**BigQuery** |  [API reference](https://bigquery.googleapis.com/$discovery/rest?version=v2)

  * [ ` bigquery.googleapis.com/Dataset ` ](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets) Effective tags aren't supported. 
  * [ ` bigquery.googleapis.com/Model ` ](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/models) Effective tags aren't supported. 
  * [ ` bigquery.googleapis.com/Routine ` ](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines) Effective tags aren't supported. 
  * [ ` bigquery.googleapis.com/RowAccessPolicy ` ](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/rowAccessPolicies) Effective tags aren't supported. 
  * [ ` bigquery.googleapis.com/Table ` ](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables) Effective tags aren't supported. 

  
**BigQuery Data Transfer Service** BigQuery Data Transfer Service asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync. |  [API reference](https://bigquerydatatransfer.googleapis.com/$discovery/rest)

  * [ ` bigquerydatatransfer.googleapis.com/TransferConfig ` ](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs)

  
**BigQuery Migration Service** |  [API reference](https://bigquerymigration.googleapis.com/$discovery/rest)

  * [ ` bigquerymigration.googleapis.com/MigrationWorkflow ` ](https://docs.cloud.google.com/bigquery/docs/reference/migration/rest/v2/projects.locations.workflows)

  
**BigQuery Reservation API** |  [API reference](https://bigqueryreservation.googleapis.com/$discovery/rest)

  * [ ` bigqueryreservation.googleapis.com/BiReservation ` ](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest/v1/BiReservation) Not available in the analysis APIs. 
  * [ ` bigqueryreservation.googleapis.com/CapacityCommitment ` ](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations.capacityCommitments) Not available in the analysis APIs. 
  * [ ` bigqueryreservation.googleapis.com/Reservation ` ](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations.reservations) Not available in the analysis APIs. 
  * [ ` bigqueryreservation.googleapis.com/ReservationAssignment ` ](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations.reservations.assignments) Not available in the analysis APIs. 
  * [ ` bigqueryreservation.googleapis.com/ReservationGroup ` ](https://docs.cloud.google.com/bigquery/docs/reference/reservations/rest/v1/projects.locations.reservationGroups) Not available in the analysis APIs. 

  
**BigQuery sharing** |  [API reference](https://analyticshub.googleapis.com/$discovery/rest?version=v1)

  * [ ` analyticshub.googleapis.com/DataExchange ` ](https://docs.cloud.google.com/bigquery/docs/reference/analytics-hub/rest/v1/projects.locations.dataExchanges) Not available in the analysis APIs. 
  * [ ` analyticshub.googleapis.com/Listing ` ](https://docs.cloud.google.com/bigquery/docs/reference/analytics-hub/rest/v1/projects.locations.dataExchanges.listings) Not available in the analysis APIs. 

  
**Bigtable** |  [API reference](https://bigtableadmin.googleapis.com/$discovery/rest?version=v2)

  * [ ` bigtableadmin.googleapis.com/AppProfile ` ](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.appProfiles)
  * [ ` bigtableadmin.googleapis.com/AuthorizedView ` ](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables.authorizedViews) Not available in the analysis APIs. 
  * [ ` bigtableadmin.googleapis.com/Backup ` ](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups)
  * [ ` bigtableadmin.googleapis.com/Cluster ` ](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters)
  * [ ` bigtableadmin.googleapis.com/Instance ` ](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances)
  * [ ` bigtableadmin.googleapis.com/LogicalView ` ](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.logicalViews) Not available in the analysis APIs. 
  * [ ` bigtableadmin.googleapis.com/MaterializedView ` ](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.materializedViews) Not available in the analysis APIs. 
  * [ ` bigtableadmin.googleapis.com/SchemaBundle ` ](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables.schemaBundles) Not available in the analysis APIs. 
  * [ ` bigtableadmin.googleapis.com/Table ` ](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables)

  
**Binary Authorization** |  [API reference](https://binaryauthorization.googleapis.com/$discovery/rest)

  * [ ` binaryauthorization.googleapis.com/Attestor ` ](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.attestors) Not available in the analysis APIs. 
  * [ ` binaryauthorization.googleapis.com/PlatformPolicy ` ](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.policies) Not available in the analysis APIs. 
  * [ ` binaryauthorization.googleapis.com/Policy ` ](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.policy) Not available in the analysis APIs. 

  
**Blockchain Node Engine** |  [API reference](https://blockchainnodeengine.googleapis.com/$discovery/rest)

  * [ ` blockchainnodeengine.googleapis.com/BlockchainNode ` ](https://docs.cloud.google.com/blockchain-node-engine/docs/reference/rest/v1/projects.locations.blockchainNodes)

  
**Certificate Authority Service** |  [API reference](https://privateca.googleapis.com/$discovery/rest?version=v1)

  * [ ` privateca.googleapis.com/CaPool ` ](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools)
  * [ ` privateca.googleapis.com/Certificate ` ](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates)
  * [ ` privateca.googleapis.com/CertificateAuthority ` ](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificateAuthorities)
  * [ ` privateca.googleapis.com/CertificateRevocationList ` ](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificateAuthorities.certificateRevocationLists) IAM policies might be missing for this asset type.
  * [ ` privateca.googleapis.com/CertificateTemplate ` ](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.certificateTemplates)

  
**Certificate Manager** |  [API reference](https://certificatemanager.googleapis.com/$discovery/rest?version=v1)

  * [ ` certificatemanager.googleapis.com/Certificate ` ](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificates) Not available in the analysis APIs. 
  * [ ` certificatemanager.googleapis.com/CertificateIssuanceConfig ` ](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateIssuanceConfigs) Not available in the analysis APIs. 
  * [ ` certificatemanager.googleapis.com/CertificateMap ` ](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateMaps) Not available in the analysis APIs. 
  * [ ` certificatemanager.googleapis.com/CertificateMapEntry ` ](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.certificateMaps.certificateMapEntries) Not available in the analysis APIs. 
  * [ ` certificatemanager.googleapis.com/DnsAuthorization ` ](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.dnsAuthorizations) Not available in the analysis APIs. 
  * [ ` certificatemanager.googleapis.com/TrustConfig ` ](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rest/v1/projects.locations.trustConfigs) Not available in the analysis APIs. 

  
**Chrome Enterprise Premium** |  [API reference](https://beyondcorp.googleapis.com/$discovery/rest?version=v1)

  * [ ` beyondcorp.googleapis.com/AppConnection ` ](https://docs.cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.appConnections)
  * [ ` beyondcorp.googleapis.com/AppConnector ` ](https://docs.cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.appConnectors)
  * [ ` beyondcorp.googleapis.com/AppGateway ` ](https://docs.cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.appGateways)
  * [ ` beyondcorp.googleapis.com/ClientConnectorService ` ](https://docs.cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.clientConnectorServices)
  * [ ` beyondcorp.googleapis.com/ClientGateway ` ](https://docs.cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.clientGateways)

  
**Cloud Asset Inventory** |  [API reference](https://cloudasset.googleapis.com/$discovery/rest?version=v1)

  * [ ` cloudasset.googleapis.com/Feed ` ](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds) Effective tags aren't supported. Not available in the analysis APIs. 

  
**Cloud Billing** |  [API reference](https://cloudbilling.googleapis.com/$discovery/rest?version=v1)

  * [ ` cloudbilling.googleapis.com/BillingAccount ` ](https://docs.cloud.google.com/billing/docs/reference/rest/v1/billingAccounts)
  * [ ` cloudbilling.googleapis.com/ProjectBillingInfo ` ](https://docs.cloud.google.com/billing/docs/reference/rest/v1/ProjectBillingInfo) Not available in the analysis APIs. 

  
**Cloud Build** |  [API reference](https://cloudbuild.googleapis.com/$discovery/rest?version=v1)

  * [ ` cloudbuild.googleapis.com/BitbucketServerConfig ` ](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs) Not available in the analysis APIs. 
  * [ ` cloudbuild.googleapis.com/Build ` ](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds) Effective tags aren't supported. Not available in the analysis and search APIs. 
  * [ ` cloudbuild.googleapis.com/BuildTrigger ` ](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers) Not available in the analysis APIs. 
  * [ ` cloudbuild.googleapis.com/Connection ` ](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections) Not available in the analysis APIs. 
  * [ ` cloudbuild.googleapis.com/GithubEnterpriseConfig ` ](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.githubEnterpriseConfigs) Not available in the analysis APIs. 
  * ` cloudbuild.googleapis.com/GlobalTriggerSettings ` Not available in the analysis APIs. 
  * [ ` cloudbuild.googleapis.com/Repository ` ](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories) Not available in the analysis APIs. 
  * [ ` cloudbuild.googleapis.com/WorkerPool ` ](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools) Not available in the analysis APIs. 

  
**Cloud Config Manager API** |  [API reference](https://config.googleapis.com/$discovery/rest?version=v1)

  * [ ` config.googleapis.com/Deployment ` ](https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/projects.locations.deployments)
  * [ ` config.googleapis.com/Preview ` ](https://docs.cloud.google.com/infrastructure-manager/docs/reference/rest/v1/projects.locations.previews) Not available in the analysis APIs. 

  
**Cloud Controls Partner API** |  [API reference](https://cloudcontrolspartner.googleapis.com/$discovery/rest?version=v1)

  * [ ` cloudcontrolspartner.googleapis.com/Customer ` ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers)
  * [ ` cloudcontrolspartner.googleapis.com/Partner ` ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations)
  * [ ` cloudcontrolspartner.googleapis.com/Workload ` ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/sovereign-partners/reference/rest/v1/organizations.locations.customers.workloads)

  
**Cloud Data Fusion** |  [API reference](https://datafusion.googleapis.com/$discovery/rest)

  * [ ` datafusion.googleapis.com/DnsPeering ` ](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings)
  * [ ` datafusion.googleapis.com/Instance ` ](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances)

  
**Cloud Deploy** |  [API reference](https://clouddeploy.googleapis.com/$discovery/rest?version=v1)

  * [ ` clouddeploy.googleapis.com/Automation ` ](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations)
  * [ ` clouddeploy.googleapis.com/AutomationRun ` ](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns)
  * [ ` clouddeploy.googleapis.com/CustomTargetType ` ](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes)
  * [ ` clouddeploy.googleapis.com/DeliveryPipeline ` ](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines)
  * [ ` clouddeploy.googleapis.com/DeployPolicy ` ](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies)
  * [ ` clouddeploy.googleapis.com/JobRun ` ](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns)
  * [ ` clouddeploy.googleapis.com/Release ` ](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases)
  * [ ` clouddeploy.googleapis.com/Rollout ` ](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts)
  * [ ` clouddeploy.googleapis.com/Target ` ](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets)

  
**Cloud DNS** |  [API reference](https://dns.googleapis.com/$discovery/rest?version=v1)

  * [ ` dns.googleapis.com/ManagedZone ` ](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones) Searchable attributes:
    * ` dnsName `
    * ` peeringConfig.targetNetwork.networkUrl `
  * [ ` dns.googleapis.com/Policy ` ](https://docs.cloud.google.com/dns/docs/reference/v1/policies)
  * [ ` dns.googleapis.com/ResourceRecordSet ` ](https://docs.cloud.google.com/dns/docs/reference/v1/resourceRecordSets) Not available in the analysis APIs. 
  * [ ` dns.googleapis.com/ResponsePolicy ` ](https://docs.cloud.google.com/dns/docs/reference/v1/responsePolicies) Not available in the analysis APIs. 
  * [ ` dns.googleapis.com/ResponsePolicyRule ` ](https://docs.cloud.google.com/dns/docs/reference/v1/responsePolicyRules) Not available in the analysis APIs. 

  
**Cloud Domains** |  [API reference](https://domains.googleapis.com/$discovery/rest?version=v1)

  * [ ` domains.googleapis.com/Registration ` ](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations)

  
**Cloud Healthcare API** Cloud Healthcare API asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync. |  [API reference](https://healthcare.googleapis.com/$discovery/rest)

  * [ ` healthcare.googleapis.com/ConsentStore ` ](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores)
  * [ ` healthcare.googleapis.com/Dataset ` ](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets)
  * [ ` healthcare.googleapis.com/DicomStore ` ](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores)
  * [ ` healthcare.googleapis.com/FhirStore ` ](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores)
  * [ ` healthcare.googleapis.com/Hl7V2Store ` ](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores)

  
**Cloud Intrusion Detection System** |  [API reference](https://ids.googleapis.com/$discovery/rest?version=v1)

  * [ ` ids.googleapis.com/Endpoint ` ](https://docs.cloud.google.com/intrusion-detection-system/docs/configuring-ids#create_a_endpoint)

  
**Cloud Key Management Service** |  [API reference](https://cloudkms.googleapis.com/$discovery/rest?version=v1)

  * [ ` cloudkms.googleapis.com/AutokeyConfig ` ](https://docs.cloud.google.com/kms/docs/reference/rest/v1/AutokeyConfig)
  * [ ` cloudkms.googleapis.com/CryptoKey ` ](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys)
  * [ ` cloudkms.googleapis.com/CryptoKeyVersion ` ](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions)
  * [ ` cloudkms.googleapis.com/EkmConfig ` ](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConfig)
  * [ ` cloudkms.googleapis.com/EkmConnection ` ](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.ekmConnections)
  * [ ` cloudkms.googleapis.com/ImportJob ` ](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs)
  * [ ` cloudkms.googleapis.com/KeyHandle ` ](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyHandles)
  * [ ` cloudkms.googleapis.com/KeyRing ` ](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings)
  * [ ` cloudkms.googleapis.com/RetiredResource ` ](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.retiredResources) Not available in the analysis APIs. 

  
**Cloud Load Balancing** |  [API reference](https://networksecurity.googleapis.com/$discovery/rest?version=v1)

  * [ ` networksecurity.googleapis.com/AuthzPolicy ` ](https://docs.cloud.google.com/load-balancing/docs/reference/network-security/rest/v1/projects.locations.authzPolicies) Not available in the analysis APIs. 

  
**Cloud Logging** Cloud Logging asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync. |  [API reference](https://logging.googleapis.com/$discovery/rest?version=v2)

  * [ ` logging.googleapis.com/Link ` ](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets.links) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` logging.googleapis.com/LogBucket ` ](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets)
  * [ ` logging.googleapis.com/LogMetric ` ](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics)
  * [ ` logging.googleapis.com/LogSink ` ](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.sinks)
  * [ ` logging.googleapis.com/LogView ` ](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets.views) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` logging.googleapis.com/RecentQuery ` ](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.recentQueries) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` logging.googleapis.com/SavedQuery ` ](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` logging.googleapis.com/Settings ` ](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/Settings) Effective tags aren't supported. Not available in the analysis APIs.  The resource is served only when the Logging update API is called.

  
**Cloud Monitoring** |  [API reference](https://monitoring.googleapis.com/$discovery/rest?version=v3)

  * [ ` monitoring.googleapis.com/AlertPolicy ` ](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies)
  * [ ` monitoring.googleapis.com/Dashboard ` ](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards) Not available in the analysis APIs. 
  * [ ` monitoring.googleapis.com/NotificationChannel ` ](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels)
  * [ ` monitoring.googleapis.com/Snooze ` ](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes)
  * [ ` monitoring.googleapis.com/UptimeCheckConfig ` ](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs) Not available in the analysis APIs. 

  
**Cloud Next Generation Firewall Enterprise** Cloud Next Generation Firewall Enterprise asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync. |  [API reference](https://networksecurity.googleapis.com/$discovery/rest?version=v1)

  * [ ` networksecurity.googleapis.com/AddressGroup ` ](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/projects.locations.tlsInspectionPolicies)
  * [ ` networksecurity.googleapis.com/FirewallEndpoint ` ](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.firewallEndpoints) Not available in the analysis APIs. 
  * [ ` networksecurity.googleapis.com/FirewallEndpointAssociation ` ](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/projects.locations.firewallEndpointAssociations) Not available in the analysis APIs. 
  * [ ` networksecurity.googleapis.com/SecurityProfile ` ](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.securityProfiles) Not available in the analysis APIs. 
  * [ ` networksecurity.googleapis.com/SecurityProfileGroup ` ](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/organizations.locations.securityProfileGroups) Not available in the analysis APIs. 
  * [ ` networksecurity.googleapis.com/TlsInspectionPolicy ` ](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest/v1/projects.locations.tlsInspectionPolicies) Not available in the analysis APIs. 

  
**Cloud OS Config** Cloud OS Config asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync. |  [API reference](https://osconfig.googleapis.com/$discovery/rest?version=v1)

  * [ ` osconfig.googleapis.com/OSPolicyAssignment ` ](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments) Effective tags aren't supported. 
  * [ ` osconfig.googleapis.com/OSPolicyAssignmentReport ` ](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.instances.osPolicyAssignments.reports) Effective tags aren't supported. 
  * [ ` osconfig.googleapis.com/PatchDeployment ` ](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments) Effective tags aren't supported. 
  * [ ` osconfig.googleapis.com/VulnerabilityReport ` ](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.instances.vulnerabilityReports) Effective tags aren't supported. Not available in the analysis APIs. 

  
**Cloud Quotas** |  [API reference](https://cloudquotas.googleapis.com/$discovery/rest?version=v1)

  * [ ` cloudquotas.googleapis.com/QuotaPreference ` ](https://docs.cloud.google.com/docs/quotas/reference/rest/v1/projects.locations.quotaPreferences) Effective tags aren't supported. Not available in the analysis APIs. 

  
**Cloud Run** |  [API reference](https://run.googleapis.com/$discovery/rest?version=v1)

  * [ ` run.googleapis.com/DomainMapping ` ](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.domainmappings) Not available in the analysis APIs. 
  * [ ` run.googleapis.com/Execution ` ](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.executions) Effective tags aren't supported. 
  * [ ` run.googleapis.com/Job ` ](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs)
  * [ ` run.googleapis.com/Revision ` ](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.revisions) Effective tags aren't supported. 
  * [ ` run.googleapis.com/Service ` ](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.services)
  * [ ` run.googleapis.com/WorkerPool ` ](https://docs.cloud.google.com/run/docs/reference/rest/v1/projects.locations.workerpools) Not available in the analysis APIs. 

  
**Cloud Run functions (1st and 2nd gen)** This includes both [1st and 2nd gen](https://docs.cloud.google.com/functions/docs/concepts/version-comparison) Cloud Run functions. The asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync.  |  [API reference](https://cloudfunctions.googleapis.com/$discovery/rest)

  * [ ` cloudfunctions.googleapis.com/Function ` ](https://docs.cloud.google.com/functions/docs/reference/rest/v2/projects.locations.functions) Searchable attributes:
    * ` environment `

  
**Cloud Run functions (1st gen)** This only includes [1st gen](https://docs.cloud.google.com/functions/docs/concepts/version-comparison) Cloud Run functions. The asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync. |  [API reference](https://cloudfunctions.googleapis.com/$discovery/rest)

  * [ ` cloudfunctions.googleapis.com/CloudFunction ` ](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions)

  
**Cloud Service Mesh** |  [API reference](https://networksecurity.googleapis.com/$discovery/rest?version=v1)

  * [ ` networksecurity.googleapis.com/AuthorizationPolicy ` ](https://docs.cloud.google.com/service-mesh/docs/reference/network-security/rest/v1/projects.locations.authorizationPolicies) Not available in the analysis APIs. 
  * [ ` networksecurity.googleapis.com/ClientTlsPolicy ` ](https://docs.cloud.google.com/service-mesh/docs/reference/network-security/rest/v1/projects.locations.clientTlsPolicies) Not available in the analysis APIs. 
  * [ ` networksecurity.googleapis.com/ServerTlsPolicy ` ](https://docs.cloud.google.com/service-mesh/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies) Not available in the analysis APIs. 

  
**Cloud SQL** Cloud SQL asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync. |  [API reference](https://sqladmin.googleapis.com/$discovery/rest?version=v1beta4)

  * [ ` sqladmin.googleapis.com/Backup ` ](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backupRuns) Not available in the analysis APIs. 
  * [ ` sqladmin.googleapis.com/BackupRun ` ](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backupRuns)
  * [ ` sqladmin.googleapis.com/Instance ` ](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances)

  
**Cloud Storage** |  [API reference](https://storage.googleapis.com/$discovery/rest?version=v1)

  * [ ` storage.googleapis.com/Bucket ` ](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets)

  
**Cloud Tasks** |  [API reference](https://cloudtasks.googleapis.com/$discovery/rest?version=v2)

  * [ ` cloudtasks.googleapis.com/Queue ` ](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues)

  
**Cloud TPU** |  [API reference](https://tpu.googleapis.com/$discovery/rest?version=v1)

  * [ ` tpu.googleapis.com/Node ` ](https://docs.cloud.google.com/tpu/docs/reference/rest/v1/projects.locations.nodes)
  * [ ` tpu.googleapis.com/QueuedResource ` ](https://docs.cloud.google.com/tpu/docs/reference/rest/v2/projects.locations.queuedResources) Effective tags aren't supported. Not available in the analysis and search APIs. 

  
**Cloud Workstations** |  [API reference](https://workstations.googleapis.com/$discovery/rest?version=v1)

  * [ ` workstations.googleapis.com/Workstation ` ](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters.workstationConfigs.workstations) Not available in the analysis APIs. 
  * [ ` workstations.googleapis.com/WorkstationCluster ` ](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters) Not available in the analysis APIs. 
  * [ ` workstations.googleapis.com/WorkstationConfig ` ](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters.workstationConfigs) Not available in the analysis APIs. 

  
**Cluster Director** Previously known as Hypercompute Cluster |  [API reference](https://hypercomputecluster.googleapis.com/$discovery/rest?version=v1)

  * [ ` hypercomputecluster.googleapis.com/Cluster ` ](https://docs.cloud.google.com/cluster-director/docs/reference/rest) Not available in the analysis APIs. 

  
**Compute Engine** |  [API reference](https://www.googleapis.com/discovery/v1/apis/compute/v1/rest?version=v1)

  * [ ` compute.googleapis.com/Address ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses) Returns global and regional addresses in the search and analysis APIs, and only regional addresses in the list, export, query, and monitor APIs.
  * [ ` compute.googleapis.com/Autoscaler ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers)
  * [ ` compute.googleapis.com/BackendBucket ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets)
  * [ ` compute.googleapis.com/BackendService ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices) Returns global and regional backend services in the search and analysis APIs, and only regional backend services in the list, export, query, and monitor APIs.
  * [ ` compute.googleapis.com/Commitment ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments)
  * [ ` compute.googleapis.com/CrossSiteNetwork ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/crossSiteNetworks)
  * [ ` compute.googleapis.com/Disk ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks) Returns zonal and regional disks in the search and analysis APIs, and only zonal disks in the list, export, query, and monitor APIs.
  * [ ` compute.googleapis.com/ExternalVpnGateway ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/externalVpnGateways)
  * [ ` compute.googleapis.com/Firewall ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls)
  * [ ` compute.googleapis.com/FirewallPolicy ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies) Not available in the analysis APIs. 
  * [ ` compute.googleapis.com/ForwardingRule ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules) Returns global and regional forwarding rules in the search and analysis APIs, and only regional forwarding rules in the list, export, query, and monitor APIs.
  * [ ` compute.googleapis.com/GlobalAddress ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalAddresses) Not available in the analysis and search APIs.  Use `compute.googleapis.com/Address` instead in the search and analysis APIs.
  * [ ` compute.googleapis.com/GlobalForwardingRule ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalForwardingRules) Not available in the analysis and search APIs.  Use `compute.googleapis.com/ForwardingRule` instead in the search and analysis APIs.
  * [ ` compute.googleapis.com/HealthCheck ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks)
  * [ ` compute.googleapis.com/HttpHealthCheck ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpHealthChecks)
  * [ ` compute.googleapis.com/HttpsHealthCheck ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/httpsHealthChecks)
  * [ ` compute.googleapis.com/Image ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images)
  * [ ` compute.googleapis.com/Instance ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances) Searchable attributes:
    * ` deletionProtection `
    * ` externalIPs `
    * ` internalIPs `
    * ` machineType `
    * ` networkInterfaceNetworks `
    * ` networkInterfaceNames `
The following attributes are from the [ OS Inventory](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management), which is attached on this Compute Engine Instance to provide information on operating system and packages. Learn more about [ OS inventory management](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management). 
    * ` osLongName `
    * ` osShortName `
Supported [metadata](https://docs.cloud.google.com/compute/docs/metadata/overview) fields:
    * ` block-project-ssh-keys `
    * ` enable-oslogin `
    * ` enable-osconfig `
    * ` serial-port-enable `
  * [ ` compute.googleapis.com/InstanceGroup ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups)
  * [ ` compute.googleapis.com/InstanceGroupManager ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers)
  * [ ` compute.googleapis.com/InstanceSettings ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceSettings) Not available in the analysis APIs. 
  * [ ` compute.googleapis.com/InstanceTemplate ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates)
  * [ ` compute.googleapis.com/InstantSnapshot ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instantSnapshots)
  * [ ` compute.googleapis.com/Interconnect ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnects)
  * [ ` compute.googleapis.com/InterconnectAttachment ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments)
  * [ ` compute.googleapis.com/License ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/licenses)
  * [ ` compute.googleapis.com/MachineImage ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/machineImages)
  * [ ` compute.googleapis.com/Network ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks) Searchable attributes:
    * ` gatewayIPv4 `
  * [ ` compute.googleapis.com/NetworkAttachment ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkAttachments) Searchable attributes:
    * ` connectionEndpointsIpAddresses `
    * ` connectionEndpointsIpv6Addresses `
  * [ ` compute.googleapis.com/NetworkEdgeSecurityService ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkEdgeSecurityServices)
  * [ ` compute.googleapis.com/NetworkEndpointGroup ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkEndpointGroups)
  * [ ` compute.googleapis.com/NodeGroup ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups)
  * [ ` compute.googleapis.com/NodeTemplate ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeTemplates)
  * [ ` compute.googleapis.com/PacketMirroring ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/packetMirrorings)
  * [ ` compute.googleapis.com/Project ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects) Supported [metadata](https://docs.cloud.google.com/compute/docs/metadata/overview) fields:
    * ` block-project-ssh-keys `
    * ` enable-osconfig `
    * ` enable-oslogin `
    * ` serial-port-enable `
  * [ ` compute.googleapis.com/PublicAdvertisedPrefix ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/publicAdvertisedPrefixes) Not available in the analysis APIs. 
  * [ ` compute.googleapis.com/PublicDelegatedPrefix ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/publicDelegatedPrefixes)
  * [ ` compute.googleapis.com/RegionBackendService ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices) Not available in the analysis and search APIs.  Use `compute.googleapis.com/BackendService` instead in the search and analysis APIs.
  * [ ` compute.googleapis.com/RegionDisk ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks) Not available in the analysis and search APIs.  Use `compute.googleapis.com/Disk` instead in the search and analysis APIs.
  * [ ` compute.googleapis.com/Reservation ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations)
  * [ ` compute.googleapis.com/ResourcePolicy ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies)
  * [ ` compute.googleapis.com/Route ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes)
  * [ ` compute.googleapis.com/Router ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers)
  * [ ` compute.googleapis.com/SecurityPolicy ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/securityPolicies)
  * [ ` compute.googleapis.com/ServiceAttachment ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments)
  * [ ` compute.googleapis.com/Snapshot ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots)
  * [ ` compute.googleapis.com/SslCertificate ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/sslCertificates)
  * [ ` compute.googleapis.com/SslPolicy ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/sslPolicies)
  * [ ` compute.googleapis.com/StoragePool ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/storagePools)
  * [ ` compute.googleapis.com/Subnetwork ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks) Searchable attributes:
    * ` gatewayAddress `
  * [ ` compute.googleapis.com/TargetGrpcProxy ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetGrpcProxies)
  * [ ` compute.googleapis.com/TargetHttpProxy ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpProxies)
  * [ ` compute.googleapis.com/TargetHttpsProxy ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetHttpsProxies)
  * [ ` compute.googleapis.com/TargetInstance ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetInstances)
  * [ ` compute.googleapis.com/TargetPool ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetPools)
  * [ ` compute.googleapis.com/TargetSslProxy ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetSslProxies)
  * [ ` compute.googleapis.com/TargetTcpProxy ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetTcpProxies)
  * [ ` compute.googleapis.com/TargetVpnGateway ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways)
  * [ ` compute.googleapis.com/UrlMap ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps)
  * [ ` compute.googleapis.com/VpnGateway ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnGateways)
  * [ ` compute.googleapis.com/VpnTunnel ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels)
  * [ ` compute.googleapis.com/WireGroup ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/wireGroups)

  
**Container Registry** Container Registry implements [ Docker HTTP API V2 ](https://docs.docker.com/registry/spec/api/) and does not provide a public API.  | 

  * ` containerregistry.googleapis.com/Image ` Effective tags aren't supported. Not available in the analysis APIs. 

  
**Customer Experience Insights** |  [API reference](https://contactcenterinsights.googleapis.com/$discovery/rest)

  * [ ` contactcenterinsights.googleapis.com/EncryptionSpec ` ](https://docs.cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations.encryptionSpec)
  * [ ` contactcenterinsights.googleapis.com/IssueModel ` ](https://docs.cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations.issueModels)
  * [ ` contactcenterinsights.googleapis.com/PhraseMatcher ` ](https://docs.cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations.phraseMatchers)
  * [ ` contactcenterinsights.googleapis.com/View ` ](https://docs.cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations.views)

  
**Data Lineage** |  [API reference](https://datalineage.googleapis.com/$discovery/rest?version=v1)

  * [ ` datalineage.googleapis.com/Process ` ](https://docs.cloud.google.com/data-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes)

  
**Database Migration Service** |  [API reference](https://datamigration.googleapis.com/$discovery/rest?version=v1)

  * [ ` datamigration.googleapis.com/ConnectionProfile ` ](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles)
  * [ ` datamigration.googleapis.com/ConversionWorkspace ` ](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces)
  * [ ` datamigration.googleapis.com/MigrationJob ` ](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs)
  * [ ` datamigration.googleapis.com/PrivateConnection ` ](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections)

  
**Dataflow** Dataflow asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync. |  [API reference](https://dataflow.googleapis.com/$discovery/rest?version=v1b3)

  * [ ` dataflow.googleapis.com/Job ` ](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs)

  
**Dataform** |  [API reference](https://dataform.googleapis.com/$discovery/rest?version=v1beta1)

  * [ ` dataform.googleapis.com/CompilationResult ` ](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults)
  * [ ` dataform.googleapis.com/Folder ` ](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders) Not available in the analysis APIs. 
  * [ ` dataform.googleapis.com/ReleaseConfig ` ](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.releaseConfigs)
  * [ ` dataform.googleapis.com/Repository ` ](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories)
  * [ ` dataform.googleapis.com/TeamFolder ` ](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders) Not available in the analysis APIs. 
  * [ ` dataform.googleapis.com/WorkflowConfig ` ](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowConfigs)
  * [ ` dataform.googleapis.com/WorkflowInvocation ` ](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workflowInvocations)
  * [ ` dataform.googleapis.com/Workspace ` ](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.workspaces)

  
**Dataproc Metastore** |  [API reference](https://metastore.googleapis.com/$discovery/rest?version=v1)

  * [ ` metastore.googleapis.com/Backup ` ](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services.backups) Not available in the analysis APIs. 
  * [ ` metastore.googleapis.com/Federation ` ](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.federations) Not available in the analysis APIs. 
  * [ ` metastore.googleapis.com/MetadataImport ` ](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services.metadataImports) Not available in the analysis APIs. 
  * [ ` metastore.googleapis.com/Service ` ](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services) Not available in the analysis APIs. 

  
**Datastream** |  [API reference](https://datastream.googleapis.com/$discovery/rest)

  * [ ` datastream.googleapis.com/ConnectionProfile ` ](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles)
  * [ ` datastream.googleapis.com/PrivateConnection ` ](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.privateConnections)
  * [ ` datastream.googleapis.com/Stream ` ](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams)

  
**Developer Connect** |  [API reference](https://developerconnect.googleapis.com/$discovery/rest?version=v1)

  * [ ` developerconnect.googleapis.com/Connection ` ](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest#rest-resource:-v1.projects.locations.connections) Effective tags aren't supported. 
  * [ ` developerconnect.googleapis.com/GitRepositoryLink ` ](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest#rest-resource:-v1.projects.locations.connections.gitrepositorylinks) Effective tags aren't supported. 
  * [ ` developerconnect.googleapis.com/InsightsConfig ` ](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest#rest-resource:-v1.projects.locations.insightsconfigs)

  
**Dialogflow CX** |  [API reference](https://dialogflow.googleapis.com/$discovery/rest?version=v3)

  * [ ` dialogflow.googleapis.com/Agent ` ](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents)
  * ` dialogflow.googleapis.com/LocationSettings `

  
**Dialogflow ES** |  [API reference](https://dialogflow.googleapis.com/$discovery/rest?version=v2)

  * [ ` dialogflow.googleapis.com/ConversationProfile ` ](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles)
  * [ ` dialogflow.googleapis.com/KnowledgeBase ` ](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.knowledgeBases)

  
**Discovery Engine** |  [API reference](https://discoveryengine.googleapis.com/$discovery/rest?version=v1)

  * [ ` discoveryengine.googleapis.com/Assistant ` ](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.assistants) Not available in the analysis APIs. 
  * [ ` discoveryengine.googleapis.com/Collection ` ](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections)
  * [ ` discoveryengine.googleapis.com/DataStore ` ](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores)
  * [ ` discoveryengine.googleapis.com/Engine ` ](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines)
  * ` discoveryengine.googleapis.com/Notebook ` Not available in the analysis APIs. 

  
**DNS Armor** |  [API reference](https://networksecurity.googleapis.com/$discovery/rest?version=v1)

  * [ ` networksecurity.googleapis.com/DnsThreatDetector ` ](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1/projects.locations.dnsThreatDetectors) Not available in the analysis APIs. 

  
**Document AI** |  [API reference](https://documentai.googleapis.com/$discovery/rest?version=v1)

  * [ ` documentai.googleapis.com/HumanReviewConfig ` ](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors.humanReviewConfig)
  * ` documentai.googleapis.com/LabelerPool `
  * [ ` documentai.googleapis.com/Processor ` ](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors)
  * ` documentai.googleapis.com/ProcessorVersion `

  
**Essential Contacts** |  [API reference](https://essentialcontacts.googleapis.com/$discovery/rest?version=v1)

  * [ ` essentialcontacts.googleapis.com/Contact ` ](https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest/v1/projects.contacts) Not available in the analysis APIs. 

  
**Eventarc** |  [API reference](https://eventarc.googleapis.com/$discovery/rest?version=v1)

  * [ ` eventarc.googleapis.com/Channel ` ](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.channels) Not available in the analysis APIs. 
  * [ ` eventarc.googleapis.com/ChannelConnection ` ](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.channelConnections) Not available in the analysis APIs. 
  * [ ` eventarc.googleapis.com/Enrollment ` ](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.enrollments) Not available in the analysis APIs. 
  * [ ` eventarc.googleapis.com/GoogleApiSource ` ](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.googleApiSources) Not available in the analysis APIs. 
  * [ ` eventarc.googleapis.com/GoogleChannelConfig ` ](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/GoogleChannelConfig) Not available in the analysis APIs. 
  * [ ` eventarc.googleapis.com/MessageBus ` ](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.messageBuses) Not available in the analysis APIs. 
  * [ ` eventarc.googleapis.com/Pipeline ` ](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.pipelines) Not available in the analysis APIs. 
  * [ ` eventarc.googleapis.com/Trigger ` ](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.triggers)

  
**Fault Injection Testing** | 

  * [ ` faulttesting.googleapis.com/Experiment ` ](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments) Not available in the analysis APIs. 
  * [ ` faulttesting.googleapis.com/ExperimentTemplate ` ](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experimentTemplates) Not available in the analysis APIs. 
  * [ ` faulttesting.googleapis.com/Validation ` ](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations) Not available in the analysis APIs. 

  
**Filestore** |  [API reference](https://file.googleapis.com/$discovery/rest?version=v1)

  * [ ` file.googleapis.com/Backup ` ](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.backups) In beta for the export, list, and monitor APIs.
  * [ ` file.googleapis.com/Instance ` ](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances)
  * [ ` file.googleapis.com/Snapshot ` ](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots) Not available in the analysis APIs. 

  
**Financial Services** |  [API reference](https://financialservices.googleapis.com/$discovery/rest?version=v1)

  * ` financialservices.googleapis.com/BacktestResult ` Not available in the analysis APIs. 
  * ` financialservices.googleapis.com/Dataset ` Not available in the analysis APIs. 
  * ` financialservices.googleapis.com/EngineConfig ` Not available in the analysis APIs. 
  * ` financialservices.googleapis.com/Instance `
  * ` financialservices.googleapis.com/Model ` Not available in the analysis APIs. 
  * ` financialservices.googleapis.com/PredictionResult ` Not available in the analysis APIs. 

  
**Firebase** | 

  * [ ` firebase.googleapis.com/FirebaseAppInfo ` ](https://firebase.google.com/docs/projects/api/reference/rest)
  * [ ` firebase.googleapis.com/FirebaseProject ` ](https://firebase.google.com/docs/projects/api/reference/rest)
  * [ ` firebaserules.googleapis.com/Release ` ](https://firebase.google.com/docs/reference/rules/rest/v1/projects.releases) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` firebaserules.googleapis.com/Ruleset ` ](https://firebase.google.com/docs/reference/rules/rest/v1/projects.rulesets) Not available in the analysis APIs. 

  
**Firebase Data Connect** |  [API reference](https://firebasedataconnect.googleapis.com/$discovery/rest?version=v1)

  * [ ` firebasedataconnect.googleapis.com/Connector ` ](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.connectors)
  * [ ` firebasedataconnect.googleapis.com/Schema ` ](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services.schemas)
  * [ ` firebasedataconnect.googleapis.com/Service ` ](https://firebase.google.com/docs/reference/data-connect/rest/v1beta/projects.locations.services)

  
**Firebase Storage** | 

  * ` firebasestorage.googleapis.com/Bucket ` Not available in the analysis APIs. 
  * ` firebasestorage.googleapis.com/DefaultBucket ` Not available in the analysis APIs. 

  
**Firestore** |  [API reference](https://firestore.googleapis.com/$discovery/rest?version=v1)

  * [ ` firestore.googleapis.com/Backup ` ](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.locations.backups) Not available in the analysis APIs. 
  * [ ` firestore.googleapis.com/Database ` ](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases)

  
**Gemini for Google Cloud API** |  [API reference](https://cloud.google.com/gemini/docs/api/reference/rest)

  * [ ` cloudaicompanion.googleapis.com/CodeRepositoryIndex ` ](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes)
  * [ ` cloudaicompanion.googleapis.com/RepositoryGroup ` ](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeRepositoryIndexes.repositoryGroups)

  
**GKE Multi-Cloud** |  [API reference](https://us-west1-gkemulticloud.googleapis.com/$discovery/rest?version=v1)

  * [ ` gkemulticloud.googleapis.com/AttachedCluster ` ](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/reference/rest)
  * [ ` gkemulticloud.googleapis.com/AwsCluster ` ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.awsClusters)
  * [ ` gkemulticloud.googleapis.com/AwsNodePool ` ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.awsClusters.awsNodePools)
  * [ ` gkemulticloud.googleapis.com/AzureClient ` ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.azureClients)
  * [ ` gkemulticloud.googleapis.com/AzureCluster ` ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.azureClusters)
  * [ ` gkemulticloud.googleapis.com/AzureNodePool ` ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations.azureClusters.azureNodePools)

  
**GKE on GDC** GKE on GDC metadata has no public API source. | 

  * [ ` anthos.googleapis.com/ConnectedCluster ` ](https://docs.cloud.google.com/anthos/multicluster-management/reference/rest/v1/projects.locations.memberships) Effective tags aren't supported. Not available in the analysis APIs.  In beta for the export, list, and monitor APIs.

  
**GKE On-Prem API** |  [API reference](https://gkeonprem.googleapis.com/$discovery/rest?version=v1)

  * [ ` gkeonprem.googleapis.com/BareMetalAdminCluster ` ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters) Not available in the analysis APIs. 
  * [ ` gkeonprem.googleapis.com/BareMetalCluster ` ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters)
  * [ ` gkeonprem.googleapis.com/BareMetalNodePool ` ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools)
  * [ ` gkeonprem.googleapis.com/VmwareAdminCluster ` ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters) Not available in the analysis APIs. 
  * [ ` gkeonprem.googleapis.com/VmwareCluster ` ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters)
  * [ ` gkeonprem.googleapis.com/VmwareNodePool ` ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools)

  
**Google Cloud Managed Lustre** |  [API reference](https://lustre.googleapis.com/$discovery/rest?version=v1)

  * [ ` lustre.googleapis.com/Instance ` ](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances) Not available in the analysis APIs. 

  
**Google Cloud Managed Service for Apache Kafka** |  [API reference](https://managedkafka.googleapis.com/$discovery/rest?version=v1)

  * [ ` managedkafka.googleapis.com/Cluster ` ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.clusters) Not available in the analysis APIs. 
  * [ ` managedkafka.googleapis.com/ConnectCluster ` ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/reference/rest/v1/projects.locations.connectClusters) Not available in the analysis and search APIs. 

  
**Google Cloud Migration Center** |  [API reference](https://migrationcenter.googleapis.com/$discovery/rest?version=v1)

  * [ ` migrationcenter.googleapis.com/Asset ` ](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets) Not available in the analysis APIs. 
  * ` migrationcenter.googleapis.com/CostAssessmentJob ` Not available in the analysis APIs. 

  
**Google Cloud NetApp Volumes** |  [API reference](https://netapp.googleapis.com/$discovery/rest?version=v1)

  * [ ` netapp.googleapis.com/ActiveDirectory ` ](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.activeDirectories) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` netapp.googleapis.com/Backup ` ](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.backupVaults.backups) Effective tags aren't supported. 
  * [ ` netapp.googleapis.com/BackupPolicy ` ](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.backupPolicies) Effective tags aren't supported. 
  * [ ` netapp.googleapis.com/BackupVault ` ](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.backupVaults) Effective tags aren't supported. 
  * [ ` netapp.googleapis.com/KmsConfig ` ](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.kmsConfigs) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` netapp.googleapis.com/Replication ` ](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` netapp.googleapis.com/Snapshot ` ](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.snapshots) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` netapp.googleapis.com/StoragePool ` ](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.storagePools) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` netapp.googleapis.com/Volume ` ](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes) Effective tags aren't supported. Not available in the analysis APIs. 

  
**Google Cloud VMware Engine** |  [API reference](https://docs.cloud.google.com/vmware-engine/docs/reference/rest)

  * [ ` vmwareengine.googleapis.com/Cluster ` ](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.clusters)
  * [ ` vmwareengine.googleapis.com/ExternalAccessRule ` ](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules)
  * [ ` vmwareengine.googleapis.com/ExternalAddress ` ](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.externalAddresses)
  * [ ` vmwareengine.googleapis.com/NetworkPeering ` ](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.networkPeerings)
  * [ ` vmwareengine.googleapis.com/NetworkPolicy ` ](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.networkPolicies)
  * [ ` vmwareengine.googleapis.com/PrivateCloud ` ](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds)
  * [ ` vmwareengine.googleapis.com/PrivateConnection ` ](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateConnections)
  * [ ` vmwareengine.googleapis.com/VmwareEngineNetwork ` ](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.vmwareEngineNetworks)

  
**Google Kubernetes Engine** |  [API reference](https://container.googleapis.com/$discovery/rest?version=v1)

  * [ ` admissionregistration.k8s.io/MutatingWebhookConfiguration ` ](https://kubernetes.io/docs/reference/kubernetes-api/extend-resources/mutating-webhook-configuration-v1/)
  * [ ` admissionregistration.k8s.io/ValidatingWebhookConfiguration ` ](https://kubernetes.io/docs/reference/kubernetes-api/extend-resources/validating-webhook-configuration-v1/)
  * [ ` apps.k8s.io/DaemonSet ` ](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)
  * [ ` apps.k8s.io/Deployment ` ](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/deployment-v1/)
  * [ ` apps.k8s.io/ReplicaSet ` ](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/replica-set-v1/)
  * [ ` apps.k8s.io/StatefulSet ` ](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
  * [ ` autoscaling.k8s.io/HorizontalPodAutoscaler ` ](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/) Not available in the analysis APIs.  The asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync.
  * [ ` batch.k8s.io/CronJob ` ](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)
  * [ ` batch.k8s.io/Job ` ](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/job-v1/)
  * [ ` container.googleapis.com/Cluster ` ](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters) Searchable attributes:
    * ` endpoint `
  * [ ` container.googleapis.com/NodePool ` ](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools) Searchable attributes:
    * ` locations `
  * [ ` extensions.k8s.io/DaemonSet ` ](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) Not available in the analysis APIs. 
  * ` extensions.k8s.io/Ingress ` Not available in the analysis APIs.  In beta for the export, list, and monitor APIs.
  * [ ` gateway.networking.k8s.io/Gateway ` ](https://kubernetes.io/docs/concepts/services-networking/gateway/) Not available in the analysis APIs. 
  * [ ` gateway.networking.k8s.io/GatewayClass ` ](https://kubernetes.io/docs/concepts/services-networking/gateway/) Not available in the analysis APIs. 
  * [ ` gateway.networking.k8s.io/HTTPRoute ` ](https://kubernetes.io/docs/concepts/services-networking/gateway/) Not available in the analysis APIs. 
  * [ ` gateway.networking.k8s.io/ReferenceGrant ` ](https://kubernetes.io/docs/concepts/services-networking/gateway/) Not available in the analysis APIs. 
  * [ ` k8s.io/Endpoints ` ](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/endpoints-v1/)
  * [ ` k8s.io/Namespace ` ](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/namespace-v1/)
  * [ ` k8s.io/Node ` ](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/node-v1/)
  * [ ` k8s.io/PersistentVolume ` ](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
  * [ ` k8s.io/PersistentVolumeClaim ` ](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
  * [ ` k8s.io/Pod ` ](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/)
  * [ ` k8s.io/PodTemplate ` ](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-template-v1/)
  * [ ` k8s.io/ReplicationController ` ](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/replication-controller-v1/)
  * [ ` k8s.io/ResourceQuota ` ](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
  * [ ` k8s.io/Secret ` ](https://kubernetes.io/docs/concepts/configuration/secret/) Not available in the analysis and search APIs. 
  * [ ` k8s.io/Service ` ](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/)
  * [ ` k8s.io/ServiceAccount ` ](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/service-account-v1/) Not available in the analysis APIs. 
  * [ ` networking.k8s.io/Ingress ` ](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/ingress-v1/) Not available in the analysis APIs.  In beta for the export, list, and monitor APIs.
  * [ ` networking.k8s.io/NetworkPolicy ` ](https://kubernetes.io/docs/reference/kubernetes-api/policy-resources/network-policy-v1/)
  * [ ` policy.k8s.io/PodDisruptionBudget ` ](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)
  * [ ` rbac.authorization.k8s.io/ClusterRole ` ](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/cluster-role-v1/)
  * [ ` rbac.authorization.k8s.io/ClusterRoleBinding ` ](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/cluster-role-binding-v1/)
  * [ ` rbac.authorization.k8s.io/Role ` ](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/role-v1/)
  * [ ` rbac.authorization.k8s.io/RoleBinding ` ](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/role-binding-v1/)
  * [ ` storage.k8s.io/StorageClass ` ](https://kubernetes.io/docs/concepts/storage/storage-classes/)

  
**Hub** |  [API reference](https://gkehub.googleapis.com/$discovery/rest?version=v1)

  * [ ` gkehub.googleapis.com/Feature ` ](https://docs.cloud.google.com/anthos/fleet-management/docs/reference/rest/v1/projects.locations.features)
  * [ ` gkehub.googleapis.com/Fleet ` ](https://docs.cloud.google.com/anthos/fleet-management/docs/reference/rest/v1/projects.locations.fleets) Not available in the analysis APIs. 
  * [ ` gkehub.googleapis.com/Membership ` ](https://docs.cloud.google.com/anthos/multicluster-management/reference/rest/v1/projects.locations.memberships)
  * [ ` gkehub.googleapis.com/MembershipBinding ` ](https://docs.cloud.google.com/anthos/fleet-management/docs/reference/rest/v1/projects.locations.memberships.bindings) Not available in the analysis APIs. 
  * [ ` gkehub.googleapis.com/MembershipFeature ` ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2/projects.locations.memberships.features) Not available in the analysis APIs. 
  * [ ` gkehub.googleapis.com/Namespace ` ](https://docs.cloud.google.com/anthos/fleet-management/docs/reference/rest/v1/projects.locations.scopes.namespaces) Not available in the analysis APIs. 
  * [ ` gkehub.googleapis.com/RBACRoleBinding ` ](https://docs.cloud.google.com/anthos/fleet-management/docs/reference/rest/v1/projects.locations.scopes.rbacrolebindings) Not available in the analysis APIs. 
  * [ ` gkehub.googleapis.com/Scope ` ](https://docs.cloud.google.com/anthos/fleet-management/docs/reference/rest/v1/projects.locations.scopes) Not available in the analysis APIs. 

  
**Identity and Access Management v1** IAM data can be stale by up to 7 days. |  [API reference](https://iam.googleapis.com/$discovery/rest?version=v1)

  * [ ` iam.googleapis.com/OauthClient ` ](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients) Not available in the analysis APIs. 
  * [ ` iam.googleapis.com/OauthClientCredential ` ](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.oauthClients.credentials) Not available in the analysis APIs. 
  * [ ` iam.googleapis.com/Role ` ](https://docs.cloud.google.com/iam/docs/reference/rest/v1/roles) Searchable attributes:
    * ` includedPermissions `
  * [ ` iam.googleapis.com/ServiceAccount ` ](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts) Searchable attributes:
    * ` email `
    * ` uniqueId `
Disabling or enabling a service account can take up to 48 hours to be reflected in Cloud Asset Inventory responses. 
  * [ ` iam.googleapis.com/ServiceAccountKey ` ](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys) Not available in the analysis APIs. 
  * [ ` iam.googleapis.com/WorkforcePool ` ](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools) Not available in the analysis APIs. 
  * [ ` iam.googleapis.com/WorkforcePoolProvider ` ](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers) Not available in the analysis APIs. 
  * [ ` iam.googleapis.com/WorkforcePoolProviderKey ` ](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.keys) Not available in the analysis APIs. 
  * [ ` iam.googleapis.com/WorkloadIdentityPool ` ](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools) Not available in the analysis APIs. 
  * [ ` iam.googleapis.com/WorkloadIdentityPoolManagedIdentity ` ](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces.managedIdentities) Not available in the analysis APIs. 
  * [ ` iam.googleapis.com/WorkloadIdentityPoolNamespace ` ](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces) Not available in the analysis APIs. 
  * [ ` iam.googleapis.com/WorkloadIdentityPoolProvider ` ](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers) Not available in the analysis APIs. 
  * [ ` iam.googleapis.com/WorkloadIdentityPoolProviderKey ` ](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.providers.keys) Not available in the analysis APIs. 

  
**Identity and Access Management v2** |  [API reference](https://iam.googleapis.com/$discovery/rest?version=v2)

  * [ ` iam.googleapis.com/PolicyV2 ` ](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies)

  
**Identity and Access Management v3** |  [API reference](https://iam.googleapis.com/$discovery/rest?version=v3)

  * [ ` iam.googleapis.com/PolicyBinding ` ](https://docs.cloud.google.com/iam/docs/reference/rest/v3/projects.locations.policyBindings) Not available in the analysis APIs. 
  * [ ` iam.googleapis.com/PrincipalAccessBoundaryPolicy ` ](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies) Not available in the analysis APIs. 

  
**Identity Platform** |  [API reference](https://identitytoolkit.googleapis.com/$discovery/rest?version=v2)

  * [ ` identitytoolkit.googleapis.com/Config ` ](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/Config)
  * [ ` identitytoolkit.googleapis.com/DefaultSupportedIdpConfig ` ](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.defaultSupportedIdpConfigs) Not available in the analysis APIs. 
  * [ ` identitytoolkit.googleapis.com/InboundSamlConfig ` ](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.inboundSamlConfigs) Not available in the analysis APIs. 
  * [ ` identitytoolkit.googleapis.com/OauthIdpConfig ` ](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.oauthIdpConfigs) Not available in the analysis APIs. 
  * [ ` identitytoolkit.googleapis.com/Tenant ` ](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants) Not available in the analysis APIs. 

  
**Identity-Aware Proxy** | 

  * [ ` iap.googleapis.com/TunnelDestGroup ` ](https://docs.cloud.google.com/iap/docs/reference/rest/v1/projects.iap_tunnel.locations.destGroups) Effective tags aren't supported. Not available in the analysis APIs. 

  
**Integration Connectors** |  [API reference](https://connectors.googleapis.com/$discovery/rest?version=v1)

  * [ ` connectors.googleapis.com/Connection ` ](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections)
  * [ ` connectors.googleapis.com/EndpointAttachment ` ](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.endpointAttachments)
  * [ ` connectors.googleapis.com/EventSubscription ` ](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections.eventSubscriptions)
  * [ ` connectors.googleapis.com/ManagedZone ` ](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.global.managedZones)
  * [ ` connectors.googleapis.com/RegionalSettings ` ](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/RegionalSettings)
  * [ ` connectors.googleapis.com/Settings ` ](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/Settings)

  
**Knowledge Catalog** |  [API reference](https://dataplex.googleapis.com/$discovery/rest)

  * [ ` dataplex.googleapis.com/AspectType ` ](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.aspectTypes) Not available in the analysis APIs. 
  * [ ` dataplex.googleapis.com/Asset ` ](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.lakes.zones.assets)
  * [ ` dataplex.googleapis.com/DataScan ` ](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.dataScans)
  * [ ` dataplex.googleapis.com/EncryptionConfig ` ](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/organizations.locations.encryptionConfigs) Not available in the analysis APIs. 
  * [ ` dataplex.googleapis.com/EntryGroup ` ](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.entryGroups) Not available in the analysis APIs. 
  * [ ` dataplex.googleapis.com/EntryType ` ](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.entryTypes) Not available in the analysis APIs. 
  * [ ` dataplex.googleapis.com/Glossary ` ](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.glossaries) Not available in the analysis APIs. 
  * [ ` dataplex.googleapis.com/Lake ` ](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.lakes)
  * [ ` dataplex.googleapis.com/MetadataJob ` ](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.metadataJobs) Not available in the analysis APIs. 
  * [ ` dataplex.googleapis.com/Task ` ](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.lakes.tasks)
  * [ ` dataplex.googleapis.com/Zone ` ](https://docs.cloud.google.com/dataplex/docs/reference/rest/v1/projects.locations.lakes.zones)

  
**KRM API Hosting** | 

  * ` krmapihosting.googleapis.com/KrmApiHost `

  
**Live Stream API** |  [API reference](https://livestream.googleapis.com/$discovery/rest?version=v1)

  * [ ` livestream.googleapis.com/Asset ` ](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.assets)
  * [ ` livestream.googleapis.com/Channel ` ](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels)
  * [ ` livestream.googleapis.com/Input ` ](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs)
  * [ ` livestream.googleapis.com/Pool ` ](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.pools)

  
**Looker** |  [API reference](https://looker.googleapis.com/$discovery/rest?version=v1)

  * [ ` looker.googleapis.com/Backup ` ](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances.backups) Not available in the analysis APIs. 
  * [ ` looker.googleapis.com/Instance ` ](https://docs.cloud.google.com/looker/docs/reference/rest/v1/projects.locations.instances) Not available in the analysis APIs. 

  
**Managed Service for Apache Airflow** Managed Service for Apache Airflow v1beta1 is supported. The resources in v1beta1 are a superset of those in v1. |  [API reference](https://composer.googleapis.com/$discovery/rest?version=v1beta1)

  * [ ` composer.googleapis.com/Environment ` ](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments) In beta for the export, list, and monitor APIs.

  
**Managed Service for Apache Spark** |  [API reference](https://dataproc.googleapis.com/$discovery/rest?version=v1)

  * [ ` dataproc.googleapis.com/AutoscalingPolicy ` ](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.autoscalingPolicies)
  * [ ` dataproc.googleapis.com/Batch ` ](https://docs.cloud.google.com/dataproc-serverless/docs/reference/rest/v1/projects.locations.batches)
  * [ ` dataproc.googleapis.com/Cluster ` ](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.clusters)
  * [ ` dataproc.googleapis.com/Job ` ](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.jobs)
  * [ ` dataproc.googleapis.com/Session ` ](https://docs.cloud.google.com/dataproc-serverless/docs/reference/rest/v1/projects.locations.sessions) Not available in the analysis APIs. 
  * [ ` dataproc.googleapis.com/WorkflowTemplate ` ](https://docs.cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.workflowTemplates)

  
**Managed Service for Microsoft Active Directory** |  [API reference](https://managedidentities.googleapis.com/$discovery/rest)

  * [ ` managedidentities.googleapis.com/Domain ` ](https://docs.cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains)

  
**Memorystore** | 

  * [ ` memorystore.googleapis.com/Instance ` ](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances) Not available in the analysis APIs. 

  
**Memorystore for Memcached** |  [API reference](https://memcache.googleapis.com/$discovery/rest?version=v1)

  * [ ` memcache.googleapis.com/Instance ` ](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.instances)

  
**Memorystore for Redis** |  [API reference](https://redis.googleapis.com/$discovery/rest?version=v1)

  * [ ` redis.googleapis.com/Cluster ` ](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters)
  * [ ` redis.googleapis.com/Instance ` ](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances)

  
**Migrate to Virtual Machines** |  [API reference](https://docs.cloud.google.com/vmware-engine/docs/reference/rest)

  * [ ` vmmigration.googleapis.com/CloneJob ` ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cloneJobs) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` vmmigration.googleapis.com/CutoverJob ` ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cutoverJobs) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` vmmigration.googleapis.com/DatacenterConnector ` ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` vmmigration.googleapis.com/Group ` ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.groups) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` vmmigration.googleapis.com/ImageImport ` ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.imageImports) Not available in the analysis APIs. 
  * [ ` vmmigration.googleapis.com/MigratingVm ` ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` vmmigration.googleapis.com/Source ` ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` vmmigration.googleapis.com/TargetProject ` ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.targetProjects) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` vmmigration.googleapis.com/UtilizationReport ` ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.utilizationReports) Effective tags aren't supported. Not available in the analysis APIs. 

  
**Network Connectivity** |  [API reference](https://networkconnectivity.googleapis.com/$discovery/rest?version=v1)

  * [ ` networkconnectivity.googleapis.com/Group ` ](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.groups) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` networkconnectivity.googleapis.com/Hub ` ](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs)
  * [ ` networkconnectivity.googleapis.com/HubRoute ` ](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables.routes)
  * [ ` networkconnectivity.googleapis.com/InternalRange ` ](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.internalRanges) Not available in the analysis APIs. 
  * ` networkconnectivity.googleapis.com/PolicyBasedRoute `
  * [ ` networkconnectivity.googleapis.com/RegionalEndpoint ` ](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.regionalEndpoints) Not available in the Analysis APIs. 
  * [ ` networkconnectivity.googleapis.com/RouteTable ` ](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.routeTables)
  * [ ` networkconnectivity.googleapis.com/Spoke ` ](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes)

  
**Network Management API** |  [API reference](https://networkmanagement.googleapis.com/$discovery/rest)

  * [ ` networkmanagement.googleapis.com/ConnectivityTest ` ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests)
  * [ ` networkmanagement.googleapis.com/VpcFlowLogsConfig ` ](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs) Effective tags aren't supported. Not available in the analysis and search APIs. 

  
**Network Security Integration** Network Security Integration asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync. |  [API reference](https://networksecurity.googleapis.com/$discovery/rest?version=v1)

  * [ ` networksecurity.googleapis.com/InterceptDeployment ` ](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeployments) Not available in the analysis APIs. 
  * [ ` networksecurity.googleapis.com/InterceptDeploymentGroup ` ](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeploymentGroups) Not available in the analysis APIs. 
  * [ ` networksecurity.googleapis.com/InterceptEndpointGroup ` ](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups) Not available in the analysis APIs. 
  * [ ` networksecurity.googleapis.com/InterceptEndpointGroupAssociation ` ](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations) Not available in the analysis APIs. 
  * [ ` networksecurity.googleapis.com/MirroringDeployment ` ](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments) Not available in the analysis APIs. 
  * [ ` networksecurity.googleapis.com/MirroringDeploymentGroup ` ](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeploymentGroups)
  * [ ` networksecurity.googleapis.com/MirroringEndpointGroup ` ](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroups) Not available in the analysis APIs. 
  * [ ` networksecurity.googleapis.com/MirroringEndpointGroupAssociation ` ](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroupAssociations) Not available in the analysis APIs. 

  
**Network Services API** |  [API reference](https://networkservices.googleapis.com/$discovery/rest?version=v1)

  * [ ` networkservices.googleapis.com/AgentGateway ` ](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.agentGateways) Not available in the analysis APIs. 
  * [ ` networkservices.googleapis.com/AuthzExtension ` ](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/projects.locations.authzExtensions) Not available in the analysis APIs. 
  * [ ` networkservices.googleapis.com/EdgeCacheKeyset ` ](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheKeysets) Not available in the analysis APIs. 
  * [ ` networkservices.googleapis.com/EdgeCacheOrigin ` ](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheOrigins) Not available in the analysis APIs. 
  * [ ` networkservices.googleapis.com/EdgeCacheService ` ](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices) Not available in the analysis APIs. 
  * [ ` networkservices.googleapis.com/EndpointPolicy ` ](https://docs.cloud.google.com/traffic-director/docs/reference/network-services/rest/v1/projects.locations.endpointPolicies)
  * [ ` networkservices.googleapis.com/Gateway ` ](https://docs.cloud.google.com/traffic-director/docs/reference/network-services/rest/v1/projects.locations.gateways)
  * [ ` networkservices.googleapis.com/GrpcRoute ` ](https://docs.cloud.google.com/traffic-director/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes)
  * [ ` networkservices.googleapis.com/HttpRoute ` ](https://docs.cloud.google.com/traffic-director/docs/reference/network-services/rest/v1/projects.locations.httpRoutes)
  * [ ` networkservices.googleapis.com/LbRouteExtension ` ](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/projects.locations.lbRouteExtensions) Not available in the analysis APIs. 
  * [ ` networkservices.googleapis.com/LbTrafficExtension ` ](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/projects.locations.lbTrafficExtensions) Not available in the analysis APIs. 
  * [ ` networkservices.googleapis.com/Mesh ` ](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.meshes)
  * [ ` networkservices.googleapis.com/ServiceBinding ` ](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceBindings)
  * [ ` networkservices.googleapis.com/ServiceLbPolicy ` ](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies) Not available in the analysis APIs. 
  * [ ` networkservices.googleapis.com/TcpRoute ` ](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes)
  * [ ` networkservices.googleapis.com/TlsRoute ` ](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes)
  * [ ` networkservices.googleapis.com/WasmPlugin ` ](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1alpha1/projects.locations.wasmPlugins) Not available in the analysis APIs. 
  * [ ` networkservices.googleapis.com/WasmPluginVersion ` ](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1alpha1/projects.locations.wasmPlugins.versions) Not available in the analysis APIs. 

  
**Oracle Database@Google Cloud** |  [API reference](https://oracledatabase.googleapis.com/$discovery/rest?version=v1)

  * [ ` oracledatabase.googleapis.com/AutonomousDatabase ` ](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases) Not available in the analysis APIs. 
  * [ ` oracledatabase.googleapis.com/CloudExadataInfrastructure ` ](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures) Not available in the analysis APIs. 
  * [ ` oracledatabase.googleapis.com/CloudVmCluster ` ](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters) Not available in the analysis APIs. 

  
**Organization Policy Service** |  [API reference](https://orgpolicy.googleapis.com/$discovery/rest?version=v2)

  * ` orgpolicy.googleapis.com/Policy ` Not available in the analysis APIs. 

  
**Organization Policy Service v2** | 

  * [ ` orgpolicy.googleapis.com/CustomConstraint ` ](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints)
  * [ ` orgpolicy.googleapis.com/Policy ` ](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.policies#Policy)

  
**Parallelstore** |  [API reference](https://parallelstore.googleapis.com/$discovery/rest?version=v1)

  * [ ` parallelstore.googleapis.com/Instance ` ](https://docs.cloud.google.com/parallelstore/docs/reference/rest/v1/projects.locations.instances) Effective tags aren't supported. Not available in the analysis APIs. 

  
**Parameter Manager** |  [API reference](https://parametermanager.googleapis.com/$discovery/rest?version=v1)

  * [ ` parametermanager.googleapis.com/Parameter ` ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` parametermanager.googleapis.com/ParameterVersion ` ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions) Effective tags aren't supported. Not available in the analysis APIs. 

  
**Privileged Access Manager** |  [API reference](https://privilegedaccessmanager.googleapis.com/$discovery/rest?version=v1)

  * ` privilegedaccessmanager.googleapis.com/Entitlement ` Not available in the analysis APIs. 
  * ` privilegedaccessmanager.googleapis.com/Grant `

  
**Pub/Sub** |  [API reference](https://pubsub.googleapis.com/$discovery/rest?version=v1)

  * [ ` pubsub.googleapis.com/Schema ` ](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.schemas)
  * [ ` pubsub.googleapis.com/Snapshot ` ](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/Snapshot)
  * [ ` pubsub.googleapis.com/Subscription ` ](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions)
  * [ ` pubsub.googleapis.com/Topic ` ](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics)

  
**reCAPTCHA** |  [API reference](https://recaptchaenterprise.googleapis.com/$discovery/rest?version=v1)

  * [ ` recaptchaenterprise.googleapis.com/FirewallPolicy ` ](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.firewallpolicies) Not available in the analysis APIs. 
  * [ ` recaptchaenterprise.googleapis.com/Key ` ](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys) Not available in the analysis APIs. 

  
**Resource Manager** |  [API reference](https://cloudresourcemanager.googleapis.com/$discovery/rest)

  * [ ` cloudresourcemanager.googleapis.com/Folder ` ](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders)
  * [ ` cloudresourcemanager.googleapis.com/Lien ` ](https://docs.cloud.google.com/resource-manager/reference/rest/v3/liens) Not available in the analysis, export, list, and monitor APIs. 
  * [ ` cloudresourcemanager.googleapis.com/Organization ` ](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations)
  * [ ` cloudresourcemanager.googleapis.com/Project ` ](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects) Searchable attributes:
    * ` projectId `
  * [ ` cloudresourcemanager.googleapis.com/TagBinding ` ](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings) Not available in the analysis and search APIs.  In search, directly attached and effective tags can be queried and/or returned along with resources. For details, see [Search for resources](https://docs.cloud.google.com/asset-inventory/docs/search-resources#vm-tagkey).
  * [ ` cloudresourcemanager.googleapis.com/TagKey ` ](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys)
  * [ ` cloudresourcemanager.googleapis.com/TagValue ` ](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues)

  
**Secret Manager** Secret Manager asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync.The `location` field in the Secret Manager asset does not reflect the replication policy of the secret. Instead, use the `replication` field to get that information. |  [API reference](https://secretmanager.googleapis.com/$discovery/rest?version=v1)

  * [ ` secretmanager.googleapis.com/Secret ` ](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets)
  * [ ` secretmanager.googleapis.com/SecretVersion ` ](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions)

  
**Secure Source Manager** Secure Source Manager asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync. |  [API reference](https://securesourcemanager.googleapis.com/$discovery/rest?version=v1)

  * [ ` securesourcemanager.googleapis.com/Instance ` ](https://docs.cloud.google.com/secure-source-manager/docs/reference/rest/v1/projects.locations.instances) Not available in the analysis APIs. 

  
**Secure Web Proxy** Secure Web Proxy asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync. |  [API reference](https://networksecurity.googleapis.com/$discovery/rest?version=v1)

  * [ ` networksecurity.googleapis.com/GatewaySecurityPolicy ` ](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1/projects.locations.gatewaySecurityPolicies) Not available in the analysis APIs. 
  * [ ` networksecurity.googleapis.com/GatewaySecurityPolicyRule ` ](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1/projects.locations.gatewaySecurityPolicies.rules) Not available in the analysis APIs. 
  * [ ` networksecurity.googleapis.com/TlsInspectionPolicy ` ](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1/projects.locations.tlsInspectionPolicies) Not available in the analysis APIs. 
  * [ ` networksecurity.googleapis.com/UrlList ` ](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1/projects.locations.urlLists) Not available in the analysis APIs. 

  
**Security Center Management API** |  [API reference](https://securitycenter.googleapis.com/$discovery/rest?version=v1)

  * [ ` securitycentermanagement.googleapis.com/EventThreatDetectionCustomModule ` ](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/projects.locations.eventThreatDetectionCustomModules)
  * [ ` securitycentermanagement.googleapis.com/SecurityCenterService ` ](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/projects.locations.securityCenterServices)
  * [ ` securitycentermanagement.googleapis.com/SecurityHealthAnalyticsCustomModule ` ](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityHealthAnalyticsCustomModules)

  
**Security Command Center** |  [API reference](https://securitycenter.googleapis.com/$discovery/rest?version=v1)

  * [ ` securitycenter.googleapis.com/BigQueryExport ` ](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/projects.locations.bigQueryExports) Not available in the analysis APIs. 
  * [ ` securitycenter.googleapis.com/ContainerThreatDetectionSettings ` ](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1beta2/projects.containerThreatDetectionSettings) Not available in the analysis APIs. 
  * [ ` securitycenter.googleapis.com/EventThreatDetectionSettings ` ](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1beta2/projects.eventThreatDetectionSettings) Not available in the analysis APIs. 
  * [ ` securitycenter.googleapis.com/MuteConfig ` ](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/projects.locations.muteConfigs) Not available in the analysis APIs. 
  * [ ` securitycenter.googleapis.com/NotificationConfig ` ](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/projects.locations.notificationConfigs) Not available in the analysis APIs. 
  * [ ` securitycenter.googleapis.com/ResourceValueConfig ` ](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.resourceValueConfigs) Not available in the analysis APIs. 
  * [ ` securitycenter.googleapis.com/SecurityHealthAnalyticsSettings ` ](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1beta2/projects.securityHealthAnalyticsSettings) Not available in the analysis APIs. 
  * [ ` securitycenter.googleapis.com/VirtualMachineThreatDetectionSettings ` ](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1beta2/projects.virtualMachineThreatDetectionSettings) Not available in the analysis APIs. 
  * [ ` securitycenter.googleapis.com/WebSecurityScannerSettings ` ](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1beta2/projects.webSecurityScannerSettings) Not available in the analysis APIs. 

  
**Security Posture API** |  [API reference](https://securityposture.googleapis.com/$discovery/rest?version=v1)

  * [ ` securityposture.googleapis.com/Posture ` ](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/Posture)
  * [ ` securityposture.googleapis.com/PostureDeployment ` ](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/PostureDeployment)

  
**Sensitive Data Protection** |  [API reference](https://dlp.googleapis.com/$discovery/rest?version=v2)

  * [ ` dlp.googleapis.com/DeidentifyTemplate ` ](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.deidentifyTemplates)
  * [ ` dlp.googleapis.com/DiscoveryConfig ` ](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.discoveryConfigs)
  * [ ` dlp.googleapis.com/DlpJob ` ](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs)
  * [ ` dlp.googleapis.com/InspectTemplate ` ](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.inspectTemplates)
  * [ ` dlp.googleapis.com/JobTrigger ` ](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers)
  * [ ` dlp.googleapis.com/StoredInfoType ` ](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes)

  
**Serverless VPC Access** |  [API reference](https://vpcaccess.googleapis.com/$discovery/rest?version=v1)

  * [ ` vpcaccess.googleapis.com/Connector ` ](https://docs.cloud.google.com/vpc/docs/reference/vpcaccess/rest/v1/projects.locations.connectors)

  
**Service Directory** |  [API reference](https://servicedirectory.googleapis.com/$discovery/rest?version=v1)

  * [ ` servicedirectory.googleapis.com/Endpoint ` ](https://docs.cloud.google.com/service-directory/docs/reference/rest/v1/projects.locations.namespaces.services.endpoints)
  * [ ` servicedirectory.googleapis.com/Namespace ` ](https://docs.cloud.google.com/service-directory/docs/reference/rest/v1/projects.locations.namespaces)
  * [ ` servicedirectory.googleapis.com/Service ` ](https://docs.cloud.google.com/service-directory/docs/reference/rest/v1/projects.locations.namespaces.services)

  
**Service Management** Service Management asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync. |  [API reference](https://servicemanagement.googleapis.com/$discovery/rest?version=v1)

  * [ ` servicemanagement.googleapis.com/ManagedService ` ](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services)
  * [ ` servicemanagement.googleapis.com/Service ` ](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs) Effective tags aren't supported. Not available in the analysis APIs. 

  
**Service Networking** |  [API reference](https://servicenetworking.googleapis.com/$discovery/rest?version=v1)

  * [ ` servicenetworking.googleapis.com/Connection ` ](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections)

  
**Service Usage** Service Usage asset change history might be incomplete. The `config` field in the metadata is not supported yet. |  [API reference](https://serviceusage.googleapis.com/$discovery/rest?version=v1)

  * [ ` serviceusage.googleapis.com/Service ` ](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services)

  
**Spanner** |  [API reference](https://spanner.googleapis.com/$discovery/rest?version=v1)

  * [ ` spanner.googleapis.com/Backup ` ](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups)
  * [ ` spanner.googleapis.com/Database ` ](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases)
  * [ ` spanner.googleapis.com/Instance ` ](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances)
  * [ ` spanner.googleapis.com/InstanceConfig ` ](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs)
  * [ ` spanner.googleapis.com/InstancePartition ` ](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions)

  
**Speech-to-Text** |  [API reference](https://speech.googleapis.com/$discovery/rest?version=v1)

  * [ ` speech.googleapis.com/Config ` ](https://docs.cloud.google.com/speech-to-text/v2/docs/reference/rest/v2/projects.locations.config)
  * [ ` speech.googleapis.com/CustomClass ` ](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/projects.locations.customClasses)
  * ` speech.googleapis.com/Endpoint ` Not available in the analysis APIs. 
  * ` speech.googleapis.com/Model ` Not available in the analysis APIs. 
  * [ ` speech.googleapis.com/PhraseSet ` ](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/projects.locations.phraseSets)
  * [ ` speech.googleapis.com/Recognizer ` ](https://docs.cloud.google.com/speech-to-text/v2/docs/reference/rest/v2/projects.locations.recognizers)

  
**Storage Batch Operations API** |  [API reference](https://storagebatchoperations.googleapis.com/$discovery/rest?version=v1)

  * [ ` storagebatchoperations.googleapis.com/Job ` ](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs)

  
**Storage Insights** |  [API reference](https://storageinsights.googleapis.com/$discovery/rest?version=v1)

  * [ ` storageinsights.googleapis.com/ReportConfig ` ](https://docs.cloud.google.com/storage/docs/insights/v1/reportConfig)
  * [ ` storageinsights.googleapis.com/ReportDetail ` ](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs.reportDetails)

  
**Storage Transfer Service** |  [API reference](https://storagetransfer.googleapis.com/$discovery/rest?version=v1)

  * [ ` storagetransfer.googleapis.com/TransferJob ` ](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs) Not available in the analysis APIs. 

  
**Transcoder API** |  [API reference](https://transcoder.googleapis.com/$discovery/rest?version=v1)

  * [ ` transcoder.googleapis.com/Job ` ](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs)
  * [ ` transcoder.googleapis.com/JobTemplate ` ](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobTemplates)

  
**Vertex AI** Vertex AI asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync. Some datasets' metadata (for example, the `TABLE` data type) could be stale due to an ongoing data issue. |  [API reference](https://aiplatform.googleapis.com/$discovery/rest?version=v1)

  * [ ` aiplatform.googleapis.com/BatchPredictionJob ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.batchPredictionJobs)
  * [ ` aiplatform.googleapis.com/CachedContent ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.cachedContents)
  * [ ` aiplatform.googleapis.com/CustomJob ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.customJobs)
  * ` aiplatform.googleapis.com/DataLabelingJob `
  * [ ` aiplatform.googleapis.com/Dataset ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.datasets)
  * [ ` aiplatform.googleapis.com/DeploymentResourcePool ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.deploymentResourcePools) Effective tags aren't supported. Not available in the analysis APIs. 
  * [ ` aiplatform.googleapis.com/Endpoint ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints) The `deployedModels` field is not populated. 
  * [ ` aiplatform.googleapis.com/FeatureGroup ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featureGroups) Not available in the analysis APIs. 
  * [ ` aiplatform.googleapis.com/FeatureOnlineStore ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featureOnlineStores) Not available in the analysis APIs. 
  * [ ` aiplatform.googleapis.com/Featurestore ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores)
  * [ ` aiplatform.googleapis.com/HyperparameterTuningJob ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.hyperparameterTuningJobs)
  * [ ` aiplatform.googleapis.com/Index ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.indexes)
  * [ ` aiplatform.googleapis.com/IndexEndpoint ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.indexEndpoints)
  * [ ` aiplatform.googleapis.com/MetadataStore ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.metadataStores)
  * [ ` aiplatform.googleapis.com/Model ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models) The `deployedModels` field is not populated. 
  * [ ` aiplatform.googleapis.com/ModelDeploymentMonitoringJob ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.modelDeploymentMonitoringJobs)
  * [ ` aiplatform.googleapis.com/NasJob ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.nasJobs)
  * [ ` aiplatform.googleapis.com/NotebookExecutionJob ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.notebookExecutionJobs)
  * [ ` aiplatform.googleapis.com/NotebookRuntime ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.notebookRuntimes) Effective tags aren't supported. 
  * [ ` aiplatform.googleapis.com/NotebookRuntimeTemplate ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.notebookRuntimeTemplates) Effective tags aren't supported. 
  * [ ` aiplatform.googleapis.com/PipelineJob ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.pipelineJobs)
  * [ ` aiplatform.googleapis.com/ReasoningEngine ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.reasoningEngines) Not available in the analysis APIs. 
  * [ ` aiplatform.googleapis.com/SpecialistPool ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.specialistPools)
  * [ ` aiplatform.googleapis.com/Tensorboard ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.tensorboards)
  * [ ` aiplatform.googleapis.com/TrainingPipeline ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.trainingPipelines)
  * [ ` aiplatform.googleapis.com/TuningJob ` ](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.tuningJobs) Not available in the analysis APIs. 

  
**Vertex AI Workbench** |  [API reference](https://notebooks.googleapis.com/$discovery/rest?version=v2)

  * [ ` notebooks.googleapis.com/Instance ` ](https://docs.cloud.google.com/vertex-ai/docs/workbench/reference/rest/v2/projects.locations.instances) Not available in the analysis APIs. 

  
**Video Stitcher API** |  [API reference](https://docs.cloud.google.com/video-stitcher/docs/reference/rest)

  * [ ` videostitcher.googleapis.com/CdnKey ` ](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.cdnKeys) Not available in the analysis APIs. 
  * [ ` videostitcher.googleapis.com/LiveConfig ` ](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveConfigs) Not available in the analysis APIs. 
  * [ ` videostitcher.googleapis.com/Slate ` ](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.slates) Not available in the analysis APIs. 
  * [ ` videostitcher.googleapis.com/VodConfig ` ](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodConfigs) Not available in the analysis APIs. 

  
**Web Security Scanner** |  [API reference](https://websecurityscanner.googleapis.com/$discovery/rest?version=v1)

  * [ ` websecurityscanner.googleapis.com/ScanConfig ` ](https://docs.cloud.google.com/security-command-center/docs/reference/web-security-scanner/rest/v1/projects.scanConfigs) Not available in the analysis APIs. 

  
**Workflows** Workflows asset change history might be incomplete. Data freshness is synchronized every 7 hours. If a sync fails, freshness is delayed until the next successful sync. |  [API reference](https://workflows.googleapis.com/$discovery/rest?version=v1)

  * [ ` workflows.googleapis.com/Workflow ` ](https://docs.cloud.google.com/workflows/docs/reference/rest/v1/projects.locations.workflows)

  
**Workload Manager** |  [API reference](https://workloadmanager.googleapis.com/$discovery/rest?version=v1)

  * [ ` workloadmanager.googleapis.com/Evaluation ` ](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.evaluations)

  
  
## Policy types

Cloud Asset Inventory uses the following asset types for the `ACCESS_POLICY`, `IAM_POLICY`, and `ORG_POLICY` [content types](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types).

Service | Asset type  
---|---  
**Access policy (VPC Service Controls policy)** |  [ API reference ](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies) **Supported policy parent**

  * [ ` cloudresourcemanager.googleapis.com/Organization ` ](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations) Not available in the analysis APIs.

**Supported policy scope**

  * [ ` cloudresourcemanager.googleapis.com/Folder ` ](https://docs.cloud.google.com/resource-manager/reference/rest/v1/folders) Not available in the analysis APIs.
  * [ ` cloudresourcemanager.googleapis.com/Organization ` ](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations) Not available in the analysis APIs.
  * [ ` cloudresourcemanager.googleapis.com/Project ` ](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects) Not available in the analysis APIs.

  
**IAM policy** Data can be delayed by approximately 36 hours. |  [ API reference ](https://docs.cloud.google.com/iam/reference/rest/v1/Policy) Supported resource types that IAM policies can be attached to:

  * All asset types in supported resource types. 
  * All policy types in this table except for IAM policy itself.
  * The following IAP resource types:
    * ` iap.googleapis.com/Tunnel ` Not available in the analysis and search APIs.
    * ` iap.googleapis.com/TunnelInstance ` Not available in the analysis and search APIs.
    * ` iap.googleapis.com/TunnelZone ` Not available in the analysis and search APIs.
    * ` iap.googleapis.com/Web ` Not available in the analysis and search APIs.
    * ` iap.googleapis.com/WebService ` Not available in the analysis and search APIs.
    * ` iap.googleapis.com/WebServiceVersion ` Not available in the analysis and search APIs.
    * ` iap.googleapis.com/WebType ` Not available in the analysis and search APIs.

  
**Organization policy** |  [ API reference ](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy) Supported resource types that organization policies can be attached to:

  * [ ` cloudresourcemanager.googleapis.com/Folder ` ](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders)
  * [ ` cloudresourcemanager.googleapis.com/Organization ` ](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations)
  * [ ` cloudresourcemanager.googleapis.com/Project ` ](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects)

  
  
## Runtime information types

Cloud Asset Inventory uses the following asset types for the `OS_INVENTORY` [content type](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview#content_types).

Service | Asset type  
---|---  
**OS inventory** Provides information on the operating system, installed packages, and available package updates for an instance. Learn more about [ OS inventory management](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management).  | 

  * [ ` compute.googleapis.com/Instance ` ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances) Only available in analysis, list, and search APIs.

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
