---
url: https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/create-a-configuration/
title: Understanding configurations \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:53.464875+00:00
---

# Understanding configurations  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/create-a-configuration/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Understanding configurations Stay organized with collections  Save and categorize content based on your preferences. 

A configuration defines the structure of your deployment. You must specify a configuration to create a deployment.

In this step, you will access a configuration that creates a deployment with two Compute Engine virtual machine (VM) instances. A VM instance is one of several kinds of resources you can deploy with Deployment Manager.

In this step, you'll examine a configuration for a deployment with two VM instances.

## Open the configuration YAML file

Change to the directory you created in [Installation and setup](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/installation-and-setup):
    
    
    cd deploymentmanager-samples/examples/v2/step_by_step_guide/step2_create_a_configuration
    

Then, open `two-vms.yaml`:
    
    
    nano two-vms.yaml   # use your preferred text editor
    

In the `resources` section, note that there are two resources: `the-first-vm` and `the-second-vm`. Each resource has a `name`, `type`, and `properties` field:

  * `name`: A name that you define for the resource.

  * `type`: Specifies what type of resource you're creating. For example, a VM is `compute.v1.instance`. Similarly, a Cloud SQL  
instance has the type `sql.v1beta4.instance`.

  * `properties`: Specifies the properties of the resource. The properties required to create the resource are the same properties required by the resource's API. For example, when you create a Compute Engine VM instance, you must provide a machine type, an image, a network interface, and a boot disk specification.




## Set up the configuration file

In `two-vms.yaml`, replace MY_PROJECT with your project ID.
    
    
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
    
    resources:
    - name: the-first-vm
      type: compute.v1.instance
      properties:
        zone: us-central1-f
        machineType: https://www.googleapis.com/compute/v1/projects/MY_PROJECT/zones/us-central1-f/machineTypes/f1-micro
        disks:
        - deviceName: boot
          type: PERSISTENT
          boot: true
          autoDelete: true
          initializeParams:
            sourceImage: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/family/debian-11
        networkInterfaces:
        - network: https://www.googleapis.com/compute/v1/projects/MY_PROJECT/global/networks/default
          accessConfigs:
          - name: External NAT
            type: ONE_TO_ONE_NAT
    - name: the-second-vm
      type: compute.v1.instance
      properties:
        zone: us-central1-f
        machineType: https://www.googleapis.com/compute/v1/projects/MY_PROJECT/zones/us-central1-f/machineTypes/g1-small
        disks:
        - deviceName: boot
          type: PERSISTENT
          boot: true
          autoDelete: true
          initializeParams:
            sourceImage: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/family/debian-11
        networkInterfaces:
        - network: https://www.googleapis.com/compute/v1/projects/MY_PROJECT/global/networks/default
          accessConfigs:
          - name: External NAT
            type: ONE_TO_ONE_NAT
    

## Save your changes

This basic configuration file is all you need to create your first deployment. You declared the resources that you want to create (in this case, two VM instances that had different machine types), and Deployment Manager takes care of creating the resources.

In the next step, you use this configuration to deploy new resources.

[ Previous arrow_back  Installation and setup  ](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/installation-and-setup)

[ Next Deploying your resources  arrow_forward  ](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/deploy-your-resources)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
