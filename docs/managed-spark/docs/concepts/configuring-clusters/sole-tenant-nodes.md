---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/sole-tenant-nodes/
title: Sole-tenant node clusters \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:51.612803+00:00
---

# Sole-tenant node clusters  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/sole-tenant-nodes/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Sole-tenant node clusters Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark clusters can be created on Compute Engine [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes). A sole-tenant node is a Compute Engine server that is dedicated to hosting your project's VMs only. Creating a Managed Service for Apache Spark cluster on a sole tenant node keeps the cluster's VMs physically separate from VMs in other projects. The clusters function as standard Managed Service for Apache Spark clusters, but with additional hardware isolation to address security and compliance concerns.

Managed Service for Apache Spark sole-tenant node clusters are created in a user-specified _sole-tenant node group_. Each cluster's master, worker, and secondary worker instances will be created within this sole-tenant node group.

**Caution:** Managed Service for Apache Spark defaults to preemptible VMs for [secondary workers](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/secondary-vms), which are not supported by Compute Engine sole-tenant nodes. If you plan to use secondary workers with your sole-tenant cluster, by [manually adding them](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/secondary-vms#using_secondary_workers) or using an [autoscaling policy](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/autoscaling#gcloud-command) that scales up secondary workers, you must set your secondary worker type to non-preemptible.

## First steps

  1. See [Before you begin](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#before-you-begin).

  2. [Create a sole-tenant node template](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#creating_a_sole-tenant_node_template).

  3. [Create a sole-tenant node group](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#creating_a_soletenant_node_group).

     * Use [autoscaling node groups](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups) if you will create [autoscaling clusters](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/autoscaling) in the sole-tenant node group.

**Node group autoscaling recommendations:**

       * Make sure the node group's `max-nodes` is sufficient for the `maxInstances` of clusters you will create in the sole-tenant node group.
       * Use the default or `migrate-within-node-group` node group maintenance policy; VMs may be unavailable for up to one hour with the `restart-in-place` policy.



## Creating a sole-tenant cluster

  * Before creating a sole-tenant cluster, see the [sole-tenant node VM restrictions](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#restrictions).

  * If you create an [autoscaling cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/autoscaling) in a sole-tenant node group, it is recommended that [node group also use autoscaling](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups) (see Node group autoscaling recommendations).




### gcloud Command

To create a sole-tenant cluster, pass the `--node-group` flag to the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command.

Flag notes:

  * `--region` (required): Must match the region of the sole-tenant-group.
  * `--node-group` (required): You can specify the sole tenant node group name ("node-group-name") or the sole-tenant node group resource URI ("projects/project-id/zones/zone/nodeGroups/node-group-name").
  * `--zone` (required): The cluster zone must match the sole-tenant node group zone.


    
    
    gcloud dataproc clusters create cluster-name \
        --region=region \
        --zone=zone \
        --node-group=node group resource name or URI \
        ... other args
      

### REST API

Create a sole-tenant cluster using a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request that specifies the [NodeGroupAffinity.nodeGroupUri](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#NodeGroupAffinity) of the sole-tenant node group.

Note: the cluster zone specified in the [`zoneUri`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#GceClusterConfig.FIELDS.zone_uri) field must match the sole-tenant node group zone.

An easy way to examine and construct the JSON body of a Managed Service for Apache Spark API clusters request is to open the Managed Service for Apache Spark [Create a cluster](https://console.cloud.google.com/dataproc/clusters/create) Google Cloud console page, fill in the applicable fields on the page, then click the **Equivalent REST** button at the bottom of the left panel to view the POST request with the completed JSON request body. 

### Console

Currently, creating a sole-tenant Managed Service for Apache Spark cluster is not supported in the Google Cloud console.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
