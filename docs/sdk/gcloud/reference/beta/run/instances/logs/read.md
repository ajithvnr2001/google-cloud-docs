---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/instances/logs/read/
title: gcloud beta run instances logs read \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:22:44.152202+00:00
---

# gcloud beta run instances logs read  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/instances/logs/read/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta run instances logs read Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta run instances logs read - read logs for a Cloud Run instance 
SYNOPSIS
    

`gcloud beta run instances logs read` `INSTANCE` [`--freshness`=`FRESHNESS`; default="1d"] [`--log-filter`=`LOG_FILTER`] [`--order`=`ORDER`; default="desc"] [`--region`=`REGION`] [`--limit`=`LIMIT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` gcloud beta run instances logs read reads log entries. Log entries matching `--log-filter` are returned according to the specified --order. If the log entries come from multiple logs, then entries from different logs might be intermingled in the results. 
EXAMPLES
     To read log entries from for a Cloud Run instance, run: 
    
    
    gcloud beta run instances logs read my-instance

To read log entries with severity ERROR or higher, run: 
    
    
    gcloud beta run instances logs read my-instance --log-filter="severity>=ERROR"

To read log entries written in a specific time window, run: 
    
    
    gcloud beta run instances logs read my-instance --log-filter='timestamp<="2015-05-31T23:59:59Z" AND
     timestamp>="2015-05-31T00:00:00Z"'

To read up to 10 log entries in your instance payloads that include the word `SearchText` and format the output in `JSON` format, run: 
    
    
    gcloud beta run instances logs read my-instance --log-filter="textPayload:SearchText" --limit=10 --format=json

Detailed information about filters can be found at: <https://cloud.google.com/logging/docs/view/advanced_filters>

POSITIONAL ARGUMENTS
    

`INSTANCE`
     Name for a Cloud Run instance. 
FLAGS
    

`--freshness`=`FRESHNESS`; default="1d"
     Return entries that are not older than this value. Works only with DESC ordering and filters without a timestamp. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--log-filter`=`LOG_FILTER`
     Filter expression that specifies the log entries to return. Detailed information about filters can be found at: <https://cloud.google.com/logging/docs/view/logging-query-language>
`--order`=`ORDER`; default="desc"
     Ordering of returned log entries based on timestamp field. `ORDER` must be one of: `desc`, `asc`. 
`--region`=`REGION`
     Region in which the resource can be found. Alternatively, set the property [run/region]. 
LIST COMMAND FLAGS
    

`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha run instances logs read](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/instances/logs/read)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
