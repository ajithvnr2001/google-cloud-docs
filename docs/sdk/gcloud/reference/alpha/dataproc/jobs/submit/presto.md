---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/presto/
title: gcloud alpha dataproc jobs submit presto \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:32:04.915390+00:00
---

# gcloud alpha dataproc jobs submit presto  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/presto/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataproc jobs submit presto Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataproc jobs submit presto - submit a Presto job to a cluster 
SYNOPSIS
    

`gcloud alpha dataproc jobs submit presto` (`--cluster`=`CLUSTER` | `--cluster-labels`=[`KEY`=`VALUE`,…]) (`--execute`=`QUERY`, `-e` `QUERY` | `--file`=`FILE`, `-f` `FILE`) [`--async`] [`--bucket`=`BUCKET`] [`--client-tags`=[`CLIENT_TAG`,…]] [`--continue-on-failure`] [`--driver-log-levels`=[`PACKAGE`=`LEVEL`,…]] [`--driver-required-memory-mb`=`DRIVER_REQUIRED_MEMORY_MB`] [`--driver-required-vcores`=`DRIVER_REQUIRED_VCORES`] [`--labels`=[`KEY`=`VALUE`,…]] [`--max-failures-per-hour`=`MAX_FAILURES_PER_HOUR`] [`--max-failures-total`=`MAX_FAILURES_TOTAL`] [`--properties`=[`PARAM`=`VALUE`,…]] [`--properties-file`=`PROPERTIES_FILE`] [`--query-output-format`=`QUERY_OUTPUT_FORMAT`] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Submit a Presto job to a cluster 
EXAMPLES
     To submit a Presto job with a local script, run: 
    
    
    gcloud alpha dataproc jobs submit presto --cluster=my-cluster --file=my_script.R

To submit a Presto job with inline queries, run: 
    
    
    gcloud alpha dataproc jobs submit presto --cluster=my-cluster -e="SELECT * FROM foo WHERE bar > 2"

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--cluster`=`CLUSTER`
     The Dataproc cluster to submit the job to. 
`--cluster-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

Labels of Dataproc cluster on which to place the job. 

Exactly one of these must be specified: 

`--execute`=`QUERY`, `-e` `QUERY`
     A Presto query to execute. 
`--file`=`FILE`, `-f` `FILE`
     HCFS URI of file containing the Presto script to execute. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--bucket`=`BUCKET`
     The Cloud Storage bucket to stage files in. Defaults to the cluster's configured bucket. 
`--client-tags`=[`CLIENT_TAG`,…]
     A list of Presto client tags to attach to this query. 
`--continue-on-failure`
     Whether to continue if a query fails. 
`--driver-log-levels`=[`PACKAGE`=`LEVEL`,…]
     A list of package-to-log4j log level pairs to configure driver logging. For example: root=FATAL,com.example=INFO 
`--driver-required-memory-mb`=`DRIVER_REQUIRED_MEMORY_MB`
     The memory allocation requested by the job driver in megabytes (MB) for execution on the driver node group (it is used only by clusters with a driver node group). 
`--driver-required-vcores`=`DRIVER_REQUIRED_VCORES`
     The vCPU allocation requested by the job driver for execution on the driver node group (it is used only by clusters with a driver node group). 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--max-failures-per-hour`=`MAX_FAILURES_PER_HOUR`
     Specifies the maximum number of times a job can be restarted per hour in event of failure. Default is 0 (no retries after job failure). 
`--max-failures-total`=`MAX_FAILURES_TOTAL`
     Specifies the maximum total number of times a job can be restarted after the job fails. Default is 0 (no retries after job failure). 
`--properties`=[`PARAM`=`VALUE`,…]
     A list of key value pairs to set Presto session properties. 
`--properties-file`=`PROPERTIES_FILE`
     Path to a local file or a file in a Cloud Storage bucket containing configuration properties for the job. The client machine running this command must have read permission to the file. 

Specify properties in the form of property=value in the text file. For example: 
    
    
      # Properties to set for the job:
      key1=value1
      key2=value2
      # Comment out properties not used.
      # key3=value3

If a property is set in both `--properties` and `--properties-file`, the value defined in `--properties` takes precedence. 

`--query-output-format`=`QUERY_OUTPUT_FORMAT`
     The query output display format. See the Presto documentation for supported output formats. 
`--region`=`REGION`
     Dataproc region to use. Each Dataproc region constitutes an independent resource namespace constrained to deploying instances into Compute Engine zones inside the region. Overrides the default `dataproc/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud dataproc jobs submit presto](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/presto)
    
    
    [gcloud beta dataproc jobs submit presto](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/submit/presto)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
