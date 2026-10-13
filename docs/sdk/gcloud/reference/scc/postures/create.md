---
url: https://docs.cloud.google.com/sdk/gcloud/reference/scc/postures/create/
title: gcloud scc postures create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:16.529597+00:00
---

# gcloud scc postures create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/scc/postures/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud scc postures create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud scc postures create - create a Cloud Security Command Center posture 
SYNOPSIS
    

`gcloud scc postures create` (`POSTURE` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) `--posture-from-file`=`PATH_TO_FILE` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Cloud Security Command Center (SCC) posture. First argument consists of the parent and name of the posture to be created. The posture details are provided in YAML file. The file path is mentioned in `--posture-from-file` flag. 

Created posture is returned as the response of the command. LRO operation ID is printed as the standard output. 

EXAMPLES
     Create a posture named `posture-foo-1` within parent `organizations/123/locations/global`(i.e. a posture in organization `123`, location `global`, with ID `posture-foo-1`): 
    
    
    gcloud scc postures create organizations/123/locations/global/postures/posture-foo-1 --posture-from-file=posture.yaml

POSITIONAL ARGUMENTS
    

Posture resource - The name of the posture to be created. For example organizations/<organizationID>/locations/<location>/postures/<postureID>. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`POSTURE`
     ID of the posture or fully qualified identifier for the posture. 

To set the `posture` attribute: 

  * provide the argument `posture` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     ID of the location where the resource exists (for example, global). To set the `location` attribute: 

  * provide the argument `posture` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     ID of the organization which is the parent of the resource. To set the `organization` attribute: 

  * provide the argument `posture` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. 


REQUIRED FLAGS
    

`--posture-from-file`=`PATH_TO_FILE`
     YAML file containing the body of the posture to be created. Use a full or relative path to a local file containing the value of posture. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `securityposture/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha scc postures create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/postures/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
