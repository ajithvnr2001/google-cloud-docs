---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/create-configuration-file/
title: Creating a Basic Configuration \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:36.873719+00:00
---

# Creating a Basic Configuration  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/create-configuration-file/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Creating a Basic Configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a configuration that can be used to create a deployment. To learn more about deployments, read [Creating a Deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments).

A configuration file defines all the Google Cloud resources that make up a deployment. You must have a configuration file to create a deployment. A configuration file must be written in YAML syntax.

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Understand basics about [configuration files](https://docs.cloud.google.com/deployment-manager/docs/configuration).



## Configuration file structure

A configuration file is written in YAML format and has the following structure:
    
    
    #  imported templates, if applicable
    imports:
      #  path relative to the configuration file
    - path: path/to/template.jinja
      name: my-template
    - path: path/to/another/template.py
      name: another-template
    
    resources:
      - name: NAME_OF_RESOURCE
        type: TYPE_OF_RESOURCE
        properties:
          property-a: value
          property-b: value
          ...
          property-z: value
      - name: NAME_OF_RESOURCE
        type: TYPE_OF_RESOURCE
        properties:
          property-a: value
          property-b: value
          ...
          property-z: value
    

Each of the sections define a different part of the deployment:

  * The `imports` sections is a list of [template files](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template) that will be used by the configuration. Deployment Manager recursively expands any imported templates to form your final configuration.

  * The `resources` section is a list of resources that make up this deployment. A resource can be:

    * A Google-managed base type, such a Compute Engine VM instance.
    * An imported template
    * A [composite type](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#composite_types).
    * A [type provider](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#basetypes).



You can also include other optional sections, such as the `outputs` and `metadata` sections. The `outputs` section allows you to [expose data from your templates and configurations as outputs](https://docs.cloud.google.com/deployment-manager/docs/configuration/expose-information-outputs) for other templates in the same deployment to consume or as outputs for your end users, while the `metadata` section lets you use other features, like [setting explicit dependencies](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-explicit-dependencies) between resources.

At the minimum, a configuration must always declare the `resources` section, followed by a list of resources. Other sections are optional.

## Declaring a resource type

Each resource in your configuration must be specified as a type. Types can be a Google-managed base type, a composite type, a type provider, or an imported template.

Google-managed base types are types that resolve to Google Cloud resources. For example, a Cloud SQL instance or a Cloud Storage bucket is a Google-managed base type. You can declare these types using the following syntax:
    
    
    type: <api>.<api-version>.<resource-type>
    

For example, a Compute Engine instance would have the following type:
    
    
    type: compute.v1.instance
    

For a BigQuery database, the type might be:
    
    
    type: bigquery.v2.dataset
    

For a list of all supported types, use the following command:
    
    
    gcloud deployment-manager types list
    

For a full list of supported Google-managed base types, see [Supported Resource Types](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-resource-types).

If you are using a [composite](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-composite-types) or [type provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/calling-type-provider), declare the type as follows:
    
    
    # Composite type
    
    resources:
    - name: my-composite-type
      type: [PROJECT]/composite:[TYPE_NAME]
    

For a type provider:
    
    
    # Base type
    
    resources:
    - name: my-base-type
      type: [PROJECT_ID]/[TYPE_PROVIDER_NAME]:[TYPE_NAME]
    

You can also create resources using Google-managed type providers (beta). For a list of Google Cloud type providers, see [Supported Type Providers](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types).

If you want to use [templates](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template), declare the template as a type, with the template name or path as the value of `type`. For example, the following configuration imports a template called my_vm_template.jinja and provides it as a type:
    
    
    imports:
    - path: path/to/template/my_vm_template.jinja
      name: my-template.jinja
    
    resources:
    - name: my-first-virtual-machine
      type: my-template.jinja
    

For more information about templates, read [Creating a Basic Template](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template).

## Declaring resource properties

After declaring the type of resource, you must also give the resource a `name` and specify the properties you want for the resource. For example, the following configuration file defines a virtual machine instance called `vm-created-by-deployment-manager` and its desired properties. Deployment Manager uses this information to create a VM instance that has these properties.
    
    
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
    

To determine the `properties` of a resource, you use the API documentation for the resource:

  * See the request format in the `insert` or `create` method for the resource.
  * If the request URI contains the zone, add the zone to the properties.
  * For arrays, use the YAML list syntax to list the elements of the array. For example, if you are creating a Compute Engine instance using the API, you must provide an array of disks to attach to the instance, in the following format:
        
        "disks": [
          {
            "type": "PERSISTENT",
            "deviceName": "disk1",
            ...
          },
          {
            "type": "PERSISTENT",
            "deviceName": "disk2",
            ...
          }
        ]
        

In your Deployment Manager configuration, you add these disks using the following syntax:
        
        disks:
        - deviceName: disk1
          type: PERSISTENT
          ...
        - deviceName: disk2
          type: PERSISTENT
        




You can also provide any writable property of that resource. To determine if a property is writeable, use the API reference documentation for the resource type. For example, the [Compute Engine reference](https://docs.cloud.google.com/compute/docs/reference/latest) marks certain properties that are output only, so you cannot define these properties in your configuration, as they are immutable.

Some APIs require a minimum set of properties for creating a resource. A [Compute Engine persistent disk](https://docs.cloud.google.com/compute/docs/reference/latest/disks/insert), for example, requires the disk name, image source, size of the disk, and so on, when create a new disk. For information about a specific resource, review the API reference for that resource.

### Defining template properties

If you import a template to use in your configuration, you would use the `properties` section to define values for [template properties](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/define-template-properties) instead of resource properties. Alternatively, if the template has no template properties, you can omit the `properties` section altogether.

## Creating resources from different Google Cloud services

Finally, a configuration file can create resources from different Google Cloud services. For example, the following configuration file creates resources from Compute Engine and BigQuery:
    
    
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
    
    - name: big-query-dataset
      type: bigquery.v2.dataset
      properties:
        datasetReference:
          datasetId: example_id
    

## Supported resource types and properties

See the full list of supported Google-managed resources in the [Supported Resource Types](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-resource-types) documentation.

## What's next

  * [Preview your configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration/preview-configuration-file) before you commit to deploying it.
  * Once you are happy with the configuration, use it to [create a deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments).
  * Eventually, you should consider reworking your configuration files to use [templates](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
