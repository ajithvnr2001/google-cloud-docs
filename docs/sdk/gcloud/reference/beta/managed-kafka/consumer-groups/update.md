---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/managed-kafka/consumer-groups/update/
title: gcloud beta managed-kafka consumer-groups update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:18:18.845923+00:00
---

# gcloud beta managed-kafka consumer-groups update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/managed-kafka/consumer-groups/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta managed-kafka consumer-groups update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta managed-kafka consumer-groups update - update a Managed Service for Apache Kafka consumer group 
SYNOPSIS
    

`gcloud beta managed-kafka consumer-groups update` (`CONSUMER_GROUP` : `--cluster`=`CLUSTER` `--location`=`LOCATION`) `--topics-file`=`JSON`|`YAML`|`FILE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a Managed Service for Apache Kafka consumer group. 
EXAMPLES
     To specify a file for updating the topics of a consumer group, run the following: 
    
    
    $gcloud beta managed-kafka consumer-groups update myconsumergroup |
        --cluster=mycluster \
        --location=us-central1 \
        --topics-file=topics.json

To update the topics of a consumer group with inline JSON, run the following: 
    
    
    $gcloud beta managed-kafka consumer-groups update myconsumergroup |
        --cluster=mycluster \
        --location=us-central1 \
        --topics-file='{"topic":{"partitions":{"0":{"offset":1,"metadata":"metadata"}}}}'

POSITIONAL ARGUMENTS
    

Consumer group resource - Identifies the consumer group to be updated. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `consumer_group` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CONSUMER_GROUP`
     ID of the consumer_group or fully qualified identifier for the consumer_group. 

To set the `consumer_group` attribute: 

  * provide the argument `consumer_group` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--cluster`=`CLUSTER`
     The cluster name. To set the `cluster` attribute: 

  * provide the argument `consumer_group` on the command line with a fully specified name; 
  * provide the argument `--cluster` on the command line. 


`--location`=`LOCATION`
     ID of the location of the Managed Service for Apache Kafka resource. See <https://cloud.google.com/managed-service-for-apache-kafka/docs/locations> for a list of supported locations. To set the `location` attribute: 

  * provide the argument `consumer_group` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--topics-file`=`JSON`|`YAML`|`FILE`
     The path to the JSON or YAML file containing the configuration of the topics to be updated for the consumer group. This also supports inline JSON or YAML. Required, sets `topics_file` value. `Input Example:`
    
    
    --topics-file=string

`File Example:`
    
    
    --topics-file=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `managedkafka/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-service-for-apache-kafka/docs>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud managed-kafka consumer-groups update](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/consumer-groups/update)
    
    
    [gcloud alpha managed-kafka consumer-groups update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/managed-kafka/consumer-groups/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
