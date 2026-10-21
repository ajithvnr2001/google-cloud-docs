---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/pig/
title: gcloud beta dataproc workflow-templates add-job pig \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:08:59.065365+00:00
---

# gcloud beta dataproc workflow-templates add-job pig  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/workflow-templates/add-job/pig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta dataproc workflow-templates add-job pig Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta dataproc workflow-templates add-job pig - add a Pig job to the workflow template 
SYNOPSIS
    

`gcloud beta dataproc workflow-templates add-job pig` `--step-id`=`STEP_ID` (`--execute`=`QUERY`, `-e` `QUERY` | `--file`=`FILE`, `-f` `FILE`) (`--workflow-template`=`WORKFLOW_TEMPLATE` : `--region`=`REGION`) [`--continue-on-failure`] [`--driver-log-levels`=[`PACKAGE`=`LEVEL`,…]] [`--jars`=[`JAR`,…]] [`--labels`=[`KEY`=`VALUE`,…]] [`--params`=[`PARAM`=`VALUE`,…]] [`--properties`=[`PROPERTY`=`VALUE`,…]] [`--properties-file`=`PROPERTIES_FILE`] [`--start-after`=`STEP_ID`,[`STEP_ID`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Add a Pig job to the workflow template. 
EXAMPLES
     To add a Pig job executing query 'QUERY' to a the workflow template 'my-workflow-template' in region 'us-central1' with step-id 'my-step-id' , run: 
    
    
    gcloud beta dataproc workflow-templates add-job pig --step-id=my-step_id -e=QUERY --workflow-template=my-workflow-template --region=us-central1

REQUIRED FLAGS
    

`--step-id`=`STEP_ID`
     The step ID of the job in the workflow template. 
Exactly one of these must be specified: 

`--execute`=`QUERY`, `-e` `QUERY`
     A Pig query to execute as part of the job. 
`--file`=`FILE`, `-f` `FILE`
     HCFS URI of file containing Pig script to execute as the job. 
Template resource - The name of the workflow template to add job to. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--workflow-template` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--workflow-template`=`WORKFLOW_TEMPLATE`
     ID of the template or fully qualified identifier for the template. 

To set the `template` attribute: 

  * provide the argument `--workflow-template` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Dataproc region for the template. Each Dataproc region constitutes an independent resource namespace constrained to deploying instances into Compute Engine zones inside the region. Overrides the default `dataproc/region` property value for this command invocation. 

To set the `region` attribute: 

  * provide the argument `--workflow-template` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `dataproc/region`. 


OPTIONAL FLAGS
    

`--continue-on-failure`
     Whether to continue if a single query fails. 
`--driver-log-levels`=[`PACKAGE`=`LEVEL`,…]
     A list of package to log4j log level pairs to configure driver logging. For example: root=FATAL,com.example=INFO 
`--jars`=[`JAR`,…]
     Comma separated list of jar files to be provided to Pig and MR. May contain UDFs. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--params`=[`PARAM`=`VALUE`,…]
     A list of key value pairs to set variables in the Pig queries. 
`--properties`=[`PROPERTY`=`VALUE`,…]
     A list of key value pairs to configure Pig. 
`--properties-file`=`PROPERTIES_FILE`
     Path to a local file or a file in a Cloud Storage bucket containing configuration properties for the job. The client machine running this command must have read permission to the file. 

Specify properties in the form of property=value in the text file. For example: 
    
    
      # Properties to set for the job:
      key1=value1
      key2=value2
      # Comment out properties not used.
      # key3=value3

If a property is set in both `--properties` and `--properties-file`, the value defined in `--properties` takes precedence. 

`--start-after`=`STEP_ID`,[`STEP_ID`,…]
     (Optional) List of step IDs to start this job after. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud dataproc workflow-templates add-job pig](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/add-job/pig)
    
    
    [gcloud alpha dataproc workflow-templates add-job pig](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/workflow-templates/add-job/pig)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
