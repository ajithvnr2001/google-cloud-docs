---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/batch/jobs/submit/
title: gcloud alpha batch jobs submit \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:28:11.775621+00:00
---

# gcloud alpha batch jobs submit  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/batch/jobs/submit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha batch jobs submit Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha batch jobs submit - submit a Batch job 
SYNOPSIS
    

`gcloud alpha batch jobs submit` [[`JOB`] `--location`=`LOCATION`] (`--config`=`PATH_TO_FILE` `--container-commands-file`=`CONTAINER_COMMANDS_FILE` `--container-entrypoint`=`CONTAINER_ENTRYPOINT` `--container-image-uri`=`CONTAINER_IMAGE_URI` | `--script-file-path`=`SCRIPT_FILE_PATH` | `--script-text`=`SCRIPT_TEXT`) [`--job-prefix`=`JOB_PREFIX`] [`--machine-type`=`MACHINE_TYPE`] [`--priority`=`PRIORITY`] [`--provisioning-model`=`PROVISIONING_MODEL`] [`--network`=`NETWORK` `--subnetwork`=`SUBNETWORK` : `--no-external-ip-address`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command creates and submits a Batch job. After you create and submit the job, Batch automatically queues, schedules, and executes it. 
EXAMPLES
     To submit a job with a sample JSON configuration file (config.json) and name `projects/foo/locations/us-central1/jobs/bar`, run: 
    
    
    gcloud alpha batch jobs submit projects/foo/locations/us-central1/jobs/bar --config=config.json

To submit a job with a sample YAML configuration file (config.yaml) and name projects/foo/locations/us-central1/jobs/bar, run: 
    
    
    gcloud alpha batch jobs submit projects/foo/locations/us-central1/jobs/bar --config=config.yaml

To submit a job through stdin with a sample job configuration and name `projects/foo/locations/us-central1/jobs/bar`, run: 
    
    
    gcloud alpha batch jobs submit projects/foo/locations/us-central1/jobs/bar --config=-
    
    
    then input json job config via stdin
    {
      job config
    }

To submit a job through HereDoc with a sample job configuration and name `projects/foo/locations/us-central1/jobs/bar`, run: 
    
    
    gcloud alpha batch jobs submit projects/foo/locations/us-central1/jobs/bar --config=- << EOF
    
    
    {
      job config
    }
    EOF

For details about how to define a job's configuration using JSON, see the projects.locations.jobs resource in the Batch API Reference. If you want to define a job's configuration using YAML, convert the JSON syntax to YAML. 

POSITIONAL ARGUMENTS
    

Job resource - The Batch job resource. If --location not specified,the current batch/location is used. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `JOB` on the command line with a fully specified name; 
  * job ID is optional and will be generated if not specified with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


[`JOB`]
     ID of the job or fully qualified identifier for the job. 

To set the `job` attribute: 

  * provide the argument `JOB` on the command line; 
  * job ID is optional and will be generated if not specified. 


`--location`=`LOCATION`
     Google Cloud location for the job. 

To set the `location` attribute: 

  * provide the argument `JOB` on the command line with a fully specified name; 
  * job ID is optional and will be generated if not specified with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `batch/location`. 


REQUIRED FLAGS
    

At least one of these must be specified: 

`--config`=`PATH_TO_FILE`
     The file path of the job config file in either JSON or YAML format. It also supports direct input from stdin with '-' or HereDoc (in shells with HereDoc support like Bash) with '- <<DELIMITER'. 

Use a full or relative path to a local file containing the value of config. 

Either specify the config file for the job or the first runnable in the task spec. Specify either a script file or container arguments for the first runnable in the task spec. 

At most one of these can be specified: 

Options to specify the container arguments for the first runnable in the task spec. 
`--container-commands-file`=`CONTAINER_COMMANDS_FILE`
     Overrides the `CMD` specified in the container. If there is an ENTRYPOINT (either in the container image or with the entrypoint field below) then commands are appended as arguments to the ENTRYPOINT. 
`--container-entrypoint`=`CONTAINER_ENTRYPOINT`
     Overrides the `ENTRYPOINT` specified in the container. 
`--container-image-uri`=`CONTAINER_IMAGE_URI`
     The URI to pull the container image from. 
Either specify a path to a script file to run or provide inline text to execute directly. 

At most one of these can be specified: 

`--script-file-path`=`SCRIPT_FILE_PATH`
     Path to script file to run as first runnable in task spec. File path should be a valid path on the instance volume. 
`--script-text`=`SCRIPT_TEXT`
     Text to run as first runnable in task spec. 
OPTIONAL FLAGS
    

`--job-prefix`=`JOB_PREFIX`
     Specify the job prefix. A job ID in the format of job prefix + %Y%m%d-%H%M%S will be generated. Note that job prefix cannot be specified while JOB ID positional argument is specified. 
`--machine-type`=`MACHINE_TYPE`
     Specify the Compute Engine machine type, for example, e2-standard-4. Currently only one machine type is supported. 
`--priority`=`PRIORITY`
     Job priority [0-99] 0 is the lowest priority. 
`--provisioning-model`=`PROVISIONING_MODEL`
     Specify the allowed provisioning model for the compute instances. `PROVISIONING_MODEL` must be one of: 

`SPOT`
     The SPOT VM provisioning model. Ideal for fault-tolerant workloads that can withstand preemption. 
`STANDARD`
     The STANDARD VM provisioning model 
`--network`=`NETWORK`
     The URL for the network resource. Must specify subnetwork as well if network is specified 
`--subnetwork`=`SUBNETWORK`
     The URL for the subnetwork resource. Must specify network as well if subnetwork is specified 
`--no-external-ip-address`
     Required if no external public IP address is attached to the VM. If no external public IP address, additional configuration is required to allow the VM to access Google Services. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud batch jobs submit](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit)
    
    
    [gcloud beta batch jobs submit](https://docs.cloud.google.com/sdk/gcloud/reference/beta/batch/jobs/submit)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
