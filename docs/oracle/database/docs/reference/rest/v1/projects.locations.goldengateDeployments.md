---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments
title: REST Resource: projects.locations.goldengateDeployments \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:50.775004+00:00
---

# REST Resource: projects.locations.goldengateDeployments  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.goldengateDeployments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GoldengateDeployment
    * JSON representation
  * GoldengateDeploymentProperties
    * JSON representation
  * GoldengateDeploymentLifecycleState
  * LicenseModel
  * GoldengateOggDeployment
    * JSON representation
  * CredentialStore
  * GoldengateGroupToRolesMapping
    * JSON representation
  * GoldengateMaintenanceWindow
    * JSON representation
  * GoldengateMaintenanceConfig
    * JSON representation
  * GoldengateDeploymentLifecycleSubState
  * GoldengateDeploymentCategory
  * DeploymentDiagnosticData
    * JSON representation
  * DiagnosticState
  * GoldengateBackupSchedule
    * JSON representation
  * FrequencyBackupScheduled
  * NextMaintenanceActionType
  * IngressIp
    * JSON representation
  * GoldengateDeploymentRoleType
  * GoldengateDeploymentLock
    * JSON representation
  * LockType
  * GoldengatePlacement
    * JSON representation
  * Methods



## Resource: GoldengateDeployment

GoldengateDeployment Goldengate Deployment resource model.

JSON representation  
---  
      
    
    {
      "name": string,
      "properties": {
        object ([GoldengateDeploymentProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateDeploymentProperties))
      },
      "gcpOracleZone": string,
      "labels": {
        string: string,
        ...
      },
      "odbNetwork": string,
      "odbSubnet": string,
      "entitlementId": string,
      "displayName": string,
      "createTime": string,
      "ociUrl": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the GoldengateDeployment resource in the following format: projects/{project}/locations/{region}/goldengateDeployments/{goldengateDeployment}  
`properties` |  `object (`[GoldengateDeploymentProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateDeploymentProperties)`)` Required. The properties of the GoldengateDeployment.  
`gcpOracleZone` |  `string` Optional. The GCP Oracle zone where Oracle GoldengateDeployment is hosted. Example: us-east4-b-r2. If not specified, the system will pick a zone based on availability.  
`labels` |  `map (key: string, value: string)` Optional. The labels or tags associated with the GoldengateDeployment.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`odbNetwork` |  `string` Optional. The name of the OdbNetwork associated with the GoldengateDeployment.  
`odbSubnet` |  `string` Required. The name of the OdbSubnet associated with the GoldengateDeployment for IP allocation.  
`entitlementId` |  `string` Output only. The ID of the subscription entitlement associated with the GoldengateDeployment  
`displayName` |  `string` Required. The display name for the GoldengateDeployment.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the GoldengateDeployment was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`ociUrl` |  `string` Output only. HTTPS link to OCI resources exposed to Customer via UI Interface.  
  
## GoldengateDeploymentProperties

Properties of GoldengateDeployment.

JSON representation  
---  
      
    
    {
      "ocid": string,
      "lifecycleState": enum ([GoldengateDeploymentLifecycleState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateDeploymentLifecycleState)),
      "licenseModel": enum ([LicenseModel](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#LicenseModel)),
      "environmentType": string,
      "cpuCoreCount": integer,
      "isAutoScalingEnabled": boolean,
      "description": string,
      "deploymentType": string,
      "oggData": {
        object ([GoldengateOggDeployment](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateOggDeployment))
      },
      "maintenanceWindow": {
        object ([GoldengateMaintenanceWindow](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateMaintenanceWindow))
      },
      "maintenanceConfig": {
        object ([GoldengateMaintenanceConfig](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateMaintenanceConfig))
      },
      "fqdn": string,
      "lifecycleSubState": enum ([GoldengateDeploymentLifecycleSubState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateDeploymentLifecycleSubState)),
      "category": enum ([GoldengateDeploymentCategory](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateDeploymentCategory)),
      "deploymentBackupId": string,
      "updateTime": string,
      "lifecycleDetails": string,
      "healthy": boolean,
      "loadBalancerSubnetId": string,
      "loadBalancerId": string,
      "nsgIds": [
        string
      ],
      "isPublic": boolean,
      "publicIpAddress": string,
      "privateIpAddress": string,
      "deploymentUrl": string,
      "isLatestVersion": boolean,
      "upgradeRequiredTime": string,
      "storageUtilizationBytes": string,
      "isStorageUtilizationLimitExceeded": boolean,
      "deploymentDiagnosticData": {
        object ([DeploymentDiagnosticData](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#DeploymentDiagnosticData))
      },
      "backupSchedule": {
        object ([GoldengateBackupSchedule](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateBackupSchedule))
      },
      "nextMaintenanceTime": string,
      "nextMaintenanceActionType": enum ([NextMaintenanceActionType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#NextMaintenanceActionType)),
      "nextMaintenanceDescription": string,
      "oggVersionSupportEndTime": string,
      "ingressIps": [
        {
          object ([IngressIp](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#IngressIp))
        }
      ],
      "deploymentRole": enum ([GoldengateDeploymentRoleType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateDeploymentRoleType)),
      "lastBackupScheduleTime": string,
      "nextBackupScheduleTime": string,
      "roleChangeTime": string,
      "locks": [
        {
          object ([GoldengateDeploymentLock](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateDeploymentLock))
        }
      ],
      "placements": [
        {
          object ([GoldengatePlacement](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengatePlacement))
        }
      ]
    }  
  
Fields  
---  
`ocid` |  `string` Output only. OCID of the GoldengateDeployment.  
`lifecycleState` |  `enum (`[GoldengateDeploymentLifecycleState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateDeploymentLifecycleState)`)` Output only. State of the GoldengateDeployment.  
`licenseModel` |  `enum (`[LicenseModel](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#LicenseModel)`)` Optional. The Oracle license model that applies to a Deployment.  
`environmentType` |  `string` Optional. The environment type of the GoldengateDeployment.  
`cpuCoreCount` |  `integer` Optional. The Minimum number of OCPUs to be made available for this Deployment.  
`isAutoScalingEnabled` |  `boolean` Optional. Indicates if auto scaling is enabled for the Deployment's CPU core count.  
`description` |  `string` Optional. The description of the GoldengateDeployment.  
`deploymentType` |  `string` Required. A valid Goldengate Deployment type. For a list of supported types, use the `ListGoldengateDeploymentTypes` operation.  
`oggData` |  `object (`[GoldengateOggDeployment](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateOggDeployment)`)` Required. The ogg data of the GoldengateDeployment.  
`maintenanceWindow` |  `object (`[GoldengateMaintenanceWindow](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateMaintenanceWindow)`)` Optional. The maintenance window of the GoldengateDeployment.  
`maintenanceConfig` |  `object (`[GoldengateMaintenanceConfig](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateMaintenanceConfig)`)` Optional. The maintenance configuration of the GoldengateDeployment.  
`fqdn` |  `string` Output only. The Fully Qualified Domain Name of the GoldengateDeployment.  
`lifecycleSubState` |  `enum (`[GoldengateDeploymentLifecycleSubState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateDeploymentLifecycleSubState)`)` Output only. The lifecycle sub-state of the GoldengateDeployment.  
`category` |  `enum (`[GoldengateDeploymentCategory](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateDeploymentCategory)`)` Output only. The category of the GoldengateDeployment.  
`deploymentBackupId` |  `string` Output only. The deployment backup id of the GoldengateDeployment.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the GoldengateDeployment was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lifecycleDetails` |  `string` Output only. The lifecycle details of the GoldengateDeployment.  
`healthy` |  `boolean` Output only. Whether the GoldengateDeployment is healthy.  
`loadBalancerSubnetId` |  `string` Output only. The load balancer subnet id of the GoldengateDeployment.  
`loadBalancerId` |  `string` Output only. The load balancer id of the GoldengateDeployment.  
`nsgIds[]` |  `string` Output only. The nsg ids of the GoldengateDeployment.  
`isPublic` |  `boolean` Output only. Whether the GoldengateDeployment is public.  
`publicIpAddress` |  `string` Output only. The public ip address of the GoldengateDeployment.  
`privateIpAddress` |  `string` Output only. The private ip address of the GoldengateDeployment.  
`deploymentUrl` |  `string` Output only. The deployment url of the GoldengateDeployment.  
`isLatestVersion` |  `boolean` Output only. Whether the GoldengateDeployment is of the latest version.  
`upgradeRequiredTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time upgrade required of the GoldengateDeployment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`storageUtilizationBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The storage utilization in bytes of the GoldengateDeployment.  
`isStorageUtilizationLimitExceeded` |  `boolean` Output only. Whether storage utilization limit is exceeded of the GoldengateDeployment.  
`deploymentDiagnosticData` |  `object (`[DeploymentDiagnosticData](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#DeploymentDiagnosticData)`)` Output only. The deployment diagnostic data of the GoldengateDeployment.  
`backupSchedule` |  `object (`[GoldengateBackupSchedule](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateBackupSchedule)`)` Output only. The backup schedule of the GoldengateDeployment.  
`nextMaintenanceTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time of next maintenance of the GoldengateDeployment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`nextMaintenanceActionType` |  `enum (`[NextMaintenanceActionType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#NextMaintenanceActionType)`)` Output only. The next maintenance action type of the GoldengateDeployment.  
`nextMaintenanceDescription` |  `string` Output only. The next maintenance description of the GoldengateDeployment.  
`oggVersionSupportEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time ogg version supported until of the GoldengateDeployment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`ingressIps[]` |  `object (`[IngressIp](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#IngressIp)`)` Output only. The ingress ips of the GoldengateDeployment.  
`deploymentRole` |  `enum (`[GoldengateDeploymentRoleType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateDeploymentRoleType)`)` Output only. The deployment role of the GoldengateDeployment.  
`lastBackupScheduleTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time last backup scheduled of the GoldengateDeployment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`nextBackupScheduleTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time next backup scheduled of the GoldengateDeployment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`roleChangeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the role of the GoldengateDeployment was changed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`locks[]` |  `object (`[GoldengateDeploymentLock](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateDeploymentLock)`)` Output only. The locks of the GoldengateDeployment.  
`placements[]` |  `object (`[GoldengatePlacement](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengatePlacement)`)` Output only. The placements of the GoldengateDeployment.  
  
## GoldengateDeploymentLifecycleState

The various lifecycle states of the GoldengateDeployment.

Enums  
---  
`GOLDENGATE_DEPLOYMENT_LIFECYCLE_STATE_UNSPECIFIED` | Default unspecified value.  
`CREATING` | The deployment is being created.  
`UPDATING` | The deployment is being updated.  
`ACTIVE` | The deployment is active.  
`INACTIVE` | The deployment is inactive.  
`DELETING` | The deployment is being deleted.  
`DELETED` | The deployment is deleted.  
`FAILED` | The deployment failed.  
`NEEDS_ATTENTION` | The deployment needs attention.  
`IN_PROGRESS` | The deployment is in progress.  
`CANCELLING` | The deployment is canceling.  
`CANCELLED` | The deployment is canceled.  
`SUCCEEDED` | The deployment succeeded.  
`WAITING` | The deployment is waiting.  
  
## LicenseModel

The license model of the GoldengateDeployment.

Enums  
---  
`LICENSE_MODEL_UNSPECIFIED` | The license model is unspecified.  
`LICENSE_INCLUDED` | The license model is included.  
`BRING_YOUR_OWN_LICENSE` | The license model is bring your own license.  
  
## GoldengateOggDeployment

The Ogg data of the GoldengateDeployment.

JSON representation  
---  
      
    
    {
      "deployment": string,
      "adminUsername": string,
      "oggVersion": string,
      "certificate": string,
      "credentialStore": enum ([CredentialStore](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#CredentialStore)),
      "identityDomainId": string,
      "passwordSecretId": string,
      "groupRolesMapping": {
        object ([GoldengateGroupToRolesMapping](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateGroupToRolesMapping))
      },
    
      // Union field deployment_password_options can be only one of the following:
      "adminPassword": string,
      "adminPasswordSecretVersion": string
      // End of list of possible types for union field deployment_password_options.
    }  
  
Fields  
---  
`deployment` |  `string` Required. The name given to the Goldengate service deployment. The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.  
`adminUsername` |  `string` Required. The Goldengate deployment console username.  
`oggVersion` |  `string` Optional. Version of OGG  
`certificate` |  `string` Output only. The certificate of the GoldengateDeployment.  
`credentialStore` |  `enum (`[CredentialStore](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#CredentialStore)`)` Output only. The credential store of the GoldengateDeployment.  
`identityDomainId` |  `string` Output only. The identity domain id of the GoldengateDeployment.  
`passwordSecretId` |  `string` Output only. The password secret id of the GoldengateDeployment.  
`groupRolesMapping` |  `object (`[GoldengateGroupToRolesMapping](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#GoldengateGroupToRolesMapping)`)` Output only. The group to roles mapping of the GoldengateDeployment.  
Union field `deployment_password_options`. The Goldengate deployment console password. `deployment_password_options` can be only one of the following:  
`adminPassword` |  `string` Optional. The Goldengate deployment console password in plain text.  
`adminPasswordSecretVersion` |  `string` Optional. Input only. The Goldengate deployment console password secret version.  
  
## CredentialStore

The credential store of the GoldengateDeployment.

Enums  
---  
`CREDENTIAL_STORE_UNSPECIFIED` | The credential store is unspecified.  
`GOLDENGATE` | The credential store is Goldengate.  
`IAM` | The credential store is IAM.  
  
## GoldengateGroupToRolesMapping

The group to roles mapping of the GoldengateDeployment.

JSON representation  
---  
      
    
    {
      "securityGroupId": string,
      "administratorGroupId": string,
      "operatorGroupId": string,
      "userGroupId": string
    }  
  
Fields  
---  
`securityGroupId` |  `string` Output only. The security group id.  
`administratorGroupId` |  `string` Output only. The administrator group id.  
`operatorGroupId` |  `string` Output only. The operator group id.  
`userGroupId` |  `string` Output only. The user group id.  
  
## GoldengateMaintenanceWindow

The maintenance window of the GoldengateDeployment.

JSON representation  
---  
      
    
    {
      "day": enum ([DayOfWeek](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DayOfWeek)),
      "startHour": integer
    }  
  
Fields  
---  
`day` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DayOfWeek)`)` Required. Days of the week.  
`startHour` |  `integer` Required. Start hour for maintenance period. Hour is in UTC.  
  
## GoldengateMaintenanceConfig

The maintenance configuration of the GoldengateDeployment.

JSON representation  
---  
      
    
    {
      "isInterimReleaseAutoUpgradeEnabled": boolean,
      "interimReleaseUpgradePeriodDays": integer,
      "bundleReleaseUpgradePeriodDays": integer,
      "majorReleaseUpgradePeriodDays": integer,
      "securityPatchUpgradePeriodDays": integer
    }  
  
Fields  
---  
`isInterimReleaseAutoUpgradeEnabled` |  `boolean` Optional. By default auto upgrade for interim releases are not enabled. If auto-upgrade is enabled for interim release, you have to specify interimReleaseUpgradePeriodDays too.  
`interimReleaseUpgradePeriodDays` |  `integer` Optional. Defines auto upgrade period for interim releases. This period must be shorter or equal to bundle release upgrade period.  
`bundleReleaseUpgradePeriodDays` |  `integer` Optional. Defines auto upgrade period for bundle releases. Manually configured period cannot be longer than service defined period for bundle releases. This period must be shorter or equal to major release upgrade period. Not passing this field during create will equate to using the service default.  
`majorReleaseUpgradePeriodDays` |  `integer` Optional. Defines auto upgrade period for major releases. Manually configured period cannot be longer than service defined period for major releases. Not passing this field during create will equate to using the service default.  
`securityPatchUpgradePeriodDays` |  `integer` Optional. Defines auto upgrade period for releases with security fix. Manually configured period cannot be longer than service defined period for security releases. Not passing this field during create will equate to using the service default.  
  
## GoldengateDeploymentLifecycleSubState

The various lifecycle sub-states of the GoldengateDeployment.

Enums  
---  
`GOLDENGATE_DEPLOYMENT_LIFECYCLE_SUB_STATE_UNSPECIFIED` | The lifecycle sub-state is unspecified.  
`RECOVERING` | The deployment is recovering.  
`STARTING` | The deployment is starting.  
`STOPPING` | The deployment is stopping.  
`MOVING` | The deployment is moving.  
`UPGRADING` | The deployment is upgrading.  
`RESTORING` | The deployment is restoring.  
`BACKING_UP` | The deployment is backing up.  
`ROLLING_BACK` | The deployment is rolling back.  
  
## GoldengateDeploymentCategory

The category of the GoldengateDeployment.

Enums  
---  
`GOLDENGATE_DEPLOYMENT_CATEGORY_UNSPECIFIED` | The category is unspecified.  
`DATA_REPLICATION` | The deployment is data replication.  
`DATA_TRANSFORMS` | The deployment is data transforms.  
  
## DeploymentDiagnosticData

The deployment diagnostic data.

JSON representation  
---  
      
    
    {
      "namespace": string,
      "bucket": string,
      "object": string,
      "diagnosticState": enum ([DiagnosticState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#DiagnosticState)),
      "diagnosticStartTime": string,
      "diagnosticEndTime": string
    }  
  
Fields  
---  
`namespace` |  `string` Output only. The namespace name.  
`bucket` |  `string` Output only. The bucket name.  
`object` |  `string` Output only. The object name.  
`diagnosticState` |  `enum (`[DiagnosticState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#DiagnosticState)`)` Output only. The diagnostic state.  
`diagnosticStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time diagnostic start.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`diagnosticEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time diagnostic end.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## DiagnosticState

The possible states of the diagnostic data.

Enums  
---  
`DIAGNOSTIC_STATE_UNSPECIFIED` | The diagnostic state is unspecified.  
`IN_PROGRESS` | The diagnostic is in progress.  
`SUCCEEDED` | The diagnostic completed successfully.  
`FAILED` | The diagnostic failed.  
  
## GoldengateBackupSchedule

The backup schedule of the GoldengateDeployment.

JSON representation  
---  
      
    
    {
      "bucket": string,
      "compartmentId": string,
      "frequencyBackupScheduled": enum ([FrequencyBackupScheduled](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#FrequencyBackupScheduled)),
      "metadataOnly": boolean,
      "namespace": string,
      "backupScheduledTime": string
    }  
  
Fields  
---  
`bucket` |  `string` Output only. The bucket name.  
`compartmentId` |  `string` Output only. The compartment id.  
`frequencyBackupScheduled` |  `enum (`[FrequencyBackupScheduled](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#FrequencyBackupScheduled)`)` Output only. The frequency backup scheduled.  
`metadataOnly` |  `boolean` Output only. If metadata only.  
`namespace` |  `string` Output only. The namespace name.  
`backupScheduledTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the backup was scheduled.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## FrequencyBackupScheduled

Enum for frequency backup scheduled.

Enums  
---  
`FREQUENCY_BACKUP_SCHEDULED_UNSPECIFIED` | The frequency backup scheduled is unspecified.  
`DAILY` | The frequency backup scheduled is daily.  
`WEEKLY` | The frequency backup scheduled is weekly.  
`MONTHLY` | The frequency backup scheduled is monthly.  
  
## NextMaintenanceActionType

The various next maintenance action types of the GoldengateDeployment.

Enums  
---  
`NEXT_MAINTENANCE_ACTION_TYPE_UNSPECIFIED` | The next maintenance action type is unspecified.  
`UPGRADE` | The next maintenance action type is upgrade.  
  
## IngressIp

The ingress IPs of the GoldengateDeployment.

JSON representation  
---  
      
    
    {
      "ingressIpAddress": string
    }  
  
Fields  
---  
`ingressIpAddress` |  `string` Output only. The ingress IP.  
  
## GoldengateDeploymentRoleType

The deployment role type of the GoldengateDeployment.

Enums  
---  
`GOLDENGATE_DEPLOYMENT_ROLE_TYPE_UNSPECIFIED` | The deployment role type is unspecified.  
`PRIMARY` | The deployment role type is primary.  
`STANDBY` | The deployment role type is standby.  
  
## GoldengateDeploymentLock

The lock of the GoldengateDeployment.

JSON representation  
---  
      
    
    {
      "type": enum ([LockType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#LockType)),
      "compartmentId": string,
      "relatedResourceId": string,
      "message": string,
      "createTime": string
    }  
  
Fields  
---  
`type` |  `enum (`[LockType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments#LockType)`)` Output only. The type of lock.  
`compartmentId` |  `string` Output only. The compartment id.  
`relatedResourceId` |  `string` Output only. The related resource id.  
`message` |  `string` Output only. The message.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## LockType

The type of lock.

Enums  
---  
`LOCK_TYPE_UNSPECIFIED` | The lock type is unspecified.  
`FULL` | The lock type is full.  
`DELETE` | The lock type is delete.  
  
## GoldengatePlacement

The placement of the GoldengateDeployment.

JSON representation  
---  
      
    
    {
      "availabilityDomain": string,
      "faultDomain": string
    }  
  
Fields  
---  
`availabilityDomain` |  `string` Output only. The availability domain.  
`faultDomain` |  `string` Output only. The fault domain.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments/create)`

|  Creates a new GoldengateDeployment in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments/delete)`

|  Deletes a single GoldengateDeployment.  
  
### `[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments/get)`

|  Gets details of a single GoldengateDeployment.  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments/list)`

|  Lists all the GoldengateDeployments for the given project and location.  
  
### `[start](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments/start)`

|  Starts a single GoldengateDeployment.  
  
### `[stop](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments/stop)`

|  Stops a single GoldengateDeployment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
