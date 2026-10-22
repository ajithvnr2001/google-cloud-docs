---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/calling-type-provider/
title: Calling a Type Provider in a Configuration \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:11.717110+00:00
---

# Calling a Type Provider in a Configuration  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/calling-type-provider/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Calling a Type Provider in a Configuration Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to use a type provider that you have created with Deployment Manager. It does not describe how to create a type provider. To learn how to create a type provider, read [Creating a Type Provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider).

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).



## Accessing type providers

Types providers are a per-project resource and are accessible according to the permissions described on the [Access Control](https://docs.cloud.google.com/deployment-manager/docs/access-control) documentation. That is:

  * **Project editors and viewers** can create and use types available to that project.
  * **Type viewers** can get a list of and use types available to that project.



You can also add another project as a type viewer so they can access your types. Read [Sharing Types Across Projects](https://docs.cloud.google.com/deployment-manager/docs/configuration/sharing-types-across-projects).

## Using a type provider

To use a type exposed by a type provider in your configuration, use the following syntax:
    
    
    type: [PROJECT_ID]/[TYPE_NAME]:[COLLECTION]
    

  * If this API is backed by an OpenAPI specification, `[COLLECTION]` would be the REST identifier for the path to the resource. For example:
        
        type: my-project/emailAddressesTypeProvider:emailAddresses/v1beta/people
        

  * If the API is backed by a Google Discovery document, `[COLLECTION]` is the path of resources leading to your desired resource in the API. For example, to create a [service account key](https://docs.cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys), the collection would be:
        
        type: my-project/example-type-provider:projects.serviceAccounts.keys
        




Now you continue configuring your type as required by the underlying API:
    
    
    resources:
    - name: Jane
      type: my-project/emailAddressesTypeProvider:emailAddresses/v1beta/people
      properties:
      - displayName: Jane
        email: jane@example.com
        ...
    

## What's next

  * Read about [creating a configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration).
  * [Create a deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments).
  * Learn how to [create a type provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider)
  * Learn more about [Advanced API Options](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/advanced-configuration-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
