---
url: https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/invalidate-cache/
title: gcloud edge-cache services invalidate-cache \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:49:18.814401+00:00
---

# gcloud edge-cache services invalidate-cache  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/invalidate-cache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud edge-cache services invalidate-cache Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud edge-cache services invalidate-cache - invalidate the cache for an EdgeCacheService resource 
SYNOPSIS
    

`gcloud edge-cache services invalidate-cache` (`SERVICE` : `--location`=`LOCATION`) (`--host`=`HOST` `--path`=`PATH` `--tags`=[`TAGS`,…]) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Invalidate the cache entries associated with an EdgeCacheService resource. 
EXAMPLES
     To invalidate content via a tag, or tags for a given host for an EdgeCacheService named 'my-service': 
    
    
    gcloud edge-cache services invalidate-cache my-service --tags="status=404" --host="media.example.com"

To invalidate all content under a specific path, specify an exact path, or a prefix. Prefixes are denoted with a trailing `*` character. 
    
    
    gcloud edge-cache services invalidate-cache my-service --path="/static/*"

You can optionally combine this with a status code. For example, to invalidate all cached HTTP 404s: 
    
    
    gcloud edge-cache services invalidate-cache my-service --tags="status=404" --path="/static/*"

POSITIONAL ARGUMENTS
    

Service resource - The EdgeCacheService resource you want to invalidate the cache for. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `service` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SERVICE`
     ID of the service or fully qualified identifier for the service. 

To set the `service` attribute: 

  * provide the argument `service` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location Id. To set the `location` attribute: 

  * provide the argument `service` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * use global location. 


REQUIRED FLAGS
    

At least one of these must be specified: 

`--host`=`HOST`
     The hostname to invalidate against. You can specify an exact or wildcard host - e.g. "video.example.com" or "`.example.com" - based on host component. `
\--path`=`PATH``
     The path to invalidate against. You can specify an exact or wildcard host - e.g. "/videos/hls/139123.mp4" or "/manifests/" - based on path component. 
`--tags`=[`TAGS`,…]
     A list of cache tags used to identify cached objects. 

  * Cache tags are specified when the response is first cached, by setting the "Cache-Tag" response header at the origin. 
  * By default, all objects have a cache tag representing the HTTP status code of the response, the MIME content-type, and the origin. 
  * Multiple cache tags in the same revalidation request are treated as boolean OR - e.g. tag1 OR tag2 OR tag3. 
  * If a host and/or path are also specified, these are treated as boolean AND with any tags. 



Up to 10 tags may be specified in a single invalidation request. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkservices/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha edge-cache services invalidate-cache](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cache/services/invalidate-cache)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
