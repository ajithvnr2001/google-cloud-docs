---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-context/
title: View and switch context \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:32.534931+00:00
---

# View and switch context  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-context/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  View and switch context Stay organized with collections  Save and categorize content based on your preferences. 

Organization and project are the two available contexts within the Google Distributed Cloud (GDC) air-gapped appliance resource hierarchy. You can switch between organizations and projects using gdcloud CLI properties.

## View the existing settings

After you initialize the gdcloud CLI, view the existing settings for your organization and project using the following commands.

List gdcloud CLI properties for the currently active [configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-manage-configurations):
    
    
    gdcloud config list
    

Print the organization console URL:
    
    
    gdcloud config get organization_console_url
    

Print the project property:
    
    
    gdcloud config get project
    

## Switch between contexts

If you want to switch to a new organization or project context, you can set the properties either in your active configuration, or in another named configuration.

### Set properties in the active configuration

Switch to a new organization:
    
    
    gdcloud config set organization_console_url ORGANIZATION_CONSOLE_URL
    

Switch to a new project:
    
    
    gdcloud config set project PROJECT_ID
    

### Set properties in a new named configuration

Assume you have created a new named configuration `example` which has been set with specific `https://console.example-org.com` and `example-project`:
    
    
    gdcloud config configurations create example
    
    gdcloud config set organization_console_url https://console.example-org.com
    gdcloud config set project example-project
    

Then you can switch to use such contexts by activating the configuration `example`:
    
    
    gdcloud config configurations activate example
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
