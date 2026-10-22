---
url: https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/using-multiple-templates/
title: Using multiple templates \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:57.432139+00:00
---

# Using multiple templates  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/using-multiple-templates/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Using multiple templates Stay organized with collections  Save and categorize content based on your preferences. 

In this step, you will explore a template that imports other templates.

After incorporating these templates, your configuration only needs to call a single template to create a deployment with all of these resources.

## Opening the template for a network

Open the template named `compute-engine-template.py`:
    
    
    cd deploymentmanager-samples/examples/v2/step_by_step_guide/step6_use_multiple_templates/python
    
    nano compute-engine-template.py  # use your preferred text editor
    

This template imports other templates, for all the resources in the deployment: `vm-template.py`, `vm-template-2.py` for virtual machines (VMs), `network-template.py` for a network, and `firewall-template.py` for a firewall rule.
    
    
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
    
    """Creates the Compute Engine."""
    
    
    def GenerateConfig(context):
      """Creates the Compute Engine with network and firewall."""
    
      resources = [{
          'name': 'vm-1',
          'type': 'vm-template.py'
      }, {
          'name': 'vm-2',
          'type': 'vm-template-2.py'
      }, {
          'name': 'network-1',
          'type': 'network-template.py'
      }, {
          'name': 'firewall-1',
          'type': 'firewall-template.py'
      }]
      return {'resources': resources}
    

## Viewing the configuration

Open the configuration file for the deployment:
    
    
    cd deploymentmanager-samples/examples/v2/step_by_step_guide/step6_use_multiple_templates/python
    
    nano config-with-many-templates.yaml  # use your preferred text editor
    

Notice that the configuration did not directly call the other templates. However, the other templates are imported because `compute-engine-template.py` depends on the other templates.
    
    
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
    - path: network-template.py
    - path: firewall-template.py
    - path: compute-engine-template.py
    
    resources:
    - name: compute-engine-setup
      type: compute-engine-template.py
    

## Saving the configuration and deploying it

Run this command to deploy the configuration:
    
    
    gcloud deployment-manager deployments create deployment-with-many-templates \
      --config config-with-many-templates.yaml
    

To view the deployment, run:
    
    
    gcloud deployment-manager deployments describe deployment-with-many-templates
    

## Looking ahead: template properties and environment variables

Next, you will replace some hard-coded parts of templates with reusable patterns such as custom template and environment variables.

## Deleting your deployment

We recommend that you delete the deployment to avoid charges. You don't need this deployment for the next step. Run the following command to delete the deployment:
    
    
    gcloud deployment-manager deployments delete deployment-with-many-templates
    

[ Previous arrow_back  Understanding reusable templates  ](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/create-a-template)

[ Next Understanding template properties and using environment variables  arrow_forward  ](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/using-template-and-environment-variables)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
