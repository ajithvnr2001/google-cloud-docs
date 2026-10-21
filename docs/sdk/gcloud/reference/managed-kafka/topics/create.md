---
url: https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/create/
title: gcloud managed-kafka topics create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:41:10.975004+00:00
---

# gcloud managed-kafka topics create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/topics/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud managed-kafka topics create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud managed-kafka topics create - create a Managed Service for Apache Kafka topic 
SYNOPSIS
    

`gcloud managed-kafka topics create` (`TOPIC` : `--cluster`=`CLUSTER` `--location`=`LOCATION`) `--partitions`=`PARTITIONS` `--replication-factor`=`REPLICATION_FACTOR` [`--configs`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Managed Service for Apache Kafka topic. 
EXAMPLES
     To create a topic in a cluster named mycluster located in us-central1, run the following: 
    
    
    gcloud managed-kafka topics create mytopic --cluster=mycluster --location=us-central1 --partitions=1 --replication-factor=3

POSITIONAL ARGUMENTS
    

Topic resource - Identifies the name of the topic that this command creates. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `topic` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TOPIC`
     ID of the topic or fully qualified identifier for the topic. 

To set the `topic` attribute: 

  * provide the argument `topic` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--cluster`=`CLUSTER`
     The cluster name. To set the `cluster` attribute: 

  * provide the argument `topic` on the command line with a fully specified name; 
  * provide the argument `--cluster` on the command line. 


`--location`=`LOCATION`
     ID of the location of the Managed Service for Apache Kafka resource. See <https://cloud.google.com/managed-service-for-apache-kafka/docs/locations> for a list of supported locations. To set the `location` attribute: 

  * provide the argument `topic` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--partitions`=`PARTITIONS`
     The number of partitions in a topic. You can increase the partition count for a topic, but you cannot decrease it. Increasing partitions for a topic that uses a key might change how messages are distributed. 
`--replication-factor`=`REPLICATION_FACTOR`
     The number of replicas of each partition. A replication factor of 3 is recommended for high availability. 
OPTIONAL FLAGS
    

`--configs`=[`KEY`=`VALUE`,…]
     Configuration for the topic that are overridden from the cluster defaults. The key of the map is a Kafka topic property name, for example: `cleanup.policy=compact`,`compression.type=producer`. If you provide a map with a key that already exists, only that configuration is updated. If the map contains a key that does not exist, the entry is appended to the topic configuration. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `managedkafka/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-service-for-apache-kafka/docs>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha managed-kafka topics create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/managed-kafka/topics/create)
    
    
    [gcloud beta managed-kafka topics create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/managed-kafka/topics/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
