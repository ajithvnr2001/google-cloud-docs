---
url: https://docs.cloud.google.com/asset-inventory/docs/legacy-fields/
title: Legacy fields \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:38.898732+00:00
---

# Legacy fields  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/legacy-fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Legacy fields Stay organized with collections  Save and categorize content based on your preferences. 

This document lists all the legacy fields and fields to be deprecated in Cloud Asset Inventory.

## Legacy field names

This section describes legacy field names and lists the assets that have multiple names for the same field.

_Legacy field names_ are not listed in the [discovery document](https://developers.google.com/discovery/v1/reference/apis). They are provided to support backward compatibility. We recommend using the field names listed in the discovery document whenever possible.

### Assets with multiple names for the same field

The following table lists the assets that have multiple names for the same field. All resources are in `compute.googleapis.com`. These field names are used by `BatchGetAssetsHistory`, `ExportAssets`, and `ListAssets`.

Resource type | Current field name (recommended) | Legacy field name  
---|---|---  
`BackendBucket` | `cdnPolicy.bypassCacheOnRequestHeaders` | `cdnPolicy.bypassCacheOnRequestHeader`  
`cdnPolicy.includeHttpHeaders` | `cdnPolicy.includeHttpHeader`  
`customResponseHeaders` | `customResponseHeader`  
`BackendService` | `cdnPolicy.bypassCacheOnRequestHeaders` | `cdnPolicy.bypassCacheOnRequestHeader`  
`cdnPolicy.cacheKeyPolicy.includeHttpHeaders` | `cdnPolicy.cacheKeyPolicy.includeHttpHeader`  
`cdnPolicy.cacheKeyPolicy.includeNamedCookies` | `cdnPolicy.cacheKeyPolicy.includeNamedCookie`  
`customResponseHeaders` | `customResponseHeader`  
`securitySettings.clientTlsPolicy` | `securitySettings.authentication`  
`securitySettings.subjectAltNames` | `securitySettings.subjectAltName`  
`ExternalVpnGateway` | `interfaces` | `interface`  
`FirewallPolicy` | `rules.match.srcSecureTags` | `rules.match.srcSecureTag`  
`targetSecureTags` | `targetSecureTag`  
`ForwardingRule` | `metadataFilters` | `metadataFilter`  
`GlobalAddress` | `users` | `user`  
`GlobalForwardingRule` | `metadataFilters` | `metadataFilter`  
`Image` | `shieldedInstanceInitialState.dbs` | `shieldedInstanceInitialState.db`  
`shieldedInstanceInitialState.dbxs` | `shieldedInstanceInitialState.dbx`  
`shieldedInstanceInitialState.keks` | `shieldedInstanceInitialState.kek`  
`Instance` | `disks.initializeParams.licenses` | `disks.initializeParams.license`  
`disks.initializeParams.resourcePolicies` | `disks.initializeParams.resourcePolicy`  
`disks.shieldedInstanceInitialState.dbs` | `disks.shieldedInstanceInitialState.db`  
`disks.shieldedInstanceInitialState.dbxs` | `disks.shieldedInstanceInitialState.dbx`  
`disks.shieldedInstanceInitialState.keks` | `disks.shieldedInstanceInitialState.kek`  
`networkInterfaces.ipv6AccessConfigs` | `networkInterfaces.ipv6AccessConfig`  
`reservationAffinity` | `allocationAffinity`  
`InstanceTemplate` | `properties.disks.initializeParams.licenses` | `properties.disks.initializeParams.license`  
`properties.disks.initializeParams.resourcePolicies` | `properties.disks.initializeParams.resourcePolicy`  
`properties.disks.shieldedInstanceInitialState.dbs` | `properties.disks.shieldedInstanceInitialState.db`  
`properties.disks.shieldedInstanceInitialState.dbxs` | `properties.disks.shieldedInstanceInitialState.dbx`  
`properties.disks.shieldedInstanceInitialState.keks` | `properties.disks.shieldedInstanceInitialState.kek`  
`properties.networkInterfaces` | `properties.networkInterface`  
`properties.reservationAffinity` | `properties.allocationAffinity`  
`properties.resourcePolicies` | `properties.resourcePolicy`  
`Interconnect` | `circuitInfos` | `circuitInfo`  
`InterconnectAttachment` | `candidateIpv6Subnets` | `candidateIpv6Subnet`  
`ipsecInternalAddresses` | `ipsecInternalAddress`  
`NodeTemplate` | `accelerators` | `accelerator`  
`disks` | `disk`  
`PacketMirroring` | `filter.cidrRanges` | `filter.cidrRange`  
`filter.ipProtocols` | `filter.ipProtocol`  
`network` | `mirroredNetwork`  
`RegionBackendService` | `cdnPolicy.bypassCacheOnRequestHeaders` | `cdnPolicy.bypassCacheOnRequestHeader`  
`cdnPolicy.cacheKeyPolicy.includeHttpHeaders` | `cdnPolicy.cacheKeyPolicy.includeHttpHeader`  
`cdnPolicy.cacheKeyPolicy.includeNamedCookies` | `cdnPolicy.cacheKeyPolicy.includeNamedCookie`  
`customResponseHeaders` | `customResponseHeader`  
`securitySettings.clientTlsPolicy` | `securitySettings.authentication`  
`securitySettings.subjectAltNames` | `securitySettings.subjectAltName`  
`ResourcePolicy` | `resourceStatus.instanceSchedulePolicy` | `resourceStatus.instanceSchedulePolicyStatus`  
`snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks` | `snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeek`  
`snapshotSchedulePolicy.snapshotProperties.storageLocations` | `snapshotSchedulePolicy.snapshotProperties.storageLocation`  
`Route` | `asPaths` | `asPath`  
`Router` | `nats.drainNatIps` | `nats.drainNatIp`  
`nats.rules` | `nats.rule`  
`SecurityPolicy` | `rules` | `rule`  
`headerAction.requestHeadersToAdds` | `headerAction.requestHeadersToAdd`  
`match.config.srcIpRanges` | `match.config.srcIpRange`  
`SslPolicy` | `customFeatures` | `customFeature`  
`enabledFeatures` | `enabledFeature`  
`warnings` | `warning`  
`TargetHttpProxy` | `authorizationPolicy` | `authorization`  
`serverTlsPolicy` | `authentication`  
`UrlMap` | `pathMatchers.routeRules.routeAction.corsPolicy.allowHeaders` | `pathMatchers.routeRules.routeAction.corsPolicy.allowHeader`  
`pathMatchers.routeRules.routeAction.corsPolicy.allowMethods` | `pathMatchers.routeRules.routeAction.corsPolicy.allowMethod`  
`pathMatchers.routeRules.routeAction.corsPolicy.allowOrigins` | `pathMatchers.routeRules.routeAction.corsPolicy.allowOrigin`  
`pathMatchers.routeRules.routeAction.corsPolicy.allowOriginRegexes` | `pathMatchers.routeRules.routeAction.corsPolicy.allowOriginRegex`  
`pathMatchers.routeRules.routeAction.corsPolicy.exposeHeaders` | `pathMatchers.routeRules.routeAction.corsPolicy.exposeHeader`  
`pathMatchers.routeRules.routeAction.retryPolicy.retryConditions` | `pathMatchers.routeRules.routeAction.retryPolicy.retryCondition`  
`pathMatchers.routeRules.routeAction.weightedBackendServices` | `pathMatchers.routeRules.routeAction.weightedBackendService`  
`pathMatchers.routeRules.service` | `pathMatchers.routeRules.backendService`  
`VpnGateway` | `vpnInterfaces` | `vpnInterface`  
  
## Resource types with the deprecated kmsKey field

This section lists all the resource types which have the legacy `kmsKey` field populated in [ResourceSearchResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#resourcesearchresult) while calling [SearchAllResources API](https://docs.cloud.google.com/asset-inventory/docs/reference/rpc/google.cloud.asset.v1#google.cloud.asset.v1.AssetService.SearchAllResources) for backward-compatibility. The new `kmsKeys` field can be used to retrieve Cloud KMS key information.

Service | Resource types  
---|---  
**Artifact Registry** | 

  * ` artifactregistry.googleapis.com/Repository `

  
**BigQuery** | 

  * ` bigquery.googleapis.com/Dataset `
  * ` bigquery.googleapis.com/Table `
  * ` bigquery.googleapis.com/Model `

  
**Bigtable** | 

  * ` bigtableadmin.googleapis.com/Backup `
  * ` bigtableadmin.googleapis.com/Cluster `

  
**Managed Service for Apache Airflow** | 

  * ` composer.googleapis.com/Environment `

  
**Cloud Run functions** | 

  * ` cloudfunctions.googleapis.com/CloudFunction `

  
**Cloud Healthcare API** | 

  * ` healthcare.googleapis.com/Dataset `

  
**Cloud Logging** | 

  * ` logging.googleapis.com/LogBucket `

  
**Cloud Run** | 

  * ` run.googleapis.com/Revision `

  
**Spanner** | 

  * ` spanner.googleapis.com/Database `

  
**Cloud SQL** | 

  * ` sqladmin.googleapis.com/Instance `
  * ` sqladmin.googleapis.com/BackupRun `

  
**Cloud Storage** | 

  * ` storage.googleapis.com/Bucket `

  
**Compute Engine** | 

  * ` compute.googleapis.com/Disk `
  * ` compute.googleapis.com/Image `

  
**Dataflow** | 

  * ` dataflow.googleapis.com/Job `

  
**Managed Service for Apache Spark** | 

  * ` dataproc.googleapis.com/Cluster `

  
**Dataproc Metastore** | 

  * ` metastore.googleapis.com/Service `

  
**Datastream** | 

  * ` datastream.googleapis.com/Stream `

  
**Dialogflow CX** | 

  * ` dialogflow.googleapis.com/LocationSettings `

  
**Document AI** | 

  * ` documentai.googleapis.com/HumanReviewConfig `
  * ` documentai.googleapis.com/Processor `
  * ` documentai.googleapis.com/ProcessorVersion `

  
**Memorystore for Redis** | 

  * ` redis.googleapis.com/Instance `

  
**Pub/Sub** | 

  * ` pubsub.googleapis.com/Topic `

  
**Vertex AI** | 

  * ` aiplatform.googleapis.com/BatchPredictionJob `
  * ` aiplatform.googleapis.com/CustomJob `
  * ` aiplatform.googleapis.com/DataLabelingJob `
  * ` aiplatform.googleapis.com/Dataset `
  * ` aiplatform.googleapis.com/Endpoint `
  * ` aiplatform.googleapis.com/HyperparameterTuningJob `
  * ` aiplatform.googleapis.com/MetadataStore `
  * ` aiplatform.googleapis.com/Model `
  * ` aiplatform.googleapis.com/ModelDeploymentMonitoringJob `
  * ` aiplatform.googleapis.com/PipelineJob `
  * ` aiplatform.googleapis.com/TrainingPipeline `

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
