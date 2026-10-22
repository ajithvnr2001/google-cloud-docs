---
url: https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/create-a-template/
title: Understanding reusable templates \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:57.894551+00:00
---

# Understanding reusable templates  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/create-a-template/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Understanding reusable templates Stay organized with collections  Save and categorize content based on your preferences. 

While developing an app, you most likely require complex architectures. To make your deployment easier to replicate and troubleshoot, we recommend that you break your configuration into _templates_.

A template is a separate file that defines a set of resources. You can reuse templates across different deployments, which creates consistency across complex deployments.

You can use Python or Jinja2 to create templates for Deployment Manager. We recommend that you use Python templates, because Python allows for greater flexibility and more features as you scale your app.

### Python templates

If you choose to write templates in Python, your templates must meet these requirements:

  * The template must be written in Python 3.x

  * The template must define a method called `GenerateConfig(context)` or `generate_config(context)`. If you use both method names in the same template, the `generate_config()` method will take precedence.

The `context` object contains metadata about the deployment and your environment, such as the deployment's name, the current project, and so on. You'll use these deployment-specific variables in later steps.

  * The method must return a [Python dictionary](https://docs.python.org/3.0/tutorial/datastructures.html#dictionaries).




## Examining sample templates

From the samples repository, open `vm-template.py`:
    
    
    cd deploymentmanager-samples/examples/v2/step_by_step_guide/step5_create_a_template/python
    
    nano vm-template.py  # use your preferred text editor
    

This template defines the first virtual machine (VM) from the earlier samples:
    
    
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
    
    """Creates the virtual machine."""
    
    COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'
    
    
    def GenerateConfig(unused_context):
      """Creates the first virtual machine."""
    
      resources = [{
          'name': 'the-first-vm',
          'type': 'compute.v1.instance',
          'properties': {
              'zone': 'us-central1-f',
              'machineType': ''.join([COMPUTE_URL_BASE, 'projects/MY_PROJECT',
                                      '/zones/us-central1-f/',
                                      'machineTypes/f1-micro']),
              'disks': [{
                  'deviceName': 'boot',
                  'type': 'PERSISTENT',
                  'boot': True,
                  'autoDelete': True,
                  'initializeParams': {
                      'sourceImage': ''.join([COMPUTE_URL_BASE, 'projects/',
                                              'debian-cloud/global/',
                                              'images/family/debian-11'])
                  }
              }],
              'networkInterfaces': [{
                  'network': '$(ref.a-new-network.selfLink)',
                  'accessConfigs': [{
                      'name': 'External NAT',
                      'type': 'ONE_TO_ONE_NAT'
                  }]
              }]
          }
      }]
      return {'resources': resources}
    

Open the second template, `vm-template-2.py`, which defines the second VM:
    
    
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
    
    """Creates the virtual machine."""
    
    COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'
    
    
    def GenerateConfig(unused_context):
      """Creates the second virtual machine."""
    
      resources = [{
          'name': 'the-second-vm',
          'type': 'compute.v1.instance',
          'properties': {
              'zone': 'us-central1-f',
              'machineType': ''.join([COMPUTE_URL_BASE, 'projects/MY_PROJECT',
                                      '/zones/us-central1-f/',
                                      'machineTypes/g1-small']),
              'disks': [{
                  'deviceName': 'boot',
                  'type': 'PERSISTENT',
                  'boot': True,
                  'autoDelete': True,
                  'initializeParams': {
                      'sourceImage': ''.join([COMPUTE_URL_BASE, 'projects/',
                                              'debian-cloud/global',
                                              '/images/family/debian-11'])
                  }
              }],
              'networkInterfaces': [{
                  'network': '$(ref.a-new-network.selfLink)',
                  'accessConfigs': [{
                      'name': 'External NAT',
                      'type': 'ONE_TO_ONE_NAT'
                  }]
              }]
          }
      }]
      return {'resources': resources}
    

In **both** templates, replace MY_PROJECT with your project ID.

## Importing templates

After you create templates, you must import them into your configuration. Open the new `two-vms.yaml`:
    
    
    cd deploymentmanager-samples/examples/v2/step_by_step_guide/step5_create_a_template/python
    
    nano two-vms.yaml  # use your preferred text editor
    

This configuration file has a new `imports` section that calls the two VM templates, `vm-template.py` and `vm-template-2.py`:
    
    
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
    
    imports:
    - path: vm-template.py
    - path: vm-template-2.py
    
    # In the resources section below, the properties of the resources are replaced
    # with the names of the templates.
    resources:
    - name: vm-1
      type: vm-template.py
    - name: vm-2
      type: vm-template-2.py
    - name: a-new-network
      type: compute.v1.network
      properties:
        routingConfig:
          routingMode: REGIONAL
        autoCreateSubnetworks: true
    

## A note about resource names

When you use a template, your resource names are defined using the `name` field provided in the template, not the name in the configuration file.

For example, in this case, the VM instances are created using the names in the templates, `the-first-vm` and `the-second-vm`. The values `vm-1` and `vm-2`, defined in the configuration, are used to name an instantiation of the template, but are not resource names.

## Saving your configuration and deploying it

To deploy the configuration, run this command:
    
    
    gcloud deployment-manager deployments create deployment-with-templates --config two-vms.yaml
    

To view your deployment, run this command:
    
    
    gcloud deployment-manager deployments describe deployment-with-templates
    

## Looking ahead: using multiple templates

In the next step, you combine templates so that your configuration only calls one template to deploy all your resources.

## Deleting your deployment

Before proceeding, we recommend that you delete the deployment to avoid charges. You don't need this deployment for the next step. Run the following command to delete the deployment:
    
    
    gcloud deployment-manager deployments delete deployment-with-templates
    

[ Previous arrow_back  Understanding references  ](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/using-references)

[ Next Using multiple templates  arrow_forward  ](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/using-multiple-templates)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
