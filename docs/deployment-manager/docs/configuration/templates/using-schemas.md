---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/using-schemas/
title: Using Schemas \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:04:47.545808+00:00
---

# Using Schemas  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/using-schemas/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Using Schemas Stay organized with collections  Save and categorize content based on your preferences. 

A schema describes the specifications of a Deployment Manager template. If a schema exists for a template, Deployment Manager uses the schema to enforce how users can interact with the corresponding template. Schemas define a set of rules that a configuration file must meet if it wants to use a particular template.

In addition to defining the rules of a template, schemas also allow your users to interface with the templates you write, without needing to review and learn about each layer of templates. Users can simply review the requirements defined in your schema instead to learn what properties are settable or required for the respective template.

For example, you could create a schema where the corresponding template must always define a specific set of required properties, and each of these properties have their own specifications. One property must be a string, another must be an integer that is less than 100, and so on. If a user wants to apply your template in their configuration, the user reviews the schema and sets the correct properties in their configuration.

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Understand how to [create a basic template](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template). 
  * Understand how to [create a configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-basic-configuration)
  * Understand [JSON Schema](http://json-schema.org/learn).



## Example schema

The example schema is written for the Jinja templating engine. If you're using a different templating engine, your file extensions are different and the template syntax can be different.

This is a simple schema file named `vm-instance-with-network.jinja.schema`:
    
    
    info:
      title: VM Template
      author: Jane
      description: Creates a new network and instance
      version: 1.0
    
    imports:
    - path: vm-instance.jinja # Must be a relative path
    
    required:
    - IPv4Range
    
    properties:
      IPv4Range:
        type: string
        description: Range of the network
    
      description:
        type: string
        default: "My super great network"
        description: Description of network
    

The schema applies to this template, `vm-instance-with-network.jinja`:
    
    
    resources:
    - name: vm-1
      type: vm-instance.jinja
    
    - name: a-new-network
      type: compute.v1.network
      properties:
        IPv4Range: {{ properties['IPv4Range'] }}
        description: {{ properties['description'] }}

If a user wanted to use this template in their configuration, they can review the schema to learn that there is one required property they must define (`IPv4Range`) and one optional property (`description`) that they can omit or include. A user might then create a configuration file like so, making sure to provide a property named `IPv4Range`:
    
    
    imports:
    - path: vm-instance-with-network.jinja
    
    resources:
    - name: vm-1
      type: vm-instance-with-network.jinja
      properties:
        IPv4Range: 10.0.0.1/16
    

## Structure of a schema

Below is an example schema document. Deployment Manager recommends that schemas be written in YAML format, but you can also write schemas in JSON and it will be accepted by Deployment Manager.

Deployment Manager accepts schemas written according to draft 4 of the [JSON schema specifications](http://json-schema.org/docs).
    
    
    <mongodb.py.schema>
    info:
      title: MongoDB Template
      author: Jane
      description: Creates a MongoDB cluster
      version: 1.0
    
    imports:
      - path: helper.py
        name: mongodb_helper.py
    
    required:
      - name
    
    properties:
      name:
        type: string
        description: Name of your Mongo Cluster
    
      size:
        type: integer
        default: 2
        description: Number of Mongo Slaves
    
      zone:
        type: string
        default: us-central1-a
        description: Zone to run
        metadata: gce-zone
    

A valid schema file is a [JSON schema file](http://json-schema.org/learn/) with the addition of two top level fields, `info` and `imports`. The following is a brief description of each field and its valid contents.

### info

The `info` property contains meta information about the schema. This includes information such as a title, a version number, a description and so on.

At a minimum, provide a title and description in this property.

### imports

The `imports` field contains a list of corresponding files that are required for templates that use this schema. When you upload a template with a schema that has a list of imports, Deployment Manager checks that all of the files in the `imports` property were uploaded along with the template.

When you specify a file in this imports field, you can omit it from your `imports` field in the configuration. In the example above, the `imports` field imports a file name `vm-instance.jinja`:
    
    
    imports:
    - path: vm-instance.jinja
    

In the corresponding configuration file, a user can omit importing the `vm-instance.jinja` file, because it will be imported automatically when Deployment Manager inspects the schema for the template.

Import paths must be relative to the location of the schema file. This lets you store templates, schemas, and configurations in the same directory, and ensuring that the files would have valid imports if the directory is shared or moved.

### required

The `required` field contains a list of elements from the properties field that are required in the template that uses the schema. Any elements not specified in this `required` field are considered optional.

### properties

The `properties` field contains the JSON schema rules for this document. Elements described in the `properties` field can be set by users of the template. You can use all supported JSON schema validations for these properties, such as:

  * `type` (string, boolean, integer, number, ...)
  * `default`
  * `minimum / exclusiveMinimum / maximum / exclusiveMaximum`
  * `minLength / maxLength`
  * `pattern`
  * `not X / allOf X, Y / anyOf X, Y / oneOf X, Y`



At a minimum, it is good practice to include a `type` and `description` of the field so users know what is an acceptable value for the property. For optional properties, it is also good practice to include a `default` value.

Read the [JSON Schema Validation documentation](http://json-schema.org/latest/json-schema-validation.html#anchor53) for a list of validation keywords.

**Note:** Technically, you don't need to describe every property that can be set for your templates in the schema. For your own reasons, you can describe some properties and not others. It is completely up to you how much information to include. For example, a possible use case might be to include a property in the `required` field that is not described in the `properties` section, meaning that the property must be set but that you decided not to describe the property in the schema.

## Set arbitrary metadata

By default, Deployment Manager ignores any fields that are not valid JSON schema. If you need to extend your schemas to have specialized fields or properties, you can arbitrarily create any property you want and add it to your schema as long as the field or property does not overlap with any JSON schema validation keywords.

For example, you can add a metadata field that annotates one of your properties:
    
    
    properties:
      zone:
        type: string
        default: us-central1-a
        description: Zone to run
        metadata: a-special-property
    

Or you create a special variable that you might use in other applications outside of Deployment Manager:
    
    
    properties:
      size:
        type: integer
        default: 2
        description: Number of Mongo Slaves
        variable-x: ultra-secret-sauce
    

## Create a schema

A schema is a separate document that is named after the template for which it describes. Schemas must be named with the same name as the corresponding template, with `.schema` appended to the end:
    
    
    TEMPLATE_NAME.EXTENSION.schema
    

For example, for a template named `vm-instance.py`, the corresponding schema file must named `vm-instance.py.schema`. Only one schema can exist for each template.

Schemas can contain one or more of the fields described in the Structure of a schema section. Alternatively, you can also write schemas in JSON. For examples of JSON schemas, see the [JSON schema](http://json-schema.org/learn/) documentation.

## Use a schema

###  gcloud 

  
When you create a deployment using the Google Cloud CLI, Deployment Manager automatically uploads all of the relevant templates for the configuration for you. Similarly, if there are any schema files, identified by the appended `.schema` format, Deployment Manager will upload the schema and validate the deployment against the schema, before it attempts to create any resources.

To use a schema, just include it in the same local directory as your templates and configuration, and [create your deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments) as you would normally. The gcloud CLI detects and passes the schema file to Deployment Manager.

###  API 

  
Follow the instructions to [create a deployment](https://docs.cloud.google.com/deployment-manager/deployments) in the API and include the schema file inline with your request body as if you were including a template.

## What's next

  * Learn about [templates](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template).
  * Use [template properties](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/define-template-properties) to further abstract your content.
  * Populate information about your projects and deployments using [environment variables](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/use-environment-variables).
  * Add a template permanently to your project as a [composite type](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-composite-types).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
