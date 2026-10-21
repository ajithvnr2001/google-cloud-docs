---
url: https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create/
title: gcloud managed-kafka clusters create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:41:01.386794+00:00
---

# gcloud managed-kafka clusters create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud managed-kafka clusters create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud managed-kafka clusters create - create a Managed Service for Apache Kafka cluster 
SYNOPSIS
    

`gcloud managed-kafka clusters create` (`CLUSTER` : `--location`=`LOCATION`) `--cpu`=`CPU` `--memory`=`MEMORY` `--subnets`=[`SUBNETS`,…] [`--allowed-source-ip-ranges`=[`ALLOWED_SOURCE_IP_RANGES`,…]] [`--async`] [`--no-auto-rebalance`] [`--broker-disk`=`BROKER_DISK`] [`--encryption-key`=`ENCRYPTION_KEY`] [`--labels`=[`KEY`=`VALUE`,…]] [`--mtls-ca-pools`=[`MTLS_CA_POOLS`,…]] [`--[no-]public-cluster`] [`--ssl-principal-mapping-rules`=`SSL_PRINCIPAL_MAPPING_RULES`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Managed Service for Apache Kafka cluster. 
EXAMPLES
     To create a cluster, run the following: 
    
    
    gcloud managed-kafka clusters create mycluster --location=us-central1 --cpu=3 --memory=3GiB --subnets=projects/PROJECT_ID/regions/us-central1/subnetworks/default

POSITIONAL ARGUMENTS
    

Cluster resource - Identifies the cluster for which the command runs. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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

`--location`=`LOCATION`
     ID of the location of the Managed Service for Apache Kafka resource. See <https://cloud.google.com/managed-service-for-apache-kafka/docs/locations> for a list of supported locations. To set the `location` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--cpu`=`CPU`
     The number of vCPUs to provision for the cluster. The minimum is 3. 
`--memory`=`MEMORY`
     The memory to provision for the cluster in bytes. The value must be between 1 GiB and 8 GiB per vCPU. Ex. 1024Mi, 4Gi. 
`--subnets`=[`SUBNETS`,…]
     A comma-separated list of VPC subnets from which the cluster is accessible. Both broker and bootstrap server IP addresses and DNS entries are automatically created in each subnet. Only one subnet per network is allowed, and the subnet must be located in the same region as the cluster. The project may differ. A minimum of 1 subnet is required. A maximum of 10 subnets can be specified. Use commas to separate multiple subnets. The name of the subnet must be in the format projects/``PROJECT_ID``/regions/``REGION``/subnetworks/``SUBNET``. 
OPTIONAL FLAGS
    

`--allowed-source-ip-ranges`=[`ALLOWED_SOURCE_IP_RANGES`,…]
     A comma-separated list of IPv4 ranges in CIDR notation that are allowed to connect to the public cluster. Use this flag only if --public-cluster is enabled. Example: `--allowed-source-ip-ranges=203.0.113.0/24,198.51.100.0/24`. To protect your cluster, allow access from only trusted external IP ranges. Don't expose your cluster to untrusted ranges. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--auto-rebalance`
     Whether the automatic rebalancing is enabled. If automatic rebalancing is enabled, topic partitions are rebalanced among brokers when the number of CPUs in the cluster changes. Automatic rebalancing is enabled by default. Use \--no-auto-rebalance to disable this flag. Enabled by default, use `--no-auto-rebalance` to disable. 
`--broker-disk`=`BROKER_DISK`
     The amount of local disk to provision for each broker. Can be specified as a plain integer (defaults to GiB) or with units (e.g., 500Gi, 500GiB, 1Ti, 1TiB). Minimum: 100 Gibibytes. 
`--encryption-key`=`ENCRYPTION_KEY`
     The relative resource path of the Cloud KMS key to use for encryption in the form: projects/``PROJECT_ID``/locations/``LOCATION``/keyRings/``KEY_RING``/cryptoKeys/``KEY``. The key must be located in the same region as the cluster. The key cannot be changed once set. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`--mtls-ca-pools`=[`MTLS_CA_POOLS`,…]
     A comma-separated list of CA pools from the Google Cloud Certificate Authority Service. The root certificates of these CA pools will be installed in the truststore of each broker in the cluster for use with mTLS. A maximum of 10 CA pools can be specified. CA pools can be in a different project and region than the cluster. This command overwrites the entire set of pools currently configured on the cluster. If you want to add a new pool to an existing configuration, you must provide the full list of both the old and new CA pools in the command. Each CA pool must be in the format projects/``PROJECT_ID``/locations/``LOCATION``/caPools/``CA_POOL``. Clear the CA pools using the `--clear-mtls-ca-pools` flag. 
`--[no-]public-cluster`
     Enable a public cluster. If disabled, public cluster config is cleared. Use `--public-cluster` to enable and `--no-public-cluster` to disable. 
`--ssl-principal-mapping-rules`=`SSL_PRINCIPAL_MAPPING_RULES`
     The rules for mapping mTLS certificate Distinguished Names (DNs) to shortened principal names for Kafka ACLs. This flag corresponds exactly to the `ssl.principal.mapping.rules` broker config and matches the format and syntax defined in the Apache Kafka documentation. Setting or modifying this field will trigger a rolling restart of the Kafka brokers to apply the change. An empty string means that the default Kafka behavior is used. Example: "RULE:^CN=(.`?),OU=ServiceUsers.`$/$1@example.com/,DEFAULT" 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `managedkafka/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-service-for-apache-kafka/docs>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha managed-kafka clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/managed-kafka/clusters/create)
    
    
    [gcloud beta managed-kafka clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/managed-kafka/clusters/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
