---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/submit/pyspark/
title: gcloud beta dataproc jobs submit pyspark \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:21:49.143583+00:00
---

# gcloud beta dataproc jobs submit pyspark  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/jobs/submit/pyspark/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta dataproc jobs submit pyspark Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta dataproc jobs submit pyspark - submit a PySpark job to a cluster 
SYNOPSIS
    

`gcloud beta dataproc jobs submit pyspark` `PY_FILE` (`--cluster`=`CLUSTER` | `--cluster-labels`=[`KEY`=`VALUE`,…]) [`--archives`=[`ARCHIVE`,…]] [`--async`] [`--bucket`=`BUCKET`] [`--driver-log-levels`=[`PACKAGE`=`LEVEL`,…]] [`--driver-required-memory-mb`=`DRIVER_REQUIRED_MEMORY_MB`] [`--driver-required-vcores`=`DRIVER_REQUIRED_VCORES`] [`--files`=[`FILE`,…]] [`--jars`=[`JAR`,…]] [`--labels`=[`KEY`=`VALUE`,…]] [`--max-failures-per-hour`=`MAX_FAILURES_PER_HOUR`] [`--max-failures-total`=`MAX_FAILURES_TOTAL`] [`--properties`=[`PROPERTY`=`VALUE`,…]] [`--properties-file`=`PROPERTIES_FILE`] [`--py-files`=[`PY_FILE`,…]] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`] [-- `JOB_ARGS` …]
DESCRIPTION
     `(BETA)` Submit a PySpark job to a cluster. 
EXAMPLES
     To submit a PySpark job with a local script and custom flags, run: 
    
    
    gcloud beta dataproc jobs submit pyspark --cluster=my-cluster my_script.py -- --custom-flag

To submit a Spark job that runs a script that is already on the cluster, run: 
    
    
    gcloud beta dataproc jobs submit pyspark --cluster=my-cluster file:///usr/lib/spark/examples/src/main/python/pi.py -- 100

POSITIONAL ARGUMENTS
    

`PY_FILE`
     Main .py file to run as the driver. 
[-- `JOB_ARGS` …]
     Arguments to pass to the driver. 

The '--' argument must be specified between gcloud specific args on the left and JOB_ARGS on the right. 

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--cluster`=`CLUSTER`
     The Dataproc cluster to submit the job to. 
`--cluster-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

Labels of Dataproc cluster on which to place the job. 

OPTIONAL FLAGS
    

`--archives`=[`ARCHIVE`,…]
     Comma separated list of archives to be extracted into the working directory of each executor. Must be one of the following file formats: .zip, .tar, .tar.gz, or .tgz. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--bucket`=`BUCKET`
     The Cloud Storage bucket to stage files in. Defaults to the cluster's configured bucket. 
`--driver-log-levels`=[`PACKAGE`=`LEVEL`,…]
     List of key value pairs to configure driver logging, where key is a package and value is the log4j log level. For example: root=FATAL,com.example=INFO 
`--driver-required-memory-mb`=`DRIVER_REQUIRED_MEMORY_MB`
     The memory allocation requested by the job driver in megabytes (MB) for execution on the driver node group (it is used only by clusters with a driver node group). 
`--driver-required-vcores`=`DRIVER_REQUIRED_VCORES`
     The vCPU allocation requested by the job driver for execution on the driver node group (it is used only by clusters with a driver node group). 
`--files`=[`FILE`,…]
     Comma separated list of files to be placed in the working directory of both the app driver and executors. 
`--jars`=[`JAR`,…]
     Comma separated list of jar files to be provided to the executor and driver classpaths. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--max-failures-per-hour`=`MAX_FAILURES_PER_HOUR`
     Specifies the maximum number of times a job can be restarted per hour in event of failure. Default is 0 (no retries after job failure). 
`--max-failures-total`=`MAX_FAILURES_TOTAL`
     Specifies the maximum total number of times a job can be restarted after the job fails. Default is 0 (no retries after job failure). 
`--properties`=[`PROPERTY`=`VALUE`,…]
     List of key value pairs to configure PySpark. For a list of available properties, see: <https://spark.apache.org/docs/latest/configuration.html#available-properties>. 
`--properties-file`=`PROPERTIES_FILE`
     Path to a local file or a file in a Cloud Storage bucket containing configuration properties for the job. The client machine running this command must have read permission to the file. 

Specify properties in the form of property=value in the text file. For example: 
    
    
      # Properties to set for the job:
      key1=value1
      key2=value2
      # Comment out properties not used.
      # key3=value3

If a property is set in both `--properties` and `--properties-file`, the value defined in `--properties` takes precedence. 

`--py-files`=[`PY_FILE`,…]
     Comma separated list of Python files to be provided to the job. Must be one of the following file formats ".py, .zip, or .egg". 
`--region`=`REGION`
     Dataproc region to use. Each Dataproc region constitutes an independent resource namespace constrained to deploying instances into Compute Engine zones inside the region. Overrides the default `dataproc/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud dataproc jobs submit pyspark](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit/pyspark)
    
    
    [gcloud alpha dataproc jobs submit pyspark](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/jobs/submit/pyspark)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
