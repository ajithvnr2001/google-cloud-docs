---
url: https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connectors/create/
title: gcloud managed-kafka connectors create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:41:05.389946+00:00
---

# gcloud managed-kafka connectors create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connectors/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud managed-kafka connectors create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud managed-kafka connectors create - create a Managed Service for Apache Kafka connector 
SYNOPSIS
    

`gcloud managed-kafka connectors create` (`CONNECTOR` : `--connect-cluster`=`CONNECT_CLUSTER` `--location`=`LOCATION`) (`--config-file`=`JSON`|`YAML`|`FILE` | `--configs`=[`KEY`=`VALUE`,…]) [`--task-retry-disabled`] [`--task-restart-max-backoff`=`TASK_RESTART_MAX_BACKOFF` `--task-restart-min-backoff`=`TASK_RESTART_MIN_BACKOFF`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Managed Service for Apache Kafka connector. 
EXAMPLES
     To create a connector, run the following: 
    
    
    gcloud managed-kafka connectors create myconnector --location=us-central1 --connect-cluster=mycluster --configs=connector.class="com.google.pubsub.kafka.source.CloudPubSubSourceConnector",cps.subscription="my-subscription",… [--task-restart-min-backoff=60s] [--task-restart-max-backoff=30m] [--task-retry-disabled=true] OR
    gcloud managed-kafka connectors create myconnector --location=us-central1 --connect-cluster=mycluster --config-file=my-config-file.yaml [--task-restart-min-backoff=60s] [--task-restart-max-backoff=30m] [--task-retry-disabled=true]

POSITIONAL ARGUMENTS
    

Connector resource - Identifies the connector for which the command runs. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `connector` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CONNECTOR`
     ID of the connector or fully qualified identifier for the connector. 

To set the `connector` attribute: 

  * provide the argument `connector` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--connect-cluster`=`CONNECT_CLUSTER`
     The connect cluster name. To set the `connect-cluster` attribute: 

  * provide the argument `connector` on the command line with a fully specified name; 
  * provide the argument `--connect-cluster` on the command line. 


`--location`=`LOCATION`
     ID of the location of the Managed Service for Apache Kafka resource. See <https://cloud.google.com/managed-service-for-apache-kafka/docs/locations> for a list of supported locations. To set the `location` attribute: 

  * provide the argument `connector` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--config-file`=`JSON`|`YAML`|`FILE`
     The path to the JSON or YAML file containing the configuration that are overridden from the connector defaults. This also supports inline JSON or YAML. Sets `config_file` value. `Input Example:`
    
    
    --config-file=string

`File Example:`
    
    
    --config-file=path_to_file.(yaml|json)

`--configs`=[`KEY`=`VALUE`,…]
     Configuration for the connector that are overridden from the connector defaults. The key of the map is a Kafka topic property name, for example: `cleanup.policy=compact`,`compression.type=producer`. 
OPTIONAL FLAGS
    

`--task-retry-disabled`
     Disable default task retry policy. 
`--task-restart-max-backoff`=`TASK_RESTART_MAX_BACKOFF`
     The maximum amount of time to wait before retrying a failed task in seconds. This sets an upper bound for the backoff delay. The default value is 1800s (30 minutes). See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--task-restart-min-backoff`=`TASK_RESTART_MIN_BACKOFF`
     The minimum amount of time to wait before retrying a failed task in seconds. This sets a lower bound for the backoff delay. The default value is 60s. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `managedkafka/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-service-for-apache-kafka/docs>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha managed-kafka connectors create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/managed-kafka/connectors/create)
    
    
    [gcloud beta managed-kafka connectors create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/managed-kafka/connectors/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
