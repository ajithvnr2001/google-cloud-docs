---
url: https://docs.cloud.google.com/cluster-toolkit/docs/slurm/reconfigure-cluster/
title: Reconfigure a running cluster \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:07.687195+00:00
---

# Reconfigure a running cluster  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/slurm/reconfigure-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Reconfigure a running cluster Stay organized with collections  Save and categorize content based on your preferences. 

To make basic configuration changes to a running cluster, it is recommended to edit and redeploy the blueprint. This method of reconfiguring a live cluster must only be used for the following cases:

  * To add or remove a partition from the cluster
  * To resize an existing partition



## Set up environment to allow for reconfiguration

To set up the environment to allow for reconfiguration, complete the following steps:

  1. Set top level variables to allow for cluster reconfiguration. Placing these settings in the `vars` block ensures that they are applied to any module that accepts them as inputs.
         
         # Slurm v6
         vars:
           ...
           enable_cleanup_compute: true
         

  2. To use the settings in the previous step, install local python dependencies. Python dependencies must be installed on the deployment machine where the [`gcluster` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster) is run from. For installation instructions, review the Slurm v6 [`schedmd-slurm-gcp-v6-controller` documentation](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/community/modules/scheduler/schedmd-slurm-gcp-v6-controller/README.md#description).




## Reconfigure partitions on running cluster

To reconfigure a running cluster, complete the following steps:

**Warning:** Take caution when performing this task, as manual changes to the cluster might be overwritten by redeploying the blueprint.

  1. To enable cluster reconfiguration, ensure that you Set up environment to allow for reconfiguration.
  2. Ensure that redeployment happens with the same version of `gcluster` as the original deployment. Graceful redeployment across versions of the Cluster Toolkit isn't assured.

You can check the version of `gcluster` by using the `gcluster --version` command. Also, `gcluster` prints a warning if you are using a different version on the redeploy.

  3. Redeploy the blueprint as follows:

     1. Edit the blueprint file. For example, you can increase the `node_count_static` on a node set.
     2. Recreate the deployment by running the [`gcluster create` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-create). The `-w` flag is required for the previous deployment to be overwritten.
            
            gcluster create BLUEPRINT_NAME -w

     3. Redeploy the deployment by running the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy):
            
            gcluster deploy DEPLOYMENT_FOLDER_NAME

Carefully evaluate the terraform plan to make sure that no unexpected resources are replaced or deleted.




## What's next

  * Learn how to [Manage static compute node](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/manage-static-nodes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
