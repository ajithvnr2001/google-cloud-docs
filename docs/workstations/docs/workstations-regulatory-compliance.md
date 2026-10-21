---
url: https://docs.cloud.google.com/workstations/docs/workstations-regulatory-compliance/
title: Regulatory support in Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:05.856786+00:00
---

# Regulatory support in Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/workstations-regulatory-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Resources ](https://docs.cloud.google.com/workstations/docs/resources)



Send feedback 

#  Regulatory support in Cloud Workstations Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features, configurations and APIs in Cloud Workstations that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

Show AllData Boundary for ITARAW Regional Controls - Premium - US Data Boundary and SupportData Boundary for FedRAMP HighData Boundary for FedRAMP ModerateData Boundary for Impact Level 2 (IL2)Data Boundary for Impact Level 4 (IL4)Data Boundary for Impact Level 5 (IL5)EU Data Boundary with Access Justifications  
  
---  
  
## Data Boundary for ITAR

### Supported services

The following table lists the Cloud Workstations APIs and versions that meet the requirements of Data Boundary for ITAR. | Service | Version | Status  
---|---|---  
workstations.googleapis.com | v1 |  SUPPORTED   
workstations.googleapis.com | v1alpha |  SUPPORTED   
workstations.googleapis.com | v1beta |  SUPPORTED   
  
### Compliance supported regions

Cloud Workstations is available for Data Boundary for ITAR in the following Google Cloud regions:

  * us-central1
  * us-east1
  * us-east4
  * us-east5
  * us-west1
  * us-west4



### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Filtering and querying | 

  * `filter`
  * `pageToken`

  
Resource identification | 

  * `name`
  * `workstationClusterId`
  * `workstationConfigId`
  * `workstationId`

  
Resource scope | 

  * `parent`

  
Workstation cluster metadata and labels | 

  * `workstationCluster.annotations.key`
  * `workstationCluster.displayName`
  * `workstationCluster.etag`
  * `workstationCluster.labels.key`
  * `workstationCluster.labels.value`
  * `workstationCluster.name`

  
Workstation cluster networking | 

  * `workstationCluster.domainConfig.domain`
  * `workstationCluster.network`
  * `workstationCluster.privateClusterConfig.allowedProjects`
  * `workstationCluster.subnetwork`

  
Workstation configuration details | 

  * `workstationConfig.displayName`
  * `workstationConfig.etag`
  * `workstationConfig.name`
  * `workstationConfig.replicaZones`

  
Workstation container configuration | 

  * `workstationConfig.container.args`
  * `workstationConfig.container.command`
  * `workstationConfig.container.env.key`
  * `workstationConfig.container.env.value`
  * `workstationConfig.container.image`
  * `workstationConfig.container.workingDir`

  
Workstation encryption | 

  * `workstationConfig.encryptionKey.kmsKey`
  * `workstationConfig.encryptionKey.kmsKeyServiceAccount`

  
Workstation host configuration | 

  * `workstationConfig.host.gceInstance.machineType`
  * `workstationConfig.host.gceInstance.serviceAccount`
  * `workstationConfig.host.gceInstance.serviceAccountScopes`
  * `workstationConfig.host.gceInstance.startupScriptUri`
  * `workstationConfig.host.gceInstance.tags`

  
Workstation persistent storage | 

  * `workstationConfig.persistentDirectories.gcePd.diskType`
  * `workstationConfig.persistentDirectories.gcePd.fsType`
  * `workstationConfig.persistentDirectories.gcePd.sourceSnapshot`
  * `workstationConfig.persistentDirectories.mountPath`

  
  
  
  
## AW Regional Controls - Premium - US Data Boundary and Support

### Supported services

The following table lists the Cloud Workstations APIs and versions that meet the requirements of AW Regional Controls - Premium - US Data Boundary and Support. | Service | Version | Status  
---|---|---  
workstations.googleapis.com | v1 |  SUPPORTED   
workstations.googleapis.com | v1alpha |  SUPPORTED   
workstations.googleapis.com | v1beta |  SUPPORTED   
  
### Compliance supported regions

Cloud Workstations is available for AW Regional Controls - Premium - US Data Boundary and Support in the following Google Cloud regions:

  * us-central1
  * us-central2
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4



### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Filtering and pagination | 

  * `filter`
  * `pageToken`

  
Parent resource | 

  * `parent`

  
Resource identification | 

  * `name`
  * `workstationClusterId`
  * `workstationConfigId`
  * `workstationId`

  
Workstation cluster - metadata and labels | 

  * `workstationCluster.annotations.key`
  * `workstationCluster.annotations.value`
  * `workstationCluster.displayName`
  * `workstationCluster.labels.key`
  * `workstationCluster.labels.value`

  
Workstation cluster - network | 

  * `workstationCluster.domainConfig.domain`
  * `workstationCluster.network`
  * `workstationCluster.subnetwork`

  
Workstation cluster - security | 

  * `workstationCluster.privateClusterConfig.allowedProjects`
  * `workstationCluster.tags.key`
  * `workstationCluster.tags.value`

  
Workstation configuration - compute | 

  * `workstationConfig.host.gceInstance.accelerators.type`
  * `workstationConfig.host.gceInstance.boostConfigs.accelerators.type`
  * `workstationConfig.host.gceInstance.boostConfigs.machineType`
  * `workstationConfig.host.gceInstance.machineType`

  
Workstation configuration - container | 

  * `workstationConfig.container.args`
  * `workstationConfig.container.command`
  * `workstationConfig.container.image`
  * `workstationConfig.container.workingDir`

  
Workstation configuration - security and access | 

  * `workstationConfig.encryptionKey.kmsKey`
  * `workstationConfig.encryptionKey.kmsKeyServiceAccount`
  * `workstationConfig.host.gceInstance.serviceAccount`
  * `workstationConfig.host.gceInstance.serviceAccountScopes`
  * `workstationConfig.host.gceInstance.vmTags.key`
  * `workstationConfig.host.gceInstance.vmTags.value`

  
Workstation configuration - storage | 

  * `workstationConfig.ephemeralDirectories.gcePd.diskType`
  * `workstationConfig.ephemeralDirectories.mountPath`
  * `workstationConfig.persistentDirectories.gcePd.diskType`
  * `workstationConfig.persistentDirectories.gcePd.sourceSnapshot`
  * `workstationConfig.persistentDirectories.mountPath`

  
  
  
  
## Data Boundary for FedRAMP High

### Supported services

The following table lists the Cloud Workstations APIs and versions that meet the requirements of Data Boundary for FedRAMP High. | Service | Version | Status  
---|---|---  
workstations.googleapis.com | v1 |  SUPPORTED   
workstations.googleapis.com | v1alpha |  SUPPORTED   
workstations.googleapis.com | v1beta |  SUPPORTED   
  
### Compliance supported regions

Cloud Workstations is available for Data Boundary for FedRAMP High in the following Google Cloud regions:

  * us-central1
  * us-central2
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4



### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Filtering and pagination | 

  * `filter`
  * `pageToken`

  
Parent resource | 

  * `parent`

  
Resource configuration - compute instance settings | 

  * `workstationConfig.host.gceInstance.boostConfigs.machineType`
  * `workstationConfig.host.gceInstance.instanceMetadata.key`
  * `workstationConfig.host.gceInstance.instanceMetadata.value`
  * `workstationConfig.host.gceInstance.machineType`
  * `workstationConfig.host.gceInstance.startupScriptUri`
  * `workstationConfig.host.gceInstance.tags`

  
Resource configuration - container settings | 

  * `workstationConfig.container.args`
  * `workstationConfig.container.command`
  * `workstationConfig.container.env.key`
  * `workstationConfig.container.env.value`
  * `workstationConfig.container.image`
  * `workstationConfig.container.workingDir`

  
Resource configuration - general | 

  * `etag`

  
Resource configuration - labels and annotations | 

  * `workstation.annotations.key`
  * `workstation.annotations.value`
  * `workstation.labels.key`
  * `workstation.labels.value`
  * `workstationCluster.annotations.key`
  * `workstationCluster.annotations.value`

  
Resource configuration - networking | 

  * `workstationCluster.network`
  * `workstationCluster.subnetwork`
  * `workstationConfig.host.gceInstance.serviceAccount`
  * `workstationConfig.host.gceInstance.serviceAccountScopes`

  
Resource configuration - security | 

  * `workstationCluster.privateClusterConfig.allowedProjects`
  * `workstationConfig.encryptionKey.kmsKey`
  * `workstationConfig.encryptionKey.kmsKeyServiceAccount`

  
Resource configuration - storage | 

  * `workstationConfig.ephemeralDirectories.gcePd.diskType`
  * `workstationConfig.ephemeralDirectories.gcePd.sourceSnapshot`
  * `workstationConfig.ephemeralDirectories.mountPath`
  * `workstationConfig.persistentDirectories.gcePd.diskType`
  * `workstationConfig.persistentDirectories.gcePd.fsType`
  * `workstationConfig.persistentDirectories.gcePd.sourceSnapshot`

  
Resource identification | 

  * `name`
  * `workstationClusterId`
  * `workstationConfigId`
  * `workstationId`

  
  
  
  
## Data Boundary for FedRAMP Moderate

### Supported services

The following table lists the Cloud Workstations APIs and versions that meet the requirements of Data Boundary for FedRAMP Moderate. | Service | Version | Status  
---|---|---  
workstations.googleapis.com | v1 |  SUPPORTED   
workstations.googleapis.com | v1alpha |  SUPPORTED   
workstations.googleapis.com | v1beta |  SUPPORTED   
  
### Compliance supported regions

Cloud Workstations is available for Data Boundary for FedRAMP Moderate in the following Google Cloud regions:

  * us-central1
  * us-central2
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4



### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Filtering and pagination | 

  * `filter`
  * `pageToken`

  
Resource identification | 

  * `name`
  * `parent`
  * `workstationClusterId`
  * `workstationConfigId`
  * `workstationId`

  
Resource updates | 

  * `etag`
  * `updateMask.paths`
  * `workstation.etag`
  * `workstationCluster.etag`
  * `workstationConfig.etag`

  
Workstation cluster - identifiers and urls | 

  * `workstationCluster.consoleBaseUrl`
  * `workstationCluster.workstationAuthorizationUrl`
  * `workstationCluster.workstationLaunchUrl`

  
Workstation cluster - metadata and labels | 

  * `workstationCluster.annotations.key`
  * `workstationCluster.annotations.value`
  * `workstationCluster.displayName`
  * `workstationCluster.labels.key`
  * `workstationCluster.labels.value`
  * `workstationCluster.tags.key`

  
Workstation cluster - networking | 

  * `workstationCluster.domainConfig.domain`
  * `workstationCluster.network`
  * `workstationCluster.privateClusterConfig.allowedProjects`
  * `workstationCluster.subnetwork`

  
Workstation configuration - compute | 

  * `workstationConfig.host.gceInstance.accelerators.type`
  * `workstationConfig.host.gceInstance.boostConfigs.accelerators.type`
  * `workstationConfig.host.gceInstance.boostConfigs.id`
  * `workstationConfig.host.gceInstance.boostConfigs.machineType`
  * `workstationConfig.host.gceInstance.machineType`
  * `workstationConfig.host.gceInstance.serviceAccountScopes`

  
Workstation configuration - container | 

  * `workstationConfig.container.args`
  * `workstationConfig.container.command`
  * `workstationConfig.container.env.key`
  * `workstationConfig.container.env.value`
  * `workstationConfig.container.image`
  * `workstationConfig.container.workingDir`

  
Workstation configuration - security | 

  * `workstationConfig.encryptionKey.kmsKey`
  * `workstationConfig.encryptionKey.kmsKeyServiceAccount`
  * `workstationConfig.host.gceInstance.serviceAccount`
  * `workstationConfig.host.gceInstance.tags`
  * `workstationConfig.host.gceInstance.vmTags.key`
  * `workstationConfig.host.gceInstance.vmTags.value`

  
Workstation configuration - storage | 

  * `workstationConfig.ephemeralDirectories.gcePd.sourceSnapshot`
  * `workstationConfig.ephemeralDirectories.mountPath`
  * `workstationConfig.persistentDirectories.gceHd.sourceSnapshot`
  * `workstationConfig.persistentDirectories.gcePd.diskType`
  * `workstationConfig.persistentDirectories.gcePd.sourceSnapshot`
  * `workstationConfig.persistentDirectories.mountPath`

  
  
  
  
## Data Boundary for Impact Level 2 (IL2)

### Supported services

The following table lists the Cloud Workstations APIs and versions that meet the requirements of Data Boundary for Impact Level 2 (IL2). | Service | Version | Status  
---|---|---  
workstations.googleapis.com | v1 |  SUPPORTED   
workstations.googleapis.com | v1alpha |  SUPPORTED   
workstations.googleapis.com | v1beta |  SUPPORTED   
  
### Compliance supported regions

Cloud Workstations is available for Data Boundary for Impact Level 2 (IL2) in the following Google Cloud regions:

  * us-central1
  * us-central2
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4



### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Filtering and pagination | 

  * `filter`
  * `pageToken`

  
Resource identification | 

  * `name`
  * `parent`
  * `workstationClusterId`
  * `workstationConfigId`
  * `workstationId`

  
Update mask | 

  * `updateMask.paths`

  
Workstation cluster details | 

  * `workstationCluster.displayName`
  * `workstationCluster.domainConfig.domain`
  * `workstationCluster.etag`
  * `workstationCluster.name`
  * `workstationCluster.network`
  * `workstationCluster.subnetwork`

  
Workstation cluster network and security | 

  * `workstationCluster.annotations.key`
  * `workstationCluster.annotations.value`
  * `workstationCluster.privateClusterConfig.allowedProjects`
  * `workstationCluster.tags.key`
  * `workstationCluster.tags.value`
  * `workstationCluster.workstationAuthorizationUrl`

  
Workstation configuration details | 

  * `workstation.displayName`
  * `workstation.name`
  * `workstation.sourceWorkstation`
  * `workstationConfig.displayName`
  * `workstationConfig.etag`
  * `workstationConfig.name`

  
Workstation container configuration | 

  * `workstationConfig.container.args`
  * `workstationConfig.container.command`
  * `workstationConfig.container.env.key`
  * `workstationConfig.container.env.value`
  * `workstationConfig.container.image`
  * `workstationConfig.container.workingDir`

  
Workstation host configuration | 

  * `workstationConfig.host.gceInstance.accelerators.type`
  * `workstationConfig.host.gceInstance.instanceMetadata.key`
  * `workstationConfig.host.gceInstance.machineType`
  * `workstationConfig.host.gceInstance.serviceAccount`
  * `workstationConfig.host.gceInstance.startupScriptUri`
  * `workstationConfig.host.gceInstance.tags`

  
Workstation labels and annotations | 

  * `workstation.annotations.key`
  * `workstation.annotations.value`
  * `workstation.labels.key`
  * `workstation.labels.value`
  * `workstationConfig.labels.key`
  * `workstationConfig.labels.value`

  
Workstation persistent storage | 

  * `workstation.persistentDirectories.gcePd.name`
  * `workstation.persistentDirectories.mountPath`
  * `workstationConfig.persistentDirectories.gceHd.sourceSnapshot`
  * `workstationConfig.persistentDirectories.gcePd.fsType`
  * `workstationConfig.persistentDirectories.gcePd.sourceSnapshot`
  * `workstationConfig.persistentDirectories.mountPath`

  
  
  
  
## Data Boundary for Impact Level 4 (IL4)

### Supported services

The following table lists the Cloud Workstations APIs and versions that meet the requirements of Data Boundary for Impact Level 4 (IL4). | Service | Version | Status  
---|---|---  
workstations.googleapis.com | v1 |  SUPPORTED   
workstations.googleapis.com | v1alpha |  SUPPORTED   
workstations.googleapis.com | v1beta |  SUPPORTED   
  
### Compliance supported regions

Cloud Workstations is available for Data Boundary for Impact Level 4 (IL4) in the following Google Cloud regions:

  * us-central1
  * us-central2
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4



### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Filtering and sorting | 

  * `filter`
  * `pageToken`

  
Metadata and labels | 

  * `workstation.labels.key`
  * `workstation.labels.value`
  * `workstationCluster.annotations.key`
  * `workstationCluster.annotations.value`
  * `workstationCluster.labels.key`
  * `workstationCluster.labels.value`

  
Parent resource specification | 

  * `parent`

  
Resource identification | 

  * `name`
  * `workstationClusterId`
  * `workstationConfigId`
  * `workstationId`

  
Resource naming conventions | 

  * `workstation.name`
  * `workstationCluster.name`
  * `workstationConfig.name`

  
Workstation cluster - networking and domain | 

  * `workstationCluster.domainConfig.domain`
  * `workstationCluster.network`
  * `workstationCluster.privateClusterConfig.allowedProjects`
  * `workstationCluster.subnetwork`

  
Workstation configuration - compute resources | 

  * `workstationConfig.host.gceInstance.accelerators.type`
  * `workstationConfig.host.gceInstance.boostConfigs.accelerators.type`
  * `workstationConfig.host.gceInstance.boostConfigs.id`
  * `workstationConfig.host.gceInstance.boostConfigs.machineType`
  * `workstationConfig.host.gceInstance.machineType`

  
Workstation configuration - container and execution | 

  * `workstationConfig.container.args`
  * `workstationConfig.container.command`
  * `workstationConfig.container.env.key`
  * `workstationConfig.container.env.value`
  * `workstationConfig.container.image`
  * `workstationConfig.container.workingDir`

  
Workstation configuration - security and access control | 

  * `workstationConfig.encryptionKey.kmsKey`
  * `workstationConfig.encryptionKey.kmsKeyServiceAccount`
  * `workstationConfig.host.gceInstance.serviceAccount`
  * `workstationConfig.host.gceInstance.serviceAccountScopes`
  * `workstationConfig.host.gceInstance.tags`
  * `workstationConfig.host.gceInstance.vmTags.key`

  
Workstation configuration - storage | 

  * `workstationConfig.ephemeralDirectories.gcePd.sourceImage`
  * `workstationConfig.ephemeralDirectories.mountPath`
  * `workstationConfig.persistentDirectories.gcePd.diskType`
  * `workstationConfig.persistentDirectories.gcePd.fsType`
  * `workstationConfig.persistentDirectories.gcePd.sourceSnapshot`
  * `workstationConfig.persistentDirectories.mountPath`

  
  
  
  
## Data Boundary for Impact Level 5 (IL5)

### Supported services

The following table lists the Cloud Workstations APIs and versions that meet the requirements of Data Boundary for Impact Level 5 (IL5). | Service | Version | Status  
---|---|---  
workstations.googleapis.com | v1 |  SUPPORTED   
workstations.googleapis.com | v1alpha |  SUPPORTED   
workstations.googleapis.com | v1beta |  SUPPORTED   
  
### Compliance supported regions

Cloud Workstations is available for Data Boundary for Impact Level 5 (IL5) in the following Google Cloud regions:

  * us-central1
  * us-central2
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4



### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Advanced configuration - container | 

  * `workstationConfig.container.args`
  * `workstationConfig.container.command`
  * `workstationConfig.container.env.value`
  * `workstationConfig.container.workingDir`
  * `workstationConfig.replicaZones`

  
Advanced configuration - host | 

  * `workstationConfig.host.gceInstance.boostConfigs.machineType`
  * `workstationConfig.host.gceInstance.instanceMetadata.key`
  * `workstationConfig.host.gceInstance.reservationAffinity.key`
  * `workstationConfig.host.gceInstance.startupScriptUri`
  * `workstationConfig.host.gceInstance.tags`
  * `workstationConfig.host.gceInstance.vmTags.key`

  
Filtering and pagination | 

  * `filter`
  * `pageToken`

  
Metadata and labels | 

  * `workstation.annotations.key`
  * `workstation.annotations.value`
  * `workstation.labels.key`
  * `workstation.labels.value`
  * `workstationConfig.labels.key`
  * `workstationConfig.labels.value`

  
Resource configuration - Workstation | 

  * `workstation.displayName`
  * `workstation.env.key`
  * `workstation.env.value`
  * `workstation.persistentDirectories.gcePd.name`
  * `workstation.persistentDirectories.mountPath`
  * `workstation.sourceWorkstation`

  
Resource configuration - Workstation cluster | 

  * `workstationCluster.consoleBaseUrl`
  * `workstationCluster.domainConfig.domain`
  * `workstationCluster.network`
  * `workstationCluster.privateClusterConfig.allowedProjects`
  * `workstationCluster.subnetwork`
  * `workstationCluster.workstationLaunchUrl`

  
Resource configuration - Workstation configuration | 

  * `workstationConfig.container.env.key`
  * `workstationConfig.container.image`
  * `workstationConfig.encryptionKey.kmsKey`
  * `workstationConfig.host.gceInstance.machineType`
  * `workstationConfig.host.gceInstance.serviceAccount`
  * `workstationConfig.persistentDirectories.gcePd.diskType`

  
Resource identification | 

  * `name`
  * `parent`
  * `workstationClusterId`
  * `workstationConfigId`
  * `workstationId`

  
Resource management | 

  * `boostConfig`
  * `updateMask.paths`
  * `workstation.etag`
  * `workstationCluster.etag`
  * `workstationConfig.etag`

  
  
  
  
## EU Data Boundary with Access Justifications

### Supported services

The following table lists the Cloud Workstations APIs and versions that meet the requirements of EU Data Boundary with Access Justifications. | Service | Version | Status  
---|---|---  
workstations.googleapis.com | v1 |  SUPPORTED   
workstations.googleapis.com | v1alpha |  SUPPORTED   
workstations.googleapis.com | v1beta |  SUPPORTED   
  
### Compliance supported regions

Cloud Workstations is available for EU Data Boundary with Access Justifications in the following Google Cloud regions:

  * europe-central2
  * europe-north1
  * europe-north2
  * europe-southwest1
  * europe-west1
  * europe-west10
  * europe-west12
  * europe-west3
  * europe-west4
  * europe-west8
  * europe-west9



### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Filtering and pagination | 

  * `filter`
  * `pageToken`

  
Parent resource | 

  * `parent`

  
Resource configuration - compute instance specifics | 

  * `workstationConfig.host.gceInstance.accelerators.type`
  * `workstationConfig.host.gceInstance.instanceMetadata.key`
  * `workstationConfig.host.gceInstance.machineType`
  * `workstationConfig.host.gceInstance.startupScriptUri`
  * `workstationConfig.host.gceInstance.tags`
  * `workstationConfig.host.gceInstance.vmTags.key`

  
Resource configuration - container specifics | 

  * `workstationConfig.container.args`
  * `workstationConfig.container.command`
  * `workstationConfig.container.env.key`
  * `workstationConfig.container.env.value`
  * `workstationConfig.container.image`
  * `workstationConfig.container.workingDir`

  
Resource configuration - general | 

  * `workstation.displayName`
  * `workstation.name`
  * `workstationCluster.displayName`
  * `workstationCluster.name`
  * `workstationConfig.displayName`
  * `workstationConfig.name`

  
Resource configuration - labels and annotations | 

  * `workstation.annotations.key`
  * `workstation.annotations.value`
  * `workstation.labels.key`
  * `workstation.labels.value`
  * `workstationConfig.labels.key`
  * `workstationConfig.labels.value`

  
Resource configuration - networking | 

  * `workstationCluster.network`
  * `workstationCluster.subnetwork`
  * `workstationConfig.host.gceInstance.serviceAccount`
  * `workstationConfig.host.gceInstance.serviceAccountScopes`

  
Resource configuration - security and encryption | 

  * `workstationCluster.privateClusterConfig.allowedProjects`
  * `workstationConfig.encryptionKey.kmsKey`
  * `workstationConfig.encryptionKey.kmsKeyServiceAccount`

  
Resource configuration - storage and persistence | 

  * `workstation.persistentDirectories.gcePd.name`
  * `workstation.persistentDirectories.mountPath`
  * `workstationConfig.persistentDirectories.gceHd.sourceSnapshot`
  * `workstationConfig.persistentDirectories.gcePd.diskType`
  * `workstationConfig.persistentDirectories.gcePd.fsType`
  * `workstationConfig.persistentDirectories.mountPath`

  
Resource identification | 

  * `name`
  * `workstationClusterId`
  * `workstationConfigId`
  * `workstationId`

  
  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
