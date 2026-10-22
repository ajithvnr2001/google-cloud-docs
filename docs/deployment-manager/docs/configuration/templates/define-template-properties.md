---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/define-template-properties/
title: Defining Template Properties \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:12.867733+00:00
---

# Defining Template Properties  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/define-template-properties/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Defining Template Properties Stay organized with collections  Save and categorize content based on your preferences. 

One of the advantages of using [templates](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template) is the ability to create and define custom template properties. Template properties are arbitrary variables that you define in template files. Any configuration file or template file that uses the template in question can provide a value for the template property without changing the template directly. This lets you abstract the property so that you can change the property's value for each unique configuration without updating the underlying template.

For example, the following line specifies a template property in the machine type's URL:
    
    
    machineType: zones/**{{ properties["zone"] }}**/machineTypes/n1-standard-1

In a configuration that uses this template, you can set the value of `zone` in the `properties` section of the template:
    
    
    imports:
    - path: vm_template.jinja
    
    resources:
    - name: my-vm
      type: vm_template.jinja
      **properties :
        zone: us-central1-a**

Deployment Manager will know to pass in the value of `zone` to the underlying template.

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Understand how to [create a basic template](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template). 
  * Understand how to [create a configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-basic-configuration)



## Creating a template property

To create a template property:

###  Jinja 

In Jinja, define a property using the following syntax:
    
    
    {{ properties["PROJECT_NAME"] }}

For example:
    
    
    - name: vm-{{ env["deployment"] }}
      type: compute.v1.instance
      properties:
        zone: us-central1-a
        machineType: zones/{{ properties["zone"] }}/machineTypes/n1-standard-1
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

In Python, define a property using the following syntax:
    
    
      context.properties["PROPERTY_NAME"]
    

For example:
    
    
    resources.append({
        'name': 'vm-' + context.env['deployment'],
        'type': 'compute.v1.instance',
        'properties': {
            'zone': 'us-central1-a',
            'machineType': ''.join(['zones/', context.properties['zone'],
                                    '/machineTypes/n1-standard-1']),
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

## Setting values for template properties on the top-level config

On the top-level configuration, you can set values for template properties using the syntax:
    
    
    imports:
    - path: vm_template.jinja
    
    resources:
    - name: my-vm
      type: vm_template.jinja
      **properties :
        zone: us-central1-a**

You must set values for all template properties in the template. For example, if a template has template properties `zone`, `image`, `network`, you must define values for all of those properties in the top-level configuration.

If certain template properties have default values, consider using [schemas](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/using-schemas) to set these default values. A template property with a default value can be omitted from the top-level configuration if the default value is appropriate for the deployment.

## Setting values for template properties on the command-line

Instead of supplying values for template properties in the parent file importing the template, Deployment Manager offers the ability to set these values directly in the Google Cloud CLI. You can skip creating the top-level YAML file; Deployment Manager will automatically generate a top-level configuration for your deployment based on the information in your request.

For example, assume you have the following template which has a template property called `zone`:
    
    
    - name: vm-{{ env["deployment"] }}
      type: compute.v1.instance
      properties:
        zone: us-central1-a
        machineType: zones/{{ properties["zone"] }}/machineTypes/n1-standard-1
        disks:
        - deviceName: boot
          type: PERSISTENT
          boot: true
          autoDelete: true
          initializeParams:
            sourceImage: projects/debian-cloud/global/images/family/debian-11
        networkInterfaces:
        - network: global/networks/default

With the Google Cloud CLI, you can pass in this template file directly and provide the values for your template properties on the command-line. For example, the following request passes in the template and specifies the `zone` property directly on the command-line:
    
    
    gcloud deployment-manager deployments create a-single-vm --template vm_template.jinja \
        --properties zone:us-central1-a
    

Keep in mind that:

  * All values are parsed as YAML values. For example, `version: 3` is passed in as an integer. If you want to specify it as a string, put escaped single quotes around the value, `version: \'3\'`.

  * Boolean values are case insensitive, so `TRUE`, `true`, and `True` are treated the same.

  * You must pass in all required properties defined by the template. You cannot provide just a subset of the properties. If certain properties have default values, you can omit the property from the command-line.




To specify multiple properties, provide comma-separated key:value pairs. It does not matter in what order you specify the pairs. For example:
    
    
    gcloud deployment-manager deployments create my-igm \
        --template vm_template.jinja \
        --properties zone:us-central1-a,machineType:n1-standard-1,image:debian-9

After running this command, Deployment Manager creates a deployment using the template you provided. You can confirm that the deployment has been created using the Google Cloud console or the gcloud CLI. For information on viewing a deployment, read [Viewing a manifest](https://docs.cloud.google.com/deployment-manager/docs/deployments/viewing-manifest#view_a_manifest).

## What's next

  * Populate information about your projects and deployments using [environment variables](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/use-environment-variables).
  * Add a template permanently to your project as a [composite type](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-composite-types).
  * [Host templates externally](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/hosting-templates-externally) to share with others.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
