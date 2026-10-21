---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/set-machine-type/
title: gcloud beta compute instances set-machine-type \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:09:51.805250+00:00
---

# gcloud beta compute instances set-machine-type  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/set-machine-type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute instances set-machine-type Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute instances set-machine-type - set machine type for Compute Engine virtual machines 
SYNOPSIS
    

`gcloud beta compute instances set-machine-type` `INSTANCE_NAME` [`--machine-type`=`MACHINE_TYPE`] [`--zone`=`ZONE`] [`--custom-cpu`=`CUSTOM_CPU` `--custom-memory`=`CUSTOM_MEMORY` : `--custom-extensions` `--custom-vm-type`=`CUSTOM_VM_TYPE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` ``gcloud beta compute instances set-machine-type`` lets you change the machine type of a virtual machine in the `TERMINATED` state (that is, a virtual machine instance that has been stopped). 

For example, if ``example-instance`` is a ``g1-small`` virtual machine currently in the `TERMINATED` state, running: 
    
    
    gcloud beta compute instances set-machine-type example-instance --zone us-central1-b --machine-type n1-standard-4

will change the machine type to ``n1-standard-4``, so that when you next start ``example-instance``, it will be provisioned as an ``n1-standard-4`` instead of a ``g1-small``. 

See <https://cloud.google.com/compute/docs/machine-types> for more information on machine types. 

EXAMPLES
     To change the machine type of a VM to `n1-standard-4`, run: 
    
    
    gcloud beta compute instances set-machine-type example-instance --zone=us-central1-b --machine-type=n1-standard-4

POSITIONAL ARGUMENTS
    

`INSTANCE_NAME`
     Name of the instance to operate on. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
FLAGS
    

`--machine-type`=`MACHINE_TYPE`
     Specifies the machine type used for the instances. To get a list of available machine types, run 'gcloud compute machine-types list'. Either this flag, \--custom-cpu, or --custom-memory must be specified. 
`--zone`=`ZONE`
     Zone of the instance to operate on. If not specified, you might be prompted to select a zone (interactive mode only). `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` attempts to identify the appropriate zone by searching for resources in your currently active project. If the zone cannot be determined, `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with all available Google Cloud Platform zones. 

To avoid prompting when this flag is omitted, the user can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

Custom machine type extensions. 
`--custom-cpu`=`CUSTOM_CPU`
     A whole number value specifying the number of cores that are needed in the custom machine type. 

For some machine types, shared-core values can also be used. For example, for E2 machine types, you can specify `micro`, `small`, or `medium`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--custom-memory`=`CUSTOM_MEMORY`
     A whole number value indicating how much memory is desired in the custom machine type. A size unit should be provided (eg. 3072MB or 9GB) - if no units are specified, GB is assumed. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--custom-extensions`
     Use the extended custom machine type. 
`--custom-vm-type`=`CUSTOM_VM_TYPE`
     Specifies a custom machine type. The default is `n1`. For more information about custom machine types, see: <https://cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types>
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute instances set-machine-type](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-machine-type)
    
    
    [gcloud alpha compute instances set-machine-type](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-machine-type)
    
    
    [gcloud preview compute instances set-machine-type](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/set-machine-type)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
