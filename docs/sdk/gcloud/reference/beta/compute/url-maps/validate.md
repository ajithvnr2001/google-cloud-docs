---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/validate/
title: gcloud beta compute url-maps validate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:49.895604+00:00
---

# gcloud beta compute url-maps validate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/url-maps/validate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute url-maps validate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute url-maps validate - validate a URL map 
SYNOPSIS
    

`gcloud beta compute url-maps validate` [`--load-balancing-scheme`=`LOAD_BALANCING_SCHEME`] [`--source`=`SOURCE`] [`--global` | `--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Runs static validation for the UrlMap. In particular, the tests of the provided UrlMap will be run. Calling this method does NOT create or update the UrlMap. 
EXAMPLES
     A URL map can be validated by running: 
    
    
    gcloud beta compute url-maps validate --source=<path-to-file>

FLAGS
    

`--load-balancing-scheme`=`LOAD_BALANCING_SCHEME`
     Specifies the load balancer type this validation request is for. Use `EXTERNAL_MANAGED` for global external Application Load Balancer. Use `EXTERNAL` for classic Application Load Balancer. 

Other load balancer types are not supported. For more information, refer to [Choosing a load balancer](https://cloud.google.com/load-balancing/docs/choosing-load-balancer/). 

If unspecified, the load balancing scheme will be inferred from the backend service resources this URL map references. If that can not be inferred (for example, this URL map only references backend buckets, or this URL map is for rewrites and redirects only and doesn't reference any backends), `EXTERNAL` will be used as the default type. 

If specified, the scheme must not conflict with the load balancing scheme of the backend service resources this URL map references. 

`LOAD_BALANCING_SCHEME` must be one of: `EXTERNAL`, `EXTERNAL_MANAGED`. 

`--source`=`SOURCE`
     Path to a YAML file containing configuration export data. The YAML file must not contain any output-only fields. Alternatively, you may omit this flag to read from standard input. For a schema describing the export/import format, see: $CLOUDSDKROOT/lib/googlecloudsdk/schemas/compute/beta/UrlMap.yaml. 
At most one of these can be specified: 

`--global`
     If set, the URL map is global. 
`--region`=`REGION`
     Region of the URL map to validate. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute url-maps validate](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/validate)
    
    
    [gcloud alpha compute url-maps validate](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/url-maps/validate)
    
    
    [gcloud preview compute url-maps validate](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/url-maps/validate)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
