---
url: https://docs.cloud.google.com/deployment-manager/docs/deployments/updating-deployments/
title: Updating a Deployment \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:57.254534+00:00
---

# Updating a Deployment  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/deployments/updating-deployments/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Updating a Deployment Stay organized with collections  Save and categorize content based on your preferences. 

After you have created a deployment, you can update it as your application or service changes. You can use Deployment Manager to update a deployment by:

  * Adding or removing resources from a deployment.
  * Updating the properties of existing resources in a deployment.



A single update can contain any combination of these changes. For example, you can make changes to the properties of existing resources and add new resources in the same request. You update your deployment by following these steps:

  1. Make changes to or create a configuration file with the changes you want.
  2. Optionally, pick the policies to use for your updates or use the default policies.
  3. Make the update request to Deployment Manager.



## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Understand how to [create deployments](https://docs.cloud.google.com/deployment-manager/deployments).



## Prepare your update

Before updating your deployment, use these guidelines to prepare the update:

  * **If you are updating your deployment to add new resources to your project, check whether the resources already exist.**

By default, if a resource that you want to add already exists in your project, it is acquired by the deployment, without creating a new resource. If you do not want to acquire an existing resource, you must change the policy to use for the update.

For information on the policies you can use while updating deployments, see Policies for adding resources.

  * **If you are updating your deployment to replace a resource, check its dependencies**

If you want to replace a resource from your deployment, you must first make sure that deleting it doesn't cause a _deployment cycle_. A deployment cycle occurs when a resource depends on itself, either directly or indirectly. For example, consider the following deployment:
        
        resources:
        - name: vm-a
          properties:
            zone: us-central1-f
            ...
            metadata:
              dependsOn:
              - vm-depends-on
        
        # The second VM
        - name: vm-depends-on
          properties:
            zone: $(ref.vm-a.zone)
            ...
        

In this deployment, for `vm-a`, the `dependsOn` statement requires that `vm-depends-on` must be created before `vm-a`. However, `vm-depends-on` uses a reference to the zone for `vm-a`, which requires that `vm-a` must be created before `vm-depends-on`. In such a scenario, the dependencies are in a loop, and the deployment fails.

If you have resource that both depends on and is depended on by other resources, replacing that resource might cause a deployment cycle.

For example, consider a deployment has a persistent disk called `disk-a`, a VM called `vm-a`, and an instance group called `ig-a`. The configuration for `vm-a` includes a reference to `disk-a`, and the configuration for `ig-a` includes a reference to `vm-a`. In an updated configuration, you want to remove `vm-a` and replace it with `vm-b`. In such a scenario, resolving the dependencies for vm-a and vm-b can cause a deployment cycle, and your deployment fails.

To avoid deployment cycles when you want to replace a resource in a chain of dependencies, do one of the following:

    * Remove the dependencies for the resource you want to replace, either by removing the dependsOn clause, or by removing or changing references to other resources. After you have updated the deployment with these changes, make another update to replace the resource.

    * Delete the chain of dependent resources, and update the deployment. Then, in the next update, re-create the resources that you want to use.

  * **Ensure that there is an underlying API that supports your update.**

Deployment Manager uses the APIs of each service to create and modify your deployments. To check that your request can be completed by Deployment Manager, review the API documentation of the Cloud Platform service for the resources that you want to update.

For example, if you want to update a [BigQuery](https://docs.cloud.google.com/bigquery) dataset in your deployment, see the available methods in the [Datasets API reference](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets#methods). The methods include an `update` method, which indicates that you can update the dataset using Deployment Manager.

Some APIs have custom methods for updating their resources. For example, Compute Engine offers a custom method for updating an instance’s metadata called `setMetadata`. In such cases, Deployment Manager attempts to use the custom methods.

  * **Ensure that the resources you are updating are mutable.**

Some resources are immutable after they have been created, and they cannot be updated. To determine whether a resource is immutable, see the API reference for the resource. Typically, an immutable resource lacks an `update` API method or a custom method to update the properties of the resource.




## Limitations

  * For each deployment, you can apply one update at a time. If an update is already in progress, you must stop the current update before starting a new update.

  * If you modified a resource in a deployment without using Deployment Manager, such as in the Google Cloud console or `gcloud`, you might see errors or unexpected issues when you try to modify the resource in an update.




## Make changes to your configuration

If you saved an existing configuration, make changes to the configuration and use that in your update request.

If you do not have an existing configuration saved, create a new configuration. For steps to create a configuration file, read [Configurations](https://docs.cloud.google.com/deployment-manager/docs/configuration).

Deployment Manager compares the configuration you provide in your update request to the previous manifest and use the differences to update your deployment.

For example, the following table shows two configurations: one describes an existing deployment and one describes the desired updated state of the deployment. You provide the updated configuration and Deployment Manager evaluates the differences and makes the appropriate updates.

This example updates an existing instance resource to include some custom metadata and also adds a new virtual machine resource to the deployment. The parts in **bold** are differences between the templates.

**Note:** For readability, the example replaces URLs with placeholders. In practice, you need to provide URLs for these properties, such as the machine type.Current template | Updated template | 
    
    
    resources:
    - name: vm-created-by-cloud-config
      type: compute.v1.instance
      properties:
        zone: us-central1-a
        machineType: machine-type-url
        disks:
        - deviceName: boot
          type: PERSISTENT
          boot: true
          autoDelete: true
          initializeParams:
            diskName: disk-created-by-cloud-config
            sourceImage: image-url
        networkInterfaces:
        - network: network-url

| 
    
    
    resources:
    - name: vm-created-by-cloud-config
      type: compute.v1.instance
      properties:
        zone: us-central1-a
        machineType: machine-type-url
        disks:
        - deviceName: boot
          type: PERSISTENT
          boot: true
          initializeParams:
            diskName: disk-created-by-cloud-config
            sourceImage: image-url
        networkInterfaces:
        - network: network-url
        **metadata :
          items:
          - key: 'foo'
            value: 'bar'
          - key: 'dev'
            value: 'vm'**
    
    **- name: a-new-vm
      type: compute.v1.instance
      properties:
        zone: us-central1-a
        machineType: machine-type-url
          - deviceName: boot
          type: PERSISTENT
          boot: true
          autoDelete: false
          initializeParams:
            diskName: a-new-vm-disk
            sourceImage: image-url
        networkInterfaces:
        - network: network-url**  
  
---|---  
  
## (Optional) Determine the policies to use for the update

Next, determine what policies you want to use for the update. The policy determines how your resources are updated when you update the deployment.

**Note:** If you want to see your updated deployment before committing any changes, you can preview your configuration.

Deployment Manager uses these default policies:

  * The default policy for adding resources is `CREATE_OR_ACQUIRE`.
  * The default policy for removing resources is `DELETE`.
  * The default policy for updating resources is `UPDATE`.



For information on each policy, review the sections below.

### Policies for adding resources

When adding resources, you can choose to create a new resource and add it to a deployment or you can acquire an existing resource:

  * `CREATE_OR_ACQUIRE` \- **[Default]** Deployment Manager acquires resources that exist in the project, or creates resources if they do not exist. To acquire a resource, Deployment Manager checks your configuration for the properties of the resource you are trying to create. If there is an existing resource with the same properties, Deployment Manager acquires that resource as part of your deployment.

The properties that Deployment Manager checks depend on the type of resource you are creating, and might include:

    * The `name` of the resource
    * The `type` of the resource
    * The `zone` or `region` of the resource, if applicable

The properties are part of the URL for `GET` API request for the resource. To see which properties Deployment Manager uses to acquire a resource, see the API documentation for the resource's `GET` method. For example, for Compute Engine instances, the request URL for [`instances.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get) method includes the `resourceId` (`name` in your configuration), `zone`, and `project`.

**Note:** If you want to acquire a resource and then update it, we recommend first providing all the _current_ properties of the resource, as if you were creating it. After the resource is acquired, to update the resource, change the resource's properties in your configuration and run the update command again.
  * `CREATE` \- Deployment Manager creates resources that do not exist. If any of the resources in your configuration already exist in the project, the deployment fails.

  * `ACQUIRE` \- Deployment Manager acquires resources that already exist, using the same criteria as `CREATE_OR_ACQUIRE`.

Use the `ACQUIRE` policy if you have a number of resources already in your project, and want to manage them together, as a single deployment.

In your template or configuration, you must provide the required properties for these resources as if you are creating them. If any of the resources in your configuration do not exist in the project, the deployment fails.

**Warning:** Do not acquire resources that are already part of another deployment. If you do, any changes you make to one deployment can cause unexpected behavior with the resources in the other deployment.



### Policies for removing resources

Provide one of the following policies for removing resources:

  * `DELETE` \- **[Default]** This removes any references to the resource from the deployment and deletes the underlying resource. This is permanent and cannot be undone, but you can recreate a new resource with the same properties.

  * `ABANDON` \- This removes any references to the resource from the deployment but does not delete the underlying resource. For example, abandoning an instance means that it is removed from a deployment but the instance still exists for you to use.

The `ABANDON` policy only applies when you delete entire resources, not when you delete the properties of a resource, or update a resource with new properties. If you want to preserve the properties of a resource, you must include the resource with all its original properties in your updated configuration. If you're using a new configuration file for your update, we recommend copying the resource's definition from your original configuration.




### Policies for updating an existing resource

If an `UPDATE` method exists for updating existing resources, Deployment Manager uses that.

Otherwise, if a custom method exists, Deployment Manager uses the custom method. Deployment Manager supports custom methods that use the verb `set`. For example, `setMetadata()` is a valid custom method, but `addAccessConfigs()` is not.

## (Optional) Preview an updated configuration

You can preview the update you want to make before committing any changes, with the Google Cloud CLI or the API. The Deployment Manager service previews the configuration by expanding the full configuration and creating "shell" resources.

Deployment Manager **does not** instantiate any actual resources when you preview a configuration, giving you the opportunity to see the deployment before committing to it.

###  gcloud 

With the Google Cloud CLI, make an `update` request with the `--preview` parameter:
    
    
    gcloud deployment-manager deployments update example-deployment \
        --config configuration-file.yaml \
        --preview
    

###  API 

In the API, create a [`PUT()`](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/update) request with an existing deployment and provide the `preview=true` query parameter. The request body must contain the `intent`, `target`, and `name` fields. Provide the deployment name in both the URL and in the request body.

For example, the following API request previews a simple update:
    
    
    PUT https://www.googleapis.com/deploymentmanager/v2/projects/myproject/global/deployments/example-deployment?preview=true
    
    {
     "target": {
      "config": {
       "content": "resources:\n- name: vm-created-by-cloud-config\n  type: compute.v1.instance\n  properties:\n    zone: us-central1-a\n    machineType: https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/machineTypes/n1-standard-1\n    disks:\n    - deviceName: boot\n      type: PERSISTENT\n      boot: true\n      autoDelete: true\n      initializeParams:\n        diskName: disk-created-by-cloud-config\n        sourceImage: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-9-stretch-v20180716\n    networkInterfaces:\n    - network: https://www.googleapis.com/compute/v1/projects/myproject/global/networks/default"
      }
     },
     "name": "example-deployment"
    }
    

After previewing a deployment, you can fully deploy the configuration by making the same `PUT()` request, omitting both the configuration and the `preview` query parameter. Deployment Manager uses your last preview to perform the update. For example:
    
    
    gcloud deployment-manager deployments update example-deployment
    

For steps to make an update request, see Make the update request.

If you decide not to continue with the update, cancel the current preview before making another update or preview request.

### Cancel a preview

After you preview an update, you must decide if you want to continue with the update. If you do not want to continue, or if you want to use a different configuration file to update the deployment, cancel the current preview.

###  gcloud 

With the Google Cloud CLI, make a `deployments cancel-preview` request:
    
    
    gcloud deployment-manager deployments cancel-preview my-first-deployment
    

###  API 

In the API, make a `PUT()` request to the [`cancelPreview`](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/cancelPreview) method and provide the latest deployment fingerprint. A fingerprint is a randomly generated value that changes with each update request. To prevent errors during the update, provide the latest fingerprint with your request.

To get the latest fingerprint of a deployment, use the [`get()`](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/get) method to get a deployment, and look for the fingerprint value. The fingerprint value looks like this:
    
    
    "fingerprint": "nU2v7bzeA7gBBI8bdbtmFg=="
    

Your `cancelPreview()` request looks like this:
    
    
    POST https://www.googleapis.com/deploymentmanager/v2/projects/myproject/global/deployments/example-deployment/cancelPreview
    
    {
     "fingerprint": "nU2v7bzeA7gBBI8bdbtmFg=="
     }
    

## Make the update request

To perform the update:

###  gcloud 

With the Google Cloud CLI, use the `deployments update` subcommand, providing a new configuration and optionally, your update policies.
    
    
    gcloud deployment-manager deployments update my-first-deployment \
        --create-policy POLICY \
        --delete-policy POLICY
    

If you previously [previewed](https://docs.cloud.google.com/deployment-manager/deployments/updating-deployments#optional_preview_an_updated_configuration) a configuration, omit the configuration and Deployment Manager uses the last previewed configuration to perform the update.
    
    
    gcloud deployment-manager deployments update my-first-deployment
    

###  API 

In the API, make an [`update`](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/update) request and provide the latest deployment fingerprint. A fingerprint is a randomly generated value that changes with each update request. To prevent errors during the update, provide the latest fingerprint with your request.

To get the latest fingerprint of a deployment, use the [`get()`](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/get) method to get a deployment, and look for the fingerprint value. The fingerprint value looks like this:
    
    
    "fingerprint": "nU2v7bzeA7gBBI8bdbtmFg=="
    

Next, provide the fingerprint in your request, along with with your new configuration and update policies. If you previously [previewed](https://docs.cloud.google.com/deployment-manager/deployments/updating-deployments#optional_preview_an_updated_configuration) the configuration, omit the configuration and update policies, and Deployment Manager uses the last previewed configuration to perform the update.

Provide the deployment name in both the URL and in the request body.
    
    
    PUT https://www.googleapis.com/deploymentmanager/v2/projects/myproject/global/deployments/example-deployment?createPolicy=ACQUIRE&deletePolicy=ABANDON
    
    {
     "target": {
      "config": {
       "content": "resources:\n- name: vm-created-by-cloud-config\n  type: compute.v1.instance\n  properties:\n    zone: us-central1-a\n    machineType: https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/machineTypes/n1-standard-1\n    disks:\n    - deviceName: boot\n      type: PERSISTENT\n      boot: true\n      autoDelete: true\n      initializeParams:\n        diskName: disk-created-by-cloud-config\n        sourceImage: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-9-stretch-v20180716\n    networkInterfaces:\n    - network: https://www.googleapis.com/compute/v1/projects/myproject/global/networks/default"
      }
     },
     "name": "example-deployment",
     "fingerprint": "nU2v7bzeA7gBBI8bdbtmFg=="
    }
    

## Stop an update

You can stop an update that is in progress using the [`stop()`](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/stop). method. This cancels any further progress from a particular update, but does not undo any change that have already been made.

If you are trying to cancel a preview, see the Cancel a preview section.

###  gcloud 

With the Google Cloud CLI, make a `deployments stop` request:
    
    
    gcloud deployment-manager deployments stop my-first-deployment
    

###  API 

In the API, make a `POST()` request to the [`stop`](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/stop) method and provide the latest fingerprint property. A fingerprint is a randomly generated value that changes with each update request. In order to prevent conflicting changes, you must provide the latest fingerprint with your request, to perform optimistic locking so that only one update can be made at a time.

To get the latest fingerprint of a deployment, use the [`get()`](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/deployments/get) method to get a deployment, and look for the fingerprint value. The fingerprint value looks like this:
    
    
    "fingerprint": "nU2v7bzeA7gBBI8bdbtmFg=="
    

Your request looks like this:
    
    
    POST https://www.googleapis.com/deploymentmanager/v2/projects/myproject/global/deployments/example-deployment/stop
    
    {
     "fingerprint": "nU2v7bzeA7gBBI8bdbtmFg=="
     }
    

## What's next

  * [Add labels](https://docs.cloud.google.com/deployment-manager/docs/deployments/add-labels-deployments) to your deployment.
  * View your [deployment manifest](https://docs.cloud.google.com/deployment-manager/docs/deployments/viewing-manifest).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
