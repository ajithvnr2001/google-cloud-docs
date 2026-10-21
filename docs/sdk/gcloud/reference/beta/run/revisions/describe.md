---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/revisions/describe/
title: gcloud beta run revisions describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:28:25.470589+00:00
---

# gcloud beta run revisions describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/revisions/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta run revisions describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta run revisions describe - obtain details about revisions 
SYNOPSIS
    

`gcloud beta run revisions describe` (`REVISION` : `--namespace`=`NAMESPACE`) [`--endpoint-mode`=`ENDPOINT_MODE`] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Obtain details about revisions. 
EXAMPLES
     To describe a revision `my-service-00001-abc`in us-central1: 
    
    
    gcloud beta run revisions describe --region=us-central1 my-service-00001-abc

`
POSITIONAL ARGUMENTS
    

Revision resource - Revision to describe. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`REVISION`
     ID of the revision or fully qualified identifier for the revision. 

To set the `revision` attribute: 

  * provide the argument `REVISION` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--namespace`=`NAMESPACE`
     Specific to Cloud Run for Anthos: Kubernetes namespace for the revision. 

To set the `namespace` attribute: 

  * provide the argument `REVISION` on the command line with a fully specified name; 
  * provide the argument `--namespace` on the command line; 
  * set the property `run/namespace`; 
  * For Cloud Run on Kubernetes Engine, defaults to "default". Otherwise, defaults to project ID.; 
  * provide the argument `project` on the command line; 
  * set the property `core/project`. 


FLAGS
    

`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--region`=`REGION`
     Region in which the resource can be found. Alternatively, set the property [run/region]. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud run revisions describe](https://docs.cloud.google.com/sdk/gcloud/reference/run/revisions/describe)
    
    
    [gcloud alpha run revisions describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/revisions/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
