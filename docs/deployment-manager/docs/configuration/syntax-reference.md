---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/syntax-reference/
title: Syntax Reference \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:32:24.712877+00:00
---

# Syntax Reference  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/syntax-reference/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Syntax Reference Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the syntax used by Deployment Manager. Use this guide as a reference for what syntax to use in your configurations and templates.

## Syntax for configurations and templates

### Basic syntax

  * `resources` \- A set of resources to create. 
    * `name` \- The name for this instantiation of this resource.
    * `type` \- The resource type. This can be a base type like `compute.v1.instance`, a type provider such as `gcp-types/compute-v1:addresses`, or an imported template. [See the list of supported type providers](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types).
    * `properties` \- The properties of this resource. For an introduction, see Template properties.
    * `metadata` \- Extra configuration for this resource. See a list of fields in Metadata.



**Example**
    
    
    resources:
    - name: vm-instance
      type: compute.v1.instance
      properties:
        machineType: zones/us-central1-a/machineTypes/n1-standard-1
        ...
    

### Access Control

If you want to set IAM policies on your resources, you use an `accessControl` section:

  1. Add the `accessControl` section to the top-level configuration for each resource for which you want to apply access control policies.

  2. Specify the desired `gcpIamPolicy` for the resource. Each IAM policy can contain a list of bindings. Each binding binds a list of principals to a role.




For detailed information on controlling access to resources, see [Setting access control in a configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration/set-access-control-resources).

For example, the following `accessControl` section adds bindings that grant these roles to users:

User | Role  
---|---  
`alice@example.com` | `roles/pubsub.editor`  
  
  * `my-other-app@appspot.gserviceaccount.com`
  * `jane@example.com`

| `roles/pubsub.publisher`  
      
    
    resources:
    - name: a-new-pubsub-topic
      type: pubsub.v1.topic
      properties:
        ...
    
      accessControl:
        gcpIamPolicy:
          bindings:
          - role: roles/pubsub.editor
            members:
            - "user:alice@example.com"
          - role: roles/pubsub.publisher
            members:
            - "user:jane@example.com"
            - "serviceAccount:my-other-app@appspot.gserviceaccount.com"
    

### References

For information on when to use references, and more examples, learn more about [creating references](https://docs.cloud.google.com/deployment-manager/docs/configuration/use-references).

You can use **references** to the properties of other resources instead of directly providing values. For example, if you want to create an instance group manager that uses an instance template from the same deployment, instead of explicitly typing the full link for the instance template, you can use a reference with the syntax `$(ref.instance-template.selfLink)`.

To see which properties you can create references to, see the `get` method for the resource's API. For example, for a list of all the properties for a VM instance, see the response for the [`instances.get()` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get).

You declare references using a similar syntax to the [JSONPath 'dot' notation](http://goessner.net/index.html). Use the following syntax to declare a reference:
    
    
    $(ref.RESOURCE_NAME.PATH_TO_PROPERTY)
    

For properties that are lists, such as the network interfaces for a Compute Engine instances, use the following syntax:
    
    
    $(ref.RESOURCE_NAME.LIST_PROPERTY[index].ITEM)
    

**Examples**
    
    
    $(ref.exampleInstance.networkInterfaces[0].natIp)
    $(ref.exampleInstance.serviceAccounts[0].email)
    

### Deployment-specific environment variables

When you create a deployment, Deployment Manager creates environment variables that contain pieces of information about your deployment, such as the current project name, the deployment's name, and so on.

For a full list of available environment variables, see [Environment variables](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/use-environment-variables).

To use an environment variable:
    
    
    {{ env["deployment"] }} # Jinja
    
    context.env["deployment"] # Python

**Example**
    
    
    - type: compute.v1.instance
      name: vm-{{ env["deployment"] }}
    

### Template properties

A template property is an arbitrary property that you create. Instead of hard-coding a value, you could declare a template property and set the value of the property in the top-level configuration, as opposed to statically providing the property and value directly in the template. To create a template property, use the syntax:
    
    
    {{ properties["property-name"] }} # Jinja
    
    context.properties["property-name"] # Python

Then in your top-level configuration or parent template, set the value of the property:
    
    
    imports:
    - path: vm_template.jinja
    
    resources:
    - name: my-vm
      type: vm_template.jinja
      properties:
       property-name: example-value
    

Learn more about [Template Properties](https://docs.cloud.google.com/deployment-manager/docs/configuration/adding-templates#template_properties).

### Outputs

In the outputs section, you can define arbitrary key/value pairs that expose certain information about your deployment. You provide the key and set the value either as a static string, a reference to a property, a template variable, or an environment variable.

  * `outputs` \- Declares a list of outputs that users can call in their resource properties. 
    * `name` \- Name of the output property.
    * `value` \- Value of the output property.



**Example**
    
    
    resources:
    - name: vm-instance
      type: compute.v1.instance
      ...
    
    outputs:
    - name: databaseIp
      value: $(ref.vm-instance.networkInterfaces[0].natIp)
    - name: databaseName
      value: example-database
    

Learn more about [Outputs](https://docs.cloud.google.com/deployment-manager/docs/configuration/expose-information-outputs).

### Metadata

The `metadata` section contains special metadata that you can apply on a per-resource basis. Deployment Manager has unique metadata that triggers certain features. For example, the `dependsOn` feature relies on a metadata entry.

#### Depends on

The `dependsOn` property creates explicit dependencies between your resources. For example, specifying that Resource A depends on Resource B ensures that Resource B is always created before Resource A.
    
    
    metadata: the metadata for this resource
      dependsOn: Any explicit dependencies to another resource.
    

**Example**
    
    
    resources:
    - name: vm-instance
      type: compute.v1.instance
      properties:
        machineType: zones/us-central1-a/machineTypes/n1-standard-1
        ...
      metadata:
        dependsOn:
        - persistent-disk-1
        - a-new-network-1
    

Learn more about creating [explicit dependencies](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-explicit-dependencies).

## Syntax for schemas

A schema is a way for you to control how your users can interact with your templates. The following syntax can be used in your schema file. Learn more about [Schemas](https://docs.cloud.google.com/deployment-manager/docs/configuration/using-schemas).

### info

The `info` property contains meta information about the schema. This includes information such as a title, a version number, a description and so on.

At a minimum, provide a title and description in this property.

**Example**
    
    
    info:
      title: MongoDB Template
      author: Jane
      description: Creates a MongoDB cluster
      version: 1.0
    

### imports

The `imports` field contains a list of corresponding files that are required for templates that use this schema. When you upload a template with a schema that has a list of imports, Deployment Manager checks that all of the files in the imports property were uploaded along with the template.

**Example**
    
    
    imports:
      - path: helper.py
        name: mongodb_helper.py
    

### required

The required field contains a list of elements from the properties field that are required in the template that uses the schema. Any elements not specified in this required field are considered optional.

**Example**
    
    
    required:
      - name
    
    properties:
      name:
        type: string
        description: Name of your Mongo Cluster
    
      size:
        type: integer
        default: 2
        description: Number of Mongo Secondaries
    

### properties

The `properties` field contains the JSON schema rules for this document. Elements described in the properties field can be set by users of the template. You can use all supported JSON schema validations for these properties, such as:

  * `type` (string, boolean, integer, number, ...)
  * `default`
  * `minimum / exclusiveMinimum / maximum / exclusiveMaximum`
  * `minLength / maxLength`
  * `pattern`
  * `not X / allOf X, Y / anyOf X, Y / oneOf X, Y`



At a minimum, it is good practice to include a type and description of the field so users know what is an acceptable value for the property. For optional properties, it is also good practice to include a default value.

Read the [JSON Schema Validation documentation](http://json-schema.org/latest/json-schema-validation.html#anchor53) for a list of validation keywords.

**Example**
    
    
    properties:
      name:
        type: string
        description: Name of your Mongo Cluster
    
      size:
        type: integer
        default: 2
        description: Number of Mongo Secondaries
        minimum: 1
    

## What's next

  * Learn about [References](https://docs.cloud.google.com/deployment-manager/docs/configuration/use-references).
  * Learn about [Environment Variables](https://docs.cloud.google.com/deployment-manager/docs/configuration/adding-templates#environment_variables).
  * Learn about [Template Properties](https://docs.cloud.google.com/deployment-manager/docs/configuration/adding-templates#template_properties).
  * Learn about [Outputs](https://docs.cloud.google.com/deployment-manager/docs/configuration/outputs).
  * Learn about [Schemas](https://docs.cloud.google.com/deployment-manager/docs/configuration/using-schemas). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
