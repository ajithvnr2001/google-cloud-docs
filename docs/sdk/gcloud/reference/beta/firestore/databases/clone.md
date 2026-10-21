---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/databases/clone/
title: gcloud beta firestore databases clone \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:16:56.955805+00:00
---

# gcloud beta firestore databases clone  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore/databases/clone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta firestore databases clone Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta firestore databases clone - clone a Google Cloud Firestore database from another 
SYNOPSIS
    

`gcloud beta firestore databases clone` `--destination-database`=`DESTINATION_DATABASE` `--snapshot-time`=`SNAPSHOT_TIME` `--source-database`=`SOURCE_DATABASE` [`--tags`=[`KEY`=`VALUE`,…]] [`--encryption-type`=`ENCRYPTION_TYPE` : `--kms-key-name`=`KMS_KEY_NAME`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To clone a database from another: 
    
    
    gcloud beta firestore databases clone --source-database=projects/PROJECT_ID/databases/SOURCE_DATABASE --snapshot-time=2025-05-26T10:20:00.00Z --destination-database=DATABASE_ID

To clone to a CMEK-enabled database: 
    
    
    gcloud beta firestore databases clone --source-database=projects/PROJECT_ID/databases/SOURCE_DATABASE --snapshot-time=2025-05-26T10:20:00.00Z --destination-database=DATABASE_ID --encryption-type=customer-managed-encryption --kms-key-name=projects/PROJECT_ID/locations/LOCATION_ID/keyRings/KEY_RING_ID/cryptoKeys/CRYPTO_KEY_ID

REQUIRED FLAGS
    

`--destination-database`=`DESTINATION_DATABASE`
     Destination database to clone to. Destination database will be created in the same location as the source database. 

This value should be 4-63 characters. Valid characters are /[a-z][0-9]-/ with first character a letter and the last a letter or a number. Must not be UUID-like /[0-9a-f]8(-[0-9a-f]4)3-[0-9a-f]12/. 

Using "(default)" database ID is also allowed. 

For example, to clone to database `testdb`: 
    
    
    gcloud beta firestore databases clone --destination-database=testdb

`--snapshot-time`=`SNAPSHOT_TIME`
     Snapshot time at which to clone. This must be a whole minute, in the past, and not earlier than the source database's earliest_version_time. Additionally, if older than one hour in the past, PITR must be enabled on the source database. 

For example, to restore from snapshot `2025-05-26T10:20:00.00Z` of source database `source-db`: 
    
    
    gcloud beta firestore databases clone --source-database=projects/PROJECT_ID/databases/source-db --snapshot-time=2025-05-26T10:20:00.00Z

`--source-database`=`SOURCE_DATABASE`
     The source database to clone from. 

For example, to clone from database source-db: 
    
    
    gcloud beta firestore databases clone --source-database=projects/PROJECT_ID/databases/source-db

OPTIONAL FLAGS
    

`--tags`=[`KEY`=`VALUE`,…]
     Tags to attach to the destination database. Example: \--tags=key1=value1,key2=value2 

For example, to attach tags to a database: 

$ --tags=key1=value1,key2=value2 

The encryption configuration of the new database being created from the database. If not specified, the same encryption settings as the database will be used. 

To create a CMEK-enabled database: 
    
    
    gcloud beta firestore databases clone --encryption-type=customer-managed-encryption --kms-key-name=projects/PROJECT_ID/locations/LOCATION_ID/keyRings/KEY_RING_ID/cryptoKeys/CRYPTO_KEY_ID

To create a Google-default-encrypted database: 
    
    
    gcloud beta firestore databases clone --encryption-type=google-default-encryption

To create a database using the same encryption settings as the database: 
    
    
    gcloud beta firestore databases clone --encryption-type=use-source-encryption

`--encryption-type`=`ENCRYPTION_TYPE`
     The encryption type of the destination database. `ENCRYPTION_TYPE` must be one of: `use-source-encryption`, `customer-managed-encryption`, `google-default-encryption`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--kms-key-name`=`KMS_KEY_NAME`
     The resource ID of a Cloud KMS key. If set, the database created will be a Customer-Managed Encryption Key (CMEK) database encrypted with this key. This feature is allowlist only in initial launch. 

Only a key in the same location as this database is allowed to be used for encryption. For Firestore's nam5 multi-region, this corresponds to Cloud KMS location us. For Firestore's eur3 multi-region, this corresponds to Cloud KMS location europe. See <https://cloud.google.com/kms/docs/locations>. 

This value should be the KMS key resource ID in the format of `projects/{project_id}/locations/{kms_location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`. How to retrieve this resource ID is listed at <https://cloud.google.com/kms/docs/getting-resource-ids#getting_the_id_for_a_key_and_version>. This flag must only be specified when encryption-type is `customer-managed-encryption`. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud firestore databases clone](https://docs.cloud.google.com/sdk/gcloud/reference/firestore/databases/clone)
    
    
    [gcloud alpha firestore databases clone](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firestore/databases/clone)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
