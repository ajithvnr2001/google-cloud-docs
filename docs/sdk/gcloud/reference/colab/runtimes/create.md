---
url: https://docs.cloud.google.com/sdk/gcloud/reference/colab/runtimes/create/
title: gcloud colab runtimes create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:16.434388+00:00
---

# gcloud colab runtimes create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/colab/runtimes/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud colab runtimes create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud colab runtimes create - create a notebook runtime 
SYNOPSIS
    

`gcloud colab runtimes create` `--display-name`=`DISPLAY_NAME` `--runtime-template`=`RUNTIME_TEMPLATE` [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`--region`=`REGION`] [`--runtime-id`=`RUNTIME_ID`] [`--runtime-user`=`RUNTIME_USER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a notebook runtime that can be used to run code from your notebook (IPYNB file). 
EXAMPLES
     To create a runtime in region 'us-central1' with the display name 'my-runtime' and template with id 'my-template', run: 
    
    
    gcloud colab runtimes create --region=us-central1 --display-name=my-runtime --runtime-template=my-template

To create a runtime for user 'USER@DOMAIN.COM', run: 
    
    
    gcloud colab runtimes create --runtime-user=USER@DOMAIN.COM --region=us-central1 --display-name=my-runtime --runtime-template=my-template

REQUIRED FLAGS
    

`--display-name`=`DISPLAY_NAME`
     The display name of the runtime to create. 
Runtime template resource - Unique name of the runtime template to configure the runtime with. This was optionally provided by setting --runtime-template-id in the create runtime-template command, or was system-generated if unspecified. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--runtime-template` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `region` attribute: 

  * provide the argument `--runtime-template` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `colab/region`. 



This must be specified. 

`--runtime-template`=`RUNTIME_TEMPLATE`
     ID of the runtime template or fully qualified identifier for the runtime template. 

To set the `name` attribute: 

  * provide the argument `--runtime-template` on the command line. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     The description 
`--labels`=[`KEY`=`VALUE`,…]
     Add labels to identify and group the runtime template. 
Region resource - Cloud region to create runtime. Please see <https://cloud.google.com/colab/docs/locations> for a list of supported regions. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--region` on the command line with a fully specified name; 
  * set the property `colab/region` with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--region`=`REGION`
     ID of the region or fully qualified identifier for the region. 

To set the `region` attribute: 

  * provide the argument `--region` on the command line; 
  * set the property `colab/region`. 


`--runtime-id`=`RUNTIME_ID`
     The id of the runtime to create. If not specified, a random id will be generated. 
`--runtime-user`=`RUNTIME_USER`
     User email for the runtime owner. Runtimes can only be used by the owner. If a user is not provided, the gcloud user will be assumed to be the owner. The user cannot be a service account. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta colab runtimes create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/colab/runtimes/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
