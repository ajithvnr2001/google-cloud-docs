---
url: https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-users/
title: Configure data RBAC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:03.672302+00:00
---

# Configure data RBAC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure data RBAC

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This page describes how _data role-based access control_ (_data RBAC_) administrators can configure data RBAC within Google Security Operations. Through the creation and assignment of data scopes, which are defined by labels, you can ensure that data is only accessible to authorized users.

Data RBAC relies on [IAM](https://docs.cloud.google.com/iam/docs/overview#how_cloud_iam_works) concepts including [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview), [custom roles](https://docs.cloud.google.com/iam/docs/roles-overview#custom), and [IAM conditions](https://docs.cloud.google.com/iam/docs/conditions-overview).

The following is a high-level overview of the configuration process:

  1. **Plan your implementation:** identify the different types of data you want to restrict user access to. Identify the different roles within your organization and determine the data access requirements for each role.

  2. **Optional: Create custom labels:** create custom labels (in addition to the [default labels](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview#access-control-with-scopes-labels)) to categorize your data.

  3. **Create data scopes:** define scopes by combining relevant labels.

  4. **Assign scopes to users:** assign scopes to user roles in IAM based on their responsibilities.

  5. **Enable data RBAC:** enable data RBAC to apply the scope assignments. You have the following two options to set up data RBAC:

     * **Enable data RBAC _before_ assigning scopes:** when data RBAC is enabled, rules, reference lists, and data tables don't have any scopes assigned. Only users with global access have access to the data. Scoped users don't have access to any data by default. This prevents unintended access and ensures a secure starting point. To grant access, define scopes and assign them to users, rules, and reference lists based on your requirement.

     * **Enable data RBAC _after_ assigning scopes:** setting up and assigning scopes in advance provides immediate data access to users when data RBAC is enabled. Additionally, since rules have scopes assigned, the generated detections are tagged with scopes. This allows users to see detections that were generated after the scope assignments.

**Note:** While rules and reference lists (in addition to IAM user assignments) support scope configuration prior to enabling data RBAC, pre-enablement scope assignment is not supported for other resources, such as data tables.**Important:** Before data RBAC is enabled, all users, regardless of assigned scopes, have global access and can view all data.



## Before you begin

  * To understand the core concepts of data RBAC, different access types, and the corresponding user roles, the working of labels and scopes, and the impact of data RBAC on Google SecOps features, see [Overview of Data RBAC](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview).

  * Onboard your Google SecOps instance. For more information, see [Onboarding or migrating a Google Security Operations instance](https://docs.cloud.google.com/chronicle/docs/onboard).

  * Make sure that you have the [required roles](https://docs.cloud.google.com/chronicle/docs/onboard#configure_data_access_control).




## Create and manage custom labels

Custom labels are metadata that you can add to the SIEM ingested Google SecOps data to categorize and organize it based on UDM-normalized values.

For example, consider you want to monitor network activity. You want to track Dynamic Host Configuration Protocol (DHCP) events from a specific IP address (10.0.0.1) that you suspect might be compromised.

To filter and identify these specific events, you can create a custom label with the name Suspicious DHCP Activity with the following query:

`metadata.event_type = "NETWORK_DHCP" AND principal.ip = "10.0.0.1"`

The custom label works in the following manner:

Google SecOps continuously ingests network logs and events into its UDM. When a DHCP event is ingested, Google SecOps checks if it matches the criteria of the custom label. If the `metadata.event_type` field is `NETWORK_DHCP` and if the `principal.ip` field (the IP address of the device requesting the DHCP lease) is `10.0.0.1`, Google SecOps applies the custom label to the event.

You can use the Suspicious DHCP Activity label to create a scope and assign the scope to the relevant users. The scope assignment lets you restrict access to these events to specific users or roles within your organization.

### Custom Label requirements and limitations

We recommend that you review the following limits and requirements when you define and use custom labels:

#### Naming and syntax requirements

  * Custom Label names must be unique and can have a maximum length of 63 characters. The name can contain only lowercase letters, numeric characters, and hyphens. A deleted label name cannot be reused after deletion.



#### Functional limitations

Custom Label query don't support the following advanced features:

  * Reference lists
  * Enrichment fields
  * Data tables



**Query execution time** : Custom label query is subject to a maximum execution time limit of 5 seconds.

### Create custom label

To create a custom label, do the following:

  1. [Log in to Google SecOps](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui).

  2. Click **Settings** > **SIEM Settings** > **Data Access**.

  3. On the **Custom labels** tab, click **Create custom label**.

  4. In the **UDM Search** window, type your query and click **Run Search**.

You can refine the query and click **Run Search** until the results display the data that you want to label. For more information about running a query, see [Enter a UDM Search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#enter_a_udm_search).

  5. Click **Create label**.

  6. On the **Create label** window, select **Save as new label** , and enter the label name and description.

  7. Click **Create label**.

A new custom label is created. During data ingestion, this label is applied to data that matches the UDM query. The label is not applied to data that is already ingested.




### Modify custom label

You can only modify the label description and the query associated with a label. Label names cannot be updated. When you modify a custom label, the changes are applied only to new data and not to the data that is already ingested.

To modify a label, do the following:

  1. [Log in to Google SecOps](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui).

  2. Click **Settings** > **SIEM Settings** > **Data Access**.

  3. On the **Custom labels** tab, click more_vert **Menu** against the label that you want to edit and select **Edit**.

  4. In the **UDM Search** window, update your query and click **Run Search**.

You can refine the query and click **Run Search** until the results display the data that you want to label. For more information about running a query, see [Enter a UDM Search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#enter_a_udm_search).

  5. Click **Save changes**.




The custom label is modified.

### Delete custom label

Deleting a label prevents new data from being associated with it. Data that is already associated with the label remains associated with the label. After deletion, you can't recover the custom label or reuse the label name to create new labels.

  1. Click **Settings** > **SIEM Settings** > **Data Access**.

  2. In the **Custom labels** tab, click the more_vert **Menu** for the label that you want to delete and select **Delete**.

  3. Click **Delete**.

  4. On the confirmation window, click **Confirm**.




The custom label is deleted.

### View custom label

To view a custom label details, do the following:

  1. Click **Settings** > **SIEM Settings** > **Data Access**.

  2. In the **Custom labels** tab, click more_vert **Menu** against the label that you want to edit and select **View**.

The label details are displayed.




## Create and manage scopes

You can create and manage data scopes within the Google SecOps user interface, and then assign those scopes to users or groups through IAM. You can create a scope by applying labels that define the data that a user with the scope has access to.

### Create scopes

To create a scope, do the following:

  1. [Log in to Google SecOps](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui).

  2. Click **Settings** > **SIEM Settings** > **Data Access**.

  3. On the **Scopes** tab, click **Create scope**.

  4. In the **Create new scope** window, do the following:

     1. Enter **Scope name** and **Description**.

     2. In **Define scope access with labels** > **Allow access** , do the following:

        * To select the labels and their corresponding values that you want to grant users the access to, click **Allow certain labels**.

In a scope definition, labels of the same type (for example, log type) are combined using the OR operator, while labels of different types (for example, log type and namespace) are combined using the AND operator. For more information about how labels define data access in scopes, see [Data visibility with allow and deny labels](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview#data-visibility-with-labels).

        * To give access to all data, select **Allow access to everything**.

     3. To exclude access to some labels, select **Exclude certain labels** , then select the label type and the corresponding values that you want to deny users the access to.

When multiple deny access labels are applied within a scope, access is denied if they match _any_ of those labels.

     4. Click **Test scope** to verify how the labels are applied to the scope.

     5. In the **UDM Search** window, type your query and click **Run Search**.

You can refine the query and click **Run Search** until the results display the data that you want to label. For more information about running a query, see [Enter a UDM Search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#enter_a_udm_search).

     6. Click **Create scope**.

     7. In the **Create scope** window, confirm the scope name and description and click **Create scope**.




The scope is created. You must assign the scope to users to give them access to the data in the scope.

### Modify scope

You can only modify scope description and the associated labels. Scope names cannot be updated. After you update a scope, the users associated with the scope are restricted as per the new labels. The rules that are bound to the scope are not re-matched against the updated one.

To modify a scope, do the following:

  1. [Log in to Google SecOps](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui).

  2. Click **Settings** > **SIEM Settings** > **Data Access**.

  3. On the **Scopes** tab, click more_vert **Menu** corresponding to the scope that you want to edit and select **Edit**.

  4. Click edit **Edit** to edit the scope description.

  5. In the **Define scope access with labels** section, update the labels and their corresponding values as required.

  6. Click **Test scope** to verify how the new labels are applied to the scope.

  7. In the **UDM Search** window, type your query and click **Run Search**.

You can refine the query and click **Run Search** until the results display the data that you want to label. For more information about running a query, see [Enter a UDM Search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search#enter_a_udm_search).

  8. Click **Save changes**.




The scope is modified.

### Delete scope

When a scope is deleted, users don't have access to the data associated with the scope. After deletion, the scope name cannot be reused to create new scopes.

To delete a scope, do the following:

  1. [Log in to Google SecOps](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui).

  2. Click **Settings** > **SIEM Settings** > **Data Access**.

  3. On the **Scopes** tab, click more_vert **Menu** against the scope that you want to delete.

  4. Click **Delete**.

**Note:** After you delete a scope, you can't reuse the scope name.
  5. In the confirmation window, click **Confirm**.




The scope is deleted.

### View scope

To view scope details, do the following:

  1. [Log in to Google SecOps](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui).

  2. Click **Settings** > **Data Access**.

  3. In the **Scopes** tab, click more_vert **Menu** against the scope that you want to view and select **View**.




The scope details are displayed.

## Assign scope to users

Scope assignment is required for controlling data access for users with restricted permissions. Assigning specific scopes to users determines the data that they can view and interact with. When a user is assigned multiple scopes, they gain access to the combined data from all those scopes. You can assign the appropriate scopes to users who require global access so that the users can view and interact with all the data. To assign scopes to a user, do the following:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project)

  2. Select the project that is bound to Google SecOps.

  3. Click person_add **Grant access**.

  4. In the **New principals** field, do the following:

     1. If you're using Workforce Identity Federation or any other third party authentication, [add your principal identifier](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#representing-workforce-users) as follows: 
            
            principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/USER_EMAIL_ADDRESS

Replace the following:

        * `POOL_ID`: the identifier for the pool created for your identity provider.
        * `USER_EMAIL`: the user's email address.
     2. If you're using Cloud Identity or Google Workspace, [add your principal identifier](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#representing-workforce-users) as follows: 
            
            user:USER_EMAIL

Replace the following:

        * `USER_EMAIL`: the user's email address.
  5. In the **Assign roles** > **Select a role** menu, select the required role. Click **Add another role** to add multiple roles. To understand which roles need to be added, see [User roles](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview#user-roles).

  6. To assign a scope to the user, add conditions to the Chronicle Restricted Data Access role that is assigned to the user (does not apply to global access roles).

**Note:** When assigning a scope to a group, make sure that the group has at least one member. A scope assigned to an empty group doesn't apply to any users. Members of groups without assigned scopes can sign in to Google SecOps but can't access data until they belong to a scoped group.
     1. Click **Add IAM condition** against the **Chronicle Restricted Data Access** role. The **Add condition** window appears.

     2. Enter the condition title and the optional description.

     3. Add the condition expression.

You can add a condition expression using either the **Condition builder** or the **Condition editor**.

The condition builder provides an interactive interface to select the condition type, operator, and other applicable details about the expression. The following operators let you create precise rules for controlling access to multiple scopes with a single IAM condition:

     * **ENDS_WITH** : checks if the scope name ends with a specific word. To match the exact word, add a `/` before the word.

Consider an example data access scope named `projects/1234/locations/us/instances/2342-434-44-3434-343434/dataAccessScopes/scopename`.

       * `ENDS_WITH /scopename` matches the exact name and evaluates as `true` for the example scope.

       * `ENDS_WITH scopename` matches any name that ends with "scopename" and is evaluated as `true` for the example scope and also for `projects/1234/locations/us/instances/2342-434-44-3434-343434/dataAccessScopes/testscopename`.

     * **STARTS_WITH** : checks if the scope name starts with a specific word. For example, `STARTS_WITH projects/project1` grants access to all the scopes within "project1".

     * **EQUALS_TO** : checks if the name exactly matches a specific word or phrase. This gives access to only one scope. For example, `EQUALS_TO projects/1234/locations/us/instances/2342-434-44-3434-343434/dataAccessScopes/scopename` evaluates as `true` for the example scope.

To add scopes to the role, we recommend the following:

     1. Select **Name** in **Condition type** , the operator in **Operator** , and enter the scope name in **Value**.

`/<scopename>`

     2. To assign multiple scopes, add more conditions using the OR operator. You can add up to 12 conditions for each role binding. To add more than 12 conditions, create multiple role bindings and add up to 12 conditions to each of these bindings.

For more information about conditions, see [Overview of IAM conditions](https://docs.cloud.google.com/iam/docs/conditions-overview).

     3. Click **Save**.

The condition editor provides a text-based interface to manually enter an expression using [CEL syntax](https://docs.cloud.google.com/iam/docs/conditions-overview#cel).

     4. Enter the following expression:
            
            (scope-name: resource.name.endsWith('/SCOPENAME1') || resource.name.endsWith('/SCOPENAME2') || … || resource.name.endsWith('/SCOPENAME'))

Replace /SCOPENAME1, /SCOPENAME2, and other placeholders with the scope names that you want to assign to the principle.

     5. Click **Run Linter** to validate the CEL syntax.

     6. Click **Save**.

**Note:** Conditional role bindings don't override role bindings with no conditions. If a principal is bound to a role, and the role binding does not have a condition, then the principal always has that role. Adding the principal to a conditional binding for the same role has no effect.
  7. Click **Test changes** to see how your changes affect the user access to the data.

  8. Click **Save**.




The users can now access the data that is associated with the scopes.

## Enable data RBAC

Enabling data RBAC applies all assigned scopes to rules and reference lists, making sure users see only the data relevant to their scopes. To enable data RBAC, do the following:

  1. [Log in to Google SecOps](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui).

  2. Click **Settings** > **SIEM Settings** > **Data Access**.

  3. Navigate to the **Assignments** tab and review the scope assignments of the rules and reference lists. To find specific items, use the filter or search functionalities.

  4. Click **Enforce data access**. The Enforce data access window displays the number of rules and reference lists that will be scoped after data RBAC is enforced.

  5. Click **Yes, Enforce**.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
