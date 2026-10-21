---
url: https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/managing-constraint/
title: Manage the nested virtualization constraint \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:13.542795+00:00
---

# Manage the nested virtualization constraint  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/managing-constraint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage the nested virtualization constraint Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document describes how to check whether nested virtualization is enabled, and how to modify the boolean constraint that controls whether nested virtualization is enabled for your organization, project, or folder.

A boolean constraint within an organization policy determines whether you can create nested VMs. The boolean constraint for nested virtualization is a restriction, which means that when it's enforced, it tells the organization policy to restrict the creation of nested VMs. Enforcing this constraint prevents Compute Engine from exposing virtualization extensions to VMs (L1 VMs). This means that while you can still create L1 VMs with configurations that enable nested virtualization, you can't run any nested VMs (L2 VMs) on those L1 VMs. For more information about boolean constraints, see [Understanding constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints).

The **Disable VM nested virtualization** constraint is not enforced by default, so you do not have to modify any boolean constraint to enable nested virtualization. Even so, Google recommends explicitly setting the value of the constraint so that your organization, folders, and projects don't rely on the default setting. If your project is not subordinate to an organization, the constraint is not enforced by default and you can't change the constraint.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Check whether nested virtualization is allowed

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `orgpolicy.policy.get` on the organization, folder, or project 



Check whether nested virtualization is allowed for an organization, folder, or project by using the Google Cloud console, the Google Cloud CLI, or REST.

###  Console 

Check whether you can create nested VMs in your organization, folder, or project by checking if the boolean constraint for disabling nested virtualization is not enforced. If the **Disable VM nested virtualization** constraint is not enforced by the organization policy, then you can create nested VMs.

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. In the organization, folder, and project selector, select the entity to view the organization policies for.

  3. Select the **Disable VM nested virtualization** constraint to open the **Policy details** page.

  4. View the value for **Enforcement** :

     * If the value is **Not enforced** , then nested virtualization is enabled, and you can create nested VMs.

     * If the value is **Enforced** , then nested virtualization is disabled, and you can't create nested VMs.




###  gcloud 

Check the value of the `compute.disableNestedVirtualization` boolean constraint by using the [`gcloud resource-manager org-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/describe).

If the Google Cloud CLI output does not show a value for `booleanPolicy`, then nested virtualization is allowed and you can create nested VMs.

If the Google Cloud CLI output value for `booleanPolicy` is `enforced: true`, then the organization policy is enforcing the disable nested virtualization constraint and you can't create nested VMs.
    
    
    gcloud resource-manager org-policies \
      describe constraints/compute.disableNestedVirtualization \
      (--organization=ORGANIZATION_ID | --folder=FOLDER_ID |
      --project=PROJECT_ID) --effective
    

Replace exactly one of the following:

  * `ORGANIZATION_ID`: the ID of the organization to get the constraint value of. For a list of accessible organizations and their IDs, run the [`gcloud organizations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/list).

  * `FOLDER_ID`: the ID of the folder to get the constraint value of. For a list of accessible folders and their IDs, run the [`gcloud resource-manager folders list` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/folders/list).

  * `PROJECT_ID`: the ID of the project to get the constraint value of. For a list of accessible projects and their IDs, run the [`gcloud projects list` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/list).




###  REST 

Use REST to check the value of the `compute.disableNestedVirtualization` boolean constraint, which determines whether you can create nested VMs in your organization, folder, or project.

If the REST response doesn't return a value for `"booleanPolicy"` for the constraint, then nested virtualization is not disabled and you can create nested VMs.

If the value for `"booleanPolicy"` in the output is `"enforced": true`, then nested virtualization is disabled and you can't create nested VMs.
    
    
    POST https://cloudresourcemanager.googleapis.com/v1/RESOURCE/RESOURCE_ID:getOrgPolicy
    
    {
      "constraint": "compute.disableNestedVirtualization"
    }
    

Replace the following:

  * `RESOURCE`: the resource to get the organization policy for. Set to one of the following:

    * `organizations`: calls the [`organizations.getOrgPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/getOrgPolicy)

    * `folders`: calls the [`folders.getOrgPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/folders/getOrgPolicy)

    * `projects`: calls the [`projects.getOrgPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getOrgPolicy)

  * `RESOURCE_ID`: the organization, folder, or project on which to check the status of the disable nested virtualization constraint




From within a Linux VM, you can run the command `grep -c vmx /proc/cpuinfo` to check if virtualization extensions are available to the VM. If this command returns `0`, virtualization extensions aren't available and you can't run nested VMs. One reason for this might be because the **Disable VM nested virtualization** constraint is enforced by an organization policy. If you attempt to start a nested VM by using KVM, you might see an error message similar to the following: `Could not access KVM kernel module: No such file or directory`.

## Modify the nested virtualization organization policy

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `orgpolicy.policy.get` on the organization, folder, or project 
  * `orgpolicy.policy.set` on the organization, folder, or project 



If you have the appropriate role, you can control whether an organization, folder, or project can create nested VMs. Control this enforcement by using the boolean constraint for nested virtualization.

Use the Google Cloud console, the Google Cloud CLI, or REST to enable nested virtualization for an organization, folder, or project.

###  Console 

To enable nested virtualization, disable the enforcement of the **Disable VM nested virtualization** boolean constraint, and to disable nested virtualization, enable the enforcement of the boolean constraint.

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. In the organization, folder, and project selector, select the entity to edit the organization policies for.

  3. Select the **Disable VM nested virtualization** constraint to open the **Policy details** page.

  4. Click **Edit** , then select **Customize**.

  5. Under **Enforcement** , select one of the following enforcement options for the **Disable VM nested virtualization** boolean constraint:

     * **On** : enable enforcement and disable nested virtualization
     * **Off** : disable enforcement and enable nested virtualization
  6. Click **Save**.




###  gcloud 

Use the [`gcloud resource-manager org-policies` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies) to enable or disable enforcement of the `compute.disableNestedVirtualization` organization policy boolean constraint.

If you disable the `compute.disableNestedVirtualization` constraint by using the `disable-enforce` command, then you can create VMs that have nested virtualization enabled.

If you enable the constraint by using the `enable-enforce` command, then you can't create VMs that have nested virtualization enabled.
    
    
    gcloud resource-manager org-policies \
      ( disable-enforce | enable-enforce ) compute.disableNestedVirtualization \
      (--organization=ORGANIZATION_ID | --folder=FOLDER_ID |
      --project=PROJECT_ID)
    

Replace exactly one of the following:

  * `ORGANIZATION_ID`: the ID of the organization to modify the constraint value of. For a list of accessible organizations and their IDs, run the [`gcloud organizations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/list).

  * `FOLDER_ID`: the ID of the folder to modify the constraint value of. For a list of accessible folders and their IDs, run the [`gcloud resource-manager folders list` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/folders/list).

  * `PROJECT_ID`: the ID of the project to modify the constraint value of. For a list of accessible projects and their IDs, run the [`gcloud projects list` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/list).




###  REST 

Use REST to modify the value of the `compute.disableNestedVirtualization` boolean constraint, which determines whether you can create nested VMs in your organization, folder, or project.
    
    
    POST https://cloudresourcemanager.googleapis.com/v1/RESOURCE/RESOURCE_ID:setOrgPolicy
    
    {
      "policy": {
        "booleanPolicy": {
          "enforced": ENFORCE
        },
        "constraint": "constraints/compute.disableNestedVirtualization"
      }
    }
    

Replace the following:

  * `RESOURCE`: the resource to modify the organization policy of. Set this to one of the following:

    * `organizations`: calls the [`organizations.setOrgPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/setOrgPolicy)

    * `folders`: calls the [`folders.setOrgPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/folders/setOrgPolicy)

    * `projects`: calls the [`projects.setOrgPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setOrgPolicy)

  * `RESOURCE_ID`: the organization, folder, or project on which to check the status of the disable nested virtualization constraint

  * `ENFORCE`: determines whether the organization policy enforces the `compute.disableNestedVirtualization` boolean constraint. Set to one of the following:

    * `true`: to enforce the constraint. With this setting you can't create VMs that have nested virtualization enabled.

    * `false`: to not enforce the constraint. With this setting, you can create VMs that have nested virtualization enabled.




## What's next

  * [Enable nested virtualization on a VM](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/enabling)
  * [Troubleshoot nested virtualization](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-nested-vms)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
