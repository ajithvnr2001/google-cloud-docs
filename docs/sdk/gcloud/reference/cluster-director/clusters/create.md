---
url: https://docs.cloud.google.com/sdk/gcloud/reference/cluster-director/clusters/create/
title: gcloud cluster-director clusters create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:19:01.397085+00:00
---

# gcloud cluster-director clusters create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/cluster-director/clusters/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud cluster-director clusters create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud cluster-director clusters create - creates a Cluster Director resource 
SYNOPSIS
    

`gcloud cluster-director clusters create` (`CLUSTER` : `--location`=`LOCATION`) (`--config`=[`computeResources`=`COMPUTERESOURCES`],[`description`=`DESCRIPTION`],[`labels`=`LABELS`],[`name`=`NAME`],[`networkResources`=`NETWORKRESOURCES`],[`orchestrator`=`ORCHESTRATOR`],[`storageResources`=`STORAGERESOURCES`] | `--buckets`=[`id`=`ID`],[`name`=`NAME`] `--create-buckets`=[`enableAutoclass`=`ENABLEAUTOCLASS`],[`enableHNS`=`ENABLEHNS`],[`id`=`ID`],[`name`=`NAME`],[`storageClass`=`STORAGECLASS`] `--create-filestores`=[`capacityGb`=`CAPACITYGB`],[`description`=`DESCRIPTION`],[`fileshare`=`FILESHARE`],[`id`=`ID`],[`name`=`NAME`],[`protocol`=`PROTOCOL`],[`tier`=`TIER`] `--create-lustres`=[`capacityGb`=`CAPACITYGB`],[`description`=`DESCRIPTION`],[`filesystem`=`FILESYSTEM`],[`id`=`ID`],[`name`=`NAME`],[`perUnitStorageThroughput`=`PERUNITSTORAGETHROUGHPUT`] `--description`=`DESCRIPTION` `--filestores`=[`id`=`ID`],[`name`=`NAME`] `--flex-start-instances`=[`id`=`ID`],[`machineType`=`MACHINETYPE`],[`maxDuration`=`MAXDURATION`],[`zone`=`ZONE`] `--labels`=[`LABELS`,…] `--lustres`=[`id`=`ID`],[`name`=`NAME`] `--on-demand-instances`=[`id`=`ID`],[`machineType`=`MACHINETYPE`],[`zone`=`ZONE`] `--reserved-instances`=[`id`=`ID`],[`reservation`=`RESERVATION`] `--spot-instances`=[`id`=`ID`],[`machineType`=`MACHINETYPE`],[`terminationAction`=`TERMINATIONACTION`],[`zone`=`ZONE`] `--create-network`=[`description`=`DESCRIPTION`],[`name`=`NAME`] | [`--network`=`NETWORK` `--subnet`=`SUBNET` : `--network-project`=`NETWORK_PROJECT`] `--quickstart-cluster` | `--reference-architecture`=`REFERENCE_ARCHITECTURE` `--slurm-default-partition`=`SLURM_DEFAULT_PARTITION` `--slurm-epilog-scripts`=[`SLURM_EPILOG_SCRIPTS`,…] `--slurm-login-node`=[`bootDisk`=`BOOTDISK`],[`count`=`COUNT`],[`enableOsLogin`=`ENABLEOSLOGIN`],[`enablePublicIps`=`ENABLEPUBLICIPS`],[`labels`=`LABELS`],[`machineType`=`MACHINETYPE`],[`startupScript`=`STARTUPSCRIPT`],[`storageConfigs`=`STORAGECONFIGS`],[`zone`=`ZONE`] `--slurm-node-sets`=[`computeId`=`COMPUTEID`],[`computeInstance`=`COMPUTEINSTANCE`],[`id`=`ID`],[`maxDynamicNodeCount`=`MAXDYNAMICNODECOUNT`],[`staticNodeCount`=`STATICNODECOUNT`],[`storageConfigs`=`STORAGECONFIGS`] `--slurm-partitions`=[`id`=`ID`],[`nodeSetIds`=`NODESETIDS`] `--slurm-prolog-scripts`=[`SLURM_PROLOG_SCRIPTS`,…]) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud cluster-director clusters create` facilitates the creation of a cluster resource. 

Use one of the following options to create a cluster: 

  * [Preferred] Use granular flags to define cluster specs. 
  * Use --config flag with cluster specs in JSON format. 
  * Use --quickstart-cluster or --reference-architecture to apply pre-configured templates. 


QUICKSTART CLUSTER AND REFERENCE ARCHITECTURES
     Quickstart cluster and reference architectures allow you to quickly provision clusters with pre-defined configurations for compute, storage, and orchestrator. 

`quickstart` (applied when using `--quickstart-cluster`): 

  * Compute: 2x a3-megagpu-8g nodes (Flex Start, max duration 7 days). 
  * Login Node: 1x n2-standard-16 node. 
  * Storage: 36TB Lustre storage (scratch disk). 



`a3-ultra` (applied when using `--reference-architecture=a3-ultra`): 

  * Compute: 4x reserved nodes (requires specifying `--reserved-instances`). 
  * Login Node: 1x n2-standard-16 node. 
  * Storage: 36TB Lustre storage (scratch disk) and 5.1TB Filestore storage. 



`a4-high-flex-start` (applied when using `--reference-architecture=a4-high-flex-start`): 

  * Compute: 4x a4-highgpu-8g nodes (Flex Start, max duration 7 days). 
  * Login Node: 1x n2-standard-16 node. 
  * Storage: 18TB Lustre storage (scratch disk) and 2TB Filestore storage. 



`a4x-high` (applied when using `--reference-architecture=a4x-high`): 

  * Compute: 18x reserved nodes (requires specifying `--reserved-instances`). 
  * Login Node: 1x n2-standard-16 node. 
  * Storage: 36TB Lustre storage (scratch disk). 



`g4-flex-start` (applied when using `--reference-architecture=g4-flex-start`): 

  * Compute: 4x g4-standard-384 nodes (Flex Start, max duration 7 days). 
  * Login Node: 1x n2-standard-16 node. 
  * Storage: 36TB Lustre storage (scratch disk) and 10.2TB Filestore storage. 



`h4d-highmem-flex-start` (applied when using `--reference-architecture=h4d-highmem-flex-start`): 

  * Compute: 4x h4d-highmem-192 nodes (Flex Start, max duration 7 days). 
  * Login Node: 1x n2-standard-16 node. 
  * Storage: 18TB Lustre storage (scratch disk) and 1TB Filestore storage. 



Please refer to the examples below for more details. 

EXAMPLES
     To create a cluster `my-cluster` in location `us-central1` with granular flags, run the following example: 
    
    
    gcloud cluster-director clusters create my-cluster --location=us-central1 --description="My cluster description" --labels=env=prod,client=gcloud-cli --create-network=name=network0 --create-filestores=name=locations/us-central1-a/instances/filestore0,tier=ZONAL,capacityGb={filestoreSize},fileshare={fileshare} --filestores=locations/us-central1-a/instances/filestore1 --create-buckets=name=bucket0 --buckets=bucket1 --create-lustres=name=locations/us-central1-a/instances/lustre0,capacityGb={lustreSize},filesystem={filesystem} --lustres=locations/us-central1-a/instances/lustre1 --reserved-instances=id=compute0,reservation=zones/us-central1-a/reservations/{reservation} --slurm-login-node=machineType={machineType},zone=us-central1-a --slurm-node-sets=id=nodeset0,computeId=compute0 --slurm-partitions=id=partition0,nodesetIds=[nodeset0] --slurm-default-partition=partition0 --format=json

To create a cluster `my-cluster` in location `us-central1` with config in JSON string format run the following example: 
    
    
    gcloud cluster-director clusters create my-cluster --location=us-central1 --config='{"key": "value"}'

Or create a JSON file `my-cluster-config.json` with the cluster specs and run the following file example: 
    
    
    gcloud cluster-director clusters create my-cluster --location=us-central1 --config=my-cluster-config.json

To create a cluster `my-cluster` in location `us-central1` using the quickstart setup with default cluster parameters, run the following example: 
    
    
    gcloud cluster-director clusters create my-cluster --location=us-central1 --quickstart-cluster --create-network=name=network0

To create a cluster `my-cluster` in location `us-central1` using a pre-defined reference architecture choice (such as `g4-flex-start`), run the following example: 
    
    
    gcloud cluster-director clusters create my-cluster --location=us-central1 --reference-architecture=g4-flex-start --create-network=name=network0

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
    

Cluster configuration for provisioning. 

Exactly one of these must be specified: 

`--config`=[`computeResources`=`COMPUTERESOURCES`],[`description`=`DESCRIPTION`],[`labels`=`LABELS`],[`name`=`NAME`],[`networkResources`=`NETWORKRESOURCES`],[`orchestrator`=`ORCHESTRATOR`],[`storageResources`=`STORAGERESOURCES`]
     Configuration of the cluster specs in the form of a JSON object. See example below: 
    
    
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
    
    
    --config=computeResources={string={config={newDwsFlexInstances={machineType=string,maxDuration=string,zone=string},newFlexStartInstances={machineType=string,maxDuration=string,zone=string},newOnDemandInstances={machineType=string,zone=string},newReservedInstances={reservation=string},newSpotInstances={machineType=string,terminationAction=string,zone=string}}}},description=string,labels={string=string},name=string,networkResources={string={config={existingComputeNetwork={network=string,subnetwork=string},existingNetwork={network=string,subnetwork=string},newComputeNetwork={description=string,network=string},newNetwork={description=string,network=string}}}},orchestrator={slurm={defaultPartition=string,epilogBashScripts,loginNodes={bootDisk={sizeGb=int,type=string},count=int,enableOsLogin=boolean,enablePublicIps=boolean,labels={string=string},machineType=string,startupScript=string,storageConfigs=[{id=string,localMount=string}],zone=string},nodeSets=[{computeId=string,computeInstance={bootDisk={sizeGb=int,type=string},labels={string=string},startupScript=string},id=string,maxDynamicNodeCount=int,staticNodeCount=int,storageConfigs=[{id=string,localMount=string}]}],partitions=[{id=string,nodeSetIds=[string]}],prologBashScripts}},storageResources={string={config={existingBucket={bucket=string},existingFilestore={filestore=string},existingLustre={lustre=string},newBucket={autoclass={enabled=boolean},bucket=string,hierarchicalNamespace={enabled=boolean},storageClass=string},newFilestore={description=string,fileShares=[{capacityGb=int,fileShare=string}],filestore=string,id=string,protocol=string,tier=string},newLustre={capacityGb=int,description=string,filesystem=string,id=string,lustre=string,perUnitStorageThroughput=int}}}}

`JSON Example:`
    
    
    --config='{"computeResources": {"string": {"config": {"newDwsFlexInstances": {"machineType": "string", "maxDuration": "string", "zone": "string"}, "newFlexStartInstances": {"machineType": "string", "maxDuration": "string", "zone": "string"}, "newOnDemandInstances": {"machineType": "string", "zone": "string"}, "newReservedInstances": {"reservation": "string"}, "newSpotInstances": {"machineType": "string", "terminationAction": "string", "zone": "string"}}}}, "description": "string", "labels": {"string": "string"}, "name": "string", "networkResources": {"string": {"config": {"existingComputeNetwork": {"network": "string", "subnetwork": "string"}, "existingNetwork": {"network": "string", "subnetwork": "string"}, "newComputeNetwork": {"description": "string", "network": "string"}, "newNetwork": {"description": "string", "network": "string"}}}}, "orchestrator": {"slurm": {"defaultPartition": "string", "epilogBashScripts", "loginNodes": {"bootDisk": {"sizeGb": int, "type": "string"}, "count": int, "enableOsLogin": boolean, "enablePublicIps": boolean, "labels": {"string": "string"}, "machineType": "string", "startupScript": "string", "storageConfigs": [{"id": "string", "localMount": "string"}], "zone": "string"}, "nodeSets": [{"computeId": "string", "computeInstance": {"bootDisk": {"sizeGb": int, "type": "string"}, "labels": {"string": "string"}, "startupScript": "string"}, "id": "string", "maxDynamicNodeCount": int, "staticNodeCount": int, "storageConfigs": [{"id": "string", "localMount": "string"}]}], "partitions": [{"id": "string", "nodeSetIds": ["string"]}], "prologBashScripts"}}, "storageResources": {"string": {"config": {"existingBucket": {"bucket": "string"}, "existingFilestore": {"filestore": "string"}, "existingLustre": {"lustre": "string"}, "newBucket": {"autoclass": {"enabled": boolean}, "bucket": "string", "hierarchicalNamespace": {"enabled": boolean}, "storageClass": "string"}, "newFilestore": {"description": "string", "fileShares": [{"capacityGb": int, "fileShare": "string"}], "filestore": "string", "id": "string", "protocol": "string", "tier": "string"}, "newLustre": {"capacityGb": int, "description": "string", "filesystem": "string", "id": "string", "lustre": "string", "perUnitStorageThroughput": int}}}}}'

`File Example:`
    
    
    --config=path_to_file.(yaml|json)

Or at least one of these can be specified: 

Flag Configurations to define cluster spec. 
`--buckets`=[`id`=`ID`],[`name`=`NAME`]
     Reference of existing Google Cloud Storage bucket. 

id: ID of the bucket resource, used to refer to this resource in storage-configs. name: Name of the existing Cloud Storage bucket to import from your project in the format of bucket-name. 

For example --buckets id=my-bucket,name=bucket-1. 

Sets `buckets` value. 

`id`
     Required, sets `id` value. 
`name`
     Required, sets `name` value. 
`Shorthand Example:`
    
    
    --buckets=id=string,name=string --buckets=id=string,name=string

`JSON Example:`
    
    
    --buckets='[{"id": "string", "name": "string"}]'

`File Example:`
    
    
    --buckets=path_to_file.(yaml|json)

`--create-buckets`=[`enableAutoclass`=`ENABLEAUTOCLASS`],[`enableHNS`=`ENABLEHNS`],[`id`=`ID`],[`name`=`NAME`],[`storageClass`=`STORAGECLASS`]
     Parameters to create a Google Cloud Storage bucket. 

Required fields: 

  * id 
  * name 



For example --create-buckets id=my-bucket,name=bucket-1,storageClass=STANDARD,enableHNS=true 

Supported storageClass values: 

  * STANDARD 
  * NEARLINE 
  * COLDLINE 
  * ARCHIVE 



Defaults: 

  * storageClass: STANDARD 



Note: 

  * Either storageClass or enableAutoclass can be set. 
  * HNS: Hierarchical namespace. Hierarchical namespace buckets cannot use Autoclass. 



Sets `create_buckets` value. `Shorthand Example:`
    
    
    --create-buckets=enableAutoclass=boolean,enableHNS=boolean,id=string,name=string,storageClass=string --create-buckets=enableAutoclass=boolean,enableHNS=boolean,id=string,name=string,storageClass=string

`JSON Example:`
    
    
    --create-buckets='[{"enableAutoclass": boolean, "enableHNS": boolean, "id": "string", "name": "string", "storageClass": "string"}]'

`File Example:`
    
    
    --create-buckets=path_to_file.(yaml|json)

`--create-filestores`=[`capacityGb`=`CAPACITYGB`],[`description`=`DESCRIPTION`],[`fileshare`=`FILESHARE`],[`id`=`ID`],[`name`=`NAME`],[`protocol`=`PROTOCOL`],[`tier`=`TIER`]
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



Sets `create_filestores` value. `Shorthand Example:`
    
    
    --create-filestores=capacityGb=int,description=string,fileshare=string,id=string,name=string,protocol=string,tier=string --create-filestores=capacityGb=int,description=string,fileshare=string,id=string,name=string,protocol=string,tier=string

`JSON Example:`
    
    
    --create-filestores='[{"capacityGb": int, "description": "string", "fileshare": "string", "id": "string", "name": "string", "protocol": "string", "tier": "string"}]'

`File Example:`
    
    
    --create-filestores=path_to_file.(yaml|json)

`--create-lustres`=[`capacityGb`=`CAPACITYGB`],[`description`=`DESCRIPTION`],[`filesystem`=`FILESYSTEM`],[`id`=`ID`],[`name`=`NAME`],[`perUnitStorageThroughput`=`PERUNITSTORAGETHROUGHPUT`]
     Parameters to create a Lustre instance. 

Required fields: 

  * id 
  * name 
  * capacityGb 
  * filesystem. 



id: ID of the lustre resource, used to refer to this resource in storage-configs. 

name: Name of the Managed Lustre instance to create in your project in the format of locations/us-central1/instances/lustre-1. 

For example --create-lustres id=my-lustre,name=locations/us-central1/instances/lustre-1,capacityGb=1024,filesystem=fs-1,perUnitStorageThroughput=1000 

Values for perUnitStorageThroughput: 125, 250, 500, 1000. 

Sets `create_lustres` value. `Shorthand Example:`
    
    
    --create-lustres=capacityGb=int,description=string,filesystem=string,id=string,name=string,perUnitStorageThroughput=int --create-lustres=capacityGb=int,description=string,filesystem=string,id=string,name=string,perUnitStorageThroughput=int

`JSON Example:`
    
    
    --create-lustres='[{"capacityGb": int, "description": "string", "filesystem": "string", "id": "string", "name": "string", "perUnitStorageThroughput": int}]'

`File Example:`
    
    
    --create-lustres=path_to_file.(yaml|json)

`--description`=`DESCRIPTION`
     Description of the cluster. 

For example --description "My cluster" 

`--filestores`=[`id`=`ID`],[`name`=`NAME`]
     Reference of existing filestore instance. 

id: ID of the filestore resource, used to refer to this resource in storage-configs. name: Name of the existing filestore instance to import from your project in the format of locations/us-central1/instances/filestore-1. 

For example --filestores id=my-fs,name=locations/us-central1/instances/filestore-1. 

Sets `filestores` value. 

`id`
     Required, sets `id` value. 
`name`
     Required, sets `name` value. 
`Shorthand Example:`
    
    
    --filestores=id=string,name=string --filestores=id=string,name=string

`JSON Example:`
    
    
    --filestores='[{"id": "string", "name": "string"}]'

`File Example:`
    
    
    --filestores=path_to_file.(yaml|json)

`--flex-start-instances`=[`id`=`ID`],[`machineType`=`MACHINETYPE`],[`maxDuration`=`MAXDURATION`],[`zone`=`ZONE`]
     Parameters to define cluster Flex Start instances. 

For example --flex-start-instances id=c1,zone=us-central1-a,machineType=n1-standard-1,maxDuration=10000s. 

Sets `flex_start_instances` value. 

`id`
     Required, sets `id` value. 
`machineType`
     Required, sets `machineType` value. 
`maxDuration`
     Required, sets `maxDuration` value. 
`zone`
     Required, sets `zone` value. 
`Shorthand Example:`
    
    
    --flex-start-instances=id=string,machineType=string,maxDuration=string,zone=string --flex-start-instances=id=string,machineType=string,maxDuration=string,zone=string

`JSON Example:`
    
    
    --flex-start-instances='[{"id": "string", "machineType": "string", "maxDuration": "string", "zone": "string"}]'

`File Example:`
    
    
    --flex-start-instances=path_to_file.(yaml|json)

`--labels`=[`LABELS`,…]
     Cluster labels as key value pairs. 

For example --labels key1=value1,key2=value2. 

Sets `labels` value. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --labels={string=string}

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

`--lustres`=[`id`=`ID`],[`name`=`NAME`]
     Reference of existing Lustre instance. 

id: ID of the lustre resource, used to refer to this resource in storage-configs. name: Name of the existing Managed Lustre instance to import from your project in the format of locations/us-central1/instances/lustre-1. 

For example --lustres id=my-lustre,name=locations/us-central1/instances/lustre-1. 

Sets `lustres` value. 

`id`
     Required, sets `id` value. 
`name`
     Required, sets `name` value. 
`Shorthand Example:`
    
    
    --lustres=id=string,name=string --lustres=id=string,name=string

`JSON Example:`
    
    
    --lustres='[{"id": "string", "name": "string"}]'

`File Example:`
    
    
    --lustres=path_to_file.(yaml|json)

`--on-demand-instances`=[`id`=`ID`],[`machineType`=`MACHINETYPE`],[`zone`=`ZONE`]
     Parameters to define cluster on demand instances. 

For example --on-demand-instances id=c1,zone=us-central1-a,machineType=n1-standard-1. 

Sets `on_demand_instances` value. 

`id`
     Required, sets `id` value. 
`machineType`
     Required, sets `machineType` value. 
`zone`
     Required, sets `zone` value. 
`Shorthand Example:`
    
    
    --on-demand-instances=id=string,machineType=string,zone=string --on-demand-instances=id=string,machineType=string,zone=string

`JSON Example:`
    
    
    --on-demand-instances='[{"id": "string", "machineType": "string", "zone": "string"}]'

`File Example:`
    
    
    --on-demand-instances=path_to_file.(yaml|json)

`--reserved-instances`=[`id`=`ID`],[`reservation`=`RESERVATION`]
     Parameters to define cluster reserved instances. 

For example --reserved-instances id=c1,reservation=zones/us-central1-a/reservations/reservation-1. 

Sets `reserved_instances` value. 

`id`
     Required, sets `id` value. 
`reservation`
     Sets `reservation` value. 
`Shorthand Example:`
    
    
    --reserved-instances=id=string,reservation=string --reserved-instances=id=string,reservation=string

`JSON Example:`
    
    
    --reserved-instances='[{"id": "string", "reservation": "string"}]'

`File Example:`
    
    
    --reserved-instances=path_to_file.(yaml|json)

`--spot-instances`=[`id`=`ID`],[`machineType`=`MACHINETYPE`],[`terminationAction`=`TERMINATIONACTION`],[`zone`=`ZONE`]
     Parameters to define cluster spot instances. 

For example --spot-instances id=c1,zone=us-central1-a,machineType=n1-standard-1. 

Sets `spot_instances` value. 

`id`
     Required, sets `id` value. 
`machineType`
     Required, sets `machineType` value. 
`terminationAction`
     Sets `terminationAction` value. 
`zone`
     Required, sets `zone` value. 
`Shorthand Example:`
    
    
    --spot-instances=id=string,machineType=string,terminationAction=string,zone=string --spot-instances=id=string,machineType=string,terminationAction=string,zone=string

`JSON Example:`
    
    
    --spot-instances='[{"id": "string", "machineType": "string", "terminationAction": "string", "zone": "string"}]'

`File Example:`
    
    
    --spot-instances=path_to_file.(yaml|json)

Network configuration for the cluster. 

At most one of these can be specified: 

`--create-network`=[`description`=`DESCRIPTION`],[`name`=`NAME`]
     Parameters to create a VPC (Virtual Private Cloud) network. 

Required fields: 

  * name Name: Must match the regex `[a-z]([-a-z0-9]*[a-z0-9])?`, be 1-63 characters in length, and comply with RFC1035. 



Description: A description of the network. Maximum of 2048 characters. 

For example --create-network name=network-1,description="My network". 

Sets `create_network` value. `Shorthand Example:`
    
    
    --create-network=description=string,name=string

`JSON Example:`
    
    
    --create-network='{"description": "string", "name": "string"}'

`File Example:`
    
    
    --create-network=path_to_file.(yaml|json)

Or at least one of these can be specified: 

Use an existing network source for the cluster. 
`--network`=`NETWORK`
     Reference of existing network name. If the network is in a different project (Shared VPC), specify the project ID using --network-project. 

For example --network network-1 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--subnet`=`SUBNET`
     Reference of existing subnetwork name. If the subnetwork is in a different project (Shared VPC), specify the project ID using --network-project. 

For example --subnet regions/us-central1/subnetworks/subnet-1 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--network-project`=`NETWORK_PROJECT`
     Project ID of the project containing the network and subnetwork resources, if different from the cluster project (e.g. for Shared VPC). 
At most one of these can be specified: 

`--quickstart-cluster`
     If specified, creates a cluster with sensible defaults: 

  * Compute: 2x a3-megagpu-8g nodes (Flex Start, max duration 7 days). 
  * Login: 1x n2-standard-16 node. 
  * Storage: 36TB Lustre storage (scratch disk). 


`--reference-architecture`=`REFERENCE_ARCHITECTURE`
     Reference a pre-defined architecture. Available options: 

  * a3-ultra: 4x reserved nodes (requires --reserved-instances), 1x login node (n2-standard-16), 36TB Lustre storage, and 5.1TB Filestore storage. 
  * a4-high-flex-start: 4x a4-highgpu-8g compute nodes (Flex Start), 1x login node (n2-standard-16), 18TB Lustre storage, and 2TB Filestore storage. 
  * a4x-high: 18x reserved nodes (requires --reserved-instances), 1x login node (n2-standard-16), and 36TB Lustre storage. 
  * g4-flex-start: 4x g4-standard-384 compute nodes (Flex Start), 1x login node (n2-standard-16), 36TB Lustre storage, and 10.2TB Filestore storage. 
  * h4d-highmem-flex-start: 4x h4d-highmem-192 compute nodes (Flex Start), 1x login node (n2-standard-16), 18TB Lustre storage, and 1TB Filestore storage. `REFERENCE_ARCHITECTURE` must be one of: `a3-ultra`, `a4-high-flex-start`, `a4x-high`, `g4-flex-start`, `h4d-highmem-flex-start`. 


Orchestrator configuration for the cluster. 
Slurm orchestrator configuration for the cluster. 
`--slurm-default-partition`=`SLURM_DEFAULT_PARTITION`
     Parameters to define slurm cluster default partition. 

For example --slurm-default-partition p1 

`--slurm-epilog-scripts`=[`SLURM_EPILOG_SCRIPTS`,…]
     Slurm epilog bash scripts. 

For example --slurm-epilog-scripts script1.sh,script2.sh 

`--slurm-login-node`=[`bootDisk`=`BOOTDISK`],[`count`=`COUNT`],[`enableOsLogin`=`ENABLEOSLOGIN`],[`enablePublicIps`=`ENABLEPUBLICIPS`],[`labels`=`LABELS`],[`machineType`=`MACHINETYPE`],[`startupScript`=`STARTUPSCRIPT`],[`storageConfigs`=`STORAGECONFIGS`],[`zone`=`ZONE`]
     Parameters to define slurm cluster login node. 

Required: 

  * machineType 
  * zone 



For example --slurm-login-node machineType=n1-standard-1,zone=us-central1-a,count=1 

Defaults: 

  * count: 1 
  * enableOsLogin: true 
  * enablePublicIPs: true 
  * bootDisk.sizeGb: 100 



Note: 

  * startupScript: 
    * Either str or file_path 
    * For file_path, only bash file format (.sh or .bash) is supported. 
    * For file_path, only absolute path is supported. 
  * bootDisk: 
    * Must be 50 GB or greater. 

Sets `slurm_login_node` value. 


`Shorthand Example:`
    
    
    --slurm-login-node=bootDisk={sizeGb=int,type=string},count=int,enableOsLogin=boolean,enablePublicIps=boolean,labels={string=string},machineType=string,startupScript=string,storageConfigs=[{id=string,localMount=string}],zone=string

`JSON Example:`
    
    
    --slurm-login-node='{"bootDisk": {"sizeGb": int, "type": "string"}, "count": int, "enableOsLogin": boolean, "enablePublicIps": boolean, "labels": {"string": "string"}, "machineType": "string", "startupScript": "string", "storageConfigs": [{"id": "string", "localMount": "string"}], "zone": "string"}'

`File Example:`
    
    
    --slurm-login-node=path_to_file.(yaml|json)

`--slurm-node-sets`=[`computeId`=`COMPUTEID`],[`computeInstance`=`COMPUTEINSTANCE`],[`id`=`ID`],[`maxDynamicNodeCount`=`MAXDYNAMICNODECOUNT`],[`staticNodeCount`=`STATICNODECOUNT`],[`storageConfigs`=`STORAGECONFIGS`]
     Parameters to define slurm cluster nodeset config. 

Required fields: 

  * id 



For example --slurm-node-sets id=ns1,computeId=c1,staticNodeCount=1,maxDynamicNodeCount=2,computeInstance=[startupScript="echo hello",labels="k1=v1"] 

Defaults: 

Note: 

  * startupScript: 
    * Either str or file_path 
    * For file_path, only bash file format (.sh or .bash) is supported. 
    * For file_path, only absolute path is supported. 

Sets `slurm_node_sets` value. 


`Shorthand Example:`
    
    
    --slurm-node-sets=computeId=string,computeInstance={bootDisk={sizeGb=int,type=string},labels={string=string},startupScript=string},id=string,maxDynamicNodeCount=int,staticNodeCount=int,storageConfigs=[{id=string,localMount=string}] --slurm-node-sets=computeId=string,computeInstance={bootDisk={sizeGb=int,type=string},labels={string=string},startupScript=string},id=string,maxDynamicNodeCount=int,staticNodeCount=int,storageConfigs=[{id=string,localMount=string}]

`JSON Example:`
    
    
    --slurm-node-sets='[{"computeId": "string", "computeInstance": {"bootDisk": {"sizeGb": int, "type": "string"}, "labels": {"string": "string"}, "startupScript": "string"}, "id": "string", "maxDynamicNodeCount": int, "staticNodeCount": int, "storageConfigs": [{"id": "string", "localMount": "string"}]}]'

`File Example:`
    
    
    --slurm-node-sets=path_to_file.(yaml|json)

`--slurm-partitions`=[`id`=`ID`],[`nodeSetIds`=`NODESETIDS`]
     Parameters to define slurm cluster partitions. 

For example --slurm-partitions id=p1,nodesetIds=[ns1,ns2]. 

Sets `slurm_partitions` value. 

`id`
     Required, sets `id` value. 
`nodeSetIds`
     Required, sets `nodeSetIds` value. 
`Shorthand Example:`
    
    
    --slurm-partitions=id=string,nodeSetIds=[string] --slurm-partitions=id=string,nodeSetIds=[string]

`JSON Example:`
    
    
    --slurm-partitions='[{"id": "string", "nodeSetIds": ["string"]}]'

`File Example:`
    
    
    --slurm-partitions=path_to_file.(yaml|json)

`--slurm-prolog-scripts`=[`SLURM_PROLOG_SCRIPTS`,…]
     Slurm prolog bash scripts. 

For example --slurm-prolog-scripts script1.sh,script2.sh 

OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha cluster-director clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/cluster-director/clusters/create)
    
    
    [gcloud beta cluster-director clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/cluster-director/clusters/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
