---
url: https://docs.cloud.google.com/compute/docs/instances/manage-placement-policies/
title: Replace, remove, or delete placement policies \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:42.454710+00:00
---

# Replace, remove, or delete placement policies  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/manage-placement-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Replace, remove, or delete placement policies Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to replace, remove, or delete placement policies.

Replacing, removing, or deleting [placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview) is useful in the following cases:

  * Replace a placement policy in a virtual machine (VM) instance to move the VM to a different position relative to other VMs.

  * Remove a placement policy from a VM when you're no longer interested in its position relative to other VMs.

  * Delete a placement policy when you no longer need it.




## Before you begin

  * Review the [ restrictions](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#restrictions) for placement policies.
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

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




### Required roles

To get the permissions that you need to replace, remove, or delete placement policies, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to replace, remove, or delete placement policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to replace, remove, or delete placement policies:

  * To replace or remove a placement policy from a VM: `compute.instances.update` on the project 
  * To delete a placement policy: `compute.resourcePolicies.delete` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Replace a placement policy in a VM

Before you replace a spread placement policy in a VM with a compact placement policy, make sure that the VM uses a [supported machine type and host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies). If you need to update the VM before replacing its placement policy, then do one or both of the following:

  * [Change the host maintenance policy of the VM](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#updatingoption).

  * [Change the machine type of the VM](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance).




After you replace the placement policy in a VM, you must restart the VM to make the newly applied placement policy effective.

To replace a placement policy in a VM, select one of the following options:

###  gcloud 

  1. Create an empty YAML file.

  2. To export the properties of a VM into the YAML file that you've just created, use the [`gcloud compute instances export` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/export).
         
         gcloud compute instances export VM_NAME \
             --destination=FILE_PATH \
             --zone=ZONE
         

Replace the following:

     * `VM_NAME`: the name of an existing VM that specifies a placement policy.

     * `FILE_PATH`: the path to the YAML file that you created in the previous step.

     * `ZONE`: the zone where the VM is located.

  3. In the YAML configuration file, edit the value of the `resourcePolicies` field to specify a different placement policy.
         
         resourcePolicies:
         - https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where the placement policy is located. You can only specify a placement policy that is located in the same project as the VM.

     * `REGION`: the region where the placement policy is located.

     * `POLICY_NAME`: the name of the placement policy.

**Tip:** To avoid getting an error such as `"ERROR: (gcloud.compute.instances.update-from-file) Cannot parse YAML: [Expected type  for field value, found True (type )]"`, add quotes (`' '`) around any label values of `yes` or `no` in the exported instance configuration file. This indicates the values are strings, not Boolean values.
  4. To update the VM and restart it, use the [`gcloud compute instances update-from-file` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file) with the `--most-disruptive-allowed-action` flag set to `RESTART`.
         
         gcloud compute instances update-from-file VM_NAME \
             --most-disruptive-allowed-action=RESTART \
             --source=YAML_FILE \
             --zone=ZONE
         

Replace the following:

     * `VM_NAME`: the name of the VM.

     * `YAML_FILE`: the path to the YAML file with the configuration data that you modified in the previous step.

     * `ZONE`: the zone where the VM is located.




###  REST 

  1. Create an empty JSON file.

  2. To view the properties of an existing VM, make a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get).
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where the VM is located.

     * `ZONE`: the zone where the VM is located.

     * `VM_NAME`: the name of an existing VM that specifies a placement policy.

  3. In the empty JSON file that you created in the previous steps, do the following:

     1. Enter the VM properties from the `GET` request output.

     2. Locate the `resourcePolicies` field, and then edit its value to specify a different placement policy.
            
            "resourcePolicies": [
              "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
            ]
            

Replace the following:

        * `PROJECT_ID`: the ID of the project where the placement policy is located. You can only specify a placement policy that is located in the same project as the VM.

        * `REGION`: the region where the placement policy is located.

        * `POLICY_NAME`: the name of the placement policy.

  4. To update the VM and restart it, make a `PUT` request to the [`instances.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/update). In the request, do the following:

     * In the request URL, include the `most_disruptive_allowed_action` query parameter set to `RESTART`.

     * For the request body, use the VM configuration details from the JSON file that you created and updated in the previous steps.
    
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME?most_disruptive_allowed_action=RESTART
    
    {
      ...
      "resourcePolicies": [
        "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
      ],
      ...
    }
    




For more information about updating the properties of a VM, see [Update VM properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties#update).

## Remove a placement policy from a VM

If you want to remove a spread placement policy with two or more availability domains from a VM, then you can do so without stopping the VM. If you want to remove a compact placement policy or a spread placement policy with only one availability domain, then you must first [stop the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm) before removing the placement policy attached to it.

Removing a placement policy from a VM doesn't affect its physical location. However, if the VM is live migrating, Compute Engine might move the VM to a different physical location.

To remove a placement policy from a VM, select one of the following options:

###  gcloud 

To remove a placement policy from a VM, use the [`gcloud compute instances remove-resource-policies` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/remove-resource-policies).
    
    
    gcloud compute instances remove-resource-policies VM_NAME \
        --resource-policies=POLICY_NAME \
        --zone=ZONE
    

Replace the following:

  * `VM_NAME`: the name of an existing VM that specifies a placement policy.

  * `POLICY_NAME`: the name of the placement policy applied to the VM. To verify the name of the placement policy, [view the details of the VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-details) and check the value of the `resourcePolicies` field.

  * `ZONE`: the zone where the VM is located.




###  REST 

To remove a placement policy from a VM, make a `POST` request to the [`instances.removeResourcePolicies` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/removeResourcePolicies).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/removeResourcePolicies
    
    {
      "resourcePolicies": [
        "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the VM is located.

  * `ZONE`: the zone where the VM is located.

  * `VM_NAME`: the name of an existing VM that specifies a placement policy.

  * `REGION`: the region where the placement policy is located.

  * `POLICY_NAME`: the name of the placement policy applied to the VM. To verify the name of the placement policy, [view the details of the VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-details) and check the value of the `resourcePolicies` field.




## Delete a placement policy

You can only delete a placement policy if it's not applied to _any_ Compute Engine resource. Otherwise, deleting the placement policy fails. If you want to delete a placement policy that is applied to one or more Compute Engine resources, then do one of the following:

  * If the policy is applied to VMs only and you want to keep the VMs, do the following:

    1. Remove the placement policy from the VMs as described in this document.

    2. Delete the placement policy as described in this section.

  * Otherwise, do the following:

    1. Optional: Remove the placement policy from any VM you want to keep as described in this document.

    2. Delete _every_ other Compute Engine resource the placement policy is applied to in the following order:

       1. VMs

       2. Reservations

       3. Instance templates

    3. Delete the placement policy as described in this section.




To delete a placement policy, select one of the following options:

###  gcloud 

To delete a placement policy, use the [`gcloud compute resource-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/delete).
    
    
    gcloud compute resource-policies delete POLICY_NAME \
        --region=REGION
    

Replace the following:

  * `POLICY_NAME`: the name of an existing placement policy.

  * `REGION`: the region where the placement policy is located.




###  REST 

To delete a placement policy, make a `DELETE` request to the [`resourcePolicies.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/delete).
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the placement policy is located.

  * `REGION`: the region where the placement policy is located.

  * `POLICY_NAME`: the name of an existing placement policy.




## What's next?

  * Learn how to [view placement policies](https://docs.cloud.google.com/compute/docs/instances/view-placement-policies).

  * Learn how to do the following with a VM that specifies a placement policy:

    * [View the status of the VM](https://docs.cloud.google.com/compute/docs/instances/checking-instance-status).

    * [Connect to the VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
