---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/identity-service/delete/
title: gcloud alpha container hub identity-service delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:11.994668+00:00
---

# gcloud alpha container hub identity-service delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/identity-service/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container hub identity-service delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container hub identity-service delete - delete a resource from the Identity Service Feature 
SYNOPSIS
    

`gcloud alpha container hub identity-service delete` [`--fleet-default-member-config`] [`--membership`=`MEMBERSHIP` : `--location`=`LOCATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Deletes a resource from the Identity Service Feature. 
EXAMPLES
     To delete the Identity Service configuration from a membership, run: 
    
    
    gcloud alpha container hub identity-service delete --membership=MEMBERSHIP_NAME

To delete the fleet-level default membership configuration, run: 
    
    
    gcloud alpha container hub identity-service delete --fleet-default-member-config

FLAGS
    

`--fleet-default-member-config`
     If specified, deletes the default membership configuration present in your fleet. 
    
    
    To delete the default membership configuration present in your
    fleet, run:
    
    
    gcloud alpha container hub identity-service delete --fleet-default-member-config

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
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud container hub identity-service delete](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/identity-service/delete)
    
    
    [gcloud beta container hub identity-service delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/identity-service/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
