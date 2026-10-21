---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/allow-all-traffic/
title: Create allow-all network policies \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:48.121848+00:00
---

# Create allow-all network policies  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/allow-all-traffic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create allow-all network policies Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions to configure allow-all traffic network policies in Google Distributed Cloud (GDC) air-gapped.

Project network policies define either ingress or egress rules. You can define policies that allow communication within projects, between projects, and with external IP addresses.

## Before you begin

To configure allow-all traffic network policies, you must have the following:

  * The necessary identity and access roles. For more information, see [Prepare predefined roles and access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview#prepare-predefined-roles-and-access).
  * An existing project. For more information, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project).



## Create an allow-all traffic policy

This policy allows traffic to and from any source, including other projects and external IP addresses.

### Allow all ingress traffic

To allow all incoming traffic from any source to all workloads in your project, create the following policy:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT
      name: allow-all-ingress
    spec:
      policyType: Ingress
      ingress:
      - {}
    EOF
    

### Allow all egress traffic

To allow all outgoing traffic to any destination from all workloads in your project, create the following policy:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT
      name: allow-all-egress
    spec:
      policyType: Egress
      egress:
      - {}
    EOF
    

Replace the following:

  * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
  * `PROJECT`: the name of the project where you want to allow all traffic.



## Create an allow-all-external traffic policy

This policy allows traffic to and from IP addresses external to the organization.

### Allow all external ingress traffic

To allow all incoming traffic from external IP addresses to all workloads in a project, create the following policy:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT
      name: allow-all-external-ingress
    spec:
      policyType: Ingress
      ingress:
      - from:
        - ipBlock:
            cidr: 0.0.0.0/0
    EOF
    

**Warning:** Because the `0.0.0.0/0` CIDR block does not match workloads within the organization across zones and clusters, this rule blocks traffic from those workloads.

### Allow all external egress traffic

To allow all outgoing traffic from all workloads in your project to external IP addresses, create the following policy:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT
      name: allow-all-external-egress
    spec:
      policyType: Egress
      egress:
      - to:
        - ipBlock:
            cidr: 0.0.0.0/0
    EOF
    

Replace the following:

  * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
  * `PROJECT`: the name of the project where you want to allow all external traffic.



## Create an allow-all-projects traffic policy

This policy allows traffic to and from all projects within the organization.

### Allow all projects ingress traffic

To allow incoming traffic from all projects to all workloads in your project, create the following policy:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT
      name: allow-all-projects-ingress
    spec:
      policyType: Ingress
      ingress:
      - from:
        - projectSelector: {}
    EOF
    

### Allow all projects egress traffic

To allow outgoing traffic from all workloads in your project to all projects, create the following policy:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT
      name: allow-all-projects-egress
    spec:
      policyType: Egress
      egress:
      - to:
        - projectSelector: {}
    EOF
    

Replace the following:

  * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
  * `PROJECT`: the name of the project where you want to allow all projects traffic.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
