---
url: https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/deploy-your-resources/
title: Deploying Your Resources \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:53.559297+00:00
---

# Deploying Your Resources  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/deploy-your-resources/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Deploying Your Resources Stay organized with collections  Save and categorize content based on your preferences. 

Now that you have a [configuration](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/create-a-configuration), you can use it to create a deployment. A deployment creates the resources that you defined in a configuration. In this tutorial, your deployment has two virtual machine (VM) instances.

To deploy your configuration, run this command:
    
    
    gcloud deployment-manager deployments create deployment-with-2-vms --config two-vms.yaml
    

Wait for the indication that you successfully created the deployment (note that your actual operation ID will differ):
    
    
    Waiting for create operation-1432319707382-516afeb5d00f1-b864f0e7-b7103978...done.
    Create operation operation-1432319707382-516afeb5d00f1-b864f0e7-b7103978 completed successfully.
    NAME           TYPE                 STATE      ERRORS  INTENT
    the-first-vm   compute.v1.instance  COMPLETED  []
    the-second-vm  compute.v1.instance  COMPLETED  []

You have created a deployment! To get a list of resources you created, run:
    
    
    gcloud deployment-manager resources list --deployment deployment-with-2-vms
    

To get more detailed information about the deployment, such as the start and end time, and the operation ID if you need to debug a deployment, run:
    
    
    gcloud deployment-manager deployments describe deployment-with-2-vms
    

In this example, you created some static configurations that were hard-coded. In future configurations, you might want to create more dynamic configurations using variables and reusable templates. Follow the rest of this guide to learn how to make this static configuration much more dynamic and useful.

## View your deployment in the Google Cloud console interface

You can also view an expanded list of all your deployments in the [Google Cloud console](https://console.cloud.google.com/), Google Cloud's graphical interface. To do so:

  1. Go to the [**Deployments**](https://console.cloud.google.com/project/_/deployments) page in the Google Cloud console.
  2. Expand your deployment to see the associated resources.

![Screenshot of expanded deployments](https://docs.cloud.google.com/static/deployment-manager/images/deployment-manager-ui-expand-step-step-guide.png)




You can open this page at any time to see your deployments in a visual tree. With more complicated deployments, this page can help you understand the hierarchy of resources in your deployment.

## Delete your deployment

You won't use this deployment for the remainder of the tutorial. Since Compute Engine resources incur charges, you should delete this deployment. Deleting a deployment also deletes all the resources in a deployment.

**If you don't delete the deployment, you will run into conflicts with future examples.**

To delete this deployment, run:
    
    
    gcloud deployment-manager deployments delete deployment-with-2-vms
    

Next, you will use _references_ to access the properties of other resources in your deployment.

[ Previous arrow_back  Understanding configurations  ](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/create-a-configuration)

[ Next Understanding references  arrow_forward  ](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/using-references)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
