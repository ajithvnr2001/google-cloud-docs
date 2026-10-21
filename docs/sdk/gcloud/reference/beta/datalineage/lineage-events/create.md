---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/datalineage/lineage-events/create/
title: gcloud beta datalineage lineage-events create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:26:32.480598+00:00
---

# gcloud beta datalineage lineage-events create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/datalineage/lineage-events/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta datalineage lineage-events create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta datalineage lineage-events create - create a Data Lineage event 
SYNOPSIS
    

`gcloud beta datalineage lineage-events create` (`LINEAGE_EVENT` : `--location`=`LOCATION` `--process`=`PROCESS` `--run`=`RUN`) `--start-time`=`START_TIME` [`--end-time`=`END_TIME`] [`--links`=[`source`=`SOURCE`],[`target`=`TARGET`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a Data Lineage event. 
EXAMPLES
     To create a lineage event with ID `my-event` under run `my-run` and process `my-process`, run: 
    
    
    gcloud beta datalineage lineage-events create my-event --run=my-run --process=my-process --location=us-central1 --start-time="2026-06-19T10:00:00Z" --end-time="2026-06-19T10:30:00Z"

To record a lineage link with column-level details: 
    
    
    gcloud beta datalineage lineage-events create my-event --run=my-run --process=my-process --location=us-central1 --start-time="2026-06-19T10:00:00Z" --links="source={fullyQualifiedName=my_source_fqn,field=[col1]},target={fullyQualifiedName=my_target_fqn,field=[col2]}"

POSITIONAL ARGUMENTS
    

Lineage event resource - The lineage event to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `lineage_event` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`LINEAGE_EVENT`
     ID of the lineage_event or fully qualified identifier for the lineage_event. 

To set the `lineage_event` attribute: 

  * provide the argument `lineage_event` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the lineage_event. To set the `location` attribute: 

  * provide the argument `lineage_event` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--process`=`PROCESS`
     The name of the process. 

To set the `process` attribute: 

  * provide the argument `lineage_event` on the command line with a fully specified name; 
  * provide the argument `--process` on the command line. 


`--run`=`RUN`
     The name of the run. 

To set the `run` attribute: 

  * provide the argument `lineage_event` on the command line with a fully specified name; 
  * provide the argument `--run` on the command line. 


REQUIRED FLAGS
    

`--start-time`=`START_TIME`
     The start time of the lineage event. 
OPTIONAL FLAGS
    

`--end-time`=`END_TIME`
     The end time of the lineage event. 
`--links`=[`source`=`SOURCE`],[`target`=`TARGET`]
     A list of source-target links representing data lineage. 

`source`
     Required, The source entity. 

`field`
     The fields of the source entity. 
`fullyQualifiedName`
     Required, The fully qualified name of the source entity. 
`target`
     Required, The target entity. 

`field`
     The fields of the target entity. 
`fullyQualifiedName`
     Required, The fully qualified name of the target entity. 
`Shorthand Example:`
    
    
    --links=source={field=[string],fullyQualifiedName=string},target={field=[string],fullyQualifiedName=string} --links=source={field=[string],fullyQualifiedName=string},target={field=[string],fullyQualifiedName=string}

`JSON Example:`
    
    
    --links='[{"source": {"field": ["string"], "fullyQualifiedName": "string"}, "target": {"field": ["string"], "fullyQualifiedName": "string"}}]'

`File Example:`
    
    
    --links=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `datalineage/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/data-catalog>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud datalineage lineage-events create](https://docs.cloud.google.com/sdk/gcloud/reference/datalineage/lineage-events/create)
    
    
    [gcloud alpha datalineage lineage-events create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/datalineage/lineage-events/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
