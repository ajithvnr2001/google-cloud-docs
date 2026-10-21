---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/service-directory/services/resolve/
title: gcloud beta service-directory services resolve \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:46:21.667550+00:00
---

# gcloud beta service-directory services resolve  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/service-directory/services/resolve/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta service-directory services resolve Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta service-directory services resolve - resolves a service 
SYNOPSIS
    

`gcloud beta service-directory services resolve` (`SERVICE` : `--location`=`LOCATION` `--namespace`=`NAMESPACE`) [`--endpoint-filter`=`ENDPOINT_FILTER`] [`--max-endpoints`=`MAX_ENDPOINTS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Resolves a service. 
EXAMPLES
     To resolve Service Directory services, run: 
    
    
    gcloud beta service-directory services resolve my-service --namespace=my-namespace --location=us-east1

POSITIONAL ARGUMENTS
    

Service resource - The Service Directory service to resolve. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `service` on the command line with a fully specified name; 
  * set the property `core/project`. 



This must be specified. 

`SERVICE`
     ID of the service or fully qualified identifier for the service. 

To set the `service` attribute: 

  * provide the argument `service` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The name of the region for the service. 

To set the `location` attribute: 

  * provide the argument `service` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--namespace`=`NAMESPACE`
     The name of the namespace for the service. 

To set the `namespace` attribute: 

  * provide the argument `service` on the command line with a fully specified name; 
  * provide the argument `--namespace` on the command line. 


FLAGS
    

`--endpoint-filter`=`ENDPOINT_FILTER`
     Apply a Boolean filter EXPRESSION to each endpoint in the service. If the expression evaluates True, then that endpoint is listed. 
`--max-endpoints`=`MAX_ENDPOINTS`
     Maximum number of endpoints to return. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud service-directory services resolve](https://docs.cloud.google.com/sdk/gcloud/reference/service-directory/services/resolve)
    
    
    [gcloud alpha service-directory services resolve](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/service-directory/services/resolve)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
