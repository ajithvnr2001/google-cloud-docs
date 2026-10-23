---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/development-mode/
title: Development mode \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:07.948590+00:00
---

# Development mode  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/development-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Development mode

This guide describes how to use the two working modes for Manufacturing Data Engine (MDE).

Starting on v1.5.0, Manufacturing Data Engine (MDE) has a `Development Mode` to protect the deployment from involuntary changes that could have an impact on the configuration of the system. By default, MDE is on **Production mode** (`Development Mode` is disabled).

### Enable development mode

You can enable the `Development Mode` either using a REST call or the console. After enabling the `Development Mode` the following actions are allowed:

  * MDE entities (types, message classes, parsers, metadata buckets and file ingestion especifications) can be deleted.
  * Configuration packages can be uploaded.
  * Configuration packages can be activated.
  * Configuration packages can be removed.



If any of these actions are triggered in `Production Mode` (`Development Mode` is disabled), you will receive an error similar to this:

`412 - The system is not in development mode and no delete operations can be executed. You will need to switch the environment mode to development first`

For more information about configuration packages, see [Configuration package lifecycle](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/configuration/lifecycle).

### REST

Enable `Development Mode` executing the REST API request with the following information:

  * **Method** : POST.
  * **Endpoint** : `/configuration/v1/environment`
  * **Request body (JSON)** :
        
        {
            "developmentMode": true
        }
        

  * **Response code:** 200 OK.

  * **Response body (JSON)** :
        
        {
            "id": "aa72b317-1148-4760-ada3-7f359f7b812e",
            "createdTime": "1742502041205",
            "operationsLogLevel": "ERROR",
            "technicalLogLevel": "DEFAULT",
            "developmentMode": true
        }
        




### Console

Enable `Development Mode` in the MDE web interface:

  1. Click the Cloud Configuration tab.
  2. Click the Production Mode toggle.
  3. A warning banner will appear on the top of the Configurations page with the following message: "Development mode is enabled", and the tag next to the toggle will change to `Development`.



![Enable the development mode](https://docs.cloud.google.com/static/manufacturing-data-engine/images/development-mode-enabled-toggle.png)

### Enable production mode

You can disable `Development Mode` either using a REST call or the console.

### REST

Disable the `Development Mode` executing the REST API request with the following information:

  * **Method** : POST.
  * **Endpoint** : `/configuration/v1/environment`.
  * **Request body (JSON)** :
        
        {
            "developmentMode": false
        }
        

  * **Response code** : 200 OK.

  * **Response body (JSON)** :
        
        {
            "id": "aa72b317-1148-4760-ada3-7f359f7b812e",
            "createdTime": "1742502041205",
            "operationsLogLevel": "ERROR",
            "technicalLogLevel": "DEFAULT",
            "developmentMode": false
        }
        




### Console

Disable the `Development Mode` on the MDE web interface:

  1. Click the Cloud Configuration tab.
  2. Click the Production Mode toggle.
  3. Confirm you want to change to `Production Mode` by clicking **Yes, switch the mode**.

![Switching mode](https://docs.cloud.google.com/static/manufacturing-data-engine/images/switching-mode-warning-message.png)

  4. The warning banner will disappear from the top of the Configurations page and the tag next to the toggle will change to `Production`.

![Enable the development mode](https://docs.cloud.google.com/static/manufacturing-data-engine/images/production-mode-enabled-toggle.png)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
