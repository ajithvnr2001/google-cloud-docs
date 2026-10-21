---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/tpu-vm/service-identity/create/
title: gcloud alpha compute tpus tpu-vm service-identity create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:48:06.090610+00:00
---

# gcloud alpha compute tpus tpu-vm service-identity create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/tpu-vm/service-identity/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute tpus tpu-vm service-identity create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute tpus tpu-vm service-identity create - create a Cloud TPU VM service identity for a project 
SYNOPSIS
    

`gcloud alpha compute tpus tpu-vm service-identity create` [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Cloud TPU VM service identity for a project. 

The Cloud TPU VM creates a service identity (Google-owned service account) for management of resources when the first Cloud TPU VM is created in a project after TPU service activation. However, there are cases where the service identity may need to be created beforehand to grant specific IAM permissions to it, like access to a Google Cloud Storage bucket. This method generates the service account without need to first create a Cloud TPU VM. 

This command generates a service identity valid for Cloud TPU VMs across all zones in a project. The zone is required (either set in the gcloud config defaults, as an environment variable, or `--zone` flag), but the service identity generated will work across all Cloud TPU VM zones. 

EXAMPLES
     To generate a Cloud TPU VM service identity for a project (using zone `europe-west4-a`), run: 
    
    
    gcloud alpha compute tpus tpu-vm service-identity create --zone=europe-west4-a

FLAGS
    

Location resource - Zone to use for the request. 

If not specified, will use the value of the [compute/zone] property in the current gcloud configuration. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--zone` on the command line with a fully specified name; 
  * set the property `compute/zone` with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--zone`=`ZONE`
     ID of the location or fully qualified identifier for the location. 

To set the `zone` attribute: 

  * provide the argument `--zone` on the command line; 
  * set the property `compute/zone`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `tpu/v2alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/tpu/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud compute tpus tpu-vm service-identity create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/service-identity/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
