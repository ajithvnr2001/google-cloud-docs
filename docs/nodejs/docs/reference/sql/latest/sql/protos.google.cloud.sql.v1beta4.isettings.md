---
url: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.isettings
title: Interface protos.google.cloud.sql.v1beta4.ISettings (0.29.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:58.892892+00:00
---

# Interface protos.google.cloud.sql.v1beta4.ISettings (0.29.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.isettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.sql.v1beta4.ISettings (0.29.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.25.0  0.23.0  0.19.1  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.4.0 

Properties of a Settings.

## Package

[@google-cloud/sql](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)

## Properties 

### acceleratedReplicaMode
    
    
    acceleratedReplicaMode?: (google.protobuf.IBoolValue|null);

Settings acceleratedReplicaMode

### activationPolicy
    
    
    activationPolicy?: (google.cloud.sql.v1beta4.Settings.SqlActivationPolicy|keyof typeof google.cloud.sql.v1beta4.Settings.SqlActivationPolicy|null);

Settings activationPolicy

### activeDirectoryConfig
    
    
    activeDirectoryConfig?: (google.cloud.sql.v1beta4.ISqlActiveDirectoryConfig|null);

Settings activeDirectoryConfig

### advancedMachineFeatures
    
    
    advancedMachineFeatures?: (google.cloud.sql.v1beta4.IAdvancedMachineFeatures|null);

Settings advancedMachineFeatures

### authorizedGaeApplications
    
    
    authorizedGaeApplications?: (string[]|null);

Settings authorizedGaeApplications

### autoUpgradeEnabled
    
    
    autoUpgradeEnabled?: (boolean|null);

Settings autoUpgradeEnabled

### availabilityType
    
    
    availabilityType?: (google.cloud.sql.v1beta4.SqlAvailabilityType|keyof typeof google.cloud.sql.v1beta4.SqlAvailabilityType|null);

Settings availabilityType

### backupConfiguration
    
    
    backupConfiguration?: (google.cloud.sql.v1beta4.IBackupConfiguration|null);

Settings backupConfiguration

### collation
    
    
    collation?: (string|null);

Settings collation

### connectionPoolConfig
    
    
    connectionPoolConfig?: (google.cloud.sql.v1beta4.IConnectionPoolConfig|null);

Settings connectionPoolConfig

### connectorEnforcement
    
    
    connectorEnforcement?: (google.cloud.sql.v1beta4.Settings.ConnectorEnforcement|keyof typeof google.cloud.sql.v1beta4.Settings.ConnectorEnforcement|null);

Settings connectorEnforcement

### crashSafeReplicationEnabled
    
    
    crashSafeReplicationEnabled?: (google.protobuf.IBoolValue|null);

Settings crashSafeReplicationEnabled

### dataApiAccess
    
    
    dataApiAccess?: (google.cloud.sql.v1beta4.Settings.DataApiAccess|keyof typeof google.cloud.sql.v1beta4.Settings.DataApiAccess|null);

Settings dataApiAccess

### databaseFlags
    
    
    databaseFlags?: (google.cloud.sql.v1beta4.IDatabaseFlags[]|null);

Settings databaseFlags

### databaseReplicationEnabled
    
    
    databaseReplicationEnabled?: (google.protobuf.IBoolValue|null);

Settings databaseReplicationEnabled

### dataCacheConfig
    
    
    dataCacheConfig?: (google.cloud.sql.v1beta4.IDataCacheConfig|null);

Settings dataCacheConfig

### dataDiskProvisionedIops
    
    
    dataDiskProvisionedIops?: (number|Long|string|null);

Settings dataDiskProvisionedIops

### dataDiskProvisionedThroughput
    
    
    dataDiskProvisionedThroughput?: (number|Long|string|null);

Settings dataDiskProvisionedThroughput

### dataDiskSizeGb
    
    
    dataDiskSizeGb?: (google.protobuf.IInt64Value|null);

Settings dataDiskSizeGb

### dataDiskType
    
    
    dataDiskType?: (google.cloud.sql.v1beta4.SqlDataDiskType|keyof typeof google.cloud.sql.v1beta4.SqlDataDiskType|null);

Settings dataDiskType

### deletionProtectionEnabled
    
    
    deletionProtectionEnabled?: (google.protobuf.IBoolValue|null);

Settings deletionProtectionEnabled

### denyMaintenancePeriods
    
    
    denyMaintenancePeriods?: (google.cloud.sql.v1beta4.IDenyMaintenancePeriod[]|null);

Settings denyMaintenancePeriods

### edition
    
    
    edition?: (google.cloud.sql.v1beta4.Settings.Edition|keyof typeof google.cloud.sql.v1beta4.Settings.Edition|null);

Settings edition

### enableDataplexIntegration
    
    
    enableDataplexIntegration?: (google.protobuf.IBoolValue|null);

Settings enableDataplexIntegration

### enableGoogleMlIntegration
    
    
    enableGoogleMlIntegration?: (google.protobuf.IBoolValue|null);

Settings enableGoogleMlIntegration

### entraidConfig
    
    
    entraidConfig?: (google.cloud.sql.v1beta4.ISqlServerEntraIdConfig|null);

Settings entraidConfig

### finalBackupConfig
    
    
    finalBackupConfig?: (google.cloud.sql.v1beta4.IFinalBackupConfig|null);

Settings finalBackupConfig

### insightsConfig
    
    
    insightsConfig?: (google.cloud.sql.v1beta4.IInsightsConfig|null);

Settings insightsConfig

### ipConfiguration
    
    
    ipConfiguration?: (google.cloud.sql.v1beta4.IIpConfiguration|null);

Settings ipConfiguration

### kind
    
    
    kind?: (string|null);

Settings kind

### locationPreference
    
    
    locationPreference?: (google.cloud.sql.v1beta4.ILocationPreference|null);

Settings locationPreference

### maintenanceWindow
    
    
    maintenanceWindow?: (google.cloud.sql.v1beta4.IMaintenanceWindow|null);

Settings maintenanceWindow

### passwordValidationPolicy
    
    
    passwordValidationPolicy?: (google.cloud.sql.v1beta4.IPasswordValidationPolicy|null);

Settings passwordValidationPolicy

### performanceCaptureConfig
    
    
    performanceCaptureConfig?: (google.cloud.sql.v1beta4.IPerformanceCaptureConfig|null);

Settings performanceCaptureConfig

### pricingPlan
    
    
    pricingPlan?: (google.cloud.sql.v1beta4.SqlPricingPlan|keyof typeof google.cloud.sql.v1beta4.SqlPricingPlan|null);

Settings pricingPlan

### readPoolAutoScaleConfig
    
    
    readPoolAutoScaleConfig?: (google.cloud.sql.v1beta4.IReadPoolAutoScaleConfig|null);

Settings readPoolAutoScaleConfig

### replicationLagMaxSeconds
    
    
    replicationLagMaxSeconds?: (google.protobuf.IInt32Value|null);

Settings replicationLagMaxSeconds

### replicationType
    
    
    replicationType?: (google.cloud.sql.v1beta4.SqlReplicationType|keyof typeof google.cloud.sql.v1beta4.SqlReplicationType|null);

Settings replicationType

### retainBackupsOnDelete
    
    
    retainBackupsOnDelete?: (google.protobuf.IBoolValue|null);

Settings retainBackupsOnDelete

### settingsVersion
    
    
    settingsVersion?: (google.protobuf.IInt64Value|null);

Settings settingsVersion

### sqlServerAuditConfig
    
    
    sqlServerAuditConfig?: (google.cloud.sql.v1beta4.ISqlServerAuditConfig|null);

Settings sqlServerAuditConfig

### storageAutoResize
    
    
    storageAutoResize?: (google.protobuf.IBoolValue|null);

Settings storageAutoResize

### storageAutoResizeLimit
    
    
    storageAutoResizeLimit?: (google.protobuf.IInt64Value|null);

Settings storageAutoResizeLimit

### tier
    
    
    tier?: (string|null);

Settings tier

### timeZone
    
    
    timeZone?: (string|null);

Settings timeZone

### userLabels
    
    
    userLabels?: ({ [k: string]: string }|null);

Settings userLabels

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
