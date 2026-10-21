---
url: https://docs.cloud.google.com/deployment-manager/docs/how-to/
title: How-To Guides \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:52.974554+00:00
---

# How-To Guides  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/how-to/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  How-To Guides Stay organized with collections  Save and categorize content based on your preferences. 

## Get started

  * ### [Walkthrough: best practices Get familiar with Deployment Manager's best practices, such as creating reusable templates for your Google Cloud environment.  ](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide)



## Building configurations

  * ### [Configurations overview Learn about configurations.  ](https://docs.cloud.google.com/deployment-manager/docs/configuration)
  * ### [Creating a basic configuration Create a basic configuration file.  ](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-basic-configuration)
  * ### [Previewing a configuration Preview a configuration before you deploy it.  ](https://docs.cloud.google.com/deployment-manager/docs/configuration/preview-configuration-file)



## Adding Templates

  * ### [Creating a basic template Create your first template.  ](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template)
  * ### [Defining template properties Template properties are arbitrary variables that you can use in place of hard coding template values.  ](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/define-template-properties)
  * ### [Using environment variables Use predefined environment variables in your templates.  ](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/use-environment-variables)
  * ### [Creating template modules Create and use template modules as helper files for your templates.  ](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-template-modules)
  * ### [Importing Python libraries If you are writing Python templates, you can import and use common Python libraries in your templates.  ](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/import-python-libraries)
  * ### [Adding templates as composite type If you plan to use certain templates regularly, add those templates permanently to Deployment Manager as composite types.  ](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-composite-types)
  * ### [Describing, listing, and deleting types List, describe, and delete types that belong to your project.  ](https://docs.cloud.google.com/deployment-manager/docs/configuration/describing-listing-deleting-types)
  * ### [Defining schemas for templates Create a schema file to enforce how users interact with your templates.  ](https://docs.cloud.google.com/deployment-manager/docs/configuration/using-schemas)
  * ### [Storing templates on an external host Learn how to use templates hosted on Google Cloud Storage or hosted on third-party sites like GitHub.  ](https://docs.cloud.google.com/deployment-manager/docs/configuration/hosting-templates-externally)



## Using References

  * ### [Using references When you define the properties for your configuration or template files, you can use references to other properties instead of directly providing property values.  ](https://docs.cloud.google.com/deployment-manager/docs/configuration/use-references)



## Exposing information from deployments

  * ### [Exposing information from deployments You can use the outputs section in your template or configuration to define a list of key/value pairs that users can call.  ](https://docs.cloud.google.com/deployment-manager/docs/configuration/expose-information-outputs)



## Creating explicit dependencies

  * ### [Creating explicit dependencies Setting a dependsOn property tells Deployment Manager to always create specific resources before others. This is useful if you need certain parts of your deployment to exist before other parts can come online.  ](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-explicit-dependencies)



## Creating Deployments

  * ### [Creating a deployment Learn how to deploy a configuration.  ](https://docs.cloud.google.com/deployment-manager/docs/deployments)
  * ### [Create deployments with Cloud Marketplace Use the Click-to-Deploy tool to launch predefined solutions on Google Cloud Deployment Manager.  ](https://docs.cloud.google.com/deployment-manager/docs/deployment-manager-and-cloud-marketplace)
  * ### [Updating a deployment Learn how to update an existing deployment.  ](https://docs.cloud.google.com/deployment-manager/docs/deployments/updating-deployments)
  * ### [Deleting a deployment Learn how to delete a deployment.  ](https://docs.cloud.google.com/deployment-manager/docs/deployments/deleting-deployments)



## Sharing resources across projects

  * ### [Using images from other projects ](https://docs.cloud.google.com/deployment-manager/docs/configuration/using-images-from-other-projects-for-vm-instances)
  * ### [Sharing types across projects ](https://docs.cloud.google.com/deployment-manager/docs/configuration/using-images-from-other-projects-for-vm-instances)



## Storing and retrieving data at runtime

  * ### [Creating and deleting RuntimeConfig resources Learn how to create and delete RuntimeConfig resources.  ](https://docs.cloud.google.com/deployment-manager/runtime-configurator/create-and-delete-runtimeconfig-resources)
  * ### [Setting and getting data Learn how to set and get variables using the Runtime Configurator.  ](https://docs.cloud.google.com/deployment-manager/runtime-configurator/set-and-get-variables)
  * ### [Deleting a variable Delete a variable.  ](https://docs.cloud.google.com/deployment-manager/runtime-configurator/deleting-a-variable)
  * ### [Watching a variable for changes Learn how to watch a variable for changes.  ](https://docs.cloud.google.com/deployment-manager/runtime-configurator/watching-a-variable)
  * ### [Creating a waiter Create a waiter to wait for a variable to a certain end condition.  ](https://docs.cloud.google.com/deployment-manager/runtime-configurator/creating-a-waiter)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
