---
url: https://docs.cloud.google.com/iam/docs/pab-blocked-permissions/
title: Principal Access Boundary policy enforcement version permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:21.613041+00:00
---

# Principal Access Boundary policy enforcement version permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/pab-blocked-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Principal Access Boundary policy enforcement version permissions Stay organized with collections  Save and categorize content based on your preferences. 

Principal Access Boundary policies can block all permissions that are included in the policy's _enforcement version_. If a Principal Access Boundary policy can block a permission, then it can prevent principals from using that permission to access resources.

You specify a policy's enforcement version when you create the policy. Updating the enforcement version updates the permissions that the policy can block.

If Principal Access Boundary policies can't block a permission, then they have no effect on whether principals can use the permission. In other words, IAM can't enforce the policy for access attempts involving that permission.

Periodically, IAM adds new Principal Access Boundary enforcement versions that can block additional permissions. Each new version can also block all of the permissions in the previous version.

This page lists the permissions that each enforcement version can block.

For more information about how to set and manage enforcement versions, see [Manage enforcement versions](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#versions).

## Default enforcement version

The default enforcement version is used for the following Principal Access Boundary policies:

  * New policies that don't specify a version number
  * Policies that use the value `latest` for the version



The current default enforcement version is `4`.

## Enforcement version `4`

Policies with enforcement version `4` can block all of the permissions listed in the following enforcement versions:

  * Enforcement version `1`
  * Enforcement version `2`
  * Enforcement version `3`



Additionally, policies with the enforcement version `4` can also block all of the permissions listed in the following table.

Each row contains the following information:

  * The name of a service with permissions that Principal Access Boundary policies can block.
  * The permissions for that service that Principal Access Boundary policies can block.

In some cases, a section of a permission name is replaced with a wildcard character (`*`). This format indicates that Principal Access Boundary policies can block all permissions that match that pattern.




Service | Permissions | Exceptions  
---|---|---  
BigQuery sharing | 

  * `analyticshub.googleapis.com/dataExchanges.*`

| None  
BigQuery | 

  * `bigquery.googleapis.com/capacityCommitments.*`
  * `bigquery.googleapis.com/datasources.*`
  * `bigquery.googleapis.com/readsessions.*`
  * `bigquery.googleapis.com/reservations.*`
  * `bigquery.googleapis.com/transfers.*`

| None  
Cloud Deploy | 

  * `clouddeploy.googleapis.com/*.*`

| None  
Filestore | 

  * `file.googleapis.com/*.*`

| None  
Network Connectivity Center | 

  * `networkconnectivity.googleapis.com/groups.*`
  * `networkconnectivity.googleapis.com/hubRouteTables.*`
  * `networkconnectivity.googleapis.com/hubRoutes.*`
  * `networkconnectivity.googleapis.com/hubs.*`
  * `networkconnectivity.googleapis.com/internalRanges.*`
  * `networkconnectivity.googleapis.com/policyBasedRoutes.*`
  * `networkconnectivity.googleapis.com/regionalEndpoints.*`
  * `networkconnectivity.googleapis.com/spokes.*`

| None  
Certificate Authority Service | 

  * `privateca.googleapis.com/*.*`

| None  
Identity and Access Management | 

  * `iam.googleapis.com/oauthClientCredentials.*`
  * `iam.googleapis.com/oauthClients.*`
  * `iam.googleapis.com/workforcePoolProviderKeys.*`
  * `iam.googleapis.com/workforcePoolProviders.*`
  * `iam.googleapis.com/workforcePoolSubjects.*`
  * `iam.googleapis.com/workforcePools.*`
  * `iam.googleapis.com/workloadIdentityPoolNamespaces.*`
  * `iam.googleapis.com/workloadIdentityPoolProviderKeys.*`
  * `iam.googleapis.com/workloadIdentityPoolProviders.*`
  * `iam.googleapis.com/workloadIdentityPools.*`

| 

  * `iam.googleapis.com/*.createPolicyBinding`
  * `iam.googleapis.com/*.deletePolicyBinding`
  * `iam.googleapis.com/*.searchPolicyBindings`
  * `iam.googleapis.com/*.updatePolicyBinding`

  
Live Stream | 

  * `livestream.googleapis.com/*.*`

| None  
Document AI | 

  * `documentai.googleapis.com/*.*`

| None  
Security Center Management API | 

  * `securitycentermanagement.googleapis.com/*.*`

| None  
Web Security Scanner | 

  * `cloudsecurityscanner.googleapis.com/*.*`

| None  
Security Command Center | 

  * `securitycenter.googleapis.com/*.*`

| None  
Cloud Quotas | 

  * `cloudquotas.googleapis.com/*.*`

| None  
Recommender | 

  * `recommender.googleapis.com/*.*`

| None  
AlloyDB for PostgreSQL | 

  * `alloydb.googleapis.com/*.*`

| 

  * `alloydb.googleapis.com/databases.*`

  
App Hub | 

  * `apphub.googleapis.com/*.*`

| None  
Cloud Integrations | 

  * `integrations.googleapis.com/*.*`

| 

  * `integrations.googleapis.com/apigeeauthconfigs.*`
  * `integrations.googleapis.com/apigeecertificates.*`
  * `integrations.googleapis.com/apigeeintegrations.*`
  * `integrations.googleapis.com/apigeeintegrationvers.*`
  * `integrations.googleapis.com/apigeeproducts.*`
  * `integrations.googleapis.com/apigeesfdcchannels.*`
  * `integrations.googleapis.com/apigeesfdcinstances.*`
  * `integrations.googleapis.com/apigeesuspensions.*`
  * `integrations.googleapis.com/integrations.deploy`
  * `integrations.googleapis.com/integrations.update`
  * `integrations.googleapis.com/locations.*`
  * `integrations.googleapis.com/securityauthconfigs.*`
  * `integrations.googleapis.com/securityexecutions.*`
  * `integrations.googleapis.com/securityintegrations.*`
  * `integrations.googleapis.com/securityintegrationvers.delete`
  * `integrations.googleapis.com/securityintegrationvers.deploy`
  * `integrations.googleapis.com/securityintegrationvers.list`
  * `integrations.googleapis.com/securityintegtemps.*`
  * `integrations.googleapis.com/securityproducts.*`
  * `integrations.googleapis.com/sfdcchannels.create`
  * `integrations.googleapis.com/sfdcchannels.list`
  * `integrations.googleapis.com/workflows.*`

  
Backup for GKE | 

  * `gkebackup.googleapis.com/*.*`

| None  
Managed Service for Apache Airflow | 

  * `composer.googleapis.com/*.*`

| None  
Cloud Data Fusion | 

  * `datafusion.googleapis.com/instances.*`
  * `datafusion.googleapis.com/locations.*`
  * `datafusion.googleapis.com/namespaces.getIamPolicy`
  * `datafusion.googleapis.com/namespaces.list`
  * `datafusion.googleapis.com/namespaces.setIamPolicy`
  * `datafusion.googleapis.com/operations.*`

| None  
Cloud Key Management Service | 

  * `cloudkms.googleapis.com/*.*`

| 

  * `cloudkms.googleapis.com/locations.get`
  * `cloudkms.googleapis.com/locations.list`

  
Firebase Storage | 

  * `firebasestorage.googleapis.com/*.*`

| None  
Translation | 

  * `cloudtranslate.googleapis.com/*.*`

| 

  * `cloudtranslate.googleapis.com/custommodels.*`
  * `cloudtranslate.googleapis.com/translationmemories.*`

  
Cloud Workstations | 

  * `workstations.googleapis.com/*.*`

| None  
Confidential Computing | 

  * `confidentialcomputing.googleapis.com/*.*`

| None  
Google Cloud Contact Center as a Service | 

  * `contactcenteraiplatform.googleapis.com/*.*`

| None  
Database Migration Service | 

  * `datamigration.googleapis.com/*.*`

| 

  * `datamigration.googleapis.com/mappingrules.*`

  
Dataform | 

  * `dataform.googleapis.com/*.*`

| 

  * `dataform.googleapis.com/comments.*`
  * `dataform.googleapis.com/commentsnested.*`
  * `dataform.googleapis.com/commentthreads.*`
  * `dataform.googleapis.com/commentthreadsnested.*`

  
Datastream | 

  * `datastream.googleapis.com/*.*`

| None  
Infrastructure Manager | 

  * `config.googleapis.com/*.*`

| None  
Parallelstore | 

  * `parallelstore.googleapis.com/*.*`

| None  
Policy Simulator | 

  * `policysimulator.googleapis.com/*.*`

| None  
Secret Manager | 

  * `secretmanager.googleapis.com/*.*`

| None  
Serverless VPC Access | 

  * `vpcaccess.googleapis.com/*.*`

| None  
Service Usage | 

  * `serviceusage.googleapis.com/*.*`

| None  
Cloud Asset Inventory | 

  * `cloudasset.googleapis.com/*.*`

| None  
Kubernetes Metadata API | 

  * `kubernetesmetadata.googleapis.com/*.*`

| None  
Service Management | 

  * `servicemanagement.googleapis.com/consumers.getIamPolicy`
  * `servicemanagement.googleapis.com/consumers.setIamPolicy`
  * `servicemanagement.googleapis.com/services.create`
  * `servicemanagement.googleapis.com/services.delete`
  * `servicemanagement.googleapis.com/services.get`
  * `servicemanagement.googleapis.com/services.getIamPolicy`
  * `servicemanagement.googleapis.com/services.list`
  * `servicemanagement.googleapis.com/services.setIamPolicy`
  * `servicemanagement.googleapis.com/services.update`

| None  
Backup and Disaster Recovery | 

  * `backupdr.googleapis.com/backupPlanAssociations.create`
  * `backupdr.googleapis.com/backupPlanAssociations.createForAlloydbCluster`
  * `backupdr.googleapis.com/backupPlanAssociations.createForCloudSqlInstance`
  * `backupdr.googleapis.com/backupPlanAssociations.createForComputeDisk`
  * `backupdr.googleapis.com/backupPlanAssociations.createForComputeInstance`
  * `backupdr.googleapis.com/backupPlanAssociations.deleteForAlloydbCluster`
  * `backupdr.googleapis.com/backupPlanAssociations.deleteForCloudSqlInstance`
  * `backupdr.googleapis.com/backupPlanAssociations.deleteForComputeDisk`
  * `backupdr.googleapis.com/backupPlanAssociations.deleteForComputeInstance`
  * `backupdr.googleapis.com/backupPlanAssociations.fetchForAlloydbCluster`
  * `backupdr.googleapis.com/backupPlanAssociations.fetchForCloudSqlInstance`
  * `backupdr.googleapis.com/backupPlanAssociations.fetchForComputeDisk`
  * `backupdr.googleapis.com/backupPlanAssociations.fetchForComputeInstance`
  * `backupdr.googleapis.com/backupPlanAssociations.getForAlloydbCluster`
  * `backupdr.googleapis.com/backupPlanAssociations.getForCloudSqlInstance`
  * `backupdr.googleapis.com/backupPlanAssociations.getForComputeDisk`
  * `backupdr.googleapis.com/backupPlanAssociations.getForComputeInstance`
  * `backupdr.googleapis.com/backupPlanAssociations.list`
  * `backupdr.googleapis.com/backupPlanRevisions.*`
  * `backupdr.googleapis.com/backupPlans.*`
  * `backupdr.googleapis.com/backupVaults.*`
  * `backupdr.googleapis.com/bvbackups.*`
  * `backupdr.googleapis.com/bvdataSources.abandonBackup`
  * `backupdr.googleapis.com/bvdataSources.fetchAccessToken`
  * `backupdr.googleapis.com/bvdataSources.finalizeBackup`
  * `backupdr.googleapis.com/bvdataSources.get`
  * `backupdr.googleapis.com/bvdataSources.initiateBackup`
  * `backupdr.googleapis.com/bvdataSources.list`
  * `backupdr.googleapis.com/bvdataSources.remove`
  * `backupdr.googleapis.com/bvdataSources.setInternalStatus`
  * `backupdr.googleapis.com/bvdataSources.update`
  * `backupdr.googleapis.com/compute.*`
  * `backupdr.googleapis.com/dataSourceReferences.fetchForAlloydbCluster`
  * `backupdr.googleapis.com/dataSourceReferences.fetchForCloudSqlInstance`
  * `backupdr.googleapis.com/dataSourceReferences.fetchForFilestoreInstance`
  * `backupdr.googleapis.com/dataSourceReferences.list`
  * `backupdr.googleapis.com/locations.*`
  * `backupdr.googleapis.com/managementServers.create`
  * `backupdr.googleapis.com/managementServers.createConnection`
  * `backupdr.googleapis.com/managementServers.delete`
  * `backupdr.googleapis.com/managementServers.get`
  * `backupdr.googleapis.com/managementServers.getIamPolicy`
  * `backupdr.googleapis.com/managementServers.list`
  * `backupdr.googleapis.com/managementServers.setIamPolicy`
  * `backupdr.googleapis.com/managementServers.update`
  * `backupdr.googleapis.com/operations.*`
  * `backupdr.googleapis.com/serviceConfig.*`

| 

  * `backupdr.googleapis.com/bvbackups.useReadOnlyForAlloydbCluster`
  * `backupdr.googleapis.com/bvbackups.useReadOnlyForCloudSqlInstance`
  * `backupdr.googleapis.com/bvbackups.useReadOnlyForFilestoreInstance`

  
Sensitive Data Protection | 

  * `dlp.googleapis.com/charts.*`
  * `dlp.googleapis.com/columnDataProfiles.*`
  * `dlp.googleapis.com/connections.*`
  * `dlp.googleapis.com/deidentifyTemplates.*`
  * `dlp.googleapis.com/estimates.*`
  * `dlp.googleapis.com/fileStoreProfiles.*`
  * `dlp.googleapis.com/inspecttemplates.*`
  * `dlp.googleapis.com/jobTriggers.*`
  * `dlp.googleapis.com/jobs.*`
  * `dlp.googleapis.com/projectDataProfiles.*`
  * `dlp.googleapis.com/storedInfoTypes.*`
  * `dlp.googleapis.com/subscriptions.*`
  * `dlp.googleapis.com/tableDataProfiles.*`

| None  
Secure Source Manager | 

  * `securesourcemanager.googleapis.com/branchRules.*`
  * `securesourcemanager.googleapis.com/hooks.*`
  * `securesourcemanager.googleapis.com/instances.access`
  * `securesourcemanager.googleapis.com/instances.create`
  * `securesourcemanager.googleapis.com/instances.delete`
  * `securesourcemanager.googleapis.com/instances.get`
  * `securesourcemanager.googleapis.com/instances.getIamPolicy`
  * `securesourcemanager.googleapis.com/instances.linkDeveloperConnect`
  * `securesourcemanager.googleapis.com/instances.list`
  * `securesourcemanager.googleapis.com/instances.setIamPolicy`
  * `securesourcemanager.googleapis.com/issuecomments.*`
  * `securesourcemanager.googleapis.com/issues.*`
  * `securesourcemanager.googleapis.com/locations.*`
  * `securesourcemanager.googleapis.com/operations.*`
  * `securesourcemanager.googleapis.com/prcomments.*`
  * `securesourcemanager.googleapis.com/pullRequests.*`
  * `securesourcemanager.googleapis.com/repositories.create`
  * `securesourcemanager.googleapis.com/repositories.delete`
  * `securesourcemanager.googleapis.com/repositories.fetch`
  * `securesourcemanager.googleapis.com/repositories.get`
  * `securesourcemanager.googleapis.com/repositories.getIamPolicy`
  * `securesourcemanager.googleapis.com/repositories.list`
  * `securesourcemanager.googleapis.com/repositories.setIamPolicy`
  * `securesourcemanager.googleapis.com/repositories.update`

| None  
Connectors | 

  * `connectors.googleapis.com/*.*`

| 

  * `connectors.googleapis.com/connections.executeSqlQuery`
  * `connectors.googleapis.com/connections.generateOpenAPISpec`
  * `connectors.googleapis.com/connections.listenEvent`

  
Dataproc Metastore | 

  * `metastore.googleapis.com/backups.*`
  * `metastore.googleapis.com/databases.delete`
  * `metastore.googleapis.com/databases.getIamPolicy`
  * `metastore.googleapis.com/databases.setIamPolicy`
  * `metastore.googleapis.com/databases.update`
  * `metastore.googleapis.com/federations.*`
  * `metastore.googleapis.com/imports.*`
  * `metastore.googleapis.com/locations.*`
  * `metastore.googleapis.com/operations.*`
  * `metastore.googleapis.com/services.*`
  * `metastore.googleapis.com/tables.delete`
  * `metastore.googleapis.com/tables.getIamPolicy`
  * `metastore.googleapis.com/tables.setIamPolicy`
  * `metastore.googleapis.com/tables.update`

| 

  * `metastore.googleapis.com/federations.use`
  * `metastore.googleapis.com/services.use`

  
  
## Enforcement version `3`

Policies with enforcement version `3` can block all of the permissions listed in the following enforcement versions:

  * Enforcement version `1`
  * Enforcement version `2`



Additionally, policies with the enforcement version `3` can also block all of the permissions listed in the following table.

Each row contains the following information:

  * The name of a service with permissions that Principal Access Boundary policies can block.
  * The permissions for that service that Principal Access Boundary policies can block.

In some cases, a section of a permission name is replaced with a wildcard character (`*`). This format indicates that Principal Access Boundary policies can block all permissions that match that pattern.




Service | Permissions | Exceptions  
---|---|---  
Essential Contacts | 

  * `essentialcontacts.googleapis.com/contacts.*`

| None  
Identity and Access Management | 

  * `iam.googleapis.com/denypolicies.*`
  * `iam.googleapis.com/roles.*`
  * `iam.googleapis.com/serviceAccountKeys.*`
  * `iam.googleapis.com/serviceAccounts.*`

| 

  * `iam.googleapis.com/serviceAccounts.createTagBinding`
  * `iam.googleapis.com/serviceAccounts.deleteTagBinding`
  * `iam.googleapis.com/serviceAccounts.getCertificateAs`
  * `iam.googleapis.com/serviceAccounts.listEffectiveTags`
  * `iam.googleapis.com/serviceAccounts.listTagBindings`

  
Managed Service for Apache Spark | 

  * `dataproc.googleapis.com/autoscalingPolicies.*`
  * `dataproc.googleapis.com/batches.*`
  * `dataproc.googleapis.com/clusters.*`
  * `dataproc.googleapis.com/jobs.*`
  * `dataproc.googleapis.com/operations.*`
  * `dataproc.googleapis.com/sessionTemplates.*`
  * `dataproc.googleapis.com/sessions.*`
  * `dataproc.googleapis.com/workflowTemplates.*`

| None  
Service Management | 

  * `servicemanagement.googleapis.com/services.check`
  * `servicemanagement.googleapis.com/services.report`

| None  
Bigtable | 

  * `bigtable.googleapis.com/*.*`

| None  
Cloud Bigtable Admin API | 

  * `bigtableadmin.googleapis.com/*.*`

| None  
Cloud SQL | 

  * `cloudsql.googleapis.com/*.*`

| None  
Network Services | 

  * `networkservices.googleapis.com/endpointPolicies.*`
  * `networkservices.googleapis.com/gateways.*`
  * `networkservices.googleapis.com/grpcRoutes.*`
  * `networkservices.googleapis.com/httpRoutes.*`
  * `networkservices.googleapis.com/httpfilters.*`
  * `networkservices.googleapis.com/meshes.*`
  * `networkservices.googleapis.com/route_views.*`
  * `networkservices.googleapis.com/serviceBindings.*`
  * `networkservices.googleapis.com/serviceLbPolicies.*`
  * `networkservices.googleapis.com/tcpRoutes.*`
  * `networkservices.googleapis.com/tlsRoutes.*`

| None  
Cloud Service Mesh | 

  * `trafficdirector.googleapis.com/*.*`

| None  
Network Management API | 

  * `networkmanagement.googleapis.com/*.*`

| None  
Compute Engine | 

  * `compute.googleapis.com/addresses.*`
  * `compute.googleapis.com/backendBuckets.*`
  * `compute.googleapis.com/backendServices.*`
  * `compute.googleapis.com/externalVpnGateways.*`
  * `compute.googleapis.com/firewallPolicies.*`
  * `compute.googleapis.com/firewalls.*`
  * `compute.googleapis.com/forwardingRules.*`
  * `compute.googleapis.com/globalAddresses.*`
  * `compute.googleapis.com/globalForwardingRules.*`
  * `compute.googleapis.com/healthChecks.*`
  * `compute.googleapis.com/httpHealthChecks.*`
  * `compute.googleapis.com/httpsHealthChecks.*`
  * `compute.googleapis.com/interconnectAttachments.*`
  * `compute.googleapis.com/interconnectLocations.*`
  * `compute.googleapis.com/interconnectRemoteLocations.*`
  * `compute.googleapis.com/interconnects.*`
  * `compute.googleapis.com/networks.*`
  * `compute.googleapis.com/packetMirrorings.*`
  * `compute.googleapis.com/publicAdvertisedPrefixes.*`
  * `compute.googleapis.com/publicDelegatedPrefixes.*`
  * `compute.googleapis.com/regionBackendServices.*`
  * `compute.googleapis.com/regionFirewallPolicies.*`
  * `compute.googleapis.com/regionHealthChecks.*`
  * `compute.googleapis.com/regionSslPolicies.*`
  * `compute.googleapis.com/regionTargetHttpProxies.*`
  * `compute.googleapis.com/regionTargetTcpProxies.*`
  * `compute.googleapis.com/regionUrlMaps.*`
  * `compute.googleapis.com/routes.*`
  * `compute.googleapis.com/sslPolicies.*`
  * `compute.googleapis.com/subnetworks.*`
  * `compute.googleapis.com/targetGrpcProxies.*`
  * `compute.googleapis.com/targetHttpProxies.*`
  * `compute.googleapis.com/targetHttpsProxies.*`
  * `compute.googleapis.com/targetInstances.*`
  * `compute.googleapis.com/targetPools.*`
  * `compute.googleapis.com/targetSslProxies.*`
  * `compute.googleapis.com/targetTcpProxies.*`
  * `compute.googleapis.com/targetVpnGateways.*`
  * `compute.googleapis.com/urlMaps.*`
  * `compute.googleapis.com/vpnGateways.*`

| None  
Artifact Registry | 

  * `artifactregistry.googleapis.com/*.*`

| None  
Pub/Sub | 

  * `pubsub.googleapis.com/*.*`

| None  
Workflows | 

  * `workflows.googleapis.com/*.*`

| None  
Google Distributed Cloud | 

  * `gkeonprem.googleapis.com/*.*`

| None  
API Keys | 

  * `apikeys.googleapis.com/apikeys.*` **Note:** In the IAM v1 API, these permissions are named `serviceusage.apiKeys.*`. 
  * `apikeys.googleapis.com/keys.*`

| None  
Cloud DNS | 

  * `dns.googleapis.com/*.*`

| None  
Firestore | 

  * `datastore.googleapis.com/backupSchedules.*`
  * `datastore.googleapis.com/backups.delete`
  * `datastore.googleapis.com/backups.get`
  * `datastore.googleapis.com/backups.list`
  * `datastore.googleapis.com/databases.*`
  * `datastore.googleapis.com/entities.*`
  * `datastore.googleapis.com/indexes.*`
  * `datastore.googleapis.com/locations.*`
  * `datastore.googleapis.com/operations.*`
  * `datastore.googleapis.com/userCreds.*`

| None  
Cloud Key Management Service | 

  * `cloudkms.googleapis.com/autokeyConfigs.*`
  * `cloudkms.googleapis.com/cryptoKeyVersions.create`
  * `cloudkms.googleapis.com/cryptoKeyVersions.destroy`
  * `cloudkms.googleapis.com/cryptoKeyVersions.get`
  * `cloudkms.googleapis.com/cryptoKeyVersions.list`
  * `cloudkms.googleapis.com/cryptoKeyVersions.restore`
  * `cloudkms.googleapis.com/cryptoKeyVersions.update`
  * `cloudkms.googleapis.com/cryptoKeyVersions.useToDecrypt`
  * `cloudkms.googleapis.com/cryptoKeyVersions.useToEncrypt`
  * `cloudkms.googleapis.com/cryptoKeyVersions.useToSign`
  * `cloudkms.googleapis.com/cryptoKeyVersions.useToVerify`
  * `cloudkms.googleapis.com/cryptoKeyVersions.viewPublicKey`
  * `cloudkms.googleapis.com/ekmConfigs.*`
  * `cloudkms.googleapis.com/importJobs.*`
  * `cloudkms.googleapis.com/keyHandles.*`
  * `cloudkms.googleapis.com/keyRings.*`

| 

  * `cloudkms.googleapis.com/importJobs.useToImport`

  
Organization Policy Service | 

  * `orgpolicy.googleapis.com/*.*`

| None  
Knowledge Catalog | 

  * `dataplex.googleapis.com/aspectTypes.*`
  * `dataplex.googleapis.com/datascans.*`
  * `dataplex.googleapis.com/entries.*`
  * `dataplex.googleapis.com/entryGroups.create`
  * `dataplex.googleapis.com/entryGroups.delete`
  * `dataplex.googleapis.com/entryGroups.get`
  * `dataplex.googleapis.com/entryGroups.getIamPolicy`
  * `dataplex.googleapis.com/entryGroups.import`
  * `dataplex.googleapis.com/entryGroups.list`
  * `dataplex.googleapis.com/entryGroups.setIamPolicy`
  * `dataplex.googleapis.com/entryGroups.update`
  * `dataplex.googleapis.com/entryGroups.useContactsAspect`
  * `dataplex.googleapis.com/entryGroups.useGenericAspect`
  * `dataplex.googleapis.com/entryGroups.useGenericEntry`
  * `dataplex.googleapis.com/entryGroups.useOverviewAspect`
  * `dataplex.googleapis.com/entryGroups.useSchemaAspect`
  * `dataplex.googleapis.com/entryTypes.*`
  * `dataplex.googleapis.com/metadataJobs.*`

| None  
Data Lineage API | 

  * `datalineage.googleapis.com/events.*`
  * `datalineage.googleapis.com/locations.*`
  * `datalineage.googleapis.com/operations.*`
  * `datalineage.googleapis.com/processes.*`
  * `datalineage.googleapis.com/runs.*`

| None  
GKE Hub | 

  * `gkehub.googleapis.com/fleets.*`

| None  
Cloud Run functions | 

  * `cloudfunctions.googleapis.com/*.*`

| None  
Spanner | 

  * `spanner.googleapis.com/*.*`

| None  
Google Kubernetes Engine | 

  * `container.googleapis.com/*.*`

| None  
  
## Enforcement version `2`

Policies with enforcement version `2` can block all of the permissions listed in Enforcement version `1`. Additionally, policies with the enforcement version `2` can also block all of the permissions listed in the following table.

Each row contains the following information:

  * The name of a service with permissions that Principal Access Boundary policies can block.
  * The permissions for that service that Principal Access Boundary policies can block.

In some cases, a section of a permission name is replaced with a wildcard character (`*`). This format indicates that Principal Access Boundary policies can block all permissions that match that pattern.


Service | Permissions | Exceptions  
---|---|---  
Access Context Manager | 

  * `accesscontextmanager.googleapis.com/*`

| None  
Artifact Analysis | 

  * `containeranalysis.googleapis.com/*`

| None  
BigQuery | 

  * `bigquery.googleapis.com/rowAccessPolicies.*`
  * `bigquery.googleapis.com/datasets.*`
  * `bigquery.googleapis.com/jobs.*`
  * `bigquery.googleapis.com/models.*`
  * `bigquery.googleapis.com/routines.*`
  * `bigquery.googleapis.com/tables.*`

| None  
BigQuery Data Policy | 

  * `bigquerydatapolicy.googleapis.com/*`

| None  
BigQuery Data Transfer Service | 

  * `bigquerydatatransfer.googleapis.com/transfers.*`

| None  
Chrome Enterprise Premium | 

  * `beyondcorp.googleapis.com/*`

| None  
Cloud Asset Inventory | 

  * `cloudasset.googleapis.com/*`

| None  
Cloud Billing | 

  * `billing.googleapis.com/budgets.*`

| None  
Cloud Build | 

  * `cloudbuild.googleapis.com/*`

| None  
Cloud Monitoring | 

  * `monitoring.googleapis.com/*`

| 

  * `monitoring.googleapis.com/metricsScopes.link`
  * `monitoring.googleapis.com/timeSeries.list`

  
Cloud Service Mesh | 

  * `meshconfig.googleapis.com/*`

| None  
Cloud Storage | 

  * `storage.googleapis.com/bucketOperations.*`
  * `storage.googleapis.com/buckets.*`
  * `storage.googleapis.com/managedFolders.*`
  * `storage.googleapis.com/multipartUploads.*`
  * `storage.googleapis.com/folders.*`
  * `storage.googleapis.com/hmacKeys.*`
  * `storage.googleapis.com/objects.*`

| None  
Cloud Trace | 

  * `cloudtrace.googleapis.com/*`

| None  
Compute Engine | 

  * `compute.googleapis.com/networkAttachments.*`
  * `compute.googleapis.com/networkEdgeSecurityServices.*`
  * `compute.googleapis.com/regionSecurityPolicies.*`
  * `compute.googleapis.com/securityPolicies.*`
  * `compute.googleapis.com/serviceAttachments.*`
  * `compute.googleapis.com/routers.*`

| None  
Firebase Security Rules | 

  * `firebaserules.googleapis.com/*`

| None  
GKE Multi-Cloud | 

  * `gkemulticloud.googleapis.com/*`

| None  
Identity-Aware Proxy | 

  * `iap.googleapis.com/*`

| None  
Memorystore for Redis | 

  * `redis.googleapis.com/*`

| None  
Network Management API | 

  * `networkmanagement.googleapis.com/*`

| None  
Network Services | 

  * `networkservices.googleapis.com/edgeCacheKeysets.*`
  * `networkservices.googleapis.com/edgeCacheOrigins.*`
  * `networkservices.googleapis.com/edgeCacheServices.*`

| None  
Google Cloud Fraud Defense | 

  * `recaptchaenterprise.googleapis.com/*`

| None  
Resource Manager | 

  * `cloudresourcemanager.googleapis.com/*`

| 

  * `cloudresourcemanager.googleapis.com/*.createPolicyBinding`
  * `cloudresourcemanager.googleapis.com/*.deletePolicyBinding`
  * `cloudresourcemanager.googleapis.com/*.searchPolicyBindings`
  * `cloudresourcemanager.googleapis.com/*.updatePolicyBinding`

  
Video Stitcher API | 

  * `videostitcher.googleapis.com/*`

| None  
  
## Enforcement version `1`

The following table lists the permissions that Principal Access Boundary policies with enforcement version `1` can block.

Each row contains the following information:

  * The name of a service with permissions that Principal Access Boundary policies can block.
  * The permissions for that service that Principal Access Boundary policies can block.

In some cases, a section of a permission name is replaced with a wildcard character (`*`). This format indicates that Principal Access Boundary policies can block all permissions that match that pattern.

  * The permissions for the service that Principal Access Boundary can't block, even if those permissions match one of the supported permission patterns.


Service | Permissions | Exceptions  
---|---|---  
Access Approval | 

  * `accessapproval.googleapis.com/requests.list`
  * `accessapproval.googleapis.com/serviceaccounts.get`
  * `accessapproval.googleapis.com/settings.*`

|  None   
Access Context Manager | 

  * `accesscontextmanager.googleapis.com/*`

| 

  * `accesscontextmanager.googleapis.com/gcpUserAccessBindings.*`

  
BigQuery | 

  * `bigquery.googleapis.com/datasets.create`
  * `bigquery.googleapis.com/datasets.delete`
  * `bigquery.googleapis.com/datasets.get`
  * `bigquery.googleapis.com/datasets.setIamPolicy`
  * `bigquery.googleapis.com/datasets.update`
  * `bigquery.googleapis.com/jobs.create`
  * `bigquery.googleapis.com/jobs.delete`
  * `bigquery.googleapis.com/jobs.list`
  * `bigquery.googleapis.com/jobs.get`
  * `bigquery.googleapis.com/models.create`
  * `bigquery.googleapis.com/models.delete`
  * `bigquery.googleapis.com/models.list`
  * `bigquery.googleapis.com/models.updateMetadata`
  * `bigquery.googleapis.com/routines.create`
  * `bigquery.googleapis.com/routines.delete`
  * `bigquery.googleapis.com/routines.list`
  * `bigquery.googleapis.com/routines.update`

| None  
Binary Authorization | 

  * `binaryauthorization.googleapis.com/*`

| None  
Cloud Logging | 

  * `logging.googleapis.com/logEntries.create`
  * `logging.googleapis.com/logMetrics.*`

| None  
Cloud Run | 

  * `run.googleapis.com/authorizeddomains.*`
  * `run.googleapis.com/configurations.get`
  * `run.googleapis.com/configurations.list`
  * `run.googleapis.com/domainmappings.*`
  * `run.googleapis.com/services.create`
  * `run.googleapis.com/services.delete`
  * `run.googleapis.com/services.get`
  * `run.googleapis.com/services.list`
  * `run.googleapis.com/services.update`
  * `run.googleapis.com/executions.*`
  * `run.googleapis.com/jobs.create`
  * `run.googleapis.com/jobs.delete`
  * `run.googleapis.com/jobs.get`
  * `run.googleapis.com/jobs.list`
  * `run.googleapis.com/jobs.run`
  * `run.googleapis.com/revisions.*`
  * `run.googleapis.com/routes.get`
  * `run.googleapis.com/routes.list`
  * `run.googleapis.com/tasks.*`

| None  
Cloud Storage | 

  * `storage.googleapis.com/buckets.get`
  * `storage.googleapis.com/buckets.getIamPolicy`
  * `storage.googleapis.com/buckets.list`
  * `storage.googleapis.com/buckets.setIamPolicy`
  * `storage.googleapis.com/buckets.update`
  * `storage.googleapis.com/hmacKeys.update`
  * `storage.googleapis.com/objects.delete`
  * `storage.googleapis.com/objects.get`
  * `storage.googleapis.com/objects.setRetention`

| None  
Dataflow | 

  * `dataflow.googleapis.com/messages.list`
  * `dataflow.googleapis.com/metrics.get`
  * `dataflow.googleapis.com/snapshots.list`
  * `dataflow.googleapis.com/workItems.*`
  * `dataflow.googleapis.com/jobs.*`

| 

  * `dataflow.googleapis.com/jobs.snapshot`

  
Firestore | 

  * `datastore.googleapis.com/databases.create`
  * `datastore.googleapis.com/databases.delete`
  * `datastore.googleapis.com/databases.get`
  * `datastore.googleapis.com/databases.getMetadata`
  * `datastore.googleapis.com/databases.list`

| None  
Firebase Security Rules | 

  * `firebaserules.googleapis.com/*`

| None  
GKE Hub | 

  * `gkehub.googleapis.com/membershipbindings.*`
  * `gkehub.googleapis.com/rbacrolebindings.*`
  * `gkehub.googleapis.com/features.*`
  * `gkehub.googleapis.com/fleet.create`
  * `gkehub.googleapis.com/fleet.get`
  * `gkehub.googleapis.com/fleet.patch`
  * `gkehub.googleapis.com/locations.*`
  * `gkehub.googleapis.com/memberships.*`
  * `gkehub.googleapis.com/scopes.*`

| 

  * `gkehub.googleapis.com/*.createTagBinding`
  * `gkehub.googleapis.com/*.deleteTagBinding`
  * `gkehub.googleapis.com/*.listEffectiveTags`
  * `gkehub.googleapis.com/*.listTagBindings`

  
Pub/Sub | 

  * `pubsub.googleapis.com/*`

| 

  * `pubsub.googleapis.com/*.getIamPolicy`
  * `pubsub.googleapis.com/*.setIamPolicy`
  * `pubsub.googleapis.com/schemas.delete`
  * `pubsub.googleapis.com/schemas.validate`
  * `pubsub.googleapis.com/subscriptions.consume`

  
Memorystore for Redis | 

  * `redis.googleapis.com/instances.create`
  * `redis.googleapis.com/instances.delete`
  * `redis.googleapis.com/instances.failover`
  * `redis.googleapis.com/instances.get`
  * `redis.googleapis.com/instances.getAuthString`
  * `redis.googleapis.com/instances.list`
  * `redis.googleapis.com/instances.update`
  * `redis.googleapis.com/instances.upgrade`

| None  
Gemini Enterprise Agent Platform | 

  * `aiplatform.googleapis.com/*`

| 

  * `aiplatform.googleapis.com/operations.*`

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
