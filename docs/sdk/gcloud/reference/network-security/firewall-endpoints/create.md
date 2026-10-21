---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/create/
title: gcloud network-security firewall-endpoints create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:35:20.601941+00:00
---

# gcloud network-security firewall-endpoints create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-security firewall-endpoints create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-security firewall-endpoints create - create a Firewall Plus endpoint 
SYNOPSIS
    

`gcloud network-security firewall-endpoints create` (`FIREWALL_ENDPOINT` : `--organization`=`ORGANIZATION` `--zone`=`ZONE`) [`--async`] [`--billing-project`=`BILLING_PROJECT`] [`--description`=`DESCRIPTION`] [`--enable-jumbo-frames`] [`--labels`=[`KEY`=`VALUE`,…]] [`--location`=`LOCATION`] [`--max-wait`=`MAX_WAIT`; default="60m"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a firewall endpoint. Successful creation of an endpoint results in an endpoint in READY state. Check the progress of endpoint creation by using `[gcloud network-security firewall-endpoints list](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/list)`. 

For more examples, refer to the EXAMPLES section below. 

EXAMPLES
     To create a firewall endpoint called `my-endpoint`, in zone `us-central1-a` and organization ID 1234, run: 
    
    
    gcloud network-security firewall-endpoints create my-endpoint --zone=us-central1-a --organization=1234

POSITIONAL ARGUMENTS
    

Firewall endpoint resource - Firewall Plus. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `FIREWALL_ENDPOINT` on the command line with a fully specified name; 
  * set the property `core/project`. This resource can be one of the following types: [networksecurity.organizations.locations.firewallEndpoints, networksecurity.projects.locations.firewallEndpoints]. 



This must be specified. 

`FIREWALL_ENDPOINT`
     ID of the firewall endpoint or fully qualified identifier for the firewall endpoint. 

To set the `endpoint-name` attribute: 

  * provide the argument `FIREWALL_ENDPOINT` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--organization`=`ORGANIZATION`
     Organization ID of the firewall endpoint. 

To set the `organization` attribute: 

  * provide the argument `FIREWALL_ENDPOINT` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [networksecurity.organizations.locations.firewallEndpoints]. 


`--zone`=`ZONE`
     Zone of the firewall endpoint. 

To set the `zone` attribute: 

  * provide the argument `FIREWALL_ENDPOINT` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--billing-project`=`BILLING_PROJECT`
     The Google Cloud project ID to use for API enablement check, quota, and endpoint uptime billing. Overrides the default `billing/quota_project` property value for this command invocation. 
`--description`=`DESCRIPTION`
     Description of the endpoint 
`--enable-jumbo-frames`
     Enable jumbo frames for the firewall endpoint. To disable jumbo frames, use \--no-enable-jumbo-frames. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--location`=`LOCATION`
     Location of the endpoint 
`--max-wait`=`MAX_WAIT`; default="60m"
     Time to synchronously wait for the operation to complete, after which the operation continues asynchronously. Ignored if --no-async isn't specified. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha network-security firewall-endpoints create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/firewall-endpoints/create)
    
    
    [gcloud beta network-security firewall-endpoints create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/firewall-endpoints/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-09 UTC."],[],[]] 
