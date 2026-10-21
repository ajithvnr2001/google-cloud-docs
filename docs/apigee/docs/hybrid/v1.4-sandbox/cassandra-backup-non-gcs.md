---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.4-sandbox/cassandra-backup-non-gcs/
title: Backup and recovery without Google Cloud \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:12:01.559242+00:00
---

# Backup and recovery without Google Cloud  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.4-sandbox/cassandra-backup-non-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  Backup and recovery without Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This section discusses how to configure backup and recovery of your Cassandra database using ssh and your file system instead of using Google Cloud. See also: 

  * [Cassandra backup and recovery](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4-sandbox/backup-recovery).
  * [Cassandra database](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4-sandbox/what-is-hybrid#cassandra-datastore).



##  What is Cassandra backup and recovery without Google Cloud Services? 

Backup without Cloud Services stores backups of your Cassandra database to compressed files in the file system of a server you specify. Backups occur on a schedule you specify in your overrides file. The connection to the server is by secure SSH. 

**Note:** You must ensure there is enough space on the file system for the backups, and adjust the frequency of the backups do avoid unnecessarily filling the alloted storage space. Apigee does not dictate a retention policy for the backup files. You may want to create a retention policy for files appropriate to your installation.

##  Setting up backups without Cloud Services: 

The following steps include common examples for completing specific tasks, like creating an SSH key pair. Use the methods that are appropriate to your installation. 

The procedure has the following parts: 

  * Set up the server and SSH
  * Set the schedule and destination for backup
  * Set up for revovery



###  Set up the server and SSH 

  1. Designate a Linux or Unix server for your backups. This server must be reachable via SSH from your Apigee hybrid runtime plane. It must have enough storage for your backups.
  2. Set up an SSH server on the server, or ensure that it has a secure SSH server configured. **Caution:** For security purposes, make sure your SSH server is up to date.
  3. Create an SSH key pair and store the private key file in a path that is accessible from your hybrid runtime plane. **Do not use a blank password for you key pair**. For example: 
         
         ssh-keygen -t rsa -b 4096 -C exampleuser@example.com
           Enter file in which to save the key (/Users/exampleuser/.ssh/id_rsa): $APIGEE_HOME/hybrid-files/certs/ssh_key
           Enter passphrase (empty for no passphrase):
           Enter same passphrase again:
           Your identification has been saved in ssh_key
           Your public key has been saved in ssh_key.pub
           The key fingerprint is:
           SHA256:DWKo334XMZcZYLOLrd/8HNpjTERPJJ0mc11UYmrPvSA exampleuser@example.com
           The key's randomart image is:
           +---[RSA 4096]----+
           |          +.  ++X|
           |     .   . o.=.*+|
           |    . o . . o==o |
           |   . . . =oo+o...|
           |  .     S +E oo .|
           |   . .   .. . o .|
           |    . . .  . o.. |
           |     .  ...o ++. |
           |      .. .. +o+. |
           +----[SHA256]-----+

  4. Create a user account on the backup server with the name "`apigee`". Make sure the new "`apigee`" user has a home directory under `/home`.
  5. On the backup server, create an "`ssh`" directory in the new `/home/apigee` directory.
  6. Copy the public key (`ssh_key.pub` in the previous example) into a file named "`authorized_keys`" in the new `/home/apigee/ssh` directory. For example: 
         
         cd /home/apigee
         mkdir .ssh
         cd .ssh
         vi authorized_keys

  7. On your backup server, create a backup directory within the `/home/apigee/` directory. The backup directory can be any directory as long as the "apigee" user has access to it. For example: 
         
         cd /home/apigee
         mkdir cassandra-backup

  8. Test the connection. You need to make sure that your Cassandra pods can connect to your backup server via SSH: 
     1. Log into the shell of your Cassandra pod. For example: 
            
            kubectl exec -it -n apigee apigee-cassandra-default-0 -- /bin/bash

Where apigee-cassandra-default-0 is the name of a cassandra pod. Change this to the name of the pod you want to connect from. 

     2. Connect by SSH to your backup server, using the server IP address: 
            
            ssh apigee@backup-server-ip

**Note:** You may see an warning at this point saying this is the server's fingerprint is unrecognized and asking if you would like to continue. For purposes of this test, this means you can successfully reach your backup server from your cassandra pod. You do not need to continue.



###  Set the schedule and destination for backup 

You set the schedule and destination for backups in your `overrides.yaml` file. 

  1. Add the following parameters to your `overrides.yaml` file: 

### Parameters
         
         cassandra:backup:
              enabled: true
              keyFile: "path-to-private-key-file"
              server: "backup-server-ip"
              storageDirectory: "/home/apigee/backup-directory"
              cloudProvider: "HYBRID" # required verbatim "HYBRID" (all caps)
              schedule: "schedule"
         

### Example
         
         cassandra:backup:
              enabled: true
              keyFile: "/Users/exampleuser/apigee-hybrid/hybrid-files/service-accounts/private.key"
              server: "34.56.78.90"
              storageDirectory: "/home/apigee/cassbackup"
              cloudProvider: "HYBRID"
              schedule: "0 2 * * *"
         

Where: 

Property | Description  
---|---  
`backup:enabled` | Backup is disabled by default. You must set this property to `true`  
path-to-private-key-file | The path on your local file system to the SSH private key file (named `ssh_key` in the step where you created the SSH key pair).  
backup-server-ip | The IP address of your backup server.  
backup-directory | The name of the backup directory on your backup server. This must be a directory within `home/apigee` (the backup directory is named `cassandra_backup` in the step where you created the backup directory).  
**`HYBRID`** | The `cloudProvider: "HYBRID"` property is required.  
schedule | The time when the backup starts, specified in [standard crontab syntax](https://en.wikipedia.org/wiki/Cron). Default: `0 2 * * *` **Note:** Avoid scheduling a backup that starts a short time after you apply the backup configuration to your cluster. When you apply the backup configuration, Kubernetes recreates the Cassandra nodes. If the backup starts before the nodes restart (possibly several minutes) the backup will fail.   
  2. Use `apigeectl` to apply the backup configuration to the storage scope of your cluster: 
         
         $APIGEECTL_HOME/apigeectl --datastore -f your-overrides-file

Where your-overrides-file is the path to the overrides file you just edited. 




###  Configure restore 

Restoration takes the data from the backup file with the timestamp you specify and restores it into a new Cassandra cluster with the same number of pods. The new cluster must have a namespace that is different than your runtime plane cluster. 

To restore Cassandra backups: 

  1. Create a new Kubernetes cluster with a new namespace. You cannot use the same cluster/namespace that you used for the original hybrid installation. 
  2. In the root hybrid installation directory, create a new `overrides-restore.yaml` file.
  3. Copy the complete Cassandra configuration from your original `overrides.yaml` file into the new one.
  4. Add the following parameters to your `overrides-restore.yaml` file: 

### Parameters
         
         namespace: restore-namespace
         
         cassandra:
           restore:
              enabled: true
              keyFile: "path-to-private-key-file"
              server: "backup-server-ip"
              storageDirectory: "/home/apigee/backup-directory"
              cloudProvider: "HYBRID"  # required verbatim "HYBRID" (all caps)
              snapshotTimestamp: "backup-to-restore"
         

### Example
         
         namespace: cassandra-restore
         
         cassandra:
           restore:
              enabled: true
              keyFile: "/Users/exampleuser/apigee-hybrid/hybrid-files/service-accounts/private.key"
              server: "34.56.78.90"
              storageDirectory: "/home/apigee/cassbackup"
              cloudProvider: "HYBRID"
              snapshotTimestamp: "20201001183903"
         

Where: 

Property | Description  
---|---  
restore-namespace | The name of the new namespace you for the new Cassandra cluster. Do not use the same namespace you used for your original cluster.  
`restore:enabled` | Restore is disabled by default. You must set this property to `true`  
path-to-private-key-file | The path on your local file system to the SSH private key file (named `ssh_key` in the step where you created the SSH key pair).  
backup-server-ip | The IP address of your backup server.  
backup-directory | The name of the backup directory on your backup server. This must be a directory within `home/apigee` (the backup directory is named `cassandra_backup` in the step where you created the backup directory).  
**`HYBRID`** | The `cloudProvider: "HYBRID"` property is required.  
backup-to-restore | The specific backup you want to restore, specified in [standard crontab syntax](https://en.wikipedia.org/wiki/Cron) (no wildcards allowed).   
  5. Use `apigeectl` to apply the backup configuration to the storage scope of your cluster: 
         
         $APIGEECTL_HOME/apigeectl --datastore -f your-overrides-restore-file

Where your-overrides-restore-file is the path to the `overrides-restore.yaml` file you just edited. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
