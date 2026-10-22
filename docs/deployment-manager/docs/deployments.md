---
url: https://docs.cloud.google.com/deployment-manager/docs/deployments/
title: Creating a Deployment using gcloud or the API \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:20.439989+00:00
---

# Creating a Deployment using gcloud or the API  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/deployments/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Creating a Deployment using gcloud or the API Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a deployment. A deployment is an instantiation of a set of resources that are defined in a [configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration). You provide a valid configuration in the request to create the deployment. A deployment can contain a number of resources, across a variety of Google Cloud services. When you create a deployment, Deployment Manager creates all of the described resources in the respective Google Cloud APIs.

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Create a [configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-configuration-file).



## Creating a deployment

When you create a deployment, you are creating a [Deployment resource](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments) that contains a collection of resources. Each resource is explicitly defined in a configuration that you provide in your request.

###  gcloud 

With the Google Cloud CLI, use the `deployments create` command:
    
    
    gcloud deployment-manager deployments create my-first-deployment \
        --config vm.yaml
    

The `--config` flag is a relative path to your YAML configuration file.

By default, if your configuration includes resources that are already in your project, those resources are acquired by the deployment, and can be managed using the deployment. If you don't want to acquire a resource, you must use the `--create-policy` option, as in the following `gcloud beta` command:
    
    
    gcloud beta deployment-manager deployments create my-first-deployment \
        --config vm.yaml --create-policy CREATE
    

For information on what policies you can use when you are creating deployments, see Setting the policy for creating resources.

If your deployment is successfully created, you can get a description of the deployment:
    
    
    gcloud deployment-manager deployments describe my-first-deployment
    

###  API 

In the API, make an [`insert()`](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/insert) request with the configuration provided inline, in the request body:
    
    
    POST https://www.googleapis.com/deploymentmanager/v2/projects/myproject/global/deployments
    
    {
     "name": "example-config-with-templates",
     "target": {
      "config": {
       "content": "resources:\n- name: vm-created-by-cloud-config\n  type: compute.v1.instance\n  properties:\n    zone: us-central1-a\n    machineType: https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/machineTypes/n1-standard-1\n    disks:\n    - deviceName: boot\n      type: PERSISTENT\n      boot: true\n      autoDelete: true\n      initializeParams:\n        diskName: disk-created-by-cloud-config\n        sourceImage: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-7-wheezy-v20151104\n    networkInterfaces:\n    - network: https://www.googleapis.com/compute/v1/projects/myproject/global/networks/default\n"
      }
     }
    }
    

If you import [templates](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template), you must also provide those templates as part of the request body. For example, the following API request has a `target` that imports one template, named `vm_template.jinja`:
    
    
    POST https://www-www.googleapis.com/deploymentmanager/v2/projects/myproject/global/deployments
    
    {
     "name": "my-example-config-with-templates-2",
     "target": {
      "config": {
        "content": "imports:\n- path: vm_template.jinja\n\nresources:\n- name: my-vm\n  type: vm_template.jinja"
      },
      "imports": [
       {
        "content": "resources:\n- name: vm-created-by-cloud-config\n  type: compute.v1.instance\n  properties:\n    zone: us-central1-a\n    machineType: https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/machineTypes/n1-standard-1\n    disks:\n    - deviceName: boot\n      type: PERSISTENT\n      boot: true\n      autoDelete: true\n      initializeParams:\n        diskName: disk-created-by-cloud-config\n        sourceImage: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-7-wheezy-v20151104\n    networkInterfaces:\n    - network: https://www.googleapis.com/compute/v1/projects/myproject/global/networks/default",
        "name": "vm_template.jinja"
       }
      ]
     }
    }
    

**Note:** When you use the API to create a deployment, the operation might take a substantial length of time to complete. For guidelines on checking the operation's status, read about [managing long-running operations](https://docs.cloud.google.com/deployment-manager/docs/reference/managing-long-running-operations).

## Setting the policy for creating resources

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

When you create a new deployment, if a resource that you want to create already exists in your project, it is acquired by the deployment. In such cases, Deployment Manager does not create a new resource. If you do not want to acquire an existing resource, you must use the `CREATE` policy for your deployment.

You can use the following policies for creating your resources:

  * `CREATE_OR_ACQUIRE` \- **[Default]** Deployment Manager acquires resources that exist in the project, or creates resources if they do not exist. To acquire a resource, Deployment Manager checks your configuration for the properties of the resource you are trying to create. If there is an existing resource with the same properties, Deployment Manager acquires that resource as part of your deployment.

The properties that Deployment Manager checks depend on the type of resource you are creating, and might include:

    * The `name` of the resource
    * The `type` of the resource
    * The `zone` or `region` of the resource, if applicable

The properties are part of the URL for `GET` API request for the resource. To see which properties Deployment Manager uses to acquire a resource, see the API documentation for the resource's `GET` method. For example, for Compute Engine instances, the request URL for [`instances.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get) method includes the `resourceId` (`name` in your configuration), `zone`, and `project`.

**Note:** If you want to acquire a resource, you must provide all the required properties of the resource, as if you were creating it.
  * `CREATE` \- Deployment Manager creates resources that do not exist. If any of the resources in your configuration already exist in the project, the deployment fails.

  * `ACQUIRE` \- Deployment Manager acquires resources that already exist, using the same criteria as `CREATE_OR_ACQUIRE`.

Use the `ACQUIRE` policy if you have a number of resources already in your project, and want to manage them together, as a single deployment.

In your template or configuration, you must provide the required properties for these resources as if you are creating them. If any of the resources in your configuration do not exist in the project, the deployment fails.

**Warning:** Do not acquire resources that are already part of another deployment. If you do, any changes you make to one deployment can cause unexpected behavior with the resources in the other deployment.



## Listing your deployments

View a list of your deployments in either the [Google Cloud console](https://console.cloud.google.com/), the API, or the Google Cloud CLI.

###  Console 

Go to the [**Deployments**](https://console.cloud.google.com/project/_/deployments) page in the Google Cloud console.

###  gcloud 

With the Google Cloud CLI, use the `deployments list` subcommand:
    
    
    gcloud deployment-manager deployments list
    

###  API 

In the API, make an empty `GET` request to the Deployments collection:
    
    
    GET https://www.googleapis.com/deploymentmanager/v2beta1/projects/myproject/global/deployments
    

## What's next

  * Add [labels to your deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments/add-labels-deployments).
  * [Update your deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments/updating-deployments).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
