---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/instances/proxy/
title: gcloud beta run instances proxy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:55.178631+00:00
---

# gcloud beta run instances proxy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/instances/proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta run instances proxy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta run instances proxy - proxy an instance to localhost authenticating as the active account or with the specified token 
SYNOPSIS
    

`gcloud beta run instances proxy` `INSTANCE` [`--port`=`PORT`] [`--region`=`REGION`] [`--token`=`TOKEN`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Runs a server on localhost that proxies requests to the specified Cloud Run Instance with credentials attached. 

You can use this to test instances protected with IAM authentication. 

The Cloud Run instance must be reachable from the machine running this command. For example, if the Cloud Run Instance is configured to only allow `internal` ingress, this command will not work from outside the instance's VPC network. 

EXAMPLES
     To proxy the instance 'my-instance' at localhost port 8080: 
    
    
    gcloud beta run instances proxy my-instance --port=8080

POSITIONAL ARGUMENTS
    

Instance resource - Instance to proxy locally. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `INSTANCE` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INSTANCE`
     ID of the Instance or fully qualified identifier for the Instance. 

To set the `instances` attribute: 

  * provide the argument `INSTANCE` on the command line. 


FLAGS
    

`--port`=`PORT`
     Local port number to expose the proxied instance. If not specified, it will be set to 8080. 
`--region`=`REGION`
     Region in which the resource can be found. Alternatively, set the property [run/region]. 
`--token`=`TOKEN`
     The specific identity token to add to all requests of the proxied service. If not specified, the identity token of the currently active authenticated account will be used (e.g. gcloud auth print-identity-token). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha run instances proxy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/instances/proxy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
