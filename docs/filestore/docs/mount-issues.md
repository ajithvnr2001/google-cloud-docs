---
url: https://docs.cloud.google.com/filestore/docs/mount-issues/
title: Troubleshoot mounting issues \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:24.041791+00:00
---

# Troubleshoot mounting issues  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/mount-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Troubleshoot mounting issues Stay organized with collections  Save and categorize content based on your preferences. 

This page provides troubleshooting information to help address issues you might encounter while attempting to mount or unmount a share on a Filestore instance.

## My VM or GKE pod can't access Filestore

Confirm whether the Filestore instance is reachable (`ping` and `traceroute` are not supported) by running:
    
    
    sudo showmount -e <filestore-ip>
    

The command should respond with a list of exported file systems. Then check whether the client can reach Filestore's RPC information by running:
    
    
    sudo rpcinfo -p <filestore-ip>
    

If the Filestore instance is not reachable, common causes include improperly configured network settings or ACL settings, or you are attempting to mount the wrong instance.

  1. Check whether IP-based access control is enabled and check whether the IP address of the client is restricted. For more information, see Permission denied when trying to mount a file share.
  2. Check your firewall settings to make sure that the required ports are open. For details, see [Configuring firewall rules](https://docs.cloud.google.com/filestore/docs/configuring-firewall).
  3. If you're trying to access Filestore from a GKE cluster, and are getting the error `mount.nfs: access denied by server while mounting ...`, see [Unable to access file share from GKE clusters](https://docs.cloud.google.com/filestore/docs/gke-access-issues).



## Permission denied when trying to mount a file share

Confirm whether there are any [NFS Export Options](https://docs.cloud.google.com/filestore/docs/access-control#ip-based_access_control) listed for the instance:
    
    
    gcloud filestore instances describe instance-id \
        --zone=zone
    

where:

  * instance-id is the instance ID of the Filestore.
  * zone is the zone where the Filestore instance resides.



The command returns something similar to:
    
    
    createTime: '2019-10-11T17:28:23.340943077Z'
    fileShares:
    - capacityGb: '1024'
      name: vol1
      nfsExportOptions:
      - accessMode: READ_WRITE
        ipRanges:
        - 128.0.0.0/29
        squashMode: NO_ROOT_SQUASH
    name: projects/yourproject/locations/us-central1-c/instances/nfs-server
    networks:
    - ipAddresses:
      - 10.0.0.2
      modes:
      - MODE_IPV4
      network: default
      reservedIpRange: 10.0.0.0/29
    state: READY
    tier: BASIC_HDD

If you find `nfsExportOptions` listed, check if the IP address of your client is within one of the ranges listed under `ipRanges` for the expected `accessMode`. If it isn't, you must [edit the NFS Export Options](https://docs.cloud.google.com/filestore/docs/editing-instances).

## Unable to mount a file share to App Engine

Filestore does not support App Engine.

## Unable to mount a file share from a GKE cluster

You cannot directly mount Filestore file shares to GKE clusters. Instead, you must [configure a PV and a PVC](https://docs.cloud.google.com/filestore/docs/csi-driver).

## Can't connect to mounted file shares when using HA VPN or Cloud Interconnect

If you use HA VPN or Cloud Interconnect and mount the file share to a client VM that's running Linux kernel version 5, set the [`nconnect` mount option](https://man7.org/linux/man-pages/man5/nfs.5.html) to `1`. This setting prevents multiple connections to different Filestore backend nodes and ensures connection to mounted file shares.
    
    
       mount -o nconnect=1
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
