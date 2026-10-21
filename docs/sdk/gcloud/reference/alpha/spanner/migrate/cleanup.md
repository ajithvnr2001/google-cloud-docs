---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/migrate/cleanup/
title: gcloud alpha spanner migrate cleanup \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:51:38.623059+00:00
---

# gcloud alpha spanner migrate cleanup  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/migrate/cleanup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha spanner migrate cleanup Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha spanner migrate cleanup - cleanup migration resources given a data migration job id 
SYNOPSIS
    

`gcloud alpha spanner migrate cleanup` `--job-id`=`JOB_ID` `--target-profile`=`TARGET_PROFILE` [`--data-shard-ids`=`DATA_SHARD_IDS`] [`--dataflow`] [`--datastream`] [`--log-level`=`LOG_LEVEL`] [`--monitoring`] [`--pub-sub`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Cleanup migration resources given a data migration job id. 
EXAMPLES
     To cleanup resources for a data migration job, specify the jobId and the boolean flags for the resources that need to be cleaned up. For sharded migrations, specific data shard Ids can also be provided. 
    
    
    For a all shards of a sharded migration, or a non-sharded migration:
    gcloud alpha spanner migrate cleanup --job-id="XXX" --target-profile="XXX" --datastream --dataflow --pub-sub --monitoring
    
    
    For a subset of shards of a sharded migration:
    gcloud alpha spanner migrate cleanup --job-id="XXX" --data-shard-ids="lorem,epsum" --target-profile="XXX" --datastream --dataflow --pub-sub --monitoring

REQUIRED FLAGS
    

`--job-id`=`JOB_ID`
     The job Id of an existing migration job. 
`--target-profile`=`TARGET_PROFILE`
     Flag for specifying connection profile for target database (e.g., "dialect=postgresql)". 
OPTIONAL FLAGS
    

`--data-shard-ids`=`DATA_SHARD_IDS`
     Relevant to sharded migrations. Optional comma separated list of data shard Ids, if nothing is specified, all shards are cleaned up. 
`--dataflow`
     Cleanup dataflow resource(s). 
`--datastream`
     Cleanup datastream resource(s). 
`--log-level`=`LOG_LEVEL`
     To configure the log level for the execution (INFO, VERBOSE). 
`--monitoring`
     Cleanup monitoring dashboard(s). 
`--pub-sub`
     Cleanup pubsub resource(s). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
