---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/batches/submit/spark-sql/
title: gcloud beta dataproc batches submit spark-sql \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:08:51.893712+00:00
---

# gcloud beta dataproc batches submit spark-sql  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/batches/submit/spark-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta dataproc batches submit spark-sql Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta dataproc batches submit spark-sql - submit a Spark SQL batch job 
SYNOPSIS
    

`gcloud beta dataproc batches submit spark-sql` `SQL_SCRIPT` [`--async`] [`--batch`=`BATCH`] [`--container-image`=`CONTAINER_IMAGE`] [`--deps-bucket`=`DEPS_BUCKET`] [`--history-server-cluster`=`HISTORY_SERVER_CLUSTER`] [`--jars`=[`JAR`,…]] [`--kms-key`=`KMS_KEY`] [`--labels`=[`KEY`=`VALUE`,…]] [`--metastore-service`=`METASTORE_SERVICE`] [`--properties`=[`PROPERTY`=`VALUE`,…]] [`--region`=`REGION`] [`--request-id`=`REQUEST_ID`] [`--resource-manager-tag`=`KEY`=`VALUE`] [`--service-account`=`SERVICE_ACCOUNT`] [`--staging-bucket`=`STAGING_BUCKET`] [`--tags`=[`TAGS`,…]] [`--ttl`=`TTL`] [`--user-workload-authentication-type`=`USER_WORKLOAD_AUTHENTICATION_TYPE`] [`--vars`=[`NAME`=`VALUE`,…]] [`--version`=`VERSION`] [`--network`=`NETWORK` | `--subnet`=`SUBNET`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Submit a Spark SQL batch job. 
EXAMPLES
     To submit a Spark SQL job running "my-sql-script.sql" and upload it to "gs://my-bucket", run: 
    
    
    gcloud beta dataproc batches submit spark-sql my-sql-script.sql --deps-bucket=gs://my-bucket --region=us-central1 --vars="NAME=VALUE,NAME2=VALUE2"

POSITIONAL ARGUMENTS
    

`SQL_SCRIPT`
     URI of the script that contains Spark SQL queries to execute. 
FLAGS
    

`--async`
     Return immediately without waiting for the operation in progress to complete. 
`--batch`=`BATCH`
     The ID of the batch job to submit. The ID must contain only lowercase letters (a-z), numbers (0-9) and hyphens (-). The length of the name must be between 4 and 63 characters. If this argument is not provided, a random generated UUID will be used. 
`--container-image`=`CONTAINER_IMAGE`
     Optional custom container image to use for the batch/session runtime environment. If not specified, a default container image will be used. The value should follow the container image naming format: {registry}/{repository}/{name}:{tag}, for example, gcr.io/my-project/my-image:1.2.3 
`--deps-bucket`=`DEPS_BUCKET`
     A Cloud Storage bucket to upload workload dependencies. 
`--history-server-cluster`=`HISTORY_SERVER_CLUSTER`
     Spark History Server configuration for the batch/session job. Resource name of an existing Dataproc cluster to act as a Spark History Server for the workload in the format: "projects/{project_id}/regions/{region}/clusters/{cluster_name}". 
`--jars`=[`JAR`,…]
     Comma-separated list of jar files to be provided to the classpaths. 
`--kms-key`=`KMS_KEY`
     Cloud KMS key to use for encryption. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--metastore-service`=`METASTORE_SERVICE`
     Name of a Dataproc Metastore service to be used as an external metastore in the format: "projects/{project-id}/locations/{region}/services/{service-name}". 
`--properties`=[`PROPERTY`=`VALUE`,…]
     Specifies configuration properties for the workload. See [Dataproc Serverless for Spark documentation](https://cloud.google.com/dataproc-serverless/docs/concepts/properties) for the list of supported properties. 
Region resource - Dataproc region to use. Each Dataproc region constitutes an independent resource namespace constrained to deploying instances into Compute Engine zones inside the region. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--region` on the command line with a fully specified name; 
  * set the property `dataproc/region` with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--region`=`REGION`
     ID of the region or fully qualified identifier for the region. 

To set the `region` attribute: 

  * provide the argument `--region` on the command line; 
  * set the property `dataproc/region`. 


`--request-id`=`REQUEST_ID`
     A unique ID that identifies the request. If the service receives two batch create requests with the same request_id, the second request is ignored and the operation that corresponds to the first batch created and stored in the backend is returned. Recommendation: Always set this value to a UUID. The value must contain only letters (a-z, A-Z), numbers (0-9), underscores (`), and hyphens (-). The maximum length is 40 characters. `
`--resource-manager-tag`=KEY`=`VALUE``
     Resource Manager Tags to be associated with the compute resources created for the workload. Only one key-value pair can be specified per flag. Repeat the flag to specify multiple tags. 
`--service-account`=SERVICE_ACCOUNT``
     The IAM service account to be used for a batch/session job. 
`--staging-bucket`=STAGING_BUCKET``
     The Cloud Storage bucket to use to store job dependencies, config files, and job driver console output. If not specified, the default [staging bucket] (https://cloud.google.com/dataproc-serverless/docs/concepts/buckets) is used. 
`--tags`=[TAGS`,…]`
     Network tags for traffic control. 
`--ttl`=TTL``
     The duration after the workload will be unconditionally terminated, for example, '20m' or '1h'. Run [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--user-workload-authentication-type`=USER_WORKLOAD_AUTHENTICATION_TYPE``
     Whether to use END_USER_CREDENTIALS or SERVICE_ACCOUNT to run the workload. 
`--vars`=[NAME`=`VALUE`,…]`
     Mapping of query variable names to values (equivalent to the Spark SQL command: SET name="value";). 
`--version`=VERSION``
     Optional runtime version. If not specified, a default version will be used. 
At most one of these can be specified: 

`--network`=NETWORK``
     Network URI to connect network to. 
`--subnet`=SUBNET``
     Subnetwork URI to connect network to. Subnet must have Private Google Access enabled. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud dataproc batches submit spark-sql](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit/spark-sql)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
