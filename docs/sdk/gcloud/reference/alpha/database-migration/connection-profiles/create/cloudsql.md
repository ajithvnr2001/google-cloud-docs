---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/database-migration/connection-profiles/create/cloudsql/
title: gcloud alpha database-migration connection-profiles create cloudsql \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:31:23.241689+00:00
---

# gcloud alpha database-migration connection-profiles create cloudsql  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/database-migration/connection-profiles/create/cloudsql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha database-migration connection-profiles create cloudsql Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha database-migration connection-profiles create cloudsql - create a Database Migration Service connection profile for Cloud SQL 
SYNOPSIS
    

`gcloud alpha database-migration connection-profiles create cloudsql` (`CONNECTION_PROFILE` : `--region`=`REGION`) `--database-version`=`DATABASE_VERSION` `--source-id`=`SOURCE_ID` `--tier`=`TIER` [`--activation-policy`=`ACTIVATION_POLICY`] [`--no-async`] [`--authorized-networks`=`NETWORK`,[`NETWORK`,…]] [`--no-auto-storage-increase`] [`--availability-type`=`AVAILABILITY_TYPE`] [`--data-disk-size`=`DATA_DISK_SIZE`] [`--data-disk-type`=`DATA_DISK_TYPE`] [`--database-flags`=[`FLAG`=`VALUE`,…]] [`--display-name`=`DISPLAY_NAME`] [`--no-enable-ip-v4`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--labels`=[`KEY`=`VALUE`,…]] [`--private-network`=`PRIVATE_NETWORK`] [`--provider`=`PROVIDER`] [`--require-ssl`] [`--root-password`=`ROOT_PASSWORD`] [`--secondary-zone`=`SECONDARY_ZONE`] [`--storage-auto-resize-limit`=`STORAGE_AUTO_RESIZE_LIMIT`] [`--user-labels`=[`KEY`=`VALUE`,…]] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Database Migration Service destination connection profile for Cloud SQL. This will create a Cloud SQL replica. Used for PostgreSQL and MySQL migrations. 
EXAMPLES
     To create a connection profile for Cloud SQL with database version MySQL 5.6: 
    
    
    [gcloud alpha database-migration connection-profiles create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/database-migration/connection-profiles/create) cloudsql my-profile --region=us-central1 --database-version=MYSQL_5_6 --source-id=cp1 --tier=db-n1-standard-1

To create a connection profile for Cloud SQL and a Cloud SQL replica with database version PostgreSQL 10: 
    
    
    [gcloud alpha database-migration connection-profiles create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/database-migration/connection-profiles/create) cloudsql my-profile --region=us-central1 --database-version=POSTGRES_10 --source-id=cp1 --tier=db-custom-1-3840 --zone=us-central1-a

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
    

`--database-version`=`DATABASE_VERSION`
     Database engine type and version. `DATABASE_VERSION` must be one of: `MYSQL_5_7`, `MYSQL_5_6`, `MYSQL_8_0`, `POSTGRES_9_6`, `POSTGRES_10`, `POSTGRES_11`, `POSTGRES_12`, `POSTGRES_13`, `POSTGRES_14`, `POSTGRES_15`. 
Connection profile resource - Database Migration Service source connection profile ID. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--source-id` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `region` attribute: 

  * provide the argument `--source-id` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 



This must be specified. 

`--source-id`=`SOURCE_ID`
     ID of the connection_profile or fully qualified identifier for the connection_profile. 

To set the `connection_profile` attribute: 

  * provide the argument `--source-id` on the command line. 


`--tier`=`TIER`
     Tier (or machine type) for this instance, for example: ``db-n1-standard-1`` (MySQL instances) or ``db-custom-1-3840`` (PostgreSQL instances). For more information, see [Cloud SQL Instance Settings](https://cloud.google.com/sql/docs/mysql/instance-settings). 
OPTIONAL FLAGS
    

`--activation-policy`=`ACTIVATION_POLICY`
     Activation policy specifies when the instance is activated; it is applicable only when the instance state is 'RUNNABLE'. Valid values: 

ALWAYS: The instance is on, and remains so even in the absence of connection requests. 

NEVER: The instance is off; it is not activated, even if a connection request arrives. 

`ACTIVATION_POLICY` must be one of: `ALWAYS`, `NEVER`. 

`--no-async`
     Waits for the operation in progress to complete before returning. 
`--authorized-networks`=`NETWORK`,[`NETWORK`,…]
     List of external networks that are allowed to connect to the instance. Specify values in CIDR notation, also known as 'slash' notation (e.g.192.168.100.0/24). 
`--auto-storage-increase`
     If you enable this setting, Cloud SQL checks your available storage every 30 seconds. If the available storage falls below a threshold size, Cloud SQL automatically adds additional storage capacity. If the available storage repeatedly falls below the threshold size, Cloud SQL continues to add storage until it reaches the maximum of 64 TB. Default: ON. Enabled by default, use `--no-auto-storage-increase` to disable. 
`--availability-type`=`AVAILABILITY_TYPE`
     Cloud SQL availability type. `AVAILABILITY_TYPE` must be one of: `REGIONAL`, `ZONAL`. 
`--data-disk-size`=`DATA_DISK_SIZE`
     Storage capacity available to the database, in GB. The minimum (and default) size is 10GB. 
`--data-disk-type`=`DATA_DISK_TYPE`
     Type of storage. `DATA_DISK_TYPE` must be one of: `PD_SSD`, `PD_HDD`. 
`--database-flags`=[`FLAG`=`VALUE`,…]
     Comma-separated list of database flags to set on the instance. Use an equals sign to separate the flag name and value. Flags without values, like skip_grant_tables, can be written out without a value, e.g., `skip_grant_tables=`. Use on/off values for booleans. View the Instance Resource API for allowed flags. (e.g., `--database-flags max_allowed_packet=55555 skip_grant_tables=,log_output=1`). 
`--display-name`=`DISPLAY_NAME`
     A user-friendly name for the connection profile. The display name can include letters, numbers, spaces, and hyphens, and must start with a letter. 
`--enable-ip-v4`
     Whether the instance should be assigned an IPv4 address or not. Enabled by default, use `--no-enable-ip-v4` to disable. 
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

`--private-network`=`PRIVATE_NETWORK`
     Resource link for the VPC network from which the Cloud SQL instance is accessible for private IP. For example, /projects/myProject/global/networks/default. This setting can be updated, but it cannot be removed after it is set. 
`--provider`=`PROVIDER`
     Database provider, for managed databases. `PROVIDER` must be one of: `RDS`, `CLOUDSQL`. 
`--require-ssl`
     Whether SSL connections over IP should be enforced or not. 
`--root-password`=`ROOT_PASSWORD`
     Root Cloud SQL user's password. 
`--secondary-zone`=`SECONDARY_ZONE`
     Google Cloud Platform zone where the failover Cloud SQL database instance is located. Used when the Cloud SQL database availability type is REGIONAL (i.e. multiple zones / highly available). 
`--storage-auto-resize-limit`=`STORAGE_AUTO_RESIZE_LIMIT`
     Maximum size to which storage capacity can be automatically increased. The default value is 0, which specifies that there is no limit. 
`--user-labels`=[`KEY`=`VALUE`,…]
     The resource labels for a Cloud SQL instance to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs. 
`--zone`=`ZONE`
     Google Cloud Platform zone where your Cloud SQL database instance is located. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud database-migration connection-profiles create cloudsql](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
