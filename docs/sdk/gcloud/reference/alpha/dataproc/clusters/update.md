---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/update/
title: gcloud alpha dataproc clusters update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:32:02.880460+00:00
---

# gcloud alpha dataproc clusters update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/clusters/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataproc clusters update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataproc clusters update - update labels and/or the number of worker nodes in a cluster 
SYNOPSIS
    

`gcloud alpha dataproc clusters update` (`CLUSTER` : `--region`=`REGION`) [`--async`] [`--graceful-decommission-timeout`=`GRACEFUL_DECOMMISSION_TIMEOUT`] [`--min-secondary-worker-fraction`=`MIN_SECONDARY_WORKER_FRACTION`] [`--num-secondary-workers`=`NUM_SECONDARY_WORKERS`] [`--num-workers`=`NUM_WORKERS`] [`--secondary-worker-flexible-config`=[`KEY`=`VALUE`,…]] [`--secondary-worker-standard-capacity-base`=`SECONDARY_WORKER_STANDARD_CAPACITY_BASE`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--worker-flexible-config`=[`KEY`=`VALUE`,…]] [`--autoscaling-policy`=`AUTOSCALING_POLICY` | `--disable-autoscaling`] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`--delete-expiration-time`=`DELETE_EXPIRATION_TIME` | `--delete-max-age`=`DELETE_MAX_AGE` | `--no-delete-max-age`] [`--delete-max-idle`=`DELETE_MAX_IDLE` | `--no-delete-max-idle`] [`--identity-config-file`=`IDENTITY_CONFIG_FILE` | `--add-user-mappings`=[`KEY`=`VALUE`,…] `--remove-user-mappings`=[`KEY`,…]] [`--stop-expiration-time`=`STOP_EXPIRATION_TIME` | `--stop-max-age`=`STOP_MAX_AGE` | `--no-stop-max-age`] [`--stop-max-idle`=`STOP_MAX_IDLE` | `--no-stop-max-idle`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update the number of worker nodes and/or the labels in a cluster. 
EXAMPLES
     To resize a cluster, run: 
    
    
    gcloud alpha dataproc clusters update my-cluster --region=us-central1 --num-workers=5

To change the number of secondary workers in a cluster, run: 
    
    
    gcloud alpha dataproc clusters update my-cluster --region=us-central1 --num-secondary-workers=5

To add the label 'customer=acme' to a cluster, run: 
    
    
    gcloud alpha dataproc clusters update my-cluster --region=us-central1 --update-labels=customer=acme

To update the label 'customer=ackme' to 'customer=acme', run: 
    
    
    gcloud alpha dataproc clusters update my-cluster --region=us-central1 --update-labels=customer=acme

To remove the label whose key is 'customer', run: 
    
    
    gcloud alpha dataproc clusters update my-cluster --region=us-central1 --remove-labels=customer

POSITIONAL ARGUMENTS
    

Cluster resource - The name of the cluster to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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

`--region`=`REGION`
     Dataproc region for the cluster. Each Dataproc region constitutes an independent resource namespace constrained to deploying instances into Compute Engine zones inside the region. Overrides the default `dataproc/region` property value for this command invocation. 

To set the `region` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `dataproc/region`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--graceful-decommission-timeout`=`GRACEFUL_DECOMMISSION_TIMEOUT`
     The graceful decommission timeout for decommissioning Node Managers in the cluster, used when removing nodes. Graceful decommissioning allows removing nodes from the cluster without interrupting jobs in progress. Timeout specifies how long to wait for jobs in progress to finish before forcefully removing nodes (and potentially interrupting jobs). Timeout defaults to 0 if not set (for forceful decommission), and the maximum allowed timeout is 1 day. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--min-secondary-worker-fraction`=`MIN_SECONDARY_WORKER_FRACTION`
     Minimum fraction of new secondary worker nodes added in a scale up update operation, required to update the cluster. If it is not met, cluster updation will rollback the addition of secondary workers. Must be a decimal value between 0 and 1. Defaults to 0.0001. 
`--num-secondary-workers`=`NUM_SECONDARY_WORKERS`
     The new number of secondary worker nodes in the cluster. 
`--num-workers`=`NUM_WORKERS`
     The new number of worker nodes in the cluster. 
`--secondary-worker-flexible-config`=[`KEY`=`VALUE`,…]
     The flexible instance group configuration for secondary workers in High Obtainability (HO) clusters. Supported keys: num-instances (non-negative integer). 
`--secondary-worker-standard-capacity-base`=`SECONDARY_WORKER_STANDARD_CAPACITY_BASE`
     The number of standard VMs in the Spot and Standard Mix feature. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--worker-flexible-config`=[`KEY`=`VALUE`,…]
     The flexible instance group configuration for primary workers in High Obtainability (HO) clusters. Supported keys: num-instances (positive integer). 
At most one of these can be specified: 

Autoscaling policy resource - The autoscaling policy to use. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--autoscaling-policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `region` attribute: 

  * provide the argument `--autoscaling-policy` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `dataproc/region`. 



`--autoscaling-policy`=`AUTOSCALING_POLICY`
     ID of the autoscaling policy or fully qualified identifier for the autoscaling policy. 

To set the `autoscaling_policy` attribute: 

* provide the argument `--autoscaling-policy` on the command line. 
`--disable-autoscaling`
     Disable autoscaling, if it is enabled. This is an alias for passing the empty string to --autoscaling-policy'. 
At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud alpha dataproc clusters update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud alpha dataproc clusters update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
At most one of these can be specified: 

`--delete-expiration-time`=`DELETE_EXPIRATION_TIME`
     The time when the cluster will be auto-deleted, such as "2017-08-29T18:52:51.142Z". See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
`--delete-max-age`=`DELETE_MAX_AGE`
     The lifespan of the cluster with auto-deletion upon completion, such as "2h" or "1d". See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--no-delete-max-age`
     Cancels the cluster auto-deletion by maximum cluster age (configured by \--delete-max-age or --delete-expiration-time flags) 
At most one of these can be specified: 

`--delete-max-idle`=`DELETE_MAX_IDLE`
     The duration after the last job completes to auto-delete the cluster, such as "2h" or "1d". See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--no-delete-max-idle`
     Cancels the cluster auto-deletion by cluster idle duration (configured by \--delete-max-idle flag) 
At most one of these can be specified: 

`--identity-config-file`=`IDENTITY_CONFIG_FILE`
     Path to a YAML (or JSON) file that contains the configuration for [Secure Multi-Tenancy](https://docs.cloud.google.com/sdk//reference/dataproc/docs/concepts/iam/sa-multi-tenancy) on the cluster. The path can be a Cloud Storage URL (example: 'gs://path/to/file') or a local filesystem path. The mappings provided in the file will overwrite existing mappings. 

The YAML file is formatted as follows: 
    
    
      # Mapping header (first line) required.
      user_service_account_mapping:
        bob@company.com: service-account-bob@project.iam.gserviceaccount.com
        alice@company.com: service-account-alice@project.iam.gserviceaccount.com

Or at least one of these can be specified: 

`--add-user-mappings`=[`KEY`=`VALUE`,…]
     List of user-to-service-account mappings to add to current mappings. If a mapping exists, its value is modified; otherwise, the new mapping is added. 
`--remove-user-mappings`=[`KEY`,…]
     List of user-to-service-account mappings to remove from the current mappings. If a mapping does not exist, it is ignored. 
At most one of these can be specified: 

`--stop-expiration-time`=`STOP_EXPIRATION_TIME`
     The time when the cluster will be auto-stopped, such as "2017-08-29T18:52:51.142Z". See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
`--stop-max-age`=`STOP_MAX_AGE`
     The lifespan of the cluster, with auto-stop upon completion, such as "2h" or "1d". See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--no-stop-max-age`
     Cancels the cluster auto-stop by maximum cluster age (configured by \--stop-max-age or --stop-expiration-time flags) 
At most one of these can be specified: 

`--stop-max-idle`=`STOP_MAX_IDLE`
     The duration after the last job completes to auto-stop the cluster, such as "2h" or "1d". See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--no-stop-max-idle`
     Cancels the cluster auto-stop by cluster idle duration (configured by \--stop-max-idle flag) 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud dataproc clusters update](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update)
    
    
    [gcloud beta dataproc clusters update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/clusters/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
