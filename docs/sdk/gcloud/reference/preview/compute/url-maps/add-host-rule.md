---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/url-maps/add-host-rule/
title: gcloud preview compute url-maps add-host-rule \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:38:17.050943+00:00
---

# gcloud preview compute url-maps add-host-rule  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/url-maps/add-host-rule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute url-maps add-host-rule Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute url-maps add-host-rule - add a rule to a URL map to map hosts to a path matcher 
SYNOPSIS
    

`gcloud preview compute url-maps add-host-rule` `URL_MAP` `--hosts`=`HOST`,[`HOST`,…] `--path-matcher-name`=`PATH_MATCHER_NAME` [`--description`=`DESCRIPTION`] [`--global` | `--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute url-maps add-host-rule` is used to add a mapping of hosts to a path matcher in a URL map. The mapping will match the host component of HTTP requests to path matchers which in turn map the request to a backend service. Before adding a host rule, at least one path matcher must exist in the URL map to take care of the path component of the requests. `[gcloud compute url-maps add-path-matcher](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher)` or `[gcloud compute url-maps edit](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/edit)` can be used to add path matchers. 
EXAMPLES
     To create a host rule mapping the `*-foo.example.com` and `example.com` hosts to the `www` path matcher, run: 
    
    
    gcloud preview compute url-maps add-host-rule MY-URL-MAP --hosts='*-foo.example.com,example.com' --path-matcher-name=www

POSITIONAL ARGUMENTS
    

`URL_MAP`
     Name of the URL map to operate on. 
REQUIRED FLAGS
    

`--hosts`=`HOST`,[`HOST`,…]
     The set of hosts to match requests against. Each host must be a fully qualified domain name (FQDN) with the exception that the host can begin with a ``*´´ or ``*-´´. ``*´´ acts as a glob and will match any string of atoms to the left where an atom is separated by dots (``.´´) or dashes (``-´´). 
`--path-matcher-name`=`PATH_MATCHER_NAME`
     The name of the path matcher to use if a request matches this host rule. The path matcher must already exist in the URL map (see `[gcloud compute url-maps add-path-matcher](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher)`). 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the host rule. 
At most one of these can be specified: 

`--global`
     If set, the URL map is global. 
`--region`=`REGION`
     Region of the URL map to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

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
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute url-maps add-host-rule](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-host-rule)
    
    
    [gcloud alpha compute url-maps add-host-rule](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/url-maps/add-host-rule)
    
    
    [gcloud beta compute url-maps add-host-rule](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/add-host-rule)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
