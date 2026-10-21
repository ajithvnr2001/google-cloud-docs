---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/web/get-iam-policy/
title: gcloud beta iap web get-iam-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:40:57.053129+00:00
---

# gcloud beta iap web get-iam-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/web/get-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta iap web get-iam-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta iap web get-iam-policy - get IAM policy for an IAP IAM resource 
SYNOPSIS
    

`gcloud beta iap web get-iam-policy` [`--region`=`REGION` `--resource-type`=`RESOURCE_TYPE` `--service`=`SERVICE` `--version`=`VERSION` `--agent`=`AGENT` | `--endpoint`=`ENDPOINT` | `--mcp-server`=`MCP_SERVER`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta iap web get-iam-policy` displays the IAM policy associated with an IAP IAM resource. If formatted as JSON, the output can be edited and used as a policy file for set-iam-policy. The output includes an "etag" field identifying the version emitted and allowing detection of concurrent policy updates; see $ [gcloud beta iap web set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/web/set-iam-policy) for additional details. 
EXAMPLES
     To get the IAM policy for the web accesses to the IAP protected resources within the active project, run: 
    
    
    gcloud beta iap web get-iam-policy

To get the IAM policy for the web accesses to the IAP protected resources within a project, run: 
    
    
    gcloud beta iap web get-iam-policy --project=PROJECT_ID

To get the IAM policy for the web accesses to the IAP protected resources within an App Engine application, run: 
    
    
    gcloud beta iap web get-iam-policy --resource-type=app-engine

To get the IAM policy for the web accesses to the IAP protected resources within an App Engine service, run: 
    
    
    gcloud beta iap web get-iam-policy --resource-type=app-engine --service=SERVICE_ID

To get the IAM policy for the web accesses to the IAP protected resources within an App Engine service version, run: 
    
    
    gcloud beta iap web get-iam-policy --resource-type=app-engine --service=SERVICE_ID --version=VERSION

To get the IAM policy for the web accesses to the IAP protected resources within all backend services, run: 
    
    
    gcloud beta iap web get-iam-policy --resource-type=backend-services

To get the IAM policy for the web accesses to the IAP protected resources within a backend service, run: 
    
    
    gcloud beta iap web get-iam-policy --resource-type=backend-services --service=SERVICE_ID

To get the IAM policy for the web accesses to the IAP protected resources within a regional backend service, run: 
    
    
    gcloud beta iap web get-iam-policy --resource-type=backend-services --service=SERVICE_ID --region=REGION

To get the IAM policy for the web accesses to the IAP protected resources within a Cloud Run service, run: 
    
    
    gcloud beta iap web get-iam-policy --resource-type=cloud-run --service=SERVICE_ID --region=REGION

FLAGS
    

`--region`=`REGION`
     Region name. Not applicable for `resource-type=app-engine`. Required when `resource-type=backend-services` and regional scoped. Not applicable for global backend-services. Required when `resource-type=cloud-run`. 
`--resource-type`=`RESOURCE_TYPE`
     Resource type of the IAP resource. `RESOURCE_TYPE` must be one of: `app-engine`, `backend-services`, `forwarding-rule`, `cloud-run`, `agent-registry`. 
`--service`=`SERVICE`
     Service name. 
`--version`=`VERSION`
     Service version. Should only be specified with `--resource-type=app-engine`. 
At most one of these can be specified: 

`--agent`=`AGENT`
     Agent ID for the agent-registry resource type. 
`--endpoint`=`ENDPOINT`
     Endpoint ID for the agent-registry resource type. 
`--mcp-server`=`MCP_SERVER`
     MCP server ID for the agent-registry resource type. 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud iap web get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/iap/web/get-iam-policy)
    
    
    [gcloud alpha iap web get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/web/get-iam-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
