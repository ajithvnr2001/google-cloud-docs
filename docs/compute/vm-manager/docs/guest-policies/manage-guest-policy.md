---
url: https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/manage-guest-policy/
title: Managing guest policies (legacy) \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:22.116261+00:00
---

# Managing guest policies (legacy)  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/manage-guest-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  Managing guest policies (legacy) Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This page includes instructions about the legacy OS guest policies. A later version of OS configuration management is now [Generally Available (GA)](https://cloud.google.com/products/#product-launch-stages). To use the later GA version, see [Managing OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/manage-os-policy). 

To view a comparison of the two versions, see [Comparing OS configuration management versions](https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/comparing_policy_options). 

After you [create a guest policy](https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/create-guest-policy), you can use the following procedures to review and manage your policies:

  * Update guest policies: modify your guest policy configurations.
  * Describe guest policies: get details about a specific guest policy.
  * List guest policies: view a list of guest policies in a project.
  * Delete a guest: delete a specific guest policy.
  * View configurations for a VM instance: view configurations that are applied to a VM instance.
  * Debug a guest policy: troubleshoot a guest policy.



Since the OS Config agent runs every 10-15 minutes, when you set up a update or deletion of a policy it will take roughly 10-15 minutes to take effect.

You can manage your guest policies using either the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute) or [REST](https://docs.cloud.google.com/compute/docs/osconfig/rest).

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Before you begin

  * Review [OS Config quotas](https://docs.cloud.google.com/compute/vm-manager/docs/os-config-quotas).
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




## Updating guest policies

To update a guest policy, complete the following steps:

  1. Update the YAML or JSON file.
  2. Run an update or patch command. The update process is similar to the create process with the addition of support for [etags](https://tools.ietf.org/html/rfc7232#section-2.3) that allow for concurrency and consistency control.



###  gcloud 

Use the [`os-config guest-policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/os-config/guest-policies/update) command to update a guest policy.
    
    
    gcloud beta compute os-config guest-policies update POLICY_ID \
         --file=FILE
    

Replace the following:

  * `POLICY_ID`: the name of the guest policy that you want to update.
  * `FILE`: the JSON or YAML file that contains the updated guest policy specifications.



###  REST 

In the API, create a `PATCH` request to the [`projects.guestPolicies.patch`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies/patch) method.
    
    
    PATCH https://osconfig.googleapis.com/v1beta/projects/PROJECT_ID/guestPolicies/POLICY_ID
    
    {
      For more information, see [Guest policy JSON](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#GuestPolicy)
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `POLICY_ID`: the name of your guest policy.



## Describing a guest policy

###  gcloud 

To view details about a guest policy, use the [`os-config guest-policies describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/os-config/guest-policies/describe) command. Replace `POLICY_ID` with the name of the guest policy that you want to describe.
    
    
    gcloud beta compute os-config guest-policies describe POLICY_ID
    

###  REST 

In the API, create a `GET` request to the [`projects.guestPolicies.get`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies/get) method.
    
    
    GET https://osconfig.googleapis.com/v1beta/projects/PROJECT_ID/guestPolicies/POLICY_ID
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `POLICY_ID`: the name of your guest policy.



## List guest policies

###  gcloud 

To view a list of guest policies in your project, use the [`os-config guest-policies list`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/os-config/guest-policies/list) command.
    
    
    gcloud beta compute os-config guest-policies list
    

###  REST 

In the API, create a `GET` request to the [`projects.guestPolicies.list`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies/list) method. Replace `PROJECT_ID` with your project ID.
    
    
    GET https://osconfig.googleapis.com/v1beta/projects/PROJECT_ID/guestPolicies
    

## Deleting guest policies

When the OS Config agent detects that a deletion of a guest policy is triggered, the current state of the system is maintained, but no further maintenance of the configuration is done. For example, say you have a guest policy `package-update-zone2b` set up that installs a package `my-package` on all VMs in zone `us-west2-b` and keeps the package `UPDATED`.

If you delete the `package-update-zone2b` policy, the following changes take place:

  * All VMs in `us-west2-b` that have `my-package` installed, keeps `my-package` installed. There is no reversion of the current system state.
  * On all future runs of the OS Config agent, after the policy deletion, the following takes place:

    * If a new VM is added to `us-west2-b`,`my-package` is not installed on this new VM.
    * For instances with `my-package` installed, the package is not updated.



###  gcloud 

To delete a guest policy, use the [`os-config guest-policies delete`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/os-config/guest-policies/delete) command. Replace `POLICY_ID` with the name of the guest policy that you want to delete.
    
    
    gcloud beta compute os-config guest-policies delete POLICY_ID
    

###  REST 

In the API, create a `DELETE` request to the [`projects.guestPolicies.delete`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies/delete) method.
    
    
    DELETE https://osconfig.googleapis.com/v1beta/projects/PROJECT_ID/guestPolicies/POLICY_ID
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `POLICY_ID`: the name of your guest policy.



## View configurations for a VM instance

###  gcloud 

To see the policies that are applied to a single VM instance, use the [`os-config guest-policies lookup`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/os-config/guest-policies/lookup) command.
    
    
    gcloud beta compute os-config guest-policies lookup VM_NAME \
        --zone=ZONE
    

Replace the following:

  * `VM_NAME`: the name of the VM instance.
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/zones) for the VM instance.



###  REST 

To see the policies that are applied to a single VM instance, use the following `POST` request.
    
    
    POST https://osconfig.googleapis.com/v1beta/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME:lookupEffectiveGuestPolicy
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/zones) for the VM instance.
  * `VM_NAME`: the name of your VM instance.



## Troubleshooting

### Inspect guest policies

You can use the Google Cloud console or Google Cloud CLI to inspect the guest policies associated with your project.

###  Console 

  1. In the Google Cloud console, go to the **OS Guest Policies** page.

[Go to the OS Guest Policies page](https://console.cloud.google.com/security/agent/deployment/policies)

  2. Select the guest policy that you want to inspect, and then click **VIEW DETAILS**.




###  gcloud 

  1. Use the [`os-config guest-policies list`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/os-config/guest-policies/list) command to list all your guest policies.
         
         gcloud beta compute os-config guest-policies list
         

  2. From the list of guest policies, copy the IDs of the guest policies you would like to inspect, and then run the command to inspect each of the guest policies. Replace `POLICY_ID` with the policy ID that you want to review.
         
         gcloud beta compute os-config guest-policies describe POLICY_ID
         




### Inspect guest policies for a specific VM

You can run the `lookup` command for a given VM to see which configurations apply to that VM.

In cases where a VM does not seem to be applying the requirements of the expected guest policy, it is useful to inspect the list of guest policies whose assignments include that specific VM instance. This helps to determine if the `Assignment` field in the guest policy matches this particular VM.

Use the [`os-config guest-policies lookup` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/os-config/guest-policies/lookup) to list the guest policies that might be targeting a particular VM. Replace `VM_NAME` with the name of the VM to inspect.
    
    
    gcloud beta compute os-config guest-policies lookup VM_NAME
    

For more information, see Viewing configurations for a VM instance.

The output from the command might reveal that the VM is not actually targeted in the VM assignment properties of the guest policy. For example, it might not be listed in the list of `Labels` or the list of VM name prefixes.

### Recovering from failure

A failed software recipe installation is not retried. This is because the system doesn't know the state in which the failed software recipe left things.

When debugging failed software recipes, we recommend the following steps:

  1. Rename the software recipe.
  2. Delete and recreate the guest policy using the renamed software recipe.



For more troubleshooting steps, see [Troubleshooting VM Manager](https://docs.cloud.google.com/compute/docs/troubleshooting/vm-manager/troubleshoot-vm-manager).

## What's next?

  * Learn more about the [OS guest policies (legacy)](https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies).
  * [Set up a guest policy](https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/create-guest-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
