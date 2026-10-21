---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/fault-testing/experiment-templates/create/
title: gcloud alpha fault-testing experiment-templates create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:40:54.627685+00:00
---

# gcloud alpha fault-testing experiment-templates create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/fault-testing/experiment-templates/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha fault-testing experiment-templates create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha fault-testing experiment-templates create - create an experiment template 
SYNOPSIS
    

`gcloud alpha fault-testing experiment-templates create` (`EXPERIMENT_TEMPLATE` : `--location`=`LOCATION`) `--duration`=`DURATION` (`--cloud-sql-failover-instance`=`CLOUD_SQL_FAILOVER_INSTANCE` | `--gce-fail-compute-instances`=[`GCE_FAIL_COMPUTE_INSTANCES`,…] | `--gce-fail-compute-location`=`GCE_FAIL_COMPUTE_LOCATION` | `--gce-fail-compute-secure-tag-value`=`GCE_FAIL_COMPUTE_SECURE_TAG_VALUE` | [`--gce-fail-compute-mig-instance-group-manager`=`GCE_FAIL_COMPUTE_MIG_INSTANCE_GROUP_MANAGER` : `--gce-fail-compute-mig-location`=`GCE_FAIL_COMPUTE_MIG_LOCATION`] | [`--l7-lb-http-fault-forwarding-rule`=`L7_LB_HTTP_FAULT_FORWARDING_RULE` : `--l7-lb-http-fault-backend-service`=`L7_LB_HTTP_FAULT_BACKEND_SERVICE` `--l7-lb-http-fault-abort-percentage`=`L7_LB_HTTP_FAULT_ABORT_PERCENTAGE` `--l7-lb-http-fault-abort-status-code`=`L7_LB_HTTP_FAULT_ABORT_STATUS_CODE` | `--l7-lb-http-fault-delay`=`L7_LB_HTTP_FAULT_DELAY` `--l7-lb-http-fault-delay-percentage`=`L7_LB_HTTP_FAULT_DELAY_PERCENTAGE`]) [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create an experiment template. 
EXAMPLES
     To create an experiment template `test-template-id` in location `asia-east1` with display name `test-template` with a duration of `100s` using Cloud SQL failover instance `test-cloud-sql-instance` in project `test-project` run: 
    
    
    gcloud alpha fault-testing experiment-templates create test-template-id --location=asia-east1 --display-name=test-template --duration=100s --cloud-sql-failover-instance="projects/test-project/instances/test-cloud-sql-instance"

POSITIONAL ARGUMENTS
    

ExperimentTemplate resource - Identifier. The resource name of this experiment template. Format: `projects/{project}/locations/{location}/experimentTemplates/{experiment_template}` The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `experiment_template` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`EXPERIMENT_TEMPLATE`
     ID of the experimentTemplate or fully qualified identifier for the experimentTemplate. 

To set the `experiment_template` attribute: 

  * provide the argument `experiment_template` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the experimentTemplate resource. 

To set the `location` attribute: 

  * provide the argument `experiment_template` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--duration`=`DURATION`
     How long the experiment is intended to run. Min duration is 0, max is 10 days. 
The action to be performed by the experiment. 

This must be specified. 

Arguments for the action. 

At most one of these can be specified: 

CloudSQLFailover causes a Cloud SQL primary instance to fail over to another instance. 
`--cloud-sql-failover-instance`=`CLOUD_SQL_FAILOVER_INSTANCE`
     The identifying name of the Cloud SQL instance to fail over. Format: `projects/{project}/instances/{instance}`
GCEFailCompute specifies which instances to fail. 
Arguments for the specifier. 

At most one of these can be specified: 

A GCEFailCompute option for failing multiple instances by name. 

`--gce-fail-compute-instances`=[`GCE_FAIL_COMPUTE_INSTANCES`,…]
     Specifies instances by name. Format: `projects/{project}/zones/{zone}/instances/{instance}`
`--gce-fail-compute-location`=`GCE_FAIL_COMPUTE_LOCATION`
     Specifies that an entire zone or region should be affected. 
`--gce-fail-compute-secure-tag-value`=`GCE_FAIL_COMPUTE_SECURE_TAG_VALUE`
     Specifies a group of non-MIG (Managed Instance Group) instances by secure tag. See <https://cloud.google.com/firewall/docs/tags-firewalls-overview> for more details on tags. Format: `{project}/{tag_key}/{tag_value}`. 
Or at least one of these can be specified: 

Details specifying a Managed Instance Group (MIG) and optionally a zone within it. 
`--gce-fail-compute-mig-instance-group-manager`=`GCE_FAIL_COMPUTE_MIG_INSTANCE_GROUP_MANAGER`
     Specifies the manager of a managed instance group. Can be zonal or regional. Format: `projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}` or `projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}`

This flag argument must be specified if any of the other arguments in this group are specified. 

`--gce-fail-compute-mig-location`=`GCE_FAIL_COMPUTE_MIG_LOCATION`
     Optionally specify a zone location to further restrict a regional MIG. 
Injection of HTTP faults into a layer 7 load balancer. 
`--l7-lb-http-fault-forwarding-rule`=`L7_LB_HTTP_FAULT_FORWARDING_RULE`
     The identifying name of the forwarding rule resource where the faults will be injected. Format: `projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}` or `projects/{project}/global/forwardingRules/{forwarding_rule}`

This flag argument must be specified if any of the other arguments in this group are specified. 

`--l7-lb-http-fault-backend-service`=`L7_LB_HTTP_FAULT_BACKEND_SERVICE`
     Optional identifying name of the backend service to inject faults into. Format: `projects/{project}/regions/{region}/backendServices/{backend_service}` or `projects/{project}/global/backendServices/{backend_service}` If not specified, all backend services connected to the forwarding_rule will be affected. 
Arguments for the fault. 

At most one of these can be specified: 

Artificially return a specific HTTP status code for a percentage of requests. 
`--l7-lb-http-fault-abort-percentage`=`L7_LB_HTTP_FAULT_ABORT_PERCENTAGE`
     Percentage of requests to abort, in the range 0 to 100, inclusive. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--l7-lb-http-fault-abort-status-code`=`L7_LB_HTTP_FAULT_ABORT_STATUS_CODE`
     HTTP status code to return. In the range 500 to 599, inclusive. 

This flag argument must be specified if any of the other arguments in this group are specified. 

Artificially delay HTTP responses for a percentage of requests. 
`--l7-lb-http-fault-delay`=`L7_LB_HTTP_FAULT_DELAY`
     Delay duration. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--l7-lb-http-fault-delay-percentage`=`L7_LB_HTTP_FAULT_DELAY_PERCENTAGE`
     Percentage of requests to delay, in the range 0 to 100, inclusive. 

This flag argument must be specified if any of the other arguments in this group are specified. 

OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     Optional user-provided description or notes. Min length 0. Max length 2000. 
`--display-name`=`DISPLAY_NAME`
     Human-readable template name. Min length 0, max 1000. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `faulttesting/v1alpha` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/fault-injection-testing>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
