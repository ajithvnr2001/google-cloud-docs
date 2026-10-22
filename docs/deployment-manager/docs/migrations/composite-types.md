---
url: https://docs.cloud.google.com/deployment-manager/docs/migrations/composite-types/
title: Converting composite types to supported templates \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:09.892381+00:00
---

# Converting composite types to supported templates  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/migrations/composite-types/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Converting composite types to supported templates Stay organized with collections  Save and categorize content based on your preferences. 

A composite type is one or more templates, configured to work together, that are added permanently to Deployment Manager. For an overview of composite types, and steps to create them, visit [Adding a template as a composite type](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-composite-types).

However, [the composite types feature is currently deprecated](https://docs.cloud.google.com/deployment-manager/docs/deprecations/composite-types), and will no longer be usable in new or updated deployments on **February 22, 2022**. Your deployment configurations are affected if they use resource types with the format `type: PROJECT_ID/composite:TEMPLATE_NAME`.

This page describes the steps to convert composite types to supported templates.

# Separating your composite type into individual templates

To convert your composite type into supported templates, you can either manually create a single template that contains all of the elements of the composite type, or separate out the elements of your composite type into individual template files.

For more information on templates and creating templates, refer to [Creating a basic template](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template).

# Moving and importing your template files

You must copy all individual template files to the same location as your deployment. To avoid naming conflicts, we recommend that you use a separate folder from the folder you used for your deployment configuration.

You must also ensure that your configuration file is set up to import the individual template file or files. For information about importing templates, visit [Importing the template](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template#importing_the_template).

# Replacing references to your composite type

Next, update your deployments to use your individual template or templates directly, instead of the previous composite type.

Find and replace all instances of composite type syntax, such as:
    
    
    type: PROJECT_ID/composite:main-template
    

Replace the composite type syntax with a direct reference to a template, such as:
    
    
    type: PATH_TO/main-template.jinja
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
