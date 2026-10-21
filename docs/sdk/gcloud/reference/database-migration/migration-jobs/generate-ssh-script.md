---
url: https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/generate-ssh-script/
title: gcloud database-migration migration-jobs generate-ssh-script \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:31:02.580168+00:00
---

# gcloud database-migration migration-jobs generate-ssh-script  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/generate-ssh-script/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud database-migration migration-jobs generate-ssh-script Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud database-migration migration-jobs generate-ssh-script - generate a SSH script for a Database Migration Service migration job 
SYNOPSIS
    

`gcloud database-migration migration-jobs generate-ssh-script` (`MIGRATION_JOB` : `--region`=`REGION`) `--vm`=`VM` (`--vm-zone`=`VM_ZONE` | [`--subnet`=`SUBNET` `--vm-machine-type`=`VM_MACHINE_TYPE` : `--vm-zone-create`=`VM_ZONE_CREATE`]) [`--endpoint-mode`=`ENDPOINT_MODE`] [`--vm-port`=`VM_PORT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Generate a script for a Database Migration Service migration job, to configure Reverse SSH tunnel connectivity with a bastion host on a Compute Engine VM instance. You can use an existing VM instance or create a new VM for this purpose. 

Copy the generated script and run it in bash from a machine that has: 

  * The gcloud command-line tool installed. 
  * Access to your source database. 
  * Access to the existing bastion VM, or permissions and access to the Cloud Compute API if creating a new bastion VM. Make sure this machine is available during the entire migration. 



Running the script will set up the SSH tunnel on the VM you selected and will establish connectivity between the source database and the Cloud SQL instance. Find additional information [here](https://cloud.google.com/database-migration/docs/mysql/configure-connectivity-reverse-ssh-tunnel). 

EXAMPLES
     To generate an SSH script with bastion VM instance creation: 
    
    
    gcloud database-migration migration-jobs generate-ssh-script my-migration-job --vm=vm1 --vm-port=1111 --vm-machine-type=n1-standard-1 --vm-zone-create=us-central1-a --subnet=sample-subnet --region=us-central1

To generate an SSH script with an existing bastion VM instance: 
    
    
    gcloud database-migration migration-jobs generate-ssh-script my-migration-job --vm=vm1 --vm-port=1111 --vm-zone=us-central1-a --region=us-central1

POSITIONAL ARGUMENTS
    

Migration job resource - The migration job to generate the SSH script for. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
     The name of the region. 

To set the `region` attribute: 

  * provide the argument `migration_job` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


REQUIRED FLAGS
    

`--vm`=`VM`
     Bastion Compute Engine VM instance name to use or to create. 
Exactly one of these must be specified: 

`--vm-zone`=`VM_ZONE`
     Zone the existing bastion VM instance is located in. 
Or at least one of these can be specified: 

`--subnet`=`SUBNET`
     Subnet to create the VM instance in. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--vm-machine-type`=`VM_MACHINE_TYPE`
     Machine type for a new VM instance. To get a list of available machine types, run 'gcloud compute machine-types list'. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--vm-zone-create`=`VM_ZONE_CREATE`
     Zone to create the VM instance in. 
OPTIONAL FLAGS
    

`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--vm-port`=`VM_PORT`
     Port that will be open on the bastion host. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `datamigration/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/database-migration/>
REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This variant is also available: 
    
    
    [gcloud alpha database-migration migration-jobs generate-ssh-script](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/database-migration/migration-jobs/generate-ssh-script)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
