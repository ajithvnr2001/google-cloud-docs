---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/get-serial-port-output/
title: gcloud compute instances get-serial-port-output \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:50.356533+00:00
---

# gcloud compute instances get-serial-port-output  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/get-serial-port-output/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute instances get-serial-port-output Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute instances get-serial-port-output - read output from a virtual machine instance's serial port 
SYNOPSIS
    

`gcloud compute instances get-serial-port-output` `INSTANCE_NAME` [`--port`=`PORT`] [`--start`=`START`] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     gcloud compute instances get-serial-port-output is used to get the output from a Compute Engine virtual machine's serial port. The serial port output from the virtual machine will be printed to standard output. This information can be useful for diagnostic purposes. 
EXAMPLES
     To get the output from instance's serial port, run: 
    
    
    gcloud compute instances get-serial-port-output example-instance --zone=us-central1-b

POSITIONAL ARGUMENTS
    

`INSTANCE_NAME`
     Name of the instance to operate on. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
FLAGS
    

`--port`=`PORT`
     Instances can support up to four serial port outputs, numbered 1 through 4. By default, this command will return the output of the first serial port. Setting this flag will return the output of the requested serial port. 
`--start`=`START`
     Specifies the byte index (zero-based) of the first byte you want returned. Use this flag if you want to continue getting the output from a previous request that was too long to return in one attempt. The last byte returned in a request will be reported on STDERR. 
`--zone`=`ZONE`
     Zone of the instance to operate on. If not specified, you might be prompted to select a zone (interactive mode only). `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` attempts to identify the appropriate zone by searching for resources in your currently active project. If the zone cannot be determined, `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with all available Google Cloud Platform zones. 

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
     These variants are also available: 
    
    
    [gcloud alpha compute instances get-serial-port-output](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/get-serial-port-output)
    
    
    [gcloud beta compute instances get-serial-port-output](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/get-serial-port-output)
    
    
    [gcloud preview compute instances get-serial-port-output](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/get-serial-port-output)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
