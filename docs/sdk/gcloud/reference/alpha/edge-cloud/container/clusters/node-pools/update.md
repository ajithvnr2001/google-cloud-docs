---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cloud/container/clusters/node-pools/update/
title: gcloud alpha edge-cloud container clusters node-pools update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:32:13.494263+00:00
---

# gcloud alpha edge-cloud container clusters node-pools update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cloud/container/clusters/node-pools/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha edge-cloud container clusters node-pools update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha edge-cloud container clusters node-pools update - updates an Edge Container node pool 
SYNOPSIS
    

`gcloud alpha edge-cloud container clusters node-pools update` (`NODE_POOL` : `--cluster`=`CLUSTER` `--location`=`LOCATION`) [`--async`] [`--local-disk-kms-key`=`LOCAL_DISK_KMS_KEY`] [`--lro-timeout`=`LRO_TIMEOUT`] [`--machine-filter`=`MACHINE_FILTER`] [`--node-count`=`NODE_COUNT`] [`--node-labels`=[`KEY`=`VALUE`,…]] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--use-google-managed-key`] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Updates an Edge Container node pool. 
EXAMPLES
     To update the number of nodes in a node pool called `my-node-pool` in region `us-central1`, run: 
    
    
    gcloud alpha edge-cloud container clusters node-pools update my-node-pool --location=us-central1 --cluster=<my-cluster> --node-count=<new-count>

POSITIONAL ARGUMENTS
    

Node pool resource - Edge Container node pool to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `node_pool` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`NODE_POOL`
     ID of the node pool or fully qualified identifier for the node pool. 

To set the `nodePool` attribute: 

  * provide the argument `node_pool` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--cluster`=`CLUSTER`
     Cluster of the node pool. 

To set the `cluster` attribute: 

  * provide the argument `node_pool` on the command line with a fully specified name; 
  * provide the argument `--cluster` on the command line. 


`--location`=`LOCATION`
     Google Cloud location for the node pool. 

To set the `location` attribute: 

  * provide the argument `node_pool` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--local-disk-kms-key`=`LOCAL_DISK_KMS_KEY`
     Google Cloud KMS key that will be used to secure local disks on nodes in this node pool. The Edge Container service account for this project must have `roles/cloudkms.cryptoKeyEncrypterDecrypter` on the key. 

If not provided, a Google-managed key will be used instead. 

`--lro-timeout`=`LRO_TIMEOUT`
     Overwrite the default LRO maximum timeout. 
`--machine-filter`=`MACHINE_FILTER`
     Only machines matching this filter will be allowed to join the node pool. The filtering language accepts strings like "name=<name>", and is documented in more detail at <https://google.aip.dev/160>. 
`--node-count`=`NODE_COUNT`
     Default nodeCount used by this node pool. 
`--node-labels`=[`KEY`=`VALUE`,…]
     Comma-delimited list of key-value pairs that comprise labels for the individual nodes in the node pool. This flag updates the Kubernetes labels, unlike `--update-labels`, `--remove-labels`, and `--clear-labels` which update the cloud resource labels. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--use-google-managed-key`
     Once specified, a Google-managed key will be used for the control plane disk encryption. 
At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud alpha edge-cloud container clusters node-pools update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud alpha edge-cloud container clusters node-pools update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the edgecontainer/v1alpha API. The full documentation for this API can be found at: <https://cloud.google.com/edge-cloud>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud edge-cloud container clusters node-pools update](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/node-pools/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
