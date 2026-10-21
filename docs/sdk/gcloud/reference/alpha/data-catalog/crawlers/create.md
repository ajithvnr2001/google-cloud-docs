---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/data-catalog/crawlers/create/
title: gcloud alpha data-catalog crawlers create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:01:39.411222+00:00
---

# gcloud alpha data-catalog crawlers create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/data-catalog/crawlers/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha data-catalog crawlers create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha data-catalog crawlers create - create a new Data Catalog crawler 
SYNOPSIS
    

`gcloud alpha data-catalog crawlers create` `CRAWLER` (`--crawl-scope`=`CRAWL_SCOPE` : `--buckets`=[`BUCKET`,…]) (`--run-option`=`RUN_OPTION` : `--run-schedule`=`RUN_SCHEDULE`) [`--bundle-specs`=[`PATTERN`,…]] [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new Data Catalog crawler. 
EXAMPLES
     Create a project-scoped crawler: 
    
    
    gcloud alpha data-catalog crawlers create crawler1 --run-option=MANUAL --display-name=my-crawler --crawl-scope=PROJECT

Create a bucket-scoped crawler that runs weekly: 
    
    
    gcloud alpha data-catalog crawlers create crawler1 --display-name=my-crawler --crawl-scope=BUCKET --buckets="gs://bucket1,gs://bucket2,gs://bucket3" --run-option=SCHEDULED --run-schedule=WEEKLY

POSITIONAL ARGUMENTS
    

Crawler resource - The crawler to create. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `crawler` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CRAWLER`
     ID of the crawler or fully qualified identifier for the crawler. 

To set the `crawler` attribute: 

  * provide the argument `crawler` on the command line. 


REQUIRED FLAGS
    

Arguments to configure the crawler scope: 

This must be specified. 

`--crawl-scope`=`CRAWL_SCOPE`
     Scope of the crawler. `CRAWL_SCOPE` must be one of: 

`bucket`
     Directs the crawler to crawl specific buckets within the project that owns the crawler. 
`organization`
     Directs the crawler to crawl all the buckets of the projects in the organization that owns the crawler. 
`project`
     Directs the crawler to crawl all the buckets of the project that owns the crawler. 
This flag argument must be specified if any of the other arguments in this group are specified. 
`--buckets`=[`BUCKET`,…]
     A list of buckets to crawl. This argument should be provided if and only if `--crawl-scope=BUCKET` was specified. 
Arguments to configure the crawler run scheduling: 

This must be specified. 

`--run-option`=`RUN_OPTION`
     Run option of the crawler. `RUN_OPTION` must be one of: 

`manual`
     The crawler run will have to be triggered manually. 
`scheduled`
     The crawler will run automatically on a schedule. 
This flag argument must be specified if any of the other arguments in this group are specified. 
`--run-schedule`=`RUN_SCHEDULE`
     Schedule for the crawler run. This argument should be provided if and only if `--run-option=SCHEDULED` was specified. `RUN_SCHEDULE` must be one of: `daily`, `weekly`. 
OPTIONAL FLAGS
    

`--bundle-specs`=[`PATTERN`,…]
     A list of bundling specifications for the crawler. Bundling specifications direct the crawler to bundle files into filesets based on the patterns provided. 
`--description`=`DESCRIPTION`
     Textual description of the crawler. 
`--display-name`=`DISPLAY_NAME`
     Human-readable display name for the crawler. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `datacatalog/v1alpha3` API. The full documentation for this API can be found at: <https://cloud.google.com/data-catalog/docs/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
