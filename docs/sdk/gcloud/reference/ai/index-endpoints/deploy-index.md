---
url: https://docs.cloud.google.com/sdk/gcloud/reference/ai/index-endpoints/deploy-index/
title: gcloud ai index-endpoints deploy-index \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:47.051038+00:00
---

# gcloud ai index-endpoints deploy-index  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/ai/index-endpoints/deploy-index/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud ai index-endpoints deploy-index Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud ai index-endpoints deploy-index - deploy an index to a Vertex AI index endpoint 
SYNOPSIS
    

`gcloud ai index-endpoints deploy-index` (`INDEX_ENDPOINT` : `--region`=`REGION`) `--deployed-index-id`=`DEPLOYED_INDEX_ID` `--display-name`=`DISPLAY_NAME` `--index`=`INDEX` [`--allowed-issuers`=[`ALLOWED_ISSUERS`,…]] [`--audiences`=[`AUDIENCES`,…]] [`--deployment-group`=`DEPLOYMENT_GROUP`] [`--deployment-tier`=`DEPLOYMENT_TIER`] [`--enable-access-logging`] [`--machine-type`=`MACHINE_TYPE`] [`--max-replica-count`=`MAX_REPLICA_COUNT`] [`--min-replica-count`=`MIN_REPLICA_COUNT`] [`--psc-automation-configs`=[`network`=`NETWORK`],[`project-id`=`PROJECT-ID`]] [`--reserved-ip-ranges`=[`RESERVED_IP_RANGES`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Deploy an index to a Vertex AI index endpoint. 
EXAMPLES
     To deploy index ``345`` to an index endpoint ``456`` with 2 min replica count and 10 max replica count under project ``example`` in region ``us-central1``, within reserved ip ranges ``vertex-ai-ip-range-1`` and ``vertex-ai-ip-range-2`` run: 
    
    
    gcloud ai index-endpoints deploy-index 456 --project=example --region=us-central1 --index=345 --deployed-index-id=deployed-index-345 --display-name=deployed-index-345 --min-replica-count=2 --max-replica-count=10 --reserved-ip-ranges=vertex-ai-ip-range-1,vertex-ai-ip-range-2

POSITIONAL ARGUMENTS
    

Index endpoint resource - The index endpoint to deploy an index. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `index_endpoint` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INDEX_ENDPOINT`
     ID of the index_endpoint or fully qualified identifier for the index_endpoint. 

To set the `name` attribute: 

  * provide the argument `index_endpoint` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Cloud region for the index_endpoint. 

To set the `region` attribute: 

  * provide the argument `index_endpoint` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `ai/region`; 
  * choose one from the prompted list of available regions. 


REQUIRED FLAGS
    

`--deployed-index-id`=`DEPLOYED_INDEX_ID`
     Id of the deployed index. 
`--display-name`=`DISPLAY_NAME`
     Display name of the deployed index. 
`--index`=`INDEX`
     ID of the index. 
OPTIONAL FLAGS
    

`--allowed-issuers`=[`ALLOWED_ISSUERS`,…]
     List of allowed JWT issuers for a deployed index. 

Each entry must be a valid Google service account, in the following format: `service-account-name@project-id.iam.gserviceaccount.com`

`--audiences`=[`AUDIENCES`,…]
     List of JWT audiences that are allowed to access a deployed index. 

JWT containing any of these audiences (<https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32#section> -4.1.3) will be accepted. 

`--deployment-group`=`DEPLOYMENT_GROUP`
     Deployment group can be no longer than 64 characters (eg:`test`, `prod`). If not set, we will use the `default` deployment group. 

Creating deployment_groups with `reserved_ip_ranges` is a recommended practice when the peered network has multiple peering ranges.This creates your deployments from predictable IP spaces for easier traffic administration. 

`--deployment-tier`=`DEPLOYMENT_TIER`
     The deployment tier that the deployed index is deployed to. If not specified, a system-chosen default tier is used. `DEPLOYMENT_TIER` must be (only one value is supported): `storage`. 
`--enable-access-logging`
     If true, online prediction access logs are sent to Cloud Logging. 

These logs are standard server access logs, containing information like timestamp and latency for each prediction request. 

`--machine-type`=`MACHINE_TYPE`
     The machine resources to be used for each node of this deployment. For available machine types, see <https://cloud.google.com/ai-platform-unified/docs/predictions/machine-types>. 
`--max-replica-count`=`MAX_REPLICA_COUNT`
     Maximum number of machine replicas the deployed index will be always deployed on. 
`--min-replica-count`=`MIN_REPLICA_COUNT`
     Minimum number of machine replicas the deployed index will be always deployed on. If specified, the value must be equal to or larger than 1. 
`--psc-automation-configs`=[`network`=`NETWORK`],[`project-id`=`PROJECT-ID`]
     A pair of `project-id` and `network` the PSC index will be deployed to. For example: `--psc-automation-configs=project-id=my-project,network=my-network`. For multiple networks, this flag can be repeated: `--psc-automation-configs=project-id=my-project,network=my-network --psc-automation-configs=project-id=my-project2,network=my-network2`
`--reserved-ip-ranges`=[`RESERVED_IP_RANGES`,…]
     List of reserved IP ranges deployed index will be deployed to. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha ai index-endpoints deploy-index](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/deploy-index)
    
    
    [gcloud beta ai index-endpoints deploy-index](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/index-endpoints/deploy-index)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
