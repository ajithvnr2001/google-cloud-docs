---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/create-external-replication/
title: Create an external replication \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:01.474789+00:00
---

# Create an external replication  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/create-external-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Create an external replication Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create an [external replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/overview#about_external_replication).

## Before you begin

Before setting up an external replication, we recommend that you review the [external replication workflow](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/overview#overview_of_external_replication_workflow). The external replication process starts by creating a destination volume and specifying the source system details. This action creates a destination volume resource and a replication child resource within NetApp Volumes for managing the replication.

## Considerations

  * The following features aren't supported for destination volumes during the external replication process:

    * Volume replication

    * Flex File service level

  * You must use manual backups when doing an integrated backup of NetApp Volumes based destination volumes. If you try to assign a backup policy to a destination volume, it will fail.

  * Select the correct storage pool and make sure that the destination volume is large enough to accommodate the logical size (not the physical size) used by your ONTAP source volume.

  * Specify the correct share name and protocol types. The share name must match the source, and the protocol types must be chosen carefully as they can't be changed after volume creation. The protocol settings you choose also map to [volume security styles](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations#volume_security_style). Make sure these settings are consistent.

  * Before creating an external replication, make sure you have CLI access and the necessary permissions on the source ONTAP system. You need to run CLI commands on the source ONTAP system within one hour of the replication process.

  * You can't migrate a volume with [tamperproof snapshots](https://docs.netapp.com/us-en/ontap/snaplock/snapshot-lock-concept.html) to a volume that uses auto-tiering.

  * When you move data to a Flex Unified pool with auto-tiering enabled, enable hot-tier bypass during the replication. Otherwise, the replication fills the hot tier and causes out-of-space errors or unwanted hot-tier expansion. After the replication is complete, you can disable hot-tier bypass.




## Prerequisites for external replication

External replication and volume migration share the same [prerequisites](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/prerequisites-ontap-netapp-volumes).

## Create an external replication

Use the following instructions to create an external replication using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **External replications** from the **Data protection** menu.

  3. Click **Replicate external volume**.

  4. In the **Prerequisites** section, review the prerequisites and click **Next**.

  5. In the **External source details** section, complete the following steps:

     1. Enter the name of your source cluster in the **Cluster name** field.

     2. Enter the name of the Storage Virtual Machine (SVM), also known as vserver, that hosts the source volume in the **Storage VM name** field.

     3. Enter the name of the source volume in the **Volume name** field.

     4. Enter the Intercluster-LIF (IC-LIF) IP address in the **Inter-cluster IP** field. Each node of the source cluster needs an IC-LIF. Specify all IC-LIFs as a comma-separated list.

     5. Optional: enter a description for the source ONTAP cluster location in the **Location** field.

  6. Optional: in the **Volume style** section, click **FlexGroup volume** checkbox to create a large capacity destination volume in NetApp Volumes.

     1. Enter the number of constituent volumes on the source volume in the **Constituent volume count** field.

     2. Click **Next**.




### Configure destination volume details

  1. In the **Storage pool details** section, complete the following steps:

     1. Click **Select storage pool**.

     2. From the list of storage pools displayed, select the required storage pool.

     3. Click **Select**.

If the storage pools in the list don't have the settings you want, click [Create new storage pool](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/create-storage-pool).

  2. In the **Volume details** section, complete the following steps:

     1. Enter the name of the destination volume in the **Destination volume name** field.

**Caution:** Your selection is permanent.
     2. Optional: enter a description for the volume in the **Description** field.

  3. In the **Protocol configuration** section, select the same protocol as the source volume. For some protocols, various options are displayed. For more information about protocol options, see [Create a new volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume#console).

  4. In the **Share name** section, enter the share name of the volume in the **Share name** field. The share name must be unique within a location. It's recommended to use the destination volume name as the share name.

**Caution:** Your selection is permanent.
  5. In the **Capacity configuration** section, complete the following steps:

     1. Click **Enable large capacity** checkbox.

**Note:** You can only enable large capacity on the destination volume if the source volume is specified as a FlexGroup volume.
     2. Enter the volume capacity in the **Capacity** field.

  6. Optional: if the selected storage pool allows auto-tiering:

     1. Select the **Enable auto-tiering** checkbox if you want to enable auto-tiering for the volume.

     2. Specify a cooling threshold between 2 and 183 days in the **Cooling threshold days** field. The default cooling threshold value is 31 days.

     3. When you replicate to a Flex Unified pool with auto-tiering enabled, select the **Enable hot tier bypass** checkbox. You can disable hot-tier bypass after the replication is complete.

  7. Optional: if you selected any NFS variant in the protocol configuration, you can specify export rules for the volume in the **Export rules** section.

  8. Optional: in the **Snapshot configuration** section, complete the following steps:

     1. Click **Make snapshot directory visible** checkbox to enable file system access to snapshot versions by clients. For more information, see [NetApp Volumes volume snapshots overview](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/overview).

     2. Select **Allow scheduled snapshots** to configure the volume to automatically take snapshots. You can specify the number of snapshots to keep at hourly, daily, weekly, and monthly snapshot intervals. Times are specified in UTC. If you reach the maximum number of snapshots, the oldest snapshot is deleted.

     3. Review your snapshot selections.

  9. Click **Next**.




### Define replication schedule

  1. In the **Replication schedule** section, complete the following steps:

     1. Enter the name of your replication in the **Replication name** field.

**Caution:** Your selection is permanent.
     2. Optional: enter a description for your replication in the **Description** field.

     3. Click the **Replication schedule** drop-down list, and select the following schedule frequency for replicating data from the source volume to the destination volume.

        * **Every 10 mins**

        * **Daily**

        * **Hourly**

The default is **HOURLY**. Large capacity volumes don't support **EVERY_10_MINUTES** option.

     4. Optional: click **Add label** to enter relevant labels for reporting and querying purposes.

  2. Click **Next**.

  3. Review your settings and click **Create** to start the replication process.


**Note:** If you see the error `Unable to find the resource you requested`, wait 30 seconds and click **Retry**.

After creating the replication process, you are redirected to the volume details view. Click the **Replication** tab to monitor the replication status.

You must authenticate the SnapMirror connection between your source ONTAP system and NetApp Volumes. Run the `cluster peer create` command on the source ONTAP cluster. If no prior peering exists, the **Replication** tab displays **Pending cluster peering**.

If you click **Configure peering** , a side page with instructions is displayed. Follow these instructions, and click **Check peering**. After a successful peering, the side page disappears, and the transfer status of the replication changes to **Preparing**. The baseline transfer is now running. A baseline transfer can take minutes, hours, or days depending on the amount of data to be transferred and the network speed. Once the baseline transfer is complete, the transfer status switches to **Mirrored**.

### gcloud

To create an external replication:
    
    
    gcloud netapp volumes create VOLUME_NAME --location=LOCATION \
      --capacity=CAPACITY --protocols=PROTOCOL \
      --share-name=SHARE_NAME --storage-pool=STORAGE_POOL \
      --hybrid-replication-parameters=hybrid-replication-type=ONPREM_REPLICATION,peer-cluster-name=PEER_CLUSTER_NAME,peer-ip-addresses=PEER_IP_ADDRESSES,peer-svm-name=PEER_SVM_NAME,peer-volume-name=PEER_VOLUME_NAME,replication=REPLICATION,replication-schedule=REPLICATION_SCHEDULE,cluster-location=CLUSTER_LOCATION,description=DESCRIPTION,labels=LABELS

When you replicate to a Flex Unified pool with auto-tiering enabled, always enable hot-tier bypass during replication. After the replication is complete, you can disable hot-tier bypass. Use the `gcloud beta netapp volumes create` command to create a volume with auto-tiering enabled.

The following example shows the required parameters to create a volume with auto-tiering enabled:
    
    
    --tiering-policy=tier-action=ENABLED,cooling-threshold-days=DAYS,enable-hot-tier-bypass-mode=on

The `hybrid-replication-parameters` block starts a replication workflow.

Replace the following information:

  * `VOLUME_NAME`: the name of the volume. This name must be unique per location.

  * `LOCATION`: the location for the volume.

  * `CAPACITY`: the capacity of the volume. It defines the capacity that NAS clients see.

  * `PROTOCOLS`: the NAS protocols the volume is exported with.

  * `SHARE_NAME`: the NFS export path or SMB share name of the volume.

  * `STORAGE_POOL`: the storage pool to create the volume in.

  * `HYBRID_REPLICATION_TYPE`: for external replication, specify `ONPREM_REPLICATION`.

  * `PEER_CLUSTER_NAME`: the name of the ONTAP cluster hosting the source volumes.

  * `PEER_IP_ADDRESSES`: the InterCluster-LIF IP addresses of the ONTAP cluster. The source cluster must provide one IC-LIF per node, separated by # signs. Make sure to specify them all.

The following example shows you how to add multiple IC-LIF IP addresses of the ONTAP cluster:
        
        peer-ip-addresses=10.0.0.25#10.0.0.26
        

  * `PEER_SVM_NAME`: the name of the storage virtual machine (SVM), also known as vserver that owns the source volume.

  * `PEER_VOLUME_NAME`: the name of the source volume.

  * `REPLICATION`: the name of the replication resource to be created.

  * `LARGE_VOLUME_CONSTITUENT_COUNT`: this parameter is only required when your source volume is a [FlexGroup](https://docs.netapp.com/us-en/ontap/flexgroup/definition-concept.html). For more information, see [FlexGroups and Large Volumes](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/flexgroups-and-large-volumes) before you proceed.

To create a large volume, `specify --large-volume true` and `--multiple-endpoints true` as create parameters too.

  * `REPLICATION_SCHEDULE`: Optional: you can set the `replication schedule` to one of the following intervals:

    * `EVERY_10_MINUTES`

    * `HOURLY`

    * `DAILY`

The default is `HOURLY`. Large volumes won't offer `EVERY_10_MINUTES`.

  * `CLUSTER_LOCATION`: Optional: the description of the source cluster location.

  * `DESCRIPTION`: Optional: the description text for the replication resource.

  * `LABELS`: Optional: labels for the replication resource.

The following example shows how to specify key-value pairs for the `labels` parameter:
        
        labels=KEY1:VALUE1#KEY2:VALUE2
        




Example invocation:
    
    
    $ gcloud beta netapp volumes create ok-destination --location australia-southeast1 \
    --capacity 100 --protocols=nfsv3 \
    --share-name ok-destination --storage-pool okrause-pool \
    --hybrid-replication-parameters=hybrid-replication-type=ONPREM_REPLICATION,peer-cluster-name=au2se1cvo2sqa,peer-ip-addresses=10.0.0.25#10.0.0.26,peer-svm-name=svm_au2se1cvo2sqa,peer-volume-name=okrause_source,replication=okrause-replication,replication-schedule=HOURLY \
    --tiering-policy=tier-action=ENABLED,cooling-threshold-days=31,enable-hot-tier-bypass-mode=on
    

To meet your volume requirements, specify all applicable optional parameters. For example, an NFS volume might require an export policy.

Look up all options:
    
    
    gcloud netapp volumes create --help
    

After creating the destination volume and the replication resource, NetApp Volumes tries to peer with your source ONTAP system. This peering process serves as an authentication and authorization step, and protects your source cluster from malicious SnapMirror requests. Therefore, make sure you only peer with trusted systems.

Look up the next steps:
    
    
    gcloud netapp volumes replications list --volume=DESTINATION_VOLUME --location=REGION
    

The current authentication status can be printed at any time. However, the state changes might take up to five minutes after an action advances the process to the next step.

A successful peering consists of the following steps:

  * The NetApp Volumes destination volume pings your source system using the specified `peer-ip-addresses`.

  * If cluster peering isn't already established, NetApp Volumes prints the cluster peering commands you must run on the source system. If your source is a Flex Unified ONTAP-mode pool, see [Using Google Cloud CLI ONTAP CLI proxy](https://docs.cloud.google.com/netapp/volumes/docs/ontap/manage-ontap#use-gcloud-ontap-cli-proxy) to run the commands.

  * Also, if SVM peering isn't already established, NetApp Volumes prints the vserver peering commands you must run on the source system.




The steps that have been completed previously are skipped, and the process automatically continues with the next step.

**Network connectivity check**

NetApp Volumes tries to send an ICMP (ping) request to the IC-LIFs you specified under `peer-ip-addresses`. If it fails, `stateDetails` displays `Cluster peering failed, please try again`, indicating a network issue. For more information, see [Network connection to Google Cloud project](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/prerequisites-ontap-netapp-volumes#network-connection). You can't proceed further until you establish a network connectivity between the source system and NetApp Volumes. For debugging purposes, try to ping the gateway IP of the `/27` CIDR that hosts the NetApp Volumes IC-LIFs.
    
    
    gcloud netapp volumes replications list --volume=DESTINATION_VOLUME --location=REGION \
     --format="table(hybridPeeringDetails.subnetIp)"
    

This prints the CIDR. Ping the first IP of that network from the source ONTAP system, using one of your source IC-LIFs.

Example:
    
    
    ONTAP> ping -lif=YOUR_IC_LIF -vserver=VSERVER_HOSTING_SOURCE_VOLUME -destination=FIRST_IP_OF_SUBNET_IP
    

**Cluster peering** :

If ICMP works, the process proceeds to cluster peering. The status `PENDING_CLUSTER_PEERING` displays if peering has not yet been established.

Look up cluster-peering instructions:
    
    
    gcloud netapp volumes replications list --volume=DESTINATION_VOLUME --location=REGION \
     --format="table(hybridPeeringDetails.command,hybridPeeringDetails.passphrase)"
    

This process outputs the command and required passphrase for execution. Copy and paste the [cluster peer create](https://docs.netapp.com/us-en/ontap-cli/cluster-peer-create.html) command onto your source cluster and run it. You will be prompted to enter the passphrase twice.

**SVM peering** :

The `cluster peer create` command from the previous step is expected to also perform the SVM peering automatically. If this doesn't occur, the state changes to `PENDING_SVM_PEERING` after a few seconds.

Verify the SVM peering:
    
    
    gcloud netapp volumes replications list --volume=DESTINATION_VOLUME --location=REGION
    

If the state is `PENDING_SVM_PEERING`, run the [vserver peering command](https://docs.netapp.com/us-en/ontap-cli-9131/vserver-peer-create.html):
    
    
    gcloud netapp volumes replications list --volume=DESTINATION_VOLUME --location=REGION \
     --format="table(hybridPeeringDetails.command)"
    

After a few seconds, the state changes to **Ready** , and mirrorState to **Preparing** which indicates that the [baseline transfer](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/overview#baseline_transfer) has started. After the baseline transfer is finished, the mirrorState changes to **Mirrored**. [Incremental transfers](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/overview#incremental_transfers) are initiated based on the defined replication schedule, indicated by mirrorState as **Transferring**.

**Note:** The peering request expires if either the source information is incorrect or if the peering commands provided by NetApp Volumes aren't run on the source system within one hour. For the exact timestamp, see `commandExpiryTime` parameter. To modify parameters or restart the peering process, use the `gcloud netapp volumes replications establish-peering` command. Alternatively, you can delete and recreate the replication.

For more information about additional optional flags, see [Google Cloud SDK documentation on external replication creation](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--hybrid-replication-parameters).

## What's next

[Manage external replications](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/manage-external-replication).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
