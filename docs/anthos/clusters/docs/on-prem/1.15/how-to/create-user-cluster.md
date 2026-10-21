---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster/
title: Create a user cluster (kubeception) \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:53.350371+00:00
---

# Create a user cluster (kubeception)  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Create a user cluster (kubeception) Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/create-user-cluster)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/create-user-cluster)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to create a user cluster that uses kubeception.

## What is kubeception?

The term [_kubeception_](https://kubernetes.io/blog/2017/01/how-we-run-kubernetes-in-kubernetes-kubeception/) is used to convey the idea that a Kubernetes cluster is used to create and manage other Kubernetes clusters. In the context of Google Distributed Cloud, kubeception refers to the case where the control plane for a user cluster runs on one or more nodes in an admin cluster.

We don't recommend using kubeception. Instead, we recommend using [Controlplane V2](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-controlplane-v2). With Controlplane V2, the control-plane nodes for the user cluster are in the user cluster itself.

## Plan your IP addresses

Follow the instructions in [Plan your IP addresses (kubeception)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/plan-ip-addresses-kubeception).

## Fill in a cluster configuration file

Follow the instructions in [Create a user cluster (Controlplane V2)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-controlplane-v2).

As you fill in your user cluster configuration file:

  * Set `enableControlplaneV2` to `false`.

  * Decide what type of load balancing you want to use. The options are:

    * MetalLB bundled load balancing. Set [`loadBalancer.kind`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#loadbalancer-kind-field) to `"MetalLB"`. Also fill in the [`loadBalancer.metalLB.addressPools`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#loadbalancer-metallb-section) section, and set `enableLoadBalancer` to `true` for at least one of your node pools. For more information, see [Bundled load balancing with MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance-metallb).

    * Seesaw bundled load balancing. Set `loadBalancer.kind` to `"Seesaw"`, and fill in the [`loadBalancer.seesaw`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#loadbalancer-seesaw-section) section. For more information, see [Bundled load balancing with Seesaw](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance).

    * Integrated load balancing with F5 BIG-IP. Set `loadBalancer.kind` to `"F5BigIP"`, and fill in the [`f5BigIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#loadbalancer-f5bigip-section) section. For more information, see [Load balancing with F5 BIG-IP](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/f5-big-ip-load-balance).

    * Manual load balancing. Set `loadBalancer.kind` to `"ManualLB"`, and fill in the [`manualLB`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#loadbalancer-manuallb-section) section. For more information, see [Manual load balancing](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/manual-load-balance).

For more information about load balancing options, see [Overview of load balancing](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/setup-load-balance).

  * Decide whether you want to enable [Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2) for your user cluster, and set [enableDataplaneV2](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#enabledataplanev2-field) accordingly.




### Example of filled-in configuration files

Here is an example of a filled-in IP block file and a filled-in user cluster configuration file. The configuration enables some, but not all, of the available features.

#### user-ipblock.yaml
    
    
    blocks:
      - netmask: 255.255.252.0
        gateway: 172.16.23.254
        ips:
        - ip: 172.16.20.21
          hostname: user-host1
        - ip: 172.16.20.22
          hostname: user-host2
        - ip: 172.16.20.23
          hostname: user-host3
        - ip: 172.16.20.24
          hostname: user-host4
    

#### user-cluster.yaml
    
    
    apiVersion: v1
    kind: UserCluster
    name: "my-user-cluster"
    gkeOnPremVersion: 1.15.0-gke.581
    enableControlplaneV2: false
    network:
      hostConfig:
        dnsServers:
        - "203.0.113.1"
        - "198.51.100.1"
        ntpServers:
        - "216.239.35.4"
      ipMode:
        type: static
        ipBlockFilePath: "user-ipblock.yaml"
      serviceCIDR: 10.96.0.0/20
      podCIDR: 192.168.0.0/16
    loadBalancer:
      vips:
        controlPlaneVIP: "172.16.20.32"
        ingressVIP: "172.16.21.30"
      kind: "MetalLB"
      metalLB:
        addressPools:
        - name: "my-address-pool"
          addresses:
          - "172.16.21.30 - 172.16.21.39"
    enableDataplaneV2: true
    masterNode:
      cpus: 4
      memoryMB: 8192
      replicas: 1
    nodePools:
    - name: "my-node-pool"
      cpus: 4
      memoryMB: 8192
      replicas: 3
      osImageType: "ubuntu_containerd"
      enableLoadBalancer: true
    antiAffinityGroups:
      enabled: true
    gkeConnect:
      projectID: "my-project-123"
      registerServiceAccountKeyPath: "connect-register-sa-2203040617.json"
    stackdriver:
      projectID: "my-project-123"
      clusterLocation: "us-central1"
      enableVPC: false
      serviceAccountKeyPath: "log-mon-sa-2203040617.json"
    autoRepair:
      enabled: true
    

## Validate your configuration file

After you've filled in your user cluster configuration file, run `gkectl check-config` to verify that the file is valid:
    
    
    gkectl check-config --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of the kubeconfig file for your admin cluster

  * USER_CLUSTER_CONFIG: the path of your user cluster configuration file




If the command returns any failure messages, fix the issues and validate the file again.

If you want to skip the more time-consuming validations, pass the `--fast` flag. To skip individual validations, use the `--skip-validation-xxx` flags. To learn more about the `check-config` command, see [Running preflight checks](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/preflight-checks).

## (Optional) Create a Seesaw load balancer for your user cluster

If you have chosen to use the bundled Seesaw load balancer, do the step in this section. Otherwise, skip this section.

Create and configure the VMs for your [Seesaw load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance):
    
    
    gkectl create loadbalancer --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

## (Optional) Import OS images to vSphere, and push container images to a private registry

Run `gkectl prepare` if any of the following are true:

  * Your user cluster is in a different vSphere data center from your admin cluster.

  * Your user cluster has a different vCenter Server from your admin cluster.

  * Your user cluster uses a private container registry that is different from the private registry used by your admin cluster.



    
    
    gkectl prepare --kubeconfig ADMIN_CLUSTER_KUBECONFIG \ 
        --bundle-path BUNDLE \
        --user-cluster-config USER_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of your admin cluster kubeconfig file

  * BUNDLE: the path of the bundle file. This file is on your admin workstation in `/var/lib/gke/bundles/`. For example:
        
        /var/lib/gke/bundles/gke-onprem-vsphere-1.14.0-gke.421-full.tgz
        

  * USER_CLUSTER_CONFIG: the path of your user cluster configuration file




## Create the user cluster

Run the following command to create the user cluster:
    
    
    gkectl create cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG 
    

Locate the user cluster kubeconfig file 

The `gkectl create cluster` command creates a kubeconfig file named `USER_CLUSTER_NAME-kubeconfig` in the current directory. You will need this kubeconfig file later to interact with your user cluster.

The kubeconfig file contains the name of your user cluster. To view the cluster name, you can run:
    
    
    kubectl config get-clusters --kubeconfig USER_CLUSTER_KUBECONFIG
    

The output shows the name of the cluster. For example:
    
    
    NAME
    my-user-cluster
    

If you like, you can change the name and location of your kubeconfig file.

## Verify that your user cluster is running

Run the following command to verify that your user cluster is running:
    
    
    kubectl get nodes --kubeconfig USER_CLUSTER_KUBECONFIG
    

Replace USER_CLUSTER_KUBECONFIG with the path of your user cluster kubeconfig file.

The output shows the user cluster nodes. For example:
    
    
    my-user-cluster-node-pool-69-d46d77885-7b7tx   Ready ...
    my-user-cluster-node-pool-69-d46d77885-lsvzk   Ready ...
    my-user-cluster-node-pool-69-d46d77885-sswjk   Ready ...
    

## Troubleshooting

See [Troubleshooting cluster creation and upgrade](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/troubleshoot-cluster-creation-upgrade).

## What's next

  * [Connect to your cluster from the Google Cloud console](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/connecting-to-a-cluster).
  * [Deploy an application](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/deploy-first-app).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
