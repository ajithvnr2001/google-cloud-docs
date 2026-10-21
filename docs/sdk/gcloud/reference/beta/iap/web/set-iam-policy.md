---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/web/set-iam-policy/
title: gcloud beta iap web set-iam-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:03:58.797710+00:00
---

# gcloud beta iap web set-iam-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/web/set-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta iap web set-iam-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta iap web set-iam-policy - set the IAM policy for an IAP IAM resource 
SYNOPSIS
    

`gcloud beta iap web set-iam-policy` `POLICY_FILE` [`--region`=`REGION` `--resource-type`=`RESOURCE_TYPE` `--service`=`SERVICE` `--version`=`VERSION` `--agent`=`AGENT` | `--endpoint`=`ENDPOINT` | `--mcp-server`=`MCP_SERVER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command replaces the existing IAM policy for an IAP IAM resource, given a file encoded in JSON or YAML that contains the IAM policy. If the given policy file specifies an "etag" value, then the replacement will succeed only if the policy already in place matches that etag. (An etag obtained via $ [gcloud beta iap web get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/web/get-iam-policy) will prevent the replacement if the policy for the resource has been subsequently updated.) A policy file that does not contain an etag value will replace any existing policy for the resource. 
EXAMPLES
     To set the IAM policy for the web accesses to the IAP protected resources within the active project, run: 
    
    
    gcloud beta iap web set-iam-policy POLICY_FILE

To set the IAM policy for the web accesses to the IAP protected resources within a project, run: 
    
    
    gcloud beta iap web set-iam-policy POLICY_FILE --project=PROJECT_ID

To set the IAM policy for the web accesses to the IAP protected resources within an App Engine application, run: 
    
    
    gcloud beta iap web set-iam-policy POLICY_FILE --resource-type=app-engine

To set the IAM policy for the web accesses to the IAP protected resources within an App Engine service, run: 
    
    
    gcloud beta iap web set-iam-policy POLICY_FILE --resource-type=app-engine --service=SERVICE_ID

To set the IAM policy for the web accesses to the IAP protected resources within an App Engine service version, run: 
    
    
    gcloud beta iap web set-iam-policy POLICY_FILE --resource-type=app-engine --service=SERVICE_ID --version=VERSION

To set the IAM policy for the web accesses to the IAP protected resources within all backend services, run: 
    
    
    gcloud beta iap web set-iam-policy POLICY_FILE --resource-type=backend-services

To set the IAM policy for the web accesses to the IAP protected resources within a backend service, run: 
    
    
    gcloud beta iap web set-iam-policy POLICY_FILE --resource-type=backend-services --service=SERVICE_ID

To set the IAM policy for the web accesses to the IAP protected resources within a regional backend service, run: 
    
    
    gcloud beta iap web set-iam-policy POLICY_FILE --resource-type=backend-services --service=SERVICE_ID --region=REGION

To set the IAM policy for the web accesses to the IAP protected resources within a Cloud Run service, run: 
    
    
    gcloud beta iap web set-iam-policy POLICY_FILE --resource-type=cloud-run --service=SERVICE_ID --region=REGION

POSITIONAL ARGUMENTS
    

`POLICY_FILE`
     JSON or YAML file containing the IAM policy. 
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
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud iap web set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/iap/web/set-iam-policy)
    
    
    [gcloud alpha iap web set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/web/set-iam-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
