---
url: https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/using-references/
title: Understanding the benefits of references \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:26:13.553490+00:00
---

# Understanding the benefits of references  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/using-references/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Understanding the benefits of references Stay organized with collections  Save and categorize content based on your preferences. 

You can use _references_ to define the properties of your configuration or templates instead of directly providing values.

With references, you can access properties that are not defined until the resource is created. For example, when you define a virtual machine (VM) in your configuration, you do not know its IP address. However, you can create a reference to the IP address.

In this step, you will examine an updated `two-vms.yaml` that contains a network, as well as VM instances that reference the network.

## Opening the new configuration

Open a new `two-vms.yaml`, which defines a network called `a-new-network`:
    
    
    cd deploymentmanager-samples/examples/v2/step_by_step_guide/step4_use_references
    
    nano two-vms.yaml  # use your preferred text editor
    

### Viewing the references to the network

In the `properties` section of both your virtual machine instances, note that the value of `network` have a reference to the new network's `selfLink` property, so that the network interface property looks like this:
    
    
    networkInterfaces:
    - network: $(ref.a-new-network.selfLink)
    

## Deploying the configuration

In the sample, replace all instances of MY_PROJECT with your project ID, then deploy your configuration with the following command:
    
    
    gcloud deployment-manager deployments create deployment-with-references --config two-vms.yaml
    

To view your deployment, use the following command:
    
    
    gcloud deployment-manager deployments describe deployment-with-references
    

## Looking ahead: templates and variables

To maximize efficiency when you're building complex configurations, follow best practices such as using variables and templates.

In the next step, you will learn about templates and how they enable flexible, dynamic configurations.

## Deleting your deployment

Once again, we recommend that you delete the deployment to avoid charges. You don't need this deployment for the next step. Run the following command to delete the deployment:
    
    
    gcloud deployment-manager deployments delete deployment-with-references
    

[ Previous arrow_back  Deploying your resources  ](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/deploy-your-resources)

[ Next Understanding reusable templates  arrow_forward  ](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/create-a-template)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
