---
url: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/directives-project-setup/
title: Projects \u00a0|\u00a0 Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:31.750609+00:00
---

# Projects  |  Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/directives-project-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ Reference ](https://docs.cloud.google.com/shell/docs/apis)



Send feedback 

#  Projects Stay organized with collections  Save and categorize content based on your preferences. 

This page lists directives related to project setup.

## Project selection
    
    
    <walkthrough-project-setup></walkthrough-project-setup>
    

Inserts an interactive widget that helps the user to create or select a project to use for the tutorial.

### Parameters

Parameter | Type | Description  
---|---|---  
`billing` | Boolean  | _(Optional)_ If the value is set to `true`, prompt a user to enable billing for projects where a billing account is missing.  
  
## Project details

The following directives insert Google Cloud details related to the currently selected project.

Directive | Description  
---|---  
`<walkthrough-project-id/>` | The user's current project ID.  
`<walkthrough-project-name/>` | The user's project name.  
  
## Enable APIs
    
    
    <walkthrough-enable-apis apis="API_LIST"></walkthrough-enable-apis>
    

Inserts a button that enables Google Cloud APIs for the current project. The tutorial must be running in Google Cloud console for this to work.

You must specify an API's service name to enable it. To explore the available APIs, visit the [API Library](https://console.cloud.google.com/apis/library). When you find an API you want, you can discover its service name by setting a project in Cloud Shell and then running the following command:
    
    
    gcloud services list --available | grep API_NAME
    

### Parameters

Parameter | Description  
---|---  
`apis` | Comma-separated list of API service names to enable.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
