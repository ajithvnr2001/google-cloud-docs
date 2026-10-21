---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/google-groups-rbac/
title: Configure Google Groups for RBAC \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:17:24.842002+00:00
---

# Configure Google Groups for RBAC  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/google-groups-rbac/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Configure Google Groups for RBAC Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to set up Google Groups to work with Kubernetes role-based access control (RBAC) in your Google Kubernetes Engine (GKE) clusters.

Google Groups for RBAC lets you assign RBAC permissions to members of Google Groups in Google Workspace. Your Google Workspace administrators maintain the users and groups completely outside of GKE or the Google Cloud console. Your cluster administrators therefore won't need detailed information about users.

Using Google Groups for RBAC also lets you integrate with your existing user account management practices, such as revoking access when someone leaves your organization.

This page is for Security specialists and Operators who want to use Google Groups with Kubernetes RBAC in GKE clusters. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the [limitations of Google Groups](https://support.google.com/a/answer/6099642#zippy=%2Cmembership) when creating groups and adding users as members.

To use Google Groups for RBAC, complete the following tasks:

  1. Meet the requirements.
  2. Set up your Google Groups.
  3. Enable Google Groups for RBAC on a cluster.
  4. Define and assign RBAC permissions to the Google Groups.



## Requirements

To use Google Groups for RBAC, you must have access to [Google Workspace](https://workspace.google.com/) or any edition of [Cloud Identity](https://docs.cloud.google.com/identity).

## Limitations

  * GKE supports users with membership in up to 2000 groups under the security group, including nested memberships, with Google Groups for RBAC.



## Set up your Google Groups

The following steps show you how to set up a group in Google Groups that works with RBAC:

  1. Create a group in your domain named `gke-security-groups`. The `gke-security-groups` name is required. Make sure the group has the **View Members** permission selected for **Group Members**. For details, see [Set permissions for managing members and content](https://support.google.com/a/users/answer/9886284).

  2. Create groups, if they do not already exist, that represent sets of users who should have different permissions on your clusters, such as developers and cluster administrators. Each group must have the **View members** permission for **Group members**.

  3. Add your groups as nested groups to the `gke-security-groups` group. Don't add individual users as members of `gke-security-groups`.




For more information on managing Google Groups, refer to the [Google Groups Help Center](https://support.google.com/a/topic/25838).

To check whether a specific user can perform an action on a cluster resource, GKE checks if the user is a member of a group with access and if that group is [nested](https://support.google.com/a/answer/167100) in the `gke-security-groups` group.

Information about Google Groups membership is cached for a short time. It might take a few minutes for changes in group memberships to propagate to all your clusters. In addition to latency from group changes, standard caching of user credentials on the cluster is about one hour.

## Enable Google Groups for RBAC on clusters

You can enable Google Groups for RBAC on new and existing GKE Standard and Autopilot clusters using the Google Cloud CLI or the Google Cloud console.

**Caution:** After you create or update a cluster to use Google Groups for RBAC, deleting any of your groups causes your role bindings and access grants to fail. For more information, see the Effects of deleting groups section.

### Create a new cluster

### gcloud

**Standard**

To create a new Standard cluster and enable Google Groups for RBAC, run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --security-group="gke-security-groups@DOMAIN"
    

Replace the following:

  * `CLUSTER_NAME`: the name of the new cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `DOMAIN`: the domain name of the `gke-security-groups` group you created.



**Autopilot**

To create a new Autopilot cluster and enable Google Groups for RBAC, run the following command:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --security-group="gke-security-groups@DOMAIN"
    

### Console

To create a new cluster and enable the Google Groups for RBAC feature, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click _add_box_ **Create**.

  3. Click **Configure** for the cluster mode that you want to use.

  4. In the navigation pane, click **Advanced settings** , and then do one of the following:

     * **Autopilot** : Expand the **Security** section, select the **Enable Google Groups for RBAC** checkbox, and fill in **Security Group** with `gke-security-groups@DOMAIN`.
     * **Standard** : In the **Google Groups for RBAC** row, click _edit_ **Edit configuration** , select the **Enable Google Groups for RBAC** checkbox, fill in **Security Group** with `gke-security-groups@DOMAIN`, and then click **Save**.
  5. Click **Create**.




### Update an existing cluster

### gcloud

To update an existing cluster to enable Google Groups for RBAC, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --security-group="gke-security-groups@DOMAIN"
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `DOMAIN`: the domain name of the `gke-security-groups` group you created.



### Console

To update an existing cluster to enable Google Groups for RBAC, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster that you want to update.

  3. On the **Details** tab, locate the **Security** section.

  4. For the **Google Groups for RBAC** field, click _edit_ **Edit Google Groups for RBAC**.

  5. Select the **Enable Google Groups for RBAC** checkbox.

  6. Fill in **Security Group** with `gke-security-groups@DOMAIN`.

  7. Click **Save changes**.




## Define and assign permissions

After creating and configuring Google Groups for RBAC, use roles and role bindings to define RBAC permissions and assign those permissions to Google Groups that are members of the `gke-security-groups` group. For instructions, refer to [Define and assign permissions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#define-and-assign).

**Note:** The Google Groups references in RBAC are case-sensitive. Use the exact group name in your RoleBinding and ClusterRoleBinding definitions.

## Verify Google Groups for RBAC configuration

The following sections show you how to verify that your Google Groups for RBAC configuration was successful, using either the gcloud CLI or the Google Cloud console.

### Verify using the gcloud CLI

Run a kubectl `can-i` command to check whether you can perform a specific action against a specific Kubernetes resource. You can use this method to automate testing RBAC access as part of your CI/CD workflow.For example, the following command tests for `get` access to `pods` resources in the `dev` namespace:
    
    
    kubectl auth can-i get pods \
        --namespace=dev \
        --as=USER \
        --as-group=GROUP
    

Replace the following:

  * `USER`: the name of the user to impersonate, such as `gke-user@example.com`. The specified user must be a member of the group for which you're testing access.
  * `GROUP`: the name of the group to impersonate, such as `gke-dev-users@example.com`.



If `USER` has access, the output is `yes`. If not, the output is `no`.

### Verify using the Google Cloud console

You can also verify RBAC access by running a kubectl command against your cluster and checking your logs.

#### Before you begin

Before you begin, ensure the following:

  * You have not interacted with the cluster you want to test (for example, you haven't run any `kubectl` commands) for at least one hour. Authentication is cached for one hour. Letting the cached credentials expire lets you make sure that the request gets logged when it happens.
  * You are a member of at least one of the groups that are members of the `gke-security-groups` group, which helps ensure that some Google Groups information is logged.



#### Enable logs and run a test command

  1. Enable data access logging for your Google Cloud project. To enable the logging:

     1. Go to the **Audit Logs** page in Google Cloud console.

[Go to Audit Logs](https://console.cloud.google.com/iam-admin/audit)

     2. In the table, select **Kubernetes Engine API**.

     3. In the **Log Type** menu, select:

        * **Admin Read**
        * **Data Read**
        * **Data Write**
     4. Click **Save**.

For more information about enabling Audit Logging, see [Configuring Data Access logs with the Cloud console](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console).

**Important:** Enabling Audit Logging incurs charges. If you only enabled Audit Logging for testing purposes, you should disable it after you've completed testing to avoid charges.
  2. Run a command using `kubectl` in the cluster, such as the following:
         
         kubectl create ns helloworld
         

  3. Enter a custom query in the **Logs Explorer** page. To run the query:

     1. Go to the **Logs Explorer** page in Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

     2. Click the arrow in the **Query preview** box at the top of the page.

     3. In the dropdown box that appears, specify the following query:
            
            resource.type="k8s_cluster"
            resource.labels.location="CLUSTER_LOCATION"
            resource.labels.cluster_name="CLUSTER_NAME"
            protoPayload.resourceName="authorization.k8s.io/v1/selfsubjectaccessreviews"
            protoPayload.authenticationInfo.principalEmail="EMAIL_ADDRESS"
            

Replace the following:

        * `CLUSTER_LOCATION`: your cluster's region or zone.
        * `CLUSTER_NAME`: the name of your cluster.
        * `EMAIL_ADDRESS`: the registered email address of your Google account.
     4. Select **Run Query**. At least one result should appear. If there are no results, try increasing the time range.

     5. Select the cluster you want to examine.

     6. Click **Expand nested fields**.

     7. The `labels.authorization.k8s.io/decision` field contains the outcome if your request was allowed or denied.

     8. The `labels."authorization.k8s.io/reason"` field contains the name of a Google group. This group is a member of the `gke-security-group` and is mapped to the Kubernetes group that determines access.

  4. Optionally, restore data access logging to previous settings to avoid further charges.




## Effects of deleting groups

After you configure Google Groups for RBAC, your RBAC access grants depend on the existence of the Google Groups that you created. Consider the following effects of deleting one of the groups:

  * **`gke-security-group`** : GKE uses the unique ID of the `gke-security-group` group to find the subjects that you reference in your RBAC policies. If you delete this group, all of the access grants for Google Groups for RBAC fail.

If you recreate the `gke-security-group` group, you must re-enable Google Groups for RBAC on your cluster by using the steps in the Update an existing cluster section. Re-enabling Google Groups for RBAC updates the cluster to use the group ID of the new `gke-security-group` group.

  * **Member groups** : if you delete one of the member groups that you configured for Google Groups for RBAC, any RBAC bindings for that group fail. As a result, all of the members of that group lose the corresponding access.

To fix an unintentional member group deletion, create a new group with exactly the same name as the deleted group. Make the new group a member of the `gke-security-group` group by following the steps in the Set up your Google Groups section.




## What's next

  * Learn how to [configure role-based access control](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).
  * Learn more about [access control in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/access-control).
  * Learn about [IAM](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam).
  * Read about [OpenID Connect (OIDC)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/oidc).
  * Learn about [RBAC Best Practices](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/rbac).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
