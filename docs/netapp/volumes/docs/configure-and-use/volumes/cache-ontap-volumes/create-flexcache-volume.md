---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/create-flexcache-volume/
title: Create a FlexCache volume \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:30.441555+00:00
---

# Create a FlexCache volume  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/create-flexcache-volume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Create a FlexCache volume Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a [FlexCache volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview#about_flexcache).

## Considerations

  * You can use ONTAP-mode volumes as a FlexCache origin or cache, and all other volumes only as cache volumes.

  * FlexCache is supported for the Flex Unified, Premium, and Extreme service levels.

  * FlexCache volumes are supported in large capacity pools.

  * Cache volumes don't support NFSv4.2.

  * The origin volume can be a [FlexVol or FlexGroup](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/flexgroups-and-large-volumes) on ONTAP clusters.

  * Access time updates must be disabled on the origin volume.

  * Choose the same volume security style for the cache volume as the origin volume. The security style of the cache volume is [determined by the protocol type you choose](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations#volume_security_style) for the cache.




Before you create a FlexCache volume on NetApp Volumes, make sure that [access time updates are disabled on your origin volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview#cache_invalidation_due_to_access_time_updates).

## Prerequisites for FlexCache

FlexCache uses the same communication channel as SnapMirror and shares the same prerequisites as volume migration. For more information, see [Prerequisites for ONTAP to NetApp Volumes communication](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/prerequisites-ontap-netapp-volumes).

The following are the key prerequisites:

  * Source ONTAP system and administrator credentials

  * Network connection to the Google Cloud project

  * IP address allocation

  * NetApp Volumes settings




If you have already established a network connection and cluster peering for [volume migration](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/overview#about_volume_migration) or [external replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/overview#about_external_replication), FlexCache can reuse these existing configurations.

To use ONTAP-mode volumes as an origin, peer your destination cluster with ONTAP-mode as described in [Peer clusters and SVMs](https://docs.cloud.google.com/netapp/volumes/docs/ontap/peer-clusters-svms), and refer to the ONTAP documentation to create a FlexCache volume on the cluster.

## Create a FlexCache volume

Creating a FlexCache volume includes a two-step process. The first step is performed on NetApp Volumes and the second on the source ONTAP system. Both steps must be completed for the FlexCache volume to function correctly.

Use the following instructions to create a FlexCache volume using the Google Cloud CLI or ONTAP-mode.

### gcloud

  1. Create a FlexCache volume:
         
         gcloud beta netapp volumes create VOLUME_NAME --location=LOCATION \
          --capacity=CAPACITY --protocols=PROTOCOL \
          --share-name=SHARE_NAME --storage-pool=STORAGE_POOL \
          --snapshot-directory=FALSE --multiple-endpoints=TRUE \
          --cache-parameters=peer-volume-name=PEER_VOLUME_NAME,peer-svm-name=PEER_SVM_NAME,peer-cluster-name=PEER_CLUSTER_NAME,peer-ip-addresses=PEER_IP_ADDRESS1#PEER_IP_ADDRESS2#...,enable-global-file-lock=ENABLE_GLOBAL_FILE_LOCK,cache-config=cifs-change-notify-enabled=ENABLE_CIFS_CHANGE_NOTIFY#write-back-enabled=ENABLE_WRITE_BACK

The `cache-parameters` block designates the new volume as a cache volume.

Replace the following information:

     * `VOLUME_NAME`: the name of the volume. This name must be unique per location.

     * `LOCATION`: the location for the volume.

     * `CAPACITY`: the capacity of the volume. It defines the capacity that NAS clients see.

     * `PROTOCOLS`: the NAS protocols the volume is exported with.

     * `SHARE_NAME`: the NFS export path or SMB share name of the volume.

     * `STORAGE_POOL`: the storage pool to create the volume in.

     * `PEER_CLUSTER_NAME`: the name of the ONTAP cluster hosting the source volumes.

     * `PEER_IP_ADDRESSES`: the InterCluster-LIF IP addresses of the ONTAP cluster. The source cluster must provide one IC-LIF per node, separated by # signs. Make sure to specify them all.

The following example shows you how to add multiple IC-LIF IP addresses of the ONTAP cluster:
           
           peer-ip-addresses=10.0.0.25#10.0.0.26
           

     * `PEER_SVM_NAME`: the name of the storage virtual machine (SVM), also known as vserver that owns the source volume.

     * `PEER_VOLUME_NAME`: the name of the source volume.

     * `ENABLE_GLOBAL_FILE_LOCK`: Optional: a boolean flag indicating whether global file locking is enabled on the cache volume. The default is `false`.

     * `cache-config`: Optional: use the `cache-config` parameter block to specify additional parameters. Individual parameters must be separated by # signs.

       * `ENABLE_CIFS_CHANGE_NOTIFY`: Optional: a boolean flag indicating whether a CIFS change notification is enabled for the cache volume. The default is `false`.

       * `ENABLE_WRITE_BACK`: Optional: a boolean flag indicating whether to enable `write-back` mode. The default is `false`, which corresponds to using `write-around` mode.

Example invocation:
    
    $ gcloud beta --project my-project netapp volumes create my-volume \
    --location australia-southeast1 --capacity 100 \
    --protocols=nfsv3 --share-name origin1 --storage-pool my-pool \
    --snapshot-directory=false --multiple-endpoints=true \
    --export-policy=access-type=READ_WRITE,allowed-clients=0.0.0.0/0,has-root-access=true,nfsv3=true \
    --cache-parameters=peer-volume-name=origin1,peer-svm-name=my-svm,peer-cluster-name=my-cluster,peer-ip-addresses=10.152.0.5,enable-global-file-lock=false,cache-config=cifs-change-notify-enabled=false
    

To meet your volume requirements, specify all applicable optional parameters. For example, an NFS volume might require an export policy.

Look up all options:
    
    gcloud netapp volumes create --help
    

  2. Peer with the origin ONTAP system.

After creating the cache volume, NetApp Volumes tries to establish peering with your origin ONTAP system. This peering process serves as an authentication and authorization step, and protects your origin cluster from malicious cache creation requests. Therefore, make sure you only peer with trusted systems.

**Note:** You must execute the cluster and SVM peering commands on the ONTAP systems.

To look up the detailed commands and steps for the peering process:
         
         gcloud beta netapp volumes describe VOLUME_NAME --location=LOCATION
         

The `cacheParameters` block contains sub-parameters which show the status of the peering process. The `cacheState` parameter's output indicates the current step in the multi-step peering process.

     * If `cacheState` is `PENDING_CLUSTER_PEERING`:

       * Look up the `command` parameter and run the command listed on the ONTAP origin cluster.

       * ONTAP requests a passphrase, which can be found under the `passphrase` parameter.

       * The command format to run on the ONTAP side:
             
             cluster peer create ...
             

     * If `cacheState` is `PENDING_SVM_PEERING`:

       * Look up the `command` parameter and run the command listed on the ONTAP origin cluster.

       * ONTAP requests a passphrase, which can be found under the `passphrase` parameter.

       * The command format to run on the ONTAP side:
             
             vserver peer create ...
             

     * If `cacheState` is `PEERED`:

       * The FlexCache volume is successfully created and functional. You can now connect clients.

       * A FlexCache volume is always a volume with [multiple endpoints](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-large-capacity-volumes).

After running any of the commands indicated by the `cacheState` and `command` parameters, wait one minute, and then run the `describe` command again to get new instructions. Repeat this process until `cacheState` displays as `PEERED`.

**Important:** Your volume isn't ready for use until `cacheState` is `PEERED`.



### ONTAP-mode

To create a FlexCache volume, complete the following steps:

  1. Create a cluster and SVM peering between your ONTAP-mode pool and your peer cluster as described in [Peer clusters and SVMs](https://docs.cloud.google.com/netapp/volumes/docs/ontap/peer-clusters-svms).

  2. Run the [volume flexcache create](https://docs.netapp.com/us-en/ontap/flexcache/create-volume-task.html) command to create the FlexCache volume on the destination side.




## What's next

[Manage FlexCache volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/manage-flexcache-volume).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
