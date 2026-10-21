---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/remove/
title: gcloud container fleet policycontroller deployment remove \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:56:11.248331+00:00
---

# gcloud container fleet policycontroller deployment remove  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/remove/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container fleet policycontroller deployment remove Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container fleet policycontroller deployment remove - removes configuration properties from Policy Controller components 
SYNOPSIS
    

`gcloud container fleet policycontroller deployment remove` `DEPLOYMENT` `PROPERTY` [`VALUE`] [`--effect`=`EFFECT`] [`--all-memberships` | [`--memberships`=[`MEMBERSHIPS`,…] : `--location`=`LOCATION`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Remove customizations of on-cluster components in Policy Controller. These components are managed as individual kubernetes deployments (e.g. 'admission') in the gatekeeper-system namespace. 

When removing a 'toleration' property, it must match exactly, including the key, value and effect flag (if originally specified). 

EXAMPLES
     To remove the replica count for a component: 
    
    
    gcloud container fleet policycontroller deployment remove admission replica-count

To remove the replica count for a component across all fleet memberships: 
    
    
    gcloud container fleet policycontroller deployment remove admission replica-count --all-memberships

To remove a toleration with key 'my-key' on a component: 
    
    
    gcloud container fleet policycontroller deployment remove admission toleration my-key

To remove a toleration with key 'my-key' and 'my-value' on a component: 
    
    
    gcloud container fleet policycontroller deployment remove admission toleration my-key=my-value

To remove a toleration with key 'my-key' and 'my-value' on a component, along with the effect 'NoSchedule': 
    
    
    gcloud container fleet policycontroller deployment remove admission toleration my-key=my-value --effect=NoSchedule

To remove a memory limit: 
    
    
    gcloud container fleet policycontroller deployment remove audit memory-limit

To remove a memory request: 
    
    
    gcloud container fleet policycontroller deployment remove mutation memory-request

To remove a cpu limit: 
    
    
    gcloud container fleet policycontroller deployment remove admission cpu-limit

To remove a cpu request: 
    
    
    gcloud container fleet policycontroller deployment remove audit cpu-request

To remove the anti-affinity configuration: 
    
    
    gcloud container fleet policycontroller deployment remove admission pod-affinity

POSITIONAL ARGUMENTS
    

`DEPLOYMENT`
     The PolicyController deployment component (i.e, "admission", "audit" or "mutation" from which to remove configuration. 
`PROPERTY`
     Property to be removed. 
[`VALUE`]
     This is only required to remove a toleration. It should not be included for any other property. 
FLAGS
    

`--effect`=`EFFECT`
     Applies only to "toleration" property. To be removed, tolerations must match exactly, including the effect setting. `EFFECT` must be one of: `NoSchedule`, `PreferNoSchedule`, `NoExecute`. 
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
     These variants are also available: 
    
    
    [gcloud alpha container fleet policycontroller deployment remove](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/policycontroller/deployment/remove)
    
    
    [gcloud beta container fleet policycontroller deployment remove](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/policycontroller/deployment/remove)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
