---
url: https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies/
title: Global VM extension policies \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:40.095278+00:00
---

# Global VM extension policies  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Global VM extension policies Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of global policies in VM Extension Manager. You can use global extension policies to manage extensions across multiple zones and regions within a project. When you apply a global policy, VM Extension Manager ensures that VMs in any region or zone that match the policy criteria have the specified extensions installed and running.

For more information, see [About VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager).

The following diagram illustrates how you can use a global extension policy to apply extensions to VMs across different zones and regions in your project:

![VM Extension Manager architecture diagram showing a global policy being
applied to VMs across zones and
regions.](https://docs.cloud.google.com/static/compute/images/vm-extensions/vm-ext-manager-global-arch.svg)

As shown in the preceding diagram, you can define a global extension policy at the project level. VM Extension Manager applies this policy to all VMs that match your selection criteria. For example, you can select VMs with the label `env=prod` across all of the zones and regions in the project. In this case, VM Extension Manager applies the extensions that you specify, such as Ops Agent and Extension for SAP, to only these VMs.

## Rollout plans for global policies

Global policies use rollout plans to manage the deployment of extensions across zones and regions. A rollout plan lets you control the deployment of extensions, which helps to minimize the risk of widespread issues. By using a rollout plan, you can define the order and timing of updates to ensure a gradual and controlled rollout.

When you create or update a global policy, you can specify one of the following rollout plans:

  * **Slow rollout**. This rollout deploys extensions gradually across different zones over a period of time. The default period for this rollout is five days. This approach is recommended because it lets you identify and address potential issues in earlier rollouts before they impact your entire fleet.
  * **Fast rollout**. This rollout deploys extensions to all targeted VMs across all zones and regions immediately. This approach is useful for situations where you need to deploy an extension or a patch quickly in non-production environments.



You can also define custom rollout plans to specify the waves of deployment based on zones or regions and the time to wait between waves. For more information, see the [`rolloutPlans.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/rolloutPlans/insert).

## Rollout conflict behavior

When you create or update a global extension policy, a conflict might occur in the following situations:

  * **When creating a global policy**. A conflict in policy name occurs if a zonal policy with the same name as the global policy already exists in a zone.
  * **When updating a global policy**. A conflict in policy content occurs if an existing zonal policy was modified independently of the global policy rollout. For example, if you modify a zonal policy using a zonal API call, and a subsequent global policy rollout attempts to modify that same zonal policy, then a conflict occurs.



To help you avoid these conflicts, you can specify a conflict behavior for the rollout. This setting determines whether the global policy should overwrite conflicting zonal policies during a rollout. You can specify one of the following behaviors:

  * **Don't overwrite (default)**. If you don't specify a conflict behavior, the global policy rollout does not overwrite conflicting zonal policies. The zonal policy's configuration takes precedence in that zone.
  * **Overwrite**. If you set the conflict behavior to `overwrite`, the global overwrites conflicting zonal policies, and the global policy's configuration is applied in that zone.



Rollout conflicts and policy priority are distinct features that work independently. For more information about policy priority, see [Policy priority and conflict resolution](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#policy-priority-resolution).

For more information about rollout conflict, see the `conflictBehavior` parameter in the [`globalVmExtensionPolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/globalVmExtensionPolicies/insert).

## Retry a rollout

When you update or delete a global extension policy, VM Extension Manager starts a new rollout to apply the changes according to the rollout plan. If a rollout is interrupted, or if new zones are added, you can retry the operation by starting a new rollout for the same policy.

### Retry an update policy rollout

The following list describes scenarios where you might need to retry an update policy rollout:

  * **New zones added**. If new Google Cloud zones become available after you roll out a global policy, VM Extension Manager does not automatically apply existing policies to the VMs in the new zone. You can retry the update rollout to apply the extension policy to VMs in the new zones.
  * **Revert zonal policy changes**. If zonal policies were modified independently—for example, by using a zonal API call to modify a zonal policy—you can retry an update rollout with `conflictBehavior` set to `overwrite`. This setting re-applies the global policy's configuration and overwrites the zonal policy changes.
  * **Interrupted rollout**. If a previous rollout fails before completing, you can start a new rollout to retry the update.
  * **Accelerate a rollout**. If an ongoing rollout progresses too slowly, you can start a new rollout by using a `FAST_ROLLOUT` plan or a custom rollout plan to accelerate the update process.



For more information, see the `retryUuid` parameter in the [`globalVmExtensionPolicies.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/globalVmExtensionPolicies/update).

When retrying a rollout, you must provide a universally unique identifier (UUID) to identify the retry request. You can use any UUID generator to create one. The UUID must use the 32-character hexadecimal format, for example, `a1a2a3a4-b1b2-c1c2-d1d2-d3d4d5d6d7d8`.

### Retrying a delete policy rollout

The following list describes scenarios where you might need to retry a rollout to delete a policy:

  * **Interrupted rollout**. If a previous rollout to delete a policy was interrupted or did not complete successfully, you can start a new rollout to retry the delete operation.
  * **Accelerate a rollout**. If an ongoing delete rollout is progressing too slowly, you can start a new rollout by using a `FAST_ROLLOUT` plan or a custom rollout plan to accelerate the deletion process.



For more information, see the `retryUuid` parameter in the [`globalVmExtensionPolicies.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/globalVmExtensionPolicies/delete).

## What's next

To learn more about managing extensions, see the following resources:

  * [Install VM extensions by creating extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy)
  * [Manage VM extensions by using extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
