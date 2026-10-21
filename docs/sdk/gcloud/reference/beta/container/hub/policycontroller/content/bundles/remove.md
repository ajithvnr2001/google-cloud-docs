---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/policycontroller/content/bundles/remove/
title: gcloud beta container hub policycontroller content bundles remove \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:02:18.749257+00:00
---

# gcloud beta container hub policycontroller content bundles remove  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/policycontroller/content/bundles/remove/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container hub policycontroller content bundles remove Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container hub policycontroller content bundles remove - removes a bundle installation for Policy Controller content 
SYNOPSIS
    

`gcloud beta container hub policycontroller content bundles remove` `BUNDLE_NAME` [`--all-memberships` | [`--memberships`=[`MEMBERSHIPS`,…] : `--location`=`LOCATION`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Google-defined policy bundles of constraints can be installed onto Policy Controller installations. This command removes those bundles. 
EXAMPLES
     To remove a policy bundle: 
    
    
    [gcloud beta container hub policycontroller content bundles](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/policycontroller/content/bundles) remove cis-k8s-v1.5.1

POSITIONAL ARGUMENTS
    

`BUNDLE_NAME`
     The constraint bundle to remove from Policy Controller. 
FLAGS
    

Membership flags. 

At most one of these can be specified: 

`--all-memberships`
     If supplied, apply to all Policy Controllers memberships in the fleet. 
Or at least one of these can be specified: 

Membership resource - The group of arguments defining one or more memberships. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--memberships` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--memberships`=[`MEMBERSHIPS`,…]
     IDs of the memberships or fully qualified identifiers for the memberships. 

To set the `memberships` attribute: 

  * provide the argument `--memberships` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location for the memberships. 

To set the `location` attribute: 

  * provide the argument `--memberships` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `gkehub/location`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container hub policycontroller content bundles remove](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/content/bundles/remove)
    
    
    [gcloud alpha container hub policycontroller content bundles remove](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/policycontroller/content/bundles/remove)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
