---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/network-interfaces/get-effective-firewalls/
title: gcloud beta compute instances network-interfaces get-effective-firewalls \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:39:44.496130+00:00
---

# gcloud beta compute instances network-interfaces get-effective-firewalls  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/network-interfaces/get-effective-firewalls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute instances network-interfaces get-effective-firewalls Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute instances network-interfaces get-effective-firewalls - get the effective firewalls for a Compute Engine virtual machine network interface 
SYNOPSIS
    

`gcloud beta compute instances network-interfaces get-effective-firewalls` `INSTANCE_NAME` [`NAME` …] [`--network-interface`=`NETWORK_INTERFACE`; default="nic0"] [`--regexp`=`REGEXP`, `-r` `REGEXP`] [`--zone`=`ZONE`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute instances network-interfaces get-effective-firewalls` is used to get the effective firewalls applied to the network interfaces of a Compute Engine virtual machine. 
EXAMPLES
     To get the effective firewalls of instance with name example-instance, run: 
    
    
    [gcloud beta compute instances network-interfaces](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/network-interfaces) get-effective-firewalls example-instance

To show all fields of the firewall rules, please show in JSON format with option \--format=json 

To see more firewall rule fields in table format, run the following for "example-instance": 
    
    
    [gcloud beta compute instances network-interfaces](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/network-interfaces) get-effective-firewalls example-instance --format="table(
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

POSITIONAL ARGUMENTS
    

`INSTANCE_NAME`
     Name of the instance to operate on. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
[`NAME` …]
     (DEPRECATED) If provided, show details for the specified names and/or URIs of resources. 

Argument `NAME` is deprecated. Use `--filter="name=( 'NAME' … )"` instead. 

FLAGS
    

`--network-interface`=`NETWORK_INTERFACE`; default="nic0"
     The name of the network interface to get the effective firewalls for. 
`--regexp`=`REGEXP`, `-r` `REGEXP`
     (DEPRECATED) Regular expression to filter the names of the results on. Any names that do not match the entire regular expression will be filtered out. 

Flag `--regexp` is deprecated. Use `--filter="name~'REGEXP'"` instead. 

`--zone`=`ZONE`
     Zone of the instance to operate on. If not specified, you might be prompted to select a zone (interactive mode only). `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` attempts to identify the appropriate zone by searching for resources in your currently active project. If the zone cannot be determined, `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with all available Google Cloud Platform zones. 

To avoid prompting when this flag is omitted, the user can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

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
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute instances network-interfaces get-effective-firewalls](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/get-effective-firewalls)
    
    
    [gcloud alpha compute instances network-interfaces](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces) get-effective-firewalls
    
    
    [gcloud preview compute instances network-interfaces](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/network-interfaces) get-effective-firewalls

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
