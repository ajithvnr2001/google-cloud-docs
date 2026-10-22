---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/deny-traffic/
title: Create explicit deny network policies \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:08.519285+00:00
---

# Create explicit deny network policies  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/deny-traffic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create explicit deny network policies Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** This is a Preview feature that is available as-is and is not recommended for production environments. Google provides no Service Level Agreements (SLA) or technical support commitments for Preview features. For more information, see [feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages#preview).

This page provides instructions to configure explicit deny project network policies in Google Distributed Cloud (GDC) air-gapped.

Explicit deny rules allow you to restrict connectivity between workloads and services in different projects or CIDR ranges. In project network policies, explicit `Deny` rules take absolute precedence over `Allow` rules.

**Note:** In GDC, as soon as a workload is selected by any project network policy (whether it contains `Allow` or `Deny` rules), the workload enters a default-deny mode for that direction (ingress or egress). Since ingress does not have default platform base rules, applying a project network policy with only `Deny` rules causes the workload to enter default-deny mode and block **all** ingress traffic: the specified traffic is blocked by the `Deny` rules, and the rest is blocked by the default-deny behavior. If you want to use `Deny` rules to block specific ingress traffic while keeping other traffic open, you **must** also configure `Allow` rules to explicitly permit the traffic you want to preserve.

## Before you begin

To configure explicit deny project network policies, you must have the following:

  * The necessary identity and access roles. To manage policies for a specific project, you need the `project-networkpolicy-admin` role. For multi-zone environments where you need to manage policies that span across all zones, you need the `global-project-networkpolicy-admin` role. For more information, see [Prepare predefined roles and access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview#prepare-predefined-roles-and-access).
  * An existing project. For more information, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project).
  * For egress network policies, you must also disable [data exfiltration protection](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/data-exfiltration) for the project.



## Create a deny network policy

You can define ingress or egress deny policies to restrict communication.

### Create an ingress deny policy

To block incoming traffic from workloads in another project within your organization, you must configure an ingress policy with the `Deny` action.

The following policy blocks workloads in the `PROJECT_1` project from receiving connections from workloads in the `PROJECT_2` project.

Apply the policy:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT_1
      name: deny-ingress-from-PROJECT_2
    spec:
      policyType: Ingress
      subject:
        subjectType: UserWorkload
      ingress:
      - action: Deny
        from:
        - projectSelector:
            projects:
              matchNames:
              - PROJECT_2
    EOF
    

Replace the following:

  * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers).
  * `PROJECT_1`: the namespace of the project where you want to apply the policy.
  * `PROJECT_2`: the namespace of the project from which traffic should be denied.



### Create an egress deny policy

To block outgoing traffic from workloads in your project to workloads in another project within your organization, you must configure an egress policy with the `Deny` action.

The following policy blocks workloads in the `PROJECT_1` project from initiating connections to workloads in the `PROJECT_2` project.

Apply the policy:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT_1
      name: deny-egress-to-PROJECT_2
    spec:
      policyType: Egress
      subject:
        subjectType: UserWorkload
      egress:
      - action: Deny
        to:
        - projectSelector:
            projects:
              matchNames:
              - PROJECT_2
    EOF
    

Replace the following:

  * `GLOBAL_API_SERVER`: the global API server's kubeconfig path.
  * `PROJECT_1`: the namespace of the project where you want to apply the policy.
  * `PROJECT_2`: the namespace of the project to which traffic should be denied.



## Key constraints and safety features

To prevent accidental misconfiguration and protect platform traffic, project network policies enforce the following safety checks for deny rules:

  * **Egress safety rules** : For egress policies, the system automatically injects rules to exclude system and non-project namespaces. This ensures egress `Deny` rules don't accidentally block communication to essential platform infrastructure services (such as the API server or DNS).
  * **Required peer specification** : Ingress `Deny` rules must explicitly specify a source peer in the `from` field, and egress `Deny` rules must explicitly specify a destination peer in the `to` field. You cannot select all sources or destinations by leaving the peer field empty. Omitting the `from` or `to` block or leaving it empty is disallowed, and the policy will be rejected.
  * **IP block deny rules and infrastructure traffic** : If you use `ipBlocks` in egress `Deny` rules, safety rules can't be injected. Because `ipBlocks` rules can select cluster nodes (see [Target cluster nodes using IP blocks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview#node-selection-considerations)), broad egress `Deny` rules might block infrastructure traffic. Carefully configure IP blocks for egress `Deny` policies.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
