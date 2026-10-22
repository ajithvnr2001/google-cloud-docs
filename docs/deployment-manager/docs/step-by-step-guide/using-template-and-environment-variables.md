---
url: https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/using-template-and-environment-variables/
title: Setting template properties and using environment variables \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:57.305903+00:00
---

# Setting template properties and using environment variables  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/using-template-and-environment-variables/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Setting template properties and using environment variables Stay organized with collections  Save and categorize content based on your preferences. 

One advantage of using templates for your deployment is the ability to create and define custom properties, which let you reuse templates across zones, regions, and projects.

Template properties are arbitrary variables. Any configuration file or template file can provide a value for a template property without modifying the template. Therefore, you can change a property's value for various configurations without changing the template itself.

To reference an arbitrary value, use this syntax in a template:
    
    
    context.properties["property-name"]
    

In addition to template properties, you can also use environment variables specific to your deployment, which are pre-populated with information about the deployment. You can use environment variables in templates to get unique information about your deployment.

You call an environment variable by using this syntax:
    
    
    context.env['variable-name']
    

Valid environment variables include the deployment name, the project ID, the name property of your resource, and the type of your configuration. [Learn more about environment variables](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/use-environment-variables).

## Template properties and environment variables in a template

In this step, `vm-template.py` shows the benefits of template properties and environment variables. Open `vm-template.py`:
    
    
    cd deploymentmanager-samples/examples/v2/step_by_step_guide/step7_use_environment_variables/python
    
    nano vm-template.py  # use your preferred text editor
    

Various parts of the template have been replaced with template properties and environment variables. For example, the project ID is replaced with `context.env[project]`, so you don't have to manually replace the project ID in your templates.

The comments in the file describe other changes to the template.
    
    
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
    
    
    def GenerateConfig(context):
      """Creates the virtual machine with environment variables."""
    
      resources = [{
          # `the-first-vm` is replaced with `context.env[`name`]`
          'name': context.env['name'],
          'type': 'compute.v1.instance',
          'properties': {
              # All occurrences of `us-central1-f` are replaced with
              # `context.properties[`zone`]. 
              # All occurrences of the project ID are replaced with 
              # `context.env[`project`]`.
              # `f1-micro` is replaced with `context.properties["machineType"].  
              'zone': context.properties['zone'],
              'machineType': ''.join([COMPUTE_URL_BASE, 'projects/',
                                      context.env['project'], '/zones/',
                                      context.properties['zone'], '/machineTypes/',
                                      context.properties['machineType']]),
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
              # `$(ref.a-new-network.selfLink)` is replaced with 
              # `$(ref.` + context.properties[`network`] + `selfLink)`.
              'networkInterfaces': [{
                  'network': '$(ref.' + context.properties['network']
                             + '.selfLink)',
                  'accessConfigs': [{
                      'name': 'External NAT',
                      'type': 'ONE_TO_ONE_NAT'
                  }]
              }]
          }
      }]
      return {'resources': resources}
    

Similarly, `network-template.py` and `firewall-template.py` use the deployment's name in their definition, by calling `context.env['name']`.

## Deploying the configuration

To view the configuration file for this deployment, run the following command:
    
    
    nano config-with-many-templates.yaml
    

Save your changes and redeploy your configuration to confirm the variables work.
    
    
    gcloud deployment-manager deployments create deployment-with-template-properties --config config-with-many-templates.yaml
    

## Deleting your deployment

We recommend that you delete the deployment to avoid charges. You don't need this deployment for the next step. Run the following command to delete the deployment:
    
    
    gcloud deployment-manager deployments delete deployment-with-template-properties
    

## Looking ahead: helper scripts

Next, learn about helper scripts to efficiently perform repeated tasks.

[ Previous arrow_back  Using multiple templates  ](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/using-multiple-templates)

[ Next Exploring helper scripts  arrow_forward  ](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/learn-helper-scripts)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
