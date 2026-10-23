---
url: https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/bms-filestore-oracle-backups/
title: Create Oracle backups with Filestore on Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:31.357802+00:00
---

# Create Oracle backups with Filestore on Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/bms-filestore-oracle-backups/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create Oracle backups with Filestore on Bare Metal Solution

This guide shows how to implement Filestore on Bare Metal Solution for Oracle backups.

Filestore is a fully managed file storage that you can use with Bare Metal Solution. It is scalable and provides a consistent view of the data in your file system. For more information about Filestore, see [Filestore overview](https://docs.cloud.google.com/filestore/docs/overview).

This guide assumes that you are familiar with [Bare Metal Solution network architecture](https://docs.cloud.google.com/bare-metal/docs/bms-deploy#understand_the_components).

## Deployment

In this guide, we create a deployment that meets the following criteria:

  * A Bare Metal Solution server is connected to the Google Cloud project by Partner Interconnect.
  * Two Cloud Routers are available for the Partner Interconnect setup.
  * A Filestore instance is available in the same VPC network as the Bare Metal Solution server.
  * The Bare Metal Solution server is able to talk to the Filestore file share using the NFS ports (111, 2049, 2050).
  * The Bare Metal Solution server and the Filestore instance are aware of each other's IP range by advertising the default IP range (`0.0.0.0/0`) in the Cloud Routers.



In this example deployment, the Bare Metal Solution server is hosted on the `ops-peering-vpc` VPC network in the `Southamerica-east1` region. The Cloud Routers are `ops-peering-sp-router-a1` and `ops-peering-sp-router-a2`.

You can relate the preceding environment considerations to your own network infrastructure and modify the deployment accordingly.

## Implement Filestore on Bare Metal Solution

Implementing Filestore on Bare Metal Solution involves the following steps:

  1. Create a Filestore instance.
  2. Create a firewall rule.
  3. Advertise a default route.
  4. Mount the Filestore file share.
  5. Validate the Filestore file share.
  6. Change the ownership of the NFS mount point.
  7. Run an RMAN backup.
  8. Validate the backup.



### Create a Filestore instance

[Create a Filestore instance](https://docs.cloud.google.com/filestore/docs/creating-instances) in the same network and region as that of your Bare Metal Solution server.

Keep the following considerations in mind for this implementation:

  1. **Region** and **Zone** : Select the same region and zone as that of your Bare Metal Solution server. In this case, the region is `southamerica-east1` and the zone is `southamerica-east1-a`.
  2. **VPC Network** : Select the network that is connected to your Bare Metal Solution server. In this case, select `ops-peering-vpc`.
  3. **Allocated IP range** : To use an existing allocated IP range in the network, select **Use an existing allocated IP range**. Otherwise, select **Use an automatically allocated IP range** to automatically create an IP range and a private service access connection.
  4. **Access control** : Do the following:

     1. Select **Restrict access by IP address or range**.
     2. Enter the IP CIDR that contains the Bare Metal Solution server for Filestore to be able to connect to the Bare Metal Solution server.
     3. Select the access level.

**Note:** This step is required because the Bare Metal Solution server is hosted in a regional extension. Therefore, the default option of **Grant access to all clients on the VPC network** does not automatically allow the Bare Metal Solution server to access the Filestore instance.



### Create a firewall rule

[Create a firewall rule](https://docs.cloud.google.com/firewall/docs/using-firewalls#creating_firewall_rules) for the Bare Metal Solution server to connect with the Filestore instance.

Keep the following considerations in mind for this implementation:

  * **Network** : Select your VPC network. In this case, select `ops-peering-vpc`.
  * **Priority** : Specify `1000`.
  * **Direction** : Select `ingress`.
  * **IP ranges** : You can either allow access to all IP addresses in the network or you can limit the access to your Bare Metal Solution environment.
  * **Protocols and ports** : Do the following: 
    1. Select **Specified protocols and ports**.
    2. Select **TCP**.
    3. Enter a comma-delimited list of destination ports (111, 2049, 2050).



### Advertise a default route

Advertise a default route (`0.0.0.0/0`) in the Cloud Routers.

Follow the steps in [Add a custom advertisement for a default IP range to your BGP sessions](https://docs.cloud.google.com/bare-metal/docs/bms-setup#add_a_custom_advertisement_for_a_default_ip_range_to_your_bgp_sessions).

A Partner Interconnect setup comes with two Cloud Routers (in this case, `ops-peering-sp-router-a1` and `ops-peering-sp-router-a2`). You can advertise the default route in any one router. However, for high availability and fault tolerance, we recommend advertising a default route in both Cloud Routers.

### Mount the Filestore file share

Mount the Filestore file share on the Bare Metal Solution server.

Perform the following steps as the root user:

  1. In your Bare Metal Solution server, create an NFS mount point for the Filestore file share.
         
         mkdir /nfs_backups
         

  2. Mount the file share by running the `mount` command and specifying the Filestore instance IP address and name of the file share.
         
         mount \
         -o hard,vers=3,proto=tcp,timeo=600,retrans=3,rsize=1048576,wsize=1048576,resvport,async \
         FILESTORE_IP_ADDRESS:/FILESTORE_FILE_SHARE /NFS_MOUNT_POINT
         

Replace the following:

     * FILESTORE_IP_ADDRESS: IP address of the Filestore instance.
     * FILESTORE_FILE_SHARE: Name of the Filestore file share.
     * NFS_MOUNT_POINT: Name of the NFS mount point that you created in the previous step.

For this deployment, run the following command:
    
    mount \
    -o hard,vers=3,proto=tcp,timeo=600,retrans=3,rsize=1048576,wsize=1048576,resvport,async \
    10.177.199.242:/oracle_backups /nfs_backups
    

**Note:** For more information about the mount options, see [Optimize and test Filestore performance](https://docs.cloud.google.com/filestore/docs/performance).



### Validate the Filestore file share

To validate the Filestore file share, run the following commands:
    
    
    df -h | grep FILESTORE_FILE_SHARE
    
    oracle_backup_psoracle 1.0P 0 1.0P 0% /home/oracle/backups
    10.177.199.242:/oracle_backups 2.5T 484G 1.9T 21% /nfs_backups
    
    
    
    cd /nfs_backups
    
    
    
    touch TEST_FILENAME
    
    
    
    ls -ltr
    
    total 16
    drwx------. 2 root root 16384 Sep 16 03:43 lost+found
    -rw-r--r--. 1 root root 0 Sep 16 2020 a
    

### Change the ownership of the NFS mount point

Change the ownership of the NFS mount point. The Filestore file share is mounted as `root`.

In this case, you use the file share for Oracle Recovery Manager (RMAN) backups. Therefore, you need to change the ownership of the NFS mount point to the `oracle` user and grant the required permissions to read and write.
    
    
    chown -R oracle:oinstall /nfs_backups
    chmod -R 755 /nfs_backups
    

### Run an RMAN backup

After you have mounted the file share in the Bare Metal Solution server, you can use it to run the RMAN backups.

Run the following commands:
    
    
    rman target /
    
    
    
    run
    
    {
    ALLOCATE CHANNEL c1 DEVICE TYPE disk format '/nfs_backups/%U';
    ALLOCATE CHANNEL c2 DEVICE TYPE disk format '/nfs_backups/%U';
    ALLOCATE CHANNEL c3 DEVICE TYPE disk format '/nfs_backups/%U';
    ALLOCATE CHANNEL c4 DEVICE TYPE disk format '/nfs_backups/%U';
    ALLOCATE CHANNEL c5 DEVICE TYPE disk format '/nfs_backups/%U';
    ALLOCATE CHANNEL c6 DEVICE TYPE disk format '/nfs_backups/%U';
    ALLOCATE CHANNEL c7 DEVICE TYPE disk format '/nfs_backups/%U';
    ALLOCATE CHANNEL c8 DEVICE TYPE disk format '/nfs_backups/%U';
    Backup section size 50G database;
    }2> 3> 4> 5> 6> 7> 8> 9> 10> 11> 12> 13>
    using target database control file instead of recovery catalog
    allocated channel: c1
    Finished backup at 24-SEP-20
    Starting Control File and SPFILE Autobackup at 24-SEP-20
    piece handle=+DATA/ORCL/AUTOBACKUP/2020_09_24/s_1051968470.603.1051968471 comment=NONE
    Finished Control File and SPFILE Autobackup at 24-SEP-20
    released channel: c1
    released channel: c2
    released channel: c3
    released channel: c4
    released channel: c5
    released channel: c6
    released channel: c7
    released channel: c8
    RMAN>
    Recovery Manager complete.
    

### Validate the backup

Validate the backup in the NFS mount point directory. Run the following commands:
    
    
    ls -ltr
    
    total 507458532
    drwxr-xr-x. 2 oracle oinstall 16384 Sep 16 03:43 lost+found
    -rw-r-----. 1 oracle dba 5267456 Sep 24 13:05 javb7fcs_1_1
    -rw-r-----. 1 oracle dba 2506752 Sep 24 13:05 jevb7fcs_1_1
    -rw-r-----. 1 oracle dba 3956736 Sep 24 13:05 jdvb7fcs_1_1
    -rw-r-----. 1 oracle dba 868564992 Sep 24 13:06 jcvb7fcs_1_1
    -rw-r-----. 1 oracle dba 1778835456 Sep 24 13:06 jbvb7fcs_1_1
    -rw-r-----. 1 oracle dba 53653921792 Sep 24 13:21 j9vb7fcs_4_1
    -rw-r-----. 1 oracle dba 53684600832 Sep 24 13:21 j9vb7fcs_3_1
    -rw-r-----. 1 oracle dba 53684584448 Sep 24 13:21 j9vb7fcs_5_1
    -rw-r-----. 1 oracle dba 53682978816 Sep 24 13:22 j9vb7fcs_2_1
    -rw-r-----. 1 oracle dba 53686919168 Sep 24 13:22 j9vb7fcs_1_1
    -rw-r-----. 1 oracle dba 53686902784 Sep 24 13:22 j9vb7fcs_6_1
    -rw-r-----. 1 oracle dba 81920 Sep 24 13:22 j9vb7fcs_11_1
    -rw-r-----. 1 oracle dba 53687025664 Sep 24 13:22 j9vb7fcs_7_1
    -rw-r-----. 1 oracle dba 53685944320 Sep 24 13:22 j9vb7fcs_8_1
    -rw-r-----. 1 oracle dba 33838702592 Sep 24 13:28 j9vb7fcs_10_1
    -rw-r-----. 1 oracle dba 53685944320 Sep 24 13:32 j9vb7fcs_9_1
    

You can now create Oracle backups in the Filestore file share on your Bare Metal Solution server.

## What's next

  * Learn about [Best practices for Oracle on Bare Metal Solution](https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/bms-oracle-best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
