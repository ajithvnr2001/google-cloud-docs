---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/get-credentials/
title: gcloud container hub scopes namespaces get-credentials \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:11:35.371098+00:00
---

# gcloud container hub scopes namespaces get-credentials  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/get-credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container hub scopes namespaces get-credentials Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container hub scopes namespaces get-credentials - fetch credentials for a membership with a particular namespace 
SYNOPSIS
    

`gcloud container hub scopes namespaces get-credentials` `NAMESPACE` [`--membership`=`MEMBERSHIP`] [`--membership-location`=`MEMBERSHIP_LOCATION`] [`--set-namespace-in-config`=`SET_NAMESPACE_IN_CONFIG`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     Get the Connect Gateway kubeconfig for global membership `MEMBERSHIP`, using namespace `NAMESPACE` in the config: 
    
    
    gcloud container hub scopes namespaces get-credentials NAMESPACE --membership=MEMBERSHIP --membership-location=global --set-namespace-in-config=true

Get the Connect Gateway kubeconfig for global membership `MEMBERSHIP`: 
    
    
    gcloud container hub scopes namespaces get-credentials NAMESPACE --membership=MEMBERSHIP --membership-location=global

POSITIONAL ARGUMENTS
    

`NAMESPACE`
     Name of the namespace for which to get access to memberships. 
FLAGS
    

`--membership`=`MEMBERSHIP`
     Membership ID to get credentials from. If not provided, a prompt will offer a list of memberships in the fleet. 
`--membership-location`=`MEMBERSHIP_LOCATION`
     The location of the membership resource, e.g. `us-central1`. If not specified, defaults to `global`. 
`--set-namespace-in-config`=`SET_NAMESPACE_IN_CONFIG`
     If true, the default namespace for the context in the generated kubeconfig will be set to the Fleet namespace (i.e. the name given as the positional argument in this command). 

Otherwise, no default namespace will be set, functioning the same as `[gcloud container fleet memberships get-credentials](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/get-credentials)`. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha container hub scopes namespaces get-credentials](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/scopes/namespaces/get-credentials)
    
    
    [gcloud beta container hub scopes namespaces get-credentials](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/scopes/namespaces/get-credentials)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
