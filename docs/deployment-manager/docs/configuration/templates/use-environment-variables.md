---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/use-environment-variables/
title: Using deployment-specific environment variables \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:55.344473+00:00
---

# Using deployment-specific environment variables  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/use-environment-variables/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Using deployment-specific environment variables Stay organized with collections  Save and categorize content based on your preferences. 

For each of your deployments, Deployment Manager creates pre-defined environment variables that contain information inferred from your deployment. Use these environment variables in your Python or Jinja2 templates to get information about your project or deployment.

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Understand how to [create a basic template](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template). 
  * Understand how to [create a configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-basic-configuration)



## Available environment variables

The following environment variables are automatically set by Deployment Manager. They are replaced everywhere you use them in your templates. For example, use the `project_number` variable to add the project number to the name of a service account.

Environment variable | Value | `deployment` | The name of the deployment.  
---|---  
`name` | The `name` declared in the configuration that is using the template. This can be useful if you want the name you declare in the configuration to be the name of the resource in the underlying templates.  
`project` | The [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) for this deployment.  
`project_number` | The [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) for this deployment.  
`current_time` | The UTC timestamp when expansion started for the deployment.  
`type` | The resource type declared in the top-level configuration.  
`username` | The current Deployment Manager user.  
  
## Using an environment variable

Use the following syntax to add an environment variable to your templates:
    
    
    {{ env["deployment"] }} # Jinja
    
    context.env["deployment"] # Python

In your template, use the variables as in these examples:

###  Jinja 
    
    
    - type: compute.v1.instance
      name: vm-**{{ env["deployment"] }}**
      properties:
        machineType: zones/us-central1-a/machineTypes/f1-micro
        serviceAccounts:
        - email: **{{ env['project_number'] }}**-compute@developer.gserviceaccount.com
          scopes:
          - ...

###  Python 
    
    
    def GenerateConfig(context):
      resources = []
      resources.append ({
        'name': 'vm-' + **context.env["deployment"]**,
        'type': 'compute.v1.instance',
        'properties': {
           'serviceAccounts': [{
             'email': **context.env['project_number']** + '-compute@developer.gserviceaccount.com',
             'scopes': [...]
           }]
        }
        ...}]
      return {'resources': resources}

## What's next

  * Add a template permanently to your project as a [composite type](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-composite-types).
  * [Host templates externally](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/hosting-templates-externally) to share with others.
  * Add [schemas](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/using-schemas) to ensure users interact with your templates correctly.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
