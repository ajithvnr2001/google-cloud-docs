---
url: https://docs.cloud.google.com/sdk/gcloud/reference/app/services/set-traffic/
title: gcloud app services set-traffic \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:47:40.814966+00:00
---

# gcloud app services set-traffic  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/app/services/set-traffic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud app services set-traffic Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud app services set-traffic - set traffic splitting settings 
SYNOPSIS
    

`gcloud app services set-traffic` [`SERVICES` …] `--splits`=`SPLITS`,[`SPLITS`,…] [`--migrate`] [`--split-by`=`SPLIT_BY`; default="ip"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command sets the traffic split of versions across a service or a project. 
EXAMPLES
     To send all traffic to 'v2' of service 's1', run: 
    
    
    gcloud app services set-traffic s1 --splits=v2=1

To split traffic evenly between 'v1' and 'v2' of service 's1', run: 
    
    
    gcloud app services set-traffic s1 --splits=v2=.5,v1=.5

To split traffic across all services: 
    
    
    gcloud app services set-traffic --splits=v2=.5,v1=.5

POSITIONAL ARGUMENTS
    

[`SERVICES` …]
     The services to modify. 
REQUIRED FLAGS
    

`--splits`=`SPLITS`,[`SPLITS`,…]
     Key-value pairs describing what proportion of traffic should go to each version. The split values are added together and used as weights. The exact values do not matter, only their relation to each other. For example, v1=2,v2=2 is equivalent to v1=.5,v2=.5 
OPTIONAL FLAGS
    

`--migrate`
     The migrate flag determines whether or not to use traffic migration during the operation. Traffic migration will attempt to automatically migrate traffic from the previous version to the new version, giving the autoscaler time to respond. See the documentation here: <https://cloud.google.com/appengine/docs/python/console/trafficmigration> for more information. 
`--split-by`=`SPLIT_BY`; default="ip"
     Whether to split traffic based on cookie, IP address or random. `SPLIT_BY` must be one of: `cookie`, `ip`, `random`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta app services set-traffic](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/services/set-traffic)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
