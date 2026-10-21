---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/preview-configuration-file/
title: Previewing a configuration \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:54.469366+00:00
---

# Previewing a configuration  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/preview-configuration-file/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Previewing a configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to preview a configuration file before creating a deployment. To learn more about configurations, read [Configurations Overview](https://docs.cloud.google.com/deployment-manager/docs/configuration).

After you have [written a configuration file](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-basic-configuration), you can preview the configuration before you create a deployment. Previewing a configuration lets you see the resources that Deployment Manager would create but does not actually instantiate any actual resources. The Deployment Manager service previews the configuration by:

  1. Expanding the full configuration, including any templates.
  2. Creating a deployment and "shell" resources.



You can preview your configuration by using the `preview` query parameter when making an [`insert()`](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/insert) request.

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Understand how to [create a basic configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-basic-configuration).



## Previewing a new configuration

Preview a configuration by using the Google Cloud CLI or by making a direct request to the API.

###  gcloud 

If you're using the Google Cloud CLI, use the `create` sub-command with the `--preview` flag:
    
    
    gcloud deployment-manager deployments create example-config --config configuration-file.yaml \
         --preview
    

The server returns a list of resources whose state is `IN_PREVIEW` for you to review:
    
    
    The fingerprint of the deployment is ulPDrJON8E5ySHKC5fcukw==
    Waiting for create [operation-1492785372594-54dae2ddbff50-58d45d53-12d483cf]...done.
    Create operation operation-1492785372594-54dae2ddbff50-58d45d53-12d483cf completed successfully.
    NAME                      TYPE                 STATE       ERRORS  INTENT
    datadisk-example  compute.v1.disk      IN_PREVIEW  []      CREATE_OR_ACQUIRE
    vm-example        compute.v1.instance  IN_PREVIEW  []      CREATE_OR_ACQUIRE
    

###  API 

In the API, use the [`insert()`](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/insert) method with a request body that contains the `target` and `name` fields and the `preview=true` query parameter. Provide your configuration in the `target` field.

For example, the following API request previews a simple template:
    
    
    POST https://www.googleapis.com/deploymentmanager/v2/projects/myproject/global/deployments?preview=true
    
    {
     "name": "example-config",
     "target": {
      "config": {
        "content":  "resources:\n- name: vm-created-by-cloud-config\n  type: compute.v1.instance\n  properties:\n    zone: us-central1-a\n    machineType: https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/machineTypes/n1-standard-1\n    disks:\n    - deviceName: boot\n      type: PERSISTENT\n      boot: true\n      autoDelete: true\n      initializeParams:\n        diskName: disk-created-by-cloud-config\n        sourceImage: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-7-wheezy-v20140619\n    networkInterfaces:\n    networkInterfaces:\n    - network: https://www.googleapis.com/compute/v1/projects/myproject/global/networks/default"
       }
      }
    }
    

When a deployment is in preview mode, you can move forward with the deployment in one of three ways:

  * Deploy the configuration by [performing an update](https://docs.cloud.google.com/deployment-manager/docs/deployments/updating-deployments#make_the_update_request).
  * Cancel the preview and then delete the deployment.
  * Update the preview.



## Performing multiple previews

If you want to change your configuration and perform another preview, use the `update` command with the `--preview` flag:
    
    
    gcloud deployment-manager deployments update example-config \
        --config new-config.yaml --preview
    

In the API, make a [`PUT()`](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/update) request with an existing deployment and provide the `preview=true` query parameter. The request body must contain the `intent`, `target`, and `name` fields. For example, the following API request previews a simple update:
    
    
    PUT https://www.googleapis.com/deploymentmanager/v2/projects/myproject/global/deployments/example-config?preview=true
    
    {
     "target": {
      "config": {
       "content": "resources:\n- name: vm-created-by-cloud-config\n  type: compute.v1.instance\n  properties:\n    zone: us-central1-a\n    machineType: https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/machineTypes/n1-standard-1\n    disks:\n    - deviceName: boot\n      type: PERSISTENT\n      boot: true\n      autoDelete: true\n      initializeParams:\n        diskName: disk-created-by-cloud-config\n        sourceImage: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-7-wheezy-v20140619\n    networkInterfaces:\n    - network: https://www.googleapis.com/compute/v1/projects/myproject/global/networks/default"
      }
     },
     "name": "example-config"
    }
    

**Note:** In the API, you need to provide the deployment name in both the URL and in the request body.

## Deploying or canceling a preview

After previewing a deployment, you can move forward with the deployment by performing an update and committing the configuration. For example, assume you have a deployment named example-config currently in preview mode. You can move forward with the deployment by running the following command:
    
    
    gcloud deployment-manager deployments update example-config
    

Deployment Manager uses the last previewed configuration to create a deployment.

Alternatively, if you don't want to move forward with the configuration, you can cancel the preview, and then delete the deployment:
    
    
    gcloud deployment-manager deployments cancel-preview example-config
    

**Note:** If you perform many previews without canceling or moving forward with any of them, you will end up with many empty deployments. Make sure to [cancel](https://docs.cloud.google.com/deployment-manager/docs/deployments/updating-deployments#cancelpreview) and delete the deployments that you previewed but no longer need once you are done with them.

While a deployment is in preview mode, you cannot move forward with another configuration. For example, assume you have a deployment called `example-config` that is in preview mode using a configuration named `vm.yaml`. You decide that you want to deploy a new configuration named `two_vms.yaml` to the same deployment, skipping the preview process. While `example-config` is still in preview mode, you cannot deploy a new configuration. Cancel the preview, and then [update the deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments/updating-deployments) with the new configuration.

## What's next

  * Learn more about [configuration files](https://docs.cloud.google.com/deployment-manager/docs/configuration).
  * [Make an update](https://docs.cloud.google.com/deployment-manager/docs/deployments/updating-deployments) to your deployment after you deploy it.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
