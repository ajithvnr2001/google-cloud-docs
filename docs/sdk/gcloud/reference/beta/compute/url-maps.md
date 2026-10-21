---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/
title: gcloud beta compute url-maps \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:42:49.617594+00:00
---

# gcloud beta compute url-maps  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute url-maps Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute url-maps - list, create, and delete URL maps 
SYNOPSIS
    

`gcloud beta compute url-maps` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` List, create, and delete URL maps for external Application Load Balancer, internal Application Load Balancer, and Traffic Director. 

For more information about URL maps, see the [URL maps documentation](https://cloud.google.com/load-balancing/docs/url-map-concepts). 

See also: [URL maps API](https://cloud.google.com/compute/docs/reference/rest/v1/urlMaps) and [regional URL maps API](https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps). 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[add-host-rule](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/add-host-rule)`
     `(BETA)` Add a rule to a URL map to map hosts to a path matcher. 
`[add-path-matcher](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/add-path-matcher)`
     `(BETA)` Add a path matcher to a URL map. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/create)`
     `(BETA)` Create a URL map. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/delete)`
     `(BETA)` Delete URL maps. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/describe)`
     `(BETA)` Describe a URL map. 
`[edit](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/edit)`
     `(BETA)` Modify URL maps. 
`[export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/export)`
     `(BETA)` Export a URL map. 
`[import](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/import)`
     `(BETA)` Import a URL map. 
`[invalidate-cdn-cache](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/invalidate-cdn-cache)`
     `(BETA)` Invalidate specified objects for a URL map in Cloud CDN caches. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/list)`
     `(BETA)` List Google Compute Engine URL maps. 
`[list-cdn-cache-invalidations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/list-cdn-cache-invalidations)`
     `(BETA)` List Cloud CDN cache invalidations for a URL map. 
`[remove-host-rule](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/remove-host-rule)`
     `(BETA)` Remove a host rule from a URL map. 
`[remove-path-matcher](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/remove-path-matcher)`
     `(BETA)` Remove a path matcher from a URL map. 
`[set-default-service](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/set-default-service)`
     `(BETA)` Change the default service or default bucket of a URL map. 
`[test-iam-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/test-iam-permissions)`
     `(BETA)` Test IAM permissions for a Compute Engine URL map. 
`[validate](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/validate)`
     `(BETA)` Validate a URL map. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute url-maps](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps)
    
    
    [gcloud alpha compute url-maps](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/url-maps)
    
    
    [gcloud preview compute url-maps](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/url-maps)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
