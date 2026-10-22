---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/create-explicit-dependencies/
title: Creating Explicit Dependencies \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:14.287163+00:00
---

# Creating Explicit Dependencies  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/create-explicit-dependencies/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Creating Explicit Dependencies Stay organized with collections  Save and categorize content based on your preferences. 

In some cases, you can have dependencies between your resources, such as when you need certain parts of your environment to exist before you can deploy other parts of the environment. For example, if you want to create a new project as part of a deployment, you need to ensure that the project is created before you add any resources to it.

You can specify these dependencies using the `dependsOn` option in your configuration files or templates. When you add the `dependsOn` option for a resource, Deployment Manager creates or updates the dependencies before creating or updating the resource.

You can create dependencies between base types that are part of your deployment, either in the configuration file, or in the templates that you use for the deployment. You cannot set a dependency on template files or composite types.

For background information on base and composite types, see the [Types Overview](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#types).

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).



## Creating dependencies

To add a dependency to a resource, add a `metadata` section that contains a `dependsOn` section. Then, in the `dependsOn` section, specify one or more dependencies.

In the following example, to make `a-special-vm` dependent on the creation of two persistent disks, add the `metadata` and `dependsOn` sections for `a-special-vm`. Then, add the dependencies for each persistent disk.

In the same deployment, you must define the persistent disks that are dependencies. In this example, the disks are `persistent-disk-a` and `persistent-disk-b`:
    
    
    resources:
    - name: a-special-vm
      type: compute.v1.instances
      properties:
        ...
    
      metadata:
        dependsOn:
        - persistent-disk-a
        - persistent-disk-b
    
    - name: persistent-disk-a
      type: compute.v1.disks
      properties:
        ...
    
    - name: persistent-disk-b
      type: compute.v1.disks
      properties:
        ...
    

In this deployment, Deployment Manager creates `persistent-disk-a` and `persistent-disk-b` before creating `a-special-vm`.

**Warning:** Avoid creating dependency loops. For example, if you specify that resource A depends on resource B, and resource B depends on resource A, a dependency loop is created, and the deployment fails. Additionally, if you use [references](https://docs.cloud.google.com/deployment-manager/docs/configuration/use-references) in your deployment, implicit dependencies are created, which might also cause dependency loops.

## What's next

  * [Create a deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments).
  * Learn about [references](https://docs.cloud.google.com/deployment-manager/docs/configuration/use-references).
  * Learn more about [templates](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
