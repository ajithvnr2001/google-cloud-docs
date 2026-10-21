---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/managed-kafka/clusters/update/
title: gcloud alpha managed-kafka clusters update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:33:03.566152+00:00
---

# gcloud alpha managed-kafka clusters update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/managed-kafka/clusters/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha managed-kafka clusters update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha managed-kafka clusters update - update a Managed Service for Apache Kafka cluster 
SYNOPSIS
    

`gcloud alpha managed-kafka clusters update` (`CLUSTER` : `--location`=`LOCATION`) (`--allowed-source-ip-ranges`=[`ALLOWED_SOURCE_IP_RANGES`,…] `--auto-rebalance` `--broker-disk`=`BROKER_DISK` `--cpu`=`CPU` `--dns-zone-target`=`DNS_ZONE_TARGET` `--labels`=[`KEY`=`VALUE`,…] `--memory`=`MEMORY` `--psc-resource-target`=`PSC_RESOURCE_TARGET` `--[no-]public-cluster` `--ssl-principal-mapping-rules`=`SSL_PRINCIPAL_MAPPING_RULES` `--subnets`=[`SUBNETS`,…] `--clear-mtls-ca-pools` | `--mtls-ca-pools`=[`MTLS_CA_POOLS`,…]) [`--allow-broker-downscale-on-cluster-upscale`] [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update a Managed Service for Apache Kafka cluster. 
EXAMPLES
     To update an attribute in a cluster named mycluster located in us-central1, such as the CPU, run the following: 
    
    
    gcloud alpha managed-kafka clusters update mycluster --location=us-central1 --cpu=3

POSITIONAL ARGUMENTS
    

Cluster resource - Identifies the cluster to be updated. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
    

At least one of these must be specified: 

`--allowed-source-ip-ranges`=[`ALLOWED_SOURCE_IP_RANGES`,…]
     A comma-separated list of IPv4 ranges in CIDR notation that are allowed to connect to the public cluster. Use this flag only if --public-cluster is enabled. Example: `--allowed-source-ip-ranges=203.0.113.0/24,198.51.100.0/24`. To protect your cluster, allow access from only trusted external IP ranges. Don't expose your cluster to untrusted ranges. 
`--auto-rebalance`
     Whether the automatic rebalancing is enabled. If automatic rebalancing is enabled, topic partitions are rebalanced among brokers when the number of CPUs in the cluster changes. Automatic rebalancing is enabled by default. Use \--no-auto-rebalance to disable this flag. 
`--broker-disk`=`BROKER_DISK`
     The amount of local disk to provision for each broker. Can be specified as a plain integer (defaults to GiB) or with units (e.g., 500Gi, 500GiB, 1Ti, 1TiB). Minimum: 100 Gibibytes. 
`--cpu`=`CPU`
     The number of vCPUs to provision for the cluster. The minimum is 3. 
`--dns-zone-target`=`DNS_ZONE_TARGET`
     The Private DNS Zone target config. `DNS_ZONE_TARGET` must be one of: 

`cluster-project`
     The DNS Zone is created in the Cluster's project. 
`cluster-project-manual-binding`
     The DNS Zone is created in the Cluster's project, and automated binding is skipped. 
`network-project`
     The DNS Zone is created in the VPC Network's project. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`--memory`=`MEMORY`
     The memory to provision for the cluster in bytes. The value must be between 1 GiB and 8 GiB per vCPU. Ex. 1024Mi, 4Gi. 
`--psc-resource-target`=`PSC_RESOURCE_TARGET`
     The Private Service Connect (PSC) resource target config. `PSC_RESOURCE_TARGET` must be one of: 

`cluster-project`
     The PSC connections are created in the Cluster's project. 
`network-project`
     The PSC connections are created in the VPC Network's project. 
`--[no-]public-cluster`
     Enable a public cluster. If disabled, public cluster config is cleared. Use `--public-cluster` to enable and `--no-public-cluster` to disable. 
`--ssl-principal-mapping-rules`=`SSL_PRINCIPAL_MAPPING_RULES`
     The rules for mapping mTLS certificate Distinguished Names (DNs) to shortened principal names for Kafka ACLs. This flag corresponds exactly to the `ssl.principal.mapping.rules` broker config and matches the format and syntax defined in the Apache Kafka documentation. Setting or modifying this field will trigger a rolling restart of the Kafka brokers to apply the change. An empty string means that the default Kafka behavior is used. Example: "RULE:^CN=(.`?),OU=ServiceUsers.`$/$1@example.com/,DEFAULT" 
`--subnets`=[`SUBNETS`,…]
     A comma-separated list of VPC subnets from which the cluster is accessible. Both broker and bootstrap server IP addresses and DNS entries are automatically created in each subnet. Only one subnet per network is allowed, and the subnet must be located in the same region as the cluster. The project may differ. A minimum of 1 subnet is required. A maximum of 10 subnets can be specified. Use commas to separate multiple subnets. The name of the subnet must be in the format projects/``PROJECT_ID``/regions/``REGION``/subnetworks/``SUBNET``. 
At most one of these can be specified: 

`--clear-mtls-ca-pools`
     Remove all the CA pools from the cluster. This will remove all root certificates from the truststore of each broker in the cluster. 
`--mtls-ca-pools`=[`MTLS_CA_POOLS`,…]
     A comma-separated list of CA pools from the Google Cloud Certificate Authority Service. The root certificates of these CA pools will be installed in the truststore of each broker in the cluster for use with mTLS. A maximum of 10 CA pools can be specified. CA pools can be in a different project and region than the cluster. This command overwrites the entire set of pools currently configured on the cluster. If you want to add a new pool to an existing configuration, you must provide the full list of both the old and new CA pools in the command. Each CA pool must be in the format projects/``PROJECT_ID``/locations/``LOCATION``/caPools/``CA_POOL``. Clear the CA pools using the `--clear-mtls-ca-pools` flag. 
OPTIONAL FLAGS
    

`--allow-broker-downscale-on-cluster-upscale`
     If enabled, this setting allows an update operation that could significantly decrease the per-broker vCPU and/or memory allocation, which can lead to reduced performance and availability. By default, an update operation will fail if it results in a reduction of 10% or more to the brokers' vCPU or memory allocation. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `managedkafka/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-service-for-apache-kafka/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud managed-kafka clusters update](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/update)
    
    
    [gcloud beta managed-kafka clusters update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/managed-kafka/clusters/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
