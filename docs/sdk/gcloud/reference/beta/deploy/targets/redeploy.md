---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/deploy/targets/redeploy/
title: gcloud beta deploy targets redeploy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:43.786064+00:00
---

# gcloud beta deploy targets redeploy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/deploy/targets/redeploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta deploy targets redeploy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta deploy targets redeploy - redeploy the last release to a target 
SYNOPSIS
    

`gcloud beta deploy targets redeploy` (`TARGET` : `--region`=`REGION`) `--delivery-pipeline`=`DELIVERY_PIPELINE` [`--annotations`=[`KEY`=`VALUE`,…]] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`--override-deploy-policies`=[`POLICY`,…]] [`--rollout-id`=`ROLLOUT_ID`] [`--starting-phase-id`=`STARTING_PHASE_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Redeploy the last rollout that has a state of SUCCESSFUL or FAILED to a target. If rollout-id is not specified, a rollout ID will be generated. 
EXAMPLES
     To redeploy a target `prod` for delivery pipeline `test-pipeline` in region `us-central1`, run: 
    
    
    gcloud beta deploy targets redeploy prod --delivery-pipeline=test-pipeline --region=us-central1

POSITIONAL ARGUMENTS
    

Target resource - The name of the Target. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `target` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TARGET`
     ID of the target or fully qualified identifier for the target. 

To set the `target` attribute: 

  * provide the argument `target` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The Cloud region for the target. Alternatively, set the property [deploy/region]. 

To set the `region` attribute: 

  * provide the argument `target` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `deploy/region`. 


REQUIRED FLAGS
    

`--delivery-pipeline`=`DELIVERY_PIPELINE`
     The name of the Cloud Deploy delivery pipeline 
OPTIONAL FLAGS
    

`--annotations`=[`KEY`=`VALUE`,…]
     Annotations to apply to the rollout. Annotations take the form of key/value string pairs. 

Examples: 

Add annotations: 
    
    
    gcloud beta deploy targets redeploy --annotations="from_target=test,status=stable"

`--description`=`DESCRIPTION`
     Description of rollout created during a rollback. 
`--labels`=[`KEY`=`VALUE`,…]
     Labels to apply to the rollout. Labels take the form of key/value string pairs. 

Examples: 

Add labels: 
    
    
    gcloud beta deploy targets redeploy --labels="commit=abc123,author=foo"

`--override-deploy-policies`=[`POLICY`,…]
     Deploy policies to override 
`--rollout-id`=`ROLLOUT_ID`
     ID to assign to the generated rollout for promotion. 
`--starting-phase-id`=`STARTING_PHASE_ID`
     If set, starts the created rollout at the specified phase. 

Start rollout at `stable` phase: 
    
    
    gcloud beta deploy targets redeploy --starting-phase-id=stable

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud deploy targets redeploy](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/targets/redeploy)
    
    
    [gcloud alpha deploy targets redeploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/deploy/targets/redeploy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
