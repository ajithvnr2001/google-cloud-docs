---
url: https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/add-cluster-endpoints/
title: gcloud redis clusters add-cluster-endpoints \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:17:56.216138+00:00
---

# gcloud redis clusters add-cluster-endpoints  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/add-cluster-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud redis clusters add-cluster-endpoints Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud redis clusters add-cluster-endpoints - add more cluster endpoints 
SYNOPSIS
    

`gcloud redis clusters add-cluster-endpoints` (`CLUSTER` : `--region`=`REGION`) `--cluster-endpoint`=[`psc-connection`=`PSC-CONNECTION`] [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This is required to enable multi-vpc for Redis cluster. 

To add one cluster endpoint to an existing Redis cluster, two PSC connections MUST be added as a pair: one for the Redis cluster's discovery service attachment and the other for the additional service attachment. 

Multiple cluster endpoints COULD be added simultaneously. 

This command can fail for the following reasons: 

  * The cluster specified does not exist. 
  * The number of connections provided to a cluster endpoint are not in pairs. 
  * One of the connections is not found. 


EXAMPLES
     To connect redis cluster to one additional VPC, run: 
    
    
    gcloud redis clusters add-cluster-endpoints my-redis-cluster add-cluster-endpoints --cluster-endpoint='["psc-connection":[{"psc-connection-id":"$ID","address":"$IP","network":"projects/$PROJECT/global/networks/$NETWORK","forwarding-rule":"projects/$PROJECT/regions/us-east1/forwardingRules/$FR_NAME","service-attachment":"projects/$PROJECT/regions/$REGION/serviceAttachments/$SA_NAME"},{$ADDITIONAL_PSC_CONNECTION}]]' --cluster_endpoint=$ADDITIONAL_CLUSTER_ENDPOINT $PSCConnectionID SHOULD be extracted from forwarding rules. E.g. 75311697652483351

POSITIONAL ARGUMENTS
    

Cluster resource - Arguments and flags that specify the Memorystore Redis cluster you want to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CLUSTER`
     ID of the cluster or fully qualified identifier for the cluster. 

To set the `cluster` attribute: 

  * provide the argument `cluster` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The name of the Redis region of the cluster. Overrides the default redis/region property value for this command invocation. To set the `region` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `redis/region`. 


REQUIRED FLAGS
    

`--cluster-endpoint`=[`psc-connection`=`PSC-CONNECTION`]
     Required, Resource details of a redis cluster endpoint. 

`psc-connection`
     Sets `psc-connection` value. 

`address`
     Sets `address` value. 
`forwarding-rule`
     Sets `forwarding-rule` value. 
`network`
     Sets `network` value. 
`psc-connection-id`
     Sets `psc-connection-id` value. 
`service-attachment`
     Sets `service-attachment` value. 
`Shorthand Example:`
    
    
    --cluster-endpoint=psc-connection=[{address=string,forwarding-rule=string,network=string,psc-connection-id=string,service-attachment=string}] --cluster-endpoint=psc-connection=[{address=string,forwarding-rule=string,network=string,psc-connection-id=string,service-attachment=string}]

`JSON Example:`
    
    
    --cluster-endpoint='[{"psc-connection": [{"address": "string", "forwarding-rule": "string", "network": "string", "psc-connection-id": "string", "service-attachment": "string"}]}]'

`File Example:`
    
    
    --cluster-endpoint=path_to_file.(yaml|json)

OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `redis/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/memorystore/docs/redis/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha redis clusters add-cluster-endpoints](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/redis/clusters/add-cluster-endpoints)
    
    
    [gcloud beta redis clusters add-cluster-endpoints](https://docs.cloud.google.com/sdk/gcloud/reference/beta/redis/clusters/add-cluster-endpoints)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
