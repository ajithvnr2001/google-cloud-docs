---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-firewall-policies/get-effective-firewalls/
title: gcloud preview compute network-firewall-policies get-effective-firewalls \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:22:02.963886+00:00
---

# gcloud preview compute network-firewall-policies get-effective-firewalls  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-firewall-policies/get-effective-firewalls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute network-firewall-policies get-effective-firewalls Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute network-firewall-policies get-effective-firewalls - get the effective firewalls for a network 
SYNOPSIS
    

`gcloud preview compute network-firewall-policies get-effective-firewalls` `--network`=`NETWORK` [`--region`=`REGION`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute network-firewall-policies get-effective-firewalls` is used to get the effective firewalls applied to the network, including regional firewalls in a specified region. 
EXAMPLES
     To get the effective firewalls of network with name ``example-network``, including effective regional firewalls for that network, in region ``region-a``, run: 
    
    
    [gcloud preview compute network-firewall-policies](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-firewall-policies) get-effective-firewalls --network=example-network --region=region-a

To show all fields of the firewall rules, please show in JSON format with option \--format=json 

To list more the fields of the rules of network ``example-network`` in table format, run: 
    
    
    [gcloud preview compute network-firewall-policies](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-firewall-policies) get-effective-firewalls --network=example-network --region=region-a --format="table(
      type,
      firewall_policy_name,
      rule_type,
      priority,
      action,
      direction,
      ip_ranges.list():label=IP_RANGES,
      target_svc_acct,
      enableLogging,
      description,
      name,
      disabled,
      target_tags,
      src_svc_acct,
      src_tags,
      ruleTupleCount,
      targetResources:label=TARGET_RESOURCES)"

REQUIRED FLAGS
    

`--network`=`NETWORK`
     The network to get the effective firewalls for. 
FLAGS
    

`--region`=`REGION`
     The region to get the effective regional firewalls. 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--uri`
     Print a list of resource URIs instead of the default output, and change the command output to a list of URIs. If this flag is used with `--format`, the formatting is applied on this URI list. To display URIs alongside other keys instead, use the `uri()` transform. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute network-firewall-policies get-effective-firewalls](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/get-effective-firewalls)
    
    
    [gcloud alpha compute network-firewall-policies](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-firewall-policies) get-effective-firewalls
    
    
    [gcloud beta compute network-firewall-policies](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-firewall-policies) get-effective-firewalls

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
