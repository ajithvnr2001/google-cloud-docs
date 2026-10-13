---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cloud/networking/routers/create/
title: gcloud alpha edge-cloud networking routers create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:54.499495+00:00
---

# gcloud alpha edge-cloud networking routers create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cloud/networking/routers/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha edge-cloud networking routers create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha edge-cloud networking routers create - create a Distributed Cloud Edge Network router 
SYNOPSIS
    

`gcloud alpha edge-cloud networking routers create` (`ROUTER` : `--location`=`LOCATION` `--zone`=`ZONE`) `--asn`=`ASN` `--network`=`NETWORK` [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new Distributed Cloud Edge Network router. 
EXAMPLES
     To create a router called 'my-router' with asn 65555 in edge zone 'us-central1-edge-den1', run: 
    
    
    gcloud alpha edge-cloud networking routers create my-router --network=my-network --location=us-central1 --zone=us-central1-edge-den1 --asn=65555

POSITIONAL ARGUMENTS
    

Router resource - Distributed Cloud Edge Network router to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `router` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ROUTER`
     ID of the router or fully qualified identifier for the router. 

To set the `router` attribute: 

  * provide the argument `router` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The global location name. 

To set the `location` attribute: 

  * provide the argument `router` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--zone`=`ZONE`
     The name of the Google Distributed Cloud Edge zone. 

To set the `zone` attribute: 

  * provide the argument `router` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line. 


REQUIRED FLAGS
    

`--asn`=`ASN`
     The locally assigned BGP ASN. 
`--network`=`NETWORK`
     The network that this subnetwork belongs to. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     An optional, textual description for the router. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `edgenetwork/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/distributed-cloud-edge/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud edge-cloud networking routers create](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
