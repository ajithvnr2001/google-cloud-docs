---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/reference/gcloud-create-cluster-examples/
title: Examples using the gcloud CLI to create a user cluster \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:52.985313+00:00
---

# Examples using the gcloud CLI to create a user cluster  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/reference/gcloud-create-cluster-examples/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Examples using the gcloud CLI to create a user cluster Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/reference/gcloud-create-cluster-examples)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/reference/gcloud-create-cluster-examples)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page provides examples of using the command `gcloud container vmware clusters create` to create a user cluster. After creating the user cluster, you need to create at least one node pool. You can use the command `gcloud container vmware node-pools create` to create a node pool.

**Important:** These are examples. You must replace the IP addresses and CIDR ranges with values from your network. See [Plan your IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/plan-ip-addresses) for more information.

All of the examples use the defaults for the [control plane](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-api#control_plane), so those flags aren't included.

## DCHP

This section shows examples of getting IP addresses for you cluster nodes from a DHCP server.

### MetalLB
    
    
    gcloud container vmware clusters create user-cluster-1 \
      --project=example-project-12345 \
      --location=us-west1 \
      --admin-cluster-membership=projects/example-project-12345/locations/global/memberships/admin-cluster-1 \
      --version=1.15.9-gke.20 \
      --admin-users=sara@example.com \
      --admin-users=amal@example.com \
      --enable-dhcp \
      --service-address-cidr-blocks=10.96.232.0/24 \
      --pod-address-cidr-blocks=192.168.0.0/16 \
      --metal-lb-config-address-pools='pool=lb-pool-1,manual-assign=False,avoid-buggy-ips=True,addresses=10.251.133.0/24;10.251.134.80/32;10.251.134.81/32' \
      --metal-lb-config-address-pools='pool=lb-pool-2,manual-assign=True,addresses=172.16.20.62/32' \
      --control-plane-vip=172.16.20.61 \
      --ingress-vip=172.16.20.62
    

For a description of the `--metal-lb-config-address-pools` flag, see [Load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-api#load_balancer).

### F5 load balancer
    
    
    gcloud container vmware clusters create user-cluster-2 \
      --project=example-project-12345 \
      --location=us-west1 \
      --admin-cluster-membership=projects/example-project-12345/locations/global/memberships/admin-cluster-1 \
      --version=1.15.9-gke.20 \
      --admin-users=sara@example.com \
      --admin-users=amal@example.com \
      --enable-dhcp \
      --service-address-cidr-blocks=10.96.232.0/24 \
      --pod-address-cidr-blocks=192.168.0.0/16 \
      --f5-config-address=203.0.113.2 \
      --f5-config-partition=my-f5-admin-partition \
      --control-plane-vip=172.16.20.61 \
      --ingress-vip=172.16.20.62
    

For a description of the F5 flags, see [Load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-api#load_balancer).

## Static IPs

This section provides examples using static IPs for your cluster nodes. A user cluster needs to have one IP address for each node and an additional IP address for a temporary node that is needed during cluster upgrades, updates, and auto repair. For a description of the `--static-ip-config-ip-blocks` flag see [Networking](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-api#networking).

###  MetalLB
    
    
    gcloud container vmware clusters create user-cluster-3 \
      --project=example-project-12345 \
      --location=europe-west1 \
      --admin-cluster-membership=projects/example-project-12345/locations/global/memberships/admin-cluster-1 \
      --version=1.15.9-gke.20 \
      --admin-users=sara@example.com \
      --admin-users=amal@example.com \
      --static-ip-config-ip-blocks='gateway=172.16.23.254,netmask=255.255.252.0,ips=172.16.20.10 user-vm-1;172.16.20.11 user-vm-2' \
      --static-ip-config-ip-blocks='gateway=172.16.23.255,netmask=255.255.252.0,ips=172.16.20.12 user-vm-3;172.16.20.13 extra-vm' \
      --dns-servers=203.0.113.1,198.51.100.1 \
      --dns-search-domains=example.com,altostrat.com \
      --ntp-servers=216.239.35.4,216.239.35.5 \
      --service-address-cidr-blocks=10.96.232.0/24 \
      --pod-address-cidr-blocks=192.168.0.0/16 \
      --metal-lb-config-address-pools='pool=lb-pool-1,manual-assign=False,avoid-buggy-ips=True,addresses=10.251.133.0/24;10.251.134.80/32;10.251.134.81/32' \
      --metal-lb-config-address-pools='pool=lb-pool-2,manual-assign=True,addresses=172.16.20.62/32' \
      --control-plane-vip=172.16.20.61 \
      --ingress-vip=172.16.20.62
    

### Manual load balancer
    
    
    gcloud container vmware clusters create user-cluster-4 \
      --project=example-project-12345 \
      --location=asia-east1 \
      --admin-cluster-membership=projects/example-project-12345/locations/global/memberships/admin-cluster-1 \
      --version=1.15.9-gke.20 \
      --admin-users=sara@example.com \
      --admin-users=amal@example.com \
      --static-ip-config-ip-blocks='gateway=172.16.23.254,netmask=255.255.252.0,ips=172.16.20.10 user-vm-1;172.16.20.11 user-vm-2' \
      --static-ip-config-ip-blocks='gateway=172.16.23.255,netmask=255.255.252.0,ips=172.16.20.12 user-vm-3;172.16.20.13 extra-vm' \
      --dns-servers=203.0.113.1,198.51.100.1  \
      --ntp-servers=216.239.35.4,216.239.35.5 \
      --service-address-cidr-blocks=10.96.232.0/24 \
      --pod-address-cidr-blocks=192.168.0.0/16 \
      --control-plane-vip=172.16.20.61 \
      --control-plane-node-port=30968 \
      --ingress-vip=172.16.20.62 \
      --ingress-http-node-port=32527 \
      --ingress-https-node-port=30139 \
      --konnectivity-server-node-port=30969
    

## Create a node pool

You can use the following command to create a node pool:
    
    
    gcloud container vmware node-pools create default-pool \
        --cluster=user-cluster-1  \
        --project=example-project-12345 \
        --location=us-west1 \
        --image-type=ubuntu_containerd  \
        --boot-disk-size=40 \
        --cpus=8 \
        --memory=8192 \
        --replicas=5  \
        --min-replicas=5  \
        --max-replicas=10  \
        --enable-load-balancer
      

For descriptions of the flags, see [Create a node pool](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-api#create_the_cluster_and_node_pools).

## What's next

  * [Create a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-api#create_a_user_cluster)
  * [The gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/vmware)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
