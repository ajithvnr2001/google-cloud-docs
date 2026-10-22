---
url: https://docs.cloud.google.com/cluster-toolkit/docs/slurm/static-nodes-best-practices/
title: Best practices for static compute nodes \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:30:35.566131+00:00
---

# Best practices for static compute nodes  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/slurm/static-nodes-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Best practices for static compute nodes Stay organized with collections  Save and categorize content based on your preferences. 

To achieve optimal usability and performance for high performance computing (HPC) and artificial intelligence (AI) workloads, use the best practices in this document to configure your static compute nodes. These practices help you achieve better resource availability and reduced network latency for the Compute Engine instances that you create. For more information about static compute nodes, see [About node types](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/node-types).

## Reservations

Use [reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type) to help ensure that Compute Engine resources are available. Reservations help you obtain capacity for Compute Engine zonal resources.

For static clusters, use reservations. A reservation is an effective method to obtain resources for these clusters because it helps ensure that Compute Engine resources are available when you need them. You must create your reservation manually before you deploy your cluster. Note that after you create a reservation, Google Cloud bills you for the compute resources as if the compute instances are running, even if they haven't yet been created or used. You can monitor the consumption trends of your reservations to reduce unnecessary costs from wasted or unused resources. For more information, see [Monitor reservations consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-monitor).

## Compact placement policies

Use a compact placement policy to place your static compute nodes physically closer to each other, which reduces network latency between nodes.

Unlike autoscaling nodes, which might create a new compact placement policy for each job, the placement of static compute nodes is based on the nodeset lifecycle, not the job lifecycle.

However, the topology of static compute nodes might change when you restart, recreate, or migrate nodes. These topology changes can happen because of explicit actions, such as when you [update images](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/manage-static-nodes#update-images), or during [maintenance events](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/manage-static-nodes#host-maintenance).

### Configure the static compute nodes with a reservation and a compact placement policy

Create the placement policy before you create the reservation. When you create the reservation, specify the placement policy. If you provide Slurm with a reservation that includes a placement policy, then Slurm automatically uses the placement policy that is attached to the reservation.

To configure static compute nodes to use a compact placement policy and reservation, complete the following steps by using the Google Cloud CLI:

  1. Create a compact placement policy by using the [`gcloud compute resource-policies create group-placement` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/group-placement) with the `--collocation=COLLOCATED` flag.
         
         gcloud compute resource-policies create group-placement PLACEMENT_POLICY_NAME \
             --collocation=COLLOCATED \
             --project=PROJECT_ID \
             --region=REGION
         

  2. Create a reservation for a set of compute instances by using the [`gcloud compute reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/create) and specify the compact placement policy that you created in step 1.
         
         gcloud compute reservations create RESERVATION_NAME \
           --vm-count=INSTANCE_COUNT \
           --machine-type=MACHINE_TYPE \
           --require-specific-reservation \
           --project=PROJECT_ID \
           --zone=ZONE \
           --resource-policies=compact-placement=PLACEMENT_POLICY_NAME
         

  3. Update the cluster blueprint to use the reservation for your static compute nodes before you [deploy the cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/deploy-cluster-overview). When you specify `reservation_name`, Cluster Toolkit automatically applies the placement policy attached to the reservation, so configuring the `enable_placement: false` field is optional.
         
         ‐ id: static_nodeset
            source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
            use: [network]
            settings:
              node_count_static: INSTANCE_COUNT
              node_count_dynamic_max: 0
              reservation_name: RESERVATION_NAME
              machine_type: MACHINE_TYPE   
           
         
          ‐ id: static_partition
            source: community/modules/compute/schedmd-slurm-gcp-v6-partition
            use: [static_nodeset]
            settings:
              partition_name: static
              exclusive: false
          




Replace the following:

  * `RESERVATION_NAME`: the name of your reservation
  * `INSTANCE_COUNT`: the number of compute instances in the reservation
  * `MACHINE_TYPE`: a machine type from the [compute-optimized](https://docs.cloud.google.com/compute/docs/compute-optimized-machines) or [accelerator-optimized](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) machine family
  * `PLACEMENT_POLICY_NAME`: the name of your placement policy
  * `PROJECT_ID`: your project ID
  * `REGION`: the region where your compute instances are located
  * `ZONE`: the zone where your compute instances are located



## Summary of best practices

The following table summarizes the recommended best practices for clusters that use static compute nodes:

Requirement | Recommendation  
---|---  
Compute instance availability | 

  * Use a reservation

  
Reduce network latency | Use a compact placement policy  
  
## What's next

  * Learn how to [manage static compute nodes](https://docs.cloud.google.com/cluster-toolkit/docs/slurm/manage-static-nodes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
