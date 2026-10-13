---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/get-credentials/
title: gcloud container fleet memberships get-credentials \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:55.777555+00:00
---

# gcloud container fleet memberships get-credentials  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/get-credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container fleet memberships get-credentials Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container fleet memberships get-credentials - fetch credentials for a fleet-registered cluster to be used in Connect Gateway 
SYNOPSIS
    

`gcloud container fleet memberships get-credentials` (`MEMBERSHIP_NAME` : `--location`=`LOCATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     gcloud container fleet memberships get-credentials updates the `kubeconfig` file with the appropriate credentials and endpoint information to send `kubectl` commands to a fleet-registered and -connected cluster through the Connect Gateway service. 

It takes a project, passed through by set defaults or flags. By default, credentials are written to `$HOME/.kube/config`. You can provide an alternate path by setting the `KUBECONFIG` environment variable. If `KUBECONFIG` contains multiple paths, the first one is used. 

Upon success, this command will switch the current context to the target cluster if other contexts are already present in the `kubeconfig` file. 

To force the use of Application Default Credentials (ADC) for authentication, you can set the `container/use_application_default_credentials` property to `true`: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) container/use_application_default_credentials true

EXAMPLES
     Get the Gateway kubeconfig for a globally registered cluster: 
    
    
    gcloud container fleet memberships get-credentials my-cluster
    gcloud container fleet memberships get-credentials my-cluster --location=global

Get the Gateway kubeconfig for a cluster registered in us-central1: 
    
    
    gcloud container fleet memberships get-credentials my-cluster --location=us-central1

POSITIONAL ARGUMENTS
    

Membership resource - The group of arguments defining a membership. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `MEMBERSHIP_NAME` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MEMBERSHIP_NAME`
     ID of the membership or fully qualified identifier for the membership. 

To set the `membership` attribute: 

  * provide the argument `MEMBERSHIP_NAME` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the membership resource, e.g. `us-central1`. If not specified, attempts to automatically choose the correct region. To set the `location` attribute: 

  * provide the argument `MEMBERSHIP_NAME` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `gkehub/location`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha container fleet memberships get-credentials](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/memberships/get-credentials)
    
    
    [gcloud beta container fleet memberships get-credentials](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/memberships/get-credentials)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
