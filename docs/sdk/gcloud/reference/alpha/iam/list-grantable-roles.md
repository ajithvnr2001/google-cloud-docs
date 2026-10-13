---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/list-grantable-roles/
title: gcloud alpha iam list-grantable-roles \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:27:55.304039+00:00
---

# gcloud alpha iam list-grantable-roles  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/list-grantable-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha iam list-grantable-roles Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha iam list-grantable-roles - list IAM grantable roles for a resource 
SYNOPSIS
    

`gcloud alpha iam list-grantable-roles` `RESOURCE` [`--filter`=`EXPRESSION`] [`--page-size`=`PAGE_SIZE`; default=300] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command displays the list of grantable roles for a resource. The resource can be referenced either via the full resource name or via a URI. User can then add IAM policy bindings to grant the roles. 
EXAMPLES
     List grantable roles for a project: 
    
    
    gcloud alpha iam list-grantable-roles //cloudresourcemanager.googleapis.com/projects/PROJECT_ID

List grantable roles for a resource identified via full resource name: 
    
    
    gcloud alpha iam list-grantable-roles //compute.googleapis.com/projects/example-project/zones/us-central1-f/instances/example-instance

List grantable roles for a resource identified via URI: 
    
    
    gcloud alpha iam list-grantable-roles [https://www.googleapis.com/compute/v1/projects/example-project/\](https://www.googleapis.com/compute/v1/projects/example-project/\\)
    zones/us-central1-f/instances/example-instance

POSITIONAL ARGUMENTS
    

`RESOURCE`
     The full resource name or URI to get the list of roles for. 

See ["Resource Names"](https://cloud.google.com/apis/design/resource_names) for details. To get a URI from most `list` commands in `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)`, pass the `--uri` flag. For example: 
    
    
    [gcloud compute instances list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list) --project prj --uri <https://compute.googleapis.com/compute/v1/projects/prj/zones/us-east1-c/instances/i1> <https://compute.googleapis.com/compute/v1/projects/prj/zones/us-east1-d/instances/i2>

LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`; default=300
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is `300`. Paging may be applied before or after `--filter` and `--limit` depending on the service. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud iam list-grantable-roles](https://docs.cloud.google.com/sdk/gcloud/reference/iam/list-grantable-roles)
    
    
    [gcloud beta iam list-grantable-roles](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/list-grantable-roles)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
