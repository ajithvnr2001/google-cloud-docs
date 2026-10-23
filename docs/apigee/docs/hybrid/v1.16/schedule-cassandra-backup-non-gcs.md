---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/schedule-cassandra-backup-non-gcs/
title: Scheduling backups in a remote server \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:06.238038+00:00
---

# Scheduling backups in a remote server  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/schedule-cassandra-backup-non-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Scheduling backups in a remote server Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/schedule-cassandra-backup-non-gcs.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/schedule-cassandra-backup-non-gcs.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/schedule-cassandra-backup-non-gcs.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/schedule-cassandra-backup-non-gcs.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/schedule-cassandra-backup-non-gcs.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/schedule-cassandra-backup-non-gcs.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/schedule-cassandra-backup-non-gcs.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/schedule-cassandra-backup-non-gcs.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/schedule-cassandra-backup-non-gcs.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/schedule-cassandra-backup-non-gcs.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/schedule-cassandra-backup-non-gcs.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/schedule-cassandra-backup-non-gcs.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/schedule-cassandra-backup-non-gcs.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/schedule-cassandra-backup-non-gcs.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/schedule-cassandra-backup-non-gcs.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/schedule-cassandra-backup-non-gcs.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/schedule-cassandra-backup-non-gcs.html)



This page describes how to schedule backups for Cassandra without the Cloud Storage. In this method, backups are stored on a remote server specified by you instead of a Cloud Storage bucket. Apigee uses SSH to communicate with the remote server.

You must schedule the backups as `cron` jobs. Once a backup schedule has been applied to your hybrid cluster, a Kubernetes backup job is periodically executed according to the schedule in the runtime plane. The job interacts with each Cassandra pod in your hybrid cluster to collect all the data, create an archive (compressed) file of the data, and send the archive to the server specified in your `overrides.yaml` file. 

**Note:** You must ensure there is enough space on the file system for the backups, and adjust the frequency of the backups to avoid unnecessarily filling the allotted storage space. Apigee does not dictate a retention policy for the backup files. You may want to create a retention policy for files appropriate to your installation. 

The following steps include common examples for completing specific tasks, like creating an SSH key pair. Use the methods that are appropriate to your installation. 

The procedure has the following parts: 

  * Set up the server and SSH
  * Set the schedule and destination for backup



###  Set up the server and SSH 

  1. Designate a Linux or Unix server for your backups. This server must be reachable using SSH from your Apigee hybrid runtime plane. It must have enough storage for your backups.
  2. Set up an SSH server on the server, or ensure that it has a secure SSH server configured. **Caution:** For security purposes, make sure your SSH server is up to date.
  3. Create an SSH key pair and store the private key file in a path that is accessible from your hybrid runtime plane. **You must use a blank password for your key pair or the backup will fail**. For example: 
         
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

Where: exampleuser@example.com is a string. Any string that follows `-C` in the `ssh-keygen` command becomes a comment included in the newly created `ssh` key. The input string can be any string. When you use an account name in the form of exampleuser@example.com, you can quickly identify which account goes with the key. 

  4. Create a user account on the backup server with the name `apigee`. Make sure the new `apigee` user has a home directory under `/home`.
  5. On the backup server, create an `.ssh` directory in the new `/home/apigee` directory.
  6. Copy the public key (`ssh_key.pub` in the previous example) into a file named `authorized_keys` in the new `/home/apigee/.ssh` directory. For example: 
         
         cd /home/apigee
         mkdir .ssh
         cd .ssh
         vi authorized_keys

  7. On your backup server, create a backup directory within the `/home/apigee/` directory. The backup directory can be any directory as long as the `apigee` user has access to it. For example: 
         
         cd /home/apigee
         mkdir cassandra-backup




###  Set the schedule and destination for backup 

You set the schedule and destination for backups in your `overrides.yaml` file. 

  1. Add the following parameters to your `overrides.yaml` file: 

### Parameters
         
         cassandra:
           backup:
             enabled: true
             keyFile: "PATH_TO_PRIVATE_KEY_FILE"
             server: "BACKUP_SERVER_IP"
             storageDirectory: "/home/apigee/BACKUP_DIRECTORY"
             cloudProvider: "HYBRID" # required verbatim "HYBRID" (all caps)
             schedule: "SCHEDULE"

### Example
         
         cassandra:
           backup:
             enabled: true
             keyFile: "private.key"# path relative to apigee-datastore path
             server: "34.56.78.90"
             storageDirectory: "/home/apigee/cassbackup"
             cloudProvider: "HYBRID"
             schedule: "0 2 * * *"

Where: 

Property | Description  
---|---  
`backup:enabled` | Backup is disabled by default. You must set this property to `true`.  
`backup:keyFile` | PATH_TO_PRIVATE_KEY_FILE The path on your local file system to the SSH private key file (named `ssh_key` in the step where you created the SSH key pair). This path must be relative to the `apigee-datastore` chart directory.  
`backup:server` | BACKUP_SERVER_IP The IP address of your backup server.  
`backup:storageDirectory` | BACKUP_DIRECTORY The name of the backup directory on your backup server. This must be a directory within `home/apigee` (the backup directory is named `cassandra_backup` in the step where you created the backup directory).  
`backup:cloudProvider` | **`HYBRID`** For a remote server backup, set the property to `HYBRID`.   
`backup:schedule` | SCHEDULE The time when the backup starts, specified in [standard crontab syntax](https://en.wikipedia.org/wiki/Cron). Times are in the local time zone of the Kubernetes cluster. Default: `0 2 * * *` **Note:** Avoid scheduling a backup that starts a short time after you apply the backup configuration to your cluster.   
  2. Apply the backup configuration to the storage scope of your cluster: 
         
         helm upgrade datastore apigee-datastore/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f OVERRIDES_FILE.yaml
         

Where OVERRIDES_FILE is the path to the overrides file you just edited.

  3. Verify the backup job. For example: 
         
         kubectl get cronjob -n APIGEE_NAMESPACE
         
         NAME                      SCHEDULE     SUSPEND   ACTIVE   LAST SCHEDULE   AGE
         apigee-cassandra-backup   33 * * * *   False     0        <none>          94s




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
