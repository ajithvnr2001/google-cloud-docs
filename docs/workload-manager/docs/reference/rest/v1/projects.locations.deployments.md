---
url: https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments
title: REST Resource: projects.locations.deployments \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:52.000740+00:00
---

# REST Resource: projects.locations.deployments  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/workload-manager/docs/authentication)



Send feedback 

#  REST Resource: projects.locations.deployments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Deployment
    * JSON representation
  * WorkloadType
  * TerraformVariable
    * JSON representation
  * SapSystemS4Config
    * JSON representation
  * LocationDetails
    * JSON representation
  * InternetAccess
  * DatabaseDetails
    * JSON representation
  * AppDetails
    * JSON representation
  * Version
  * EnvironmentType
  * DeploymentModel
  * ScalingMethod
  * SqlServerWorkload
    * JSON representation
  * OperatingSystemType
  * DeploymentModel
  * HAType
  * SqlLocationDetails
    * JSON representation
  * InternetAccess
  * ActiveDirectory
    * JSON representation
  * ActiveDirectoryType
  * Database
    * JSON representation
  * TenancyModel
  * Pacemaker
    * JSON representation
  * FciType
  * SqlServerEditionType
  * SqlServerVersionType
  * OsImageType
  * State
  * Methods



## Resource: Deployment

The Deployment object represents user intent for deploying a specific type of workload.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "workloadType": enum ([WorkloadType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#WorkloadType)),
      "terraformVariables": {
        string: {
          object ([TerraformVariable](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#TerraformVariable))
        },
        ...
      },
      "createTime": string,
      "updateTime": string,
      "state": enum ([State](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#State)),
      "serviceAccount": string,
      "workerPool": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "sapSystemS4Config": {
        object ([SapSystemS4Config](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#SapSystemS4Config))
      },
      "sqlServerWorkload": {
        object ([SqlServerWorkload](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#SqlServerWorkload))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` The name of the deployment resource. The format is 'projects/{projectId}/locations/{locationId}/deployments/{deploymentId}'.  
`description` |  `string` Description of the deployment.  
`workloadType` |  `enum (`[WorkloadType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#WorkloadType)`)` Optional. Workload type of the deployment.  
`terraformVariables` |  `map (key: string, value: object (`[TerraformVariable](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#TerraformVariable)`))` Optional. terraformVariables represents all the Terraform variables for the deployment workload. The key is the name of the Terraform variable, and the value is the TerraformVariable. For example: { "projectId": { "inputValue": { "stringValue": "my-project-id" } }, "zone": { "inputValue": { "stringValue": "us-central1-a" } } }An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time stamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time stamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#State)`)` Output only. Current state of the deployment.  
`serviceAccount` |  `string` User-specified Service Account (SA) credentials to be used for Cloud Build. Format: `projects/{projectID}/serviceAccounts/{serviceAccount}` The default Cloud Build SA will be used initially if this field is not set during deployment creation.  
`workerPool` |  `string` Optional. The user-specified Cloud Build worker pool resource in which the Cloud Build job will execute. Format: `projects/{project}/locations/{location}/workerPools/{workerPoolId}`. If this field is unspecified, the default Cloud Build worker pool will be used.  
DeploymentMetadata of the deployment. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`sapSystemS4Config` |  `object (`[SapSystemS4Config](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#SapSystemS4Config)`)` SAP system workload input.  
`sqlServerWorkload` |  `object (`[SqlServerWorkload](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#SqlServerWorkload)`)` MS SQL workload input.  
End of mutually exclusive fields.  
  
## WorkloadType

Enum of workload type.

Enums  
---  
`WORKLOAD_TYPE_UNSPECIFIED` | Unspecified workload type.  
`SAP_S4` | SAP S/4HANA workload type.  
`SQL_SERVER` | SQL Server workload type.  
`ORACLE` | Oracle workload type.  
  
## TerraformVariable

In order to align with the Infra Manager dependency, we create the same TerraformVariable message to represent a Terraform input variable, by following Infra Manager's API documentation: <https://cloud.google.com/infrastructure-manager/docs/reference/rest>. A Terraform input variable.

JSON representation  
---  
      
    
    {
      "inputValue": value
    }  
  
Fields  
---  
`inputValue` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Optional. Input variable value.  
  
## SapSystemS4Config

Message for SAP system workload.

JSON representation  
---  
      
    
    {
      "gcpProjectId": string,
      "location": {
        object ([LocationDetails](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#LocationDetails))
      },
      "database": {
        object ([DatabaseDetails](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#DatabaseDetails))
      },
      "app": {
        object ([AppDetails](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#AppDetails))
      },
      "allowStoppingForUpdate": boolean,
      "version": enum ([Version](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#Version)),
      "environmentType": enum ([EnvironmentType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#EnvironmentType)),
      "deploymentModel": enum ([DeploymentModel](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#DeploymentModel)),
      "scalingMethod": enum ([ScalingMethod](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#ScalingMethod)),
      "mediaBucketName": string,
      "sapBootDiskImage": string,
      "vmPrefix": string,
      "ansibleRunnerServiceAccount": string
    }  
  
Fields  
---  
`gcpProjectId` |  `string` The project that infrastructure is deployed in. Currently only supports the same project where the deployment resource exists.  
`location` |  `object (`[LocationDetails](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#LocationDetails)`)` Database details.  
`database` |  `object (`[DatabaseDetails](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#DatabaseDetails)`)` Database details.  
`app` |  `object (`[AppDetails](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#AppDetails)`)` Instance details.  
`allowStoppingForUpdate` |  `boolean`  
`version` |  `enum (`[Version](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#Version)`)` Required. SAP HANA version.  
`environmentType` |  `enum (`[EnvironmentType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#EnvironmentType)`)` Required. Deployment environment.  
`deploymentModel` |  `enum (`[DeploymentModel](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#DeploymentModel)`)` Required. Supports non-HA and HA models.  
`scalingMethod` |  `enum (`[ScalingMethod](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#ScalingMethod)`)` Required. Supports scale up and scale out.  
`mediaBucketName` |  `string` Required. Media bucket name.  
`sapBootDiskImage` |  `string` Optional. SAP boot disk image.  
`vmPrefix` |  `string` VM prefix.  
`ansibleRunnerServiceAccount` |  `string` Ansible runner service account. Let customers bring their own service account for the Ansible runner.  
  
## LocationDetails

Message for SAP instance details.

JSON representation  
---  
      
    
    {
      "vpcName": string,
      "zone1Name": string,
      "zone2Name": string,
      "dnsZoneNameSuffix": string,
      "regionName": string,
      "internetAccess": enum ([InternetAccess](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#InternetAccess)),
      "subnetName": string,
      "dnsZone": string,
      "networkProject": string,
      "createCommsFirewall": boolean,
      "customTags": [
        string
      ],
      "deploymentDnsEnabled": boolean
    }  
  
Fields  
---  
`vpcName` |  `string` Required. VPC name.  
`zone1Name` |  `string` Required. Zone 1 name.  
`zone2Name` |  `string` Optional. Zone 2 name.  
`dnsZoneNameSuffix` |  `string` Optional. DNS zone name suffix.  
`regionName` |  `string` Required. Region name.  
`internetAccess` |  `enum (`[InternetAccess](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#InternetAccess)`)`  
`subnetName` |  `string` Required. Subnet name.  
`dnsZone` |  `string` Optional. DNS zone name.  
`networkProject` |  `string` Optional. Network project.  
`createCommsFirewall` |  `boolean` Optional. Create firewall. If true, creates a firewall for the deployment. This field provides an option to not always create a firewall for the deployment.  
`customTags[]` |  `string` Optional. Network tags.  
`deploymentDnsEnabled` |  `boolean` Optional. When the user skips DNS configuration in the UI, `deploymentDnsEnabled` is false; otherwise `deploymentDnsEnabled` is true.  
  
## InternetAccess

Internet access.

Enums  
---  
`INTERNETACCESS_UNSPECIFIED` |   
`ALLOW_EXTERNAL_IP` |   
`CONFIGURE_NAT` |   
  
## DatabaseDetails

Message for SAP instance details.

JSON representation  
---  
      
    
    {
      "sid": string,
      "machineType": string,
      "diskType": string,
      "secretManagerSecret": string,
      "image": string,
      "instanceId": string,
      "primaryDbVm": string,
      "secondaryDbVm": string,
      "databaseServiceAccount": string
    }  
  
Fields  
---  
`sid` |  `string` Required. The SID is a three-digit server-specific unique identification code.  
`machineType` |  `string` Required. Machine type.  
`diskType` |  `string` Required. Disk type.  
`secretManagerSecret` |  `string` Required. Secret Manager secret.  
`image` |  `string` Required. Image for the database server.  
`instanceId` |  `string` Optional. Instance ID.  
`primaryDbVm` |  `string` Optional. Primary DB VM name.  
`secondaryDbVm` |  `string` Optional. Secondary DB VM name.  
`databaseServiceAccount` |  `string` Database service account. Let customers bring their own SA for the database.  
  
## AppDetails

Message for SAP instance details.

JSON representation  
---  
      
    
    {
      "sid": string,
      "vmsMultiplier": integer,
      "machineType": string,
      "ascsMachineType": string,
      "secretManagerSecret": string,
      "image": string,
      "ascsInstanceId": string,
      "ersInstanceId": string,
      "appInstanceId": string,
      "ascsVm": string,
      "ersVm": string,
      "ascsImage": string,
      "appVmNames": [
        string
      ],
      "ascsServiceAccount": string,
      "appServiceAccount": string,
      "sharedStorage": string
    }  
  
Fields  
---  
`sid` |  `string` Required. The SAP SID is a three-digit server-specific unique identification code.  
`vmsMultiplier` |  `integer` Required. VMs multiplier.  
`machineType` |  `string` Required. Machine type.  
`ascsMachineType` |  `string` Required. ASCS machine type.  
`secretManagerSecret` |  `string` Required. Secret Manager secret.  
`image` |  `string` Required. Image for the app server and ASCS server.  
`ascsInstanceId` |  `string` Optional. Instance ID for ASCS.  
`ersInstanceId` |  `string` Optional. Instance ID for ERS.  
`appInstanceId` |  `string` Optional. Instance ID for app.  
`ascsVm` |  `string` Optional. ASCS VM name.  
`ersVm` |  `string` Optional. ERS VM name.  
`ascsImage` |  `string` Required. Image for the ASCS server.  
`appVmNames[]` |  `string` Optional. Customized VM names.  
`ascsServiceAccount` |  `string` ASCS service account. Let customers bring their own service account for ASCS.  
`appServiceAccount` |  `string` Application service account. Let customers bring their own service account for the application.  
`sharedStorage` |  `string` Optional. Storage location.  
  
## Version

Version.

Enums  
---  
`VERSION_UNSPECIFIED` |   
`S4_HANA_2021` |   
`S4_HANA_2022` |   
`S4_HANA_2023` |   
  
## EnvironmentType

Environment type.

Enums  
---  
`ENVIRONMENT_TYPE_UNSPECIFIED` | Unspecified environment type.  
`NON_PRODUCTION` | Non-production environment type.  
`PRODUCTION` | Production environment type.  
  
## DeploymentModel

Deployment model.

Enums  
---  
`DEPLOYMENT_MODEL_UNSPECIFIED` |   
`DISTRIBUTED` |   
`DISTRIBUTED_HA` |   
  
## ScalingMethod

Scaling method.

Enums  
---  
`SCALE_METHOD_UNSPECIFIED` |   
`SCALE_UP` | Scale up: Increases the size of a physical machine by increasing the amount of RAM and CPU available for processing.  
`SCALE_OUT` | Scale out: Combines multiple independent computers into one system.  
  
## SqlServerWorkload

Message for MS SQL workload.

JSON representation  
---  
      
    
    {
      "environmentType": enum ([EnvironmentType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#EnvironmentType)),
      "operatingSystemType": enum ([OperatingSystemType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#OperatingSystemType)),
      "osImage": string,
      "deploymentModel": enum ([DeploymentModel](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#DeploymentModel_1)),
      "haType": enum ([HAType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#HAType)),
      "vmPrefix": string,
      "mediaBucket": string,
      "location": {
        object ([SqlLocationDetails](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#SqlLocationDetails))
      },
      "activeDirectory": {
        object ([ActiveDirectory](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#ActiveDirectory))
      },
      "database": {
        object ([Database](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#Database))
      },
      "pacemaker": {
        object ([Pacemaker](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#Pacemaker))
      },
      "fciType": enum ([FciType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#FciType)),
      "isSqlPayg": boolean,
      "sqlServerEdition": enum ([SqlServerEditionType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#SqlServerEditionType)),
      "sqlServerVersion": enum ([SqlServerVersionType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#SqlServerVersionType)),
      "osImageType": enum ([OsImageType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#OsImageType)),
      "computeEngineServiceAccount": string
    }  
  
Fields  
---  
`environmentType` |  `enum (`[EnvironmentType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#EnvironmentType)`)` Required. Deployment environment.  
`operatingSystemType` |  `enum (`[OperatingSystemType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#OperatingSystemType)`)` Required. The type of the operating system the SQL server is going to run on top of.  
`osImage` |  `string` Required. The image of the operating system.  
`deploymentModel` |  `enum (`[DeploymentModel](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#DeploymentModel_1)`)` Required. HIGH_AVAILABILITY or SINGLE_INSTANCE.  
`haType` |  `enum (`[HAType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#HAType)`)` Optional. AOAG or FCI. It is only needed for the High Availability deployment mode.  
`vmPrefix` |  `string` Required. Should be unique in the project.  
`mediaBucket` |  `string` Required. Name of the media storing SQL server installation files.  
`location` |  `object (`[SqlLocationDetails](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#SqlLocationDetails)`)` Required. Location details.  
`activeDirectory` |  `object (`[ActiveDirectory](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#ActiveDirectory)`)` Required. Active Directory details.  
`database` |  `object (`[Database](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#Database)`)` Required. Database details.  
`pacemaker` |  `object (`[Pacemaker](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#Pacemaker)`)` Optional. Pacemaker configuration, only applicable for Linux HA deployments.  
`fciType` |  `enum (`[FciType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#FciType)`)` Optional. SHARED_DISK or S2D.  
`isSqlPayg` |  `boolean` Required. SQL licensing type.  
`sqlServerEdition` |  `enum (`[SqlServerEditionType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#SqlServerEditionType)`)` Optional. SQL Server Edition type, only applicable when the operating system is Linux.  
`sqlServerVersion` |  `enum (`[SqlServerVersionType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#SqlServerVersionType)`)` Optional. 2017, 2019, or 2022.  
`osImageType` |  `enum (`[OsImageType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#OsImageType)`)` Optional. OS image type. It's used to create boot disks for VM instances. When either Windows licensing type or SQL licensing type is BYOL, this option is disabled and defaults to a custom image.  
`computeEngineServiceAccount` |  `string` Compute Engine service account. Let customers bring their own service account for Compute Engine.  
  
## OperatingSystemType

Operating system type.

Enums  
---  
`OPERATING_SYSTEM_TYPE_UNSPECIFIED` | Unspecified operating system type.  
`WINDOWS` | Windows operating system type.  
`UBUNTU` | Ubuntu operating system type.  
`RED_HAT_ENTERPRISE_LINUX` | Red Hat Enterprise Linux operating system type.  
`SUSE` | SUSE operating system type.  
  
## DeploymentModel

Deployment model.

Enums  
---  
`DEPLOYMENT_MODEL_UNSPECIFIED` | Unspecified deployment model.  
`HIGH_AVAILABILITY` | High Availability deployment model.  
`SINGLE_INSTANCE` | Single instance deployment model.  
  
## HAType

HA type.

Enums  
---  
`HA_TYPE_UNSPECIFIED` | Unspecified HA type.  
`AOAG` | AOAG HA type.  
`FCI` | FCI HA type.  
  
## SqlLocationDetails

Location and networking details for configuring SQL server workload.

JSON representation  
---  
      
    
    {
      "gcpProjectId": string,
      "region": string,
      "primaryZone": string,
      "secondaryZone": string,
      "network": string,
      "subnetwork": string,
      "internetAccess": enum ([InternetAccess](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#InternetAccess_1)),
      "dnsZone": string,
      "tertiaryZone": string
    }  
  
Fields  
---  
`gcpProjectId` |  `string` Required. The project that infrastructure is deployed in. Currently only supports the same project where the deployment resource exists.  
`region` |  `string` Required. Region name.  
`primaryZone` |  `string` Required. Primary zone.  
`secondaryZone` |  `string` Optional. Secondary zone cannot be the same as primaryZone and is only for High Availability deployment mode.  
`network` |  `string` Required. Network name.  
`subnetwork` |  `string` Required. Subnetwork name.  
`internetAccess` |  `enum (`[InternetAccess](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#InternetAccess_1)`)` Required. Internet Access.  
`dnsZone` |  `string` Optional. Create a new DNS zone when the field is empty. Only shown for `Using an existing DNS`. List of existing DNS zones. Terraform variable name: existing_dns_zone_name.  
`tertiaryZone` |  `string` Optional. Tertiary zone cannot be the same as primaryZone and secondaryZone, and it is only for High Availability deployment mode.  
  
## InternetAccess

Internet access options.

Enums  
---  
`INTERNET_ACCESS_UNSPECIFIED` | Unspecified internet access.  
`ALLOW_EXTERNAL_IP` | Allow external IP.  
`CONFIGURE_NAT` | Configure NAT.  
  
## ActiveDirectory

Active Directory details.

JSON representation  
---  
      
    
    {
      "type": enum ([ActiveDirectoryType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#ActiveDirectoryType)),
      "domainUsername": string,
      "secretManagerSecret": string,
      "dnsAddress": string,
      "domain": string
    }  
  
Fields  
---  
`type` |  `enum (`[ActiveDirectoryType](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#ActiveDirectoryType)`)` Required. Active Directory type.  
`domainUsername` |  `string` Optional. Domain username.  
`secretManagerSecret` |  `string` Required. Secret Manager secret.  
`dnsAddress` |  `string` Optional. DNS IP address.  
`domain` |  `string` Optional. Human readable form of a domain such as `example.com`.  
  
## ActiveDirectoryType

Active Directory type options.

Enums  
---  
`ACTIVE_DIRECTORY_TYPE_UNSPECIFIED` | Unspecified Active Directory type.  
`GCP_MANAGED` | GCP managed Active Directory type.  
`SELF_MANAGED` | Self managed Active Directory type.  
  
## Database

Database details.

JSON representation  
---  
      
    
    {
      "secretManagerSecret": string,
      "floatingIpAddress": string,
      "machineType": string,
      "smt": boolean,
      "tempdbOnSsd": boolean,
      "tenancyModel": enum ([TenancyModel](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#TenancyModel)),
      "diskType": string,
      "soleTenantNode": string,
      "soleTenantNodeType": string,
      "secondarySoleTenantNode": string,
      "secondarySoleTenantNodeType": string
    }  
  
Fields  
---  
`secretManagerSecret` |  `string` Required. Secret Manager secret.  
`floatingIpAddress` |  `string` Optional. Only useful for Linux High Availability setup.  
`machineType` |  `string` Required. Machine type.  
`smt` |  `boolean` Required. Whether simultaneous multithreading is enabled or not.  
`tempdbOnSsd` |  `boolean` Required. Whether to have TempDB on local SSD.  
`tenancyModel` |  `enum (`[TenancyModel](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#TenancyModel)`)` Required. SHARED or SOLE_TENANT.  
`diskType` |  `string` Required. Disk type.  
`soleTenantNode` |  `string` Optional. The name of a primary sole-tenant node/node group.  
`soleTenantNodeType` |  `string` Optional. The type of a primary sole-tenant node/node group. E.g., compute.googleapis.com/node-name.  
`secondarySoleTenantNode` |  `string` Optional. The name of a secondary-sole-tenant node/node group.  
`secondarySoleTenantNodeType` |  `string` Optional. The type of a secondary-sole-tenant node/node group. E.g., compute.googleapis.com/node-name.  
  
## TenancyModel

Tenancy model.

Enums  
---  
`TENANCY_MODEL_UNSPECIFIED` | Unspecified tenancy model.  
`SHARED` | Shared tenancy model.  
`SOLE_TENANT` | Sole Tenant tenancy model.  
  
## Pacemaker

Pacemaker configuration.

JSON representation  
---  
      
    
    {
      "pacemakerCluster": string,
      "pacemakerClusterUsername": string,
      "pacemakerClusterSecret": string,
      "sqlPacemakerUsername": string,
      "sqlPacemakerSecret": string,
      "bucketNameNodeCertificates": string
    }  
  
Fields  
---  
`pacemakerCluster` |  `string` Required. Pacemaker cluster name.  
`pacemakerClusterUsername` |  `string` Required. Pacemaker cluster username.  
`pacemakerClusterSecret` |  `string` Required. Pacemaker cluster secret name.  
`sqlPacemakerUsername` |  `string` Required. SQL Pacemaker username.  
`sqlPacemakerSecret` |  `string` Required. SQL Pacemaker secret name.  
`bucketNameNodeCertificates` |  `string` Required. Bucket location for node certificates.  
  
## FciType

FCI type, only applicable when the operating system is Windows and the HA type is FCI.

Enums  
---  
`FCI_TYPE_UNSPECIFIED` | Unspecified FCI type.  
`SHARED_DISK` | SHARED DISK FCI type.  
`S2D` | S2D FCI type.  
  
## SqlServerEditionType

SQL Server Edition type, only applicable when the operating system is Linux.

Enums  
---  
`SQL_SERVER_EDITION_TYPE_UNSPECIFIED` | Unspecified type.  
`SQL_SERVER_EDITION_TYPE_DEVELOPER` | Developer type.  
`SQL_SERVER_EDITION_TYPE_ENTERPRISE` | Enterprise type.  
`SQL_SERVER_EDITION_TYPE_STANDARD` | Standard type.  
`SQL_SERVER_EDITION_TYPE_WEB` | Web type.  
  
## SqlServerVersionType

SQL Server Version type, only applicable when the operating system is Linux.

Enums  
---  
`SQL_SERVER_VERSION_TYPE_UNSPECIFIED` | Unspecified type.  
`SQL_SERVER_VERSION_TYPE_2017` | 2017 type.  
`SQL_SERVER_VERSION_TYPE_2019` | 2019 type.  
`SQL_SERVER_VERSION_TYPE_2022` | 2022 type.  
  
## OsImageType

OS image type.

Enums  
---  
`OS_IMAGE_TYPE_UNSPECIFIED` | Unspecified OS image type.  
`PUBLIC_IMAGE` | Public image.  
`CUSTOM_IMAGE` | Custom image.  
  
## State

The state of the deployment.

Enums  
---  
`STATE_UNSPECIFIED` | The default value. This value is used if the state is omitted.  
`CREATING` | The deployment is being created.  
`ACTIVE` | The deployment is healthy.  
`UPDATING` | The deployment is being updated.  
`DELETING` | The deployment is being deleted.  
`FAILED` | The deployment has encountered an unexpected error.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments/create)`

|  Creates a new Deployment in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments/delete)`

|  Deletes a single Deployment.  
  
### `[get](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments/get)`

|  Gets details of a single Deployment.  
  
### `[list](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments/list)`

|  Lists Deployments in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
