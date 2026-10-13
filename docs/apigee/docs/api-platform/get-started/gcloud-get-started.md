---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/gcloud-get-started/
title: Getting started using gcloud with Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:01.844938+00:00
---

# Getting started using gcloud with Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/gcloud-get-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Getting started using gcloud with Apigee Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The `**gcloud apigee**` CLI enables you to perform the following: 

  * View API proxies
  * Create and manage API products
  * Deploy and undeploy API proxies, and view deployment details
  * View information about developers and apps
  * List your environments and organizations
  * Manage third-party applications that call Apigee API proxies



In addition, the `**gcloud beta apigee**` CLI enables you to deploy and manage archives in your Apigee environment. 

The following sections describe how to install, authorize, and use the `gcloud apigee` and `gcloud beta apigee` CLIs, and optionally set environment variables. 

## Before you begin

Ensure that you have met the [prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/overview#prerequisites) for using Apigee, including installing the [Google Cloud SDK](https://docs.cloud.google.com/sdk/install). 

**Note:** As an alternative, you can use the [Google Cloud Shell](https://console.cloud.google.com/?cloudshell=true). The Google Cloud Shell is a command-line environment that already includes the Google Cloud SDK, so you wouldn't need to install it. 

##  Installing the gcloud beta apigee components 

To access the `gcloud beta apigee` commands, you must install the complete gcloud beta component, as follows:
    
    
    gcloud components install beta

To confirm that the beta component has been installed, enter the following command:
    
    
    gcloud components list

You should see the beta component in the list, as follows: 

Status | Name | ID | Size  
---|---|---|---  
Installed | gcloud Beta Commands | beta | < 1 MiB  
  
For more information, see [Managing SDK components](https://docs.cloud.google.com/sdk/docs/components).

##  Authenticate for the gcloud CLI 

See [Authenticate for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate#user-accounts) for instructions on how to authenticate. 

For example, to authorize access using your user account and perform other common Cloud SDK setup steps, use the following command: 
    
    
    gcloud init

Follow the prompts to authenticate the account, grant access permissions, and initialize your Cloud SDK installation, as described in [Initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize). 

Alternatively, to authorize access without performing any additional set up, use the following command: 
    
    
    gcloud auth login

Follow the browser-based authorization flow to authenticate the account and grant access permissions. 

For more information about authorizing and revoking access to the gcloud CLI, see [Credentials](https://docs.cloud.google.com/sdk/docs/cheatsheet#credentials).

## Setting environment variables for gcloud commands

The Apigee API and gcloud CLI examples provided throughout the documentation use one or more of the environment variables defined in the following table.

By setting the environment variables upfront to meaningful values in your environment, you can copy and paste the example requests to execute them in your own environment with minimal or no modifications. 

Environment variable | Description  
---|---  
`$API` | Name of your API proxy.  
`$APIPRODUCT` | Name of the API product.  
`$APP` | ID of an app.  
`$DEVELOPER_EMAIL` | Email address of the developer.  
`$ENV` | Name of your environment, such as `test` or `prod`.  
`$ID` | Resource ID.  
`$KEY` | Consumer key.  
`$NAME` | Name of your resource.  
`$ORG` | Your Apigee organization.  
`$REV` | Revision number of your API proxy.  
`$SHAREDFLOW` | Name of your shared flow.  
`$TYPE` | [Resource type](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files#resourcetypes).  
  
## Using the gcloud CLI 

Use the `gcloud` CLI as follows: 
    
    
    gcloud apigee [GROUP](https://docs.cloud.google.com/sdk/gcloud/reference/apigee#GROUP) [[GCLOUD_WIDE_FLAG](https://docs.cloud.google.com/sdk/gcloud/reference/apigee#GCLOUD-WIDE-FLAGS) …]

For more information about the available command groups and flags, see [gcloud apigee](https://docs.cloud.google.com/sdk/gcloud/reference/apigee). 

For example, the following command lists the API proxies in your organization: 
    
    
    gcloud apigee apis list --organization=**$ORG**

The following provides an example of the response for the `my-org` organization: 
    
    
    Using Apigee organization `myorg`
     - hello-world
     - weather-app
     

## More information 

For more information, see:

  * [gcloud apigee](https://docs.cloud.google.com/sdk/gcloud/reference/apigee)
  * [gcloud beta apigee](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee)
  * [gcloud command-line tool overview](https://docs.cloud.google.com/sdk/gcloud)
  * [Managing SDK components](https://docs.cloud.google.com/sdk/docs/components)
  * [Scripting gcloud CLI commands](https://docs.cloud.google.com/sdk/docs/scripting-gcloud)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
