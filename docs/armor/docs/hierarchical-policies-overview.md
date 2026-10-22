---
url: https://docs.cloud.google.com/armor/docs/hierarchical-policies-overview/
title: Hierarchical security policies overview \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:30.389046+00:00
---

# Hierarchical security policies overview  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/hierarchical-policies-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Hierarchical security policies overview Stay organized with collections  Save and categorize content based on your preferences. 

Hierarchical security policies are a category of security policies that extend the reach of Google Cloud Armor web application firewall (WAF) and DDoS protection beyond individual projects. They are attached at the organization, folder, or project level. These differ from service-level security policies, which are attached directly to backend services or backend buckets.

When you configure a hierarchical security policy at the organization or folder level, projects at lower levels of the hierarchy inherit that security policy. This inheritance lets you set up security policy rules that you want to apply to all or several projects within your organization. This allows for centralized and consistent security enforcement across your Google Cloud environment.

This page explains how hierarchical security policies differ from service-level security policies. Before you proceed, read the [security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-overview) to make sure that you understand how security policies work. In addition, we recommend that you familiarize yourself with the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

## Use cases

In large organizations, managing security policies across numerous projects can be complex and time consuming. Hierarchical security policies offer the following advantages to help you address these challenges:

  * Centralized control: provide organization and folder-level administrators with the ability to define and enforce security policies across multiple projects.
  * Consistency: provide uniform security posture across the organization, reducing the risk of misconfigurations and security gaps.
  * Efficiency: streamline the deployment of security updates and mitigations, such as blocking specific IP address ranges or addressing critical vulnerabilities, across a large number of resources simultaneously.
  * Delegation: enable delegation of security responsibilities to different teams or departments by applying policies at appropriate levels of the hierarchy.



You can apply and combine these general principles to fit your organization's needs. Consider the following example use cases:

  * Organization-wide IP address blocking: you can block traffic from known malicious IP address ranges across all projects in your organization.
  * Geography-based restrictions: you can restrict traffic from specific geographic regions at the organization or folder level.
  * CVE mitigation: you can quickly deploy WAF rules to mitigate critical vulnerabilities across multiple projects.
  * Compliance enforcement: you can enforce adherence to regulatory requirements by applying consistent security policies across your organization.
  * Granular access control: you can grant specific IP address ranges or geographic regions access to all of the resources within a specific folder.



## Features

Hierarchical security policies support a subset of the features that service-level security policies support. The following table compares the Cloud Armor features that you can use with hierarchical security policies and service-level security policies:

| Service-level global backend security policy | Hierarchical backend security policy  
---|---|---  
Frontend type | 

  * Global external Application Load Balancer
  * Classic Application Load Balancer

| 

  * Global external Application Load Balancer
  * Classic Application Load Balancer

  
Attachment point (protected resource) | Backend service | Resource hierarchy nodes  
Rule actions | 

  * Allow
  * Deny
  * Redirect (`GOOGLE_RECAPTCHA` and `EXTERNAL_302`)
  * Throttle
  * Rate-based ban

| 

  * Allow
  * Deny
  * Redirect (only `EXTERNAL_302`)
  * Goto next

  
Client IP address |  |   
Client geography |  |   
Client ASN |  |   
Rate limiting |  |   
TLS fingerprinting (JA3 and JA4) |  |   
Bot management |  |  (only `EXTERNAL_302` and request decoration)  
HTTP filtering |  |   
Body filtering |  |   
WAF |  |   
Managed rules |  |   
Google Threat Intelligence |  |   
reCAPTCHA |  |   
Adaptive Protection |  |   
Address Groups |  |   
Org-level Address Groups |  |   
Security Command Center |  |   
Cloud Monitoring |  |   
Request logging |  |   
  
## How hierarchical security policies work

When you create a hierarchical security policy, you create it at the organization or folder level, and that resource has ownership over the hierarchical security policy. After you create a hierarchical security policy, your security policy rules aren't applied to any of your resources.

Next, you associate the hierarchical security policy with an organization, folder, or project, which can be the same as the resource that owns the policy. After you have associated a hierarchical security policy with a resource, it applies the security policy rules to the protected resources at and under that node in the resource hierarchy. To help you decide which resource to attach your hierarchical security policies to, see the following list of basic use cases for each resource:

  * **Organization** : consider organization-level hierarchical security policies as the default type of hierarchical security policy. These policies have broad Identity and Access Management (IAM) permissions, and they apply to all nodes under the organization. Specify these resources by using the `--organization` flag during association.
  * **Folder** : use these hierarchical security policies when you want to apply the same security policy rules across multiple projects but not across your entire organization. Specify these resources by using the `--folder` flag during association.
  * **Project** : use this type of hierarchical security policy when you need to apply the same security policy rules across all resources in a project, like applying an IP address denylist across several backend services. Specify these resources by using the `--project` flag during association.
  * **Service-level** : use service-level security policies when you need unique security policy rules that differ among each of your services. Each service-level security policy only applies its rules to the backend policy that it's attached to. Specify these resources by using the `--project-number` flag.



You can only use one of these flags per hierarchical security policy. You specify the rest of the flags, like `--name` or `--type`, just like you do when you configure a service-level security policy. See the following list for more information about how hierarchical security policies work:

  * When a hierarchical security policy is associated with a resource hierarchy node, all protected resources lower than that node in the hierarchy inherit the policy.
  * You can view the security policies that apply to each protected resource in a project, across all hierarchical security policies and service-level security policies. For more information, see [View all effective Cloud Armor rules for a protected resource](https://docs.cloud.google.com/armor/docs/hierarchical-policies-using#view-rules).
  * You can move hierarchical security policies from one resource hierarchy node to another. You might do this when you plan to reorganize your folder structure.
  * When you delete a resource hierarchy node, like a folder or a project, the hierarchical security policy attached to that node is only deleted if you _created_ it under that resource hierarchy node. 
    * If you created the security policy elsewhere and then moved it under the node, it isn't deleted.
    * To avoid accidental deletion of your hierarchical security policies, we recommend that you move any hierarchical security policies that you intend to keep to another resource hierarchy node before you delete the existing node.



### Rule evaluation order

Cloud Armor evaluates security policies in the following order:

  1. Organization-level hierarchical security policies
  2. Folder-level hierarchical security policies (beginning with the parent folder, then proceeding to each subfolder)
  3. Project-level hierarchical security policies
  4. Service-level security policies



This rule evaluation order means that you might have a hierarchical security policy with a low priority that is evaluated before a service-level security policy with a high priority. Think carefully about your existing high-priority service-level security policy rules, and consider what happens if Cloud Armor doesn't evaluate a request that is allowed or denied by a hierarchical security policy against them.

[ ![Cloud Armor hierarchical security policies rule evaluation.](https://docs.cloud.google.com/static/armor/images/ca-hp.svg)](https://docs.cloud.google.com/static/armor/images/ca-hp.svg) Cloud Armor hierarchical security policies rule evaluation (click to enlarge).

### The `goto_next` action

Cloud Armor has a rule action that is exclusive to hierarchical security policies: the `goto_next` action. When Cloud Armor applies this action, it stops evaluating rules within the current security policy and begins evaluating rules in the next security policy.

Consider an example in which you have a hierarchical security policy at the organization-level with many rules that you want to use to restrict requests across your entire organization. You want to let requests that come from a certain IP address range skip evaluating these organization-wide rules. Therefore, you create a top-priority rule that matches on that IP address range with the action `goto_next`. The requests from that IP address range are evaluated against this rule first, and because they meet the match condition, they aren't evaluated against any other rules in this organization-level hierarchical security policy.

In the same example, if you used an `allow` or `deny` action instead of the `goto_next` action, the request is allowed or denied as soon as the match condition is met. This hierarchical evaluation means that no additional security policies are evaluated against that request.

## Google Cloud Armor Enterprise enrollment and billing behavior

When you attach a hierarchical security policy, each of the projects that inherit the hierarchical security policy must be enrolled in Cloud Armor Enterprise. This includes all of the projects in an organization or folder with a hierarchical security policy that aren't explicitly excluded, and all projects with a hierarchical security policy attached directly to the project.

  * Projects that are linked to a Cloud Billing account with a subscription to Cloud Armor Enterprise Annual are automatically enrolled in Cloud Armor Enterprise Annual if they aren't already enrolled.
  * Without a Cloud Armor Enterprise Annual subscription, projects are automatically enrolled in Cloud Armor Enterprise Paygo when they inherit a hierarchical security policy. If you subscribe the billing account to Cloud Armor Enterprise Annual after your project was automatically enrolled in Cloud Armor Enterprise Paygo, the project isn't automatically enrolled to Annual. For more information about Cloud Armor Enterprise Paygo, see [Cloud Armor Standard versus Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview#standard_versus).
  * If you update a hierarchical security policy to exclude a project _after_ the project has been automatically enrolled in Cloud Armor Enterprise, the project isn't automatically unenrolled. To manually unenroll your project, see [Remove a project from Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-using#remove-project).
  * You can't remove a project from Cloud Armor Enterprise while it has any inherited hierarchical security policies.



Auto-enrollment can take up to the next business day to complete. During this time, your hierarchical security policies are effective and no Cloud Armor Enterprise costs are incurred. When your project is enrolled, audit logs are updated to reflect the project's Cloud Armor Enterprise status. You also see the new project tier in the Google Cloud console.

Projects are auto-enrolled only when at least one backend service for global external load balancers uses HTTP, HTTPS, HTTP2, H2C, or GRPC.

## Limitations

Hierarchical security policies have the following limitations:

  * Hierarchical security policies aren't available for projects that aren't within an organization.
  * For new or recently restored projects, it might take a few hours for any inherited security policies on the project to propagate.
  * For a project that has recently enabled the Compute Engine API, it might take a few hours for any inherited security policies on this project to propagate.
  * You can tune preconfigured WAF rules in hierarchical security policies that you own, but the owners of services that inherit a hierarchical security policy can't perform rule tuning.



## What's next

  * [Configure hierarchical security policies](https://docs.cloud.google.com/armor/docs/hierarchical-policies-using)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
