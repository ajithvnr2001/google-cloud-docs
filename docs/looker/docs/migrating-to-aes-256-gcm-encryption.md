---
url: https://docs.cloud.google.com/looker/docs/migrating-to-aes-256-gcm-encryption/
title: Migrating to AES-256 GCM encryption \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:35:15.559546+00:00
---

# Migrating to AES-256 GCM encryption  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/migrating-to-aes-256-gcm-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Migrating to AES-256 GCM encryption Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Starting in Looker 22.8, the legacy 128-bit encryption is deprecated. Any customer-hosted instance that is running Looker 22.8 or later and that has not migrated to AES-256 GCM encryption will receive this error at startup: "This Looker instance must be migrated to GCM encryption using 'migrate_encryption'."

For customer-hosted Looker instances that are running a version earlier than Looker 22.8, a known vulnerability exists in the legacy 128-bit encryption: Google strongly recommends that all customer-hosted instances migrate to AES-256 GCM encryption using the procedure described on this page.

Looker uses AES-256 Galois/Counter Mode (GCM) encryption to encrypt sensitive data that is stored internally, including:

  * Backups of Looker's internal database
  * Database and service connection information
  * User authentication information
  * User attribute values
  * Customer data that is cached or readied for delivery



For a detailed list of the data that Looker encrypts, [open a support request](http://console.cloud.google.com/support/cases).

Data is encrypted using a unique data key and contains a signed and versioned encryption envelope to guarantee verification. This mode requires the use of an external Customer Master Key (CMK). The CMK is used to derive, encrypt, and decrypt the Key Encryption Key (KEK), which in turn is used to derive, encrypt, and decrypt data keys.

Encryption is used only for Looker's internal database and cache. Customer databases are not affected by Looker's encryption in any way. In addition, only static data (data stored on disk) is encrypted in this manner.

Customer-hosted installations can use their own AWS KMS accounts or their own custom key management systems. All data keys and the KEK are encrypted and used internally on the customer-hosted Looker installation. If not using AWS KMS, the external CMK should be kept securely.

Existing customer-hosted installations that want to use GCM encryption need to migrate from the legacy encryption to the new GCM encryption. New customer-hosted installations require additional configuration for GCM encryption.

Follow the procedures in the following sections in order.

## Stopping Looker and creating a full backup

If you are migrating to GCM encryption from an existing Looker instance, be sure to create a full backup in case there is a problem with the encryption migration. If you are installing a new Looker instance, skip this section.

If you are using Looker's internal database:
    
    
    cd looker
    ./looker stop
    tar -zcvf /tmp/looker-pre-encrypt.tar.gz  /home/lookerops/looker --exclude=.cache --exclude=log --exclude=.tmp --exclude=.snapshots --exclude=looker.jar --exclude=authorized_keys --exclude=dr-log --exclude=core
    

If you are running an [external MySQL database](https://docs.cloud.google.com/looker/docs/migrating-looker-backend-db-to-mysql) to store Looker application data, back up the database separately. If the database is a MySQL instance, take a snapshot. The database is relatively small, so it should only take a few minutes. Then stop Looker.

If Looker is clustered, make sure to stop every node before proceeding:
    
    
    cd looker
    ./looker stop
    

If any nodes are still running when you later issue the migration command, the command will fail with the message, "There are other live nodes connected to this backend Looker database. If Looker was shutdown within the last minute, try again shortly, otherwise verify all nodes in the cluster are shut down."

## Generating a CMK

If you are using AWS KMS, [create a CMK](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) using either the AWS Management Console or the API.

If you are not using AWS KMS, generate a Base64, 32-byte CMK. You can store the CMK either in an environment variable or in a file.

  * To generate the CMK and store it in an environment variable, you can use the following command to generate the CMK:
        
        openssl rand -base64 32
        

After generating the CMK, copy it, and use the following command to store the CMK in the `LKR_MASTER_KEY_ENV` environment variable (where `<CMK_value>` is the CMK you generated with the previous command):
        
        export LKR_MASTER_KEY_ENV=<CMK_value>
        

If Looker is clustered, run the previous command on every node in the cluster.

  * To generate and store the CMK in a file, you can use the following command (where `<path_to_CMK_file>` is the path and filename to store the CMK):
        
        openssl rand -base64 32 > <path_to_key_file>
        




After generating the CMK file, set the key file permissions to current user read-only:
    
    
    chmod 0400 <path_to_key_file>
    

> After you have generated a CMK, be sure to store it in a safe and permanent location before continuing! Losing the CMK after encrypting the internal database can result in the loss of your instance.

## Creating an AWS IAM role

If you are not using AWS KMS, skip this section.

If you are using AWS KMS, Looker recommends that you [create a new IAM role](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#create-iam-role) that is unique for your CMK and [attach it with your Looker instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#attach-iam-role).

Following is an example IAM role that contains the minimum permissions required for your CMK:
    
    
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": "kms:GenerateRandom",
                "Resource": "*"
            },
            {
                "Sid": "VisualEditor1",
                "Effect": "Allow",
                "Action": [
                    "kms:Decrypt",
                    "kms:Encrypt",
                    "kms:Generate*",
                ],
                "Resource": "arn:aws:kms:*:*:key/*"
            }
        ]
    }
    

## Setting environment variables

If you are using AWS KMS, set the `AWS_REGION` environment variable to your AWS region, and the `LKR_AWS_CMK` environment variable to the alias of your CMK:
    
    
    export AWS_REGION=<AWS_region>
    export LKR_AWS_CMK=alias/<CMK_alias>
    

Optionally, you can also set the `LKR_AWS_CMK_EC` environment variable to set a custom [AWS encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html). If you do not set this environment variable, Looker will use the default encryption context, the string `Looker_Encryption_Context`.
    
    
    export LKR_AWS_CMK_EC=<My_Encryption_Context>
    

If you are not using AWS KMS, and you are storing your CMK in a file, set the `LKR_MASTER_KEY_FILE` environment variable to the path of the CMK file:
    
    
    export LKR_MASTER_KEY_FILE=<path_to_key_file>
    

If you are not using AWS KMS, and you are storing your CMK in an environment variable, set the `LKR_MASTER_KEY_ENV` environment variable to the value of the CMK:
    
    
    export LKR_MASTER_KEY_ENV=<CMK_value>
    

If Looker is clustered, run the previous command on every node in the cluster.

## Encrypting the internal database

If you are migrating an existing Looker instance to GCM encryption, migrate Looker's internal database and start Looker:
    
    
    java -jar looker.jar migrate_encryption
    ./looker  start
    

> If your Looker instance starts with either the `-d <db.yaml>` or the `--internal-db-creds=<db.yaml>` [startup options](https://docs.cloud.google.com/looker/docs/startup-options), which provide a path to a YAML file with your database credentials, you will need to include the same option with the `java -jar looker.jar migrate_encryption` command.
> 
> For example, `java -jar looker.jar migrate_encryption -d /path/file`.

If you are installing a new Looker instance, the encryption process will begin when you start the new Looker instance.

The encryption process usually takes less than a minute. Once Looker has started, you can verify the new encryption by searching for `GCM` in the Looker log:
    
    
    grep GCM log/looker.log
    
    2018-10-29 22:42:20.279 +0000 [INFO|007d0|crypt] :: Starting migration from AES-128-CBC Legacy to AES-GCM-256
    2018-10-29 22:42:20.468 +0000 [INFO|007d0|db:looker] :: (0.000152s) INSERT INTO "SETTING" ("KEY", "VALUE") VALUES
    

## Troubleshooting

This section lists some common errors and resolutions to those errors:

  * **Could not find task "migrate_encryption"** : Update your Looker instance to Looker 6.4.

  * **Looker can not start because: Missing backing keystore** : Looker cannot find the CMK. Check that the CMK path in the `LKR_MASTER_KEY_FILE` environment variable is correct.

  * **Looker can not start because: Size of the Master Key is invalid it must be 32 bytes however is X** : The CMK must be exactly 32 bytes in length.

  * **Looker can not start because: Permission for backing key file must be 0400, but is XXX**: The CMK file must be read-only with a `chmod` value of `0400`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
