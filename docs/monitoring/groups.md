---
url: https://docs.cloud.google.com/monitoring/groups/
title: Cloud Monitoring resource groups \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:16.714480+00:00
---

# Cloud Monitoring resource groups  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Cloud Monitoring resource groups Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Monitoring lets you define a set of resources as a group. After you define a group, you can set up alerting policies, charts, and dashboards to monitor the group. You can create up to 500 groups per metrics scope .

**Note:** Use of resource groups is no longer recommended. The preferred way to organize your resources is to use [tags and labels](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview). For example, if you use Cloud Storage, then you might want to use the [metadata](https://docs.cloud.google.com/storage/docs/metadata) included with your Cloud Storage objects.

## About groups

Groups provide a mechanism for alerting on the behavior of a set of resources, rather than on individual resources. For example, you can create an alerting policy that is triggered if some number of resources in the group violates a particular condition (for example, CPU load), rather than having each resource inform you of violations individually.

You define the membership criteria for your groups. A resource belongs to a group if the resource meets the membership criteria of the group. Membership criteria can be based on labels, regions, applications, and other criteria. Resources can belong to multiple groups.

The set of members in a group is dynamic, making groups useful for monitoring changing environments. For example, if you create a group whose membership criteria specifies a geographic region, then new resources in that region are automatically added to the group. You don't have to modify dashboards or alerting policies if the group membership changes.

Groups can contain subgroups, up to eight levels deep. One application for groups and subgroups is management of physical or logical topologies. For example, with groups, you can separate your monitoring of production resources from your monitoring of test or development resources. You can also create subgroups to monitor your production resources by zone.

**Note:** Only load balancer resources of type [`aws_alb_load_balancer`](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_alb_load_balancer) can be put into groups.

## Using groups

When you create a group, Monitoring creates a dashboard for it. In addition to the standard dashboard controls, group dashboards provide controls to do the following:

  * Edit or delete the group. You can't edit or delete a group that is being used by an alerting policy.
  * Manage the alerting policies that depend on the group.
  * Create and view subgroups.
  * View alerts.
  * View events.
  * View group resources.
  * Access group resource dashboards.



Group dashboards are limited to 100 charts. Charts on a group dashboard display data only from the members of the group.

The following screenshot is the default dashboard for the group "My instances":

![Default group dashboard for the My instances group.](https://docs.cloud.google.com/static/monitoring/images/mip-group-default-dashboard.png)

## Overview of your resource groups

In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/groups-icon.png) **Groups** page: 

[Go to **Groups**](https://console.cloud.google.com/monitoring/groups)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

You can add filters to modify which groups are listed. To add a filter, click **Filter table** , and make a selection for the filter type. Based on the type you select, make a selection for the filter value or enter the value.

For any group shown on the **Groups** page, you can do the following:

  * View a group's dashboard by clicking on the group's display name.
  * Edit the group by clicking _edit_ **Edit**
  * Delete the group by clicking delete **Delete**
  * View the associated alerting policies by clicking **Policies** _notifications_
  * View the number VM instance and the number of resources in the group



## Create a group

To create a group by using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/groups-icon.png) **Groups** page: 

[Go to **Groups**](https://console.cloud.google.com/monitoring/groups)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click **Create Group**. The following screenshot shows the **Create group** dialog:

![Group-creation panel.](https://docs.cloud.google.com/static/monitoring/images/mip-group-create-panel.png)

  3. Replace **Name** with a display name for the group. The display name isn't required to be unique in the project.

  4. Add the group membership criteria. See the next section, Specifying membership criteria, for more information.

  5. Click **Create**.




### Specify membership criteria

A group can have multiple membership criteria. The criteria that you see depend on the services that your Google Cloud project is using.

To specify a single criterion when using the Google Cloud console, do the following in the **Create group** dialog:

  1. In the **Add criterion** dialog, select the **Type** of criterion from the menu:

     * **Name** : (Default) Group membership is determined by the display name of the resource.
     * **Tag** : Group membership is determined by tags. For this option, a secondary menu of resource values that are dependent on your configuration is displayed. For example, if you've created Compute Engine instances and have assigned [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) or [labels](https://docs.cloud.google.com/compute/docs/labeling-resources) to the instances, these tags and labels are listed in the secondary menu.

Tag names should be lowercase.

**Note:** You can't create a Monitoring group by selecting [Resource manager tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).
     * **Region** : The location of the resource.

     * **Resource Type** : A resource from which metric data is captured. Resources might include disks, Cloud Storage buckets, or virtual machines (VMs).

     * **Security Group** : Group membership is determined by Role Based Access Control (RBAC). For example, you can specify a security group when you are creating a Google Kubernetes Engine cluster. For more information, see the Kubernetes reference page [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).

     * **Cloud Project** : Your Google Cloud project identifier.

     * **App Engine App** : Your App Engine applications.

     * **App Engine Service** : App Engine services such as the Users API, Memcache, and Images API.

  2. If you select the **Name** or **Tag** criterion, then an **Operator** menu is displayed. In this case, select how the comparison is to be performed. By default, the comparison operation is set to **Contains**.

For example, if you don't want your group to contain any resources with `instance` in the name, then set type to **Name** , value to `instance`, and the operator to **Does not contain**.

When the **Operator** menu isn't displayed, the comparison operator is **Equals**.

  3. Enter the value to be matched.

  4. Click **Done**.




If you want to add a criterion, then repeat the previous procedure. When you have multiple criteria, you set how the criterion are to be combined with the **Combine criteria operator** selector. Choose **AND** if membership requires that a resource satisfy every criterion. Choose **OR** if membership requires that a resource satisfy a single criterion.

The following screenshot shows the group definition for a group named "My instances":

![Create a group of resources named instance.](https://docs.cloud.google.com/static/monitoring/images/mip-group-configuration.png)

In this example, there are 2 criterion, both of which must be met.

## Delete a group

To delete a group by using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/groups-icon.png) **Groups** page: 

[Go to **Groups**](https://console.cloud.google.com/monitoring/groups)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the group you want to delete, and then click delete **Delete**.
  3. In the **Delete group and subgroup** dialog, click **Delete** to confirm the action to delete the group and its subgroups. If you delete a group, you also remove the group from alerting policies and uptime checks.



You can't delete a group that is being used by an alerting policy. For information about how to identify the alerting policy, see View associated alerting policies.

## Edit a group

To edit a group by using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/groups-icon.png) **Groups** page: 

[Go to **Groups**](https://console.cloud.google.com/monitoring/groups)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the group to edit, and then click _edit_ **Edit**.



You can't edit a group that is being used by an alerting policy. For information about how to identify the alerting policy, see View associated alerting policies.

## View associated alerting policies

To view the alerting policies that depend on a group, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/groups-icon.png) **Groups** page: 

[Go to **Groups**](https://console.cloud.google.com/monitoring/groups)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the group, and then click _notifications_ **Policies**.

The **Policies** dialog includes the following:

     * Link to each policy.
     * Options to edit, copy, or delete the policy.
     * Toggle to enable or disable the policy.
     * **Create Policy** button.



## Create an alerting policy for the group

To create an alerting policy that restricts the time series selected by the metric to a group, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/groups-icon.png) **Groups** page: 

[Go to **Groups**](https://console.cloud.google.com/monitoring/groups)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the group, and then click _notifications_ **Policies**.
  3. Click **Create Policy**.
  4. Select the metric type and resource to monitor.
  5. Click **Filter** and select **Group**.
  6. Expand _arrow_drop_down_ **Value** and select the group name.
  7. Click **Done**.
  8. Complete the steps to configure the alerting policy. For more information, see [Create metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).



## Manage groups by using the Cloud Monitoring API

You can create, modify, retrieve, and delete groups by using the [`projects.groups`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups#Group) API. However, groups created by using the API are not editable in the UI.

In the API, groups are identified by a `groupId` field. This is an identifier assigned by Cloud Monitoring when you create the group. The value you provide for the group in the **Group Name** field is a display-only name, stored in a `displayName` field.

You can also use Monitoring filters to do the following:

  * [Add resources](https://docs.cloud.google.com/monitoring/api/v3/filters#group-filter) to a group.
  * [List the members](https://docs.cloud.google.com/monitoring/api/v3/filters#group-member-filter) of a group.
  * [Retrieve time-series data](https://docs.cloud.google.com/monitoring/api/v3/filters#time-series-filter) based on groups.



## What's next

  * Create and view [uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks#create) for the group.
  * Create [alerting policies](https://docs.cloud.google.com/monitoring/alerts) for the group.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
