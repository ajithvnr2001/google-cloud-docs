---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/network-policy/
title: Network policy \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:08:14.286360+00:00
---

# Network policy  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/network-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Network policy Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to set network policies for a virtual machine (VM) instance in Google Distributed Cloud (GDC) air-gapped.

To set a network policy for VM workloads at the project namespace level, use the `ProjectNetworkPolicy` resource, a multi-cluster network policy for Distributed Cloud. You can then define policies to enable communication within projects, between projects, and to external IP addresses.

For traffic within a project, GDC applies a predefined project network policy, the [intra-project policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/intra-project-traffic), to each project by default, which can be overridden or extended. To enable and control traffic across projects within the same organization, define [cross-project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/cross-project-traffic). When multiple policies are present, GDC additively combines the rules for each project. GDC also allows traffic if at least one of the rules match.

This document is for developers in platform administrator or application operator groups that create and manage network policies for VMs in a Distributed Cloud environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

### Request IAM roles

Contact your Project IAM Admin to request the following roles on your project:

  * **Project NetworkPolicy Admin** (`project-networkpolicy-admin`): create, list, update and delete project network policies for VM instances in the project namespace.



This role must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.Project

## Intra-project traffic

By default, VM workloads in a project namespace have the ability to communicate with each other without exposing services to the external world, even if the VMs are part of different clusters within the same project.

### Ingress intra-project traffic network policy

When you create a project, you create a default base `ProjectNetworkPolicy` on the Management API server to allow intra-project communication. This policy allows ingress traffic from other workloads in the same project. You can remove it, but be careful if doing so, as this results in denying both intraproject and container workload communication.

### Egress intra-project traffic network policy

By default, you don't need to take action regarding egress. This is because in the absence of an egress policy, all traffic is allowed. However, when you set a single policy, only the traffic the policy specifies is allowed.

When you disable [Data Exfiltration Prevention](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/data-exfiltration#allow-egress-traffic) and apply an egress `ProjectNetworkPolicy` to the project, such as preventing access to an external resource, use a required policy to allow intra-project egress:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
      apply -f - <<EOF
    apiVersion: networking.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT_1
      name: allow-intra-project-egress-traffic
    spec:
      policyType: Egress
      ingress:
      - from:
        - projects:
            matchNames:
            - PROJECT_1
    EOF
    

## Cross-project (within org) traffic

VM workloads from different project namespaces _but within the same organization_ can communicate with each other by applying a cross-project network policy.

**Important:** This policy only applies to projects _within the same org_ that are from different project namespaces. To read about _cross-organization_ traffic, which requires specific instructions since Data Exfiltration Prevention protects against all such egress by default, see the Cross-org traffic section.

### Ingress cross-project traffic network policy

For project workloads to allow connections from other workloads in another project, you must configure an Ingress policy to allow the other project workloads to data transfer out.

The following policy enables workloads in the `PROJECT_1` project to permit connections from workloads in the `PROJECT_2` project, as well as the return traffic for the same flows. If you want to access your VM in the `PROJECT_1` from a source inside the `PROJECT_2`, you can also use this policy. Run the following command to apply the policy:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
      apply -f - <<EOF
    apiVersion: networking.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT_1
      name: allow-ingress-traffic-from-PROJECT_2
    spec:
      policyType: Ingress
      subject:
        subjectType: UserWorkload
      ingress:
      - from:
        - projects:
            matchNames:
            - PROJECT_2
    EOF
    

The preceding command allows `PROJECT_2` to go to `PROJECT_1`, but doesn't allow connections initiated from `PROJECT_1` to `PROJECT_2`. For the latter, you require a reciprocal policy in the `PROJECT_2` project. Run the following command to apply the reciprocal policy:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER \
      apply -f - <<EOF
    apiVersion: networking.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT_2
      name: allow-ingress-traffic-from-PROJECT_1
    spec:
      policyType: Ingress
      subject:
        subjectType: UserWorkload
      ingress:
      - from:
        - projects:
            matchNames:
            - PROJECT_1
    EOF
    

You've now permitted connections initiated to and from `PROJECT_1` and `PROJECT_2`.

Use the following definitions for your variables.

Variable| Definition  
---|---  
`MANAGEMENT_API_SERVER`| The Management API server `kubeconfig` path.  
`PROJECT_1`| The name of a GDC project corresponding to PROJECT_1 in the example.  
`PROJECT_2`| The name of a GDC project corresponding to PROJECT_2 in the example.  
  
### Egress cross-project traffic network policy

When you grant an ingress cross-project traffic policy to enable workloads in one project, `PROJECT_1`, to allow connections from workloads in another project, `PROJECT_2`, this also grants the return traffic for the same flows. Therefore, you don't need an egress cross-project traffic network policy.

## Cross-organization traffic

To connect a VM workload to a destination outside of your project that resides in a different organization requires explicit approval. That approval is due to Data Exfiltration Prevention, which GDC enables by default and prevents a project from having egress to workloads outside the organization where the project resides. The instructions to add a specific egress policy and enable data exfiltration are as follows in this section.

### Ingress cross-organization traffic network policy

To allow ingress traffic across different organizations, a `ProjectNetworkPolicy` must be applied which allows traffic from organization external clients to your project, for example connect to the VM using SSH.

A corresponding Egress policy is not required for the reply traffic. Return traffic is implicitly allowed.

If you want to access your VM in the `PROJECT_1` from a source outside the organization that the VM resides in, you must apply the following policy to achieve this. You have to get and use the `CIDR` which contains your source IP address. The `CIDR` should be in `network/len` notation. For example, `192.0.2.0/21` is a valid one.

  1. Configure and apply your Ingress `ProjectNetworkPolicy`, following the `kubectl` example. Apply the policy on all user workloads in `PROJECT_1`. It allows ingress traffic to all hosts in `CIDR`, which reside outside the organization.

  2. Apply your `ProjectNetworkPolicy` configuration:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           apply -f - <<EOF
         apiVersion: networking.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: PROJECT_1
           name: allow-external-traffic
         spec:
           policyType: Ingress
           subject:
             subjectType: UserWorkload
           ingress:
           - from:
             - ipBlock:
                 cidr: CIDR
         EOF
         




### Egress cross-organization traffic network policy

To enable data transfer out to services outside of the organization, customize your project network policy, `ProjectNetworkPolicy`. Since Data Exfiltration Prevention is enabled by default, your customized Egress `ProjectNetworkPolicy` shows a validation error in the status field, and the dataplane ignores it. This process happens by design.

As stated in [Security and connectivity](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview#security-and-connectivity), workloads can data transfer out when you let data exfiltration for a given project. The traffic that you permit to data transfer out is a source network address translation (NAT) using a known IP address allocated for the project. [Security and connectivity](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview#security-and-connectivity) also provides details about project network policy (`ProjectNetworkPolicy`) enforcement.

A corresponding Ingress policy is not required for the reply traffic. Return traffic is implicitly allowed.

Enable your customized egress policy:

  1. Configure and apply your own customized Egress `ProjectNetworkPolicy`, following the `kubectl` example. Apply the policy on all user workloads in `PROJECT_1`. It allows egress traffic to all hosts in `CIDR`, which reside outside the organization. Your first attempt causes a necessary status error, which is intended.

  2. Apply your `ProjectNetworkPolicy` configuration:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           apply -f - <<EOF
         apiVersion: networking.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: PROJECT_1
           name: allow-egress-traffic-to-NAME
         spec:
           policyType: Egress
           subject:
             subjectType: UserWorkload
           egress:
           - to:
             - ipBlock:
                 cidr: CIDR
         EOF
         

  3. When you finish, confirm that you see a _validation error_ in your status.

**Important:** Only the Egress traffic to destinations outside your project's organization that you explicitly allow in your Egress `ProjectNetworkPolicy` configuration is granted egress. Any other egress traffic is denied. Therefore, only apply a customized Egress `ProjectNetworkPolicy` when requirements mandate such a policy.
  4. Ask the administrator user to disable Data Exfiltration Prevention. This enables your configuration, while preventing all other egress.

**Important:** Disabling Data Exfiltration Prevention, without defining one or more valid `ProjectNetworkPolicy`s, permits all egress traffic to destinations outside your project's organization. Never disable this without first completing step 1 to configure your customized Egress `ProjectNetworkPolicy`.
  5. Check the `ProjectNetworkPolicy` that you just created and verify that the error in the validation status field is gone, and the status `Ready` is `True`, indicating that your policy is in effect:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           get projectnetworkpolicy allow-egress-traffic-to-NAME \
           -n PROJECT_1 \
           -o yaml
         

Replace the variables, using the following definitions.

Variable| Definition  
---|---  
`MANAGEMENT_API_SERVER`| The Management API server kubeconfig path.  
`PROJECT_1`| The name of the GDC project.  
`CIDR`| The Classless Inter-Domain Routing (CIDR) block of the permitted destination.  
`NAME`| A name associated with the destination.  
  
After you have applied this policy, and provided that you have not defined other egress policies, all other egress traffic is denied for `PROJECT_1`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
