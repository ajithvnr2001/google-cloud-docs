---
url: https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/update/
title: gcloud oracle-database autonomous-databases update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:43:31.862562+00:00
---

# gcloud oracle-database autonomous-databases update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/autonomous-databases/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud oracle-database autonomous-databases update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud oracle-database autonomous-databases update - update an AutonomousDatabase 
SYNOPSIS
    

`gcloud oracle-database autonomous-databases update` `AUTONOMOUS_DATABASE` [`--async`] [`--location`=`LOCATION`] [`--request-id`=`REQUEST_ID`] [`--clear-properties` `--properties-local-adg-auto-failover-max-data-loss-limit-duration`=`PROPERTIES_LOCAL_ADG_AUTO_FAILOVER_MAX_DATA_LOSS_LIMIT_DURATION` `--[no-]properties-local-data-guard-enabled` `--[no-]properties-refreshable-clone` `--encryption-key-provider`=`ENCRYPTION_KEY_PROVIDER` `--key-ring`=`KEY_RING` `--clear-encryption-key-kms` | `--encryption-key-kms`=`ENCRYPTION_KEY_KMS`] [`--labels`=[`LABELS`,…] | `--update-labels`=[`UPDATE_LABELS`,…] `--clear-labels` | `--remove-labels`=`REMOVE_LABELS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update an AutonomousDatabase. 
EXAMPLES
     To Update the encryption for a given AutonomousDatabase with id `my-autonomous-database` with custom KMS encryption key `projects/project-id/locations/us-east4/keyRings/keyring/cryptoKeys/key`, run: 
    
    
    gcloud oracle-database autonomous-databases update my-autonomous-database --location=us-east4 --encryption-key-provider=GOOGLE_MANAGED --encryption-key-kms=projects/project-id/locations/us-east4/keyRings/keyring/cryptoKeys/key

To enable Local Data Guard on an AutonomousDatabase with id `my-instance` in the location `us-east4` and set the auto failover max data loss limit to 0, run: 
    
    
    gcloud oracle-database autonomous-databases update my-instance --location=us-east4 --properties-local-data-guard-enabled=true --properties-local-adg-auto-failover-max-data-loss-limit-duration=0

To update Local Data Guard settings on an AutonomousDatabase with id `my-instance` in the location `us-east4` and set the auto failover max data loss limit to 60 seconds, run: 
    
    
    gcloud oracle-database autonomous-databases update my-instance --location=us-east4 --properties-local-adg-auto-failover-max-data-loss-limit-duration=60

To disable Local Data Guard on an AutonomousDatabase with id `my-instance` in the location `us-east4`, run: 
    
    
    gcloud oracle-database autonomous-databases update my-instance --location=us-east4 --properties-local-data-guard-enabled=false

POSITIONAL ARGUMENTS
    

AutonomousDatabase resource - Identifier. The name of the Autonomous Database resource in the following format: projects/{project}/locations/{region}/autonomousDatabases/{autonomous_database} This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `autonomous_database` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `autonomous_database` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`AUTONOMOUS_DATABASE`
     ID of the autonomousDatabase or fully qualified identifier for the autonomousDatabase. 

To set the `autonomous_database` attribute: 

  * provide the argument `autonomous_database` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--location`=`LOCATION`
     For resources [autonomous_database, encryption-key-kms], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
`--request-id`=`REQUEST_ID`
     An optional ID to identify the request. This value is used to identify duplicate requests. If you make a request with the same request ID and the original request is still in progress or completed, the server ignores the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

The properties of an Autonomous Database. 
`--clear-properties`
     Set autonomousDatabase.properties back to default value. 
Arguments for the local adg auto failover max data loss limit duration. 
`--properties-local-adg-auto-failover-max-data-loss-limit-duration`=`PROPERTIES_LOCAL_ADG_AUTO_FAILOVER_MAX_DATA_LOSS_LIMIT_DURATION`
     This field indicates the maximum data loss limit for an Autonomous Database, in seconds. 
Arguments for the local data guard enabled. 
`--[no-]properties-local-data-guard-enabled`
     Indicates whether the Autonomous Database has a local (in-region) standby database. Not applicable to cross-region Data Guard or dedicated Exadata infrastructure. Use `--properties-local-data-guard-enabled` to enable and `--no-properties-local-data-guard-enabled` to disable. 
Arguments for the refreshable clone. 
`--[no-]properties-refreshable-clone`
     Indicates if the Autonomous Database is a refreshable clone. This field is used in update flow to connect / disconnect a refreshable clone from its source database. Use `--properties-refreshable-clone` to enable and `--no-properties-refreshable-clone` to disable. 
The encryption key used to encrypt the Autonomous Database. 
`--encryption-key-provider`=`ENCRYPTION_KEY_PROVIDER`
     The provider of the encryption key. `ENCRYPTION_KEY_PROVIDER` must be one of: 

`google-managed`
     Google Managed KMS key, if selected, please provide the KMS key name. 
`oracle-managed`
     Oracle Managed. 
All arguments needed to update encryption_key_kms. 
`--key-ring`=`KEY_RING`
     The keyRing id of the cryptoKey resource. 

To set the `key-ring` attribute: 

  * provide the argument `--current` on the command line with a fully specified name; 
  * provide the argument `--key-ring` on the command line. 


Update encryption_key_kms. 

At most one of these can be specified: 

`--clear-encryption-key-kms`
     Clear encryption_key_kms value and set to null. 
CryptoKey resource - Set encryption_key_kms to new value. 

The KMS key used to encrypt the Autonomous Database. This field is required if the provider is GOOGLE_MANAGED. The name of the KMS key resource in the following format: `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--encryption-key-kms` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--encryption-key-kms` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



To set the `key-ring` attribute: 

  * provide the argument `--encryption-key-kms` on the command line with a fully specified name; 
  * provide the argument `--key-ring` on the command line. 


`--encryption-key-kms`=`ENCRYPTION_KEY_KMS`
     ID of the cryptoKey or fully qualified identifier for the cryptoKey. 

To set the `crypto-key` attribute: 

  * provide the argument `--encryption-key-kms` on the command line. 


Update labels. 

At most one of these can be specified: 

`--labels`=[`LABELS`,…]
     Set labels to new value. The labels or tags associated with the Autonomous Database. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --labels=string=string

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--update-labels`=[`UPDATE_LABELS`,…]
     Update labels value or add key value pair. The labels or tags associated with the Autonomous Database. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --update-labels=string=string

`JSON Example:`
    
    
    --update-labels='{"string": "string"}'

`File Example:`
    
    
    --update-labels=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-labels`
     Clear labels value and set to empty map. 
`--remove-labels`=`REMOVE_LABELS`
     Remove existing value from map labels. Sets `remove_labels` value. `Shorthand Example:`
    
    
    --remove-labels=string,string

`JSON Example:`
    
    
    --remove-labels=["string"]

`File Example:`
    
    
    --remove-labels=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `oracledatabase/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/oracle/database/docs>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
