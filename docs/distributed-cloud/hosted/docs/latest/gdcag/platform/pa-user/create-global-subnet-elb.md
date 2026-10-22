---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-global-subnet-elb/
title: Create a global subnet for external load balancing \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:27.391076+00:00
---

# Create a global subnet for external load balancing  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-global-subnet-elb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a global subnet for external load balancing Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through how to create a global subnet in Google Distributed Cloud (GDC) air-gapped and use that subnet for an external load balancer (ELB).

Global subnets let you configure subnets that can use external load balancing operations across multiple zones in your GDC organization. Load balancing brings the benefits of improved performance, reliability, and availability of applications and services by distributing network traffic across multiple servers. For more information about global subnets for load balancing, see [About subnets for load balancing](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnet-lb-overview).

This page is for developers within the application operator group who are looking to manage load balancing for their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To create a global subnet and configure it for ELBs, you must have the following:

  * Own the project you are configuring the load balancer for. For more information, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project).
  * The necessary identity and access roles:

    * Ask your Organization IAM Admin to grant you the Load Balancer Admin (`load-balancer-admin`) role.
    * Ask your Organization IAM Admin to grant you the Global Load Balancer Admin (`global-load-balancer-admin`) role.
    * Ask your Organization IAM Admin to grant you the Subnet Organization Admin (`subnet-org-admin`) role.
    * Ask your Organization IAM Admin to grant you the Subnet Project Admin (`subnet-project-admin`) role.

For more information, see [Predefined role descriptions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-descriptions).




## Create a parent global subnet

The parent global subnet you create in this section serves as the IP address pool from which your ELB IP addresses are sourced from. The subnet must include the `ipam.gdc.goog/network-segment: data` label. You can specify the subnet parent using the `spec.parentReference.name` field. You have two options for configuring the CIDR for this parent subnet:

  * Create a subnet using a static CIDR configuration
  * Create a subnet using a dynamic CIDR configuration



For more information on the difference between static and dynamic CIDR configurations, see [Static and dynamic CIDR configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview#static-dynamic-cidr).

### Create a subnet using a static CIDR configuration

Use a static CIDR configuration when you require precise control over your IP address space. This subnet has a type of `Branch`. For more information on the root, branch, and leaf subnet types, see [Subnet hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview#subnet-hierarchy).

To create a global parent subnet with a static CIDR configuration, add your chosen CIDR block to the `spec.ipv4Request.cidr` field:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: ipam.global.gdc.goog/v1
    kind: Subnet
    metadata:
      labels:
        ipam.gdc.goog/network-segment: data
      name: ELB_PARENT_SUBNET_NAME
      namespace: platform
    spec:
      ipv4Request:
        cidr: STATIC_CIDR
      parentReference:
        name: PARENT_NAME
        namespace: platform
      propagationStrategy: None
      type: Branch
    EOF
    

Replace the following:

  * `GLOBAL_API_SERVER`: the global management API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig) for details.
  * `ELB_PARENT_SUBNET_NAME`: the chosen name for your global parent subnet for the ELB.
  * `STATIC_CIDR`: the specific CIDR block you want to allocate for this parent subnet, such as `10.0.10.0/27`.
  * `PARENT_NAME`: the name of the existing parent subnet from which this new subnet is created.



To configure this subnet to work with ELBs, you must create a leaf subnet for the ELB.

### Create a subnet using a dynamic CIDR configuration

The dynamic CIDR configuration automatically allocates an available CIDR block of a specified size from the parent subnet. This simplifies IP address management, especially in larger environments. This subnet has a type of `Branch`. For more information on the root, branch, and leaf subnet types, see [Subnet hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview#subnet-hierarchy). To create a global parent subnet with a dynamic CIDR, configure the `spec.ipv4Request.prefixLength` field with the chosen prefix length:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    piVersion: ipam.global.gdc.goog/v1
    kind: Subnet
    metadata:
      labels:
      ipam.gdc.goog/network-segment: data
      name: ELB_PARENT_SUBNET_NAME
      namespace: platform
    spec:
      ipv4Request:
        prefixLength: PREFIX_LENGTH
      parentReference:
        name: PARENT_NAME
        namespace: platform
      propagationStrategy: None
      type: Branch
    EOF
    

Replace the following:

  * `ELB_PARENT_SUBNET_NAME`: your chosen name for the ELB parent subnet, such as `lb-global-lancer-elb-subnet`.
  * `STATIC_CIDR`: the specific CIDR block you want to use, such as `10.0.10.0/27`. This variable is only applicable for static CIDR configuration.
  * `PARENT_NAME`: the name of the existing parent subnet from which this new subnet is created, such as `default-vpc-workload-cidr`.
  * `PREFIX_LENGTH`: the chosen prefix length for the dynamically allocated CIDR such as `27`. This variable is only applicable for the dynamic CIDR configuration.



To configure this subnet to work with ELBs, you must create a leaf subnet for the ELB.

## Create a leaf subnet for the ELB

After setting up the global parent subnet, you must create a leaf subnet to allocate a single IP address for the global ELB service. This leaf subnet must have a `type` field value of `Leaf` and must reside in the same project namespace as your load balancer resources, such as the `ForwardingRule`, `BackendService`, and `Backend`.

To create the leaf subnet and link it to the ELB, follow these steps:

  1. Create a leaf subnet with a `prefixLength` value of `32`, as it's intended to allocate a single IP address. The `parentReference` value references the previously created parent global subnet:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: ipam.global.gdc.goog/v1
         kind: Subnet
         metadata:
           labels:
             ipam.gdc.goog/allocation-preference: default
             ipam.gdc.goog/network-segment: data
           name: ELB_IP_SUBNET_NAME
           namespace: PROJECT_NAMESPACE
         spec:
           ipv4Request:
             prefixLength: 32
           parentReference:
             name: PARENT_REF
             namespace: platform
           type: Leaf
         EOF
         

Replace the following:

     * `ELB_IP_SUBNET_NAME`: your chosen name for the leaf subnet, such as `lb-project-elb-ip`.
     * `PROJECT_NAMESPACE`: the Kubernetes namespace corresponding to your project where your ELB objects are located, for example, `lb-project`.
     * `PARENT_REF`: the name of the parent subnet that this leaf subnet sources its IP address from, such as the parent global subnet you previously created.
  2. Connect the newly created leaf subnet, which holds the allocated IP address, with the `ForwardingRuleExternal` resource of your ELB. In your `ForwardingRuleExternal` resource, update the `spec.cidrRef.name` field to reference the name of the leaf subnet you created in the previous step:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ForwardingRuleExternal
         metadata:
           name: FRI_NAME
           namespace: PROJECT_NAMESPACE
         spec:
           ports:
             - port: PORT
               protocol: PROTOCOL
           backendServiceRef:
             name: BES_NAME
           cidrRef:
             name: LEAF_SUBNET_NAME
         EOF
         

Replace the following:

     * `FRI_NAME`: your chosen name for the `ForwardingRuleExternal`object, such as `nginx-elb-static-fr`.
     * `PORT`: the port number on which your ELB listens to for incoming traffic such as `80`.
     * `PROTOCOL`: the network protocol your ELB uses, such as `TCP` or `UDP`.
     * `BES_NAME`: the name of the `BackendService` associated with this `ForwardingRuleExternal` resource such as `nginx-bes`.
     * `LEAF_SUBNET_NAME`: the name of the leaf subnet you created in the previous step, such as `lb-project-elb-ip`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
