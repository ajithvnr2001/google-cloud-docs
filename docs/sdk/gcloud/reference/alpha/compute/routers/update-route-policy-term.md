---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/routers/update-route-policy-term/
title: gcloud alpha compute routers update-route-policy-term \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:32:54.755652+00:00
---

# gcloud alpha compute routers update-route-policy-term  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/routers/update-route-policy-term/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute routers update-route-policy-term Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute routers update-route-policy-term - updates a term of an existing route policy of a Comute Engine router 
SYNOPSIS
    

`gcloud alpha compute routers update-route-policy-term` `NAME` `--actions`=[`ACTION`;…] `--match`=`MATCH` `--policy-name`=`POLICY_NAME` `--priority`=`PRIORITY` [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute routers update-route-policy-term` updates a term of a route policy. 
EXAMPLES
     To update a term with priority 128 with match `destination == '192.168.0.0/24'` and actions `med.set(12345);asPath.prependSequence([1, 2])` of a route policy `example-policy-name` of a router `example-router` in region `router-region`, run: 
    
    
    gcloud alpha compute routers update-route-policy-term example-router --region=router-region --policy-name=example-policy-name --priority=128 --match="destination == '192.168.0.0/24'" --actions="med.set(12345);asPath.prependSequence([1, 2])"

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the router to update. 
REQUIRED FLAGS
    

`--actions`=[`ACTION`;…]
     Semicolon separated CEL expressions for the actions to take when the rule matches. 
`--match`=`MATCH`
     CEL expression for matching a route. 
`--policy-name`=`POLICY_NAME`
     Name of the route policy to which the term should be updated. 
`--priority`=`PRIORITY`
     Order of the term within the policy. 
OPTIONAL FLAGS
    

`--region`=`REGION`
     Region of the router to update. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute routers update-route-policy-term](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/update-route-policy-term)
    
    
    [gcloud beta compute routers update-route-policy-term](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/routers/update-route-policy-term)
    
    
    [gcloud preview compute routers update-route-policy-term](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/routers/update-route-policy-term)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
