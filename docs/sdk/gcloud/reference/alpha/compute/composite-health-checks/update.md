---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/composite-health-checks/update/
title: gcloud alpha compute composite-health-checks update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:50.229824+00:00
---

# gcloud alpha compute composite-health-checks update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/composite-health-checks/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute composite-health-checks update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute composite-health-checks update - update a composite health check 
SYNOPSIS
    

`gcloud alpha compute composite-health-checks update` (`COMPOSITE_HEALTH_CHECK` : `--region`=`REGION`) (`--description`=`DESCRIPTION` `--health-destination`=`HEALTH_DESTINATION` `--health-sources`=`HEALTH_SOURCES`,[…]) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update a composite health check. 
EXAMPLES
     The following command updates an existing composite health check: 
    
    
    gcloud alpha compute composite-health-checks update <COMPOSITE_HEALTH_CHECK_NAME> --region=<REGION> --health-destination=my-new-fr

POSITIONAL ARGUMENTS
    

Composite health check resource - The name of the composite health check you want to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `composite_health_check` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`COMPOSITE_HEALTH_CHECK`
     ID of the composite health check or fully qualified identifier for the composite health check. 

To set the `composite_health_check` attribute: 

  * provide the argument `composite_health_check` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The name of the Google Compute Engine region. 

To set the `region` attribute: 

  * provide the argument `composite_health_check` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `compute/region`. 


REQUIRED FLAGS
    

At least one of these must be specified: 

`--description`=`DESCRIPTION`
     A textual description of this resource. 
`--health-destination`=`HEALTH_DESTINATION`
     URL to the destination resource. Must be set. Must be a ForwardingRule. The ForwardingRule must have load balancing scheme INTERNAL or INTERNAL_MANAGED and must be regional and in the same region as the CompositeHealthCheck (cross-region deployment for INTERNAL_MANAGED is not supported). Can be mutated. 
`--health-sources`=`HEALTH_SOURCES`,[…]
     URLs to the HealthSource resources whose results are AND'ed. I.e. the aggregated result is HEALTHY only if all sources are HEALTHY. Must have at least 1. Must not have more than 10. Must be regional and in the same region as the CompositeHealthCheck. Can be mutated. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `compute/alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/compute/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute composite-health-checks update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/composite-health-checks/update)
    
    
    [gcloud beta compute composite-health-checks update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/composite-health-checks/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
