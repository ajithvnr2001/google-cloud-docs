---
url: https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/exadb-vm-clusters/create/
title: gcloud oracle-database exadb-vm-clusters create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:43:36.447591+00:00
---

# gcloud oracle-database exadb-vm-clusters create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/exadb-vm-clusters/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud oracle-database exadb-vm-clusters create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud oracle-database exadb-vm-clusters create - create a new ExadbVmCluster 
SYNOPSIS
    

`gcloud oracle-database exadb-vm-clusters create` `EXADB_VM_CLUSTER` `--backup-odb-subnet`=`BACKUP_ODB_SUBNET` `--display-name`=`DISPLAY_NAME` `--odb-subnet`=`ODB_SUBNET` (`--properties-enabled-ecpu-count-per-node`=`PROPERTIES_ENABLED_ECPU_COUNT_PER_NODE` `--properties-exascale-db-storage-vault`=`PROPERTIES_EXASCALE_DB_STORAGE_VAULT` `--properties-grid-image-id`=`PROPERTIES_GRID_IMAGE_ID` `--properties-hostname-prefix`=`PROPERTIES_HOSTNAME_PREFIX` `--properties-node-count`=`PROPERTIES_NODE_COUNT` `--properties-shape-attribute`=`PROPERTIES_SHAPE_ATTRIBUTE` `--properties-ssh-public-keys`=[`PROPERTIES_SSH_PUBLIC_KEYS`,…] `--vm-file-system-storage-size-in-gbs-per-node`=`VM_FILE_SYSTEM_STORAGE_SIZE_IN_GBS_PER_NODE` : `--properties-additional-ecpu-count-per-node`=`PROPERTIES_ADDITIONAL_ECPU_COUNT_PER_NODE` `--properties-cluster-name`=`PROPERTIES_CLUSTER_NAME` `--properties-license-model`=`PROPERTIES_LICENSE_MODEL` `--properties-scan-listener-port-tcp`=`PROPERTIES_SCAN_LISTENER_PORT_TCP` `--data-collection-options-is-diagnostics-events-enabled` `--data-collection-options-is-health-monitoring-enabled` `--data-collection-options-is-incident-logs-enabled` `--time-zone-id`=`TIME_ZONE_ID` `--time-zone-version`=`TIME_ZONE_VERSION`) [`--async`] [`--labels`=[`LABELS`,…]] [`--location`=`LOCATION`] [`--odb-network`=`ODB_NETWORK`] [`--request-id`=`REQUEST_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a new ExadbVmCluster. 
EXAMPLES
     To create an ExadbVmCluster with id `my-instance` in the location `us-east4` with display-name `my instance`, node-count `2`, enabled-ecpu-count-per-node `4`, vm-file-system-storage-size-in-gbs-per-node `100`, shape-attribute `SMART_STORAGE`, exascale-db-storage-vault `projects/my-project/locations/us-east4/exascaleDbStorageVaults/my-vault`, hostname-prefix `my-host`, ssh-public-keys `VtTxzlPJtIivthmLOmWdRDFy5l27pKUTwLp02`, odb-network `projects/my-project/locations/us-east4/odbNetworks/my-network`, odb-subnet `projects/my-project/locations/us-east4/odbNetworks/my-network/odbSubnets/my-subnet`, backup-odb-subnet `projects/my-project/locations/us-east4/odbNetworks/my-network/odbSubnets/my-backup-subnet`, grid-image-id `projects/my-project/locations/us-east4/giVersions/19.0.0.0`, run: 
    
    
    gcloud oracle-database exadb-vm-clusters create my-instance --location=us-east4 --display-name="my instance" --properties-node-count=2 --properties-enabled-ecpu-count-per-node=4 --vm-file-system-storage-size-in-gbs-per-node=100 --properties-shape-attribute=SMART_STORAGE --properties-exascale-db-storage-vault=projects/my-project/locations/us-east4/exascaleDbStorageVaults/my-vault --properties-hostname-prefix=my-host --properties-ssh-public-keys="VtTxzlPJtIivthmLOmWdRDFy5l27pKUTwLp02" --odb-network=projects/my-project/locations/us-east4/odbNetworks/my-network --odb-subnet=projects/my-project/locations/us-east4/odbNetworks/my-network/odbSubnets/my-subnet --backup-odb-subnet=projects/my-project/locations/us-east4/odbNetworks/my-network/odbSubnets/my-backup-subnet --properties-grid-image-id=projects/my-project/locations/us-east4/giVersions/19.0.0.0

POSITIONAL ARGUMENTS
    

ExadbVmCluster resource - Identifier. The name of the ExadbVmCluster resource in the following format: projects/{project}/locations/{region}/exadbVmClusters/{exadb_vm_cluster} This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `exadb_vm_cluster` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `exadb_vm_cluster` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`EXADB_VM_CLUSTER`
     ID of the exadbVmCluster or fully qualified identifier for the exadbVmCluster. 

To set the `exadb_vm_cluster` attribute: 

  * provide the argument `exadb_vm_cluster` on the command line. 


REQUIRED FLAGS
    

OdbSubnet resource - The name of the backup OdbSubnet associated with the ExadbVmCluster. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet} This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--backup-odb-subnet` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--backup-odb-subnet` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



To set the `odb-network` attribute: 

  * provide the argument `--backup-odb-subnet` on the command line with a fully specified name; 
  * provide the argument `--odb-network` on the command line. 



This must be specified. 

`--backup-odb-subnet`=`BACKUP_ODB_SUBNET`
     ID of the odbSubnet or fully qualified identifier for the odbSubnet. 

To set the `odb-subnet` attribute: 

  * provide the argument `--backup-odb-subnet` on the command line. 


`--display-name`=`DISPLAY_NAME`
     The display name for the ExadbVmCluster. The name does not have to be unique within your project. The name must be 1-255 characters long and can only contain alphanumeric characters. 
OdbSubnet resource - The name of the OdbSubnet associated with the ExadbVmCluster for IP allocation. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet} This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--odb-subnet` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--odb-subnet` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



To set the `odb-network` attribute: 

  * provide the argument `--odb-subnet` on the command line with a fully specified name; 
  * provide the argument `--odb-network` on the command line. 



This must be specified. 

`--odb-subnet`=`ODB_SUBNET`
     ID of the odbSubnet or fully qualified identifier for the odbSubnet. 

To set the `odb-subnet` attribute: 

  * provide the argument `--odb-subnet` on the command line. 


The properties of an ExadbVmCluster. 

This must be specified. 

`--properties-enabled-ecpu-count-per-node`=`PROPERTIES_ENABLED_ECPU_COUNT_PER_NODE`
     The number of ECPUs enabled per node for an exadata vm cluster on exascale infrastructure. 

This flag argument must be specified if any of the other arguments in this group are specified. 

ExascaleDbStorageVault resource - The name of ExascaleDbStorageVault associated with the ExadbVmCluster. It can refer to an existing ExascaleDbStorageVault. Or a new one can be created during the ExadbVmCluster creation (requires storage_vault_properties to be set). Format: projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault} This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--properties-exascale-db-storage-vault` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--properties-exascale-db-storage-vault` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`--properties-exascale-db-storage-vault`=`PROPERTIES_EXASCALE_DB_STORAGE_VAULT`
     ID of the exascaleDbStorageVault or fully qualified identifier for the exascaleDbStorageVault. 

To set the `exascale-db-storage-vault` attribute: 

  * provide the argument `--properties-exascale-db-storage-vault` on the command line. 


`--properties-grid-image-id`=`PROPERTIES_GRID_IMAGE_ID`
     Grid Infrastructure Version. 
`--properties-hostname-prefix`=`PROPERTIES_HOSTNAME_PREFIX`
     Prefix for VM cluster host names. 
`--properties-node-count`=`PROPERTIES_NODE_COUNT`
     The number of nodes/VMs in the ExadbVmCluster. 
`--properties-shape-attribute`=`PROPERTIES_SHAPE_ATTRIBUTE`
     The shape attribute of the VM cluster. The type of Exascale storage used for Exadata VM cluster. The default is SMART_STORAGE which supports Oracle Database 23ai and later. `PROPERTIES_SHAPE_ATTRIBUTE` must be one of: 

`block-storage`
     Indicates that the resource is in block storage. 
`smart-storage`
     Indicates that the resource is in smart storage. 
`--properties-ssh-public-keys`=[`PROPERTIES_SSH_PUBLIC_KEYS`,…]
     The SSH public keys for the ExadbVmCluster. 
The storage allocation for the exadbvmcluster, in gigabytes (GB). 

This must be specified. 

`--vm-file-system-storage-size-in-gbs-per-node`=`VM_FILE_SYSTEM_STORAGE_SIZE_IN_GBS_PER_NODE`
     The storage allocation for the exadbvmcluster per node, in gigabytes (GB). This field is used to calculate the total storage allocation for the exadbvmcluster. 
`--properties-additional-ecpu-count-per-node`=`PROPERTIES_ADDITIONAL_ECPU_COUNT_PER_NODE`
     The number of additional ECPUs per node for an Exadata VM cluster on exascale infrastructure. 
`--properties-cluster-name`=`PROPERTIES_CLUSTER_NAME`
     The cluster name for Exascale vm cluster. The cluster name must begin with an alphabetic character and may contain hyphens(-) but can not contain underscores(`). It should be not more than 11 characters and is not case sensitive. OCI Cluster name. `
`--properties-license-model`=PROPERTIES_LICENSE_MODEL``
     The license type of the ExadbVmCluster. PROPERTIES_LICENSE_MODEL` must be one of: 

`bring-your-own-license`
     Bring your own license. 
`license-included`
     Default is license included. 
`
`--properties-scan-listener-port-tcp`=PROPERTIES_SCAN_LISTENER_PORT_TCP``
     SCAN listener port - TCP 
Data collection options for diagnostics. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/DataCollectionOptions>
`--data-collection-options-is-diagnostics-events-enabled`
     Indicates whether to enable data collection for diagnostics. 
`--data-collection-options-is-health-monitoring-enabled`
     Indicates whether to enable health monitoring. 
`--data-collection-options-is-incident-logs-enabled`
     Indicates whether to enable incident logs and trace collection. 
Represents a time zone from the [IANA Time Zone Database](https://www.iana.org/time-zones). 
`--time-zone-id`=TIME_ZONE_ID``
     IANA Time Zone Database time zone. For example "America/New_York". 
`--time-zone-version`=TIME_ZONE_VERSION``
     IANA Time Zone Database version number. For example "2019a". 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--labels`=[`LABELS`,…]
     The labels or tags associated with the ExadbVmCluster. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --labels=string=string

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

`--location`=`LOCATION`
     For resources [backup-odb-subnet, exadb_vm_cluster, odb-network, odb-subnet, properties-exascale-db-storage-vault], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
`--odb-network`=`ODB_NETWORK`
     For resources [backup-odb-subnet, odb-network, odb-subnet], provides fallback value for resource odb-network attribute. When the resource's full URI path is not provided, odb-network will fallback to this flag value. 
`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `oracledatabase/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/oracle/database/docs>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
