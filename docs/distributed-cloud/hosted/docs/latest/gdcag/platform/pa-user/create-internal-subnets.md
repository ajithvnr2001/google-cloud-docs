---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-internal-subnets/
title: Provision IP addresses for workloads \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:45.918641+00:00
---

# Provision IP addresses for workloads  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-internal-subnets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Provision IP addresses for workloads Stay organized with collections  Save and categorize content based on your preferences. 

Create additional subnets in your organization's internal Virtual Private Cloud (VPC), or Default VPC, to support your internal networking requirements. For example, add VPC subnets to ensure that your internal workloads, such as virtual machines (VMs) and containers, have enough IP addresses.

There are several tasks outlined on this page, which are not intended to be completed in order:

  * **Create a zonal branch subnet for workloads**: this task is useful to further organize or allocate your zone's existing internal IP addresses to workloads.
  * **Create a leaf subnet for an individual workload**: this task is useful when you have a new workload that doesn't yet have an IP address to use.
  * **Allocate zonal subnet from global IP address range**: this task is useful when your zone no longer has enough internal IP address space.
  * **Divide root global subnet without zone allocation**: this task is useful to further organize the internal IP addresses in the global API server before allocating them to a zone.
  * **Add new network root range global subnet**: this task is useful when your Default VPC no longer has enough global internal IP address space to allocate to your zones.



For an overview of subnets and their concepts before you complete the tasks in this page, see [Subnets and IP addresses](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview).

This document is for platform administrators and application operators who are responsible for managing network traffic for their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To get the permission that you need to create subnets, ask your IAM Org Admin to grant you the Subnet Org Admin (`subnet-org-admin`) IAM role. This role is not bound to a namespace.

## Create a zonal branch subnet for workloads

To further subdivide IP addresses in your zonal Default VPC, you can create a zonal internal subnet from the zone's existing zonal root subnet. You must create this subnet type in the `platform` namespace.

If the parent zonal root subnet doesn't have enough IP addresses available, allocate another zonal subnet from the global IP address range before you continue.

  * In a terminal window, create the new zonal subnet in the management API server:
        
        kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG apply -f - <<EOF
        apiVersion: ipam.gdc.goog/v1
        kind: Subnet
        metadata:
          labels:
            ipam.gdc.goog/vpc: default-vpc
          name: SUBNET_NAME
          namespace: platform
        spec:
          ipv4Request:
            prefixLength: CIDR_PREFIX_LENGTH
          networkSpec:
            enableGateway: true
            enableVLANID: false
          parentReference:
            name: PARENT_SUBNET_NAME
            namespace: platform
          type: Branch
        EOF
        

Replace the following:

    * `MANAGEMENT_API_SERVER_KUBECONFIG`: the path to the kubeconfig file of your management API server. For more information, see [Zonal management API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).

    * `SUBNET_NAME`: the name of your new network subnet.

    * `CIDR_PREFIX_LENGTH`: the prefix length for your new subnet, such as `27`. This field dynamically allocates the next available IP address range of that size from the parent subnet. Use the `prefixLength` field when you only care about the size of the subnet, not its specific IP address range.

To assign a specific IP address range instead, follow these steps:

      1. Remove the `prefixLength: CIDR_PREFIX_LENGTH` line.
      2. Add a `cidr: "YOUR_CIDR_BLOCK"` line in its place, such as `cidr: "10.0.10.0/27"`.

Use the `cidr` field when you are following a strict IP plan and need to assign a precise, predictable IP address range. This range must be a valid and available subnet within the parent subnet.

    * `PARENT_SUBNET_NAME`: the name of the parent subnet, such as `default-vpc-zone0-cidr`. The parent subnet is typically a zonal root subnet in the Default VPC.

For more information, see the API reference documentation for the [`Subnet`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/v1/ipam-v1#subnet) resource.

You can continue to subdivide your zonal subnets or create a leaf subnet to allocate an individual IP address directly to an internal workload.




## Create a leaf subnet for an individual workload

To allocate a single IP address for your workload, you must create a leaf subnet. This leaf subnet must have the field value `type: Leaf` and must reside in the same project namespace as your workload resource, such as a VM or container.

Your leaf subnet must be configured with a `prefixLength` value of `32`, because it's intended to allocate a single IP address. The `parentReference` value references a previously allocated subnet, such as the parent zonal subnet you created in Create a zonal branch subnet for workloads.

  * In a terminal window, create the leaf subnet in the management API server:
        
        kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG apply -f - <<EOF
        apiVersion: ipam.gdc.goog/v1
        kind: Subnet
        metadata:
          labels:
            ipam.gdc.goog/vpc: default-vpc
          name: SUBNET_NAME
          namespace: PROJECT_NAMESPACE
        spec:
          ipv4Request:
            prefixLength: 32
          parentReference:
            name: PARENT_SUBNET
            namespace: PARENT_NAMESPACE
          type: Leaf
        EOF
        

Replace the following:

    * `MANAGEMENT_API_SERVER_KUBECONFIG`: the path to the kubeconfig file of your management API server. For more information, see [Zonal management API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).
    * `SUBNET_NAME`: the name for the leaf subnet.
    * `PROJECT_NAMESPACE`: the project namespace corresponding to your project where your workloads are located.
    * `PARENT_SUBNET`: the name of the parent subnet that this leaf subnet will source its IP address from.
    * `PARENT_NAMESPACE`: the `PROJECT_NAMESPACE` or the `platform` namespace.



Your individual IP address is now available to be used by your internal workloads, such as VMs and containers. For more information about how to configure the IP address for your workloads, see [Create a VM with a static or dynamic IP address](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start#create-vm-with-ip) or [Configure an internal load balancer for container workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/ilb-service).

## Allocate zonal subnet from global IP address range

If your zone doesn't provide enough IP addresses for your workloads from the existing zonal root subnet IP address range, you can allocate additional IP addresses from the global IP address root range.

To allocate a zonal subnet from the global IP address range, complete the following steps for the Default VPC network in the `platform` namespace:

  1. In a terminal window, describe all of the Default VPC's root subnets and check their available CIDR blocks:
         
         kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG describe subnets --namespace platform \
             -l ipam.gdc.goog/vpc=default-vpc,ipam.gdc.goog/usage=network-root-range
         

Replace `GLOBAL_API_SERVER_KUBECONFIG` with the path to the kubeconfig file of the global API server. For more information, see [Global API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig). The labels are constant and must remain the same.

The output is similar to the following:
         
         Name:         default-vpc-root-cidr
         Namespace:    platform
         Labels:       ipam.gdc.goog/allocation-preference=default
                       ipam.gdc.goog/subnet-group=default-vpc-root-group
                       ipam.gdc.goog/usage=network-root-range
                       ipam.gdc.goog/vpc=default-vpc
         Annotations:  <none>
         API Version:  ipam.global.gdc.goog/v1
         Kind:         Subnet
         Metadata:
           Creation Timestamp:  2025-06-18T23:05:38Z
           Finalizers:
             global-subnet-finalizer
           Generation:        1
           Resource Version:  439434
           UID:               5ed1c51a-b5ee-473e-a185-8e065a87ae8f
         Spec:
           ipv4Request:
             Cidr:                10.252.0.0/14
           Propagation Strategy:  None
           Type:                  Root
         Status:
           Children Refs:
             Name:       default-vpc-zone1-root-cidr
             Namespace:  platform
             Type:       SingleSubnet
           Conditions:
             Last Transition Time:  2025-06-18T23:05:38Z
             Message:               IP allocation finished successfully
             Observed Generation:   1
             Reason:                AllocationSucceeded
             Status:                True
             Type:                  Ready
           ipv4Allocation:
             Available CIDRs:
               10.254.0.0/15
               10.253.0.0/16
             Cidr:  10.252.0.0/14
         Events:    <none>
         

Note the `Status.ipv4Allocation.Available CIDRs` values. These values are the available CIDR blocks that the next step references. In the previous output, the CIDR ranges `10.254.0.0/15` and `10.253.0.0/16` are available. Your output might show multiple subnets. Note all available CIDR blocks and their source subnets.

  2. Compare the largest available CIDR block from the previous step with the size of the CIDR block needed for your zone. If the largest available CIDR block is not large enough to allocate your new subnet, add a new network root range global subnet before you continue. Note the parent subnet from which you decide to get the CIDR block for your new subnet.

For example, if you require a `/13` CIDR block, but the available CIDRs only include `/15` and `/16`, you must add a new network root range global subnet. If you require a `/15` subnet, you can allocate a new zonal subnet from the existing `/15` CIDR block.

  3. Create the new subnet in the global API server:
         
         kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG apply -f - <<EOF
         apiVersion: ipam.global.gdc.goog/v1
         kind: Subnet
         metadata:
           labels:
             ipam.gdc.goog/vpc: default-vpc
             ipam.gdc.goog/usage: zone-network-root-range
           name: SUBNET_NAME
           namespace: platform
         spec:
           ipv4Request:
             prefixLength: CIDR_PREFIX_LENGTH
           zone: ZONE_NAME
           propagationStrategy: SingleZone
           type: Branch
           parentReference:
             name: PARENT_SUBNET_NAME
             namespace: ORG_NAME
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER_KUBECONFIG`: the path to the kubeconfig file of the global API server. For more information, see [Global API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig).
     * `SUBNET_NAME`: the name of the new subnet.
     * `CIDR_PREFIX_LENGTH`: the CIDR prefix length of the new subnet that is dynamically allocated, such as `20`. To statically set the CIDR, replace the `prefixLength` field with the `cidr` field, and then set the CIDR block, such as `10.0.10.0/27`.
     * `ZONE_NAME`: the zone for which to allocate the subnet, such as `zone1`.
     * `PARENT_SUBNET_NAME`: the name of the parent subnet, such as `default-vpc-root-cidr`, or the new network root range global subnet you created.
     * `ORG_NAME`: the name of the organization.

For more information, see the API reference documentation for the [`Subnet`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/v1/ipam-v1#subnet) resource.

  4. Verify the subnet is ready and available in the global API server by checking that its status `Ready` type is `true`:
         
         kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG get subnet --namespace platform \
             SUBNET_NAME --output jsonpath='{.status.conditions[?(@.type=="Ready")].status}'
         

The output is similar to the following:
         
         status:
           conditions:
           - lastTransitionTime: "2025-06-06T07:28:48Z"
             message: IP allocation finished successfully
             observedGeneration: 1
             reason: AllocationSucceeded
             status: "True"
             type: Ready
         

  5. Verify the zonal subnet is created in the zonal management API server, and its status `Ready` type is `true`:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER_KUBECONFIG get subnet --namespace platform \
             SUBNET_NAME --output jsonpath='{.status.conditions[?(@.type=="Ready")].status}'
         

Replace `MANAGEMENT_API_SERVER_KUBECONFIG` with the path to the kubeconfig file of your management API server. For more information, see [Zonal management API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).

The output is similar to the following:
         
         status:
           conditions:
           - lastTransitionTime: "2025-06-06T07:29:34Z"
             message: IP allocation finished successfully
             observedGeneration: 1
             reason: AllocationSucceeded
             status: "True"
             type: Ready
         

From this new zonal subnet, you can create more zonal child subnets or allocate an individual IP address directly to an internal workload.




## Divide root global subnet without zone allocation

To further divide a global subnet without allocating it to a zone, create a global subnet and omit the propagation strategy in the `Subnet` custom resource. This approach is useful if you want to continue organizing your globally accessible IP address range from the global root subnet without allocating the IP addresses to a zone.

To divide your global root subnet within the global scope, complete the following steps in the `platform` namespace:

  1. In a terminal window, describe all of the Default VPC's root subnets and check their available CIDR blocks:
         
         kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG describe subnets --namespace platform \
             -l ipam.gdc.goog/vpc=default-vpc,ipam.gdc.goog/usage=network-root-range
         

Replace `GLOBAL_API_SERVER_KUBECONFIG` with the path to the kubeconfig file of the global API server. For more information, see [Global API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig). The labels are constant and must remain the same.

The output is similar to the following:
         
         Name:         default-vpc-root-cidr
         Namespace:    platform
         Labels:       ipam.gdc.goog/allocation-preference=default
                       ipam.gdc.goog/subnet-group=default-vpc-root-group
                       ipam.gdc.goog/usage=network-root-range
                       ipam.gdc.goog/vpc=default-vpc
         Annotations:  <none>
         API Version:  ipam.global.gdc.goog/v1
         Kind:         Subnet
         Metadata:
           Creation Timestamp:  2025-06-18T23:05:38Z
           Finalizers:
             global-subnet-finalizer
           Generation:        1
           Resource Version:  439434
           UID:               5ed1c51a-b5ee-473e-a185-8e065a87ae8f
         Spec:
           ipv4Request:
             Cidr:                10.252.0.0/14
           Propagation Strategy:  None
           Type:                  Root
         Status:
           Children Refs:
             Name:       default-vpc-zone1-root-cidr
             Namespace:  platform
             Type:       SingleSubnet
           Conditions:
             Last Transition Time:  2025-06-18T23:05:38Z
             Message:               IP allocation finished successfully
             Observed Generation:   1
             Reason:                AllocationSucceeded
             Status:                True
             Type:                  Ready
           ipv4Allocation:
             Available CIDRs:
               10.254.0.0/15
               10.253.0.0/16
             Cidr:  10.252.0.0/14
         Events:    <none>
         

Note the `Status.ipv4Allocation.Available CIDRs` values. These values are the available CIDR blocks that the next step references. In the previous output, the CIDR ranges `10.254.0.0/15` and `10.253.0.0/16` are available. There can be multiple subnets in your output depending on the number of root subnets you have, so note all the available CIDR blocks, and note from which subnet the available CIDR block is from.

  2. Compare the largest available CIDR block from the previous step with the size of the CIDR block needed for your new global subnet. If the largest available CIDR block is not large enough to allocate your new subnet, add a new network root range global subnet before you continue. Note the parent subnet from which you decide to get the CIDR block for your new subnet.

For example, if you require a `/13` CIDR block, but the available CIDRs only include `/15` and `/16`, you must create a new network root range global subnet. If you require a `/15` subnet, you can allocate the new global subnet from the existing `/15` CIDR block.

  3. Create the new subnet in the global API server:
         
         kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG apply -f - <<EOF
         apiVersion: ipam.global.gdc.goog/v1
         kind: Subnet
         metadata:
           labels:
             ipam.gdc.goog/vpc: default-vpc
             ipam.gdc.goog/usage: zone-network-root-range
           name: SUBNET_NAME
           namespace: platform
         spec:
           ipv4Request:
             prefixLength: CIDR_PREFIX_LENGTH
           propagationStrategy: None
           type: Branch
           parentReference:
             name: PARENT_SUBNET_NAME
             namespace: ORG_NAME
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER_KUBECONFIG`: the path to the kubeconfig file of the global API server. For more information, see [Global API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig).
     * `SUBNET_NAME`: the name of the new subnet.
     * `CIDR_PREFIX_LENGTH`: the CIDR prefix length of the new subnet that is dynamically allocated, such as `20`. To statically set the CIDR, replace the `prefixLength` field with the `cidr` field, and then set the CIDR block, such as `10.0.10.0/27`.
     * `PARENT_SUBNET_NAME`: the name of the parent subnet, such as `default-vpc-root-cidr`, or the new network root range global subnet you created.
     * `ORG_NAME`: the name of the organization.

For more information, see the API reference documentation for the global [`Subnet`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/ipam/v1/global-ipam-v1#subnet) resource.

  4. Verify the subnet is ready and available in the global API server by checking that its status `Ready` type is `true`:
         
         kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG get subnet --namespace platform \
             SUBNET_NAME --output jsonpath='{.status.conditions[?(@.type=="Ready")].status}'
         

The output is similar to the following:
         
         status:
           conditions:
           - lastTransitionTime: "2025-06-06T07:28:48Z"
             message: IP allocation finished successfully
             observedGeneration: 1
             reason: AllocationSucceeded
             status: "True"
             type: Ready
         




The new global subnet for your organization in the Default VPC is available. You can create a subnet for a particular zone from this new global parent subnet.

## Add new network root range global subnet

Global subnets with the `ipam.gdc.goog/usage: network-root-range` label host the CIDR for all the zones of the network. If the CIDR is used up, you must create a new network root range subnet in the global API server. You can create multiple root global subnets, if needed.

To create a new network root range subnet, complete the following steps:

  * In a terminal window, create the new network root range global subnet for the Default VPC in the `platform` namespace:
        
        kubectl --kubeconfig GLOBAL_API_SERVER_KUBECONFIG apply -f - <<EOF
        apiVersion: ipam.global.gdc.goog/v1
        kind: Subnet
        metadata:
          labels:
            ipam.gdc.goog/vpc: default-vpc
            ipam.gdc.goog/usage: network-root-range
          name: SUBNET_NAME
          namespace: platform
        spec:
          ipv4Request:
            cidr: NEW_CIDR
          type: Root
        EOF
        

Replace the following:

    * `GLOBAL_API_SERVER_KUBECONFIG`: the path to the kubeconfig file of the global API server. For more information, see [Global API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig).
    * `SUBNET_NAME`: the name of the new subnet.
    * `NEW_CIDR`: the new CIDR for the subnet. This CIDR cannot overlap with any CIDR in all the existing subnets with the `ipam.gdc.goog/usage: network-root-range` label in the same global API server.



This new global root range subnet can be subdivided within the global API server or allocated to a specific zone.

## What's next

  * [Subnets and IP addresses](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview)
  * [Networking overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/networking-overview)
  * [Deploy a highly available VM application](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/deploy-ha-vm-app)
  * [Deploy a highly available container application](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/deploy-ha-container-app)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
