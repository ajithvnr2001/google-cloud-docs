---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template/
title: Creating a Basic Template \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:55.527102+00:00
---

# Creating a Basic Template  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Creating a Basic Template Stay organized with collections  Save and categorize content based on your preferences. 

A basic configuration file might be enough for simple workloads but for more complex architectures or for configurations that you plan to reuse, you can break your configuration into templates.

A template is a separate file that is imported and used as a type in a configuration. You can use as many templates as you want in a configuration.

Templates allow you to separate your configuration out into different pieces that you can use and reuse across different deployments. Templates can be as generalized or specific as you need. With templates, you can also take advantage of features like template properties, environment variables, modules, and other template functionality to create dynamic configuration and template files.

For examples of templates that you can use in your own deployments, see the [Deployment Manager GitHub repository](https://github.com/GoogleCloudPlatform/deploymentmanager-samples).

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Understand how to [create a basic configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-basic-configuration).



## Template syntax

Templates can be written in either [Jinja 2.10.x](https://jinja.palletsprojects.com/en/2.10.x/) or [Python 3.x](https://docs.python.org/3/). Jinja maps more closely to the YAML syntax, so it might be easier to write templates in Jinja if you are more familiar with YAML.

You can also write template files in Python and take advantage of Python to programmatically generate parts of your templates. For example, you can use Python libraries to format template definitions. If you are familiar with Python, this might be a better format for you.

Deployment Manager accepts both Jinja and Python templates. You can import templates in both languages in the same configuration.

## Creating a basic template

A template is a file you create, written in either Jinja or Python. For example, consider the following configuration file:
    
    
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
    - name: vm-created-by-deployment-manager
      type: compute.v1.instance
      properties:
        zone: us-central1-a
        machineType: zones/us-central1-a/machineTypes/n1-standard-1
        disks:
        - deviceName: boot
          type: PERSISTENT
          boot: true
          autoDelete: true
          initializeParams:
            sourceImage: projects/debian-cloud/global/images/family/debian-11
        networkInterfaces:
        - network: global/networks/default
    

This configuration is valid, but you can further simplify the configuration by breaking different parts as individual template files that you can reuse. To create a template based on the configuration above, pull out section for the resource in question and create a new Jinja or Python file.

The following snippets show the sections of templates that can simplify your deployment. For the full templates, click **View on GitHub**.

###  Jinja 
    
    
    - name: vm-template
      type: compute.v1.instance
      properties:
        zone: us-central1-a
        machineType: zones/us-central1-a/machineTypes/n1-standard-1
        disks:
        - deviceName: boot
          type: PERSISTENT
          boot: true
          autoDelete: true
          initializeParams:
            sourceImage: projects/debian-cloud/global/images/family/debian-11
        networkInterfaces:
        - network: global/networks/default

###  Python 

Your Python templates must meet these requirements:

  * The template must define a method called `GenerateConfig(context)` or `generate_config(context)`. If you use both method names in the same template, the `generate_config()` method takes precedence.

The `context` object contains metadata about the deployment and your environment, such as the deployment's name, the current project, and so on. [Learn more about using deployment-specific environment variables](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/use-environment-variables#using_an_environment_variable).

  * The method must return a [Python dictionary](https://docs.python.org/2.7/tutorial/datastructures.html#dictionaries).




Other than that, it is up to you to generate the contents of your template.

**Example**
    
    
    resources.append({
        'name': 'vm-template',
        'type': 'compute.v1.instance',
        'properties': {
            'zone': 'us-central1-a',
            'machineType': 'zones/us-central1-a/machineTypes/n1-standard-1',
            'disks': [{
                'deviceName': 'boot',
                'type': 'PERSISTENT',
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage':
                        'projects/debian-cloud/global/images/family/debian-11'
                }
            }],
            'networkInterfaces': [{
                'network': 'global/networks/default'
            }]
        }
    })

For the full Python example, see the Deployment Manager [GitHub repository](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/blob/master/examples/v2/build_configuration/add_templates/python/vm-template.py).

## Importing the template

After creating a template, import it into your configuration file to use it. To import a template, add an `imports` section in your configuration, followed by the relative or absolute path from the current directory. For example, you can import your virtual machine template from the previous step by adding the following line to the top of your configuration:
    
    
    imports:
      - path: path/to/my_vm_template.jinja
    

If you have a long file path, you can provide an optional `name` property as an alias for the file. You can use this name to reference the template later. If you do not provide the name, the template can be referenced using the `path`.
    
    
    imports:
      - path: path/to/my_vm_template.jinja
        name: my_renamed_template.jinja
    

**Note:** Template name and paths must end with a file extension, such as `.py` and `.jinja`. Non-template file extensions are also accepted, like `.txt`.

You can mix and match imports of multiple templates, regardless of whether the templates are Jinja or Python:
    
    
    imports:
      - path: path/to/my_vm_template.jinja
        name: my_renamed_template.jinja
      - path: special_vm.py
    

If your template uses other templates as dependencies, import the dependent templates in your configuration as well:
    
    
    imports:
      - path: path/to/my_vm_template.jinja
      - path: special_vm.py
      - path: base_vm.jinja
    

You can also import text files in order to inline the content. For example, if you create a file named resource_type.txt with the following string:
    
    
    compute.v1.instance
    

Import it into your configuration and provide the content inline like so:
    
    
    imports:
    - path: resource_type.txt
    
    resources:
    - name: my-vm
      type: {{ imports["resource_type.txt"] }} # Resolves to "compute.v1.instance"
      properties:
        zone: us-central1-a
        machineType: zones/us-central1-a/machineTypes/f1-micro
        disks:
        - deviceName: boot
          type: PERSISTENT
          boot: true
          autoDelete: true
          initializeParams:
            sourceImage: projects/debian-cloud/global/images/family/debian-9
        networkInterfaces:
        - network: global/networks/default
          accessConfigs:
          - name: External NAT
            type: ONE_TO_ONE_NAT

## Deploying templates

Once you import a template, use it as a type in your configuration:

###  Jinja 
    
    
    imports:
    - path: vm-template.jinja
    
    resources:
    - name: my-vm
      type: vm-template.jinja

###  Python 
    
    
    imports:
    - path: vm-template.py
    
    resources:
    - name: my-vm
      type: vm-template.py

If you did not provide a name for your template, call the template using the template path:
    
    
    imports:
    - path: path/to/my_vm_template.jinja
    
    resources:
    - name: my-first-virtual-machine
      type: path/to/my_vm_template.jinja
    

## Deploying templates directly with the command-line tool

Instead of creating a top-level configuration file, Deployment Manager offers the ability to deploy a template directly in the Google Cloud CLI.

For example, the following request deploys a template called `vm-template.jinja`:
    
    
    gcloud deployment-manager deployments create a-single-vm --template vm-template.jinja
    

If your template has [template properties](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/define-template-properties), you can also set these properties on the command-line using the `--properties` flag:
    
    
    gcloud deployment-manager deployments create my-igm \
        --template vm-template.jinja \
        --properties zone:us-central1-a
    

Keep in mind that:

  * All values are parsed as YAML values. For example, `version: 3` is passed in as an integer. If you want to specify it as a string, put escaped single quotes around the value, `version: \'3\'`.

  * Boolean values are case insensitive, so `TRUE`, `true`, and `True` are treated the same.

  * You must pass in all required properties defined by the template. You cannot provide just a subset of the properties. If certain properties have default values, you can omit the property from the command-line.




To specify multiple properties, provide comma-separated key:value pairs. It does not matter in what order you specify the pairs. For example:
    
    
    gcloud deployment-manager deployments create my-igm   
    
        --template vm-template.jinja   
    
        --properties zone:us-central1-a,machineType:n1-standard-1,image:debian-9

After running this command, Deployment Manager creates a deployment using the template you provided. You can confirm that the deployment has been created using the Google Cloud console or the gcloud CLI. For information on viewing a deployment, read [Viewing a manifest](https://docs.cloud.google.com/deployment-manager/docs/deployments/viewing-manifest#view_a_manifest).

## What's next

  * For examples of production-ready templates, see the [Cloud Foundation Toolkit examples in GitHub](https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit).
  * Use [template properties](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/define-template-properties) to further abstract your content.
  * Populate information about your projects and deployments using [environment variables](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/use-environment-variables).
  * Add a template permanently to your project as a [composite type](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-composite-types).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
