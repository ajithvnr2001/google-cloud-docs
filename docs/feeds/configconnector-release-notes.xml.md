---
url: https://docs.cloud.google.com/feeds/configconnector-release-notes.xml
title: Config Connector - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:40:21.742702+00:00
---

# Config Connector - Release notes

> Source: https://docs.cloud.google.com/feeds/configconnector-release-notes.xml

tag:google.com,2016:configconnector-release-notesConfig Connector - Release notesGoogle Cloud Platform2026-10-06T00:00:00-07:00October 06, 2026tag:google.com,2016:configconnector-release-notes#October_06_20262026-10-06T00:00:00-07:00Announcement 

Config Connector version 1.158.0 is now available.

### Feature

New Alpha Resources (Direct Reconciler):

  * `AgentRegistryBinding`

    * Manage [Agent Registry bindings](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings) to connect agent tools and authentication configurations.
  * `AIPlatformPersistentResource`

    * Manage [Vertex AI Persistent Resources](https://cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.persistentResources) for cluster computing and training jobs.
  * `AssuredWorkloadsWorkload`

    * Manage [Assured Workloads](https://cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads) to enforce security and compliance controls for regulated workloads.
  * `BigtableSchemaBundle`

    * Manage [Bigtable schema bundles](https://cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.tables.schemaBundles) for storing protocol buffer (protobuf) schemas in Bigtable.
  * `CloudNumberRegistryRegistryBook`

    * Manage [Cloud Number Registry registry books](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks) to organize IP address management (IPAM) information and discovered IP address ranges.
  * `EventarcMessageBus`

    * Manage [Eventarc message buses](https://cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.messageBuses) to route events from publishers to subscribers.
  * `ModelArmorFloorSetting`

    * Manage [Model Armor floor settings](https://docs.cloud.google.com/model-armor/reference/rest/v1/FloorSetting) at project, folder, or organization scope to enforce baseline safety and security filters for LLMs.



### Feature

New Fields:

  * [`BackupDRBackupPlanAssociation`](https://cloud.google.com/config-connector/docs/reference/resource-docs/backupdr/backupdrbackupplanassociation)

    * Added `spec.resource.sqlInstanceRef` field to support backing up Cloud SQL instances.
  * `ComputeNetworkFirewallPolicyRule`

    * Added `spec.match.srcNetworkContext` and `spec.match.destNetworkContext` fields.
  * [`ComputeRegionNetworkEndpointGroup`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computeregionnetworkendpointgroup)

    * Added `INTERNET_IP_PORT`, `INTERNET_FQDN_PORT`, and `GCE_VM_IP_PORTMAP` values for `spec.networkEndpointType`.
  * [`RedisCluster`](https://cloud.google.com/config-connector/docs/reference/resource-docs/redis/rediscluster)

    * Added `spec.clusterEndpoints` and `status.clusterEndpoints` fields.
    * Added `spec.gcsSource` field.
    * Added `spec.managedBackupSource` field.
  * [`SQLInstance`](https://cloud.google.com/config-connector/docs/reference/resource-docs/sql/sqlinstance)

    * Added `spec.settings.databaseReplicationEnabled` field.



### Feature

New Features:

  * Added support for pausing and unpausing actuation at the individual resource level by using the `cnrm.cloud.google.com/actuation-mode` annotation.



### Change

Reconciliation Improvements:

Added support for direct reconciliation to more resources, with opt-in behavior. The API is unchanged. To use the direct reconciler, add the `alpha.cnrm.cloud.google.com/reconciler: direct` annotation to the corresponding Config Connector object. The following resources now have direct reconciliation support:

  * [`FilestoreInstance`](https://cloud.google.com/config-connector/docs/reference/resource-docs/filestore/filestoreinstance)
    * Added support for direct reconciliation (opt-in).



### Fixed

Bug Fixes:

  * [`BigQueryDataset`](https://cloud.google.com/config-connector/docs/reference/resource-docs/bigquery/bigquerydataset) ([#12383](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12383))

    * Fixed a reconciliation failure in projects with a project ID that contains a colon (such as domain-scoped projects `example.com:my-project`), where creation previously failed with an invalid ID format error and `resourceID` and `selfLink` were not populated.
  * [`ComposerEnvironment`](https://cloud.google.com/config-connector/docs/reference/resource-docs/composer/composerenvironment) ([#12795](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12795))

    * Fixed infinite reconciliation loops, false drift, and HTTP 400 errors when using empty map fields (`envVariables: {}`, `labels: {}`), partial `workloadsConfig` blocks, or disabling `scheduledSnapshotsConfig`.
  * [`ComputeRouterNAT`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computerouternat) ([#12813](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12813))

    * Fixed reference validation and resolution in the direct controller so that `spec.routerRef` accepts both short router names and canonical long paths.
  * Removed empty `status.observedState` fields from `v1alpha1` CRDs to align with Kubernetes structural schema requirements ([#12627](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12627)).


]]> September 23, 2026tag:google.com,2016:configconnector-release-notes#September_23_20262026-09-23T00:00:00-07:00Announcement 

Config Connector version 1.157.0 is now available.

### Feature

New Alpha Resources (Direct Reconciler):

  * `AIPlatformModel`

    * Manage [Vertex AI models](https://cloud.google.com/vertex-ai/docs/model-registry/introduction).
  * `APIHubExternalAPI`

    * Manage [API Hub external APIs](https://cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.externalApis).
  * `NotebookInstanceV2`

    * Manage [Agent Platform Workbench instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances).
  * `RedisClusterEndpoint`

    * Manage [Memorystore for Redis Cluster endpoints](https://cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#ClusterEndpoint).



### Feature

New Fields:

  * `NetworkServicesEdgeCacheService`
    * Added `routeMethods` and `compressionMode` support.



### Fixed

Bug Fixes:

  * [`NetworkConnectivityInternalRange`](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12615)
    * Fixed continuous reconciliation loop and 400 error on `NetworkConnectivityInternalRange` when auto-allocation fields are set.



### Change

Other:

  * **BeyondCorpClientGateway** : Removed support for the deprecated BeyondCorp Enterprise client connector.

]]> September 08, 2026tag:google.com,2016:configconnector-release-notes#September_08_20262026-09-08T00:00:00-07:00Announcement 

Config Connector version 1.156.0 is now available.

### Feature

New Alpha Resources (Direct Reconciler):

  * `CCInsightsQAScorecard`

    * Manage [Contact Center Insights QA scorecards](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.qaScorecards) to manage and evaluate agent performance.
  * `ContentWarehouseSynonymSet`

    * Manage [Document AI Warehouse Synonym Sets](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.synonymSets) to manage custom synonym groups for searches.
  * `DevConnectAccountConnector`

    * Manage [Developer Connect Account Connectors](https://cloud.google.com/developer-connect/docs) to connect GKE clusters to developer systems.
  * `DiscoveryEngineEngine`

    * Manage [Discovery Engine search engines](https://cloud.google.com/generative-ai-app-builder/docs) to power search experiences.
  * `DiscoveryEngineServingConfig`

    * Manage [Discovery Engine serving configurations](https://cloud.google.com/generative-ai-app-builder/docs) to control search, recommendation, and listing features.
  * `GKEHubFleet`

    * Manage [GKE Hub Fleets](https://cloud.google.com/kubernetes-engine/fleet-management/docs) to logically group and manage clusters.
  * `ModelArmorTemplate`

    * Manage [Model Armor templates](https://docs.cloud.google.com/model-armor/manage-templates) to define safety and security policies for large language models.
  * `NetworkSecurityAuthzPolicy`

    * Manage [Network Security Authorization Policies](https://cloud.google.com/service-mesh/docs/tutorials/authz) to authorize traffic.
  * `RapidMigrationAssessmentCollector`

    * Manage [Rapid Migration Assessment collectors](https://cloud.google.com/migration-center/docs) to gather environment discovery data for cloud migration.
  * `SecurityCenterManagementEventThreatDetectionCustomModule`

    * Manage [Security Command Center event threat detection custom modules](https://cloud.google.com/security-command-center/docs) to customize threat detection.
  * `StorageInsightsDatasetConfig`

    * Manage [Cloud Storage Insights dataset configurations](https://docs.cloud.google.com/storage/docs/insights/datasets) to automatically inventory and analyze storage datasets.
  * `VectorSearchCollection`

    * Manage [Vertex AI Vector Search collections](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview) to manage similarity search indexes.



### Feature

New Fields:

  * [`BigtableTable`](https://cloud.google.com/config-connector/docs/reference/resource-docs/bigtable/bigtabletable)

    * Added `spec.automatedBackupPolicy.locations` field.
  * [`ContainerCluster`](https://cloud.google.com/config-connector/docs/reference/resource-docs/container/containercluster)

    * Added `spec.nodeConfig.swapConfig` field.
  * [`ContainerNodePool`](https://cloud.google.com/config-connector/docs/reference/resource-docs/container/containernodepool)

    * Added `spec.nodeConfig.swapConfig` field.
  * [`DataprocCluster`](https://cloud.google.com/config-connector/docs/reference/resource-docs/dataproc/dataproccluster)

    * Added `spec.secondaryWorkerConfig.instanceFlexibilityPolicy` field.
  * `NetworkSecurityFirewallEndpoint`

    * Added `spec.organizationRef` field to support organizing resources at the organization level, and made `spec.projectRef` optional.



### Feature

New Features:

  * **Optional NAT IP Allocate Option** : Made `natIpAllocateOption` an optional field in `ComputeRouterNat` to support dynamic allocation.
  * **Preview Summary CLI Improvements** : Added namespace and current status to the preview summary report.



### Change

Reconciliation Improvements:

We have added support for direct reconciliation to more resources, with opt-in behavior. The API is unchanged. To use the direct reconciler, add the `alpha.cnrm.cloud.google.com/reconciler: direct` annotation to the corresponding Config Connector object. The following resources now have direct reconciliation support:

  * `VertexAITensorboard`
    * Support direct reconciliation (opt-in).

]]> August 20, 2026tag:google.com,2016:configconnector-release-notes#August_20_20262026-08-20T00:00:00-07:00Announcement 

Config Connector version 1.155.1 is now available.

### Feature

New Beta Resources (Direct Reconciler):

  * `DiscoveryEngineLicenseConfig`

    * Manage [Discovery Engine license configurations](https://cloud.google.com/generative-ai-app-builder/docs) to manage application licenses.
  * `StorageManagedFolder`

    * Manage [Google Cloud Storage managed folders](https://cloud.google.com/storage/docs/managed-folders) to apply granular access control policies to subsets of storage objects.
  * `VertexAITensorboardExperiment`

    * Manage [Vertex AI Tensorboard experiments](https://cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/tensorboard-introduction) to organize and track runs.



### Feature

New Fields:

  * [`BigtableTable`](https://cloud.google.com/config-connector/docs/reference/resource-docs/bigtable/bigtabletable)

    * Added `spec.automatedBackupPolicy` field.
  * [`CertificateManagerDNSAuthorization`](https://cloud.google.com/config-connector/docs/reference/resource-docs/certificatemanager/certificatemanagerdnsauthorization)

    * Added `spec.type` field.
  * [`ComputeForwardingRule`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computeforwardingrule)

    * Added `spec.target.redisClusterServiceAttachment` field.
  * [`ComputeURLMap`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computeurlmap)

    * Added `spec.tests[].expectedOutputURL` field.
    * Added `spec.tests[].expectedRedirectResponseCode` field.
  * [`ContainerCluster`](https://cloud.google.com/config-connector/docs/reference/resource-docs/container/containercluster)

    * Added `spec.nodeConfig.kubeletConfig.imageGcLowThresholdPercent` field.
    * Added `spec.nodeConfig.kubeletConfig.imageGcHighThresholdPercent` field.
    * Added `spec.nodeConfig.kubeletConfig.imageMinimumGcAge` field.
    * Added `spec.nodeConfig.kubeletConfig.imageMaximumGcAge` field.
    * Added `spec.nodeConfig.containerdConfig` field.
    * Added `spec.inTransitEncryptionConfig` field.
    * Added `spec.disableL4LbFirewallReconciliation` field.
    * Added `spec.nodeConfig.resourceManagerTags` field.
    * Added `spec.nodePoolAutoConfig.resourceManagerTags` field.
  * [`ContainerNodePool`](https://cloud.google.com/config-connector/docs/reference/resource-docs/container/containernodepool)

    * Added `spec.nodeConfig.kubeletConfig.imageGcLowThresholdPercent` field.
    * Added `spec.nodeConfig.kubeletConfig.imageGcHighThresholdPercent` field.
    * Added `spec.nodeConfig.kubeletConfig.imageMinimumGcAge` field.
    * Added `spec.nodeConfig.kubeletConfig.imageMaximumGcAge` field.
    * Added `spec.nodeConfig.containerdConfig` field.
    * Added `spec.nodeConfig.resourceManagerTags` field.
  * [`StorageBucket`](https://cloud.google.com/config-connector/docs/reference/resource-docs/storage/storagebucket)

    * Added `spec.autoclass.terminalStorageClass` field.
    * Added `status.observedState.storageClass` field.



### Feature

New Features:

  * **Configurable metrics server address** : Made the manager's built-in metrics server bind address configurable.
  * **Brownfield state comparison** : Added a generic helper function to compare desired and actual states in brownfield resources, improving reconciliation reliability.
  * **Irregular shortname pluralization** : Added support for irregular shortname pluralization of "corpus" to "corpora".



### Change

Reconciliation Improvements:

We have added support for direct reconciliation to more resources, with opt-in behavior. The API is unchanged. To use the direct reconciler, add the `alpha.cnrm.cloud.google.com/reconciler: direct` annotation to the corresponding Config Connector object. This release note was edited on October 2, 2026.

  * [`NetworkServicesHTTPRoute`](https://cloud.google.com/config-connector/docs/reference/resource-docs/networkservices/networkserviceshttproute)
    * Support direct reconciliation (opt-in).



### Fixed

Bug Fixes:

  * [`ComposerEnvironment`](https://cloud.google.com/config-connector/docs/reference/resource-docs/composer/composerenvironment)

    * Improved reconciliation, diffing, and update logic for `ComposerEnvironment` in the direct reconciler. ([GitHub PR #12364](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12365))
    * Skip the update of a ComposerEnvironment when the state of the underlying Google Cloud Composer environment is not RUNNING. ([GitHub PR #12365](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/12365))
  * [`ComputeReservation`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computereservation)

    * Ignore diff for `specificReservation.inUseCount` to prevent infinite/unwanted reconciliations.
  * [`RedisInstance`](https://cloud.google.com/config-connector/docs/reference/resource-docs/redis/redisinstance)

    * Marked `MaintenanceSchedule` field as output only to align with GCP's behavior.
  * [`SQLInstance`](https://cloud.google.com/config-connector/docs/reference/resource-docs/sql/sqlinstance)

    * Fixed legacy fuzzer roundtrip mismatch for `PscAutoConnectionPolicyEnabled`.
  * `CloudFunctions2Function`

    * Declared source fields mutable-but-unreadable to avoid spurious diffs.

]]> July 30, 2026tag:google.com,2016:configconnector-release-notes#July_30_20262026-07-30T00:00:00-07:00Announcement 

Config Connector version 1.154.1 is now available.

### Feature

New Alpha Resources (Direct Reconciler):

  * `ApigeeApiProduct`
    * Manage [Apigee API products](https://cloud.google.com/apigee/docs/api-platform/publish/what-api-product) to bundle APIs and make them available to developers.
  * `ApigeeRegistryApi`
    * Manage [Apigee Registry APIs](https://cloud.google.com/apigee/docs/apihub/what-is-api-hub) to catalog and manage APIs.
  * `ApigeeRegistryArtifact`
    * Manage [Apigee Registry artifacts](https://cloud.google.com/apigee/docs/apihub/what-is-api-hub) associated with APIs, versions, or specs.
  * `APIHubExternalAPI`
    * Manage [API Hub external APIs](https://cloud.google.com/apigee/docs/apihub/what-is-api-hub) to track APIs hosted outside of Google Cloud.
  * `APIHubInstance`
    * Manage [API Hub instances](https://cloud.google.com/apigee/docs/apihub/what-is-api-hub) to enable enterprise API management.
  * `AppOptimizeReport`
    * Manage [App Hub Optimize reports](https://cloud.google.com/app-hub/docs/overview).
  * `ArtifactRegistryVPCSCConfig`
    * Manage [Artifact Registry VPC Service Controls configurations](https://cloud.google.com/artifact-registry/docs/securing-with-vpc-sc) to secure repository access.
  * `BigQueryMigrationMigrationWorkflow`
    * Manage [BigQuery Migration workflows](https://cloud.google.com/bigquery/docs/migration-intro) to orchestrate data migration to BigQuery.
  * `BlockchainNodeEngineBlockchainNode`
    * Manage [Blockchain Node Engine blockchain nodes](https://cloud.google.com/blockchain-node-engine/docs) to deploy and manage dedicated blockchain nodes.
  * `CCInsightsConversation`
    * Manage [Contact Center Insights conversations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations) to analyze customer interactions.
  * `CCInsightsIssueModel`
    * Manage [Contact Center Insights issue models](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels) to categorize conversation topics.
  * `CCInsightsPhraseMatcher`
    * Manage [Contact Center Insights phrase matchers](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.phraseMatchers) to detect specific phrases in conversations.
  * `CESApp`
    * Manage [Consumer Experience Suite (CES) applications](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio).
  * `CloudBuildConnection`
    * Manage [Cloud Build 2nd gen connections](https://cloud.google.com/build/docs/automating-builds/github/connect-repo-github) to integrate external source repositories.
  * `CloudSecurityComplianceFramework`
    * Manage [Cloud Security Compliance frameworks](https://cloud.google.com/security-command-center/docs/compliance-manager-overview).
  * `ConnectorsConnection`
    * Manage [Integration Connectors connections](https://cloud.google.com/integration-connectors/docs) to connect to SaaS, databases, and enterprise systems.
  * `ContentWarehouseDocument`
    * Manage [Document AI Warehouse documents](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.documents).
  * `ContentWarehouseRuleSet`
    * Manage [Document AI Warehouse rule sets](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.ruleSets) to enforce document policies.
  * `ContentWarehouseSynonymSet`
    * Manage [Document AI Warehouse synonym sets](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.synonymSets) to expand search queries.
  * `DatabaseMigrationPrivateConnection`
    * Manage [Database Migration Service private connections](https://cloud.google.com/database-migration/docs) to securely connect source databases to Google Cloud.
  * `DataformFolder`
    * Manage [Dataform folders](https://cloud.google.com/dataform/docs) in Dataform repositories.
  * `DataformTeamFolder`
    * Manage [Dataform team folders](https://cloud.google.com/dataform/docs) to organize repository assets.
  * `DataLabelingDataset`
    * Manage [AI Platform Data Labeling datasets](https://cloud.google.com/ai-platform/data-labeling/docs) for annotating training data.
  * `DataLabelingEvaluationJob`
    * Manage [AI Platform Data Labeling evaluation jobs](https://cloud.google.com/ai-platform/data-labeling/docs) to assess model quality.
  * `DataLineageProcess`
    * Manage [Dataplex Data Lineage processes](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage) to track data origin and movement.
  * `DataplexAspectType`
    * Manage [Dataplex aspect types](https://cloud.google.com/dataplex/docs) to define metadata schemas.
  * `DataplexDataAttributeBinding`
    * Manage [Dataplex data attribute bindings](https://cloud.google.com/dataplex/docs) to map security and governance attributes to assets.
  * `DataplexDataScan`
    * Manage [Dataplex data scans](https://cloud.google.com/bigquery/docs/data-profile-scan) for data profiling and quality.
  * `DataplexDataTaxonomy`
    * Manage [Dataplex data taxonomies](https://cloud.google.com/dataplex/docs) to organize business metadata.
  * `DataplexGlossary`
    * Manage [Dataplex business glossaries](https://cloud.google.com/dataplex/docs) for consistent vocabulary.
  * `DataplexMetadataJob`
    * Manage [Dataplex metadata jobs](https://cloud.google.com/dataplex/docs) for metadata extraction.
  * `DevConnectConnection`
    * Manage [Developer Connect connections](https://cloud.google.com/developer-connect/docs) to securely link third-party Git hosts.
  * `DialogflowConversationDataset`
    * Manage [Dialogflow conversation datasets](https://cloud.google.com/dialogflow/cx/docs) for agent training.
  * `DialogflowSecuritySettings`
    * Manage [Dialogflow security settings](https://cloud.google.com/dialogflow/cx/docs) for data redaction and access control.
  * `DialogflowSipTrunk`
    * Manage [Dialogflow SIP trunks](https://cloud.google.com/dialogflow/cx/docs) for telecom integration.
  * `DiscoveryEngineControl`
    * Manage [Discovery Engine controls](https://cloud.google.com/generative-ai-app-builder/docs) to boost or filter search results.
  * `DiscoveryEngineSampleQuerySet`
    * Manage [Discovery Engine sample query sets](https://cloud.google.com/generative-ai-app-builder/docs) to evaluate search performance.
  * `DLPConnection`
    * Manage [Sensitive Data Protection (DLP) connections](https://cloud.google.com/sensitive-data-protection/docs).
  * `DLPDiscoveryConfig`
    * Manage [Sensitive Data Protection (DLP) discovery configurations](https://cloud.google.com/sensitive-data-protection/docs) for profiling data assets.
  * `EventarcGoogleApiSource`
    * Manage [Eventarc Google API sources](https://cloud.google.com/eventarc/docs) to configure event routing.
  * `GeminiDataAnalyticsConversation`
    * Manage [Gemini Data Analytics conversations](https://cloud.google.com/gemini/docs).
  * `GKEBackupBackupChannel`
    * Manage [Backup for GKE backup channels](https://cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke).
  * `LiveStreamAsset`
    * Manage [Live Stream assets](https://cloud.google.com/livestream/docs) for processing live video.
  * `ManagedKafkaConnectCluster`
    * Manage [Apache Kafka for BigQuery connections](https://cloud.google.com/managed-kafka/docs).
  * `MigrationCenterGroup`
    * Manage [Migration Center groups](https://cloud.google.com/migration-center/docs) to organize assets for migration assessment.
  * `NetworkSecurityAddressGroup`
    * Manage [Network Security address groups](https://cloud.google.com/firewall/docs/address-groups-firewall-policies) to define reusable network criteria.
  * `NetworkSecurityAuthzPolicy`
    * Manage [Network Security authorization policies](https://cloud.google.com/secure-web-proxy/docs) to secure network paths.
  * `NetworkSecurityFirewallEndpoint`
    * Manage [Network Security firewall endpoints](https://cloud.google.com/firewall/docs/about-firewall-endpoints) for Cloud Firewall Plus threat inspection.
  * `NetworkSecurityFirewallEndpointAssociation`
    * Manage [Network Security firewall endpoint associations](https://cloud.google.com/firewall/docs/about-firewall-endpoints) to apply threat inspection to networks.
  * `NetworkSecurityGatewaySecurityPolicy`
    * Manage [Network Security gateway security policies](https://cloud.google.com/secure-web-proxy/docs) for Secure Web Proxy configurations.
  * `NetworkSecurityPartnerSSEGateway`
    * Manage [Network Security partner Secure Service Edge (SSE) gateways](https://cloud.google.com/secure-web-proxy/docs).
  * `NetworkSecurityPartnerSSERealm`
    * Manage [Network Security partner Secure Service Edge (SSE) realms](https://cloud.google.com/secure-web-proxy/docs).
  * `NetworkSecuritySecurityProfile`
    * Manage [Network Security security profiles](https://cloud.google.com/firewall/docs/about-security-profiles) to group threat prevention policies.
  * `NetworkSecurityTLSInspectionPolicy`
    * Manage [Network Security TLS inspection policies](https://cloud.google.com/secure-web-proxy/docs/tls-inspection-overview) to inspect encrypted traffic.
  * `NetworkServicesAuthzExtension`
    * Manage [Network Services authorization extensions](https://cloud.google.com/service-extensions/docs) to integrate third-party callouts.
  * `NotebooksSchedule`
    * Manage [Vertex AI Workbench schedules](https://cloud.google.com/vertex-ai/docs/workbench) to run automated notebooks.
  * `RedisClusterEndpoint`
    * Manage [Google Cloud Memorystore for Redis Cluster endpoints](https://cloud.google.com/memorystore/docs/cluster).
  * `RunWorkerPool`
    * Manage [Cloud Run worker pools](https://cloud.google.com/run/docs) for long-running non-HTTP workloads.
  * `SaasServiceMgmtRelease`
    * Manage [SaaS Service Management releases](https://cloud.google.com/service-infrastructure/docs).
  * `SQLAdminBackup`
    * Manage [Cloud SQL backups](https://cloud.google.com/sql/docs) (read-only/reference representation).
  * `StorageInsightsDatasetConfig`
    * Manage [Storage Insights dataset configurations](https://cloud.google.com/storage/docs/insights/using-storage-insights) to generate storage inventories.
  * `TestingDeviceSession`
    * Manage [Firebase Test Lab device sessions](https://firebase.google.com/docs/test-lab).
  * `TranslateAdaptiveMtDataset`
    * Manage [Cloud Translation adaptive machine translation datasets](https://cloud.google.com/translate/docs/advanced/adaptive-translation).
  * `VectorSearchCollection`
    * Manage [Vertex AI Vector Search collections](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview).
  * `VertexAIFeatureGroup`
    * Manage [Vertex AI Feature Store feature groups](https://cloud.google.com/vertex-ai/docs/featurestore/overview) to organize features.
  * `VertexAIFeatureOnlineStore`
    * Manage [Vertex AI Feature Store feature online stores](https://cloud.google.com/vertex-ai/docs/featurestore/overview) for low-latency serving.
  * `VertexAIPipelineJob`
    * Manage [Vertex AI pipeline jobs](https://cloud.google.com/vertex-ai/docs/pipelines) to run machine learning pipelines.
  * `VertexAISpecialistPool`
    * Manage [Vertex AI specialist pools](https://cloud.google.com/vertex-ai/docs) for human labeling.
  * `VertexAIStudy`
    * Manage [Vertex AI Vizier studies](https://cloud.google.com/vertex-ai/docs/vizier) for hyperparameter tuning.
  * `VertexAITuningJob`
    * Manage [Vertex AI model tuning jobs](https://cloud.google.com/vertex-ai/docs) for model customization.
  * `VideoStitcherCDNKey`
    * Manage [Video Stitcher CDN keys](https://cloud.google.com/video-stitcher/docs) to authenticate to external CDNs.
  * `VisionProduct`
    * Manage [Cloud Vision products](https://cloud.google.com/vision/product-search/docs) for product search cataloging.
  * `VMwareEnginePrivateConnection`
    * Manage [VMware Engine private connections](https://cloud.google.com/vmware-engine/docs) to connect private clouds to other services.



### Feature

New Fields:

  * [`ComputeSubnetwork`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computesubnetwork)
    * Added `spec.reservedInternalRange` field.
  * `NetworkConnectivityInternalRange`
    * Added `spec.allocationOptions` field.
  * [`ComputeNetwork`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computenetwork)
    * Added `spec.networkProfile` field.
  * [`ComputeSecurityPolicy`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computesecuritypolicy)
    * Added `spec.region` field.
  * [`DNSRecordSet`](https://cloud.google.com/config-connector/docs/reference/resource-docs/dns/dnsrecordset)
    * Added support for routing policy `healthCheckRef` and `rrdatasRefs` fields.
  * [`ComputeAddress`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computeaddress)
    * Added `spec.ipCollection` field.
  * [`ComputeURLMap`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computeurlmap)
    * Added `spec.defaultCustomErrorResponsePolicy` field.
    * Added `spec.test[].expectedOutputUrl` and `spec.test[].expectedRedirectResponseCode` fields.
  * [`RedisCluster`](https://cloud.google.com/config-connector/docs/reference/resource-docs/redis/rediscluster)
    * Added `spec.crossClusterReplicationConfig` field.
  * [`MonitoringAlertPolicy`](https://cloud.google.com/config-connector/docs/reference/resource-docs/monitoring/monitoringalertpolicy)
    * Added `spec.conditions[].conditionSql` field (SQL Condition).
  * [`StorageBucket`](https://cloud.google.com/config-connector/docs/reference/resource-docs/storage/storagebucket)
    * Added `spec.ipFilter` field.
  * [`PubSubTopic`](https://cloud.google.com/config-connector/docs/reference/resource-docs/pubsub/pubsubtopic)
    * Added `spec.messageStoragePolicy.enforceInTransit` field.
  * [`ComputeRouterNAT`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computerouternat)
    * Added Private NAT feature support.



### Change

Reconciliation Improvements:

We have added support for direct reconciliation to more resources, with opt-in behaviour. The API is unchanged. To use the direct reconciler, add the `alpha.cnrm.cloud.google.com/reconciler: direct` annotation to the corresponding Config Connector object. This release note was edited on October 2, 2026.

  * `BigQueryReservationCapacityCommitment`
  * [`BigtableGCPolicy`](https://cloud.google.com/config-connector/docs/reference/resource-docs/bigtable/bigtablegcpolicy)
  * [`BillingBudgetsBudget`](https://cloud.google.com/config-connector/docs/reference/resource-docs/billingbudgets/billingbudgetsbudget)
  * [`CertificateManagerCertificateMap`](https://cloud.google.com/config-connector/docs/reference/resource-docs/certificatemanager/certificatemanagercertificatemap)
  * [`CertificateManagerCertificateMapEntry`](https://cloud.google.com/config-connector/docs/reference/resource-docs/certificatemanager/certificatemanagercertificatemapentry)
  * [`ComputeAddress`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computeaddress)
  * `ComputeAutoscaler`
  * `ComputeBackendServiceSignedURLKey`
  * [`ComputeDisk`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computedisk)
  * `ComputeDiskResourcePolicyAttachment`
  * [`ComputeExternalVPNGateway`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computeexternalvpngateway)
  * [`ComputeFirewall`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computefirewall)
  * [`ComputeFirewallPolicy`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computefirewallpolicy)
  * [`ComputeHTTPHealthCheck`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computehttphealthcheck)
  * [`ComputeHTTPSHealthCheck`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computehttpshealthcheck)
  * [`ComputeImage`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computeimage)
  * [`ComputeInstance`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computeinstance)
  * [`ComputeInstanceGroup`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computeinstancegroup)
  * [`ComputeInstanceGroupManager`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computeinstancegroupmanager)
  * [`ComputeNetwork`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computenetwork)
  * [`ComputeNodeTemplate`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computenodetemplate)
  * [`ComputeRoute`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computeroute)
  * [`ComputeRouter`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computerouter)
  * [`ComputeRouterInterface`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computerouterinterface)
  * [`ComputeRouterNAT`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computerouternat)
  * [`ComputeSSLPolicy`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computesslpolicy)
  * [`ComputeSecurityPolicy`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computesecuritypolicy)
  * [`ComputeTargetHTTPSProxy`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computetargethttpsproxy)
  * [`ComputeURLMap`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computeurlmap)
  * [`DataflowJob`](https://cloud.google.com/config-connector/docs/reference/resource-docs/dataflow/dataflowjob)
  * [`DataprocAutoscalingPolicy`](https://cloud.google.com/config-connector/docs/reference/resource-docs/dataproc/dataprocautoscalingpolicy)
  * [`DataprocCluster`](https://cloud.google.com/config-connector/docs/reference/resource-docs/dataproc/dataproccluster)
  * `DNSResponsePolicy`
  * [`KMSCryptoKey`](https://cloud.google.com/config-connector/docs/reference/resource-docs/kms/kmscryptokey)
  * [`KMSKeyRing`](https://cloud.google.com/config-connector/docs/reference/resource-docs/kms/kmskeyring)
  * [`LoggingLogExclusion`](https://cloud.google.com/config-connector/docs/reference/resource-docs/logging/logginglogexclusion)
  * [`MonitoringAlertPolicy`](https://cloud.google.com/config-connector/docs/reference/resource-docs/monitoring/monitoringalertpolicy)
  * [`NetworkServicesGateway`](https://cloud.google.com/config-connector/docs/reference/resource-docs/networkservices/networkservicesgateway)
  * [`PrivateCACertificateAuthority`](https://cloud.google.com/config-connector/docs/reference/resource-docs/privateca/privatecacertificateauthority)
  * [`PrivateCACertificateTemplate`](https://cloud.google.com/config-connector/docs/reference/resource-docs/privateca/privatecacertificatetemplate)
  * [`PubSubSubscription`](https://cloud.google.com/config-connector/docs/reference/resource-docs/pubsub/pubsubsubscription)
  * [`RecaptchaEnterpriseKey`](https://cloud.google.com/config-connector/docs/reference/resource-docs/recaptchaenterprise/recaptchaenterprisekey)
  * [`RedisInstance`](https://cloud.google.com/config-connector/docs/reference/resource-docs/redis/redisinstance)
  * [`ServiceDirectoryEndpoint`](https://cloud.google.com/config-connector/docs/reference/resource-docs/servicedirectory/servicedirectoryendpoint)
  * [`ServiceDirectoryNamespace`](https://cloud.google.com/config-connector/docs/reference/resource-docs/servicedirectory/servicedirectorynamespace)
  * [`Service`](https://cloud.google.com/config-connector/docs/reference/resource-docs/serviceusage/service)
  * [`ServiceIdentity`](https://cloud.google.com/config-connector/docs/reference/resource-docs/serviceusage/serviceidentity)



### Fixed

Bug Fixes:

  * [`ComposerEnvironment`](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11001): Fix storageConfig.bucketRef mapping.
  * [`MemorystoreInstance`](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11547): Prevent infinite reconciliation drift loop by aligning connections list length.
  * [`MemorystoreInstance`](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11559): Prevent false drift and update attempts on unspecified immutable fields.
  * [`ComputeBackendService`](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/11800): Fix config-connector export tool to export `backend` field.
  * [`KMSAutokeyConfig`](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/9658): Clean up and improve autokey config identity and deletion resolution.
  * [`BigQuery`](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/9623): Fix perpetual diff on tables inheriting dataset encryption.
  * [`NotebooksInstance`](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/9810): Fix direct controller for NotebookInstance to resolve references.

]]> July 01, 2026tag:google.com,2016:configconnector-release-notes#July_01_20262026-07-01T00:00:00-07:00Announcement 

Config Connector version 1.153.0 is now available.

### Feature

New Beta Resources (Direct Reconciler):

  * [`OrgPolicyPolicy`](https://cloud.google.com/config-connector/docs/reference/resource-docs/orgpolicy/orgpolicypolicy)
    * Manage [Organization Policies](https://cloud.google.com/resource-manager/docs/organization-policy/overview) to configure constraints across your Google Cloud resources.



New Alpha Resources (Direct Reconciler):

  * `AIStreamsCluster`
    * Manage [AI Streams](https://cloud.google.com/ai-streams/docs) clusters to ingest and process real-time video streams.
  * `AutoMLDataset`
    * Manage [AutoML datasets](https://cloud.google.com/vertex-ai/docs/datasets/overview) in Vertex AI.
  * `CloudBatchResourceAllowance`
    * Manage [Batch resource allowances](https://cloud.google.com/batch/docs) to control resource usage and limits for batch jobs.
  * `BeyondCorpClientGateway`
    * Manage [BeyondCorp client gateways](https://cloud.google.com/beyondcorp/docs) to secure access to private applications.
  * `BigLakeDatabase`
    * Manage [BigLake databases](https://cloud.google.com/bigquery/docs/biglake-intro) for unified analytics over data lakes.
  * `BigtableAuthorizedView`
    * Manage [Bigtable authorized views](https://cloud.google.com/bigtable/docs/authorized-views) to control access to specific subsets of data in a table.
  * `BigtableBackup`
    * Manage [Bigtable backups](https://cloud.google.com/bigtable/docs/backups) to preserve table data.
  * `BillingAccount`
    * Manage [Billing accounts](https://cloud.google.com/billing/docs) (read-only/reference representation).
  * `CertificateManagerCertificateIssuanceConfig`
    * Manage [Certificate Manager certificate issuance configurations](https://cloud.google.com/certificate-manager/docs/issuance-configs) for automated certificate provisioning.
  * `CloudDeployDeployPolicy`
    * Manage [Cloud Deploy deploy policies](https://cloud.google.com/deploy/docs) to define deployment constraints and approvals.
  * `FirestoreBackupSchedule`
    * Manage [Firestore backup schedules](https://cloud.google.com/firestore/docs/backups) for automated database backups.
  * `IAMDenyPolicy`
    * Manage [IAM deny policies](https://cloud.google.com/iam/docs/deny-overview) to explicitly deny permissions.
  * `NetworkSecurityMirroringDeployment`
    * Manage [Network Security mirroring deployments](https://cloud.google.com/secure-web-proxy/docs) to mirror network traffic for inspection.
  * `NetworkSecurityMirroringEndpointGroup`
    * Manage [Network Security mirroring endpoint groups](https://cloud.google.com/secure-web-proxy/docs) to associate mirroring endpoints.
  * `SecurityCenterBigQueryExport`
    * Manage [Security Command Center BigQuery exports](https://cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-bigquery) to automatically export findings to BigQuery.
  * `SecurityCenterMuteConfig`
    * Manage [Security Command Center mute configs](https://cloud.google.com/security-command-center/docs/how-to-mute-findings) to control finding visibility.
  * `VertexAIExampleStore`
    * Manage [Vertex AI example stores](https://cloud.google.com/vertex-ai/docs) for managing example data.



### Feature

New Features:

  * Added the `cnrm.cloud.google.com/remove-default-node-pool-allow-node-config` annotation to the `ContainerCluster` resource. This annotation lets you set a field like `spec.nodeConfig` in a `ContainerCluster` resource, while still letting Config Connector remove the field after removing the default node pool. This annotation is intended for scenarios where defining `spec.nodeConfig` is necessary for organizational policy or system requirements during initial cluster provisioning. This release note was added on August 27, 2026.



### Feature

New Fields:

  * [`ContainerCluster`](https://cloud.google.com/config-connector/docs/reference/resource-docs/container/containercluster)
    * Added `spec.confidentialNodes.confidentialInstanceType` and `spec.nodeConfig.confidentialNodes.confidentialInstanceType` fields.
  * [`ContainerNodePool`](https://cloud.google.com/config-connector/docs/reference/resource-docs/container/containernodepool)
    * Added `spec.nodeConfig.confidentialNodes.confidentialInstanceType` field.
    * Added `spec.nodeConfig.windowsNodeConfig` field.
  * [`RedisCluster`](https://cloud.google.com/config-connector/docs/reference/resource-docs/redis/rediscluster)
    * Added `spec.automatedBackupConfig` field.
    * Added `spec.crossClusterReplicationConfig` field.
    * Added `spec.kmsKeyRef` field.
    * Added `spec.maintenancePolicy` and `status.observedState.maintenancePolicy` fields.
    * Added `status.observedState.pscServiceAttachments` field.
  * [`MemorystoreInstance`](https://cloud.google.com/config-connector/docs/reference/resource-docs/memorystore/memorystoreinstance)
    * Added `spec.maintenancePolicy` and `status.observedState.maintenancePolicy` fields.
    * Added `spec.kmsKeyRef` field.
    * Added `status.observedState.encryptionInfo` field.



### Change

Reconciliation Improvements:

Added support for direct reconciliation to more resources, with opt-in behaviour. The API is unchanged. To use the direct reconciler, add the `alpha.cnrm.cloud.google.com/reconciler: direct` annotation to the corresponding Config Connector object. This release note was edited on October 2, 2026. The following resources now have direct reconciliation support:

  * [`ArtifactRegistryRepository`](https://cloud.google.com/config-connector/docs/reference/resource-docs/artifactregistry/artifactregistryrepository)
  * [`CertificateManagerCertificate`](https://cloud.google.com/config-connector/docs/reference/resource-docs/certificatemanager/certificatemanagercertificate)
  * [`DNSManagedZone`](https://cloud.google.com/config-connector/docs/reference/resource-docs/dns/dnsmanagedzone)
  * [`DNSPolicy`](https://cloud.google.com/config-connector/docs/reference/resource-docs/dns/dnspolicies)
  * [`LoggingLogBucket`](https://cloud.google.com/config-connector/docs/reference/resource-docs/logging/logginglogbucket)
  * [`LoggingLogSink`](https://cloud.google.com/config-connector/docs/reference/resource-docs/logging/logginglogsink)
  * [`LoggingLogView`](https://cloud.google.com/config-connector/docs/reference/resource-docs/logging/logginglogview)
  * [`PubSubSchema`](https://cloud.google.com/config-connector/docs/reference/resource-docs/pubsub/pubsubschema)
  * [`PubSubTopic`](https://cloud.google.com/config-connector/docs/reference/resource-docs/pubsub/pubsubtopic)
  * [`ServiceDirectoryService`](https://cloud.google.com/config-connector/docs/reference/resource-docs/servicedirectory/servicedirectoryservice)



### Fixed

Bug Fixes:

  * [#9114](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/9114): `ComposerEnvironment`: Support resource reference resolution and fix drift on private environment config.
  * [#10414](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10414): `ComputeBackendService`: Prevent the automatic injection of `subsetting: { policy: "NONE" }` for regional backend services with `INTERNAL_SELF_MANAGED` load balancing scheme.
  * [#7222](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/7222): `DataprocCluster`: `userServiceAccountMapping` field in DataprocCluster resources is now mutable.
  * [#9594](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/9594): `DNSPolicy`: Fixes to DNSPolicy for real GCP integration.
  * [#10417](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/10417): `MemorystoreInstance`: Fix crossInstanceReplicationConfig field, allowing replication roles to be synced and updated correctly.
  * [#8828](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/8828): `NetworkSecurity`: Fix UpdateAuthorizationPolicy panic with empty updateMask.
  * [#7567](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/7567): `PrivilegedAccessManager`: Fix mock drift in PrivilegedAccessManager by correcting Delete LRO and array element retention.
  * [#9602](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/9602): `RedisCluster`: Fix permanent diff caused by automated backup configuration default value.

]]> June 23, 2026tag:google.com,2016:configconnector-release-notes#June_23_20262026-06-23T00:00:00-07:00Announcement 

Config Connector version 1.152.0 is now available.

### Feature

New Fields:

  * [`ComputeReservation`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computereservation)
    * Added `spec.shareSettings` field.
  * [`ComputeForwardingRule`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computeforwardingrule)
    * Added `status.target` field.



### Change

Reconciliation Improvements:

Added support for direct reconciliation to more resources, with opt-in behaviour. The API is unchanged. To use the direct reconciler, add the `alpha.cnrm.cloud.google.com/reconciler: direct` annotation to the corresponding Config Connector object. This release note was edited on October 2, 2026. The following resources now have direct reconciliation support:

  * [`ComputeReservation`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computereservation)
  * [`FirestoreIndex`](https://cloud.google.com/config-connector/docs/reference/resource-docs/firestore/firestoreindex)



### Fixed

Bug Fixes:

  * [#8025](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/8025): `SQLInstance`: Fixed case sensitivity in `availabilityType`.
  * [#7743](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/7743): `Preview Tool`: Fixed crash on typed resources and hang on defaulting in preview mode.
  * [#7371](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/7371): `ComputeForwardingRule`: Fixed target field matching.
  * [#8479](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/8479): `ComputeFutureReservation`: Fixed validation logic for future reservation times.

]]> May 19, 2026tag:google.com,2016:configconnector-release-notes#May_19_20262026-05-19T00:00:00-07:00Announcement 

Config Connector version 1.151.0 is now available.

### Change

New Alpha Resources (Direct Reconciler):

  * CloudDeployAutomation
  * ComputeFutureReservation
  * GKEHubMembershipBinding
  * GKEHubNamespace
  * GKEHubScopeRBACRoleBinding
  * NetworkServicesWasmPlugin
  * VertexAIDataLabelingJob



### Feature

New Fields:

  * [`MemorystoreInstance`](https://cloud.google.com/config-connector/docs/reference/resource-docs/memorystore/memorystoreinstance)
    * Added `spec.automatedBackupConfig` field.
    * Added `spec.crossInstanceReplicationConfig` field.
    * Added `spec.maintenanceVersion` field.
    * Added `status.observedState.availableMaintenanceVersions` field.
    * Added `status.observedState.crossInstanceReplicationConfig` field.
    * Added `status.observedState.effectiveMaintenanceVersion` field.
    * Added `status.observedState.pscAttachmentDetails` field.



### Fixed

  * [`BigQueryDataTransferConfig`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/bigquerydatatransfer/bigquerydatatransferconfig)
    * Fix resource duplication loop.
  * [`ContainerCluster`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/container/containercluster)
    * Enable projectID to projectNumber transform in fields in Container LROs.

]]> May 12, 2026tag:google.com,2016:configconnector-release-notes#May_12_20262026-05-12T00:00:00-07:00Announcement 

Config Connector version 1.150.0 is now available.

### Feature

New Alpha Resources (Direct Reconciler):

  * `GKEHubScope`
    * Manage [Google Kubernetes Engine Hub Scopes](https://cloud.google.com/anthos/fleet-management/docs/concepts#fleet-level-features) which let you group fleet resources for fine-grained management.
  * `CloudDeployTarget`
    * Manage [Cloud Deploy targets](https://cloud.google.com/deploy/docs/targets) which define where your application is deployed.



### Feature

New Fields:

  * [`CertificateManagerCertificate`](https://cloud.google.com/config-connector/docs/reference/resource-docs/certificatemanager/certificatemanagercertificate)
    * Added `status.observedState` field, which includes `managed.state`, `managed.authorizationAttemptInfo`, and `managed.provisioningIssue`. This enables tracking the current state of the certificate even when `state-into-spec: absent` is used.
  * [`ContainerCluster`](https://cloud.google.com/config-connector/docs/reference/resource-docs/container/containercluster)
    * Added `spec.ipAllocationPolicy.additionalIpRangesConfigs` field.
  * [`ContainerNodePool`](https://cloud.google.com/config-connector/docs/reference/resource-docs/container/containernodepool)
    * Added `spec.networkConfig.subnetworkRef` field.



### Feature

Improved resource creation logging for both Direct and DCL-based controllers by including structured diffs.

### Change

Reconciliation Improvements:

Added support for direct reconciliation to more resources, with opt-in behaviour. The API is unchanged. To use the direct reconciler, add the `alpha.cnrm.cloud.google.com/reconciler: direct` annotation to the corresponding Config Connector object. This release note was edited on October 2, 2026. The following resources now have direct reconciliation support:

  * [`BigqueryTable`](https://cloud.google.com/config-connector/docs/reference/resource-docs/bigquery/bigquerytable)
    * Fixed a permanent difference in the `policyTag` field when using the direct controller, ensuring safer upgrades.
  * [`SQLInstance`](https://cloud.google.com/config-connector/docs/reference/resource-docs/sql/sqlinstance)
    * Added detailed diff reporting for the `userLabels` field.
  * [`DataplexLake`](https://cloud.google.com/config-connector/docs/reference/resource-docs/dataplex/dataplexlake)
    * Added structured diff reporting to improve visibility into resource changes.



### Fixed

Bug Fixes:

  * [`ContainerCluster`](https://cloud.google.com/config-connector/docs/reference/resource-docs/container/containercluster)
    * Fixed a permanent difference in the `databaseEncryption.state` field and added support for the `ALL_OBJECTS_ENCRYPTION_ENABLED` value.
  * [`MemorystoreInstance`](https://cloud.google.com/config-connector/docs/reference/resource-docs/memorystore/memorystoreinstance)
    * Updated the controller to use change cookies, improving reconciliation stability and correctness.

]]> May 05, 2026tag:google.com,2016:configconnector-release-notes#May_05_20262026-05-05T00:00:00-07:00Announcement 

Config Connector version 1.149.1 is now available.

### Feature

New Alpha Resources (Direct Reconciler):

  * [`NetworkServicesLBRouteExtension`](https://cloud.google.com/config-connector/docs/reference/resource-docs/networkservices/networkserviceslbrouteextension) [#6957](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/6957)
    * Manage [load balancing route extensions](https://cloud.google.com/service-extensions/docs/optimize-proxies-lb-route-extensions) which let you inject custom logic into the load balancing path.
  * [`ParameterManagerParameterVersion`](https://cloud.google.com/config-connector/docs/reference/resource-docs/parametermanager/parametermanagerparameterversion) [#7140](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/7140)
    * Manage [Parameter Manager parameter versions](https://cloud.google.com/secret-manager/docs/parameter-manager) which lets you to manage regional parameters.



### Feature

New Fields:

  * [`ContainerCluster`](https://cloud.google.com/config-connector/docs/reference/resource-docs/container/containercluster) [#7336](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/7336)
    * Added `spec.nodeConfig.ephemeralStorageLocalSsdConfig.dataCacheCount` field to support GKE Data Cache.
  * [`ContainerNodePool`](https://cloud.google.com/config-connector/docs/reference/resource-docs/container/containernodepool) [#7336](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/7336)
    * Added `spec.nodeConfig.ephemeralStorageLocalSsdConfig.dataCacheCount` field to support GKE Data Cache.



### Feature

New Features:

  * [Controlled CR reconciliation](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/6243) Added support for unmanaging specific resources through `resourceSettings` in `ConfigConnector` (global) and `ConfigConnectorContext` (per-namespace). This lets you to selectively disable reconciliation for specific Group/Kinds to save memory or manage resources differently.



### Change

Reconciliation Improvements:

Added support for direct reconciliation to more resources, with opt-in behaviour. The API is unchanged. To use the direct reconciler, add the `alpha.cnrm.cloud.google.com/reconciler: direct` annotation to the corresponding Config Connector object. This release note was edited on October 2, 2026.

  * [`BigQueryDatasetAccess`](https://cloud.google.com/config-connector/docs/reference/resource-docs/bigquery/bigquerydatasetaccess) [#7000](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/7000)



### Fixed

Bug Fixes:

  * [Preview Tool](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/7642) Fixed a connection error in the Config Connector preview tool and enforced read-only access to the cluster for improved security.

]]> April 22, 2026tag:google.com,2016:configconnector-release-notes#April_22_20262026-04-22T00:00:00-07:00Announcement 

Config Connector version 1.148.0 is now available.

### Feature

New Alpha Resources (Direct Reconciler):

  * [`ParameterManagerParameterVersion`](https://cloud.google.com/config-connector/docs/reference/resource-docs/parametermanager/parametermanagerparameterversion)
    * Configure [Parameter Manager parameter versions](https://cloud.google.com/secret-manager/docs/parameter-manager) which lets you manage regional parameters.



### Feature

New features:

  * [#6919](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/6919): `MultiClusterLeaseSpec` now supports integration with a syncer for KRM objects. This helps Config Connector take ownership of resources with service generated IDs.
  * [#7202](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/7202): `kompanion`: Added a Model Context Protocol (MCP) server to the `kompanion` tool to enable AI IDEs and assistants to interact with Config Connector resources.
  * [#7075](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/7075): `Config Connector controllers`: Added a `--skip-name-validation` flag to bypass duplicate controller name checks during registration, facilitating integration tests and multi-manager scenarios.



### Fixed

Bug Fixes:

  * [#7145](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/7145): `SQLInstance`: Fixed an issue where `settings.dataCacheConfig` was incorrectly detected as different when `dataCacheEnabled` was `false`.
  * [#7200](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/7200): `SQLInstance`: Updated matching functions to treat nil values in KRM as equivalent to empty or default objects in Google Cloud, preventing unnecessary re-reconciliation loops.
  * [#6943](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/6943): `TagKey/TagValue`: Handle `ALREADY_EXISTS` error in TagKey and TagValue controllers by acquiring the existing resource.
  * [#6774](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/6774): `BigQueryAnalyticsHubDataExchange`: Added structured reporting diff to improve visibility into resource changes and fixed reconciliation logic errors.
  * [#7115](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/7115): `CloudBuildTrigger`: Restored missing descriptions in the CRD.
  * [#6693](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/6693): `RunService`: Fixed a typo in environment variable values in samples and test fixtures.



### Feature

Documentation:

  * Added [a guide for controller configuration](https://github.com/GoogleCloudPlatform/k8s-config-connector/blob/master/docs/features/controller-configuration.md), detailing Direct, Terraform, and DCL controllers, including precedence rules and overrides.
  * Added [a guide for enabling VerticalPodAutoscaler (VPA) for Config Connector Pods](https://github.com/GoogleCloudPlatform/k8s-config-connector/blob/master/docs/features/containerresource.md) using `ControllerResource` and `NamespacedControllerResource`.
  * Added [a guide for the `config-connector` CLI and specifically for the `preview` command.](https://github.com/GoogleCloudPlatform/k8s-config-connector/blob/master/docs/cli/README.md).

]]> March 25, 2026tag:google.com,2016:configconnector-release-notes#March_25_20262026-03-25T00:00:00-07:00Announcement 

Config Connector version 1.147.1 is now available.

### Feature

New Alpha Resources (Direct Reconciler):

  * `CloudDeployCustomTargetType`
    * Please replace any instances of the `DeployCustomTargetType` resource with the new `CloudDeployCustomTargetType` (v1alpha1) resource.



### Change

Reconciliation Improvements:

  * Improved structured reporting diffs to provide better visibility into what changed during reconciliation for the following resources: 
    * `BigQueryDataset`
    * `BigQueryReservationAssignment`
    * `BigQueryTable`
    * `CertificateManagerDNSAuthorization`
    * `CloudIdentityGroup`
    * `DataformRepository`
    * `MetastoreService`
    * `PrivilegedAccessManagerEntitlement`
    * `WorkflowsWorkflow`



### Feature

New features:

  * Enhanced `config-connector preview` to support side-by-side comparison between default and alternative controllers.
  * Added a `--skip-name-validation` flag to Config Connector controllers to bypass duplicate controller name checks during registration.



### Fixed

Bug Fixes:

  * Added CRD filtering for the preview recorder to skip non-CNRM objects.

]]> March 10, 2026tag:google.com,2016:configconnector-release-notes#March_10_20262026-03-10T00:00:00-07:00Breaking 

Config Connector version 1.144.0 was identified as a bad release. Do not use this version - upgrade directly to 1.145.0 or later.

### Announcement

Config Connector version 1.146.0 is now available.

### Feature

New Alpha Resources (Direct Reconciler):

  * `ParameterManagerParameter`
    * Manage [Parameter Manager Parameters](https://cloud.google.com/secret-manager/parameter-manager/docs/overview).



### Feature

New Fields:

  * [`ContainerCluster`](https://cloud.google.com/config-connector/docs/reference/resource-docs/container/containercluster)
    * Added `spec.controlPlaneEndpointsConfig.dnsEndpointConfig.enableK8sTokensViaDns` field.



### Change

Improvements:

  * [`ContainerCluster`](https://cloud.google.com/config-connector/docs/reference/resource-docs/container/containercluster)
    * Made `spec.clusterAutoscaling.autoProvisioningDefaults.bootDiskKMSKeyRef` mutable.
  * `NetworkServicesWasmPlugin`
    * Introduced identity and reference.
  * Added structured reporting diff to numerous direct controllers to enhance diff visibility.



### Fixed

Bug Fixes:

  * [`SQLInstance`](https://cloud.google.com/config-connector/docs/reference/resource-docs/sql/sqlinstance)
    * Added client-side default for `RetainedBackups` and `RetentionUnit`, and validated the `edition` field.
    * Added `replicaConfiguration` as an unmanageable field.
    * Controller now correctly defaults the field `enablePrivatePathForGoogleCloudServices` to `false`.
  * [`CertificateManagerDnsAuthorization`](https://cloud.google.com/config-connector/docs/reference/resource-docs/certificatemanager/certificatemanagerdnsauthorization)
    * Sanitized Kubernetes labels to avoid 400 errors from invalid characters.
  * `ConfigConnector` Core 
    * `preview` now performs an early exit when no resources are found to reconcile.
    * Fixed CRD field description for shared parent.
    * Fixed incorrect exit status in lint filter.
    * Updated `mockgcp` to improve compute regional resource mocks and defaults.

]]> February 22, 2026tag:google.com,2016:configconnector-release-notes#February_22_20262026-02-22T00:00:00-08:00Announcement 

Config Connector version 1.145.0 is now available.

### Feature

New Beta Resources (Direct Reconciler):

  * [`ComputeSecurityPolicy`](https://cloud.google.com/config-connector/docs/reference/resource-docs/compute/computesecuritypolicy)
    * Manage Google Cloud Armor security policies.
  * `MemorystoreInstance`
    * Manage [Memorystore for Valkey Instances](https://cloud.google.com//memorystore/docs/valkey/reference/rest/v1/projects.locations.instances).



### Feature

New Fields:

  * [`ContainerCluster`](https://cloud.google.com/config-connector/docs/reference/resource-docs/container/containercluster)
    * Added `spec.clusterAutoscaling.defaultComputeClassConfig` field.
  * [`RunJob`](https://cloud.google.com/config-connector/docs/reference/resource-docs/run/runjob)
    * Added `spec.template.template.volumes.nfs` field to support NFS backed Volumes.
    * Added `spec.template.template.volumes.gcs` field to support GCS backed Volumes.
  * [`SQLInstance`](https://cloud.google.com/config-connector/docs/reference/resource-docs/sql/sqlinstance)
    * Added `spec.settings.failoverDrReplicaRef` field to support designating CloudSQL Enterprise Plus DR Replicas.



### Feature

New features:

  * Added the `preview` command to the `config-connector` CLI. The `preview` command has been removed from the experimental `kompanion` tool.



### Change

Added support for structured diff reporting to the following direct controllers to improve logging and debugging:

  * [`ApigeeEnvgroup`](https://cloud.google.com/config-connector/docs/reference/resource-docs/apigee/apigeeenvgroup)
  * [`ApigeeInstance`](https://cloud.google.com/config-connector/docs/reference/resource-docs/apigee/apigeeinstance)
  * [`AssetFeed`](https://cloud.google.com/config-connector/docs/reference/resource-docs/asset/assetfeed)
  * [`AssetSavedQuery`](https://cloud.google.com/config-connector/docs/reference/resource-docs/asset/assetsavedquery)
  * BackupVaultIdentity
  * BigtableLogicalView
  * [`CloudDeployDeliveryPipeline`](https://cloud.google.com/config-connector/docs/reference/resource-docs/clouddeploy/clouddeploydeliverypipeline)
  * ColabRuntime
  * [`RedisCluster`](https://cloud.google.com/config-connector/docs/reference/resource-docs/redis/rediscluster)
  * [`SpannerBackupSchedule`](https://cloud.google.com/config-connector/docs/reference/resource-docs/spanner/spannerbackupschedule)
  * [`SpannerInstance`](https://cloud.google.com/config-connector/docs/reference/resource-docs/spanner/spannerinstance)
  * SpannerInstanceConfig
  * TaskQueue
  * [`WorkstationConfig`](https://cloud.google.com/config-connector/docs/reference/resource-docs/workstations/workstationconfig)



### Fixed

Bug Fixes:

  * [`DataformRepository`](https://cloud.google.com/config-connector/docs/reference/resource-docs/dataform/dataformrepository)
    * Fixed a bug where the `serviceAccountRef` field could not be updated.
  * [`SpannerBackupSchedule`](https://cloud.google.com/config-connector/docs/reference/resource-docs/spanner/spannerbackupschedule)
    * Fixed an issue with invalid update masks by handling output-only fields.

]]> January 30, 2026tag:google.com,2016:configconnector-release-notes#January_30_20262026-01-30T00:00:00-08:00Announcement 

Config Connector version 1.144.0 is now available.

### Feature

New Beta Resources (Direct Reconciler):

  * [`TagsLocationTagBinding`](https://cloud.google.com/config-connector/docs/reference/resource-docs/tags/tagslocationtagbinding)
    * `TagsLocationTagBinding` is promoted to beta and now uses the direct reconciler by default.
    * Supports tagging of regional resources, including `ArtifactRegistryRepository`, `CloudRun` (`RunJob`, `RunService`), `BigQueryDataset`, `BigQueryTable`, and `StorageBucket`.
    * `spec.location` should be set to the region of the resource being tagged.



### Fixed

Bug Fixes:

  * Fixed incorrect diffs in `TagsLocationTagBinding` caused by project number versus. project ID mismatches.



### Change

Reconciliation Improvements:

  * [`TagsLocationTagBinding`](https://cloud.google.com/config-connector/docs/reference/resource-docs/tags/tagslocationtagbinding)
    * Switched to direct reconciliation as the default reconciler.

]]> January 27, 2026tag:google.com,2016:configconnector-release-notes#January_27_20262026-01-27T00:00:00-08:00Announcement 

Config Connector version 1.134.4 is now available.

### Fixed

Bug Fixes:

  * [#6035](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/6035): Fixed an issue where `managedFields` metadata could be incorrectly attributed to the `status` subresource during spec updates, causing "Location must be set" errors.



### Feature

[#6065](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/6065): Enabled Vertical Pod Autoscaler (VPA) support. You can enable VPA for Config Connector components via `ControllerResource` and `NamespacedControllerResource` to automatically adjust resource requests.

]]> January 23, 2026tag:google.com,2016:configconnector-release-notes#January_23_20262026-01-23T00:00:00-08:00Announcement 

Config Connector version 1.143.0 is now available.

### Feature

New Alpha Resources (Direct Reconciler):

  * `ParameterManagerParameter`



### Feature

New Beta Resources (Direct Reconciler):

  * `ArtifactRegistryRepository`
  * `LoggingLink`
  * `MemorystoreInstance`
  * `PrivateCACAPool`



### Feature

New Features:

  * Set `GOMEMLIMIT` for KCC workloads to improve memory management and stability.



### Feature

New Fields:

  * `AlloyDBInstance`
    * Added `spec.connectionPoolConfig` field.
    * Added `status.connectionPoolConfig` field.



### Change

Reconciliation Improvements:

  * `TagsTagBinding`

    * Added support for `organizations` in `parentRef`.
    * Added support for multiple targets in `parentRef`.
  * Resource References (refs.Ref) support added for the following resources to improve reference resolution:

    * `BigQueryTable`
    * `BigQueryDataset`
    * `CloudRunService`
    * `CloudRunJob`
    * `ArtifactRegistryRepository`
    * `StorageBucket`



### Fixed

Bug Fixes:

  * [Issue 6221](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/6221): `ComputeBackendService` can now correctly refer to `clientTLSPolicy`.
  * [Issue 6156](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/6156): `BigQueryTable` now ignores `int64` to `int32` schema changes when configured.
  * [Issue 6026](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/6026): Fixed identity parsing for `TagsTagValue`.

]]> January 09, 2026tag:google.com,2016:configconnector-release-notes#January_09_20262026-01-09T00:00:00-08:00Announcement 

Config Connector version 1.142.0 is now available.

### Feature

New Beta Resources (Direct Reconciler):

  * `AlloyDBBackup`
  * `AccessContextManagerAccessLevel`



### Feature

New Features:

  * IAM: Added support for `iam.cnrm.cloud.google.com/disable-dependent-services` annotation.
  * Added support for Cilium cluster-wide network policy.



### Feature

New Fields:

  * `AlloyDBInstance`
    * Added `spec.observabilityConfig` and `spec.queryInsightsConfig` fields.
  * `ContainerNodePool`
    * Added `spec.nodeConfig.enableNestedVirtualization` field.



### Change

Reconciliation Improvements:

Added support for direct reconciliation to more resources, with opt-in behaviour. The API is unchanged. To use the direct reconciler, add the `alpha.cnrm.cloud.google.com/reconciler: direct` annotation to the corresponding Config Connector object. The following resources now have direct reconciliation support:

  * `TagsLocationTagBinding`: Now supports direct reconciliation.



### Fixed

Bug Fixes:

  * `BatchJob`: Fixed a bug where the resource could not be created.
  * `FirewallPolicyRule`: Fixed an issue with updating the resource.
  * `IAMServiceAccountKey`: Fixed an issue causing unnecessary re-reconciliation.
  * Fixed a bug where `ComputeBackendService` could not refer to `clientTLSPolicy` due to an invalid format.
  * Fixed a bug where interconnect attachments were not ignored.
  * Fixed a bug in the GitHub MCP server.
  * Fixed a bug in the private cluster endpoint for `mockgcp`.

]]> December 19, 2025tag:google.com,2016:configconnector-release-notes#December_19_20252025-12-19T00:00:00-08:00Announcement 

Config Connector version 1.141.0 is now available.

### Feature

New Features:

  * Enabled Vertical Pod Autoscaler (VPA) support for Config Connector controllers.
  * Added `verticalPodAutoscalerMode` field to `ConfigConnector` and `ConfigConnectorContext` resources.



### Feature

New Fields:

  * RunJob

    * Added `spec.template.spec.containers[].port` field.
  * DataplexTask

    * Replaced `project` with `projectRef`.
    * Replaced `serviceAccount` with `serviceAccountRef`.
    * Replaced `kmsKey` with `kmsKeyRef`.



### Fixed

Bug Fixes:

  * Fixed various issues in `observedState` handling for resources with reference fields.
  * Fixed an issue where IAMPolicy and IAMPartialPolicy controllers would alphabetize the members field within the resource spec and write it back. This behavior can conflict with intent-based reconciliation from GitOps systems such as Config Sync, causing a loop of updates and potentially exhausting IAM read quotas.

]]> December 15, 2025tag:google.com,2016:configconnector-release-notes#December_15_20252025-12-15T00:00:00-08:00Announcement 

Config Connector version 1.140.2 is now available.

### Fixed

  * Fixed a bug where the IAMPolicy and IAMPartialPolicy controllers would alphabetize the members field within the resource spec and write it back. This behavior can conflict with intent-based reconciliation from GitOps systems such as Config Sync, causing a loop of updates and potentially exhausting IAM read quotas. This issue affected versions 1.140.0 and has now been patched in version 1.140.2.

]]> December 04, 2025tag:google.com,2016:configconnector-release-notes#December_04_20252025-12-04T00:00:00-08:00Announcement 

Config Connector version 1.140.0 is now available.

### Feature

New Beta Resources (Direct Reconciler):

  * `CertificateManagerCertificateIssuanceConfig`
    * Manage Certificate Manager certificate issuance configurations for automating certificate issuance.



### Change

New Alpha Resources (Direct Reconciler):

  * `AssuredWorkloadsWorkload`
    * Manage Assured Workloads workloads to support compliance and security requirements.
  * `ConfigDeliveryResourceBundle`
    * Manage Config Delivery resource bundles for Config Sync.



### Feature

New Fields:

  * `AlloyDBCluster`
    * Added `spec.restoreContinuousBackupSource` and `spec.restoreBackupSource` fields to support restoring from a backup.
  * `BigQueryReservationAssignment`
    * Added `spec.jobType` field.
  * `FirestoreDatabase`
    * Added `spec.deleteProtectionState` field.
  * `FirestoreField`
    * Added `spec.ttlConfig` field.
  * `RunJob`
    * Added `spec.template.template.containers.dependsOn` field.



### Change

Reconciliation Improvements:

  * Integrated Multi-Cluster Leader Election for improved reliability in multi-cluster setups.



### Fixed

  * Fixed an issue where `BigQueryReservationAssignment` was not exposing `externalRef`.
  * Fixed an issue with `CertificateManagerDNSAuthorization` API, Fuzzer and Mapper.
  * Fixed an issue with `FirestoreDatabase` defaulting logic.

]]> November 20, 2025tag:google.com,2016:configconnector-release-notes#November_20_20252025-11-20T00:00:00-08:00Announcement 

Config Connector version 1.139.0 is now available.

### Change

New Alpha Resources (Direct Reconciler):

  * `FirestoreField`



### Feature

New Features:

  * The controller type is now reported at the start and end of reconciliation.
  * Mockgcp now supports `iap oauth brands` and `bigtable materializedview`.



### Change

Reconciliation Improvements:

  * `IAM partial policy management`



### Fixed

  * Reduced the memory footprint of the recorder.
  * `SQLInstance`: Fixed an issue where empty `maintenanceVersion` patches were sent. The `settings` and `maintenanceVersion` fields are now unmanaged.
  * `FirestoreDatabase`: Fixed boolean value exports.

]]> November 14, 2025tag:google.com,2016:configconnector-release-notes#November_14_20252025-11-14T00:00:00-08:00Announcement 

Config Connector version 1.138.0 is now available.

### Feature

New Beta Resources (Direct Reconciler):

  * `BackupDRBackupVault`
  * `OrgPolicyCustomConstraint`



### Feature

New Alpha Resources (Direct Reconciler):

  * `FirestoreBackupSchedule`
  * `FirestoreDocument`



### Change

Reconciliation Improvements:

  * Improved Normalization logic for `OrgPolicy`, `RunJob`, `TagsTagBinding`, and `VertexAIIndex` resources.



### Fixed

Bug Fixes:

  * Fixed format validation issue in the `DataflowFlexTemplateJob` direct controller when the `spec.subnetworkRef.external` field contains full URL.
  * Updated `status.observedGeneration` in `ConfigConnector` object.

]]> October 16, 2025tag:google.com,2016:configconnector-release-notes#October_16_20252025-10-16T00:00:00-07:00Change 

New Beta Resources (Direct Reconciler):

  * `DocumentAIProcessorVersion`
  * `EssentialContactsContact`
  * `BigQueryBigLakeTable`
  * `BackupDRBackupPlan`



### Fixed

Bug Fixes:

  * Fixed an issue where `ComputeBackendService` backends were not sorted.
  * Fixed an issue where `CloudFunctionsFunction` runtime was not a supported value.
  * Fixed an issue with labels for `BackupDRBackupPlan`.
  * Fixed an issue with labels for `RunJob`.
  * Fixed a fuzzing issue for `FirestoreField`.
  * Fixed an issue with `KMSCryptoKey` import.
  * Fixed a flakiness issue in the `MonitoringDashboard` fuzzer.
  * Fixed a flakiness issue in tests.
  * Fixed an issue with bad labels in tests.
  * Fixed an issue with `etag` in direct reconciliation.



### Change

New Alpha Resources (Direct Reconciler):

  * `BigtableMaterializedView`
  * `MemorystoreInstance`



### Change

Reconciliation Improvements:

  * Enabled opt-in for IAM partial policy management.
  * Enabled server-side apply for KMS resources.
  * Improved reconciliation for `BigtableLogicalView` by using deep reflection.
  * Improved reconciliation for `FirestoreDatabase` with identity pattern and export support.
  * Improved reconciliation for `RunJob` with export support.
  * Unified `ComputeTargetTCPProxy` direct API and controller.



### Feature

New Fields:

  * `BigtableMaterializedView`: Added `spec.sourceTableRef` and `spec.definition`.
  * `BackupDRBackupPlan`: Added `spec.backupConfig.retentionPeriodDays` and `spec.backupConfig.backupWindow`.



### Announcement

Config Connector version 1.137.0 is now available.

]]> October 07, 2025tag:google.com,2016:configconnector-release-notes#October_07_20252025-10-07T00:00:00-07:00Change 

Reconciliation Improvements:

  * Introduced [Stateful Reconciliation for Direct Controllers](https://github.com/GoogleCloudPlatform/k8s-config-connector/blob/master/docs/designs/stateful-reconciliation-with-cookie.md). With stateful reconciliation, the direct controller stores a hash of the last successfully applied `.spec` in the resource's `.status`. This provides a lightweight, GitOps-safe record when a user has modified the desired state of the resource.



### Change

New Beta Resources (Direct Reconciler):

  * [`AssetFeed`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/asset/assetfeed)
  * [`BigQueryReservationAssignment`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/bigqueryreservation/bigqueryreservationassignment)
  * [`CloudDeployDeliveryPipeline`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/clouddeploy/clouddeploydeliverypipeline)
  * [`ComposerEnvironment`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/composer/composerenvironment)



### Fixed

Bug Fixes:

  * Added support for checking `etag` in spec for alpha resources.
  * Fixed an issue where `CloudIdentityMembership` roles comparison would fail.
  * Fixed a bug where the wrong GVK was reported in IAM controller.
  * Fixed a bug where errors were swallowed when reading a Secret.
  * Fixed an issue with LRO endTime in mockgcp.
  * Fixed a bug in the `etag` mapper.
  * Fixed a bug in the mapper generator for slice and single object map.
  * Fixed a bug in the mapper generator for OneOf if the input is not proto.Message.
  * Fixed an import for refs in the same package in `controllerbuilder`.



### Feature

New Fields:

  * [`ComposerEnvironment`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/composer/composerenvironment)
    * Added `spec.storageConfig` field.
    * Added `spec.config.workloadsConfig.dagProcessor` field.
    * Added `spec.config.workloadsConfig.triggerer` field.
    * Added `spec.config.softwareConfig.webServerPluginsMode` field.
    * Added `spec.config.softwareConfig.cloudDataLineageIntegration` field.



### Announcement

Config Connector version 1.136.1 is now available.

]]> September 24, 2025tag:google.com,2016:configconnector-release-notes#September_24_20252025-09-24T00:00:00-07:00Announcement 

Config Connector version 1.134.1 is now available.

### Fixed

Bug Fixes:

  * [#5230](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/5230): Fixed an issue that could lead to premature certificate rotation by ensuring errors are not swallowed when reading a Secret.
  * [#5231](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/5231): Add more verbose logging during certificate validation to assist with debugging.

]]> September 22, 2025tag:google.com,2016:configconnector-release-notes#September_22_20252025-09-22T00:00:00-07:00Fixed 

Bug Fixes:

  * [PR#5009](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/5009) Fix the nil pointer dereference error in AlloyDB direct controller



### Announcement

Config Connector version 1.135.0 is now available.

### Feature

New Fields:

  * `AlloyDBCluster`
    * Added `spec.databaseVersion` field



### Change

New Beta Resources (Direct Reconciler):

  * `AssetSavedQuery`
  * `PubSubSnapshot`



### Change

Modified Beta Reconciliation: We migrated the following resources from the Terraform-based or DCL-based controller to the new Direct Controller.

  * `VMWareEngineExternalAddress`

]]> September 03, 2025tag:google.com,2016:configconnector-release-notes#September_03_20252025-09-03T00:00:00-07:00Change 

Improved reconciliation by migrating the following resources from the Terraform-based or DCL-based controller to the new direct controller. These resources are migrated automatically and you no longer need to apply the `opt-in` annotation to enable the direct controller:

  * [`CloudIdentityGroup`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/cloudidentity/cloudidentitygroup)

  * [`CloudIdentityMembership`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/cloudidentity/cloudidentitymembership)




### Fixed

Bug Fixes:

  * `ConfigConnectorContext`: 
    * [PR#4995](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/4995): `status.observedGeneration` is now being set on the ConfigConnectorContext.
    * [PR#4657](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/4657): Added `spec.managerNamespace`.
  * `SQLInstance`: 
    * [PR#4838](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/4838): Fixed bug in SQLInstance `maintenanceVersion` UPDATE operation
    * [PR#4843](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/4843): Set status on acquisition for SQLInstance controller
    * [PR#4857](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/4857): Support SQLInstance `maintenanceVersion` in CREATE operation



### Change

New Fields:

  * `ContainerCluster`: DNS endpoint is supported in ContainerCluster.



### Announcement

Config Connector version 1.134.0 is now available.

]]> July 30, 2025tag:google.com,2016:configconnector-release-notes#July_30_20252025-07-30T00:00:00-07:00Feature 

New Beta Resources (Direct Reconciler):

  * [`APIGatewayAPI`](https://docs.cloud.google.com/config-connector/docs/reference/docs/reference/resource-docs/apigateway/apigatewayapi.md)

  * [`AppHubApplication`](https://docs.cloud.google.com/config-connector/docs/reference/docs/reference/resource-docs/apphub/apphubapplication.md)

  * `StorageAnywhereCache`




### Change

New Alpha Resources (Direct Reconciler):

  * `BigtableLogicalView`



### Change

Reconciliation Improvements

Added support for direct reconciliation to more resources, with opt-in behaviour. The API is backward compatible. The following resources now have direct reconciliation support

  * `BigQueryTable`
    * Use the `alpha.cnrm.cloud.google.com/reconciler: direct` annotation on the `BigQueryTable` CR object to opt-in the direct controller.
    * The direct controller also supports adding BigQueryDataPolicies directly to BigQueryTable columns within `spec.schema`.



### Fixed

  * [PR#4808](https://github.com/GoogleCloudPlatform/k8s-config-connector/pull/4808) filtered out Kubernetes labels that are invalid for Google Cloud in the `ComputeForwardingRule` direct controller, ensuring backward compatibility after migrating to the direct controller.



### Announcement

Config Connector version 1.133.0 is now available.

]]> July 14, 2025tag:google.com,2016:configconnector-release-notes#July_14_20252025-07-14T00:00:00-07:00Announcement 

Config Connector version 1.132.1 is now available.

### Change

Reconciliation Improvements:

  * [SpannerInstance](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/spanner/spannerinstance)
    * You can opt-in the direct controller by adding the `alpha.cnrm.cloud.google.com/reconciler: direct` annotation to the `SpannerInstance` resource`.
    * Direct controller is opt-in if using the following fields: 
      * `spec.labels`
      * `spec.defaultBackupScheduleType`
      * `spec.edition`
      * `spec.autoscalingConfig`

]]>
