---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/session-templates/import/
title: gcloud beta dataproc session-templates import \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:08:56.454847+00:00
---

# gcloud beta dataproc session-templates import  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/session-templates/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta dataproc session-templates import Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta dataproc session-templates import - import a session template 
SYNOPSIS
    

`gcloud beta dataproc session-templates import` (`SESSION_TEMPLATE` : `--location`=`LOCATION`) [`--source`=`SOURCE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` If the specified session template already exists, it will be overwritten. Otherwise, a new session template will be created. To edit an existing session template, you can export the session template to a file, edit its configuration, and then import the new configuration. 

This command does not allow output only fields, such as template id and resource name. It populates the id field based on the resource name specified as the first command line argument. 

EXAMPLES
     The following command creates or updates the contents of session template `example-session-template` based on a yaml file: 
    
    
    gcloud beta dataproc session-templates import example-session-template --source=saved-template.yaml

POSITIONAL ARGUMENTS
    

Session template resource - The session template to import. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `session_template` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SESSION_TEMPLATE`
     ID of the session template or fully qualified identifier for the session template. 

To set the `session_template` attribute: 

  * provide the argument `session_template` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Dataproc location for the session template. Each Dataproc location constitutes an independent resource namespace constrained to deploying instances into Compute Engine zones inside the location. Overrides the default `dataproc/location` property value for this command invocation. 

To set the `location` attribute: 

  * provide the argument `session_template` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `dataproc/location`. 


FLAGS
    

`--source`=`SOURCE`
     Path to a YAML file containing configuration export data. Alternatively, you may omit this flag to read from standard input. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
