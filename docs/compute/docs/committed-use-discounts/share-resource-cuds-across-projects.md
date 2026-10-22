---
url: https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects/
title: Share resource-based CUDs across projects \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:24:34.952455+00:00
---

# Share resource-based CUDs across projects  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Share resource-based CUDs across projects Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how Google Cloud shares [resource-based committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) across projects in your Cloud Billing account.

_CUD sharing_ pools your resource-based committed use discounts (CUDs) at the Cloud Billing account level so that a commitment purchased in one project can cover eligible resource usage in any other project linked to the same account. With CUD sharing enabled, you maximize your savings and reduce the overhead of managing discounts on a per-project basis.

## How CUD sharing works

CUD sharing is the default operating model for most Cloud Billing accounts. When CUD sharing is enabled, Google Cloud automatically aggregates CUDs from all active resource-based commitments within a Cloud Billing account and applies the resulting discounts to eligible resource usage across all associated projects.

For example, you purchase two resource-based commitments for 80 vCPUs each (a total of 160 vCPUs) in `Project A`, but your total monthly usage reaches 200 vCPUs. Suppose that these 200 vCPUs are distributed across multiple projects in your Cloud Billing account. Because CUD sharing is enabled for the account, you receive the applicable resource-based CUDs for 160 of those 200 vCPUs, regardless of which projects run the compute instances. The additional 40 vCPUs are billed at standard on-demand rates. If you prefer to keep a project's CUDs strictly isolated to the purchasing project, then you can disable CUD sharing for your Cloud Billing account at any time.

**Note:** CUDs are credited to custom machine types before predefined machine types. There is a surcharge for custom machine types. The discount is distributed proportionally across all projects under the same Cloud Billing account. For more information, see [Proportional attribution](https://docs.cloud.google.com/docs/cuds-attribution#type-proportional).

### CUD scope and default configuration

You enable or disable CUD sharing by changing the _CUD scope_ in your Cloud Billing account. Resource-based CUDs have two scope options:

  * **Project** : Resource-based CUDs from a commitment apply only within the project in which you purchased the commitment.
  * **Billing account** : Resource-based CUDs from commitments apply across all projects linked to the Cloud Billing account.



The default CUD scope for all new billing accounts is **Billing account** (CUD sharing enabled). On June 16, 2026, the default CUD scope changed from **Project** to **Billing account** for most billing accounts. To prevent any disruption to your active billing configurations with this change, Google Cloud auto-configured your Cloud Billing account's CUD scope in the following way, depending on the account's creation date and the active commitments:

  * **Cloud Billing accounts created on or after June 16, 2026** : The scope is **Billing account** (CUD sharing enabled) by default.
  * **Cloud Billing accounts created before June 16, 2026** : 
    * If the Cloud Billing account had **no active resource-based commitments** on June 16, 2026, then the CUD scope was changed to **Billing account** (CUD sharing enabled) on that date.
    * If the Cloud Billing account had **any active resource-based commitments** on June 16, 2026, then Google Cloud preserved the existing CUD scope (either **Project** or **Billing account**) that was in place on that date.



You can manually enable or disable CUD sharing at any time by changing your CUD scope configuration. For instructions, see Enable CUD sharing or Disable CUD sharing.

After you change your CUD scope, the time it takes for the change to take effect depends on your selection:

  * **Billing account (enabling CUD sharing)** : The change takes effect at 12:00 AM US and Canadian Pacific Time the following day.
  * **Project (disabling CUD sharing)** : The change takes effect within a few moments.



### Attribution for shared CUDs

Attribution refers to how Google Cloud allocates your CUDs across projects when CUD sharing is enabled. These allocations are reflected in Cloud Billing cost management interfaces, such as the [usage cost export](https://docs.cloud.google.com/docs/cuds-attribution#view-attribution-in-exported-data) or the [Google Cloud console](https://docs.cloud.google.com/docs/cuds-attribution#view-attribution-in-reports).

For resource-based CUDs only, you can choose one of the following types of attribution:

  * [Proportional attribution](https://docs.cloud.google.com/docs/cuds-attribution#type-proportional). Your CUDs are shared across projects based on each project's proportion of the total eligible usage. This is the default attribution type.
  * [Prioritized attribution](https://docs.cloud.google.com/docs/cuds-attribution#type-prioritized). You specify the order in which projects receive CUDs.

**Note:** Spend-based CUDs are inherently pooled at the Cloud Billing account level and always use proportional attribution. You don't have a separate CUD sharing configuration for spend-based commitments.

_Proportionally attributed_ commitments are applied to usage from projects based on each project's share of the total eligible usage. For example, suppose that `project A` consumes US$75 worth of usage and `project B` consumes US$25 worth of usage. In this scenario, `project A` gets covered by up to 75% of the available CUDs and `project B` gets covered by up to 25%.

_Prioritized attribution_ applies your commitments to usage based on the distribution settings that you specify. You can choose the projects, along with the amount of usage within each project, that get covered by the commitments. After your prioritized commitments are applied to eligible usage, any remaining unprioritized commitments are applied proportionally to the eligible usage in your remaining projects. The total amount of the allotments can't exceed the commitment amount purchased.

**Preview:** You can prioritize multiple projects by grouping them in a folder. Credits are applied proportionately across projects in the folder, based on their eligible usage. To request access to prioritized attribution with folders, [complete the interest form](https://forms.gle/9wkzFCAU4pkeVmcE6).

You can update attribution preferences anytime during the commitment's lifetime. However, any attribution preferences that you configure are applied only if CUD sharing is enabled. To choose proportional or prioritized attribution for your Compute Engine commitments, see [Choose attribution for resource-based commitments](https://docs.cloud.google.com/docs/cuds-attribution#choose-attribution-resource-based).

### Impact of changing a project's Cloud Billing account

If you move the project that is associated with a commitment to a different Cloud Billing account, then you continue to receive CUDs under the destination Cloud Billing account for the commitments associated with that project. However, the source account's attribution and CUD sharing settings no longer apply to the project. Instead, the project inherits the attribution and CUD sharing settings that apply to the destination account.

For example, suppose that you have CUD sharing enabled in the source account and disabled in the destination account. After you move your project, the projects in the source account no longer receive CUDs from resource-based commitments that are tied to the moved project. In the destination account, because CUD sharing is disabled, the resource-based CUDs are limited to the moved project.

For more information about changing the Cloud Billing account for a project, see [Change the billing account for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project).

## Limitations

  * If you have a shared reservation in a project and want usage from the shared projects to be eligible for shared CUDs from your commitment's Cloud Billing account, then you must share your reservation only with projects that are linked to the same Cloud Billing account. Otherwise, usage from those projects won't be eligible for shared CUDs and you might be charged the on-demand rates.

  * When CUD sharing is enabled for a Cloud Billing account, if any portion of a commitment remains unutilized within a given month, then the commitment fee for that remaining portion gets charged to the project where you purchased that commitment.




## Check whether CUD sharing is enabled

To check if CUD sharing is enabled for your Cloud Billing account, complete the following steps:

  1. In the Google Cloud console, go to the **CUD analysis** page.

[Go to CUD analysis](https://console.cloud.google.com/billing/commitments/analysis)

  2. At the prompt, choose the Cloud Billing account that you want to view. The **Committed use discount analysis** page appears.

  3. In the **Analyze** menu, select **Resource-based CUDs**. The settings **CUD scope & settings** button appears in the toolbar.

  4. Click settings **CUD scope & settings**.

  5. In the **Resource-based CUDs scope** section of the **CUD scope & settings** page that appears, you can review your current CUD scope configuration. The CUD scope can be one of the following:

     * **Project** : This selection indicates that CUD sharing isn't enabled for resource-based commitments. CUDs from a commitment apply to eligible usage only in the project where the commitment was purchased.

     * **Billing account** : This selection indicates that CUD sharing is enabled for resource-based commitments. CUDs from any resource-based commitment in the current Cloud Billing account are shared and applied to eligible usage across all projects that are associated with the Cloud Billing account.




## Enable CUD sharing

If CUD sharing isn't enabled on your Cloud Billing account, then you can enable CUD sharing by changing the CUD scope to **Billing account** in the Google Cloud console. After you change your CUD scope to **Billing account** , CUD sharing is enabled on all of the current and future projects that are associated with the Cloud Billing account.

CUD sharing works in conjunction with your attribution configuration. When CUD sharing is enabled, it defaults to using [_proportional attribution_](https://docs.cloud.google.com/docs/cuds-attribution#type-proportional) for your Compute Engine resource-based commitments. If CUD sharing is disabled on your Cloud Billing account and you plan to configure prioritized attribution, then Google recommends that you configure the prioritized attribution settings in the Google Cloud console before you enable CUD sharing. For more information, see [CUD sharing best practice for prioritized attribution](https://docs.cloud.google.com/docs/cuds-attribution#cud-sharing-best-practice-prioritized-attribution).

**Caution:** If you have a shared reservation in a project and want usage from the shared projects to be eligible for the current project's CUDs, then you must ensure that you share your reservation only with projects that are linked to the same Cloud Billing account. Otherwise, your usage from those projects won't be eligible for the shared CUDs and you might be charged the on-demand rates. 

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

You need specific permissions on the _Cloud Billing account_ to access Cloud Billing information. To update the CUD scope and enable CUD sharing, you need a role that includes the following permission on the Cloud Billing account:

  * `billing.subscriptions.update` on the Cloud Billing account



To gain this permission using a predefined role, ask your [ billing administrator](https://docs.cloud.google.com/billing/docs/how-to/find-billing-account-administrator) to grant you the [ Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) role on the Cloud Billing account.

To enable CUD sharing, complete the following steps:

  1. In the Google Cloud console, go to the **CUD analysis** page.

[Go to CUD analysis](https://console.cloud.google.com/billing/commitments/analysis)

  2. At the prompt, choose the Cloud Billing account for which you want to enable CUD sharing.

  3. In the toolbar of the **CUD analysis** page, click settings **CUD scope & settings**. The **CUD scope & settings** page appears.

  4. In the **Resource-based CUDs scope** section, select **Billing account**.

  5. To save your updated CUD scope and enable CUD sharing, click **Save**.

After you save the changes, the updated CUD scope takes effect at 12:00 AM US and Canadian Pacific Time the following day. You can verify that the CUD scope is correctly set.




## Disable CUD sharing

**Caution:** If you have a shared reservation in a project and want usage from the shared projects to be eligible for the current project's CUDs, then don't disable CUD sharing. Also, make sure that you share your reservation only with projects that are linked to the same Cloud Billing account. 

To disable CUD sharing, complete the following steps:

  1. In the Google Cloud console, go to the **CUD analysis** page.

[Go to CUD analysis](https://console.cloud.google.com/billing/commitments/analysis)

  2. At the prompt, choose the Cloud Billing account for which you want to disable CUD sharing.

  3. In the toolbar of the **CUD analysis** page, click settings **CUD scope & settings**. The **CUD scope & settings** page appears.

  4. In the **Resource-based CUDs scope** section, select **Project**.

  5. To save your updated CUD scope and disable CUD sharing, click **Save**.

After you save the changes, the updated CUD scope takes effect within a few moments. You can verify that the CUD scope is correctly set.




## What's next

  * Learn about [attribution for resource-based commitments](https://docs.cloud.google.com/docs/cuds-attribution).
  * Learn how to [analyze the effectiveness of your CUDs](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
