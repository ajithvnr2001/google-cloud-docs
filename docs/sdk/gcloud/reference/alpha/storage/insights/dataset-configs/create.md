---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/insights/dataset-configs/create/
title: gcloud alpha storage insights dataset-configs create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:08.747456+00:00
---

# gcloud alpha storage insights dataset-configs create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/insights/dataset-configs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha storage insights dataset-configs create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha storage insights dataset-configs create - create a new dataset config for Insights 
SYNOPSIS
    

`gcloud alpha storage insights dataset-configs create` `DATASET_CONFIG_NAME` `--location`=`LOCATION` `--organization`=`SOURCE_ORG_NUMBER` `--retention-period-days`=`RETENTION_DAYS` (`--enable-organization-scope` | `--source-folders`=[`SOURCE_FOLDER_NUMBERS`,…] | `--source-folders-file`=`SOURCE_FOLDER_NUMBERS_IN_FILE` | `--source-projects`=[`SOURCE_PROJECT_NUMBERS`,…] | `--source-projects-file`=`SOURCE_PROJECT_NUMBERS_IN_FILE`) [`--activity-data-retention-period-days`=`ACTIVITY_DATA_RETENTION_DAYS`] [`--auto-add-new-buckets`] [`--description`=`DESCRIPTION`] [`--identity`=`IDENTITY_TYPE`; default=`"IDENTITY_TYPE_PER_CONFIG"`] [`--exclude-bucket-names`=[`BUCKETS_NAMES`,…] `--exclude-bucket-prefix-regexes`=[`BUCKETS_REGEXES`,…] | `--include-bucket-names`=[`BUCKETS_NAMES`,…] `--include-bucket-prefix-regexes`=[`BUCKETS_REGEXES`,…]] [`--exclude-source-locations`=[`LIST_OF_SOURCE_LOCATIONS`,…] | `--include-source-locations`=[`LIST_OF_SOURCE_LOCATIONS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new dataset config for Insights. 
EXAMPLES
     To create a dataset config with config name as "my_config" in location "us-central1" and project numbers "123456" and "456789" belonging to organization number "54321": 
    
    
    gcloud alpha storage insights dataset-configs create my_config --location=us-central1 --source-projects=123456,456789 --organization=54321 --retention-period-days=1

To create a dataset config that automatically adds new buckets into config: 
    
    
    gcloud alpha storage insights dataset-configs create my_config --location=us-central1 --source-projects=123456,456789 --organization=54321 --auto-add-new-buckets --retention-period-days=1

POSITIONAL ARGUMENTS
    

`DATASET_CONFIG_NAME`
     Provide human readable config name. 
REQUIRED FLAGS
    

`--location`=`LOCATION`
     Provide location of the dataset config. 
`--organization`=`SOURCE_ORG_NUMBER`
     Provide the source organization number. 
`--retention-period-days`=`RETENTION_DAYS`
     Provide retention period for the config. 
List of source options either source projects or source folders or enable organization scope. Refer [Dataset Configuration Properties](https://cloud.google.com/storage/docs/insights/datasets#dataset-config) for more details. 

Exactly one of these must be specified: 

`--enable-organization-scope`
     If passed, the dataset config will be enabled on the organization. 
Or at most one of these can be specified: 

List of source folder IDs or the file containing list of folder IDs. 
`--source-folders`=[`SOURCE_FOLDER_NUMBERS`,…]
     List of source folder IDs. 
`--source-folders-file`=`SOURCE_FOLDER_NUMBERS_IN_FILE`
     CSV formatted file containing source folder IDs, one per line. 
Or at most one of these can be specified: 

List of source project numbers or the file containing list of project numbers. 
`--source-projects`=[`SOURCE_PROJECT_NUMBERS`,…]
     List of source project numbers. 
`--source-projects-file`=`SOURCE_PROJECT_NUMBERS_IN_FILE`
     CSV formatted file containing source project numbers, one per line. 
OPTIONAL FLAGS
    

`--activity-data-retention-period-days`=`ACTIVITY_DATA_RETENTION_DAYS`
     Provide retention period for the activity data in the config. This overrides the retention period for activity data. Otherwise, the `retention_period_days` value is used for activity data as well. 
`--auto-add-new-buckets`
     Automatically include any new buckets created if they satisfy criteria defined in config settings. 
`--description`=`DESCRIPTION`
     Description for dataset config. 
`--identity`=`IDENTITY_TYPE`; default=`"IDENTITY_TYPE_PER_CONFIG"`
     The type of service account used in the dataset config. `IDENTITY_TYPE` must be one of: `IDENTITY_TYPE_PER_CONFIG`, `IDENTITY_TYPE_PER_PROJECT`. 
Specify the list of buckets to be included or excluded, both a list of bucket names and prefix regexes can be specified for either include or exclude buckets. 

At most one of these can be specified: 

Specify the list of buckets to be excluded. 
`--exclude-bucket-names`=[`BUCKETS_NAMES`,…]
     List of bucket names to be excluded. 
`--exclude-bucket-prefix-regexes`=[`BUCKETS_REGEXES`,…]
     List of bucket prefix regexes to be excluded. Allowed regex patterns are similar to those for the --include-bucket-prefix-regexes flag. 
Specify the list of buckets to be included. 
`--include-bucket-names`=[`BUCKETS_NAMES`,…]
     List of bucket names be included. 
`--include-bucket-prefix-regexes`=[`BUCKETS_REGEXES`,…]
     List of bucket prefix regexes to be included. The dataset config will include all the buckets that match with the prefix regex. Examples of allowed prefix regex patterns can be testbucket`*`, testbucket.`*`foo, testb.+foo`*` . It should follow syntax specified in google/re2 on GitHub. 
Specify the list of locations for source projects to be included or excluded from [available locations](https://cloud.google.com/storage/docs/locations#available-locations). 

At most one of these can be specified: 

`--exclude-source-locations`=[`LIST_OF_SOURCE_LOCATIONS`,…]
     List of locations for projects to be excluded. 
`--include-source-locations`=[`LIST_OF_SOURCE_LOCATIONS`,…]
     List of locations for projects to be included. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud storage insights dataset-configs create](https://docs.cloud.google.com/sdk/gcloud/reference/storage/insights/dataset-configs/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
