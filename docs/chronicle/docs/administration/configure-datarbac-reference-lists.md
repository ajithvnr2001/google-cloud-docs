---
url: https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-reference-lists/
title: Configure access to reference lists \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:42.047793+00:00
---

# Configure access to reference lists  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-reference-lists/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure access to reference lists

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Caution:** Reference lists are being [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) and replaced by [data tables](https://docs.cloud.google.com/chronicle/docs/investigation/data-tables). All existing reference lists will be automatically migrated to data tables. You can continue to use your existing reference lists as they get migrated. In July 2027, the legacy reference list functionality will be fully retired from the Google SecOps platform and all data can be accessed through the data table interface. 

This page describes how _data role-based access control_ (_data RBAC_) administrators and users can assign scopes to reference lists.

A reference list is a list of values (for example, IP addresses) that are used for matching and filtering data in UDM Search and detection rules. By assigning scopes to a reference list, you can control which users and resources (for example, rules and UDM search instances) can access and utilize it.

To understand how data RBAC works, see [Overview of Data RBAC](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview).

## Add scopes to reference list

To add scopes to a reference list, you must have access to all the scopes that you intend to add. You cannot add scopes that you don't have access to.

Data RBAC impacts reference lists in the following ways:

  * **Data RBAC is enabled _before_ assigning scopes to reference lists:** all existing reference lists are automatically assigned global scope. Assign scopes to each reference list according to your data access control requirement.

  * **Data RBAC is enabled _after_ assigning scopes to reference lists**: scoped reference lists operate on ingested data according to their defined scopes, even before data RBAC is enabled.




A scoped user and a global user have different access permissions, with the following variation:

  * A scoped user can create a scoped reference list with all or a subset of scopes that are assigned to them.

  * A global user can create either an unscoped reference list (a reference list that all the users can use) or a scoped reference list.




To add scopes to a reference list, do the following:

  1. [Log in to Google Security Operations](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui).

  2. Click **Detection** > **Lists**.

  3. In the **List manager** window, select the list that you want to add scopes to.

  4. In the **Details** tab, in the **Scope assignment** menu, select all the scopes that the reference list must have access to.

  5. Click **Save edits**.




The scopes are added to the reference list.

## Update scopes in a reference list

To update the scopes in a reference list, you must have access to all the data scopes that you intend to add to the reference list. You cannot add scopes that you don't have access to.

The following considerations apply when updating a reference list:

  * Removing scopes from a reference list is allowed only if all the existing rules that use the reference list stay functional with the change.

For example, an update for a reference list from scopes A and B to scope A is not allowed if a rule with scope B uses the reference list. Similarly, an update for a reference list from being unscoped to scope A is not allowed if a rule with scope B uses the reference list.

  * A scoped user can remove a scope from a reference list which can cause another scoped user to lose access to the reference list.

For example, a user with scopes A and B can remove scope B from a reference list with scopes A and B. After this change, the user can still use the reference list, but another user with only scope B can no longer view or access the reference list.

  * Updating scopes to add more scopes can cause some users to lose their edit access to the reference list.

For example, a user with scopes A and B can add scope B to a reference list that has scope A. After this change, the user can still edit the reference list, but another user with only scope A is no longer able to edit the reference list.




To update the scopes in a reference list, do the following:

  1. [Log in to Google Security Operations](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui).

  2. Click **Detection** > **Lists**.

  3. In the **List manager** window, select the list that you want to add scopes to.

  4. In the **Details** tab, in the **Scope assignment** menu, select all the scopes that the reference list should have access to. Deselect the scopes that the reference list shouldn't have access to.

  5. Click **Save edits**.




The scope assignment of the reference list is updated.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
