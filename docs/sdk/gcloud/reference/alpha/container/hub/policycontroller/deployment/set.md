---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/policycontroller/deployment/set/
title: gcloud alpha container hub policycontroller deployment set \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:53:37.222383+00:00
---

# gcloud alpha container hub policycontroller deployment set  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/policycontroller/deployment/set/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container hub policycontroller deployment set Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container hub policycontroller deployment set - sets configuration of the Policy Controller components 
SYNOPSIS
    

`gcloud alpha container hub policycontroller deployment set` `DEPLOYMENT` `PROPERTY` `VALUE` [`--effect`=`EFFECT`] [`--all-memberships` | [`--memberships`=[`MEMBERSHIPS`,…] : `--location`=`LOCATION`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Customizes on-cluster components of Policy Controller. Supported properties may be set with this command, or removed with 'remove'. These components are managed as individual kubernetes deployments (e.g. 'admission') in the gatekeeper-system namespace. 

When setting cpu or memory limits and requests, Kubernetes-standard resource units are used. 

All properties set using this command will overwrite previous properties, with the exception of tolerations which can only be added, and any number may be added. To edit a toleration, use 'remove' to first delete it, and then 'set' the desired toleration. 

EXAMPLES
     To set the replica count for a component: 
    
    
    gcloud alpha container hub policycontroller deployment set admission replica-count 3

To set the replica count for a component across all fleet memberships: 
    
    
    gcloud alpha container hub policycontroller deployment set admission replica-count 3 --all-memberships

To set a toleration with key 'my-key' on a component (which is an 'Exists' operator): 
    
    
    gcloud alpha container hub policycontroller deployment set admission toleration my-key

To set a toleration with key 'my-key' and 'my-value' on a component (which is an 'Equal' operator): 
    
    
    gcloud alpha container hub policycontroller deployment set admission toleration my-key=my-value

To set a toleration with key 'my-key' and 'my-value' on a component, along with the effect 'NoSchedule' (which is an 'Equal' operator): 
    
    
    gcloud alpha container hub policycontroller deployment set admission toleration my-key=my-value --effect=NoSchedule

To set a memory limit: 
    
    
    gcloud alpha container hub policycontroller deployment set audit memory-limit 4Gi

To set a memory request: 
    
    
    gcloud alpha container hub policycontroller deployment set mutation memory-request 2Gi

To set a cpu limit: 
    
    
    gcloud alpha container hub policycontroller deployment set admission cpu-limit 500m

To set a cpu request: 
    
    
    gcloud alpha container hub policycontroller deployment set audit cpu-request 250m

To set anti-affinity to achieve high availability on the mutation deployment: 
    
    
    gcloud alpha container hub policycontroller deployment set mutation pod-affinity anti

POSITIONAL ARGUMENTS
    

`DEPLOYMENT`
     The PolicyController deployment component (e.g. "admission", "audit" or "mutation") upon which to set configuration. 
`PROPERTY`
     Property to be set. 
`VALUE`
     The value to set the property to. Valid input varies based on the property being set. 
FLAGS
    

`--effect`=`EFFECT`
     Applies only to "toleration" property. `EFFECT` must be one of: `NoSchedule`, `PreferNoSchedule`, `NoExecute`. 
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
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud container hub policycontroller deployment set](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller/deployment/set)
    
    
    [gcloud beta container hub policycontroller deployment set](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/policycontroller/deployment/set)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
