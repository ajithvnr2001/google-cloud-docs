---
url: https://docs.cloud.google.com/app-lifecycle-manager/delete-resources/
title: Delete resources \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:01.706298+00:00
---

# Delete resources  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/delete-resources/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  Delete resources Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide describes how to delete App Lifecycle Manager resources. App Lifecycle Manager ensures data integrity by blocking resource deletions when dependent resources exist.

A dependent resource has a reference to the resource you want to delete. For example, a unit is dependent on a unit kind. You cannot delete a unit kind if a unit references it.

## App Lifecycle Manager resource dependency

This table describes the dependency relationships between App Lifecycle Manager resources. The resource in the header column can only be deleted if there are no resources from the header row that reference that resource instance. For example, a unit kind resource cannot be deleted if a unit or release is referencing the unit kind.

**Resource type** |  **Dependent types** |  **Unit kind** |  **Unit** |  **Unit operation** |  **Release** |  **Rollout Kind** |  **Rollout** |  **Tenant** |  **App offering** |  **Notes**  
---|---|---|---|---|---|---|---|---|---|---  
**Unit Kind** |  |  |  X |  |  X |  |  |  |  |   
**Unit** |  |  X |  X |  |  X |  |  |  X |  |   
**Unit Operation** |  |  |  X |  |  |  |  X |  |  |   
**Release** |  |  X |  X |  |  |  |  |  |  |   
**Rollout Kind** |  |  |  |  |  |  |  X |  |  |   
**Rollout** |  |  |  |  X |  |  |  |  |  |   
**Tenant** |  |  |  X |  |  |  |  |  |  |   
**App offering** |  |  X |  |  |  |  |  |  X |  |   
**Note:** Unit operations are an exception. App Lifecycle Manager automatically deletes unit operations when you delete their associated unit.

## Before you begin

You should understand App Lifecycle Manager resource dependencies before you attempt to delete App Lifecycle Manager resources. A resource cannot exist without its dependencies.

## Delete an App offering

You cannot delete an App offering if any dependent unit kinds or tenants reference it.

To delete an App offering:

  1. Go to **App Lifecycle Manager** > **App offerings**.

[Go to App offerings](https://console.cloud.google.com/saas/saasOfferings)

  2. In the **Name** column, select the App offering you want to delete.

  3. Delete dependent unit kind resources. You can see an App offering's dependent unit kind resources under the **Unit kinds** tab on the **App offering details** page.

For more information about deleting App Lifecycle Manager resources, see delete Unit kinds.

  4. On the **App offering details** page, click delete**Delete**.

You've successfully deleted an App offering.




## Delete a unit kind

You must delete any dependent _unit_ and _release_ resources before you delete a _unit kind_.

To delete a unit kind:

  1. Go to **App Lifecycle Manager** > **Unit kinds**.

[Go to Unit kinds](https://console.cloud.google.com/saas/unitKinds)

  2. In the **Name** column, select the unit kind you want to delete.

  3. On the **Unit kind details** page, click delete**Delete**. A **Delete unit kind** dialog appears.

  4. Set the **Default release** property of the unit kind to **No default release**.

  5. Type the name of the unit kind you want to delete into the dialog.

  6. Click **Delete** to delete the unit kind.

You've successfully deleted a unit kind resource.




## Delete a unit

You must delete any dependent _unit_ resources before you delete a unit.

To delete a unit:

  1. Go to **App Lifecycle Manager** > **Units**.

[Go to Units](https://console.cloud.google.com/saas/units)

  2. In the **Name** column, select the unit you want to delete.

  3. Delete dependent unit resources. You can see a unit's dependent resources under the **Dependencies** tab on the **Unit details** page.

  4. On the **Unit details** page, click delete**Delete**. A **Delete unit** dialog appears.

  5. Type the name of the unit you want to delete into the dialog.

  6. Click **Delete** to delete the unit.

You've successfully deleted a unit resource.




### Delete a unit operation

App Lifecycle Manager automatically deletes unit operations when you delete their associated unit. You cannot delete a unit operation if it's in progress.

## Delete a release

You cannot delete a _release_ if:

  * _Provisioned units_ reference the release
  * The release is set as the default release of a _unit kind_ resource



You must delete any dependent _unit_ resources before you delete a release.

To delete a release:

  1. Go to **App Lifecycle Manager** > **Releases**.

[Go to Releases](https://console.cloud.google.com/saas/releases)

  2. In the **Name** column, select the release you want to delete.

  3. Delete all dependent units. You can see a release's dependent units under the **Units** tab on the **Release details** page. For information about deleting units, see delete a Unit.

  4. Unset the default release field from any unit kinds that reference this release.

  5. On the **Release details** page, click delete**Delete**. A **Delete release** dialog appears.

  6. Type the name of the release you want to delete into the dialog.

  7. Click **Delete** to delete the release.

You've successfully deleted a release resource.




## Delete a rollout kind

You cannot delete a _rollout kind_ if it's referenced by any _rollout_ resources.

To delete a rollout kind:

  1. Go to **App Lifecycle Manager** > **Rollout kinds**.

[Go to Rollout kinds](https://console.cloud.google.com/saas/rolloutKinds)

  2. In the **Name** column, select the rollout kind you want to delete.

  3. Delete all dependent rollouts. You can see a rollout kind's dependent rollout resources under the **Rollouts** tab on the **Rollout kind details** page. For information about deleting rollouts, see delete a Rollout.

  4. On the **Rollout details** page, click delete**Delete**. A **Delete rollout kind** dialog appears.

  5. Type the name of the rollout kind you want to delete into the dialog.

  6. Click **Delete** to delete the rollout kind.

You've successfully deleted a rollout kind resource.




## Delete a rollout

You cannot delete a rollout if it's running. You must stop a running rollout before you can delete it. When you delete a rollout, App Lifecycle Manager deletes all sub-rollouts created by the global root rollout.

To delete a rollout:

  1. Go to **App Lifecycle Manager** > **Rollouts**.

[Go to Rollouts](https://console.cloud.google.com/saas/rollouts)

  2. In the **Name** column, select the rollout you want to delete.

  3. Delete any dependent unit operations resources. For more information about deleting unit operations, see Delete a unit operation.

  4. On the **Rollout details** page, click delete**Delete**. A **Delete rollout** dialog appears.

  5. Type the name of the rollout you want to delete into the dialog.

  6. Click **Delete** to delete the rollout.

You've successfully deleted a rollout resource.




## Delete a tenant

You cannot delete a tenant if any units (provisioned or unprovisioned) reference it.

To delete a tenant:

  1. Go to **App Lifecycle Manager** > **Tenants**.

[Go to Tenants](https://console.cloud.google.com/saas/tenants)

  2. In the **Name** column, select the tenant you want to delete.

  3. Disassociate any units from the tenant. For information about associating units with tenants, see [Associate a unit with a tenant](https://docs.cloud.google.com/app-lifecycle-manager/create-tenants#associate_a_unit_with_a_tenant).

  4. On the **Tenant details** page, click delete**Delete**. A **Delete tenant** dialog appears.

  5. Type the name of the tenant you want to delete into the dialog.

  6. Click **Delete** to delete the tenant.

You've successfully deleted a tenant resource.




## What's next

  * Learn more about [App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/overview).
  * Understand how to [model and package App Lifecycle Manager resources](https://docs.cloud.google.com/app-lifecycle-manager/model-saas-offering).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
