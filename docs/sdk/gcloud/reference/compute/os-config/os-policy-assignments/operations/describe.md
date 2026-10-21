---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/operations/describe/
title: gcloud compute os-config os-policy-assignments operations describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:31:40.716384+00:00
---

# gcloud compute os-config os-policy-assignments operations describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/operations/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute os-config os-policy-assignments operations describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute os-config os-policy-assignments operations describe - describe an OS policy assignment operation 
SYNOPSIS
    

`gcloud compute os-config os-policy-assignments operations describe` (`OPERATION` : `--location`=`LOCATION` `--os-policy-assignment`=`OS_POLICY_ASSIGNMENT`) [`--endpoint-mode`=`ENDPOINT_MODE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describe an OS policy assignment 
EXAMPLES
    

To describe an operation with`operation-id` for an OS policy assignment `my-assignment` in location `us-central1-a`, run: 
    
    
    [gcloud compute os-config os-policy-assignments operations](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/operations) describe operation-id --location=us-central1-a --os-policy-assignment=my-assignment

You can also describe an operation by passing the full operation name: 
    
    
    [gcloud compute os-config os-policy-assignments operations](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/operations) describe projects/my-project/locations/us-central1-a/osPolicyAssignments/my-assignment/operations/operation-id

`

POSITIONAL ARGUMENTS
    

OS policy assignment operation resource - OS policy assignment data to describe. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `operation` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`OPERATION`
     ID of the OS policy assignment operation or fully qualified identifier for the OS policy assignment operation. 

To set the `operation` attribute: 

  * provide the argument `operation` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the OS policy assignment operation. To set the `location` attribute: 

  * provide the argument `operation` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `compute/zone`. 


`--os-policy-assignment`=`OS_POLICY_ASSIGNMENT`
     OS policy assignment. To set the `os-policy-assignment` attribute: 

  * provide the argument `operation` on the command line with a fully specified name; 
  * provide the argument `--os-policy-assignment` on the command line. 


FLAGS
    

`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `osconfig/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/compute/docs/osconfig/rest>
REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This variant is also available: 
    
    
    [gcloud alpha compute os-config os-policy-assignments operations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/os-config/os-policy-assignments/operations) describe

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
