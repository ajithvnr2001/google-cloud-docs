---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/health-aggregation-policies/update/
title: gcloud alpha compute health-aggregation-policies update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:45:26.198751+00:00
---

# gcloud alpha compute health-aggregation-policies update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/health-aggregation-policies/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute health-aggregation-policies update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute health-aggregation-policies update - update a health aggregation policy 
SYNOPSIS
    

`gcloud alpha compute health-aggregation-policies update` (`HEALTH_AGGREGATION_POLICY` : `--region`=`REGION`) (`--description`=`DESCRIPTION` `--healthy-percent-threshold`=`HEALTHY_PERCENT_THRESHOLD` `--min-healthy-threshold`=`MIN_HEALTHY_THRESHOLD`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update a health aggregation policy. 
EXAMPLES
     The following command updates a health aggregation policy: 


POSITIONAL ARGUMENTS
    

Health aggregation policy resource - The health aggregation policy you want to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `health_aggregation_policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`HEALTH_AGGREGATION_POLICY`
     ID of the health aggregation policy or fully qualified identifier for the health aggregation policy. 

To set the `health_aggregation_policy` attribute: 

  * provide the argument `health_aggregation_policy` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The name of the Google Compute Engine region. 

To set the `region` attribute: 

  * provide the argument `health_aggregation_policy` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `compute/region`. 


REQUIRED FLAGS
    

At least one of these must be specified: 

`--description`=`DESCRIPTION`
     A textual description of the health aggregation policy. 
`--healthy-percent-threshold`=`HEALTHY_PERCENT_THRESHOLD`
     Can only be set if the policyType field is BACKEND_SERVICE_POLICY. Specifies the threshold (as a percentage) of healthy endpoints required in order to consider the aggregated health result HEALTHY. Defaults to 60. Must be in range [0, 100]. Not applicable if the policyType field is DNS_PUBLIC_IP_POLICY. Can be mutated. This field is optional, and will be set to the default if unspecified. Note that both this threshold and minHealthyThreshold must be satisfied in order for HEALTHY to be the aggregated result. "Endpoints" refers to network endpoints within a Network Endpoint Group or instances within an Instance Group. 
`--min-healthy-threshold`=`MIN_HEALTHY_THRESHOLD`
     Can only be set if the policyType field is BACKEND_SERVICE_POLICY. Specifies the minimum number of healthy endpoints required in order to consider the aggregated health result HEALTHY. Defaults to 1. Must be positive. Not applicable if the policyType field is DNS_PUBLIC_IP_POLICY. Can be mutated. This field is optional, and will be set to the default if unspecified. Note that both this threshold and healthyPercentThreshold must be satisfied in order for HEALTHY to be the aggregated result. "Endpoints" refers to network endpoints within a Network Endpoint Group or instances within an Instance Group. 
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
    
    
    gcloud alpha compute health-aggregation-policies update <HEALTH_AGGREGATION_POLICY_NAME> --region=<REGION> --healthy-percent-threshold 60 --min-healthy-threshold 2 [gcloud compute health-aggregation-policies update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-aggregation-policies/update)
    
    
    [gcloud beta compute health-aggregation-policies update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/health-aggregation-policies/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
