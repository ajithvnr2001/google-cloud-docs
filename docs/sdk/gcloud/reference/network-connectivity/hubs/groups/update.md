---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update/
title: gcloud network-connectivity hubs groups update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:52:22.658713+00:00
---

# gcloud network-connectivity hubs groups update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-connectivity hubs groups update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-connectivity hubs groups update - update a group 
SYNOPSIS
    

`gcloud network-connectivity hubs groups update` (`GROUP` : `--hub`=`HUB`) [`--async`] [`--description`=`DESCRIPTION`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--add-auto-accept-projects`=[`AUTO-ACCEPT-PROJECTS`,…] | `--clear-auto-accept-projects` | `--remove-auto-accept-projects`=[`AUTO-ACCEPT-PROJECTS`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update the details of a group. 
EXAMPLES
     To update the description of a group named ``my-group``, in the hub ``my-hub``, run: 
    
    
    gcloud network-connectivity hubs groups update my-group --hub=my-hub --description="new group description"

To add the project ``my-project`` to the auto-accept list of a group named ``my-group`` in the hub ``my-hub``, run: 
    
    
    gcloud network-connectivity hubs groups update my-group --hub=my-hub --add-auto-accept-projects=my-project

POSITIONAL ARGUMENTS
    

Group resource - Name of the group to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `group` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`GROUP`
     ID of the group or fully qualified identifier for the group. 

To set the `group` attribute: 

  * provide the argument `group` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--hub`=`HUB`
     The hub Id. 

To set the `hub` attribute: 

  * provide the argument `group` on the command line with a fully specified name; 
  * provide the argument `--hub` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     New description of the group. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

These flags modify the member auto-accept projects of this group. This controls the list of project ids or project numbers for which auto-accept is enabled for the group. 

At most one of these can be specified: 

`--add-auto-accept-projects`=[`AUTO-ACCEPT-PROJECTS`,…]
     Append the given values to the current auto-accept projects. 
`--clear-auto-accept-projects`
     Empty the current auto-accept projects. 
`--remove-auto-accept-projects`=[`AUTO-ACCEPT-PROJECTS`,…]
     Remove the given values from the current auto-accept projects. 
At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud network-connectivity hubs groups update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud network-connectivity hubs groups update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the networkconnectivity/v1 API. The full documentation for this API can be found at: <https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest>
NOTES
     This variant is also available: 
    
    
    [gcloud beta network-connectivity hubs groups update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/hubs/groups/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
