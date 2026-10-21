---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/instances/move/
title: gcloud beta spanner instances move \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:39:44.349535+00:00
---

# gcloud beta spanner instances move  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/instances/move/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta spanner instances move Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta spanner instances move - move the Cloud Spanner instance to the specified instance configuration 
SYNOPSIS
    

`gcloud beta spanner instances move` `INSTANCE` `--target-config`=`TARGET_CONFIG` [`--target-database-move-configs`=[^:^`database-id`=`DATABASE_ID`:`kms-key-names`=`KEY1`,`KEY2`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Move the Cloud Spanner instance to the specified instance configuration. 
EXAMPLES
     To move the Cloud Spanner instance, which has two CMEK-enabled databases db1 and db2 and a database db3 with Google-managed encryption keys, to the target instance configuration nam3 (us-east4, us-east1, us-central1), run:
    
    
    gcloud beta spanner instances move my-instance-id --target-config=nam3 --target-database-move-configs=^:^database-id=db1:kms-key-names=projects/myproject/locations/us-east4/keyRings/mykeyring/cryptoKeys/cmek-key,projects/myproject/locations/us-east1/keyRings/mykeyring/cryptoKeys/cmek-key,projects/myproject/locations/us-central1/keyRings/mykeyring/cryptoKeys/cmek-key --target-database-move-configs=^:^database-id=db2:kms-key-names=projects/myproject/locations/us-east4/keyRings/mykeyring/cryptoKeys/cmek-key,projects/myproject/locations/us-east1/keyRings/mykeyring/cryptoKeys/cmek-key,projects/myproject/locations/us-central1/keyRings/mykeyring/cryptoKeys/cmek-key

POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud Spanner instance ID. 
REQUIRED FLAGS
    

`--target-config`=`TARGET_CONFIG`
     Target Instance configuration to move the instances. 
OPTIONAL FLAGS
    

`--target-database-move-configs`=[^:^`database-id`=`DATABASE_ID`:`kms-key-names`=`KEY1`,`KEY2`,…]
     Database level configurations for each database to be moved. Currently only used for CMEK-enabled databases to specificy the target database KMS keys. Sets `target_database_move_configs` value. 

`database-id`
     Required, sets `database-id` value. 
`kms-key-names`
     Sets `kms-key-names` value. 
`Shorthand Example:`
    
    
    --target-database-move-configs=database-id=string,kms-key-names=string --target-database-move-configs=database-id=string,kms-key-names=string

`JSON Example:`
    
    
    --target-database-move-configs='[{"database-id": "string", "kms-key-names": "string"}]'

`File Example:`
    
    
    --target-database-move-configs=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud spanner instances move](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instances/move)
    
    
    [gcloud alpha spanner instances move](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/instances/move)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
