---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/cluster-director/clusters/update/
title: gcloud alpha cluster-director clusters update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:47:06.503680+00:00
---

# gcloud alpha cluster-director clusters update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/cluster-director/clusters/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha cluster-director clusters update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha cluster-director clusters update - updates a Cluster Director resource 
SYNOPSIS
    

`gcloud alpha cluster-director clusters update` (`CLUSTER` : `--location`=`LOCATION`) (`--add-filestore-instances`=[`id`=`ID`],[`name`=`NAME`] `--add-flex-start-instances`=[`id`=`ID`],[`machineType`=`MACHINETYPE`],[`maxDuration`=`MAXDURATION`],[`networkTags`=`NETWORKTAGS`],[`zone`=`ZONE`] `--add-labels`=[`ADD_LABELS`,…] `--add-lustre-instances`=[`id`=`ID`],[`name`=`NAME`] `--add-new-filestore-instances`=[`capacityGb`=`CAPACITYGB`],[`description`=`DESCRIPTION`],[`fileshare`=`FILESHARE`],[`id`=`ID`],[`name`=`NAME`],[`protocol`=`PROTOCOL`],[`tier`=`TIER`] `--add-new-lustre-instances`=[`capacityGb`=`CAPACITYGB`],[`description`=`DESCRIPTION`],[`dynamicTierOptionsMode`=`DYNAMICTIEROPTIONSMODE`],[`filesystem`=`FILESYSTEM`],[`id`=`ID`],[`name`=`NAME`],[`perUnitStorageThroughput`=`PERUNITSTORAGETHROUGHPUT`] `--add-new-storage-buckets`=[`enableAutoclass`=`ENABLEAUTOCLASS`],[`enableHNS`=`ENABLEHNS`],[`id`=`ID`],[`name`=`NAME`],[`storageClass`=`STORAGECLASS`],[`terminalStorageClass`=`TERMINALSTORAGECLASS`] `--add-nfs`=[`id`=`ID`],[`mountOptions`=`MOUNTOPTIONS`],[`remoteMount`=`REMOTEMOUNT`],[`serverIpAddress`=`SERVERIPADDRESS`] `--add-on-demand-instances`=[`id`=`ID`],[`machineType`=`MACHINETYPE`],[`networkTags`=`NETWORKTAGS`],[`zone`=`ZONE`] `--add-reserved-instances`=[`id`=`ID`],[`networkTags`=`NETWORKTAGS`],[`reservation`=`RESERVATION`],[`reservationBlock`=`RESERVATIONBLOCK`],[`reservationSubBlock`=`RESERVATIONSUBBLOCK`] `--add-spot-instances`=[`id`=`ID`],[`machineType`=`MACHINETYPE`],[`networkTags`=`NETWORKTAGS`],[`terminationAction`=`TERMINATIONACTION`],[`zone`=`ZONE`] `--add-storage-buckets`=[`id`=`ID`],[`name`=`NAME`] `--description`=`DESCRIPTION` `--remove-filestore-instances`=[`REMOVE_FILESTORE_INSTANCES`,…] `--remove-flex-start-instances`=[`REMOVE_FLEX_START_INSTANCES`,…] `--remove-labels`=[`REMOVE_LABELS`,…] `--remove-lustre-instances`=[`REMOVE_LUSTRE_INSTANCES`,…] `--remove-nfs`=[`REMOVE_NFS`,…] `--remove-on-demand-instances`=[`REMOVE_ON_DEMAND_INSTANCES`,…] `--remove-reserved-instances`=[`REMOVE_RESERVED_INSTANCES`,…] `--remove-spot-instances`=[`REMOVE_SPOT_INSTANCES`,…] `--remove-storage-buckets`=[`REMOVE_STORAGE_BUCKETS`,…] `--add-managed-instance-groups`=[`acceleratorTopology`=`ACCELERATORTOPOLOGY`],[`bootDisk`=`BOOTDISK`],[`computeId`=`COMPUTEID`],[`enablePublicIps`=`ENABLEPUBLICIPS`],[`id`=`ID`],[`startupScript`=`STARTUPSCRIPT`],[`storageConfigs`=`STORAGECONFIGS`],[`targetSize`=`TARGETSIZE`] `--remove-managed-instance-groups`=[`REMOVE_MANAGED_INSTANCE_GROUPS`,…] `--update-managed-instance-groups`=[`acceleratorTopology`=`ACCELERATORTOPOLOGY`],[`bootDisk`=`BOOTDISK`],[`computeId`=`COMPUTEID`],[`enablePublicIps`=`ENABLEPUBLICIPS`],[`id`=`ID`],[`startupScript`=`STARTUPSCRIPT`],[`storageConfigs`=`STORAGECONFIGS`],[`targetSize`=`TARGETSIZE`] | `--add-slurm-epilog-scripts`=[`ADD_SLURM_EPILOG_SCRIPTS`,…] `--add-slurm-node-sets`=[`bootDisk`=`BOOTDISK`],[`computeId`=`COMPUTEID`],[`computeInstance`=`COMPUTEINSTANCE`],[`config`=`CONFIG`],[`container-resource-labels`=`CONTAINER-RESOURCE-LABELS`],[`container-startup-script`=`CONTAINER-STARTUP-SCRIPT`],[`containerNodePool`=`CONTAINERNODEPOOL`],[`id`=`ID`],[`labels`=`LABELS`],[`maxDynamicNodeCount`=`MAXDYNAMICNODECOUNT`],[`startupScript`=`STARTUPSCRIPT`],[`startupScriptTimeout`=`STARTUPSCRIPTTIMEOUT`],[`staticNodeCount`=`STATICNODECOUNT`],[`storageConfigs`=`STORAGECONFIGS`],[`type`=`TYPE`] `--add-slurm-partitions`=[`config`=`CONFIG`],[`id`=`ID`],[`nodeSetIds`=`NODESETIDS`] `--add-slurm-prolog-scripts`=[`ADD_SLURM_PROLOG_SCRIPTS`,…] `--add-slurm-task-epilog-scripts`=[`ADD_SLURM_TASK_EPILOG_SCRIPTS`,…] `--add-slurm-task-prolog-scripts`=[`ADD_SLURM_TASK_PROLOG_SCRIPTS`,…] `--no-enable-slurm-health-check` `--remove-slurm-epilog-scripts`=[`REMOVE_SLURM_EPILOG_SCRIPTS`,…] `--remove-slurm-node-sets`=[`REMOVE_SLURM_NODE_SETS`,…] `--remove-slurm-partitions`=[`REMOVE_SLURM_PARTITIONS`,…] `--remove-slurm-prolog-scripts`=[`REMOVE_SLURM_PROLOG_SCRIPTS`,…] `--remove-slurm-task-epilog-scripts`=[`REMOVE_SLURM_TASK_EPILOG_SCRIPTS`,…] `--remove-slurm-task-prolog-scripts`=[`REMOVE_SLURM_TASK_PROLOG_SCRIPTS`,…] `--slurm-default-partition`=`SLURM_DEFAULT_PARTITION` `--update-slurm-login-node`=[`bootDisk`=`BOOTDISK`],[`count`=`COUNT`],[`startupScript`=`STARTUPSCRIPT`] `--update-slurm-node-sets`=[`bootDisk`=`BOOTDISK`],[`computeId`=`COMPUTEID`],[`computeInstance`=`COMPUTEINSTANCE`],[`config`=`CONFIG`],[`container-resource-labels`=`CONTAINER-RESOURCE-LABELS`],[`container-startup-script`=`CONTAINER-STARTUP-SCRIPT`],[`containerNodePool`=`CONTAINERNODEPOOL`],[`id`=`ID`],[`labels`=`LABELS`],[`maxDynamicNodeCount`=`MAXDYNAMICNODECOUNT`],[`startupScript`=`STARTUPSCRIPT`],[`startupScriptTimeout`=`STARTUPSCRIPTTIMEOUT`],[`staticNodeCount`=`STATICNODECOUNT`],[`storageConfigs`=`STORAGECONFIGS`],[`type`=`TYPE`] `--update-slurm-partitions`=[`config`=`CONFIG`],[`id`=`ID`],[`nodeSetIds`=`NODESETIDS`] `--slurm-conf-file`=`SLURM_CONF_FILE` | `--update-slurm-config`=[`UPDATE_SLURM_CONFIG`,…] | `--config`=[`computeResources`=`COMPUTERESOURCES`],[`description`=`DESCRIPTION`],[`labels`=`LABELS`],[`name`=`NAME`],[`networkResources`=`NETWORKRESOURCES`],[`orchestrator`=`ORCHESTRATOR`],[`storageResources`=`STORAGERESOURCES`] `--update-mask`=`UPDATE_MASK`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha cluster-director clusters update` facilitates the updation of a cluster resource. 

There are following ways to update a cluster: 

  * [Preferred] Use granular flags to update cluster specs, based on read-modify-update pattern. 
    * Read the existing cluster specs through `get` cluster request. 
    * Modify the cluster specs through granular flags. 
    * Update the cluster specs through `patch` cluster request. 
  * Use --config with cluster specs and --update-mask flags, both in JSON format. 
    * Map and repeated fields update requires existing and new values. 
    * For example, to update a cluster to add a new nodeset, use the update mask "orchestrator.slurm.node_sets", and the patch cluster must include all existing nodesets as well as the new one. 

Please refer to the examples below for more details. 
EXAMPLES
     To update a cluster `my-cluster` in location `us-central1-a` with granular flags, run the following example: 

Add labels, compute instances, slurm node sets, slurm partitions and update description and default partition: 
    
    
    gcloud alpha cluster-director clusters update my-cluster --location=us-central1-a --description="My updated cluster description" --add-labels=env=prod,client=gcloud-cli --add-on-demand-instances=id=compute1,zone=us-central1-a,machineType=n2-standard-2 --add-reserved-instances=id=compute2,reservation=zones/us-central1-a/reservations/{reservation} --add-spot-instances=id=compute3,zone=us-central1-a,machineType=n2-standard-2 --add-flex-start-instances=id=compute4,zone=us-central1-a,machineType=a4-highgpu-8g,maxDuration=10000s --add-new-lustre-instances=lustre=locations/us-central1-a/instances/lustre1,capacityGb=1024,filesystem=lustre1 --add-lustre-instances=locations/us-central1-a/instances/lustre0 --add-slurm-node-sets=id=nodeset1,computeId=compute1 --add-slurm-node-sets=id=nodeset2,computeId=compute2 --add-slurm-node-sets=id=nodeset3,computeId=compute3 --add-slurm-node-sets=id=nodeset4,computeId=compute4 --add-slurm-partitions=id=partition1,nodesetIds=[nodeset1] --add-slurm-partitions=id=partition2,nodesetIds=[nodeset2,nodeset3,nodeset4] --slurm-default-partition=partition1

Update slurm node sets and slurm partitions: 
    
    
    gcloud alpha cluster-director clusters update my-cluster --location=us-central1-a --update-slurm-node-sets=id=nodeset1,staticNodeCount=2,maxDynamicNodeCount=10 --update-slurm-partitions=id=partition1,nodesetIds=[nodeset0]

Remove slurm node sets, slurm partitions and compute instances and update default partition: 
    
    
    gcloud alpha cluster-director clusters update my-cluster --location=us-central1-a --slurm-default-partition=partition0 --remove-labels=env,client --remove-lustre-instances=locations/us-central1-a/instances/lustre0 --remove-slurm-partitions=partition1 --remove-slurm-partitions=partition2 --remove-slurm-node-sets=nodeset1 --remove-slurm-node-sets=nodeset2 --remove-slurm-node-sets=nodeset3 --remove-slurm-node-sets=nodeset4 --remove-on-demand-instances=compute1 --remove-reserved-instances=compute2 --remove-spot-instances=compute3 --remove-flex-start-instances=compute4

Add and remove slurm prolog/epilog scripts: 
    
    
    gcloud alpha cluster-director clusters update my-cluster --location=us-central1-a --add-slurm-prolog-scripts=script1.sh --remove-slurm-epilog-scripts=script2.sh

Or cluster `my-cluster` in location `us-central1-a` with config JSON run the following JSON example: 
    
    
    gcloud alpha cluster-director clusters update my-cluster --location=us-central1-a --update-mask=labels --config='{"key": "value"}'

Or create a JSON file `my-cluster-config.json` with the cluster specs and run the following file example: 
    
    
    gcloud alpha cluster-director clusters update my-cluster --location=us-central1-a --update-mask=labels --config=my-cluster-config.json

Or create a JSON file with the update mask and run the following file example: 
    
    
    gcloud alpha cluster-director clusters update my-cluster --location=us-central1-a --update-mask=my-update-mask.json --config=my-cluster-config.json

POSITIONAL ARGUMENTS
    

Cluster resource - Name of the cluster resource. Formats: cluster | projects/{project}/locations/{locations}/clusters/{cluster} The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CLUSTER`
     ID of the cluster or fully qualified identifier for the cluster. 

To set the `cluster` attribute: 

  * provide the argument `cluster` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location ID of the cluster resource. 

To set the `location` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

Cluster configuration for provisioning with updates. 

Exactly one of these must be specified: 

Flag Configurations to define cluster updates. 
`--add-filestore-instances`=[`id`=`ID`],[`name`=`NAME`]
     Reference of existing filestore instance. 

id: ID of the filestore resource, used to refer to this resource in storage-configs. name: Name of the existing filestore instance to import from your project in the format of locations/us-central1/instances/filestore-1. 

For example --add-filestore-instances id=my-fs,name=locations/us-central1/instances/filestore-1. 

Sets `add_filestore_instances` value. 

`id`
     Required, sets `id` value. 
`name`
     Required, sets `name` value. 
`Shorthand Example:`
    
    
    --add-filestore-instances=id=string,name=string --add-filestore-instances=id=string,name=string

`JSON Example:`
    
    
    --add-filestore-instances='[{"id": "string", "name": "string"}]'

`File Example:`
    
    
    --add-filestore-instances=path_to_file.(yaml|json)

`--add-flex-start-instances`=[`id`=`ID`],[`machineType`=`MACHINETYPE`],[`maxDuration`=`MAXDURATION`],[`networkTags`=`NETWORKTAGS`],[`zone`=`ZONE`]
     Parameters to define cluster Flex Start instances. 

For example --add-flex-start-instances id=c1,zone=us-central1-a,machineType=n1-standard-1,maxDuration=10000s. 

Sets `add_flex_start_instances` value. 

`id`
     Required, sets `id` value. 
`machineType`
     Required, sets `machineType` value. 
`maxDuration`
     Required, sets `maxDuration` value. 
`networkTags`
     Sets `networkTags` value. 
`zone`
     Required, sets `zone` value. 
`Shorthand Example:`
    
    
    --add-flex-start-instances=id=string,machineType=string,maxDuration=string,networkTags=[string],zone=string --add-flex-start-instances=id=string,machineType=string,maxDuration=string,networkTags=[string],zone=string

`JSON Example:`
    
    
    --add-flex-start-instances='[{"id": "string", "machineType": "string", "maxDuration": "string", "networkTags": ["string"], "zone": "string"}]'

`File Example:`
    
    
    --add-flex-start-instances=path_to_file.(yaml|json)

`--add-labels`=[`ADD_LABELS`,…]
     Cluster labels as key value pairs. 

For example --add-labels key1=value1,key2=value2. 

Sets `add_labels` value. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --add-labels={string=string}

`JSON Example:`
    
    
    --add-labels='{"string": "string"}'

`File Example:`
    
    
    --add-labels=path_to_file.(yaml|json)

`--add-lustre-instances`=[`id`=`ID`],[`name`=`NAME`]
     Reference of existing Lustre instance. 

id: ID of the lustre resource, used to refer to this resource in storage-configs. name: Name of the existing Managed Lustre instance to import from your project in the format of locations/us-central1/instances/lustre-1. 

For example --add-lustre-instances id=my-lustre,name=locations/us-central1/instances/lustre-1. 

Sets `add_lustre_instances` value. 

`id`
     Required, sets `id` value. 
`name`
     Required, sets `name` value. 
`Shorthand Example:`
    
    
    --add-lustre-instances=id=string,name=string --add-lustre-instances=id=string,name=string

`JSON Example:`
    
    
    --add-lustre-instances='[{"id": "string", "name": "string"}]'

`File Example:`
    
    
    --add-lustre-instances=path_to_file.(yaml|json)

`--add-new-filestore-instances`=[`capacityGb`=`CAPACITYGB`],[`description`=`DESCRIPTION`],[`fileshare`=`FILESHARE`],[`id`=`ID`],[`name`=`NAME`],[`protocol`=`PROTOCOL`],[`tier`=`TIER`]
     Parameters to create a filestore instance. 

Required fields: 

  * id 
  * name 
  * tier 
  * capacityGb 
  * fileshare 



For example --create-filestores id=my-fs,name=locations/us-central1/instances/filestore-1,tier=REGIONAL,capacityGb=1024,fileshare=share1 

id: Alphanumeric identifier of the filestore resource. Can be used to refer to this resource in storage-configs. name: Name of the filestore instance to create in your project in the format of locations/us-central1/instances/filestore-1. 

capacityGb: Size of the filestore in GiB. Must be between 1024 and 102400, and must meet scalability requirements described at <https://cloud.google.com/filestore/docs/service-tiers>. 

fileshare: The directory on a Filestore instance where all shared files are stored. Must match the regex `[a-z]([-a-z0-9]*[a-z0-9])?`, be 1-63 characters in length, and comply with RFC1035. 

Supported protocol values: 

  * NFSV3 
  * NFSV41 
  * If not specified, defaults to NFSV3 



Defaults: 

  * protocol: NFSV3. 



Sets `add_new_filestore_instances` value. `Shorthand Example:`
    
    
    --add-new-filestore-instances=capacityGb=int,description=string,fileshare=string,id=string,name=string,protocol=string,tier=string --add-new-filestore-instances=capacityGb=int,description=string,fileshare=string,id=string,name=string,protocol=string,tier=string

`JSON Example:`
    
    
    --add-new-filestore-instances='[{"capacityGb": int, "description": "string", "fileshare": "string", "id": "string", "name": "string", "protocol": "string", "tier": "string"}]'

`File Example:`
    
    
    --add-new-filestore-instances=path_to_file.(yaml|json)

`--add-new-lustre-instances`=[`capacityGb`=`CAPACITYGB`],[`description`=`DESCRIPTION`],[`dynamicTierOptionsMode`=`DYNAMICTIEROPTIONSMODE`],[`filesystem`=`FILESYSTEM`],[`id`=`ID`],[`name`=`NAME`],[`perUnitStorageThroughput`=`PERUNITSTORAGETHROUGHPUT`]
     Parameters to create a Lustre instance. 

Required fields: 

  * id 
  * name 
  * capacityGb 
  * filesystem. 



id: ID of the lustre resource, used to refer to this resource in storage-configs. 

name: Name of the Managed Lustre instance to create in your project in the format of locations/us-central1/instances/lustre-1. 

For example --add-new-lustre-instances id=my-lustre,name=locations/us-central1/instances/lustre-1,capacityGb=1024,filesystem=fs-1,perUnitStorageThroughput=1000 

Values for perUnitStorageThroughput: 125, 250, 500, 1000. 

Sets `add_new_lustre_instances` value. `Shorthand Example:`
    
    
    --add-new-lustre-instances=capacityGb=int,description=string,dynamicTierOptionsMode=string,filesystem=string,id=string,name=string,perUnitStorageThroughput=int --add-new-lustre-instances=capacityGb=int,description=string,dynamicTierOptionsMode=string,filesystem=string,id=string,name=string,perUnitStorageThroughput=int

`JSON Example:`
    
    
    --add-new-lustre-instances='[{"capacityGb": int, "description": "string", "dynamicTierOptionsMode": "string", "filesystem": "string", "id": "string", "name": "string", "perUnitStorageThroughput": int}]'

`File Example:`
    
    
    --add-new-lustre-instances=path_to_file.(yaml|json)

`--add-new-storage-buckets`=[`enableAutoclass`=`ENABLEAUTOCLASS`],[`enableHNS`=`ENABLEHNS`],[`id`=`ID`],[`name`=`NAME`],[`storageClass`=`STORAGECLASS`],[`terminalStorageClass`=`TERMINALSTORAGECLASS`]
     Parameters to create a Google Cloud Storage bucket. 

Required fields: 

  * id 
  * name 



id: Alphanumeric identifier of the bucket resource. Can be used to refer to this resource in storage-configs. 

name: Name of the Cloud Storage bucket. Must be globally unique and omit any sensitive information. 

For example --add-new-storage-buckets id=my-bucket,name=bucket-1,storageClass=STANDARD,terminalStorageClass=NEARLINE,enableHNS=true 

Supported storageClass values: 

  * STANDARD 
  * NEARLINE 
  * COLDLINE 
  * ARCHIVE 



Supported terminalStorageClass values: 

  * NEARLINE 
  * ARCHIVE 



Defaults: 

  * storageClass: STANDARD 



Note: 

  * Either storageClass or enableAutoclass can be set. 
  * HNS: Hierarchical namespace. Hierarchical namespace buckets cannot use Autoclass. 



Sets `add_new_storage_buckets` value. `Shorthand Example:`
    
    
    --add-new-storage-buckets=enableAutoclass=boolean,enableHNS=boolean,id=string,name=string,storageClass=string,terminalStorageClass=string --add-new-storage-buckets=enableAutoclass=boolean,enableHNS=boolean,id=string,name=string,storageClass=string,terminalStorageClass=string

`JSON Example:`
    
    
    --add-new-storage-buckets='[{"enableAutoclass": boolean, "enableHNS": boolean, "id": "string", "name": "string", "storageClass": "string", "terminalStorageClass": "string"}]'

`File Example:`
    
    
    --add-new-storage-buckets=path_to_file.(yaml|json)

`--add-nfs`=[`id`=`ID`],[`mountOptions`=`MOUNTOPTIONS`],[`remoteMount`=`REMOTEMOUNT`],[`serverIpAddress`=`SERVERIPADDRESS`]
     Reference of existing NFS storage to import into your cluster. 

id: ID of the storage resource, used to refer to this resource in storage-configs. serverIpAddress: IP address of the NFS server. remoteMount: Remote mount path on the NFS server. mountOptions: Optional mount options for mounting the NFS share (e.g., ro,nosuid). 

For example --add-nfs id=my-nfs,serverIpAddress=10.0.0.1,remoteMount=/share,mountOptions=ro. 

Sets `add_nfs` value. 

`id`
     Required, sets `id` value. 
`mountOptions`
     Sets `mountOptions` value. 
`remoteMount`
     Required, sets `remoteMount` value. 
`serverIpAddress`
     Required, sets `serverIpAddress` value. 
`Shorthand Example:`
    
    
    --add-nfs=id=string,mountOptions=string,remoteMount=string,serverIpAddress=string --add-nfs=id=string,mountOptions=string,remoteMount=string,serverIpAddress=string

`JSON Example:`
    
    
    --add-nfs='[{"id": "string", "mountOptions": "string", "remoteMount": "string", "serverIpAddress": "string"}]'

`File Example:`
    
    
    --add-nfs=path_to_file.(yaml|json)

`--add-on-demand-instances`=[`id`=`ID`],[`machineType`=`MACHINETYPE`],[`networkTags`=`NETWORKTAGS`],[`zone`=`ZONE`]
     Parameters to define cluster on demand instances. 

For example --add-on-demand-instances id=c1,zone=us-central1-a,machineType=n1-standard-1. 

Sets `add_on_demand_instances` value. 

`id`
     Required, sets `id` value. 
`machineType`
     Required, sets `machineType` value. 
`networkTags`
     Sets `networkTags` value. 
`zone`
     Required, sets `zone` value. 
`Shorthand Example:`
    
    
    --add-on-demand-instances=id=string,machineType=string,networkTags=[string],zone=string --add-on-demand-instances=id=string,machineType=string,networkTags=[string],zone=string

`JSON Example:`
    
    
    --add-on-demand-instances='[{"id": "string", "machineType": "string", "networkTags": ["string"], "zone": "string"}]'

`File Example:`
    
    
    --add-on-demand-instances=path_to_file.(yaml|json)

`--add-reserved-instances`=[`id`=`ID`],[`networkTags`=`NETWORKTAGS`],[`reservation`=`RESERVATION`],[`reservationBlock`=`RESERVATIONBLOCK`],[`reservationSubBlock`=`RESERVATIONSUBBLOCK`]
     Parameters to define cluster reserved instances. 

For example --add-reserved-instances id=c1,reservation=zones/us-central1-a/reservations/reservation-1 

Exactly one of reservation, reservation-block, or reservation-sub-block must be provided. reservation: The name of the reservation to use, in the format zones/us-central1-a/reservations/reservation-1. reservationBlock: The name of the reservation block to use, in the format zones/us-central1-a/reservations/reservation-1/reservationBlocks/block-1. reservationSubBlock: The name of the reservation sub-block to use, in the format zones/us-central1-a/reservations/reservation-1/reservationBlocks/block-1/reservationSubBlocks/sub-block-1. 

Sets `add_reserved_instances` value. 

`id`
     Required, sets `id` value. 
`networkTags`
     Sets `networkTags` value. 
`reservation`
     Sets `reservation` value. 
`reservationBlock`
     Sets `reservationBlock` value. 
`reservationSubBlock`
     Sets `reservationSubBlock` value. 
`Shorthand Example:`
    
    
    --add-reserved-instances=id=string,networkTags=[string],reservation=string,reservationBlock=string,reservationSubBlock=string --add-reserved-instances=id=string,networkTags=[string],reservation=string,reservationBlock=string,reservationSubBlock=string

`JSON Example:`
    
    
    --add-reserved-instances='[{"id": "string", "networkTags": ["string"], "reservation": "string", "reservationBlock": "string", "reservationSubBlock": "string"}]'

`File Example:`
    
    
    --add-reserved-instances=path_to_file.(yaml|json)

`--add-spot-instances`=[`id`=`ID`],[`machineType`=`MACHINETYPE`],[`networkTags`=`NETWORKTAGS`],[`terminationAction`=`TERMINATIONACTION`],[`zone`=`ZONE`]
     Parameters to define cluster spot instances. 

For example --add-spot-instances id=c1,zone=us-central1-a,machineType=n1-standard-1. 

Sets `add_spot_instances` value. 

`id`
     Required, sets `id` value. 
`machineType`
     Required, sets `machineType` value. 
`networkTags`
     Sets `networkTags` value. 
`terminationAction`
     Sets `terminationAction` value. 
`zone`
     Required, sets `zone` value. 
`Shorthand Example:`
    
    
    --add-spot-instances=id=string,machineType=string,networkTags=[string],terminationAction=string,zone=string --add-spot-instances=id=string,machineType=string,networkTags=[string],terminationAction=string,zone=string

`JSON Example:`
    
    
    --add-spot-instances='[{"id": "string", "machineType": "string", "networkTags": ["string"], "terminationAction": "string", "zone": "string"}]'

`File Example:`
    
    
    --add-spot-instances=path_to_file.(yaml|json)

`--add-storage-buckets`=[`id`=`ID`],[`name`=`NAME`]
     Reference of existing Google Cloud Storage bucket. 

id: ID of the bucket resource, used to refer to this resource in storage-configs. name: Name of the existing Cloud Storage bucket to import from your project in the format of bucket-name. 

For example --add-storage-buckets id=my-bucket,name=bucket-1. 

Sets `add_storage_buckets` value. 

`id`
     Required, sets `id` value. 
`name`
     Required, sets `name` value. 
`Shorthand Example:`
    
    
    --add-storage-buckets=id=string,name=string --add-storage-buckets=id=string,name=string

`JSON Example:`
    
    
    --add-storage-buckets='[{"id": "string", "name": "string"}]'

`File Example:`
    
    
    --add-storage-buckets=path_to_file.(yaml|json)

`--description`=`DESCRIPTION`
     Description of the cluster. 

For example --description "My cluster" 

`--remove-filestore-instances`=[`REMOVE_FILESTORE_INSTANCES`,…]
     Parameters to remove filestore instance config by filestore name. 

For example --remove-filestore-instances locations/us-central1/instances/filestore-1,locations/us-central1/instances/filestore-2,… 

`--remove-flex-start-instances`=[`REMOVE_FLEX_START_INSTANCES`,…]
     Parameters to remove Flex Start instance config by compute id. 

For example --remove-flex-start-instances c1,c2,… 

`--remove-labels`=[`REMOVE_LABELS`,…]
     Parameters to remove cluster label by key. 

For example --remove-labels key1,key2,… 

`--remove-lustre-instances`=[`REMOVE_LUSTRE_INSTANCES`,…]
     Parameters to remove lustre instance config by lustre name. 

For example --remove-lustre-instances locations/us-central1/instances/lustre-1,locations/us-central1/instances/lustre-2,… 

`--remove-nfs`=[`REMOVE_NFS`,…]
     Parameters to remove NFS storage resource config by storage ID. 

For example --remove-nfs my-nfs-1,my-nfs-2,… 

`--remove-on-demand-instances`=[`REMOVE_ON_DEMAND_INSTANCES`,…]
     Parameters to remove on demand instances config by compute id. 

For example --remove-on-demand-instances c1,c2,… 

`--remove-reserved-instances`=[`REMOVE_RESERVED_INSTANCES`,…]
     Parameters to remove reserved instance config by compute id. 

For example --remove-reserved-instances c1,c2,… 

`--remove-spot-instances`=[`REMOVE_SPOT_INSTANCES`,…]
     Parameters to remove spot instance config by compute id. 

For example --remove-spot-instances c1,c2,… 

`--remove-storage-buckets`=[`REMOVE_STORAGE_BUCKETS`,…]
     Parameters to remove Google Cloud Storage bucket by bucket name. 

For example --remove-storage-buckets bucket-1,bucket-2,… 

Orchestrator configuration for the cluster. 

At most one of these can be specified: 

Configuration of orchestration type for Managed Compute Clusters. 
`--add-managed-instance-groups`=[`acceleratorTopology`=`ACCELERATORTOPOLOGY`],[`bootDisk`=`BOOTDISK`],[`computeId`=`COMPUTEID`],[`enablePublicIps`=`ENABLEPUBLICIPS`],[`id`=`ID`],[`startupScript`=`STARTUPSCRIPT`],[`storageConfigs`=`STORAGECONFIGS`],[`targetSize`=`TARGETSIZE`]
     Parameters to define Compute Engine orchestrator managed instance group config. 

Required fields: 

  * id 
  * computeId 



For example --add-managed-instance-groups id=mig1,computeId=c1,targetSize=2,\ acceleratorTopology=2x4,enablePublicIps=true,\ startupScript="echo hello",bootDisk="{type=pd-balanced,sizeGb=100}" 

Note: 

  * startupScript: 
    * Either str or file_path 
    * For file_path, only bash file format (.sh or .bash) is supported. 
    * For file_path, only absolute path is supported. 
  * bootDisk.storagePools: 
    * At most 1 storage pool is supported. 
    * storagePools: The name of the storage pool to use, in the format zones/us-central1-a/storagePools/pool1. 

Sets `add_managed_instance_groups` value. 


`Shorthand Example:`
    
    
    --add-managed-instance-groups=acceleratorTopology=string,bootDisk={image=string,sizeGb=int,storagePools=[string],type=string},computeId=string,enablePublicIps=boolean,id=string,startupScript=string,storageConfigs=[{id=string,localMount=string}],targetSize=int --add-managed-instance-groups=acceleratorTopology=string,bootDisk={image=string,sizeGb=int,storagePools=[string],type=string},computeId=string,enablePublicIps=boolean,id=string,startupScript=string,storageConfigs=[{id=string,localMount=string}],targetSize=int

`JSON Example:`
    
    
    --add-managed-instance-groups='[{"acceleratorTopology": "string", "bootDisk": {"image": "string", "sizeGb": int, "storagePools": ["string"], "type": "string"}, "computeId": "string", "enablePublicIps": boolean, "id": "string", "startupScript": "string", "storageConfigs": [{"id": "string", "localMount": "string"}], "targetSize": int}]'

`File Example:`
    
    
    --add-managed-instance-groups=path_to_file.(yaml|json)

`--remove-managed-instance-groups`=[`REMOVE_MANAGED_INSTANCE_GROUPS`,…]
     Parameters to remove managed instance group config by id. 

For example --remove-managed-instance-groups mig1,mig2,… 

`--update-managed-instance-groups`=[`acceleratorTopology`=`ACCELERATORTOPOLOGY`],[`bootDisk`=`BOOTDISK`],[`computeId`=`COMPUTEID`],[`enablePublicIps`=`ENABLEPUBLICIPS`],[`id`=`ID`],[`startupScript`=`STARTUPSCRIPT`],[`storageConfigs`=`STORAGECONFIGS`],[`targetSize`=`TARGETSIZE`]
     Parameters to update Compute Engine orchestrator managed instance group config. 

Required fields: 

  * id 



For example --update-managed-instance-groups id=mig1,targetSize=4,\ startupScript="echo updated". 

Sets `update_managed_instance_groups` value. `Shorthand Example:`
    
    
    --update-managed-instance-groups=acceleratorTopology=string,bootDisk={image=string,sizeGb=int,storagePools=[string],type=string},computeId=string,enablePublicIps=boolean,id=string,startupScript=string,storageConfigs=[{id=string,localMount=string}],targetSize=int --update-managed-instance-groups=acceleratorTopology=string,bootDisk={image=string,sizeGb=int,storagePools=[string],type=string},computeId=string,enablePublicIps=boolean,id=string,startupScript=string,storageConfigs=[{id=string,localMount=string}],targetSize=int

`JSON Example:`
    
    
    --update-managed-instance-groups='[{"acceleratorTopology": "string", "bootDisk": {"image": "string", "sizeGb": int, "storagePools": ["string"], "type": "string"}, "computeId": "string", "enablePublicIps": boolean, "id": "string", "startupScript": "string", "storageConfigs": [{"id": "string", "localMount": "string"}], "targetSize": int}]'

`File Example:`
    
    
    --update-managed-instance-groups=path_to_file.(yaml|json)

Slurm orchestrator configuration for the cluster. 
`--add-slurm-epilog-scripts`=[`ADD_SLURM_EPILOG_SCRIPTS`,…]
     Slurm epilog bash scripts. 

For example --add-slurm-epilog-scripts script1.sh,script2.sh 

`--add-slurm-node-sets`=[`bootDisk`=`BOOTDISK`],[`computeId`=`COMPUTEID`],[`computeInstance`=`COMPUTEINSTANCE`],[`config`=`CONFIG`],[`container-resource-labels`=`CONTAINER-RESOURCE-LABELS`],[`container-startup-script`=`CONTAINER-STARTUP-SCRIPT`],[`containerNodePool`=`CONTAINERNODEPOOL`],[`id`=`ID`],[`labels`=`LABELS`],[`maxDynamicNodeCount`=`MAXDYNAMICNODECOUNT`],[`startupScript`=`STARTUPSCRIPT`],[`startupScriptTimeout`=`STARTUPSCRIPTTIMEOUT`],[`staticNodeCount`=`STATICNODECOUNT`],[`storageConfigs`=`STORAGECONFIGS`],[`type`=`TYPE`]
     Parameters to define slurm cluster nodeset config. 

Required fields: 

  * id 



For example --add-slurm-node-sets id=ns1,computeId=c1,type=gce,staticNodeCount=1,maxDynamicNodeCount=2,startupScript="echo hello",bootDisk=type=hyperdisk-balanced,storagePools=[zones/us-central1-a/storagePools/pool1] 

To configure a nodeset backed by Google Kubernetes Engine, use type=gke. If type=gke is specified, Compute Engine specific fields (labels, startupScript, bootDisk, startupScriptTimeout) cannot be used, but container-specific fields (container-resource-labels, container-startup-script) may be used. For example \--add-slurm-node-sets id=ns1,computeId=c1,type=gke For example \--add-slurm-node-sets id=ns1,computeId=c1,type=gke,container-resource-labels="k1=v1",container-startup-script="echo hello" 

Defaults: 

  * type: gce 



Note: 

  * startupScript: 
    * Either str or file_path 
    * For file_path, only bash file format (.sh or .bash) is supported. 
    * For file_path, only absolute path is supported. 
  * bootDisk.storagePools: 
    * At most 1 storage pool is supported. 
    * storagePools: The name of the storage pool to use, in the format zones/us-central1-a/storagePools/pool1. 

Sets `add_slurm_node_sets` value. 


`Shorthand Example:`
    
    
    --add-slurm-node-sets=bootDisk={image=string,sizeGb=int,storagePools=[string],type=string},computeId=string,computeInstance={bootDisk={image=string,sizeGb=int,storagePools=[string],type=string},labels={string=string},startupScript=string,startupScriptTimeout=string},config={coreSpecCount=string,cpuSpecList=string,features=string,memSpecLimit=string,weight=string},container-resource-labels={string=string},container-startup-script=string,containerNodePool={resourceLabels={string=string},startupScript=string},id=string,labels={string=string},maxDynamicNodeCount=int,startupScript=string,startupScriptTimeout=string,staticNodeCount=int,storageConfigs=[{id=string,localMount=string}],type=string --add-slurm-node-sets=bootDisk={image=string,sizeGb=int,storagePools=[string],type=string},computeId=string,computeInstance={bootDisk={image=string,sizeGb=int,storagePools=[string],type=string},labels={string=string},startupScript=string,startupScriptTimeout=string},config={coreSpecCount=string,cpuSpecList=string,features=string,memSpecLimit=string,weight=string},container-resource-labels={string=string},container-startup-script=string,containerNodePool={resourceLabels={string=string},startupScript=string},id=string,labels={string=string},maxDynamicNodeCount=int,startupScript=string,startupScriptTimeout=string,staticNodeCount=int,storageConfigs=[{id=string,localMount=string}],type=string

`JSON Example:`
    
    
    --add-slurm-node-sets='[{"bootDisk": {"image": "string", "sizeGb": int, "storagePools": ["string"], "type": "string"}, "computeId": "string", "computeInstance": {"bootDisk": {"image": "string", "sizeGb": int, "storagePools": ["string"], "type": "string"}, "labels": {"string": "string"}, "startupScript": "string", "startupScriptTimeout": "string"}, "config": {"coreSpecCount": "string", "cpuSpecList": "string", "features": "string", "memSpecLimit": "string", "weight": "string"}, "container-resource-labels": {"string": "string"}, "container-startup-script": "string", "containerNodePool": {"resourceLabels": {"string": "string"}, "startupScript": "string"}, "id": "string", "labels": {"string": "string"}, "maxDynamicNodeCount": int, "startupScript": "string", "startupScriptTimeout": "string", "staticNodeCount": int, "storageConfigs": [{"id": "string", "localMount": "string"}], "type": "string"}]'

`File Example:`
    
    
    --add-slurm-node-sets=path_to_file.(yaml|json)

`--add-slurm-partitions`=[`config`=`CONFIG`],[`id`=`ID`],[`nodeSetIds`=`NODESETIDS`]
     Parameters to define slurm cluster partitions. 

For example --add-slurm-partitions id=p1,nodesetIds=[ns1,ns2]. 

Sets `add_slurm_partitions` value. 

`config`
     Sets `config` value. 

`allowAccounts`
     Sets `allowAccounts` value. 
`allowQos`
     Sets `allowQos` value. 
`defMemPerCpu`
     Sets `defMemPerCpu` value. 
`defaultTime`
     Sets `defaultTime` value. 
`denyAccounts`
     Sets `denyAccounts` value. 
`denyQos`
     Sets `denyQos` value. 
`exclusiveUser`
     Sets `exclusiveUser` value. 
`graceTime`
     Sets `graceTime` value. 
`maxNodes`
     Sets `maxNodes` value. 
`maxTime`
     Sets `maxTime` value. 
`overSubscribe`
     Sets `overSubscribe` value. 
`overTimeLimit`
     Sets `overTimeLimit` value. 
`preemptMode`
     Sets `preemptMode` value. 
`priorityJobFactor`
     Sets `priorityJobFactor` value. 
`priorityTier`
     Sets `priorityTier` value. 
`qos`
     Sets `qos` value. 
`tresBillingWeights`
     Sets `tresBillingWeights` value. 
`id`
     Required, sets `id` value. 
`nodeSetIds`
     Required, sets `nodeSetIds` value. 
`Shorthand Example:`
    
    
    --add-slurm-partitions=config={allowAccounts=string,allowQos=string,defMemPerCpu=string,defaultTime=string,denyAccounts=string,denyQos=string,exclusiveUser=string,graceTime=string,maxNodes=string,maxTime=string,overSubscribe=string,overTimeLimit=string,preemptMode=string,priorityJobFactor=string,priorityTier=string,qos=string,tresBillingWeights=string},id=string,nodeSetIds=[string] --add-slurm-partitions=config={allowAccounts=string,allowQos=string,defMemPerCpu=string,defaultTime=string,denyAccounts=string,denyQos=string,exclusiveUser=string,graceTime=string,maxNodes=string,maxTime=string,overSubscribe=string,overTimeLimit=string,preemptMode=string,priorityJobFactor=string,priorityTier=string,qos=string,tresBillingWeights=string},id=string,nodeSetIds=[string]

`JSON Example:`
    
    
    --add-slurm-partitions='[{"config": {"allowAccounts": "string", "allowQos": "string", "defMemPerCpu": "string", "defaultTime": "string", "denyAccounts": "string", "denyQos": "string", "exclusiveUser": "string", "graceTime": "string", "maxNodes": "string", "maxTime": "string", "overSubscribe": "string", "overTimeLimit": "string", "preemptMode": "string", "priorityJobFactor": "string", "priorityTier": "string", "qos": "string", "tresBillingWeights": "string"}, "id": "string", "nodeSetIds": ["string"]}]'

`File Example:`
    
    
    --add-slurm-partitions=path_to_file.(yaml|json)

`--add-slurm-prolog-scripts`=[`ADD_SLURM_PROLOG_SCRIPTS`,…]
     Slurm prolog bash scripts. 

For example --add-slurm-prolog-scripts script1.sh,script2.sh 

`--add-slurm-task-epilog-scripts`=[`ADD_SLURM_TASK_EPILOG_SCRIPTS`,…]
     Slurm task epilog bash scripts. 

For example --add-slurm-task-epilog-scripts script1.sh,script2.sh 

`--add-slurm-task-prolog-scripts`=[`ADD_SLURM_TASK_PROLOG_SCRIPTS`,…]
     Slurm task prolog bash scripts. 

For example --add-slurm-task-prolog-scripts script1.sh,script2.sh 

`--enable-slurm-health-check`
     If false, Slurm health checking is disabled, and health_check_interval, health_check_node_state, and health_check_program should not be passed in. 

For example --no-enable-slurm-health-check. 

Enabled by default, use `--no-enable-slurm-health-check` to disable. 

`--remove-slurm-epilog-scripts`=[`REMOVE_SLURM_EPILOG_SCRIPTS`,…]
     Scripts to remove from Slurm epilog bash scripts. 

For example --remove-slurm-epilog-scripts script1.sh,script2.sh 

`--remove-slurm-node-sets`=[`REMOVE_SLURM_NODE_SETS`,…]
     Parameters to remove slurm nodeset config by nodeset id. 

For example --remove-slurm-node-sets ns1,ns2,… 

`--remove-slurm-partitions`=[`REMOVE_SLURM_PARTITIONS`,…]
     Parameters to remove slurm partition config by partition id. 

For example --remove-slurm-partitions p1,p2,… 

`--remove-slurm-prolog-scripts`=[`REMOVE_SLURM_PROLOG_SCRIPTS`,…]
     Scripts to remove from Slurm prolog bash scripts. 

For example --remove-slurm-prolog-scripts script1.sh,script2.sh 

`--remove-slurm-task-epilog-scripts`=[`REMOVE_SLURM_TASK_EPILOG_SCRIPTS`,…]
     Scripts to remove from Slurm task epilog bash scripts. 

For example --remove-slurm-task-epilog-scripts script1.sh,script2.sh 

`--remove-slurm-task-prolog-scripts`=[`REMOVE_SLURM_TASK_PROLOG_SCRIPTS`,…]
     Scripts to remove from Slurm task prolog bash scripts. 

For example --remove-slurm-task-prolog-scripts script1.sh,script2.sh 

`--slurm-default-partition`=`SLURM_DEFAULT_PARTITION`
     Parameters to define slurm cluster default partition. 

For example --slurm-default-partition p1 

`--update-slurm-login-node`=[`bootDisk`=`BOOTDISK`],[`count`=`COUNT`],[`startupScript`=`STARTUPSCRIPT`]
     Parameters to update slurm cluster login node. Only bootDisk, count and startupScript can be updated. 

For example --update-slurm-login-node count=2,startupScript="echo hello",bootDisk=type=hyperdisk-balanced,storagePools=[zones/us-central1-a/storagePools/pool1] 

Note: 

  * bootDisk.storagePools: 
    * At most 1 storage pool is supported. 
    * storagePools: The name of the storage pool to use, in the format zones/us-central1-a/storagePools/pool1. 

Sets `update_slurm_login_node` value. 


`Shorthand Example:`
    
    
    --update-slurm-login-node=bootDisk={image=string,sizeGb=int,storagePools=[string],type=string},count=int,startupScript=string

`JSON Example:`
    
    
    --update-slurm-login-node='{"bootDisk": {"image": "string", "sizeGb": int, "storagePools": ["string"], "type": "string"}, "count": int, "startupScript": "string"}'

`File Example:`
    
    
    --update-slurm-login-node=path_to_file.(yaml|json)

`--update-slurm-node-sets`=[`bootDisk`=`BOOTDISK`],[`computeId`=`COMPUTEID`],[`computeInstance`=`COMPUTEINSTANCE`],[`config`=`CONFIG`],[`container-resource-labels`=`CONTAINER-RESOURCE-LABELS`],[`container-startup-script`=`CONTAINER-STARTUP-SCRIPT`],[`containerNodePool`=`CONTAINERNODEPOOL`],[`id`=`ID`],[`labels`=`LABELS`],[`maxDynamicNodeCount`=`MAXDYNAMICNODECOUNT`],[`startupScript`=`STARTUPSCRIPT`],[`startupScriptTimeout`=`STARTUPSCRIPTTIMEOUT`],[`staticNodeCount`=`STATICNODECOUNT`],[`storageConfigs`=`STORAGECONFIGS`],[`type`=`TYPE`]
     Parameters to define and update slurm cluster nodeset config. 

For example --update-slurm-node-sets id=ns1,staticNodeCount=1,maxDynamicNodeCount=2 

To update a node set backed by GKE, use container-resource-labels or container-startup-script. For example --update-slurm-node-sets id=ns1,type=gke,container-resource-labels="k1=v1",container-startup-script="echo hello". 

Sets `update_slurm_node_sets` value. `Shorthand Example:`
    
    
    --update-slurm-node-sets=bootDisk={image=string,sizeGb=int,storagePools=[string],type=string},computeId=string,computeInstance={bootDisk={image=string,sizeGb=int,storagePools=[string],type=string},labels={string=string},startupScript=string,startupScriptTimeout=string},config={coreSpecCount=string,cpuSpecList=string,features=string,memSpecLimit=string,weight=string},container-resource-labels={string=string},container-startup-script=string,containerNodePool={resourceLabels={string=string},startupScript=string},id=string,labels={string=string},maxDynamicNodeCount=int,startupScript=string,startupScriptTimeout=string,staticNodeCount=int,storageConfigs=[{id=string,localMount=string}],type=string --update-slurm-node-sets=bootDisk={image=string,sizeGb=int,storagePools=[string],type=string},computeId=string,computeInstance={bootDisk={image=string,sizeGb=int,storagePools=[string],type=string},labels={string=string},startupScript=string,startupScriptTimeout=string},config={coreSpecCount=string,cpuSpecList=string,features=string,memSpecLimit=string,weight=string},container-resource-labels={string=string},container-startup-script=string,containerNodePool={resourceLabels={string=string},startupScript=string},id=string,labels={string=string},maxDynamicNodeCount=int,startupScript=string,startupScriptTimeout=string,staticNodeCount=int,storageConfigs=[{id=string,localMount=string}],type=string

`JSON Example:`
    
    
    --update-slurm-node-sets='[{"bootDisk": {"image": "string", "sizeGb": int, "storagePools": ["string"], "type": "string"}, "computeId": "string", "computeInstance": {"bootDisk": {"image": "string", "sizeGb": int, "storagePools": ["string"], "type": "string"}, "labels": {"string": "string"}, "startupScript": "string", "startupScriptTimeout": "string"}, "config": {"coreSpecCount": "string", "cpuSpecList": "string", "features": "string", "memSpecLimit": "string", "weight": "string"}, "container-resource-labels": {"string": "string"}, "container-startup-script": "string", "containerNodePool": {"resourceLabels": {"string": "string"}, "startupScript": "string"}, "id": "string", "labels": {"string": "string"}, "maxDynamicNodeCount": int, "startupScript": "string", "startupScriptTimeout": "string", "staticNodeCount": int, "storageConfigs": [{"id": "string", "localMount": "string"}], "type": "string"}]'

`File Example:`
    
    
    --update-slurm-node-sets=path_to_file.(yaml|json)

`--update-slurm-partitions`=[`config`=`CONFIG`],[`id`=`ID`],[`nodeSetIds`=`NODESETIDS`]
     Parameters to define and update slurm cluster partition config. 

For example --update-slurm-partitions id=p1,nodesetIds=[ns1,ns2]. 

Sets `update_slurm_partitions` value. 

`config`
     Sets `config` value. 

`allowAccounts`
     Sets `allowAccounts` value. 
`allowQos`
     Sets `allowQos` value. 
`defMemPerCpu`
     Sets `defMemPerCpu` value. 
`defaultTime`
     Sets `defaultTime` value. 
`denyAccounts`
     Sets `denyAccounts` value. 
`denyQos`
     Sets `denyQos` value. 
`exclusiveUser`
     Sets `exclusiveUser` value. 
`graceTime`
     Sets `graceTime` value. 
`maxNodes`
     Sets `maxNodes` value. 
`maxTime`
     Sets `maxTime` value. 
`overSubscribe`
     Sets `overSubscribe` value. 
`overTimeLimit`
     Sets `overTimeLimit` value. 
`preemptMode`
     Sets `preemptMode` value. 
`priorityJobFactor`
     Sets `priorityJobFactor` value. 
`priorityTier`
     Sets `priorityTier` value. 
`qos`
     Sets `qos` value. 
`tresBillingWeights`
     Sets `tresBillingWeights` value. 
`id`
     Required, sets `id` value. 
`nodeSetIds`
     Sets `nodeSetIds` value. 
`Shorthand Example:`
    
    
    --update-slurm-partitions=config={allowAccounts=string,allowQos=string,defMemPerCpu=string,defaultTime=string,denyAccounts=string,denyQos=string,exclusiveUser=string,graceTime=string,maxNodes=string,maxTime=string,overSubscribe=string,overTimeLimit=string,preemptMode=string,priorityJobFactor=string,priorityTier=string,qos=string,tresBillingWeights=string},id=string,nodeSetIds=[string] --update-slurm-partitions=config={allowAccounts=string,allowQos=string,defMemPerCpu=string,defaultTime=string,denyAccounts=string,denyQos=string,exclusiveUser=string,graceTime=string,maxNodes=string,maxTime=string,overSubscribe=string,overTimeLimit=string,preemptMode=string,priorityJobFactor=string,priorityTier=string,qos=string,tresBillingWeights=string},id=string,nodeSetIds=[string]

`JSON Example:`
    
    
    --update-slurm-partitions='[{"config": {"allowAccounts": "string", "allowQos": "string", "defMemPerCpu": "string", "defaultTime": "string", "denyAccounts": "string", "denyQos": "string", "exclusiveUser": "string", "graceTime": "string", "maxNodes": "string", "maxTime": "string", "overSubscribe": "string", "overTimeLimit": "string", "preemptMode": "string", "priorityJobFactor": "string", "priorityTier": "string", "qos": "string", "tresBillingWeights": "string"}, "id": "string", "nodeSetIds": ["string"]}]'

`File Example:`
    
    
    --update-slurm-partitions=path_to_file.(yaml|json)

At most one of these can be specified: 

`--slurm-conf-file`=`SLURM_CONF_FILE`
     Path to the slurm.conf file. 

When updating, the provided configuration file declaratively replaces the cluster's existing Slurm configuration across global settings, node set configurations, and partition configurations: 

  * Global directives in the file replace the existing cluster Slurm global configuration (omitted global settings or an empty file will clear existing custom global config). Custom global directives not recognized as first-class fields are passed through as additionalSettings. 
  * NodeName and PartitionName directives in the file replace the configurations of matching existing node sets and partitions in the cluster (node sets or partitions not present in the file have their custom configurations cleared). 



See <https://slurm.schedmd.com/slurm.conf.html> for more details. 

For example --slurm-conf-file=path/to/slurm.conf 

`--update-slurm-config`=[`UPDATE_SLURM_CONFIG`,…]
     Parameters to update slurm cluster config. 

Supports both dot-notation (e.g. `schedulerParameters.bfBusyNodes=true` or `schedulerParameters.bf_busy_nodes=true`, `additionalSettings.MaxArraySize=10000`) and sub-dictionary notation (e.g. `schedulerParameters="{bfBusyNodes=true,bfInterval=30}"` or `schedulerParameters="{bf_busy_nodes=true,bf_interval=30}"`, `additionalSettings="{MaxArraySize=10000,TreeWidth=50}"`). Both camelCase and snake_case (matching native Slurm parameter names) are supported for nested parameters. 

For example: --update-slurm-config defMemPerCpu=2048,healthCheckInterval=10,schedulerParameters.bf_busy_nodes=true,preemptParameters.youngest_first=true,additionalSettings.MaxArraySize=10000 or --update-slurm-config defMemPerCpu=2048,schedulerParameters="{bf_busy_nodes=true,bf_interval=30}",preemptParameters="{youngest_first=true,suspend_grace_time=60}" 

Cluster configuration for updates. 
`--config`=[`computeResources`=`COMPUTERESOURCES`],[`description`=`DESCRIPTION`],[`labels`=`LABELS`],[`name`=`NAME`],[`networkResources`=`NETWORKRESOURCES`],[`orchestrator`=`ORCHESTRATOR`],[`storageResources`=`STORAGERESOURCES`]
     Configuration of the cluster specs in the form of a JSON object. Required, See example below: 
    
    
    --config='{
      "networkResources": {
          "network0": {
              "config": {
                  "newNetwork": {
                      "network": "network0"
                  }
              }
          }
      },
      "storageResources": {
          "lustre0": {
              "config": {
                  "newLustre": {
                      "capacityGb": 1200,
                      "filesystem": "lustre-fs"
                  }
              }
          }
      },
      "computeResources": {
          "compute0": {
              "config": {
                  "newOnDemandInstances": {
                      "machineType": "n2-standard-4",
                      "zone": "us-central1-a"
                  }
              }
          }
      },
      "orchestrator": {
          "slurm": {
              "nodeSets": [
                  {
                      "id": "nodeset0",
                      "computeId": "compute0"
                  }
              ]
          }
      }
    
    
    
     }' --format json.

`Shorthand Example:`
    
    
    --config=computeResources={string={config={newDwsFlexInstances={machineType=string,maxDuration=string,networkTags=[string],terminationAction=string,zone=string},newFlexStartInstances={machineType=string,maxDuration=string,networkTags=[string],terminationAction=string,zone=string},newOnDemandInstances={machineType=string,networkTags=[string],zone=string},newReservedInstances={machineType=string,networkTags=[string],reservation=string,reservationBlock=string,reservationSubBlock=string,type=string,zone=string},newSpotInstances={machineType=string,networkTags=[string],terminationAction=string,zone=string}}}},description=string,labels={string=string},name=string,networkResources={string={config={existingComputeNetwork={network=string,subnetwork=string},existingNetwork={network=string,subnetwork=string},newComputeNetwork={description=string,network=string},newNetwork={description=string,network=string}}}},orchestrator={computeEngine={managedInstanceGroups={string={bootDisk={image=string,sizeGb=int,storagePools=[string],type=string},computeId=string,enablePublicIps=boolean,resourcePolicyConfig={acceleratorTopology=string},startupScript=string,storageConfigs=[{id=string,localMount=string}],targetSize=int}}},slurm={defaultPartition=string,epilogBashScripts,loginNodes={bootDisk={image=string,sizeGb=int,storagePools=[string],type=string},count=int,enableOsLogin=boolean,enablePublicIps=boolean,labels={string=string},machineType=string,networkTags=[string],startupScript=string,storageConfigs=[{id=string,localMount=string}],zone=string},nodeSets=[{computeId=string,computeInstance={bootDisk={image=string,sizeGb=int,storagePools=[string],type=string},labels={string=string},startupScript=string,startupScriptTimeout=string},containerNodePool,id=string,maxDynamicNodeCount=int,staticNodeCount=int,storageConfigs=[{id=string,localMount=string}]}],partitions=[{id=string,nodeSetIds=[string]}],prologBashScripts}},storageResources={string={config={existingBucket={bucket=string},existingFilestore={filestore=string},existingLustre={lustre=string},existingNfs={mountOptions=string,remoteMount=string,serverIpAddress=string},newBucket={autoclass={enabled=boolean,terminalStorageClass=string},bucket=string,hierarchicalNamespace={enabled=boolean},storageClass=string},newFilestore={description=string,fileShares=[{capacityGb=int,fileShare=string}],filestore=string,id=string,protocol=string,tier=string},newLustre={capacityGb=int,description=string,dynamicTierOptions={mode=string},filesystem=string,id=string,lustre=string,perUnitStorageThroughput=int}}}}

`JSON Example:`
    
    
    --config='{"computeResources": {"string": {"config": {"newDwsFlexInstances": {"machineType": "string", "maxDuration": "string", "networkTags": ["string"], "terminationAction": "string", "zone": "string"}, "newFlexStartInstances": {"machineType": "string", "maxDuration": "string", "networkTags": ["string"], "terminationAction": "string", "zone": "string"}, "newOnDemandInstances": {"machineType": "string", "networkTags": ["string"], "zone": "string"}, "newReservedInstances": {"machineType": "string", "networkTags": ["string"], "reservation": "string", "reservationBlock": "string", "reservationSubBlock": "string", "type": "string", "zone": "string"}, "newSpotInstances": {"machineType": "string", "networkTags": ["string"], "terminationAction": "string", "zone": "string"}}}}, "description": "string", "labels": {"string": "string"}, "name": "string", "networkResources": {"string": {"config": {"existingComputeNetwork": {"network": "string", "subnetwork": "string"}, "existingNetwork": {"network": "string", "subnetwork": "string"}, "newComputeNetwork": {"description": "string", "network": "string"}, "newNetwork": {"description": "string", "network": "string"}}}}, "orchestrator": {"computeEngine": {"managedInstanceGroups": {"string": {"bootDisk": {"image": "string", "sizeGb": int, "storagePools": ["string"], "type": "string"}, "computeId": "string", "enablePublicIps": boolean, "resourcePolicyConfig": {"acceleratorTopology": "string"}, "startupScript": "string", "storageConfigs": [{"id": "string", "localMount": "string"}], "targetSize": int}}}, "slurm": {"defaultPartition": "string", "epilogBashScripts", "loginNodes": {"bootDisk": {"image": "string", "sizeGb": int, "storagePools": ["string"], "type": "string"}, "count": int, "enableOsLogin": boolean, "enablePublicIps": boolean, "labels": {"string": "string"}, "machineType": "string", "networkTags": ["string"], "startupScript": "string", "storageConfigs": [{"id": "string", "localMount": "string"}], "zone": "string"}, "nodeSets": [{"computeId": "string", "computeInstance": {"bootDisk": {"image": "string", "sizeGb": int, "storagePools": ["string"], "type": "string"}, "labels": {"string": "string"}, "startupScript": "string", "startupScriptTimeout": "string"}, "containerNodePool": {}, "id": "string", "maxDynamicNodeCount": int, "staticNodeCount": int, "storageConfigs": [{"id": "string", "localMount": "string"}]}], "partitions": [{"id": "string", "nodeSetIds": ["string"]}], "prologBashScripts"}}, "storageResources": {"string": {"config": {"existingBucket": {"bucket": "string"}, "existingFilestore": {"filestore": "string"}, "existingLustre": {"lustre": "string"}, "existingNfs": {"mountOptions": "string", "remoteMount": "string", "serverIpAddress": "string"}, "newBucket": {"autoclass": {"enabled": boolean, "terminalStorageClass": "string"}, "bucket": "string", "hierarchicalNamespace": {"enabled": boolean}, "storageClass": "string"}, "newFilestore": {"description": "string", "fileShares": [{"capacityGb": int, "fileShare": "string"}], "filestore": "string", "id": "string", "protocol": "string", "tier": "string"}, "newLustre": {"capacityGb": int, "description": "string", "dynamicTierOptions": {"mode": "string"}, "filesystem": "string", "id": "string", "lustre": "string", "perUnitStorageThroughput": int}}}}}'

`File Example:`
    
    
    --config=path_to_file.(yaml|json)

This flag argument must be specified if any of the other arguments in this group are specified. 

`--update-mask`=`UPDATE_MASK`
     Update mask to specify the fields to update. 

For example --update-mask "description,labels". 

Required, sets `update_mask` value. `Input Example:`
    
    
    --update-mask=string

`File Example:`
    
    
    --update-mask=path_to_file.(yaml|json)

This flag argument must be specified if any of the other arguments in this group are specified. 

OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud cluster-director clusters update](https://docs.cloud.google.com/sdk/gcloud/reference/cluster-director/clusters/update)
    
    
    [gcloud beta cluster-director clusters update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/cluster-director/clusters/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
