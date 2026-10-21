---
url: https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connect-clusters/create/
title: gcloud managed-kafka connect-clusters create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:41:04.088962+00:00
---

# gcloud managed-kafka connect-clusters create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/connect-clusters/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud managed-kafka connect-clusters create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud managed-kafka connect-clusters create - create a Managed Service for Apache Kafka connect cluster 
SYNOPSIS
    

`gcloud managed-kafka connect-clusters create` (`CONNECT_CLUSTER` : `--location`=`LOCATION`) `--cpu`=`CPU` `--kafka-cluster`=`KAFKA_CLUSTER` `--memory`=`MEMORY` `--primary-subnet`=`PRIMARY_SUBNET` [`--additional-subnet`=`ADDITIONAL_SUBNET`] [`--async`] [`--dns-name`=`DNS_NAME`] [`--labels`=[`KEY`=`VALUE`,…]] [`--secret`=`SECRET`] [`--config-file`=`JSON`|`YAML`|`FILE` | `--configs`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Managed Service for Apache Kafka connect cluster. 
EXAMPLES
     To create a connector cluster, run the following: 
    
    
    gcloud managed-kafka connect-clusters create myconnectorCluster --location=us-central1 --cpu=3 --memory=3GiB --primary-subnet=projects/PROJECT_ID/regions/us-central1/subnetworks/default --kafka-cluster=my-kafka-cluster OR --kafka-cluster=projects/PROJECT_ID/locations/us-central1/clusters/my-kafka-cluster

POSITIONAL ARGUMENTS
    

Connect cluster resource - Identifies the connect cluster that is created. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `connect_cluster` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CONNECT_CLUSTER`
     ID of the connect_cluster or fully qualified identifier for the connect_cluster. 

To set the `connect_cluster` attribute: 

  * provide the argument `connect_cluster` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     ID of the location of the Managed Service for Apache Kafka resource. See <https://cloud.google.com/managed-service-for-apache-kafka/docs/locations> for a list of supported locations. To set the `location` attribute: 

  * provide the argument `connect_cluster` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--cpu`=`CPU`
     The number of vCPUs to provision for the cluster. The minimum is 3. 
`--kafka-cluster`=`KAFKA_CLUSTER`
     The resource path of the Kafka cluster to connect to, or the name of the Kafka cluster to connect to if the cluster is in the same project as the Connect cluster. 
`--memory`=`MEMORY`
     The memory to provision for the cluster in bytes. The value must be between 1 GiB and 8 GiB per vCPU. Ex. 1024Mi, 4Gi. 
`--primary-subnet`=`PRIMARY_SUBNET`
     VPC subnet to make available to the Kafka Connect cluster. Structured like: projects/{project}/regions/{region}/subnetworks/{subnet_id}. The primary subnet is used to create a Private Service Connect (PSC) interface for the Kafka Connect workers. It must be located in the same region as the Connect cluster. 
OPTIONAL FLAGS
    

`--additional-subnet`=`ADDITIONAL_SUBNET`
     (DEPRECATED) Additional subnet to make available to the Kafka Connect cluster. Structured like: projects/{project}/regions/{region}/subnetworks/{subnet_id}. 

The --additional-subnet flag is deprecated and will be removed in a future version. Managed Kafka Connect clusters can now reach any endpoint accessible from the primary subnet without the need to define additional subnets. Please see <https://cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#worker-subnet> for more information. 

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--dns-name`=`DNS_NAME`
     DNS domain name from the subnet's network to be made visible to the Connect Cluster. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`--secret`=`SECRET`
     Secrets to load into workers. Exact SecretVersions from Secret Manager must be provided -- aliases are not supported. Up to 32 secrets may be loaded into one cluster. Format: projects/<project-id>/secrets/<secret-name>/versions/<version-id>
At most one of these can be specified: 

`--config-file`=`JSON`|`YAML`|`FILE`
     The path to the JSON or YAML file containing the configuration that are overridden from the cluster or connector defaults. This also supports inline JSON or YAML. Sets `config_file` value. `Input Example:`
    
    
    --config-file=string

`File Example:`
    
    
    --config-file=path_to_file.(yaml|json)

`--configs`=[`KEY`=`VALUE`,…]
     Configuration for the connect cluster that are overridden from the cluster defaults. The key of the map is a Kafka topic property name, for example: `cleanup.policy=compact`,`compression.type=producer`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `managedkafka/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-service-for-apache-kafka/docs>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha managed-kafka connect-clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/managed-kafka/connect-clusters/create)
    
    
    [gcloud beta managed-kafka connect-clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/managed-kafka/connect-clusters/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
