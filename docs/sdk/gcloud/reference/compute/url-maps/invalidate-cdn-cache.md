---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/invalidate-cdn-cache/
title: gcloud compute url-maps invalidate-cdn-cache \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:05:15.253391+00:00
---

# gcloud compute url-maps invalidate-cdn-cache  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/invalidate-cdn-cache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute url-maps invalidate-cdn-cache Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute url-maps invalidate-cdn-cache - invalidate specified objects for a URL map in Cloud CDN caches 
SYNOPSIS
    

`gcloud compute url-maps invalidate-cdn-cache` `URLMAP` [`--async`] [`--global`] [`--host`=`HOST`] [`--path`=`PATH`] [`--tags`=`TAGS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute url-maps invalidate-cdn-cache` requests that Cloud CDN stop using cached content for resources at a particular URL path or set of URL paths. 

`gcloud compute url-maps invalidate-cdn-cache` may succeed even if no content is cached for some or all URLs with the given path. 

POSITIONAL ARGUMENTS
    

`URLMAP`
     Name of the URL map to operate on. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--global`
     (Default) The URL map is global. Regional URL maps are not supported. 
`--host`=`HOST`
     If set, this invalidation will apply only to requests to the specified host. 
`--path`=`PATH`
     A path specifying which objects to invalidate. PATH must start with ``/´´ and the only place a ``*´´ is allowed is at the end of the path. It will be matched against URL paths, which do not include scheme, host, or any text after the first ``?´´ or ``#´´ (and those characters are not allowed here). For example, for the URL ``https://example.com/whatever/x.html?a=b``, the path is ``/whatever/x.html``. 

If PATH ends with ``*´´, the preceding string is a prefix, and all URLs whose paths begin with it will be invalidated. If PATH doesn't end with ``*´´, then only URLs with exactly that path will be invalidated. 

Examples: 

  * ``´´, ``*´´, anything that doesn't start with ``/´´: error 
  * ``/´´: just the root URL 
  * ``/*´´: everything 
  * ``/x/y´´: ``/x/y´´ only (and not ``/x/y/´´) 
  * ``/x/y/´´: ``/x/y/´´ only (and not ``/x/y´´) 
  * ``/x/y*´´: ``/x/y´´ and everything with the prefix (e.g. ``/x/yy``, ``/x/y/z´´) 


`--tags`=`TAGS`
     A single tag or a comma-delimited list of tags. When multiple tags are specified, the invalidation applies them using boolean OR logic. 

Example: 

  * ``\--tags=abcd,user123``


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute url-maps invalidate-cdn-cache](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/url-maps/invalidate-cdn-cache)
    
    
    [gcloud beta compute url-maps invalidate-cdn-cache](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/invalidate-cdn-cache)
    
    
    [gcloud preview compute url-maps invalidate-cdn-cache](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/url-maps/invalidate-cdn-cache)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
