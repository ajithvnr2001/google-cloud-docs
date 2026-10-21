---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/buckets/create/
title: gcloud alpha storage buckets create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:54:37.999592+00:00
---

# gcloud alpha storage buckets create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/buckets/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha storage buckets create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha storage buckets create - create buckets for storing objects 
SYNOPSIS
    

`gcloud alpha storage buckets create` `URL` [`URL` …] [`--additional-headers`=`HEADER`=`VALUE`] [`--default-encryption-key`=`DEFAULT_ENCRYPTION_KEY`, `-k` `DEFAULT_ENCRYPTION_KEY`] [`--default-storage-class`=`DEFAULT_STORAGE_CLASS`, `-c` `DEFAULT_STORAGE_CLASS`, `-s` `DEFAULT_STORAGE_CLASS`] [`--enable-hierarchical-namespace`] [`--enable-per-object-retention`] [`--encryption-enforcement-file`=`ENCRYPTION_ENFORCEMENT_FILE`] [`--ip-filter-file`=`IP_FILTER_FILE`] [`--lifecycle-file`=`LIFECYCLE_FILE`] [`--location`=`LOCATION`, `-l` `LOCATION`] [`--[no-]pap`, `--[no-]public-access-prevention`] [`--placement`=[`REGION`,…]] [`--recovery-point-objective`=`SETTING`, `--rpo`=`SETTING`] [`--retention-period`=`RETENTION_PERIOD`] [`--soft-delete-duration`=`SOFT_DELETE_DURATION`] [`--[no-]uniform-bucket-level-access`, `-b`] [`--autoclass-terminal-storage-class`=`AUTOCLASS_TERMINAL_STORAGE_CLASS` `--[no-]enable-autoclass`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create new buckets. 
EXAMPLES
     The following command creates 2 Cloud Storage buckets, one named ``my-bucket`` and a second bucket named ``my-other-bucket``: 
    
    
    gcloud alpha storage buckets create gs://my-bucket gs://my-other-bucket

The following command creates a bucket with the ``nearline`` default [storage class](https://cloud.google.com/storage/docs/storage-classes) in the ``asia`` [location](https://cloud.google.com/storage/docs/locations): 
    
    
    gcloud alpha storage buckets create gs://my-bucket --default-storage-class=nearline --location=asia

POSITIONAL ARGUMENTS
    

`URL` [`URL` …]
     The URLs of the buckets to create. 
FLAGS
    

`--additional-headers`=`HEADER`=`VALUE`
     Includes arbitrary headers in storage API calls. Accepts a comma separated list of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides the default `storage/additional_headers` property value for this command invocation. 
`--default-encryption-key`=`DEFAULT_ENCRYPTION_KEY`, `-k` `DEFAULT_ENCRYPTION_KEY`
     Set the default KMS key using the full path to the key, which has the following form: ``projects/[project-id]/locations/[location]/keyRings/[key-ring]/cryptoKeys/[my-key]``. 
`--default-storage-class`=`DEFAULT_STORAGE_CLASS`, `-c` `DEFAULT_STORAGE_CLASS`, `-s` `DEFAULT_STORAGE_CLASS`
     Default [storage class](https://cloud.google.com/storage/docs/storage-classes) for the bucket. If not specified, the default storage class used by Cloud Storage is "Standard". 
`--enable-hierarchical-namespace`
     Enable hierarchical namespace for the bucket. To use this flag, you must also use --uniform-bucket-level-access 
`--enable-per-object-retention`
     Enables each object in the bucket to have its own retention settings, which prevents deletion until stored for a specific length of time. 
`--encryption-enforcement-file`=`ENCRYPTION_ENFORCEMENT_FILE`
     Sets the encryption enforcement configuration for the bucket from a JSON file. This configuration determines restrictions on the types of encryption (GMEK, CMEK, CSEK) allowed for new objects created in the bucket. 

The JSON file should contain an object with keys among "gmekEnforcement", "cmekEnforcement", and "csekEnforcement". Each of these keys, if present, should have a "restrictionMode" key, determining whether the corresponding encryption type should be allowed or restricted for new objects. 

Valid values for "restrictionMode" are: 

  * "NotRestricted": The encryption type is allowed for new objects. 
  * "FullyRestricted": The encryption type is not allowed for new objects. 



Example JSON file content, to enforce only CMEK for new objects: 
    
    
    {
      "gmekEnforcement": {
        "restrictionMode": "FullyRestricted"
      },
      "cmekEnforcement": {
        "restrictionMode": "NotRestricted"
      },
      "csekEnforcement": {
        "restrictionMode": "FullyRestricted"
      }
    }

Omitted keys will not be sent in the API request. To clear restrictions for a specific encryption-type during an update, set its "restrictionMode" to "NotRestricted". For example, to clear any restrictions on GMEK: { "gmekEnforcement": { "restrictionMode": "NotRestricted" } } 

`--ip-filter-file`=`IP_FILTER_FILE`
     Sets the IP filter for the bucket. The IP filter is a list of ip ranges that are allowed to access the bucket. For example, The following JSON document shows the IP filter configuration with mode enabled and list of public network sources and vpc network sources: 
    
    
    {
      "mode": "Enabled",
      "publicNetworkSource": { "allowedIpCidrRanges": ["0.0.0.0/0"] },
      "vpcNetworkSources": [
          {
              "network": "projects/PROJECT_NAME/global/networks/NETWORK_NAME",
              "allowedIpCidrRanges": ["0.0.0.0/0"]
          },
      ]
    }

For more information about supported configurations, see [Cloud Storage bucket IP filtering configurations](https://cloud.google.com/storage/docs/create-ip-filter#ip-filtering-configurations)

`--lifecycle-file`=`LIFECYCLE_FILE`
     Sets the lifecycle management configuration on a bucket. For example, The following lifecycle management configuration JSON document specifies that all objects in this bucket that are more than 365 days old are deleted automatically: 
    
    
    {
      "rule":
      [
        {
          "action": {"type": "Delete"},
          "condition": {"age": 365}
        }
      ]
    }

`--location`=`LOCATION`, `-l` `LOCATION`
     [Location](https://cloud.google.com/storage/docs/locations) for the bucket. If not specified, the location used by Cloud Storage is ``us``. A bucket's location cannot be changed after creation. 
`--[no-]pap`, `--[no-]public-access-prevention`
     Sets public access prevention to "enforced". For details on how exactly public access is blocked, see: <http://cloud.google.com/storage/docs/public-access-prevention>. Use `--public-access-prevention` to enable and `--no-public-access-prevention` to disable. 
`--placement`=[`REGION`,…]
     A comma-separated list of regions that form the custom [dual-region](https://cloud.google.com/storage/docs/locations#location-dr). Only regions within the same continent are or will ever be valid. Invalid location pairs (such as mixed-continent, or with unsupported regions) will return an error. 
`--recovery-point-objective`=`SETTING`, `--rpo`=`SETTING`
     Sets the [recovery point objective](https://cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning) of a bucket. This flag can only be used with multi-region and dual-region buckets. `DEFAULT` option is valid for multi-region and dual-regions buckets. `ASYNC_TURBO` option is only valid for dual-region buckets. If unspecified when the bucket is created, it defaults to `DEFAULT` for dual-region and multi-region buckets. For more information, see [replication in Cloud Storage](https://cloud.google.com/storage/docs/availability-durability#cross-region-redundancy). `SETTING` must be one of: `ASYNC_TURBO`, `DEFAULT`. 
`--retention-period`=`RETENTION_PERIOD`
     Minimum [retention period](https://cloud.google.com/storage/docs/bucket-lock#retention-periods) for objects stored in the bucket, for example ``\--retention-period=P1Y1M1DT5S``. Objects added to the bucket cannot be deleted until they've been stored for the specified length of time. Default is no retention period. Only available for Cloud Storage using the JSON API. 
`--soft-delete-duration`=`SOFT_DELETE_DURATION`
     Duration to retain soft-deleted objects. For example, "2w1d" is two weeks and one day. See `[gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for more information on the duration format. Setting `0` will disable soft delete policy on the bucket. Default is 7 days. 
`--[no-]uniform-bucket-level-access`, `-b`
     Turns on uniform bucket-level access setting. Default is False. Use `--uniform-bucket-level-access` to enable and `--no-uniform-bucket-level-access` to disable. 
AUTOCLASS FLAGS
    

`--autoclass-terminal-storage-class`=`AUTOCLASS_TERMINAL_STORAGE_CLASS`
     The storage class that objects in the bucket eventually transition to if they are not read for a certain length of time. Only valid if Autoclass is enabled. 
`--[no-]enable-autoclass`
     The Autoclass feature automatically selects the best storage class for objects based on access patterns. Use `--enable-autoclass` to enable and `--no-enable-autoclass` to disable. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud storage buckets create](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
