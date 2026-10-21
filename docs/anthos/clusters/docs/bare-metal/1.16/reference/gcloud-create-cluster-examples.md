---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/gcloud-create-cluster-examples/
title: Examples using the gcloud CLI to create a user cluster \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:57.624932+00:00
---

# Examples using the gcloud CLI to create a user cluster  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/gcloud-create-cluster-examples/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Examples using the gcloud CLI to create a user cluster Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/reference/gcloud-create-cluster-examples)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/gcloud-create-cluster-examples)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This page provides examples of using the command `gcloud container bare-metal clusters create` to create an Google Distributed Cloud user cluster. After creating the user cluster, you need to create at least one node pool. You can use the command `gcloud container bare-metal node-pools create` to create a node pool. Most of the settings that the commands take correspond to fields in the cluster and node pool [configuration file](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/cluster-config-ref).

**Important:** These are examples. You must replace the IP addresses and CIDR ranges with values from your network.

For descriptions of the flags, see the following:

  * [Create a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/create-user-cluster-api#create_a_user_cluster)
  * [The gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/bare-metal)



## Examples creating a cluster

### MetalLB
    
    
    gcloud container bare-metal clusters create user-cluster-1 \
      --project=example-project-12345 \
      --location=europe-west1 \
      --admin-cluster-membership=projects/example-project-12345/locations/global/memberships/admin-cluster-1 \
      --version=1.16.8 \
      --admin-users=sara@example.com \
      --admin-users=amal@example.com \
      --island-mode-service-address-cidr-blocks=10.96.0.0/20 \
      --island-mode-pod-address-cidr-blocks=192.168.0.0/16 \
      --metal-lb-address-pools='pool=pool1,avoid-buggy-ips=True,manual-assign=True,addresses=10.251.134.80/32;10.251.133.0/24;10.251.131.70-10.251.131.74' \
      --control-plane-node-configs='node-ip=10.200.0.10' \
      --control-plane-node-configs='node-ip=10.200.0.11,labels=key2.1=value2.1' \
      --control-plane-node-configs='node-ip=10.200.0.12,labels=key3.1=value3.1;key3.2=value3.2' \
      --control-plane-node-labels=cp-node-pool-key=cp-node-pool-value \
      --control-plane-node-taints=dedicated=experimental:PreferNoSchedule \
      --control-plane-vip=172.16.20.61 \
      --control-plane-load-balancer-port=443 \
      --ingress-vip=10.251.134.80 \
      --lvp-share-path=/mnt/localpv-share \
      --lvp-share-storage-class=local-shared \
      --lvp-node-mounts-config-path=/mnt/localpv-disk \
      --lvp-node-mounts-config-storage-class=local-disks
    

Optionally, you can include the `--metal-lb-load-balancer-node-configs` flag if you need to run the load balancer on a dedicated pool of worker nodes. For details see [MetalLB nodes](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/create-user-cluster-api#metal_lb_nodes).

### Manual load balancer
    
    
    gcloud container bare-metal clusters create user-cluster-2 \
      --project=example-project-12345 \
      --location=europe-west1 \
      --admin-cluster-membership=projects/example-project-12345/locations/global/memberships/admin-cluster-1 \
      --version=1.16.8 \
      --admin-users=sara@example.com \
      --admin-users=amal@example.com \
      --island-mode-service-address-cidr-blocks=10.96.0.0/20 \
      --island-mode-pod-address-cidr-blocks=192.168.0.0/16 \
      --enable-manual-lb \
      --control-plane-node-configs='node-ip=10.200.0.10' \
      --control-plane-node-configs='node-ip=10.200.0.11,labels=key2.1=value2.1' \
      --control-plane-node-configs='node-ip=10.200.0.12,labels=key3.1=value3.1;key3.2=value3.2' \
      --control-plane-node-labels=cp-node-pool-key=cp-node-pool-value \
      --control-plane-node-taints=dedicated=experimental:PreferNoSchedule \
      --control-plane-vip=172.16.20.61 \
      --control-plane-load-balancer-port=443 \
      --ingress-vip=10.251.134.80 \
      --lvp-share-path=/mnt/localpv-share \
      --lvp-share-storage-class=local-shared \
      --lvp-node-mounts-config-path=/mnt/localpv-disk \
      --lvp-node-mounts-config-storage-class=local-disks
    

## Create a node pool

After the cluster is created, you can use the `gcloud container bare-metal node-pools create` command to create a node pool:
    
    
    gcloud container bare-metal node-pools create default-pool \
        --cluster=user-cluster-1  \
        --project=example-project-12345 \
        --location=us-west1 \
        --node-configs='node-ip=10.200.0.10' \
        --node-configs='node-ip=10.200.0.11,labels=key2.1=value2.1' \
        --node-labels=node-pool-key=node-pool-value \
        --node-taints=dedicated=experimental:PreferNoSchedule
    

For descriptions of the flags, see [Create a node pool](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/create-user-cluster-api#create_the_cluster_and_node_pools).

## What's next

  * [Create a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/creating-clusters/create-user-cluster-api#create_a_user_cluster)
  * [The gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/bare-metal)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
