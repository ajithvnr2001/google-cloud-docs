---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/
title: gcloud compute url-maps \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:45:52.969387+00:00
---

# gcloud compute url-maps  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute url-maps Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute url-maps - list, create, and delete URL maps 
SYNOPSIS
    

`gcloud compute url-maps` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     List, create, and delete URL maps for external Application Load Balancer, internal Application Load Balancer, and Traffic Director. 

For more information about URL maps, see the [URL maps documentation](https://cloud.google.com/load-balancing/docs/url-map-concepts). 

See also: [URL maps API](https://cloud.google.com/compute/docs/reference/rest/v1/urlMaps) and [regional URL maps API](https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps). 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[add-host-rule](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-host-rule)`
     Add a rule to a URL map to map hosts to a path matcher. 
`[add-path-matcher](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher)`
     Add a path matcher to a URL map. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/create)`
     Create a URL map. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/delete)`
     Delete URL maps. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/describe)`
     Describe a URL map. 
`[edit](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/edit)`
     Modify URL maps. 
`[export](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/export)`
     Export a URL map. 
`[import](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/import)`
     Import a URL map. 
`[invalidate-cdn-cache](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/invalidate-cdn-cache)`
     Invalidate specified objects for a URL map in Cloud CDN caches. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/list)`
     List Google Compute Engine URL maps. 
`[list-cdn-cache-invalidations](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/list-cdn-cache-invalidations)`
     List Cloud CDN cache invalidations for a URL map. 
`[remove-host-rule](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-host-rule)`
     Remove a host rule from a URL map. 
`[remove-path-matcher](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/remove-path-matcher)`
     Remove a path matcher from a URL map. 
`[set-default-service](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/set-default-service)`
     Change the default service or default bucket of a URL map. 
`[test-iam-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/test-iam-permissions)`
     Test IAM permissions for a Compute Engine URL map. 
`[validate](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/validate)`
     Validate a URL map. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute url-maps](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/url-maps)
    
    
    [gcloud beta compute url-maps](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps)
    
    
    [gcloud preview compute url-maps](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/url-maps)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
