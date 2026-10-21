---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-from-file/
title: gcloud alpha compute instances update-from-file \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:31:43.148185+00:00
---

# gcloud alpha compute instances update-from-file  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/update-from-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute instances update-from-file Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute instances update-from-file - update a Compute Engine virtual machine instance using a configuration file 
SYNOPSIS
    

`gcloud alpha compute instances update-from-file` `INSTANCE_NAME` [`--clear-secure-tag`] [`--discard-local-ssd`] [`--minimal-action`=`MINIMAL_ACTION`] [`--most-disruptive-allowed-action`=`MOST_DISRUPTIVE_ALLOWED_ACTION`] [`--source`=`SOURCE`] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update a Compute Engine virtual machine instance using a configuration file. For more information, see <https://cloud.google.com/compute/docs/instances/update-instance-properties>. 
EXAMPLES
     A virtual machine instance can be updated by running: 
    
    
    gcloud alpha compute instances update-from-file my-instance --source=<path-to-file>

POSITIONAL ARGUMENTS
    

`INSTANCE_NAME`
     Name of the instance to update. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
FLAGS
    

`--clear-secure-tag`
     If specified, all secure tags bound to this instance will be removed. 
`--discard-local-ssd`
     If specified, all local SSDs data attached to this instance will be discarded. This is only used with most-disruptive-allowed-action set to RESTART. 
`--minimal-action`=`MINIMAL_ACTION`
     If specified, this action or higher level action is performed on the instance irrespective of what action is required for the update to take effect. If not specified, then Compute Engine acts based on the minimum action required. 
`--most-disruptive-allowed-action`=`MOST_DISRUPTIVE_ALLOWED_ACTION`
     If specified, Compute Engine returns an error if the update requires a higher action to be applied to the instance. If not specified, the default will be REFRESH. 
`--source`=`SOURCE`
     Path to a YAML file containing configuration export data. Alternatively, you may omit this flag to read from standard input. For a schema describing the export/import format, see: $CLOUDSDKROOT/lib/googlecloudsdk/schemas/compute/alpha/Instance.yaml. 
    
    
    Note: $CLOUDSDKROOT represents the Google Cloud CLI's installation directory.

`--zone`=`ZONE`
     Zone of the instance to update. If not specified, you might be prompted to select a zone (interactive mode only). `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` attempts to identify the appropriate zone by searching for resources in your currently active project. If the zone cannot be determined, `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with all available Google Cloud Platform zones. 

To avoid prompting when this flag is omitted, the user can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute instances update-from-file](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file)
    
    
    [gcloud beta compute instances update-from-file](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/update-from-file)
    
    
    [gcloud preview compute instances update-from-file](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/update-from-file)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
