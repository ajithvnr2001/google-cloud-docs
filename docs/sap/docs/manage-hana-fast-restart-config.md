---
url: https://docs.cloud.google.com/sap/docs/manage-hana-fast-restart-config/
title: Manage the SAP HANA Fast Restart configuration \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:19.924232+00:00
---

# Manage the SAP HANA Fast Restart configuration  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/manage-hana-fast-restart-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Manage the SAP HANA Fast Restart configuration Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to enable the SAP HANA Fast Restart option for an SAP HANA workload. This guide also describes how to modify the SAP HANA Fast Restart configuration when you resize the Compute Engine instances that host the SAP HANA workload. 

The SAP HANA Fast Restart option reduces the restart time in the event that SAP HANA terminates while the operating system remains running. Google Cloud recommends that you enable this option for your SAP HANA workload, especially for multi-terabyte workloads. For more information about this option, see the SAP document [SAP HANA Fast Restart Option](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/ce158d28135147f099b761f8b1ee43fc.html).

This document is intended for SAP Basis and SAP system administrators who are familiar with managing SAP HANA workloads.

## Before you begin

  1. In the Google Cloud console, select the Google Cloud project where your SAP HANA workload is running.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Make sure that the `SIDadm` OS user that you use has permission to start and stop SAP HANA.




### Required roles

To ensure that the service account has the necessary permissions to access secrets stored in Secret Manager, ask your administrator to grant the following IAM roles to the service account on your project: 

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * If you are using the automation script provided by Google Cloud to enable the SAP HANA Fast Restart option, and are using Secret Manager to store the password to connect to the SAP HANA database: [Secret Manager Secret Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to access secrets stored in Secret Manager. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to access secrets stored in Secret Manager:

  * If you are using the automation script provided by Google Cloud to enable the SAP HANA Fast Restart option, and are using Secret Manager to store the password to connect to the SAP HANA database: `secretmanager.versions.access`



Your administrator might also be able to give the service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable the SAP HANA Fast Restart option

###  Use automation script 

Google Cloud provides a script that you can use to enable SAP HANA Fast Restart option.

**Important:** Test the script that Google Cloud provides in a non-production environment before you use it in production. You are responsible for the configuration of the SAP HANA Fast Restart option.

To enable the SAP HANA Fast Restart option by using the automation script provided by Google Cloud, complete the following steps:

  1. Establish an SSH connection with the compute instance that's running your SAP HANA workload.

  2. As the `SIDadm` user, stop the SAP HANA database.

  3. Download the `sap_lib_hdbfr.sh` script, which is provided by Google Cloud:
         
         wget https://storage.googleapis.com/cloudsapdeploy/terraform/latest/terraform/lib/sap_lib_hdbfr.sh
         

  4. Make the `sap_lib_hdbfr.sh` file executable:
         
         sudo chmod +x sap_lib_hdbfr.sh
         

  5. Verify that the script has no errors:
         
         ./sap_lib_hdbfr.sh -help
         

If the command returns an error, then contact Cloud Customer Care. For information about how to contact Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

  6. Enable the SAP HANA Fast Restart option by running the script:
         
         sudo ./sap_lib_hdbfr.sh -h 'SID' -s SECRET_NAME
         

If you're not using a Secret Manager secret to provide the password, you can provide the password in plain text. However, Google Cloud recommends against this because the password gets recorded in the command-line history of the compute instance.
         
         sudo ./sap_lib_hdbfr.sh -h 'SID' -p PASSWORD
         

Replace the following:

     * `SID`: the SAP system ID (SID) of your SAP HANA workload; for example `AB1`
     * `SECRET_NAME`: the name of the secret in Secret Manager that securely stores the password for the `SYSTEM` user of your SAP HANA database. The secret must exist in the same Google Cloud project that runs your SAP HANA workload.
     * `PASSWORD`: the password of the `SYSTEM` user of your SAP HANA database

The output is similar to the following:
    
    INFO - Script is running in standalone mode
    ls: cannot access '/hana/tmpfs*': No such file or directory
    INFO - Setting up HANA Fast Restart for system 'TST/00'.
    INFO - Number of NUMA nodes is 2
    INFO - Number of directories /hana/tmpfs* is 0
    INFO - HANA version 2.57
    INFO - No directories /hana/tmpfs* exist. Assuming initial setup.
    INFO - Creating 2 directories /hana/tmpfs* and mounting them
    INFO - Adding /hana/tmpfs* entries to /etc/fstab. Copy is in /etc/fstab.20220625_030839
    INFO - Updating the HANA configuration.
    INFO - Running command: select * from dummy
    DUMMY
    "X"
    1 row selected (overall time 4124 usec; server time 130 usec)
    
    INFO - Running command: ALTER SYSTEM ALTER CONFIGURATION ('global.ini', 'SYSTEM') SET ('persistence', 'basepath_persistent_memory_volumes') = '/hana/tmpfs0/TST;/hana/tmpfs1/TST;'
    0 rows affected (overall time 3570 usec; server time 2239 usec)
    
    INFO - Running command: ALTER SYSTEM ALTER CONFIGURATION ('global.ini', 'SYSTEM') SET ('persistent_memory', 'table_unload_action') = 'retain';
    0 rows affected (overall time 4308 usec; server time 2441 usec)
    
    INFO - Running command: ALTER SYSTEM ALTER CONFIGURATION ('indexserver.ini', 'SYSTEM') SET ('persistent_memory', 'table_default') = 'ON';
    0 rows affected (overall time 3422 usec; server time 2152 usec)
    

  7. As the `SIDadm` user, start the SAP HANA database.




###  Manual steps 

To manually enable the SAP HANA Fast Restart option for your workload, complete the following steps:

  1. Establish an SSH connection with the compute instance that's running your SAP HANA workload.

  2. As the `SIDadm` user, stop the SAP HANA database.

  3. Create directories for the NUMA nodes and mount them in the `tmpfs` file system:

     1. Review the NUMA topology of your compute instance:
            
            sudo lscpu | grep NUMA
            

The following is an example output for a compute instance based on the `m2-ultramem-208` machine type, which has four NUMA nodes numbered 0-3. Your output is similar to this example.
            
            NUMA node(s):        4
            NUMA node0 CPU(s):   0-25,104-129
            NUMA node1 CPU(s):   26-51,130-155
            NUMA node2 CPU(s):   52-77,156-181
            NUMA node3 CPU(s):   78-103,182-207
            

     2. Create a directory for each NUMA node and assign the ownership of these directories to the SAP HANA administrator user and group:
            
            mkdir -pv /hana/tmpfsNEW_NUMA_NODE_INDEX_RANGE/SID
            chown -R SID_LCadm:sapsys /hana/tmpfs*/SID
            chmod 777 -R /hana/tmpfs*/SID

Replace the following:

        * `SID`: the SAP system ID (SID) of your SAP HANA workload; for example `AB1`
        * `NUMA_NODE_INDEX_RANGE`: the index range for the NUMA nodes available on your compute instance. For example, if your compute instance was based on the `m2-ultramem-208` machine type, which has four NUMA nodes, then you'd specify the value `0..3`.
        * `SID_LC`: the SID in lowercase; for example `ab1`
     3. Mount the NUMA node directories to the `tmpfs` file system:
            
            sudo mount tmpfsSID0 -t tmpfs -o mpol=prefer:0 /hana/tmpfs0/SID
            sudo mount tmpfsSID1 -t tmpfs -o mpol=prefer:1 /hana/tmpfs1/SID
            sudo mount tmpfsSID2 -t tmpfs -o mpol=prefer:2 /hana/tmpfs2/SID
            sudo mount tmpfsSID3 -t tmpfs -o mpol=prefer:3 /hana/tmpfs3/SID
            

     4. To ensure that these mount points persist after an OS reboot, add the following entries to the `/etc/fstab` file:
            
            tmpfsSID0 /hana/tmpfs0/SID tmpfs rw,nofail,relatime,mpol=prefer:0
            tmpfsSID1 /hana/tmpfs1/SID tmpfs rw,nofail,relatime,mpol=prefer:1
            tmpfsSID1 /hana/tmpfs2/SID tmpfs rw,nofail,relatime,mpol=prefer:2
            tmpfsSID1 /hana/tmpfs3/SID tmpfs rw,nofail,relatime,mpol=prefer:3
            

  4. (Optional) Because the `tmpfs` file system can grow and shrink dynamically, you can limit its memory usage by using the following options:

     * Limit the size of a NUMA node volume:
           
           sudo mount tmpfsSID0 -t tmpfs -o mpol=prefer:0,size=SIZE /hana/tmpfs0/SID
           

Replace `SIZE` with the size to which you want to limit the NUMA node volume. For example, `250G`.

     * Limit the overall memory usage of `tmpfs` for all NUMA for a given SAP HANA instance and given compute instance by setting the `persistent_memory_global_allocation_limit` in the `[memorymanager]` section the SAP HANA `global.ini` file.

  5. From the compute instance that's running your workload, inform the SAP HANA system about the `tmpfs` locations by updating the `[persistence]` section of the `global.ini` file to include paths to the `tmpfs` location that you created in the preceding steps. Separate each `tmpfs` location with a semicolon.

The following example is specific to an `m2-ultramem-208` instance, and specifies four memory volumes that correspond to the four NUMA nodes available on the M2 instance. If you were running SAP HANA on an `m2-ultramem-416` instance, then you'd need to configure eight memory volumes.
         
         [persistence]
         basepath_datavolumes = /hana/data
         basepath_logvolumes = /hana/log
         basepath_persistent_memory_volumes = /hana/tmpfs0/SID;/hana/tmpfs1/SID;/hana/tmpfs2/SID;/hana/tmpfs3/SID
         

  6. To turn on persistent memory for any SAP HANA tables or partitions, complete the following steps on the compute instance that's running your workload:

     1. Turn on persistent memory for the SAP HANA table or partition, run the following SQL query:
            
            ALTER TABLE TABLE_OR_PARTITION_NAME persistent memory ON immediate CASCADE
            

Replace `TABLE_OR_PARTITION_NAME` with the name of the table or partition.

     2. Update the memory persistence settings by adding the `table_default` parameter in the `indexserver.ini` file:
            
            [persistent_memory]
            table_default = ON
            

For information from SAP about how to control columns, tables, and which monitoring views provide detailed information, see [Persistent Memory](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/1f61b13e096d4ef98e62c676debf117e.html).

  7. As the `SIDadm` user, start the SAP HANA database.




## Modify the fast restart configuration after increasing compute instance size

After you increase the size of the compute instance that hosts your SAP HANA workload, you must update the SAP HANA Fast Restart configuration to match the new NUMA topology.

To modify the configuration of the SAP HANA Fast Restart option for such a scenario, complete the following steps:

  1. Establish an SSH connection with the resized compute instance that runs your workload.

  2. As the `SIDadm` user, stop the SAP HANA database.

  3. Make note of the NUMA topology of the resized compute instance:
         
         sudo lscpu | grep NUMA
         

  4. Clear the occupied memory by unmounting the existing `tmpfs` file systems:
         
         sudo umount /hana/tmpfs0/SID
         sudo umount /hana/tmpfs1/SID
         sudo umount /hana/tmpfs2/SID
         sudo umount /hana/tmpfs3/SID
         

Replace `SID` with the SID of your SAP HANA database, for example `ABC`.

  5. For each new NUMA node, create a directory and assign the ownership of these new directories to the SAP HANA administrator user and group:
         
         mkdir -pv /hana/tmpfsNEW_NUMA_NODE_INDEX_RANGE/SID
         chown -R SID_LCadm:sapsys /hana/tmpfs*/SID
         chmod 777 -R /hana/tmpfs*/SID

Replace the following:

     * `NEW_NUMA_NODE_INDEX_RANGE`: the index range that denotes the new NUMA nodes. For example, imagine that your compute instance was based on the `m2-ultramem-208` machine type, which has four NUMA nodes (`0..3`). If you resized your instance to use the `m2-ultramem-416` machine type, which has 8 NUMA nodes, then you'd specify the range `4..7`.
     * `SID_LC`: the SID in lowercase; for example `abc`
  6. Mount each new NUMA node directory to the `tmpfs` file system:
         
         sudo mount tmpfsSIDSERIAL_NUMBER_OF_NEW_NODE -t tmpfs -o mpol=prefer:SERIAL_NUMBER_OF_NEW_NODE /hana/tmpfsSERIAL_NUMBER_OF_NEW_NODE/SID
         

For example, if you resized from `m2-ultramem-208` (4 NUMA nodes) to `m2-ultramem-416` (8 NUMA nodes) for a system with SID `ABC`, then you'd have to run the following:
         
         sudo mount tmpfsABC4 -t tmpfs -o mpol=prefer:4 /hana/tmpfs4/ABC
         sudo mount tmpfsABC5 -t tmpfs -o mpol=prefer:5 /hana/tmpfs5/ABC
         sudo mount tmpfsABC6 -t tmpfs -o mpol=prefer:6 /hana/tmpfs6/ABC
         sudo mount tmpfsABC7 -t tmpfs -o mpol=prefer:7 /hana/tmpfs7/ABC
         

  7. To ensure that these mount points persist and are available after an OS reboot, add an entry for each new mount point to the `/etc/fstab` file:
         
         tmpfsSIDSERIAL_NUMBER_OF_NEW_NODE /hana/tmpfsSERIAL_NUMBER_OF_NEW_NODE/SID tmpfs rw,nofail,relatime,mpol=prefer:SERIAL_NUMBER_OF_NEW_NODE
         

Continuing with the example:
         
         tmpfsABC4 /hana/tmpfs4/ABC tmpfs rw,nofail,relatime,mpol=prefer:4
         tmpfsABC5 /hana/tmpfs5/ABC tmpfs rw,nofail,relatime,mpol=prefer:5
         tmpfsABC6 /hana/tmpfs6/ABC tmpfs rw,nofail,relatime,mpol=prefer:6
         tmpfsABC7 /hana/tmpfs7/ABC tmpfs rw,nofail,relatime,mpol=prefer:7
         

  8. Inform the SAP HANA system about the new `tmpfs` locations, update the `[persistence]` section of the `global.ini` file to include paths to the new `tmpfs` locations that you created. Separate each `tmpfs` location with a semicolon.

Continuing with the example, the updated `global.ini` file looks similar to the following:
         
         [persistence]
         basepath_persistent_memory_volumes = /hana/tmpfs0/ABC;/hana/tmpfs1/ABC;/hana/tmpfs2/ABC;/hana/tmpfs3/ABC;/hana/tmpfs4/ABC;/hana/tmpfs5/ABC;/hana/tmpfs6/ABC;/hana/tmpfs7/ABC;
         

  9. As the `SIDadm` user, start the SAP HANA database.




## Modify the fast restart configuration after decreasing compute instance size

After you decrease the size of the compute instance that hosts your SAP HANA workload, you must update the SAP HANA Fast Restart configuration to match the new NUMA topology.

To modify the configuration of the SAP HANA Fast Restart option for such a scenario, complete the following steps:

  1. Establish an SSH connection with the resized compute instance that runs your workload.

  2. As the `SIDadm` user, stop the SAP HANA database.

  3. Make note of the NUMA topology of the resized compute instance:
         
         sudo lscpu | grep NUMA
         

  4. Clear the occupied memory by unmounting and removing the directories from the `tmpfs` file system that correspond to the reduced number of NUMA nodes on your resized compute instance:
         
         umount /hana/tmpfsNUMA_NODE_INDEX/SID
         rmdir /hana/tmpfsNUMA_NODE_INDEX/SID
         

Replace the following:

     * `SID`: the SID of your SAP HANA database, for example `ABC`
     * `NUMA_NODE_INDEX`: the index of the NUMA node that is no longer present

For example, image that your compute instance was based on the `m2-ultramem-208` machine type, which has four NUMA nodes (`0..3`). If you resized your instance to use the `m3-ultramem-128` machine type, which has two NUMA nodes, then you'd unmount and remove the directories corresponding to the NUMA nodes 2 and 3:
    
    unmount /hana/tmpfs2/ABC
    rmdir /hana/tmpfs2/ABC
    unmount /hana/tmpfs3/ABC
    rmdir /hana/tmpfs3/ABC
    

  5. To ensure that these changes persist even after an OS reboot, remove the entries from `/etc/fstab` file that correspond to the NUMA nodes that are no longer present.

Continuing with the example, the updated `/etc/fstab` file looks similar to the following:
         
         tmpfsABC0 /hana/tmpfs0/ABC tmpfs rw,nofail,relatime,mpol=prefer:0
         tmpfsABC1 /hana/tmpfs1/ABC tmpfs rw,nofail,relatime,mpol=prefer:1
         

  6. Inform the SAP HANA system about the updated `tmpfs` locations by modifying the `[persistence]` section of the `global.ini` file and removing paths of the `tmpfs` locations that you are no longer available.

Continuing with the example, the updated `global.ini` file looks similar to the following:
         
         [persistence]
         basepath_persistent_memory_volumes = /hana/tmpfs0/ABC;/hana/tmpfs1/ABC;
         

  7. As the `SIDadm` user, start the SAP HANA database.




## Verify that the fast restart option is enabled

To verify that the SAP HANA Fast Restart option is enabled for your SAP HANA deployment, see the SAP note [3439821 - How to know if SAP HANA database Fast Restart Option (FRO) is used on your HANA database or not](https://me.sap.com/notes/3439821).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
