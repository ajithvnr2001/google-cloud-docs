---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/manage-flexcache-volume/
title: Manage FlexCache volumes \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:13:13.845855+00:00
---

# Manage FlexCache volumes  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/manage-flexcache-volume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage FlexCache volumes Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage your [FlexCache volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview#about_flexcache).

## View FlexCache volume details

A FlexCache volume functions like a normal volume but includes a `cacheParameters` block that provides specific cache information.

Use the following instructions to view details of a FlexCache volume using the Google Cloud CLI or ONTAP-mode.

### gcloud

To view details of a FlexCache volume:
    
    
    gcloud beta netapp volumes describe VOLUME_NAME --location=LOCATION
    

Example output:
    
    
    ...
    cacheParameters:
     cacheState: PEERED
     enableGlobalFileLock: false
     peerClusterName: my-cluster
     peerSvmName: my-svm
     peerVolumeName: origin1
     cachePrePopulateState: done
    ...
    

### ONTAP-mode

Run the [volume flexcache show](https://docs.netapp.com/us-en/ontap-cli/volume-flexcache-show.html) command to view details about your FlexCache volume:

  * If the cache is hosted on an ONTAP-mode pool in NetApp Volumes, run the command using [ontap_execute](https://docs.cloud.google.com/netapp/volumes/docs/ontap/common-ontap-mode-procedures#set_up_ontap_execute).

  * If the cache is hosted on an external ONTAP cluster and the ONTAP-mode pool is the origin, run the command on the external cluster.




## Edit a FlexCache volume

You can [edit a FlexCache volume like a regular volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-volume#edit_a_volume) in Google Cloud console, but you can't manage FlexCache settings. However, [certain operations might fail](https://docs.cloud.google.com/netapp/volumes/docs/troubleshoot/known-limitations#flexcache-volume-modifications-fail) when using the Google Cloud console. If this occurs, use the Google Cloud CLI instead.

Use the following instructions to edit a FlexCache volume using the Google Cloud CLI or ONTAP-mode.

### gcloud

If the peering isn't established, you can modify the `peer-ip-addresses` using the `establish-peering` command. If you need to change any other peer parameters before peering is complete, you need to delete the volume and recreate it.

A peering which isn't established is indicated by the `cacheState` as `PENDING_CLUSTER_PEERING` or `PENDING_SVM_PEERING`. This occurs due to network issues such as routing or firewall issues, or incorrect `PEER_IP_ADDRESSES`. After one hour, the peering process will time out.

To fix the incorrect `PEER_IP_ADDRESSES` or to restart the peering process:
    
    
    gcloud beta netapp volumes establish-peering VOLUME_NAME --location=LOCATION \
      --peer-cluster-name=PEER_CLUSTER_NAME \
      --peer-svm-name=PEER_SVM_NAME \
      --peer-volume-name=PEER_VOLUME_NAME \
      --peer-ip-addresses=PEER_IP_ADDRESSES

Replace the following information:

  * `PEER_CLUSTER_NAME`: the name of the ONTAP cluster hosting the source volumes.

  * `PEER_IP_ADDRESSES`: the InterCluster-LIF IP addresses of the ONTAP cluster. The source cluster must provide one IC-LIF per node, separated by # signs. Make sure to specify them all.

The following example shows you how to add multiple IC-LIF IP addresses of the ONTAP cluster:
        
        peer-ip-addresses=10.0.0.25#10.0.0.26
        

  * `PEER_SVM_NAME`: the name of the storage virtual machine (SVM), also known as vserver that owns the source volume.

  * `PEER_VOLUME_NAME`: the name of the source volume.




After peering is established which is indicated by `cacheState` as `PEERED`, you can no longer change the peering parameters for that volume. However, you can modify the `cache-config` parameters.

To change the `cache-config` parameters:
    
    
    gcloud beta netapp volumes update VOLUME_NAME --location=LOCATION \
      --capacity=CAPACITY --protocols=PROTOCOL \
      --share-name=SHARE_NAME --storage-pool=STORAGE_POOL \
      --snapshot-directory=FALSE --multiple-endpoints=TRUE \
      --cache-parameters=enable-global-file-lock=ENABLE_GLOBAL_FILE_LOCK,cache-config=cifs-change-notify-enabled=ENABLE_CIFS_CHANGE_NOTIFY#write-back-enabled=ENABLE_WRITE_BACK

Replace the following information:

  * `ENABLE_GLOBAL_FILE_LOCK`: Optional: a boolean flag indicating whether global file locking is enabled on the cache volume. The default is `false`.

  * `cache-config`: Optional: use the `cache-config` parameter block to specify additional parameters. Individual parameters must be separated by # signs.

    * `ENABLE_CIFS_CHANGE_NOTIFY`: Optional: a boolean flag indicating whether a CIFS change notification is enabled for the cache volume. The default is `false`.

    * `ENABLE_WRITE_BACK`: Optional: a boolean flag indicating whether to enable `write-back` mode. The default is `false`, which corresponds to using `write-around` mode.




### ONTAP-mode

For instructions about how to manage FlexCache volumes, see [ONTAP FlexCache documentation](https://docs.netapp.com/us-en/ontap/flexcache/index.html).

## Delete a FlexCache volume

You can delete a FlexCache volume like any other volume. For more information about instructions, see [Delete a volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-volume#delete_a_volume). If you've enabled write-back support for your cache volume, you must disable write-back before you delete the volume. For more information, see Edit a FlexCache volume.

For ONTAP-mode caches, see [Delete ONTAP FlexCache relationships](https://docs.netapp.com/us-en/ontap/flexcache/delete-relationship-task.html).

## What's next

[Prepopulate a FlexCache volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/prepopulate-flexcache-volume).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
