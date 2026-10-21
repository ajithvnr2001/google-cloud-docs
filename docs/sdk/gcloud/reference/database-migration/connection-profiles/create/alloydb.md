---
url: https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb/
title: gcloud database-migration connection-profiles create alloydb \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:47.629171+00:00
---

# gcloud database-migration connection-profiles create alloydb  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud database-migration connection-profiles create alloydb Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud database-migration connection-profiles create alloydb - create a Database Migration Service connection profile for AlloyDB 
SYNOPSIS
    

`gcloud database-migration connection-profiles create alloydb` (`CONNECTION_PROFILE` : `--region`=`REGION`) `--cpu-count`=`CPU_COUNT` `--password`=`PASSWORD` `--primary-id`=`PRIMARY_ID` [`--no-async`] [`--authorized-network-cidr-ranges`=[`NETWORK`,…]] [`--cluster-labels`=[`KEY`=`VALUE`,…]] [`--database-flags`=[`FLAG`=`VALUE`,…]] [`--database-version`=`DATABASE_VERSION`] [`--display-name`=`DISPLAY_NAME`] [`--enable-outbound-public-ip`] [`--enable-public-ip`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--labels`=[`KEY`=`VALUE`,…]] [`--machine-type`=`MACHINE_TYPE`] [`--network`=`NETWORK`] [`--primary-labels`=[`KEY`=`VALUE`,…]] [`--role`=`ROLE`] [`--kms-key`=`KMS_KEY` : `--kms-keyring`=`KMS_KEYRING` `--kms-project`=`KMS_PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Database Migration Service destination connection profile for AlloyDB. This will create an AlloyDB cluster and primary instance. 
EXAMPLES
     To create a connection profile for AlloyDB: 
    
    
    gcloud database-migration connection-profiles create alloydb my-profile --region=us-central1 --password=my_password --primary-id=my-primary --cpu-count=2

POSITIONAL ARGUMENTS
    

Connection profile resource - The connection profile to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `connection_profile` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CONNECTION_PROFILE`
     ID of the connection_profile or fully qualified identifier for the connection_profile. 

To set the `connection_profile` attribute: 

  * provide the argument `connection_profile` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The Cloud region for the connection_profile. 

To set the `region` attribute: 

  * provide the argument `connection_profile` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


REQUIRED FLAGS
    

`--cpu-count`=`CPU_COUNT`
     Whole number value indicating how many vCPUs the machine should contain. Each vCPU count corresponds to a N2 high-mem machine: (https://cloud.google.com/compute/docs/general-purpose-machines#n2_machines). `CPU_COUNT` must be one of: `2`, `4`, `8`, `16`, `32`, `64`. 
`--password`=`PASSWORD`
     Initial password for the 'postgres' user. 
`--primary-id`=`PRIMARY_ID`
     The ID of the primary instance for this AlloyDB cluster. 
OPTIONAL FLAGS
    

`--no-async`
     Waits for the operation in progress to complete before returning. 
`--authorized-network-cidr-ranges`=[`NETWORK`,…]
     Comma-separated list of CIDR ranges that can connect to the AlloyDB instance. 
`--cluster-labels`=[`KEY`=`VALUE`,…]
     The resource labels for an AlloyDB cluster. An object containing a list of "key": "value" pairs. 
`--database-flags`=[`FLAG`=`VALUE`,…]
     Comma-separated list of database flags to set on the AlloyDB primary instance. Use an equals sign to separate the flag name and value. Flags without values, like skip_grant_tables, can be written out without a value, e.g., `skip_grant_tables=`. Use on/off values for booleans. View AlloyDB's documentation for allowed flags (e.g., `--database-flags max_allowed_packet=55555,skip_grant_tables=,log_output=1`). 
`--database-version`=`DATABASE_VERSION`
     Database engine major version. `DATABASE_VERSION` must be one of: `POSTGRES_14`, `POSTGRES_15`, `POSTGRES_16`, `POSTGRES_17`. 
`--display-name`=`DISPLAY_NAME`
     A user-friendly name for the connection profile. The display name can include letters, numbers, spaces, and hyphens, and must start with a letter. 
`--enable-outbound-public-ip`
     If true, Enables an outbound public IP address to support a database server sending requests out into the internet. 
`--enable-public-ip`
     If true, the AlloyDB instance will be accessible via public IP. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--machine-type`=`MACHINE_TYPE`
     Machine type of the VM instance. E.g. "n2-highmem-4", "n2-highmem-8", "c4a-highmem-4-lssd". cpu_count must match the number of vCPUs in the machine type. 
`--network`=`NETWORK`
     The VPC network from which the AlloyDB instance is accessible via private IP. For example, projects/myProject/global/networks/default. This setting cannot be updated after it is set. 
`--primary-labels`=[`KEY`=`VALUE`,…]
     The resource labels for an AlloyDB primary instance. An object containing a list of "key": "value" pairs. 
`--role`=`ROLE`
     The role of the connection profile. `ROLE` must be one of: `SOURCE`, `DESTINATION`. 
Kms key resource - Name of the CMEK (customer-managed encryption key) used for this AlloyDB cluster. For example, projects/myProject/locations/us-central1/keyRings/myKeyRing/cryptoKeys/myKey. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `region` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


`--kms-key`=`KMS_KEY`
     ID of the kms-key or fully qualified identifier for the kms-key. 

To set the `kms-key` attribute: 

  * provide the argument `--kms-key` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--kms-keyring`=`KMS_KEYRING`
     The CMEK keyring id of the kms-key. 

To set the `kms-keyring` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-keyring` on the command line. 


`--kms-project`=`KMS_PROJECT`
     The Cloud project id for the kms-key. 

To set the `kms-project` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-project` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
