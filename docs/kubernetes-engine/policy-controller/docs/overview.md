---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview/
title: Policy Controller overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:48.236159+00:00
---

# Policy Controller overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Policy Controller overview Stay organized with collections  Save and categorize content based on your preferences. 

This page explains what Policy Controller is and how you can use it to help ensure your Kubernetes clusters and workloads are running in a secure and compliant manner.

This page is for IT administrators, Operators, and Security specialists who define IT solutions and system architecture in accordance with company strategy, and ensure that all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to audit or enforce. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Policy Controller enables the application and enforcement of programmable policies for your Kubernetes clusters. These policies act as **guardrails** and can help with best practices, security, and compliance management of your clusters and fleet. Based on the open source [Open Policy Agent Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/docs/) project, Policy Controller is fully integrated with Google Cloud, includes a built-in dashboard, for observability, and comes with a full library of prebuilt policies for common security and compliance controls.

## Policy Controller benefits

  * **Integrated with Google Cloud** : Platform admins can [install Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller) by using the Google Cloud console, by using Terraform, or by using Google Cloud CLI on any cluster connected to your fleet. Policy Controller works with other Google Cloud services like [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview), [metrics](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-metrics), and Cloud Monitoring.
  * **Supports multiple enforcement points** : In addition to both audit and admission control for your cluster, Policy Controller can optionally enable a [shift-left approach](https://docs.cloud.google.com/architecture/devops/devops-tech-shifting-left-on-security) to [analyse and catch non-compliant changes](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/tutorials/app-policy-validation-ci-pipeline) prior to application.
  * **Prebuilt policy bundles** : Policy Controller comes with a full library of prebuilt policies for common security and compliance controls. These include both [Policy bundles](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/concepts/policy-controller-bundles) and the [constraint template library](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library).
  * **Supports custom policies** : If policy customization is required beyond what is available using the [constraint template library](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library), Policy Controller additionally supports the development of custom [_constraint templates_](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/write-custom-constraint-templates).
  * **Built-in observability** : Policy Controller includes a Google Cloud console [dashboard](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-status), providing an overview for the state of all the policies applied to your fleet (including unregistered clusters). From the dashboard, view compliance and enforcement status to help you troubleshoot, and get opinionated recommendations to resolve policy violations.



## Policy bundles

You can use policy bundles to apply a number of constraints that are grouped under a specific Kubernetes standard, security, or compliance theme. For example, you can use the following policy bundles:

  * [Enforce many of the same requirements as PodSecurityPolicies](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-constraints-to-enforce-pod-security), but with the added ability to audit your configuration before enforcing it, ensuring any policy changes aren't disruptive to running workloads.
  * [Use constraints compatible with Cloud Service Mesh](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-asm-security-policy) to audit the compliance of your mesh security vulnerabilities and best practices.
  * [Apply general best practices to your cluster resources](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-policy-essentials-v2022) to help strengthen your security posture.



[Policy Controller bundles overview ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/concepts/policy-controller-bundles) provides more details and a list of currently available policy bundles.

## Constraints

Policy Controller enforces your clusters' compliance using objects called _constraints_. You can think of constraints as the "building blocks" of policy. Each constraint defines a specific change to the Kubernetes API that is allowed or disallowed on the cluster it's applied to. You can set policies to either actively block non-compliant API requests or [audit](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/auditing-constraints) the configuration of your clusters and report violations. In either case, you can view warning messages with details on what violation occurred on a cluster. With that information, you can remediate problems. For example, you can use the following individual constraints:

  * [Require each namespace to have at least one label](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library#k8srequiredlabels). This constraint can be used to ensure accurate tracking of resource consumption when using GKE Usage Metering, for example.
  * [Restrict the repositories a given container image can be pulled from](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library#k8sallowedrepos). This constraint ensures any attempt to pull containers from unknown sources is denied, protecting your clusters from running potentially malicious software.
  * [Control whether or not a container can run in privileged mode](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library#k8spspprivilegedcontainer). This constraint controls the ability of any container to enable privileged mode, which gives you control over which containers (if any) can run with unrestricted policy.



These are just a few of the constraints provided in the [constraint template library](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library) included with Policy Controller. This library contains numerous policies that you can use to help enforce best practices and limit risk. If you require more customization beyond what is available in the constraint template library, you can also create custom [constraint templates](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/write-custom-constraint-templates).

Constraints can be applied directly to your clusters using the Kubernetes API, or distributed to a set of clusters from a centralized source, like a Git repository, by using [ Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/config-sync-overview).

## What's next

  * [Install Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller).
  * [Learn about policy bundles](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/concepts/policy-controller-bundles).
  * [Apply policy bundles](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/apply-policy-bundles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
