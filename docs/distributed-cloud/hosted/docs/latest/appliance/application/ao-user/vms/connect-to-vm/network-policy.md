---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/network-policy/
title: Network policy \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:37.139472+00:00
---

# Network policy  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/network-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Network policy Stay organized with collections  Save and categorize content based on your preferences. 

To set a network policy for virtual machine (VM) workloads at the project namespace level, use the `ProjectNetworkPolicy` resource, a multi-cluster network policy for Google Distributed Cloud air-gapped appliance (GDC). It enables you to define policies, which allows communication within projects, between projects, and to external IP addresses.

For traffic within a project, GDC applies a predefined project network policy, the intra-project policy, to each project by default. To enable and control traffic across projects within the same organization, you define [cross-project policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/connect-to-vm/network-policy#cross-project-traffic). When multiple policies are present, GDC additively combines the rules for each project. GDC also allows traffic if at least one of the rules match.

## Request permission and access

To perform the tasks listed in this page, you must have the Project NetworkPolicy Admin role. Ask your Project IAM Admin to grant you the Project NetworkPolicy Admin (`project-networkpolicy-admin`) role in the namespace of the project where the VM resides.

## Intra-project traffic

By default, VM workloads in a project namespace have the ability to communicate with each other without exposing services to the external world, even if the VMs are part of different clusters within the same project.

### Ingress intra-project traffic network policy

When you create a project, you create a default base `ProjectNetworkPolicy` on the Management API server to allow intra-project communication. This policy allows ingress traffic from other workloads in the same project. You can remove it, but be careful if doing so, as this results in denying both intraproject and container workload communication.

### Egress intra-project traffic network policy

By default, you don't need to take action regarding egress. This is because in the absence of an egress policy, all traffic is allowed. However, when you set a single policy, only the traffic the policy specifies is allowed.

When you disable Data Exfiltration Prevention and apply an egress `ProjectNetworkPolicy` to the project, such as preventing access to an external resource, use a required policy to allow intra-project egress:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
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

For project workloads to allow connections from other workloads in another project, you must configure an Ingress policy to allow the other project workloads to ingress.

The following policy enables workloads in the `PROJECT_1` project to permit connections from workloads in the `PROJECT_2` project, as well as the return traffic for the same flows. Run the following command to apply the policy:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
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
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
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

When you grant an ingress cross-project traffic policy to enable workloads in one project, `PROJECT_1`, to allow connections from workloads in another project, `PROJECT_2`, this also grants the return traffic for the same flows. Therefore, you do not need an egress cross-project traffic network policy.

## Cross-organization traffic

To connect a VM workload to a destination outside of your project that resides in a different organization requires explicit approval. That approval is due to Data Exfiltration Prevention, which GDC enables by default and prevents a project from having egress to workloads outside the organization where the project resides. The instructions to add a specific egress policy and enable data exfiltration are as follows in this section.

### Ingress cross-organization traffic network policy

When you've configured a cross-organization egress network policy, you don't need to grant ingress. The _allowed_ egress traffic from the workload outside of your organization goes through a load balancer (LB) and that egress traffic is a source network address translation (NAT) using an IP address that you've allocated for the project.

### Egress cross-organization traffic network policy

To enable egress to services outside of the organization, customize your project network policy, `ProjectNetworkPolicy`. However, because Data Exfiltration Prevention is default-enabled, your customized Egress `ProjectNetworkPolicy` shows a validation error in the status field, and the dataplane ignores it. This happens by design.

Workloads can egress when you allow data exfiltration for a given project. The traffic that you permit to egress is a source network address translation (NAT) using a well-known IP address allocated for the project.

These directions show you how to enable your customized egress policy:

  1. Configure and apply your own customized Egress `ProjectNetworkPolicy`, following the `kubectl` CLI example. Apply the policy on all user workloads in `PROJECT_1`. It allows egress traffic to all hosts in `CIDR`, which reside outside the organization. Your first attempt causes a necessary status error, which is intended.

  2. Apply your `ProjectNetworkPolicy` configuration:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
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
  4. Ask the admin user to disable Data Exfiltration Prevention. This enables your configuration, while preventing all other egress.

**Important:** Disabling Data Exfiltration Prevention, without defining one or more valid `ProjectNetworkPolicy`s, permits all egress traffic to destinations outside your project's organization. Never disable this without first completing step 1 to configure your customized Egress `ProjectNetworkPolicy`.
  5. Check the `ProjectNetworkPolicy` that you just created and verify that the error in the validation status field is gone, and the status `Ready` is `True`, indicating that your policy is in effect:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER get projectnetworkpolicy
         allow-egress-traffic-to-NAME -n PROJECT_1 -o yaml
         

Replace the variables, using the following definitions.

Variable| Definition  
---|---  
`MANAGEMENT_API_SERVER`| The Management API server `kubeconfig` file.  
`PROJECT_1`| The name of the GDC project.  
`CIDR`| The Classless Inter-Domain Routing (CIDR) block of the permitted destination.  
`NAME`| A name associated with the destination.  
  
After you have applied this policy, and provided that you have not defined other egress policies, all other egress traffic is denied for `PROJECT_1`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
