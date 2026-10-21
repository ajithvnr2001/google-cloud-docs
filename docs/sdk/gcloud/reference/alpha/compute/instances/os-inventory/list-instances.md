---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/os-inventory/list-instances/
title: gcloud alpha compute instances os-inventory list-instances \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:14:39.761032+00:00
---

# gcloud alpha compute instances os-inventory list-instances  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/os-inventory/list-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute instances os-inventory list-instances Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute instances os-inventory list-instances - list instances with specific OS inventory data values 
SYNOPSIS
    

`gcloud alpha compute instances os-inventory list-instances` [`--inventory-filter`=`INVENTORY_FILTER`] [`--kernel-version`=`KERNEL_VERSION` `--os-shortname`=`OS_SHORTNAME` `--os-version`=`OS_VERSION` `--package-name`=`PACKAGE_NAME` `--package-version`=`PACKAGE_VERSION`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` gcloud alpha compute instances os-inventory list-instances displays all Google Compute Engine instances in a project matching an inventory filter. Run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters) to see the supported filter syntax. 
EXAMPLES
     To list all instances with OS inventory data in a project in table form, run: 
    
    
    gcloud alpha compute instances os-inventory list-instances

To list the URIs of all instances whose OS short name contains rhel, run: 
    
    
    gcloud alpha compute instances os-inventory list-instances --inventory-filter="ShortName:rhel" --uri

To list the URIs of all instances whose OS short name is equal to rhel, run: 
    
    
    gcloud alpha compute instances os-inventory list-instances --os-shortname="rhel" --uri

To list all instances with package google-cloud-sdk of version 235.0.0-0 installed, run: 
    
    
    gcloud alpha compute instances os-inventory list-instances --package-name="google-cloud-sdk" --package-version="235.0.0-0"

To list all instances with package name matching a regex ^google-cloud` available for update through apt, run: 
    
    
    gcloud alpha compute instances os-inventory list-instances --inventory-filter="PackageUpdates.apt[].Name~^google-cloud*"

To list all instances with package update google-cloud-sdk of version greater than or equal to 235.0.0-0 available through apt, run: 
    
    
    gcloud alpha compute instances os-inventory list-instances --inventory-filter="PackageUpdates.apt[].['google-cloud-sdk'].Version>=235.0.0-0"

To list all instances missing the Stackdriver monitoring package stackdriver-agent, run: 
    
    
    gcloud alpha compute instances os-inventory list-instances --inventory-filter="NOT(InstalledPackages:stackdriver-agent)"

To list all Windows instances with an installed qfe hotfix whose ID equals KB4462930, run: 
    
    
    gcloud alpha compute instances os-inventory list-instances --inventory-filter="InstalledPackages.qfe[].HotFixID=KB4462930"

To list all Windows instances with a wua update whose description contains the word Security, run: 
    
    
    gcloud alpha compute instances os-inventory list-instances --inventory-filter="InstalledPackages.wua[].Description:Security"

`

FLAGS
    

`--inventory-filter`=`INVENTORY_FILTER`
     Filter expression for matching against OS inventory criteria 
Exact match values for OS inventory data: 
`--kernel-version`=`KERNEL_VERSION`
     If specified, only instances with this kernel version in their inventory data will be displayed. 
`--os-shortname`=`OS_SHORTNAME`
     If specified, only instances with this OS shortname in their inventory data will be displayed. 
`--os-version`=`OS_VERSION`
     If specified, only instances with this OS version in their inventory data will be displayed. 
`--package-name`=`PACKAGE_NAME`
     If specified, only instances with an installed package of this name in their inventory data will be displayed. 
`--package-version`=`PACKAGE_VERSION`
     If specified with a package name, only instances with the installed package of this version in their inventory data will be displayed. 
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
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute instances os-inventory list-instances](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/os-inventory/list-instances)
    
    
    [gcloud beta compute instances os-inventory list-instances](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/os-inventory/list-instances)
    
    
    [gcloud preview compute instances os-inventory list-instances](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/os-inventory/list-instances)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
