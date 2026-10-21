---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/validating-configs/
title: Validate configs \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:20:23.098431+00:00
---

# Validate configs  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/validating-configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Validate configs Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to validate configs with [Cloud Build](https://docs.cloud.google.com/build) when using Google Kubernetes Engine clusters. The same setup works in any other container-based CI/CD system, such as CircleCI, with minimal changes.

We recommend validating any configuration changes in your CI/CD pipeline in addition to checking the validity of your configs by running the [`nomos vet`](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#vet) command.

## Objectives

  * Create a Cloud Build config file that instructs Config Sync to use `nomos vet` on the configs in your repository.
  * Create a Cloud Build trigger so that your configs are checked whenever there's a change to the development branch.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Config Sync](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [ Cloud Build](https://docs.cloud.google.com/build/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com)

  8. Create, or have access to, a GKE cluster that meets the requirements for Config Sync. For details on how to create such a cluster, see [Get started with Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/tutorials/config-sync-multi-repo#create_a_cluster).



## Grant the Cloud Build service account permission

Grant the Cloud Build service account permission to access your GKE cluster.

### gcloud

To add the `Kubernetes Engine Developer` role to the Cloud Build service account, run the following command:
    
    
    PROJECT_ID=$(gcloud config get-value project)
    PROJECT_NUM=$(gcloud projects list --filter="$PROJECT_ID" --format="value(PROJECT_NUMBER)")
    gcloud projects add-iam-policy-binding $PROJECT_ID \
        --member=serviceAccount:$PROJECT_NUM@cloudbuild.gserviceaccount.com \
        --role=roles/container.developer
    

### Console

  1. Open the IAM page in Google Cloud console.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. In the **member** column find the row with the Cloud Build service account:
         
         PROJECT_NUMBER@cloudbuild.gserviceaccount.com
         

  3. In that row, click edit **Edit principal**.

  4. Click **Add another role**.

  5. In the **Select a role** list, select `Kubernetes Engine Developer`, and then click **Save**.




## Create a Cloud Build config

Create a [Cloud Build config](https://docs.cloud.google.com/build/docs/build-config) file and store it in the root directory of the repository containing your config files (for example, `my-repo/cloudbuild.yaml`).
    
    
    steps:
    - name: 'gcr.io/cloud-builders/kubectl'
      args: ['config', 'current-context']
      volumes:
      - name: 'kube'
        path: '/kube'
      env:
      - 'KUBECONFIG=/kube/config'
      - 'CLOUDSDK_COMPUTE_ZONE=ZONE'
      - 'CLOUDSDK_CONTAINER_CLUSTER=CLUSTER_NAME'
      - 'CLOUDSDK_CONTAINER_USE_APPLICATION_DEFAULT_CREDENTIALS=true'
    - name: 'bash'
      args: ['chmod', '444', '/kube/config']
      volumes:
      - name: 'kube'
        path: '/kube'
    - name: 'gcr.io/config-management-release/nomos:stable'
      args: ['nomos', 'vet', '--path', '/workspace/POLICY_DIR']
      volumes:
      - name: 'kube'
        path: '/kube'
      env:
      - 'KUBECONFIG=/kube/config'
      timeout: 30s
    

Replace the following:

  * `ZONE`: the zone where your cluster is running
  * `CLUSTER_NAME`: the name of your cluster
  * `POLICY_DIR`: the path within the Git repository that represents the top level of the repository to sync



There are three steps in this configuration:

  1. Run `kubectl config current-context` to generate the [kubeconfig file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig) needed to authenticate to the `my-cluster` GKE cluster. The root user generates this file with restricted permissions.
  2. Run `chmod 444 /kube/config` to make this file readable in the next step.
  3. Run `nomos vet` on the Git repository which is automatically cloned in `/workspace`. If you are [using an unstructured repo](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/unstructured-repo), run `nomos vet --source-format=unstructured` instead.



## Create a build trigger

The following example creates a trigger that runs for every commit to the master branch of a Cloud Source Repositories repository.

  1. Open the Triggers page in Google Cloud console.

[Go to the triggers page](https://console.cloud.google.com/cloud-build/triggers)

  2. Click **Connect repository**.

  3. Select GitHub (mirrored), and then click **Continue**.

  4. Select your repository, and then click **Connect repository**.

  5. Click **Add trigger**.

  6. Enter or select the corresponding entry in each field described in the following table:

Field | Entry  
---|---  
Event | Push to a branch  
Branch | ^master$  
Configuration | Cloud Build configuration file (yaml or json)  
Cloud Build configuration file location | / cloudbuild.yaml  
  7. Click **Create** to save your build trigger.




### Test the build trigger

Manually test the setup by running the trigger:

  1. Open the Triggers page in Google Cloud console.

[Go to the triggers page](https://console.cloud.google.com/cloud-build/triggers)

  2. Find the trigger you created, and then click **Run trigger**.

The message "Build started on master branch" appears.

  3. Click **Show**.

The Cloud Build steps appear green if set up correctly.




#### Invalid Cloud Build configurations

A trigger cannot run if the Cloud Build configuration file is invalid.

To test this, update the Cloud Build config in your repository with the following file. Notice the invalid indentation on line 6:
    
    
    steps:
    - name: 'gcr.io/cloud-builders/kubectl'
      args: ['config', 'current-context']
      volumes:
      - name: 'kube'
      **path : '/kube'**
      env:
      - 'KUBECONFIG=/kube/config'
      - 'CLOUDSDK_COMPUTE_ZONE=ZONE'
      - 'CLOUDSDK_CONTAINER_CLUSTER=CLUSTER_NAME'
      - 'CLOUDSDK_CONTAINER_USE_APPLICATION_DEFAULT_CREDENTIALS=true'
    - name: 'bash'
      args: ['chmod', '444', '/kube/config']
      volumes:
      - name: 'kube'
        path: '/kube'
    - name: 'gcr.io/nomos-release/nomos:stable'
      args: ['nomos', 'vet', '--path', '/workspace/POLICY_DIR']
      volumes:
      - name: 'kube'
        path: '/kube'
      env:
      - 'KUBECONFIG=/kube/config'
      timeout: 30s
    

If you manually run the trigger again, you receive the following error message because `path:` on line 6 is not correctly indented:
    
    
    Failed to trigger build: failed unmarshalling build config cloudbuild.yaml:
    unknown field "path" in cloudbuild_go_proto.BuildStep.
    

To fix this config, indent `path:` on line 6 to the same level as `name:` on line 5. For more information about the structure of a Cloud Build configuration file, see [Creating a basic Cloud Build config](https://docs.cloud.google.com/build/docs/configuring-builds/create-basic-configuration).

## Clean up

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

To delete the individual resources, complete the following steps:

  1. Delete the Cloud Build config file.
  2. [Delete the Cloud Build trigger](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers#deleting_a_build_trigger) that you created.
  3. [Delete the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster) that you used for this tutorial.



## What's next

  * Learn about [Cloud Build](https://docs.cloud.google.com/build/docs/overview)
  * [Temporarily stop syncing configs](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/stopping-resuming-syncing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
