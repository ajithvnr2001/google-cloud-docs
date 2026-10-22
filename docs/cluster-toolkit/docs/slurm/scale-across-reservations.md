---
url: https://docs.cloud.google.com/cluster-toolkit/docs/slurm/scale-across-reservations/
title: Scale A3 Mega cluster across multiple reservations \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:07.816548+00:00
---

# Scale A3 Mega cluster across multiple reservations  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/slurm/scale-across-reservations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Scale A3 Mega cluster across multiple reservations Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about how to use multiple reservations for an A3 Mega Slurm cluster.

As the jobs running on A3 Mega cluster grow, you might need to span your jobs across more than one reservation. To do this, you need to make a few minor changes to the following files:

  * The cluster blueprint: [`examples/machine-learning/a3-megagpu-8g/a3mega-slurm-blueprint.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-megagpu-8g/a3mega-slurm-blueprint.yaml)
  * The cluster deployment file: [`examples/machine-learning/a3-megagpu-8g/a3mega-slurm-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-megagpu-8g/a3mega-slurm-deployment.yaml)



## Overview

To update your cluster, we recommend creating a single Slurm partition with multiple `nodesets` so that a single job can span across multiple reservations.

To do this, complete the following steps:

  1. In the deployment file, create a nodeset for each additional reservation
  2. In the cluster blueprint, add all nodesets to the A3 Mega partition
  3. Deploy or redeploy the A3 Mega cluster



## Switch to the Cluster Toolkit directory

Ensure that you are in the Cluster Toolkit directory. To go to the Cluster Toolkit working directory, run the following command.
    
    
    cd cluster-toolkit

## Create one nodeset for each reservation

To create a nodeset for each reservation, you need to update your [`examples/machine-learning/a3-megagpu-8g/a3mega-slurm-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-megagpu-8g/a3mega-slurm-deployment.yaml) deployment file to add nodeset variables for each reservation.

The following example shows how to add three nodeset variables to the `a3mega-slurm-deployment.yaml` deployment file. Replace `NUMBER_OF _INSTANCES_ *` with the number of Compute Engine instances in each reservation.
    
    
    vars:
      project_id: customer-project
      region: customer-region
      zone: customer-zone
      ...
      a3mega_nodeset_a_size: NUMBER_OF_INSTANCES_A
      a3mega_nodeset_b_size: NUMBER_OF_INSTANCES_B
      a3mega_nodeset_c_size: NUMBER_OF_INSTANCES_C
      ...
    

## Add all nodesets to the A3 Mega partition

To add the nodesets to the A3 Mega partition, you need to update the [`examples/machine-learning/a3-megagpu-8g/a3mega-slurm-blueprint.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a3-megagpu-8g/a3mega-slurm-blueprint.yaml) cluster blueprint.

To add the nodesets, complete the following steps in the `a3mega-slurm-blueprint.yaml` blueprint:

  1. Locate the `id: a3mega_nodeset` section. It should resemble the following:
         
         **‐ id: a3mega_nodeset**
         source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
         use:
         ‐ sysnet
         ‐ gpunets
         settings:
           node_count_static: $(vars.a3mega_cluster_size)
           node_count_dynamic_max: 0
           ...
         

  2. Make a copy of the entire `id: a3mega_nodeset` section for each of the new reservations. In each section, change the `node_count_static` setting to specify the nodeset variable created in the preceding step.

For example, if you had created three nodesets, you would update as follows:
         
         **‐ id: a3mega_nodes_a**
         source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
         use:
         ‐ sysnet
         ‐ gpunets
         settings:
           **node_count_static: $(vars.a3mega_nodeset_a_size)**
           node_count_dynamic_max: 0
           ...
         
         **‐ id: a3mega_nodes_b**
         source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
         use:
         ‐ sysnet
         ‐ gpunets
         settings:
           **node_count_static: $(vars.a3mega_nodeset_b_size)**
           node_count_dynamic_max: 0
           ...
         
         **‐ id: a3mega_nodes_c**
         source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
         use:
         ‐ sysnet
         ‐ gpunets
         settings:
           **node_count_static: $(vars.a3mega_nodeset_c_size)**
           node_count_dynamic_max: 0
           ...
         

  3. Locate the `id: a3mega_partition` section.
         
         **‐ id: a3mega_partition**
         source: community/modules/compute/schedmd-slurm-gcp-v6-partition
         use:
         **- a3mega_nodeset**
         settings:
           ...
         

  4. Add the new nodesets.
         
         **‐ id: a3mega_partition**
          source: community/modules/compute/schedmd-slurm-gcp-v6-partition
          use:
          **- a3mega_nodes_a**
          **- a3mega_nodes_b**
          **- a3mega_nodes_c**
          settings:
           ...
         




## Deploy the A3 Mega cluster

  * If you are deploying the cluster for the first time, continue with the deployment. To deploy the cluster, see [Deploy an A3 Mega Slurm cluster for ML training](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/deploy-a3-mega-cluster#provision-cluster).
  * If you are updating an existing cluster, then run the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) from the Cluster Toolkit directory.

The `-w` flag specifies that you want to overwrite the previously deployed infrastructure.

**Caution:** If you are using a version of Terraform newer than 1.5, the following command might destroy the controller, login, and compute nodes, and might re-create several other assets such as VPC firewall rules. Any local modifications to the system won't be preserved. For more information, see [Known issue](https://github.com/GoogleCloudPlatform/cluster-toolkit/issues/2774).
        
        ./gcluster deploy -w \
        -d examples/machine-learning/a3-megagpu-8g/a3mega-slurm-deployment.yaml \
        -b examples/machine-learning/a3-megagpu-8g/a3mega-slurm-blueprint.yaml
        

This process might take approximately 10-30 minutes to delete any existing nodes and create all of the new nodes.




## Connect to the A3 Mega Slurm cluster

To login, you can use either Google Cloud console or Google Cloud CLI.

###  Console 

  1. Go to the **Compute Engine** > **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Locate the login node. It should have a name similar to `a3mega-login-001`.

  3. From the **Connect** column of the login node, click **SSH**.




###  gcloud 

To connect to the login node, use the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh).
    
    
    gcloud compute ssh $(gcloud compute instances list --filter "name ~ login" --format "value(name)") \
      --tunnel-through-iap \
      --zone ZONE
    

## Test your multi-nodeset partition

When you connect to the login or controller node, you might see the following:
    
    
    *** Slurm is currently being configured in the background. ***
    

If you see this message, wait a few minutes until Slurm has finished configuring and then reconnect to the cluster. Then you can run `sinfo` and `scontrol` to examine your new partition.

  * For the `sinfo` command, the output should resemble the following:
        
        PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
        a3mega*      up   infinite    216   idle a3mega-a3meganodesa-[0-79],a3mega-a3meganodesb-[0-63],a3mega-a3meganodesc-[0-71]
        debug        up   infinite      4  idle~ a3mega-debugnodeset-[0-3]
        

  * For the `scontrol show partition a3mega` command, the output should resemble the following:
        
        PartitionName=a3mega
        AllowGroups=ALL AllowAccounts=ALL AllowQos=ALL
        AllocNodes=ALL Default=YES QoS=N/A
        DefaultTime=NONE DisableRootJobs=NO ExclusiveUser=NO GraceTime=0 Hidden=NO
        MaxNodes=UNLIMITED MaxTime=UNLIMITED MinNodes=0 LLN=NO MaxCPUsPerNode=UNLIMITED MaxCPUsPerSocket=UNLIMITED
        **NodeSets=a3meganodesa,a3meganodesb,a3meganodesc**
        Nodes=a3mega-a3meganodesa-[0-79],a3mega-a3meganodesb-[0-63],a3mega-a3meganodesc-[0-71]
        PriorityJobFactor=1 PriorityTier=1 RootOnly=NO ReqResv=NO OverSubscribe=EXCLUSIVE
        OverTimeLimit=NONE PreemptMode=OFF
        State=UP TotalCPUs=44928 TotalNodes=216 SelectTypeParameters=NONE
        JobDefaults=(null)
        DefMemPerCPU=8944 MaxMemPerNode=UNLIMITED
        TRES=cpu=44928,mem=392421G,node=216,billing=44928
        ResumeTimeout=900 SuspendTimeout=600 SuspendTime=300 PowerDownOnIdle=NO
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
