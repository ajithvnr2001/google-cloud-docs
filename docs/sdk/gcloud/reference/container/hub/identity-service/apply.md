---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/identity-service/apply/
title: gcloud container hub identity-service apply \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:01:22.702896+00:00
---

# gcloud container hub identity-service apply  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/identity-service/apply/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container hub identity-service apply Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container hub identity-service apply - update the Identity Service Feature 
SYNOPSIS
    

`gcloud container hub identity-service apply` (`--fleet-default-member-config`=`FLEET_DEFAULT_MEMBER_CONFIG` [(`--config`=`CONFIG` | `--origin`=`ORIGIN`) : [`--membership`=`MEMBERSHIP` : `--location`=`LOCATION`]]) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command updates the Identity Service Feature in a fleet. 
EXAMPLES
     To apply an Identity Service configuration to a membership, run: 
    
    
    gcloud container hub identity-service apply --membership=MEMBERSHIP_NAME --config=/path/to/identity-service.yaml

To create or modify a fleet-level default membership configuration, run: 
    
    
    gcloud container hub identity-service apply --fleet-default-member-config=/path/to/identity-service.yaml

To apply an existing fleet-level default membership configuration to a membership, run: 
    
    
    gcloud container hub identity-service apply --origin=fleet --membership=MEMBERSHIP_NAME

REQUIRED FLAGS
    

At least one of these must be specified: 

`--fleet-default-member-config`=`FLEET_DEFAULT_MEMBER_CONFIG`
     The path to an identity-service.yaml configuration file. 
Exactly one of these must be specified: 

`--config`=`CONFIG`
     The path to an identity-service.yaml configuration file. 
`--origin`=`ORIGIN`
     Applies the fleet-level default membership configuration to a membership. `ORIGIN` must be (only one value is supported): `fleet`. 
Membership resource - The group of arguments defining a membership. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--membership` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--membership`=`MEMBERSHIP`
     ID of the membership or fully qualified identifier for the membership. 

To set the `membership` attribute: 

  * provide the argument `--membership` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location for the membership. 

To set the `location` attribute: 

  * provide the argument `--membership` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `gkehub/location`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha container hub identity-service apply](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/identity-service/apply)
    
    
    [gcloud beta container hub identity-service apply](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/identity-service/apply)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
