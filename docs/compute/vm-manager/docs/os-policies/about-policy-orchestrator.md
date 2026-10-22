---
url: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/about-policy-orchestrator/
title: About policy orchestrator \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:59.909221+00:00
---

# About policy orchestrator  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/about-policy-orchestrator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  About policy orchestrator Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the OS policy orchestrator feature in VM Manager and its capabilities for managing OS policies at scale across projects and zones.

To use this feature, you must be familiar with [OS policies and OS policy assignments](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies).

Policy orchestrator helps you to iteratively create, update, and delete OS policy assignments in your resources and minimizes errors. You can also monitor the overall rollout status of the OS policy assignments in your organization and folders. If policy assignments fail, you can edit or delete the policy orchestrator.

## Use cases

You can use policy orchestrator to perform these common tasks:

  * Apply policies across your organization
  * Automatically create policies in new projects and zones



### Apply policies across your organization

Use policy orchestrator to gradually apply OS policy changes across multiple projects and zones in your organization. The following example describes a typical use case of a policy orchestrator.

You want to apply OS policies to VMs in a few projects under Folder A in your organization. Consider two test projects, Project A and Project B, under Folder A. To apply the OS policies across these two projects, do the following:

  1. Create an OS policy orchestrator in Folder A and set the orchestrator scope to Project A and Project B.
  2. If the orchestration is successful, expand the orchestration scope by adding more projects in gradual, successive steps. You can also disable the scope filter completely to roll out changes to all projects under Folder A.



The following figure illustrates how OS policy orchestrator applies OS policies to your resources.

![OS policy orchestrator architecture.](https://docs.cloud.google.com/static/compute/images/manage-os/os_policy_orchestrator.png)

### Automatically create policies in new projects and zones

When Google makes new Google Cloud locations available or if you create or move Google Cloud projects in your organization, the policy orchestrator automatically discovers those changes and eventually enforces policies in new locations and projects. You can also define the scope of orchestration and apply changes to specific projects and resources.

## How OS policy orchestrator works

The policy orchestrator applies the OS policy to your resources iteratively. A new iteration starts every six hours. If a rollout finishes in less than six hours, the orchestrator waits six hours from the start of the previous iteration before starting the next iteration. If a rollout takes longer than six hours, the next iteration begins immediately after the current iteration finishes.

In each iteration, the policy orchestrator identifies resources in the orchestration scope and performs the requested action on those resources. Project owners can remove or modify policies created by the orchestrator, but the policy orchestrator replaces or updates those policies in the next iteration.

A policy orchestrator performs one of the following actions:

  * Create or update (upsert) an existing OS policy
  * Delete an OS policy



In addition to the action type, the policy orchestrator contains a policy ID and a policy payload. For each project-zone pair from the orchestration scope, policy orchestrator creates a resource that is specific to the policy payload and the given policy ID. To [delete OS policy assignments](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/use-policy-orchestrator#delete-assignments-orchestrator) using policy orchestrator, you must specify this policy ID.

## What's next?

  * Learn about the [prerequisites for using policy orchestrator](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites).
  * Learn how to [manage OS policy assignments using policy orchestrator](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/use-policy-orchestrator).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
