---
url: https://docs.cloud.google.com/compute/docs/instances/change-service-account/
title: Change the attached service account \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:57.391519+00:00
---

# Change the attached service account  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/change-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Change the attached service account Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to configure an existing virtual machine (VM) to use a different service account. A service account is a special kind of account typically used by an application or compute workload to make authorized API calls.

Service accounts are needed for scenarios where a workload, such as a custom application, needs to access Google Cloud resources or perform actions without end-user involvement. For more information about when to use service accounts, see [Best practices for using service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts). 

If you have applications that need to make calls to Google Cloud APIs, Google recommends that you attach a user-managed service account to the VM on which the application or workload is running. Then, you grant the service account IAM roles, which gives the service account–and, by extension, applications running on the VM–access to Google Cloud resources.

**Note:** When a user connects to a VM, that user can use all of the IAM permissions granted to the service account attached to the VM. 

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




### Required roles

To get the permissions that you need to configure service accounts on your VM, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the VM or your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to configure service accounts on your VM. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure service accounts on your VM:

  * `compute.instances.setServiceAccount`
  * `compute.instances.stop`
  * `compute.instances.start`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Overview

It is recommended that you configure service accounts for your VMs as follows:

  1. Create a new user-managed service account rather than using the Compute Engine default service account, and grant IAM roles to that service account for only the resources and operations that it needs. 
  2. Attach the service account to your VM.
  3. Set the cloud platform (`https://www.googleapis.com/auth/cloud-platform`) scope on your VM. This allows the VM's service account to call the Google Cloud APIs that it has permission to use. 
     * If you specify the service account by using the Google Cloud console, set the service account's access scope to **Allow full access to all Cloud APIs**.
     * If you specify the service account by using the Google Cloud CLI or Compute Engine API, you can use the `scopes` parameter to set the access scope.



## Set up the service account

You can either create a user-managed service account or use the Compute Engine default service account. A user-managed service account is recommended.

For the selected service account, ensure that the required Identity and Access Management (IAM) roles are assigned.

###  User-managed 

If you don't already have a user-managed service account, create a service account. For detailed instruction, see [Set up a service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#createanewserviceaccount).

###  Default 

If you are familiar with the Compute Engine default service account and want to use the credentials provided by the default service account instead of creating new service accounts, you can grant IAM roles to the default service account.

Before you assign IAM roles to the default service account, note that:

  * Granting an IAM role to the default service account affects all VMs that are running as the default service account. For example, if you grant the default service account the `roles/storage.objectAdmin` role, all VMs running as the default service account with the required access scopes will have permissions granted by the `roles/storage.objectAdmin` role. Likewise, if you limit access by omitting certain roles, this affects all VMs running as the default service account.

  * Depending on your organization policy configuration, the default service account might automatically be granted the [Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) on your project. We strongly recommend that you disable the automatic role grant by [ enforcing the `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants). If you created your organization after May 3, 2024, this constraint is enforced by default. 

If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




If you are unsure about granting IAM roles to the default service account, _create a new user-managed service account_ instead.

**Caution:** If you have existing VMs that use the default service account, modifying the default service account's roles will prevent those VMs from accessing some resources.

## Attach the service account and update the access scope

To change a VM's service account and access scopes, you must first stop the VM. After you make the necessary changes, you can restart the VM.

**Note:** When updating a VM instance, you might encounter a `Supplied fingerprint does not match current metadata fingerprint` error. This issue can happen if the VM's metadata was updated by another process since you last refreshed the page. For a detailed explanation and workaround, see [Troubleshoot VM updates](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-update).

If the service account you want to attach to the VM is in a different project than the VM, you must [configure the service account for a resource in a different project](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts).

Use one of the following methods to change the service account and access scopes on your VM.

###  Console 

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the VM instance name for which you want to change the service account.

  3. Click stop **Stop**. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**. Wait for the VM to be stopped.

  4. Click **Edit**.

  5. Scroll down to the **Service Account** section.

  6. From the drop-down list, select the service account to assign to the VM.

     * If you choose a user-managed service account, the VM's access scope defaults to the recommended `cloud-platform` scope. If you need a different scope for your user-managed service account, use the gcloud CLI or Compute Engine API to attach the service account.
     * If you choose the Compute Engine default service account, you can modify its access scopes in the Google Cloud console. 
       * To change scopes, in the **Access scopes** section, select **Set access for each API** and set the appropriate scopes for your needs.
       * **Recommended** If you're not sure of the proper access scopes to set, choose **Allow full access to all Cloud APIs** and then make sure to restrict access by setting IAM roles on the service account.
  7. Click **Save** to save your changes.

  8. Click **Start/Resume** to restart the VM.




###  gcloud 

  1. Stop the VM by using the [`instances stop` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop). Replace `VM_NAME` with the name of your VM instance.
         
         gcloud compute instances stop VM_NAME
         

  2. Attach the service account. To attach the service account, use the [`instances set-service-account` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-service-account) and provide the VM name, the service account email, and the desired scopes. For more information about setting access scopes, see Best practices.
         
         gcloud compute instances set-service-account VM_NAME \
           --service-account=SERVICE_ACCOUNT_EMAIL \
           --scopes=SCOPES
         

Replace the following:

     * `SERVICE_ACCOUNT_EMAIL`: the email address for the service account that you created. For example: `my-sa-123@my-project-123.iam.gserviceaccount.com`. To view the email address, see [Listing service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-list-edit#listing).

If you want to remove the service account from the VM, use the `--no-service-account` flag.

     * `VM_NAME`: the name of the VM instance.

     * `SCOPES`: a comma-separated list of [scope URIs or aliases](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--scopes) provided in the description for the `--scopes` flag.

If you want to remove all scopes for the VM, use the `--no-scopes` flag instead.

For example, the following command assigns the service account `my-sa-123@my-project-123.iam.gserviceaccount.com` to a VM called example-instance and sets access scopes on that VM to allow read/write access to Compute Engine and read-only access to Cloud Storage:
    
    gcloud compute instances set-service-account example-instance \
      --service-account=my-sa-123@my-project-123.iam.gserviceaccount.com \
      --scopes=compute-rw,storage-ro
    

  3. Start the VM by using the [`instances start` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/start). Replace `VM_NAME` with the name of your VM instance.
         
         gcloud compute instances start VM_NAME
         




###  REST 

  1. Stop the VM by making a `POST` request using the [`instances.stop` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/stop):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/stop
         

Replace the following:

     * `PROJECT_ID`: the project your VM is in
     * `ZONE`: the zone where your VM is located
     * `VM_NAME`: the name of the VM you want to stop
  2. Attach the service account by making a `POST` request to the [`setServiceAccount` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/setServiceAccount):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setServiceAccount
         
         {
           "email": "SERVICE_ACCOUNT_EMAIL",
           "scopes": [
             "SCOPE_URI",
             "SCOPE_URI",
             ...
           ]
         }
         

Replace the following:

     * `PROJECT_ID`: the project ID for this request.
     * `ZONE`: the zone where this VM belongs to.
     * `VM_NAME`: the name of the VM.
     * `SERVICE_ACCOUNT_EMAIL`: the email address for the service account that you created. For example: `my-sa-123@my-project-123.iam.gserviceaccount.com`. To view the email address, see [Listing service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-list-edit#listing).
     * `SCOPE_URI`: the required [scope URI](https://developers.google.com/identity/protocols/oauth2/scopes).

For example, the following request uses the service account email `my-sa-123@my-project-123.iam.gserviceaccount.com` and sets a Cloud Storage and BigQuery scope:
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setServiceAccount
    
    {
      "email": "my-sa-123@my-project-123.iam.gserviceaccount.com",
      "scopes": [
        "https://www.googleapis.com/auth/bigquery",
        "https://www.googleapis.com/auth/devstorage.read_only"
      ]
    }
    

  3. Start the VM by constructing a `POST` request using the [`instances.start` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/start):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/start
         

Replace the following:

     * `PROJECT_ID`: the project your VM is in
     * `ZONE`: the zone where your VM is located
     * `VM_NAME`: the name of the VM you want to start



## View the service account that is used by a VM

To view all the service accounts in a project, see [Listing service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-list-edit#listing).

If you need to identify the service account that is being used by a VM, complete one of the following procedures:

###  console 

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the VM instance name for which you want to change the service account.

  3. Go to the **API and identity management** section. This sections displays the service account and access scope that is used by the VM.




###  gcloud 

Run the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe):
    
    
    gcloud compute instances describe VM_NAME \
        --format json
    

The output is similar to the following:
    
    
    {
      ...
      "serviceAccounts":[
          {
            "email":"123845678986-compute@developer.gserviceaccount.com",
            "scopes":[
                "https://www.googleapis.com/auth/devstorage.full_control"
            ]
          }
      ]
      ...
       }
    

If the VM isn't using a service account, you receive a response without the `serviceAccounts` property.

###  Metadata Server 

Query the [metadata server](https://docs.cloud.google.com/compute/docs/metadata) from within the VM itself. Make a request to `http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/`:
    
    
    user@myinst:~$ curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/" \
    -H "Metadata-Flavor: Google"
    

If you enabled one or more service accounts when you created the instance, this `curl` command returns output similar to the following:
    
    
    123845678986-compute@developer.gserviceaccount.com/
    default/
    

If the instance isn't using a service account, you receive an empty response.

## Best practices

  * [Limit the privileges of service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#limiting_service_account_privileges) and regularly check your service account permissions to make sure they are up-to-date.
  * Delete service accounts with caution. Make sure your critical applications are no longer using a service account before deleting it. If you're not sure whether a service account is being used, we recommend [disabling the service account](https://docs.cloud.google.com/iam/docs/service-accounts-disable-enable#disabling) instead of deleting it. Disabled service accounts can be re-enabled if they are still needed.
  * Mitigate the security risks for your service account. For more information, see [Best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).



## What's next?

  * Review [Service account best practices](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts)
  * Review [Authenticate workloads using service accounts](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
