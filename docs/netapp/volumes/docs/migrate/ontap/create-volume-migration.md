---
url: https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/create-volume-migration/
title: Create a volume migration \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:53.179125+00:00
---

# Create a volume migration  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/create-volume-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Create a volume migration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a [volume migration](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/overview#about_volume_migration).

## Before you begin

Before setting up a volume migration, we recommend that you review the [migration workflow](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/overview#overview_of_migration_process). The volume migration process starts by creating a destination volume and specifying the source system details. This action creates a destination volume resource and a replication child resource within NetApp Volumes for managing the replication.

## Considerations

  * The following features aren't supported for destination volumes during the migration process:

    * Volume replication, the destination volume as source for a cascade. Volume replication can be enabled after migration.

    * Flex File service level.

  * You can migrate FlexGroups to a large capacity volume. For the Flex Unified service level, the destination pool must be a large capacity pool.

  * You must use manual backups when doing backups of destination volumes. If you try to assign a backup policy to a destination volume, it will fail.

  * Select the correct storage pool and make sure that the destination volume is large enough to accommodate the logical size (not physical size) of your source volume.

  * Specify the correct share name and protocol types. The share name must match the source, and the protocol types must be chosen carefully as they can't be changed after volume creation. The protocol settings you choose also map to [volume security styles](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations#volume_security_style).

  * Verify that the [volume security style](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations#volume_security_style) of the destination volume you are creating matches the volume security style of your source volume.

  * Before creating a volume migration, make sure you have CLI access and the necessary permissions on the source ONTAP system. You need to run CLI commands on the source ONTAP system within one hour of the migration process.

  * You can't migrate a volume with [tamperproof snapshots](https://docs.netapp.com/us-en/ontap/snaplock/snapshot-lock-concept.html) to a volume that uses auto-tiering.

  * You can't migrate a source volume to multiple destinations in the same project simultaneously.

  * When you move data to a Flex Unified pool with auto-tiering enabled, enable hot-tier bypass during the migration. Otherwise, the migration fills the hot tier and causes out-of-space errors or unwanted hot-tier expansion. After the migration is complete, you can disable hot-tier bypass.




## Create a volume migration

Use the following instructions to create a volume migration using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Migrations** from the **Data protection** menu.

  3. Click **Migrate from ONTAP**.

  4. In the **Storage pool details** section, complete the following steps:

     1. Click **Select storage pool**.

     2. From the list of storage pools displayed, select the required storage pool.

     3. Click **Select**.

  5. In the **Volume details** section, complete the following steps:

     1. Enter the name of the destination volume in the **Destination volume name** field.

**Caution:** Your selection is permanent.
     2. Optional: enter a description for the volume in the **Description** field.

  6. In the **Protocol configuration** section, select the same protocol as the source volume. For some protocols, various options are displayed. For more information about protocol options, see [Create a new volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume#console).

  7. In the **Share name** section, enter the share name of the volume in the **Share name** field. The share name must be unique within a location. It's recommended to use the destination volume name as the share name.

**Caution:** Your selection is permanent.
  8. In the **Capacity configuration** section, enter the volume capacity in the **Capacity** field.

  9. Optional: if the selected storage pool allows auto-tiering:

     1. Select the **Enable auto-tiering** checkbox if you want to enable auto-tiering for the volume.

     2. Specify a cooling threshold between 2 and 183 days in the **Cooling threshold days** field. The default cooling threshold value is 31 days.

     3. When you migrate to a Flex Unified pool with auto-tiering enabled, select the **Enable hot tier bypass** checkbox. You can disable hot-tier bypass after the migration is complete.

  10. Optional: if you selected any NFS variant in the protocol configuration, you can specify export rules for the volume in the **Export rules** section.

  11. Optional: in the **Snapshot configuration** section, complete the following steps:

     1. Select **Make snapshot directory visible** to enable file system access to snapshot versions by clients. For more information, see [NetApp Volumes volume snapshots overview](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/overview).

     2. Select **Allow scheduled snapshots** to configure the volume to automatically take snapshots. You can specify the number of snapshots to keep at hourly, daily, weekly, and monthly snapshot intervals. Times are specified in UTC. If you reach the maximum number of snapshots, the oldest snapshot deletes.

     3. Review your snapshot selections.

  12. Click **Next**.

  13. In the **Migration details** section, enter a name for the migration resource in the **Migration name** field.

  14. Click **Next**.

  15. In the **Source cluster details** section, complete the following actions:

     1. Enter the name of your source cluster in the **Cluster name** field.

     2. Enter the name of the Storage Virtual Machine (SVM), also known as vserver, in the **Storage VM name** field. The SVM that hosts the source volume.

     3. Enter the name of the source volume in the **Volume name** field.

     4. Enter the Intercluster-LIF (IC-LIF) IP address in the **Inter-cluster IP** field. Each node of the source cluster needs an IC-LIF. Specify all IC-LIFs as a comma-separated list.

     5. Optional: enter a description for the source cluster location in the **Location** field.

  16. Click Next.

  17. Review your settings and click **Create** to start the migration process.


**Note:** If you see the error `Unable to find the resource you requested`, wait 30 seconds and click **Retry**.

After creating the migration process, you are redirected to the volume details view. Click the **Migration** tab to monitor the migration status.

You must authenticate the SnapMirror connection between your source ONTAP system and NetApp Volumes. Run the `cluster peer create` command on the source ONTAP cluster. If no prior peering exists, the **Migration** tab displays `Migration pending cluster peering from ONTAP source cluster`. If the source system uses ONTAP-mode, don't run `cluster peer create` directly on it. Instead, run `peer_cluster.py` with `PEER_MODE=accept`. For more information, see [Cluster peering script](https://docs.cloud.google.com/netapp/volumes/docs/ontap/peer-clusters-svms#cluster_peering_script).

If you click **Initiate peering** , a side page with instructions displays. Follow these instructions, and click **Check peering**. After a successful peering, the side page disappears, and the transfer status of the migration changes to _Preparing_. The baseline transfer is now running. A baseline transfer can take minutes, hours, or days depending on the amount of data to be transferred and the network speed. Once the baseline transfer is complete, the transfer status switches to _Mirrored_.

### gcloud

To create a volume migration:
    
    
    gcloud netapp volumes create VOLUME_NAME --location=LOCATION \
      --capacity=CAPACITY --protocols=PROTOCOL \
      --share-name=SHARE_NAME --storage-pool=STORAGE_POOL \
      --hybrid-replication-parameters=cluster-location=CLUSTER_LOCATION,peer-cluster-name=PEER_CLUSTER_NAME,peer-ip-addresses=PEER_IP_ADDRESSES,peer-svm-name=PEER_SVM_NAME,peer-volume-name=PEER_VOLUME_NAME,replication=REPLICATION,description=DESCRIPTION,labels=LABELS

When you migrate to a Flex Unified pool with auto-tiering enabled, always enable hot-tier bypass during migration. After the migration is complete, you can disable hot-tier bypass. Use the `gcloud beta netapp volumes create` command to create a volume with auto-tiering enabled.

The following example shows the required parameters to create a volume with auto-tiering enabled:
    
    
    --tiering-policy=tier-action=ENABLED,cooling-threshold-days=DAYS,enable-hot-tier-bypass-mode=on

The `hybrid-replication-parameters` block starts a migration workflow.

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

  * `REPLICATION`: the name of the replication resource to be created.

  * `LARGE_VOLUME_CONSTITUENT_COUNT`: this parameter is only required when your source volume is a [FlexGroup](https://docs.netapp.com/us-en/ontap/flexgroup/definition-concept.html). For more information, see [FlexGroups and Large Volumes](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/flexgroups-and-large-volumes).

To create a large volume, `specify --large-volume true` and `--multiple-endpoints true` as create parameters too.

  * `CLUSTER_LOCATION`:Optional: the description of the source cluster location.

  * `DESCRIPTION`:Optional: the description text for the replication resource.

  * `LABELS`:Optional: labels for the replication resource.

The following example shows how to specify key-value pairs for the `labels` parameter:
        
        labels=KEY1:VALUE1#KEY2:VALUE2




Example invocation:
    
    
    $ gcloud beta netapp volumes create ok-destination --location australia-southeast1 \
    --capacity 100 --protocols=nfsv3 \
    --share-name ok-destination --storage-pool okrause-pool \
    --hybrid-replication-parameters=peer-cluster-name=au2se1cvo2sqa,peer-ip-addresses=10.0.0.25#10.0.0.26,peer-svm-name=svm_au2se1cvo2sqa,peer-volume-name=okrause_source,replication=okrause-replication \
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

  * If cluster peering isn't already established, NetApp Volumes prints the cluster peering commands you must run on the source system. If the source system uses ONTAP-mode, don't run `cluster peer create` directly on it. Instead, run `peer_cluster.py` with `PEER_MODE=accept`. For more information, see [Cluster peering script](https://docs.cloud.google.com/netapp/volumes/docs/ontap/peer-clusters-svms#cluster_peering_script).

  * Also, if SVM peering isn't already established, NetApp Volumes prints the vserver peering commands you must run on the source system.




The steps that have been completed previously are skipped, and the process automatically continues with the next step.

**Network connectivity check**

NetApp Volumes tries to send an ICMP (ping) request to the IC-LIFs you specified under `peer-ip-addresses`. If it fails, `stateDetails` displays `Cluster peering failed, please try again`, indicating a network issue. For more information, see [Network connection to Google Cloud project](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/prerequisites-ontap-netapp-volumes#network-connection). You can't proceed further until you establish a network connectivity between the source system and NetApp Volumes. For debugging purposes, try to ping the gateway IP of the `/27` CIDR that hosts the NetApp Volumes IC-LIFs.
    
    
    gcloud netapp volumes replications list --volume=DESTINATION_VOLUME --location=REGION \
     --format="table(hybridPeeringDetails.subnetIp)"
    

This prints the CIDR. Ping the first IP of that network from the source ONTAP system, using one of your source IC-LIFs.

Example:
    
    
    source> ping -lif=YOUR_IC_LIF -vserver=VSERVER_HOSTING_SOURCE_VOLUME -destination=FIRST_IP_OF_SUBNET_IP
    

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
    

After a few seconds, the state changes to **Ready** , and mirrorState to **Preparing** which indicates that the [baseline transfer](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/overview#baseline_transfer) has started. After the baseline transfer is finished, the mirrorState changes to **Mirrored**. Every hour volume migration triggers an [incremental transfer](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/overview#incremental_transfers), indicated by mirrorState as **Transferring**.

**Note:** The peering request expires if either the source information is incorrect or if the peering commands provided by NetApp Volumes aren't run on the source system within one hour. For the exact timestamp, see `commandExpiryTime` parameter. To modify parameters or restart the peering process, use the `gcloud netapp volumes replications establish-peering` command. Alternatively, you can delete and recreate the replication.

## What's next

[Manage volume migrations](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/manage-volume-migration).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
