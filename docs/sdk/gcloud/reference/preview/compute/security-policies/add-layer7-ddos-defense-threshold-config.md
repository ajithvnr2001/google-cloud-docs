---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/security-policies/add-layer7-ddos-defense-threshold-config/
title: gcloud preview compute security-policies add-layer7-ddos-defense-threshold-config \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:32:12.319263+00:00
---

# gcloud preview compute security-policies add-layer7-ddos-defense-threshold-config  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/security-policies/add-layer7-ddos-defense-threshold-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute security-policies add-layer7-ddos-defense-threshold-config Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute security-policies add-layer7-ddos-defense-threshold-config - add a layer7 ddos defense threshold config to a Compute Engine security policy 
SYNOPSIS
    

`gcloud preview compute security-policies add-layer7-ddos-defense-threshold-config` `NAME` `--threshold-config-name`=`THRESHOLD_CONFIG_NAME` [`--auto-deploy-confidence-threshold`=`AUTO_DEPLOY_CONFIDENCE_THRESHOLD`] [`--auto-deploy-expiration-sec`=`AUTO_DEPLOY_EXPIRATION_SEC`] [`--auto-deploy-impacted-baseline-threshold`=`AUTO_DEPLOY_IMPACTED_BASELINE_THRESHOLD`] [`--auto-deploy-load-threshold`=`AUTO_DEPLOY_LOAD_THRESHOLD`] [`--detection-absolute-qps`=`DETECTION_ABSOLUTE_QPS`] [`--detection-load-threshold`=`DETECTION_LOAD_THRESHOLD`] [`--detection-relative-to-baseline-qps`=`DETECTION_RELATIVE_TO_BASELINE_QPS`] [`--traffic-granularity-configs`=[`type`=`TYPE`[,`value`=`VALUE`][,`enableEachUniqueValue`=`ENABLE_EACH_UNIQUE_VALUE`];…;…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute security-policies add-layer7-ddos-defense-threshold-config` is used to add layer7 ddos defense threshold configs to security policies. 
EXAMPLES
     To add a layer7 ddos defense threshold config run the following command: 
    
    
    [gcloud preview compute security-policies](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/security-policies) add-layer7-ddos-defense-threshold-config NAME --threshold-config-name=my-threshold-config-name --auto-deploy-load-threshold=0.7 --auto-deploy-confidence-threshold=0.8 --auto-deploy-impacted-baseline-threshold=0.1 --auto-deploy-expiration-sec=4800 --detection-load-threshold=0.4 --detection-absolute-qps=1000 --detection-relative-to-baseline-qps=2.0 --traffic-granularity-configs=type=HTTP_HEADER_HOST,value=www.my-test-host.com;type=HTTP_PATH,enableEachUniqueValue=true

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the security policy to update. 
REQUIRED FLAGS
    

`--threshold-config-name`=`THRESHOLD_CONFIG_NAME`
     The name for the threshold config. 
OPTIONAL FLAGS
    

`--auto-deploy-confidence-threshold`=`AUTO_DEPLOY_CONFIDENCE_THRESHOLD`
     The threshold of the confidence of an identified attack, over which auto-deploy takes action. 
`--auto-deploy-expiration-sec`=`AUTO_DEPLOY_EXPIRATION_SEC`
     The duration of actions, if any, taken by auto-deploy. 
`--auto-deploy-impacted-baseline-threshold`=`AUTO_DEPLOY_IMPACTED_BASELINE_THRESHOLD`
     The threshold on the estimated impact to the baseline traffic of a suggested mitigation, below which auto-deploy takes action. 
`--auto-deploy-load-threshold`=`AUTO_DEPLOY_LOAD_THRESHOLD`
     The threshold on backend's load, over which auto-deploy takes action. 
`--detection-absolute-qps`=`DETECTION_ABSOLUTE_QPS`
     The absolute QPS of the incoming traffic, over which adaptive protection detects an attack. 
`--detection-load-threshold`=`DETECTION_LOAD_THRESHOLD`
     The threshold on backend's load, over which adaptive protection detects an attack. 
`--detection-relative-to-baseline-qps`=`DETECTION_RELATIVE_TO_BASELINE_QPS`
     The QPS of the incoming traffic relative to the average baseline QPS, over which adaptive protection detects an attack. 
`--traffic-granularity-configs`=[`type`=`TYPE`[,`value`=`VALUE`][,`enableEachUniqueValue`=`ENABLE_EACH_UNIQUE_VALUE`];…;…]
     Specify up to 2 configs matching a specific type/value of traffic. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute security-policies](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies) add-layer7-ddos-defense-threshold-config
    
    
    [gcloud alpha compute security-policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/security-policies) add-layer7-ddos-defense-threshold-config
    
    
    [gcloud beta compute security-policies](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/security-policies) add-layer7-ddos-defense-threshold-config

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
