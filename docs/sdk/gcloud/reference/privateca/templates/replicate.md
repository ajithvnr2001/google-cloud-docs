---
url: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/templates/replicate/
title: gcloud privateca templates replicate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:40:20.370298+00:00
---

# gcloud privateca templates replicate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/templates/replicate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud privateca templates replicate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud privateca templates replicate - replicate a certificate template to multiple locations 
SYNOPSIS
    

`gcloud privateca templates replicate` (`CERTIFICATE_TEMPLATE` : `--location`=`LOCATION`) (`--all-locations` | `--target-locations`=[`LOCATION`,…]) [`--continue-on-error`] [`--overwrite`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Replicate a certificate template to multiple locations. 
EXAMPLES
     To replicate a certificate templates to all supported locations, run: 
    
    
    gcloud privateca templates replicate my-template --location=us-west1 --all-locations

To replicate a certificate template to 'us-west2' and 'us-east1', run: 
    
    
    gcloud privateca templates replicate my-template --location=us-west1 --target-locations=us-west2,us-east1

To overwrite existing templates with the same resource ID in the target locations, use the --overwrite flag: 
    
    
    gcloud privateca templates replicate my-template --location=us-west1 --target-locations=us-west2,us-east1 --overwrite

To continue replicating templates in other locations in the event of a failure in one or more locations, use the --continue-on-error flag: 
    
    
    gcloud privateca templates replicate my-template --location=us-west1 --all-locations --continue-on-error

POSITIONAL ARGUMENTS
    

CERTIFICATE TEMPLATE resource - The template to replicate. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `CERTIFICATE_TEMPLATE` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CERTIFICATE_TEMPLATE`
     ID of the CERTIFICATE_TEMPLATE or fully qualified identifier for the CERTIFICATE_TEMPLATE. 

To set the `certificate template` attribute: 

  * provide the argument `CERTIFICATE_TEMPLATE` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the CERTIFICATE_TEMPLATE. 

To set the `location` attribute: 

  * provide the argument `CERTIFICATE_TEMPLATE` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `privateca/location`. 


REQUIRED FLAGS
    

Specify where the certificate template should be replicated. 

Exactly one of these must be specified: 

`--all-locations`
     Replicate this template to all supported locations. 
`--target-locations`=[`LOCATION`,…]
     Replicate this template to the given locations. 
OPTIONAL FLAGS
    

`--continue-on-error`
     Continue replicating the template to other locations even if an error is encountered. If this is set, an error in one location will be logged but will not prevent replication to other locations. 
`--overwrite`
     Overwrite any existing templates with the same name, if they exist. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
