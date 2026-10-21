---
url: https://docs.cloud.google.com/looker/docs/changing-encryption-keys/
title: Changing Looker's encryption keys \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:01:29.230272+00:00
---

# Changing Looker's encryption keys  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/changing-encryption-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Changing Looker's encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Starting in Looker 22.8, the legacy 128-bit encryption is deprecated. Any customer-hosted instance that is running Looker 22.8 or later and that has not migrated to AES-256 GCM encryption will receive this error at startup: "This Looker instance must be migrated to GCM encryption using 'migrate_encryption'." 

For customer-hosted Looker instances that are running a version earlier than Looker 22.8, a known vulnerability exists in the legacy 128-bit encryption: Google strongly recommends that all customer-hosted instances [migrate to AES-256 GCM encryption](https://docs.cloud.google.com/looker/docs/migrating-to-aes-256-gcm-encryption).

Looker uses AES-256 Galois/Counter Mode (GCM) encryption to encrypt data internally. Every item of data is encrypted using a unique data key and contains a signed and versioned encryption envelope to guarantee verification. This mode requires the use of an external Customer Master Key (CMK). The CMK is used to derive, encrypt, and decrypt the Key Encryption Key (KEK), which in turn is used to derive, encrypt, and decrypt data keys.

Customer-hosted installations that are using legacy encryption must migrate their internal databases to AES-256 GCM encryption. New customer-hosted installations need to configure their installations for AES-256 GCM encryption. See the [Using AES-256 GCM encryption](https://docs.cloud.google.com/looker/docs/migrating-to-aes-256-gcm-encryption) documentation page for instructions on migrating or configuring your customer-hosted installation for AES-256 GCM encryption.

If you want to change your CMK, or if you want to move from a local key-based configuration to an AWS KMS configuration (or the reverse), you can do so by creating a new CMK and rekeying your AES-256 GCM encryption.

Rekeying is done offline, meaning that the Looker instance must be shut down. For clustered Looker instances, all nodes of the cluster must be shut down.

Rekeying invalidates the entire Looker on-disk cache, including the query result cache. As a result, after you complete a rekey and start up the instance, the client databases may experience higher than usual load.

To rekey AES-256 GCM encryption, perform the following procedures:

  1. Stop Looker and create a full backup
  2. Set `_SOURCE` and `_DESTINATION` environment variables
  3. Run the `rekey` command
  4. Set new environment variables
  5. Start Looker



## Stop Looker and create a full backup

Issue the following commands:
    
    
    cd looker
    ./looker stop
    tar -zcvf /tmp/looker-pre-encrypt.tar.gz  /home/lookerops/looker --exclude=.cache --exclude=log --exclude=.tmp --exclude=.snapshots --exclude=looker.jar --exclude=authorized_keys --exclude=dr-log --exclude=core
    

If you are running an [external MySQL database](https://docs.cloud.google.com/looker/docs/migrating-looker-backend-db-to-mysql) to store Looker application data, back up the database separately. If the database is a MySQL instance, take a snapshot. The database is relatively small, so it should only take a few minutes.

If Looker is clustered, make sure to stop every node before proceeding:
    
    
    cd looker
    ./looker stop
    

If any nodes are still running when you later issue the `rekey` command, the command will fail with the message, "There are other live nodes connected to this backend Looker database. If Looker was shutdown within the last minute, try again shortly, otherwise verify all nodes in the cluster are shut down."

## Set `_SOURCE` and `_DESTINATION` environment variables

When your Looker instance was initially [migrated to or configured for AES-256 GCM encryption](https://docs.cloud.google.com/looker/docs/migrating-to-aes-256-gcm-encryption), one or more environment variables were created that indicate where Looker can find your CMK. These variables differ depending on whether you are using AWS KMS.

The rekey operation uses additional environment variables, based on whether you are currently using AWS KMS, and whether you will use AWS KMS after the rekey operation. Environment variables with the suffix `_SOURCE` indicate where Looker can currently find your CMK, and environment variables with the suffix `_DESTINATION` indicate where Looker can find your CMK after the rekey operation.

### Setting `_SOURCE` variables

Perform one of the following procedures, depending on whether your current configuration uses AWS KMS.

#### If you are currently using AWS KMS

If you initially configured your encryption using AWS KMS, you created one or both of the following environment variables:

  * `LKR_AWS_CMK`: Stores the AWS `CMK_alias`.
  * `LKR_AWS_CMK_EC`: An optional variable that defines the encryption context used with AWS KMS keystores.



Recreate the environment variables:
    
    
    export LKR_AWS_CMK=alias/<CMK_alias>
    export LKR_AWS_CMK_EC=<encryption_context>
    

Then create the `_SOURCE` variables. Set the following new variables with the `_SOURCE` suffix:
    
    
    export LKR_AWS_CMK_SOURCE=alias/<CMK_alias>
    export LKR_AWS_CMK_EC_SOURCE=<encryption_context>
    

#### If you are not currently using AWS KMS

If you initially configured your encryption using a KMS other than AWS, you created one of the following environment variables, depending on whether you store your CMK in an environment variable or in a file on your instance:

  * `LKR_MASTER_KEY_ENV`: If you store your CMK in an environment variable, this stores your CMK.
  * `LKR_MASTER_KEY_FILE`: If you store your CMK in a file, this stores the path and filename of the file containing your CMK.



Recreate the environment variable used for your configuration:
    
    
    export LKR_MASTER_KEY_FILE=<path_to_key_file>
    

Or:
    
    
    export LKR_MASTER_KEY_ENV=<CMK_value>
    

Then create the `_SOURCE` variable.

If you store your CMK in a file, create the following variable:
    
    
    export LKR_MASTER_KEY_FILE_SOURCE=<path_to_key_file>
    

If you store your CMK in an environment variable, create the following variable:
    
    
    export LKR_MASTER_KEY_ENV_SOURCE=<CMK_value>
    

### Setting `_DESTINATION` variables

Perform one of the following procedures, depending on whether you will use AWS KMS after the rekey operation.

#### Your new configuration will use AWS KMS

If your new configuration will use AWS KMS, create the following environment variables to indicate the new CMK location:
    
    
    export LKR_AWS_CMK_DESTINATION=alias/<new_CMK_alias>
    export LKR_AWS_CMK_EC_DESTINATION=<new_encryption_context>
    

##### Your new configuration will not use AWS KMS

If your new configuration will not use AWS KMS, you have the option of using the `LKR_MASTER_KEY_FILE_DESTINATION` or `LKR_MASTER_KEY_ENV_DESTINATION` variables to specify the CMK destination.

If you want to store your CMK in a file, issue the following command:
    
    
    export LKR_MASTER_KEY_FILE_DESTINATION=<path_to_new_key_file>
    

Or, if you want to store your CMK using an environment variable, issue the following command:
    
    
    export LKR_MASTER_KEY_ENV_DESTINATION=<CMK_value>
    

### Run the `rekey` command

Issue the following command:
    
    
    ./looker rekey
    

> If your Looker instance starts with either the `-d <db.yaml>` or the `--internal-db-creds=<db.yaml>` [startup options](https://docs.cloud.google.com/looker/docs/startup-options), which provide a path to a YAML file with your database credentials, you will need to include the same option with the `rekey` command.
> 
> For example, `java -jar looker.jar rekey -d /path/file/db.yaml`.

### Set new environment variables

Set one or more of the following environment variables as appropriate for your new configuration.

If your new configuration uses AWS KMS:
    
    
    export LKR_AWS_CMK=alias/<new_CMK_alias>
    export LKR_AWS_CMK_EC=<new_encryption_context>
    

If your new configuration does not use AWS KMS and you store your CMK in an environment variable:
    
    
    export LKR_MASTER_KEY_ENV=<CMK_value>
    

If your new configuration does not use AWS KMS and you store your CMK in a file:
    
    
    export LKR_MASTER_KEY_FILE=<path_to_CMK_file>
    

If you moved from a locally stored key to AWS KMS or from AWS KMS to a locally stored key, you will have environment variables from your previous configuration that are unnecessary. Delete the old environment variables.

If you moved from a locally stored key to AWS KMS:
    
    
    unset LKR_MASTER_KEY_FILE
    

If you moved from AWS KMS to a locally stored key:
    
    
    unset LKR_AWS_CMK
    unset LKR_AWS_CMK_EC
    

### Start Looker

Issue the following command:
    
    
    ./looker start
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
