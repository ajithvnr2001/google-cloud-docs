---
url: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/view-edit-policy-orchestrator/
title: View, edit, and delete policy orchestrators \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:20.209035+00:00
---

# View, edit, and delete policy orchestrators  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/view-edit-policy-orchestrator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  View, edit, and delete policy orchestrators Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view and delete policy orchestrators in your folders or organization.

## Before you begin

  * Review [OS policy and OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies).
  * Review [OS Config quotas](https://docs.cloud.google.com/compute/vm-manager/docs/os-config-quotas).
  * Ensure that you meet the [prerequisites](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites) for using policy orchestrator.
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




## List OS policy orchestrators

To view all policy orchestrators in a project, folder or organization, complete the following steps:

###  Project 

###  Console 

To list policy orchestrators, do the following:

  1. In the Google Cloud console, go to the **OS policies** page.

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  2. Click the **Project Selector** on the Google Cloud console action bar and select the project in which you want to view policy orchestrators.

  3. Click **Global orchestrators**.




###  gcloud 

To view details of policy orchestrators that were created in a project, run the [`os-config policy-orchestrators list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/list):
    
    
        gcloud compute os-config policy-orchestrators list
    

###  REST 

To view all policy orchestrators in a project, send a `GET` request to the [`projects.locations.global.policyOrchestrators.list` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.global.policyOrchestrators/list):
    
    
      GET https://osconfig.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/policyOrchestrators
    

Replace `PROJECT_NUMBER` with the numeric ID of the project in which you created the policy orchestrators.

###  Folder 

###  Console 

To list policy orchestrators, do the following:

  1. In the Google Cloud console, go to the **OS policies** page.

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  2. Click the **Project Selector** on the Google Cloud console action bar and select the folder in which you want to view policy orchestrators.

  3. Click **Global orchestrators**.




###  gcloud 

To view details of policy orchestrators that were created in a folder, run the [`os-config policy-orchestrators list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/list):
    
    
        gcloud --billing-project=QUOTA_PROJECT_ID compute os-config policy-orchestrators list \
          --folder=FOLDER_NUMBER
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of the [quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
  * `FOLDER_NUMBER`: the numeric ID of the folder in which you created the policy orchestrators.

**Example**
        
        gcloud --billing-project=my-quota-project compute os-config policy-orchestrators list \
          --folder=123456
        




###  REST 

To view all policy orchestrators in a folder, send a `GET` request to the [`folders.locations.global.policyOrchestrators.list` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators/list):
    
    
      GET https://osconfig.googleapis.com/v2/folders/FOLDER_NUMBER/locations/global/policyOrchestrators
      -H "x-goog-user-project: QUOTA_PROJECT_ID"
    

Replace `FOLDER_NUMBER` with the numeric ID of the folder in which you created the policy orchestrators.

###  Organization 

###  Console 

To list policy orchestrators, do the following:

  1. In the Google Cloud console, go to the **OS policies** page.

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  2. Click the **Project Selector** on the Google Cloud console action bar and select the organization in which you want to view policy orchestrators.

  3. Click **Global orchestrators**.




###  gcloud 

To view details of policy orchestrators that were created in an organization, run the [`os-config policy-orchestrators list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/list):
    
    
        gcloud --billing-project=QUOTA_PROJECT_ID compute os-config policy-orchestrators list \
          --organization=ORGANIZATION_NUMBER
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of the [quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
  * `ORGANIZATION_NUMBER`: the numeric ID of the organization in which you created the policy orchestrators.

**Example**
        
        gcloud --billing-project=my-quota-project compute os-config policy-orchestrators list \
          --organization=123456
        




###  REST 

To view all policy orchestrators in an organization, send a `GET` request to the [`organizations.locations.global.policyOrchestrators.list` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators/list):
    
    
      GET https://osconfig.googleapis.com/v2/organizations/ORGANIZATION_NUMBER/locations/global/policyOrchestrators
      -H "x-goog-user-project: QUOTA_PROJECT_ID"
    

Replace `ORGANIZATION_NUMBER` with the numeric ID of the organization in which you created the policy orchestrators.

## View details of a policy orchestrator

To view details of a policy orchestrator in a project, folder, or organization, complete the following steps:

###  Project 

###  Console 

To view a policy orchestrator, do the following:

  1. In the Google Cloud console, go to the **OS policies** page.

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  2. Click the **Project Selector** on the Google Cloud console action bar and then select the project that contains the policy orchestrator.

  3. Click **Global orchestrators**.

  4. Select the name of the policy orchestrator that you want to view. The **Orchestrator details** page opens.

  5. To view details of the OS policies applied to VMs, go to the **Assigned OS policies** section and then click **View**.




###  gcloud 

To view details of a policy orchestrator that was created in a project, run the [`os-config policy-orchestrators describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/describe):
    
    
      gcloud compute os-config policy-orchestrators describe ORCHESTRATOR_NAME
    

Replace `ORCHESTRATOR_NAME` with the name for the policy orchestrator.

**Example**
    
    
        gcloud compute os-config policy-orchestrators describe my-os-policy-orchestrator
     

###  REST 

To view details of a policy orchestrator, send a `GET` request to the [`projects.locations.global.policyOrchestrators.get` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.global.policyOrchestrators/get),
    
    
      GET https://osconfig.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/policyOrchestrators/ORCHESTRATOR_NAME
    

Replace the following:

  * `PROJECT_NUMBER`: the numeric ID of the project in which the policy orchestrator exists.
  * `ORCHESTRATOR_NAME`: the name of the policy orchestrator that you want to view.



The request body must be empty.

###  Folder 

###  Console 

To view a policy orchestrator, do the following:

  1. In the Google Cloud console, go to the **OS policies** page.

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  2. Click the **Project Selector** on the Google Cloud console action bar and then select the folder that contains the policy orchestrator.

  3. Click **Global orchestrators**.

  4. Select the name of the policy orchestrator that you want to view. The **Orchestrator details** page opens.

  5. To view details of the OS policies applied to VMs, go to the **Assigned OS policies** section and then click **View**.




###  gcloud 

To view details of a policy orchestrator that was created in a folder, run the [`os-config policy-orchestrators describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/describe):
    
    
      gcloud --billing-project=QUOTA_PROJECT_ID compute os-config policy-orchestrators describe ORCHESTRATOR_NAME \
        --folder=FOLDER_NUMBER
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of the [quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
  * `ORCHESTRATOR_NAME`: name for the policy orchestrator.
  * `FOLDER_NUMBER`: the numeric ID of the folder in which you created the policy orchestrator.

**Example**
        
        gcloud --billing-project=my-quota-project compute os-config policy-orchestrators describe my-os-policy-orchestrator \
            --folder=123456
        




###  REST 

To view details of a policy orchestrator, send a `GET` request to the [`folders.locations.global.policyOrchestrators.get` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators/get),
    
    
      GET https://osconfig.googleapis.com/v2/folders/FOLDER_NUMBER/locations/global/policyOrchestrators/ORCHESTRATOR_NAME
      -H "x-goog-user-project: QUOTA_PROJECT_ID"
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of the [quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
  * `FOLDER_NUMBER`: the numeric ID of the folder in which the policy orchestrator exists.
  * `ORCHESTRATOR_NAME`: the name of the policy orchestrator that you want to view.



The request body must be empty.

###  Organization 

###  Console 

To view a policy orchestrator, do the following:

  1. In the Google Cloud console, go to the **OS policies** page.

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  2. Click the **Project Selector** on the Google Cloud console action bar and then select the organization that contains the policy orchestrator.

  3. Click **Global orchestrators**.

  4. Select the name of the policy orchestrator that you want to view. The **Orchestrator details** page opens.

  5. To view details of the OS policies applied to VMs, go to the **Assigned OS policies** section and then click **View**.




###  gcloud 

To view details of a policy orchestrator that was created in an organization, run the [`os-config policy-orchestrators describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/describe):
    
    
      gcloud --billing-project=QUOTA_PROJECT_ID compute os-config policy-orchestrators describe ORCHESTRATOR_NAME \
        --organization=ORGANIZATION_NUMBER
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of the [quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
  * `ORCHESTRATOR_NAME`: name for the policy orchestrator.
  * `ORGANIZATION_NUMBER`: the numeric ID of the organization in which you created the policy orchestrator.

**Example**
        
        gcloud --billing-project=my-quota-project compute os-config policy-orchestrators describe my-os-policy-orchestrator \
            --organization=123456
        




###  REST 

To view details of a policy orchestrator, send a `GET` request to the [`organizations.locations.global.policyOrchestrators.get` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators/get),
    
    
      GET https://osconfig.googleapis.com/v2/organizations/ORGANIZATION_NUMBER/locations/global/policyOrchestrators/ORCHESTRATOR_NAME
      -H "x-goog-user-project: QUOTA_PROJECT_ID"
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of the [quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
  * `ORGANIZATION_NUMBER`: the numeric ID of the organization in which the policy orchestrator exists.
  * `ORCHESTRATOR_NAME`: the name of the policy orchestrator that you want to view.



The request body must be empty.

## Edit OS policy orchestrators

You can modify policy orchestrators to add or update the OS policy assignments, orchestrator scope and resources.

###  Project 

###  Console 

To change the settings of a policy orchestrator, do the following:

  1. In the Google Cloud console, go to the **OS policies** page.

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  2. Click the **Project Selector** on the Google Cloud console action bar and select the project in which the policy orchestrator exists.

  3. Click **Global orchestrators**.

  4. Select the name of the policy orchestrator that you want to edit. The **Orchestrator details** page opens.

  5. Click **Edit**.

  6. In the **OS policies** section, upload the OS policy file.

  7. Optional: In the **State** section, select one of the following options to specify the behaviour of the policy orchestrator:

     * `ACTIVE`: Once created, the policy orchestrator takes actions immediately.
     * `STOPPED`: A policy orchestrator is created in this state does not take any actions immediately. You can edit the policy orchestrator later to change its state.
  8. In the **Orchestration scope** section, specify the folders and projects in which you want to roll out the OS policies. You must enter only the project numbers and folder numbers in these fields. For example, 123456, 7654321.

  9. Optional: Select the zones that contain the VMs that you want to apply the OS policies to.

  10. Optional: In the **Target VM instances** section, specify the target VMs That you want to apply the OS policies to.

     * Select the OS families.
     * You can further filter the VMs by specifying include and exclude labels.

For example, you can select all the Ubuntu VMs in your test environment, and exclude those that are running Google Kubernetes Engine, by specifying the following: 

       * OS short name: `ubuntu`
       * Include: `env:test`, `env:staging`
       * Exclude: `goog-gke-node`
  11. Specify a rollout plan.

     * Specify the wave size (also referred to as the disruption budget). For example, 10%.
     * Specify the wait time. For example, 15 minutes.
  12. Click **Save**.




###  gcloud 

To update a policy orchestrator, use the [`os-config policy-orchestrators update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update).
    
    
       gcloud compute os-config policy-orchestrators update ORCHESTRATOR_NAME \
       --state=stopped
    

Replace `ORCHESTRATOR_NAME` with the name for the policy orchestrator.
    
    
    **Example**
    
    <pre class="devsite-click-to-copy">
      gcloud compute os-config policy-orchestrators update my-os-policy-orchestrator \
        --include-projects=5432134,4567890
    </pre>
    

###  REST 

To update a policy orchestrator in a project, send a `PATCH` request to the [`projects.locations.global.policyOrchestrators.patch` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.global.policyOrchestrators/patch).

In the request body, edit the OS policy assignment specifications.
    
    
          PATCH https://osconfig.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/policyOrchestrators/ORCHESTRATOR_NAME
    
            {
              JSON_OS_POLICY_ORCHESTRATOR
            }
    

Replace the following:

  * `PROJECT_NUMBER`: the numeric ID of the project in which the policy orchestrator exists.
  * `ORCHESTRATOR_NAME`: the name of the policy orchestrator that you want to edit.
  * `JSON_OS_POLICY_ORCHESTRATOR`: the policy orchestrator object in JSON format that defines the orchestrator scope, orchestrated resource, and orchestration state. For more information about the parameters and format, see [`Resource: projects.locations.global.policyOrchestrators`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.global.policyOrchestrators#PolicyOrchestrator).



###  Folder 

###  Console 

To change the settings of a policy orchestrator, do the following:

  1. In the Google Cloud console, go to the **OS policies** page.

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  2. Click the **Project Selector** on the Google Cloud console action bar and select the folder in which the policy orchestrator exists.

  3. Click **Global orchestrators**.

  4. Select the name of the policy orchestrator that you want to edit. The **Orchestrator details** page opens.

  5. Click **Edit**.

  6. In the **OS policies** section, upload the OS policy file.

  7. Optional: In the **State** section, select one of the following options to specify the behaviour of the policy orchestrator:

     * `ACTIVE`: Once created, the policy orchestrator takes actions immediately.
     * `STOPPED`: A policy orchestrator is created in this state does not take any actions immediately. You can edit the policy orchestrator later to change its state.
  8. In the **Orchestration scope** section, specify the folders and projects in which you want to roll out the OS policies. You must enter only the project numbers and folder numbers in these fields. For example, 123456, 7654321.

  9. Optional: Select the zones that contain the VMs that you want to apply the OS policies to.

  10. Optional: In the **Target VM instances** section, specify the target VMs That you want to apply the OS policies to.

     * Select the OS families.
     * You can further filter the VMs by specifying include and exclude labels.

For example, you can select all the Ubuntu VMs in your test environment, and exclude those that are running Google Kubernetes Engine, by specifying the following: 

       * OS short name: `ubuntu`
       * Include: `env:test`, `env:staging`
       * Exclude: `goog-gke-node`
  11. Specify a rollout plan.

     * Specify the wave size (also referred to as the disruption budget). For example, 10%.
     * Specify the wait time. For example, 15 minutes.
  12. Click **Save**.




###  gcloud 

To update a policy orchestrator, use the [`os-config policy-orchestrators update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update).
    
    
       gcloud --billing-project=QUOTA_PROJECT_ID compute os-config policy-orchestrators update ORCHESTRATOR_NAME \
       --folder=FOLDER_NUMBER
       --state=stopped
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of the [quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
  * `ORCHESTRATOR_NAME`: name for the policy orchestrator.
  * `FOLDER_NUMBER`: the numeric folder ID of the folder in which the policy orchestrator exists.

**Example**
        
        gcloud --billing-project=my-quota-project compute os-config policy-orchestrators update my-os-policy-orchestrator \
            --folder=123456 \
            --include-projects=5432134,4567890
        




###  REST 

To update a policy orchestrator in a folder, send a `PATCH` request to the [`folders.locations.global.policyOrchestrators.patch` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators/patch).

In the request body, edit the OS policy assignment specifications.
    
    
          PATCH https://osconfig.googleapis.com/v2/folders/FOLDER_NUMBER/locations/global/policyOrchestrators/ORCHESTRATOR_NAME
          -H "x-goog-user-project: QUOTA_PROJECT_ID"
    
            {
              JSON_OS_POLICY_ORCHESTRATOR
            }
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of the [quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project)
  * `FOLDER_NUMBER`: the numeric ID of the folder in which the policy orchestrator exists.
  * `ORCHESTRATOR_NAME`: the name of the policy orchestrator that you want to edit.
  * `JSON_OS_POLICY_ORCHESTRATOR`: the policy orchestrator object in JSON format that defines the orchestrator scope, orchestrated resource, and orchestration state. For more information about the parameters and format, see [`Resource: folders.locations.global.policyOrchestrators`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators#PolicyOrchestrator).



###  Organization 

###  Console 

To change the settings of a policy orchestrator, do the following:

  1. In the Google Cloud console, go to the **OS policies** page.

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  2. Click the **Project Selector** on the Google Cloud console action bar and select the organization in which the policy orchestrator exists.

  3. Click **Global orchestrators**.

  4. Select the name of the policy orchestrator that you want to edit. The **Orchestrator details** page opens.

  5. Click **Edit**.

  6. In the **OS policies** section, upload the OS policy file.

  7. Optional: In the **State** section, select one of the following options to specify the behaviour of the policy orchestrator:

     * `ACTIVE`: Once created, the policy orchestrator takes actions immediately.
     * `STOPPED`: A policy orchestrator is created in this state does not take any actions immediately. You can edit the policy orchestrator later to change its state.
  8. In the **Orchestration scope** section, specify the folders and projects in which you want to roll out the OS policies. You must enter only the project numbers and folder numbers in these fields. For example, 123456, 7654321.

  9. Optional: Select the zones that contain the VMs that you want to apply the OS policies to.

  10. Optional: In the **Target VM instances** section, specify the target VMs That you want to apply the OS policies to.

     * Select the OS families.
     * You can further filter the VMs by specifying include and exclude labels.

For example, you can select all the Ubuntu VMs in your test environment, and exclude those that are running Google Kubernetes Engine, by specifying the following: 

       * OS short name: `ubuntu`
       * Include: `env:test`, `env:staging`
       * Exclude: `goog-gke-node`
  11. Specify a rollout plan.

     * Specify the wave size (also referred to as the disruption budget). For example, 10%.
     * Specify the wait time. For example, 15 minutes.
  12. Click **Save**.




###  gcloud 

To update a policy orchestrator, use the [`os-config policy-orchestrators update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/update).
    
    
       gcloud --billing-project=QUOTA_PROJECT_ID compute os-config policy-orchestrators update ORCHESTRATOR_NAME \
       --organization=ORGANIZATION_NUMBER
       --state=stopped
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of the [quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
  * `ORCHESTRATOR_NAME`: name for the policy orchestrator.
  * `ORGANIZATION_NUMBER`: the numeric folder ID of the organization in which the policy orchestrator exists.

**Example**
        
        gcloud --billing-project=my-quota-project compute os-config policy-orchestrators update my-os-policy-orchestrator \
            --organization=123456 \
            --include-projects=5432134,4567890
        




###  REST 

To update a policy orchestrator in an organization, send a `PATCH` request to the [`organizations.locations.global.policyOrchestrators.patch` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators/patch).

In the request body, edit the OS policy assignment specifications.
    
    
          PATCH https://osconfig.googleapis.com/v2/organizations/ORGANIZATION_NUMBER/locations/global/policyOrchestrators/ORCHESTRATOR_NAME
          -H "x-goog-user-project: QUOTA_PROJECT_ID"
    
            {
              JSON_OS_POLICY_ORCHESTRATOR
            }
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of the [quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project)
  * `ORGANIZATION_NUMBER`: the numeric ID of the organization in which the policy orchestrator exists.
  * `ORCHESTRATOR_NAME`: the name of the policy orchestrator that you want to edit.
  * `JSON_OS_POLICY_ORCHESTRATOR`: the policy orchestrator object in JSON format that defines the orchestrator scope, orchestrated resource, and orchestration state. For more information about the parameters and format, see [`Resource: organizations.locations.global.policyOrchestrators`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators#PolicyOrchestrator).



## Delete a policy orchestrator

**Note:** Deleting a policy orchestrator only deletes the policy orchestrator resource from the specified scope, not the OS policy assignments it applied on the zonal resources. If you want to delete the OS policy assignments created by a policy orchestrator, first [edit the orchestrator](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/view-edit-policy-orchestrator#edit-orchestrator) and change its `action` to `delete`. After the orchestrator deletes the OS policy assignments, delete the orchestrator.

To delete a policy orchestrator and to cancel all ongoing rollouts, complete the following steps:

###  Project 

###  Console 

To delete a policy orchestrator, do the following:

  1. In the Google Cloud console, go to the **OS policies** page.

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  2. Click the **Project Selector** on the Google Cloud console action bar and select the project from which you want to delete the policy orchestrator.

  3. Click **Global orchestrators**.

  4. Select the name of the policy orchestrator that you want to delete. The **Orchestrator details** page opens.

  5. Click **Delete**.




###  gcloud 

To delete a policy orchestrator from a project, do the following:

  1. Use the [`os-config policy-orchestrators delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/delete):
         
         gcloud compute os-config policy-orchestrators delete ORCHESTRATOR_NAME
         

Replace `ORCHESTRATOR_NAME` with the name for the policy orchestrator.

**Example**
         
         gcloud compute os-config policy-orchestrators delete my-os-policy-orchestrator
           




###  REST 

To delete a policy orchestrator in a project, send a `DELETE` request to the [`projects.locations.global.policyOrchestrators.delete` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.global.policyOrchestrators/delete):
    
    
      DELETE https://osconfig.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/policyOrchestrators/ORCHESTRATOR_NAME
    

Replace the following:

  * `PROJECT_NUMBER`: the numeric ID of the project in which the policy orchestrator exists.
  * `ORCHESTRATOR_NAME`: the name of the policy orchestrator that you want to delete.



###  Folder 

###  Console 

To delete a policy orchestrator, do the following:

  1. In the Google Cloud console, go to the **OS policies** page.

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  2. Click the **Project Selector** on the Google Cloud console action bar and select the folder from which you want to delete the policy orchestrator.

  3. Click **Global orchestrators**.

  4. Select the name of the policy orchestrator that you want to delete. The **Orchestrator details** page opens.

  5. Click **Delete**.




###  gcloud 

To delete a policy orchestrator from a folder, do the following:

  1. Use the [`os-config policy-orchestrators delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/delete):
         
         gcloud --billing-project=QUOTA_PROJECT_ID compute os-config policy-orchestrators delete ORCHESTRATOR_NAME \
               --folder=FOLDER_NUMBER
         

Replace the following:

     * `QUOTA_PROJECT_ID`: the project ID of the [quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
     * `ORCHESTRATOR_NAME`: name for the policy orchestrator.
     * `FOLDER_NUMBER`: the numeric ID of the folder in which you created the policy orchestrator.

**Example**
           
           gcloud --billing-project=my-quota-project compute os-config policy-orchestrators delete my-os-policy-orchestrator \
             --folder=123456
           




###  REST 

To delete a policy orchestrator in a folder, send a `DELETE` request to the [`folders.locations.global.policyOrchestrators.delete` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators/delete):
    
    
      DELETE https://osconfig.googleapis.com/v2/folders/FOLDER_NUMBER/locations/global/policyOrchestrators/ORCHESTRATOR_NAME
      -H "x-goog-user-project: QUOTA_PROJECT_ID"
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of the [quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
  * `FOLDER_NUMBER`: the numeric ID of the folder in which the policy orchestrator exists.
  * `ORCHESTRATOR_NAME`: the name of the policy orchestrator that you want to delete.



###  Organization 

###  Console 

To delete a policy orchestrator, do the following:

  1. In the Google Cloud console, go to the **OS policies** page.

[Go to OS policies](https://console.cloud.google.com/compute/config/assignments/)

  2. Click the **Project Selector** on the Google Cloud console action bar and select the organization from which you want to delete the policy orchestrator.

  3. Click **Global orchestrators**.

  4. Select the name of the policy orchestrator that you want to delete. The **Orchestrator details** page opens.

  5. Click **Delete**.




###  gcloud 

To delete a policy orchestrator from an organization, do the following:

  1. Use the [`os-config policy-orchestrators delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/delete):
         
         gcloud --billing-project=QUOTA_PROJECT_ID compute os-config policy-orchestrators delete ORCHESTRATOR_NAME \
               --organization=ORGANIZATION_NUMBER
         

Replace the following:

     * `QUOTA_PROJECT_ID`: the project ID of the [quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
     * `ORCHESTRATOR_NAME`: name for the policy orchestrator.
     * `ORGANIZATION_NUMBER`: the numeric ID of the organization in which you created the policy orchestrator.

**Example**
           
           gcloud --billing-project=my-quota-project compute os-config policy-orchestrators delete my-os-policy-orchestrator \
             --organization=123456
           




###  REST 

To delete a policy orchestrator in an organization, send a `DELETE` request to the [`organizations.locations.global.policyOrchestrators.delete` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators/delete):
    
    
      DELETE https://osconfig.googleapis.com/v2/organizations/ORGANIZATION_NUMBER/locations/global/policyOrchestrators/ORCHESTRATOR_NAME
      -H "x-goog-user-project: QUOTA_PROJECT_ID"
    

Replace the following:

  * `QUOTA_PROJECT_ID`: the project ID of the [quota or the billing project](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/orchestrator-prerequisites#setup-quota-project).
  * `ORGANIZATION_NUMBER`: the numeric ID of the organization in which the policy orchestrator exists.
  * `ORCHESTRATOR_NAME`: the name of the policy orchestrator that you want to delete.



## What's next?

  * Learn how to [manage OS policy assignments using policy orchestrator](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/use-policy-orchestrator).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
