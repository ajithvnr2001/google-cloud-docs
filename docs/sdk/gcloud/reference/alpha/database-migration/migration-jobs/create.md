---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/database-migration/migration-jobs/create/
title: gcloud alpha database-migration migration-jobs create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:31:23.536553+00:00
---

# gcloud alpha database-migration migration-jobs create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/database-migration/migration-jobs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha database-migration migration-jobs create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha database-migration migration-jobs create - create a Database Migration Service migration job 
SYNOPSIS
    

`gcloud alpha database-migration migration-jobs create` (`MIGRATION_JOB` : `--region`=`REGION`) `--destination`=`DESTINATION` `--source`=`SOURCE` `--type`=`TYPE` [`--no-async`] [`--display-name`=`DISPLAY_NAME`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--labels`=[`KEY`=`VALUE`,…]] [`--dump-flags`=[`KEY`=`VALUE`,…] | `--dump-path`=`DUMP_PATH`] [`--peer-vpc`=`PEER_VPC` | `--static-ip` | [`--vm-ip`=`VM_IP` `--vm-port`=`VM_PORT` `--vpc`=`VPC` : `--vm`=`VM`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Database Migration Service migration job. Recommended steps before creating the migration job: 

  * Create a source connection profile. See prerequisites [here](https://cloud.google.com/database-migration/docs/mysql/configure-source-database). 
  * Create a destination connection profile. For migrating to Cloud SQL for MySQL or Cloud SQL for PostgreSQL, use the cloudsql connection profile for DMS to create the CloudSQL replica for you. 
  * Configure the connectivity method. See prerequisites [here](https://cloud.google.com/database-migration/docs/mysql/configure-connectivity). 


EXAMPLES
     To create a continuous migration job with IP allowlist connectivity: 
    
    
    gcloud alpha database-migration migration-jobs create my-migration-job --region=us-central1 --type=CONTINUOUS --source=cp1 --destination=cp2

To create a continuous migration job with VPC peering connectivity: 
    
    
    gcloud alpha database-migration migration-jobs create my-migration-job --region=us-central1 --type=CONTINUOUS --source=cp1 --destination=cp2 --peer-vpc=projects/my-project/global/networks/my-network

To create a one-time migration job with reverse-SSH tunnel connectivity: 
    
    
    gcloud alpha database-migration migration-jobs create my-migration-job --region=us-central1 --type=ONE_TIME --source=cp1 --destination=cp2 --vm=vm1 --vm-ip=1.1.1.1 --vm-port=1111 --vpc=projects/my-project/global/networks/my-network

POSITIONAL ARGUMENTS
    

Migration job resource - The migration job to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `migration_job` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MIGRATION_JOB`
     ID of the migration_job or fully qualified identifier for the migration_job. 

To set the `migration_job` attribute: 

  * provide the argument `migration_job` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The Cloud region for the migration_job. 

To set the `region` attribute: 

  * provide the argument `migration_job` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


REQUIRED FLAGS
    

Connection profile resource - ID of the destination connection profile, representing the destination database. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--destination` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `region` attribute: 

  * provide the argument `--destination` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 



This must be specified. 

`--destination`=`DESTINATION`
     ID of the connection_profile or fully qualified identifier for the connection_profile. 

To set the `connection_profile` attribute: 

  * provide the argument `--destination` on the command line. 


Connection profile resource - ID of the source connection profile, representing the source database. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--source` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `region` attribute: 

  * provide the argument `--source` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 



This must be specified. 

`--source`=`SOURCE`
     ID of the connection_profile or fully qualified identifier for the connection_profile. 

To set the `connection_profile` attribute: 

  * provide the argument `--source` on the command line. 


`--type`=`TYPE`
     Type of the migration job. `TYPE` must be one of: `ONE_TIME`, `CONTINUOUS`. 
OPTIONAL FLAGS
    

`--no-async`
     Waits for the operation in progress to complete before returning. 
`--display-name`=`DISPLAY_NAME`
     A user-friendly name for the migration job. The display name can include letters, numbers, spaces, and hyphens, and must start with a letter. 
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

At most one of these can be specified: 

`--dump-flags`=[`KEY`=`VALUE`,…]
     A list of dump flags. An object containing a list of "key": "value" pairs. 
`--dump-path`=`DUMP_PATH`
     Path to the dump file in Google Cloud Storage, in the format: `gs://[BUCKET_NAME]/[OBJECT_NAME]`. 
The connectivity method used by the migration job. If a connectivity method isn't specified, then it isn't added to the migration job. 

At most one of these can be specified: 

`--peer-vpc`=`PEER_VPC`
     Name of the VPC network to peer with the Cloud SQL private network. 
`--static-ip`
     Use the default IP allowlist method. This method creates a public IP that will be used with the destination Cloud SQL database. The method works by configuring the source database server to accept connections from the outgoing IP of the Cloud SQL instance. 
Or at least one of these can be specified: 

Parameters for the reverse-SSH tunnel connectivity method. 
`--vm-ip`=`VM_IP`
     Bastion Virtual Machine IP. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--vm-port`=`VM_PORT`
     Forwarding port for the SSH tunnel. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--vpc`=`VPC`
     Name of the VPC network where the VM is hosted. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--vm`=`VM`
     Name of VM that will host the SSH tunnel bastion. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud database-migration migration-jobs create](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
