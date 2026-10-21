---
url: https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create/
title: gcloud oracle-database cloud-exadata-infrastructures create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:43:32.187307+00:00
---

# gcloud oracle-database cloud-exadata-infrastructures create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud oracle-database cloud-exadata-infrastructures create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud oracle-database cloud-exadata-infrastructures create - create a new ExadataInfrastructure 
SYNOPSIS
    

`gcloud oracle-database cloud-exadata-infrastructures create` (`CLOUD_EXADATA_INFRASTRUCTURE` : `--location`=`LOCATION`) [`--async`] [`--display-name`=`DISPLAY_NAME`] [`--gcp-oracle-zone`=`GCP_ORACLE_ZONE`] [`--labels`=[`LABELS`,…]] [`--request-id`=`REQUEST_ID`] [[`--properties-shape`=`PROPERTIES_SHAPE` : `--properties-compute-count`=`PROPERTIES_COMPUTE_COUNT` `--properties-customer-contacts`=[`email`=`EMAIL`] `--properties-database-server-type`=`PROPERTIES_DATABASE_SERVER_TYPE` `--properties-storage-count`=`PROPERTIES_STORAGE_COUNT` `--properties-storage-server-type`=`PROPERTIES_STORAGE_SERVER_TYPE` `--properties-total-storage-size-gb`=`PROPERTIES_TOTAL_STORAGE_SIZE_GB` `--maintenance-window-custom-action-timeout-mins`=`MAINTENANCE_WINDOW_CUSTOM_ACTION_TIMEOUT_MINS` `--maintenance-window-days-of-week`=[`MAINTENANCE_WINDOW_DAYS_OF_WEEK`,…] `--maintenance-window-hours-of-day`=[`MAINTENANCE_WINDOW_HOURS_OF_DAY`,…] `--maintenance-window-is-custom-action-timeout-enabled` `--maintenance-window-lead-time-week`=`MAINTENANCE_WINDOW_LEAD_TIME_WEEK` `--maintenance-window-months`=[`MAINTENANCE_WINDOW_MONTHS`,…] `--maintenance-window-patching-mode`=`MAINTENANCE_WINDOW_PATCHING_MODE` `--maintenance-window-preference`=`MAINTENANCE_WINDOW_PREFERENCE` `--maintenance-window-weeks-of-month`=[`MAINTENANCE_WINDOW_WEEKS_OF_MONTH`,…]]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Creates a new ExadataInfrastructure. 
EXAMPLES
     Choose an available system shapes in your location by running `gcloud oracle-database db-system-shapes list --location=us-east4`. To create Exadata Infrastructure instance with id `my-instance` in the location `us-east4` with display-name `my instance`, compute count `2` and choosen shape "Exadata.FOO", run: 
    
    
    gcloud oracle-database cloud-exadata-infrastructures create my-instance --location=us-east4 --display-name="my instance" --properties-shape=Exadata.FOO --properties-compute-count=2 --properties-storage-count=3

POSITIONAL ARGUMENTS
    

CloudExadataInfrastructure resource - Identifier. The name of the Exadata Infrastructure resource with the format: projects/{project}/locations/{region}/cloudExadataInfrastructures/{cloud_exadata_infrastructure} The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `cloud_exadata_infrastructure` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CLOUD_EXADATA_INFRASTRUCTURE`
     ID of the cloudExadataInfrastructure or fully qualified identifier for the cloudExadataInfrastructure. 

To set the `cloud_exadata_infrastructure` attribute: 

  * provide the argument `cloud_exadata_infrastructure` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the cloudExadataInfrastructure resource. 

To set the `location` attribute: 

  * provide the argument `cloud_exadata_infrastructure` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--display-name`=`DISPLAY_NAME`
     User friendly name for this resource. 
`--gcp-oracle-zone`=`GCP_ORACLE_ZONE`
     The GCP Oracle zone where Oracle Exadata Infrastructure is hosted. Example: us-east4-b-r2. If not specified, the system will pick a zone based on availability. 
`--labels`=[`LABELS`,…]
     Labels or tags associated with the resource. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --labels=string=string

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

`--request-id`=`REQUEST_ID`
     An optional ID to identify the request. This value is used to identify duplicate requests. If you make a request with the same request ID and the original request is still in progress or completed, the server ignores the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

Various properties of Exadata Infrastructure. 
`--properties-shape`=`PROPERTIES_SHAPE`
     The shape of the Exadata Infrastructure. The shape determines the amount of CPU, storage, and memory resources allocated to the instance. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--properties-compute-count`=`PROPERTIES_COMPUTE_COUNT`
     The number of compute servers for the Exadata Infrastructure. 
`--properties-customer-contacts`=[`email`=`EMAIL`]
     The list of customer contacts. 

`email`
     The email address used by Oracle to send notifications regarding databases and infrastructure. 
`Shorthand Example:`
    
    
    --properties-customer-contacts=email=string --properties-customer-contacts=email=string

`JSON Example:`
    
    
    --properties-customer-contacts='[{"email": "string"}]'

`File Example:`
    
    
    --properties-customer-contacts=path_to_file.(yaml|json)

`--properties-database-server-type`=`PROPERTIES_DATABASE_SERVER_TYPE`
     The database server type of the Exadata Infrastructure. 
`--properties-storage-count`=`PROPERTIES_STORAGE_COUNT`
     The number of Cloud Exadata storage servers for the Exadata Infrastructure. 
`--properties-storage-server-type`=`PROPERTIES_STORAGE_SERVER_TYPE`
     The storage server type of the Exadata Infrastructure. 
`--properties-total-storage-size-gb`=`PROPERTIES_TOTAL_STORAGE_SIZE_GB`
     The total storage allocated to the Exadata Infrastructure resource, in gigabytes (GB). 
Maintenance window as defined by Oracle. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/MaintenanceWindow>
`--maintenance-window-custom-action-timeout-mins`=`MAINTENANCE_WINDOW_CUSTOM_ACTION_TIMEOUT_MINS`
     Determines the amount of time the system will wait before the start of each database server patching operation. Custom action timeout is in minutes and valid value is between 15 to 120 (inclusive). 
`--maintenance-window-days-of-week`=[`MAINTENANCE_WINDOW_DAYS_OF_WEEK`,…]
     Days during the week when maintenance should be performed. `MAINTENANCE_WINDOW_DAYS_OF_WEEK` must be one of: 

`friday`
     Friday 
`monday`
     Monday 
`saturday`
     Saturday 
`sunday`
     Sunday 
`thursday`
     Thursday 
`tuesday`
     Tuesday 
`wednesday`
     Wednesday 
`--maintenance-window-hours-of-day`=[`MAINTENANCE_WINDOW_HOURS_OF_DAY`,…]
     The window of hours during the day when maintenance should be performed. The window is a 4 hour slot. Valid values are: 0 - represents time slot 0:00 - 3:59 UTC 4 - represents time slot 4:00 - 7:59 UTC 8 - represents time slot 8:00 - 11:59 UTC 12 - represents time slot 12:00 - 15:59 UTC 16 - represents time slot 16:00 - 19:59 UTC 20 - represents time slot 20:00 - 23:59 UTC 
`--maintenance-window-is-custom-action-timeout-enabled`
     If true, enables the configuration of a custom action timeout (waiting period) between database server patching operations. 
`--maintenance-window-lead-time-week`=`MAINTENANCE_WINDOW_LEAD_TIME_WEEK`
     Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to 4. 
`--maintenance-window-months`=[`MAINTENANCE_WINDOW_MONTHS`,…]
     Months during the year when maintenance should be performed. `MAINTENANCE_WINDOW_MONTHS` must be one of: 

`april`
     The month of April. 
`august`
     The month of August. 
`december`
     The month of December. 
`february`
     The month of February. 
`january`
     The month of January. 
`july`
     The month of July. 
`june`
     The month of June. 
`march`
     The month of March. 
`may`
     The month of May. 
`november`
     The month of November. 
`october`
     The month of October. 
`september`
     The month of September. 
`--maintenance-window-patching-mode`=`MAINTENANCE_WINDOW_PATCHING_MODE`
     Cloud CloudExadataInfrastructure node patching method, either "ROLLING" or "NONROLLING". Default value is ROLLING. `MAINTENANCE_WINDOW_PATCHING_MODE` must be one of: 

`non-rolling`
     The non-rolling maintenance method first updates your storage servers at the same time, then your database servers at the same time. 
`rolling`
     Updates the Cloud Exadata database server hosts in a rolling fashion. 
`--maintenance-window-preference`=`MAINTENANCE_WINDOW_PREFERENCE`
     The maintenance window scheduling preference. `MAINTENANCE_WINDOW_PREFERENCE` must be one of: 

`custom-preference`
     Custom preference. 
`no-preference`
     No preference. 
`--maintenance-window-weeks-of-month`=[`MAINTENANCE_WINDOW_WEEKS_OF_MONTH`,…]
     Weeks during the month when maintenance should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a duration of 7 days. Weeks start and end based on calendar dates, not days of the week. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `oracledatabase/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/oracle/database/docs>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-28 UTC."],[],[]] 
