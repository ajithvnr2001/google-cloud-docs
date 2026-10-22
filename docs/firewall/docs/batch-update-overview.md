---
url: https://docs.cloud.google.com/firewall/docs/batch-update-overview/
title: Overview \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:37.470855+00:00
---

# Overview  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/batch-update-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

You can use a single request from the [Google Cloud CLI](https://docs.cloud.google.com/sdk/install) or the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies#get) to batch update all the firewall policy rules for hierarchical and network firewall policies. This ensures the integrity of the firewall policy's rule set. Using the batch updates, Cloud Next Generation Firewall (Cloud NGFW) provides an efficient and manageable way for you to handle firewall policy rule updates in your cloud environments.

For more information about how to configure batch update, see [Configure batch updates to firewall policy rules](https://docs.cloud.google.com/firewall/docs/configure-batch-updates).

## Permissions

Make sure that you have the following permissions to batch update the firewall policy rules.

  * The `compute.firewallPolicies.get` permission to export the hierarchical firewall policy rules.
  * The `compute.firewallPolicies.update` permission to import the hierarchical firewall policy rules.
  * The `compute.firewallPolicies.get` permission to export the network firewall policy rules.
  * The `compute.regionFirewallPolicies.get` permission to export regional network firewall policy rules.
  * The `compute.firewallPolicies.update` permission to import the network firewall policy rules.
  * The `compute.regionFirewallPolicies.update` permission to import the regional network firewall policy rules.



For more information about the roles and permissions, see [Compute Engine roles](https://docs.cloud.google.com/iam/docs/roles-permissions/compute).

## Specification

Batch update of firewall policy rules has the following specifications:

  * The update process is atomic. This means that if an error occurs while the rules are being imported, all changes are rolled back, and your firewall policy rule remains in its previous state.

  * When you use the REST APIs to update firewall policy rules, the REST APIs require a fingerprint for optimistic locking. For more information, see [Optimistic concurrency control](https://en.wikipedia.org/wiki/Optimistic_concurrency_control). To get the latest fingerprint, we recommend that you first make a `get` request to the firewall policy. A `get` request to the firewall policy gets the most recent version of the policy, which helps ensure that updates are based on the most recent version of the policy. This helps prevent conflicts if concurrent modifications are made to the policy.

  * When you use the REST API `patch` method, you can replace all existing rules by providing a completely new list in your request.

  * If a firewall policy `patch` operation is in progress, you can't modify rules using methods such as [`addRule`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/addRule), [`patchRule`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/patchRule), [`removeRule`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/removeRule), or [`cloneRules`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/cloneRules). This helps ensure that there are no conflicting modifications during the patch operation.




## Configure batch update

The batch update process involves three key steps:

  1. **Export** : export your current firewall policy rules.
  2. **Modify** : make the required batch updates to the exported firewall policy rules.
  3. **Import** : import the modified file back into the firewall policy rules.



To configure the batch update to firewall policy rules, do the following:

  1. Export your firewall policy rules. For more information, see [Export firewall policy rule](https://docs.cloud.google.com/firewall/docs/configure-batch-updates#export-rules).

  2. Modify the exported file. You can perform the following steps to update the file:

     * **Add new rules** : make sure that each new rule adheres to the [`FirewallPolicyRule.yaml`](https://json-schema.org/draft-06/schema) schema.

     * **Modify existing rules** : change the attributes of the rules that you want to update. These attributes include the action, description, and match conditions against which incoming traffic is evaluated.

     * **Delete rules** : remove the entries for the firewall policy rules you want to delete.

For more information, see [Modify firewall policy rules](https://docs.cloud.google.com/firewall/docs/configure-batch-updates#modify-firewall-rules).

  3. Import the rules back into your firewall policy. For more information, see [Import firewall policy rules](https://docs.cloud.google.com/firewall/docs/configure-batch-updates#import-rules).




## What's next

  * For an introduction to firewall rules, see [Firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details).
  * To learn how to configure batch updates to firewall policy rules, see [Configure batch updates for firewall policies](https://docs.cloud.google.com/firewall/docs/configure-batch-updates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
