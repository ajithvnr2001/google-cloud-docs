---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/privileged-admission-organizations/
title: Restrict privileged GKE workloads in organizations \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:32:00.131943+00:00
---

# Restrict privileged GKE workloads in organizations  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/privileged-admission-organizations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Restrict privileged GKE workloads in organizations Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

You can use policies to control which privileged workloads can run in Google Kubernetes Engine (GKE) clusters across your Google Cloud organization. This document shows you how to use policies to define approved workload sources and enforce good practices to improve your security posture. 

This document is for identity and account admins who want to allow only approved privileged workloads to run anywhere in the organization. You should already be familiar with the concepts in the following pages:

  * [About privileged workload admission in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-privileged-workloads)
  * [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview)
  * [Using managed constraints in an organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#managed-constraints).



## How privileged workload admission control works for organizations

By default, GKE Autopilot enforces a set of [security measures](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security) for workloads. The only way to run workloads that violate these constraints is to install _allowlists_ for those workloads. To install an allowlist from a specific source, the cluster must be configured to admit allowlists from that source.

By default, Google Cloud organizations let platform admins configure clusters to admit allowlists from [GKE partners](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners#allowlisted-partner-workloads) and [verified open source projects](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/run-autopilot-open-source-workloads). If your organization has security requirements to limit privileged workloads to an explicit known set of sources, you can use an organization policy to modify the default behavior.

When you enforce a list of approved allowlist sources for your organization, folder, or project, platform admins can specify only those sources when they create or update Autopilot or Standard clusters. If a cluster is created or updated with an unapproved source specified, the operation fails.

The organization policies that you should configure depend on your use case, as follows:

  * **Allow only specific privileged workloads to run in your organization, folder, or project** :

    1. Configure an organization policy for allowlists
    2. Configure an organization policy to allow only Autopilot clusters
  * **Allow privileged workloads to run in Autopilot mode in Standard clusters** : Configure an organization policy for allowlists




## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. Enable the Resource Manager API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudresourcemanager.googleapis.com)

  3. Enable the Resource Manager API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudresourcemanager.googleapis.com)

  4. If your teams have allowlists for privileged workloads that they own, ask them to give you the paths to those allowlists in Cloud Storage.



### Required roles and permissions

To get the permissions that you need to manage organization policies, ask your administrator to grant you the [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization, folder, or project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure an organization policy for allowlists

You can control the approved sources of allowlists for an organization, folder, or project by creating or updating an organization policy based on the `constraints/container.managed.autopilotPrivilegedAdmission` managed constraint. When you enforce this organization policy, cluster administrators can install allowlists only from the sources that you define in the policy.

In addition to these steps, we recommend that you enforce an organization policy that allows only Autopilot clusters to run in your environment. When there are no Standard clusters in the environment, only your approved privileged workloads can run. For more information, see the Configure an organization policy to allow only Autopilot clusters section.

To configure an organization policy for approved privileged workload allowlists, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Organization policies** page:

[Go to Organization policies](https://console.cloud.google.com/projectselector2/iam-admin/orgpolicies?supportedpurview=organizationId,folder,project)

  2. In the table of constraints, find the `container.managed.autopilotPrivilegedAdmission` managed constraint.

  3. Click more_vert **Actions** > **Edit policy**. The **Edit policy** page opens.

  4. In the **Policy source** section, select **Override parent's policy**.

  5. In the **Rules** section, click **Add a rule**.

  6. In the **Enforcement** section, select **On**. The **Parameters** section appears.

  7. To control whether GKE-approved allowlists can be installed, follow these steps:

     1. In the **allowAnyGKEPath** parameter, click edit **Edit**. The **Edit parameter values** pane opens.
     2. In the **Value type** section, select **User-defined**.
     3. In the **User-defined values** section, select one of the following options:

        * **True** : administrators can configure clusters to run allowlists from any path that starts with `gke://`. This is the default value.
        * **False** : administrators can configure clusters to run allowlists only from the paths that you specify in the `allowPaths` parameter of the organization policy. If you don't specify paths in the `allowPaths` parameter, clusters can't run any allowlists from any source.
     4. Click **Save**. The **Edit parameter values** pane closes.

  8. To define the specific allowlists that can be installed, follow these steps:

     1. In the **allowPaths** parameter, click edit **Edit**. The **Edit parameter values** pane opens.
     2. In the **Value type** section, select **User-defined**.
     3. In the **User-defined values** section, specify one or more paths to allowlist sources. For more information about what you can specify, see [Allowlist paths](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-privileged-workloads#allowlist-paths).
     4. Click **Save**. The **Edit parameter values** pane closes.
     5. In the **Edit rule** section, click **Done**.
  9. Optional: To test the impact of enforcing the organization policy, click **Test changes**. For more information, see [Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies).

  10. To enforce the policy in [dry-run mode](https://docs.cloud.google.com/resource-manager/docs/organization-policy/dry-run-policy), click **Set dry run policy**.

  11. After you verify that the organization policy works as intended in dry-run mode, set the live policy by clicking **Set policy**.




Changes to your organization policy can take up to 15 minutes to be fully enforced.

###  gcloud 

  1. Create a YAML file that defines the organization policy:
         
         name: RESOURCE_TYPE/RESOURCE_ID/policies/container.managed.autopilotPrivilegedAdmission
         spec:
           rules:
           - enforce: true
             parameters:
               allowAnyGKEPath: ALLOW_GKE_PATHS
               allowPaths:
               - ALLOWLIST1_PATH
               - ALLOWLIST2_PATH
         

Replace the following:

     * `RESOURCE_TYPE`: the type of Google Cloud resource. This must be one of the following values:

       * `organizations`
       * `folders`
       * `projects`
     * `RESOURCE_ID`: the organization ID, folder ID, or project ID.

     * `ALLOW_GKE_PATHS`: whether to allow any GKE-approved allowlists. Specify one of the following values:

       * `True`: allow cluster configuration with any GKE partner workload or verified open source workloads. This is the default value.
       * `False`: allow cluster configuration with only the paths in the `allowPaths` field.

**Caution:** This value prevents Autopilot and Standard clusters from being created or updated to use the default GKE configuration, which allows the use of GKE-approved allowlists. Operations such as creating clusters without modifying any allowlist options will fail. For more information, see [Managed constraint parameters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-privileged-workloads#constraint-parameters).
     * `ALLOWLIST1_PATH`,`ALLOWLIST2_PATH`: the path to allowlists. For more information about what you can specify, see [Allowlist paths](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-privileged-workloads#allowlist-paths).

Optionally, to make the organization policy conditional on a tag, add a `condition` block to the `rules` field. If you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more information, see [Setting an organization policy with tags](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy).

  2. To set the organization policy in [dry-run mode](https://docs.cloud.google.com/resource-manager/docs/organization-policy/dry-run-policy), specify the `dryRunSpec` value for the [`--update-mask`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-policy#--update-mask) flag in the `gcloud org-policies set-policy` command:
         
         gcloud org-policies set-policy POLICY_FILEPATH \
             --update-mask=dryRunSpec
         

Replace `POLICY_FILEPATH` with the path to the YAML file that you created in the previous step.

  3. Optional: To test the impact of enforcing this organization policy, use the [`gcloud policy-intelligence simulate org-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/policy-intelligence/simulate/orgpolicy) command:
         
         gcloud policy-intelligence simulate org-policy \
             --organization=ORGANIZATION_ID \
             --policy-path=POLICY_FILEPATH
         

Replace `ORGANIZATION_ID` with your organization ID.

  4. After you verify that the organization policy works as intended in dry-run mode, set the live policy by specifying the `spec` value for the `--update-mask` flag in the `gcloud org-policies set-policy` command:
         
         gcloud org-policies set-policy POLICY_FILEPATH \
             --update-mask=spec
         

Changes to your organization policy can take up to 15 minutes to be fully enforced.




**Success:** In the organization, folder, or project where you enforced the policy, platform admins can specify only approved allowlist paths when they create or update clusters.

## Configure an organization policy to allow only Autopilot clusters

**Caution:** If you follow these steps to enforce an organization policy that allows only Autopilot clusters in an organization, folder, or project, new and existing Standard clusters will violate the policy. Test the impact of enforcing the policy by setting it in dry-run mode and by simulating violations with Policy Simulator, as described in this section.

This section shows you how to configure an organization policy that allows only Autopilot clusters. We recommend that you configure this policy in addition to creating an organization policy for allowlists, because Standard clusters can run most privileged workloads. Allowing only Autopilot clusters means that your environment runs only the privileged workloads that you allow. The steps in this section are optional.

To configure this policy, select one of the following options:

###  Console 

  1. Create a custom constraint that allows only Autopilot cluster creation:

     1. In the Google Cloud console, go to the **Organization policies** page:

[Go to Organization policies](https://console.cloud.google.com/projectselector2/iam-admin/orgpolicies?supportedpurview=organizationId,folder,project)

     2. Click add **Custom constraint**. The **Create custom constraint** page opens.

     3. Specify a display name and a unique ID for the constraint.

     4. In the **Enforcement** section, follow these steps:

        1. In the **Resource type** list, select **container.googleapis.com/Cluster**.
        2. In the **Enforcement method** list, select **Enforcement on create**.
        3. In the **Condition** section, click edit **Edit Condition**. The **Add condition** pane opens.
        4. Specify the following expression:
               
               resource.autopilot.enabled == true
               

        5. Click **Save**. The **Add condition** pane closes.

        6. In the **Action** section, select **Allow**.

     5. Click **Create constraint**.

  2. Create a custom organization policy that enforces the constraint:

     1. In the table of constraints, find the custom constraint that you created in the previous step.
     2. Click more_vert **Actions** > **Edit policy**. The **Edit policy** page opens.
     3. In the **Policy source** section, select **Override parent's policy**.
     4. Click **Add a rule**.
     5. In the **Enforcement** section, select **On**.
     6. To test the impact of enforcing the organization policy, click **Test changes**. For more information, see [Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies).
     7. To enforce the policy in [dry-run mode](https://docs.cloud.google.com/resource-manager/docs/organization-policy/dry-run-policy), click **Set dry run policy**.
     8. After you verify that the organization policy works as intended in dry-run mode, set the live policy by clicking **Set policy**.

Changes to your organization policy can take up to 15 minutes to be fully enforced.




###  gcloud 

  1. Create a custom constraint that allows only Autopilot cluster creation:

     1. Create a YAML file that defines the custom constraint:
            
            name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
            resourceTypes: container.googleapis.com/Cluster
            methodTypes:
            - CREATE
            condition: resource.autopilot.enabled == true
            actionType: ALLOW
            displayName: "Allow only Autopilot clusters"
            

Replace the following:

        * `ORGANIZATION_ID`: your organization ID.
        * `CONSTRAINT_NAME`: a name for your new constraint.
     2. Set the custom constraint:
            
            gcloud org-policies set-custom-constraint CONSTRAINT_FILEPATH
            

Replace `CONSTRAINT_FILEPATH` with the path to the YAML file that you created in the previous step.

The custom constraint is available to use in an organization policy.

  2. Create a custom organization policy that enforces the constraint:

     1. Create a YAML file that defines the organization policy:
            
            name: RESOURCE_TYPE/RESOURCE_ID/policies/custom.CONSTRAINT_NAME
            spec:
              rules:
              - enforce: true
            

Replace the following:

        * `RESOURCE_TYPE`: the type of Google Cloud resource. This must be one of the following values:

          * `organizations`
          * `folders`
          * `projects`
        * `RESOURCE_ID`: the ID of the organization, folder, or project.

Optionally, to make the organization policy conditional on a tag, add a `condition` block to the `rules` field. If you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more information, see [Setting an organization policy with tags](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy).

     2. To set the organization policy in [dry-run mode](https://docs.cloud.google.com/resource-manager/docs/organization-policy/dry-run-policy), specify the `dryRunSpec` value for the [`--update-mask`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-policy#--update-mask) flag in the `gcloud org-policies set-policy` command:
            
            gcloud org-policies set-policy POLICY_FILEPATH \
                --update-mask=dryRunSpec
            

Replace `POLICY_FILEPATH` with the path to the YAML file that you created in the previous step.

     3. To test the impact of enforcing this organization policy, use the [`gcloud policy-intelligence simulate org-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/policy-intelligence/simulate/orgpolicy) command:
            
            gcloud policy-intelligence simulate org-policy \
                --organization=ORGANIZATION_ID \
                --policy-path=POLICY_FILEPATH
            

Replace `ORGANIZATION_ID` with your organization ID.

     4. After you verify that the organization policy works as intended in dry-run mode, set the live policy by specifying the `spec` value for the `--update-mask` flag in the `gcloud org-policies set-policy` command:
            
            gcloud org-policies set-policy POLICY_FILEPATH \
                --update-mask=spec
            

Changes to your organization policy can take up to 15 minutes to be fully enforced.




**Success:** In the organization, folder, or project where you enforced the policy, platform admins can create only Autopilot clusters.

## What's next

  * Tell your platform admins to [run privileged workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-autopilot-partner-workloads)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
