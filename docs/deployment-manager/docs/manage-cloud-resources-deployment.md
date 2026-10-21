---
url: https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment/
title: Quickstart: Manage Google Cloud resources as a deployment \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:15:29.271357+00:00
---

# Quickstart: Manage Google Cloud resources as a deployment  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage Google Cloud resources as a deployment

You can use Google Cloud Deployment Manager to create a set of Google Cloud resources and manage them as a unit, called a _deployment_. For example, if your team's development environment needs two virtual machines (VMs) and a BigQuery database, you can define these resources in a _configuration_ file, and use Deployment Manager to create, change, or delete these resources. You can make the configuration file part of your team's code repository, so that anyone can create the same environment with consistent results.

In this tutorial, you'll use Google Cloud Deployment Manager to create a virtual machine (VM) instance. You'll define the VM in a basic configuration file, and use that configuration file to create a deployment.

To complete this tutorial, you must be comfortable running commands in a Linux, macOS, or Windows terminal.

For an interactive version of this tutorial, open it in Cloud Shell, where you can edit the sample configuration and deploy your resources without installing anything on your workstation. If you want to follow the tutorial on your own computer, skip to the next section.

[![Quickstart in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://console.cloud.google.com/cloudshell/open?git_repo=https%3A%2F%2Fgithub.com%2FGoogleCloudPlatform%2Fdeploymentmanager-samples&page=editor&tutorial=quickstart.md)

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Deployment Manager and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=deploymentmanager,compute_component)

  7. On your workstation, [install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/quickstarts).
  8. Configure the Google Cloud CLI to use your project. In the following command, replace `[MY_PROJECT]` with your project ID: 
         
         gcloud config set project [MY_PROJECT]




## Define your resources

You describe your resources in a configuration file, which is written in the YAML syntax.

  1. Copy the sample configuration below, and paste it into a text editor.
         
         # Copyright 2016 Google Inc. All rights reserved.
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #     http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         
         # Put all your resources under `resources:`. For each resource, you need:
         # - The type of resource. In this example, the type is a Compute VM instance.
         # - An internal name for the resource.
         # - The properties for the resource. In this example, for VM instances, you add
         #   the machine type, a boot disk, network information, and so on.
         #
         # For a list of supported resources,
         # see https://cloud.google.com/deployment-manager/docs/configuration/supported-resource-types.
         resources:
         - type: compute.v1.instance
           name: quickstart-deployment-vm
           properties:
             # The properties of the resource depend on the type of resource. For a list
             # of properties, see the API reference for the resource.
             zone: us-central1-f
             # Replace [MY_PROJECT] with your project ID
             machineType: https://www.googleapis.com/compute/v1/projects/[MY_PROJECT]/zones/us-central1-f/machineTypes/f1-micro
             disks:
             - deviceName: boot
               type: PERSISTENT
               boot: true
               autoDelete: true
               initializeParams:
                 # See a full list of image families at https://cloud.google.com/compute/docs/images#os-compute-support
                 # The format of the sourceImage URL is: https://www.googleapis.com/compute/v1/projects/[IMAGE_PROJECT]/global/images/family/[FAMILY_NAME]
                 sourceImage: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/family/debian-11
             # Replace [MY_PROJECT] with your project ID
             networkInterfaces:
             - network: https://www.googleapis.com/compute/v1/projects/[MY_PROJECT]/global/networks/default
               # Access Config required to give the instance a public IP address
               accessConfigs:
               - name: External NAT
                 type: ONE_TO_ONE_NAT
         

This basic configuration file describes a deployment that contains one virtual machine instance with the following properties:

     * Machine type: `f1-micro`
     * Image family: `debian-11`
     * Zone: `us-central1-f`
     * Root persistent disk: `boot`
     * A randomly assigned external IP address
  2. Replace all instances of `[MY_PROJECT]` with your project ID.

  3. Save the file as `vm.yaml`.




## Deploy the resources

To deploy your resources, use the Google Cloud CLI to create a new deployment, using your configuration file:
    
    
    gcloud deployment-manager deployments create quickstart-deployment --config vm.yaml
    

If the deployment is successful, you receive a message similar to the following example:
    
    
    Create operation operation-1432319707382-516afeb5d00f1-b864f0e7-b7103978 completed successfully.
    NAME                    TYPE                STATE      ERRORS
    quickstart-deployment   compute.v1.instance COMPLETED  -
    

You now have your first deployment!

## Check on your new deployment

To check the status of the deployment, run the following command:
    
    
    gcloud deployment-manager deployments describe quickstart-deployment
    

You see a description of the deployment, including its start and end time, the resources created, and any warnings or errors:
    
    
    fingerprint: xmVVeTtPq-5rr8F-vWFlrg==
    id: '54660732508021769'
    insertTime: '2016-03-09T04:45:26.032-08:00'
    manifest: https://www.googleapis.com/deploymentmanager/v2/projects/myproject/global/deployments/my-first-deployment/manifests/manifest-1457527526037
    name: quickstart-deployment
    operation:
      endTime: '2016-03-09T04:46:19.480-08:00'
      id: '8993923014899639305'
      kind: deploymentmanager#operation
      name: operation-1457527525951-52d9d126f4618-f1ca6e72-3404bd3b
      operationType: insert
      progress: 100
      startTime: '2016-03-09T04:45:27.275-08:00'
      status: DONE
    ...
    resources:
    NAME                     TYPE                 STATE      ERRORS
    quickstart-deployment-vm  compute.v1.instance  COMPLETED  -

## Review your resources

After you have created the deployment, you can review your resources in Google Cloud console.

  1. To see a list of your deployments, open the Deployment Manager page.

[Go to Deployment Manager](https://console.cloud.google.com/dm/deployments?project=_)

  2. To see the resources in the deployment, click **quickstart-deployment**. The deployment overview opens, with information about the deployment, and the resources that are part of the deployment.

  3. To see information about your VM, click **quickstart-deployment-vm**.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 
    
    
    gcloud deployment-manager deployments delete quickstart-deployment
    

Type `y` at the prompt:
    
    
    The following deployments will be deleted:
    - quickstart-deployment
    
    Do you want to continue (y/N)?

The deployment and the resources you created are permanently deleted.

## What's next

  * Learn about best practices for creating deployments by following the [Step-by-step guide to Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide).
  * Learn about [Deployment Manager concepts](https://docs.cloud.google.com/deployment-manager/docs/fundamentals).
  * See the [resources that you can create and manage](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-resource-types) in your deployments.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
