---
url: https://docs.cloud.google.com/migrate/kf/docs/2.3/quickstart/
title: Kf Quickstart \u00a0|\u00a0 Kf 2.3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:50.355999+00:00
---

# Kf Quickstart  |  Kf 2.3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.3/quickstart/

Version 2.3

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.3 ](https://docs.cloud.google.com/migrate/kf/docs/2.3)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.3/getting-started)



Send feedback 

#  Kf Quickstart Stay organized with collections  Save and categorize content based on your preferences. 

In this quickstart, you will deploy a sample Cloud Foundry app on an existing Kf cluster. 

## Before you begin

  * Complete the [Kf install steps](https://docs.cloud.google.com/migrate/kf/docs/2.3/install) for Kf.



## Pushing an application

### Prerequisites

The following are required to complete this section:

  1. A `.kubeconfig` targeting the Kf cluster.
  2. The `kf` CLI installed and in your path. See Install Kf for instructions.
  3. The `git` CLI installed and in your path.



### Prepare space

  1. Create new space:
         
         kf create-space test-space

  2. Target the space:
         
         kf target -s test-space




### Push the Cloud Foundry test app

  1. Clone the [test-app repo](https://github.com/cloudfoundry-samples/test-app).
         
         git clone https://github.com/cloudfoundry-samples/test-app go-test-app
         cd go-test-app

  2. Push the app.

**Note:** It will take a few minutes for the build to complete.
         
         kf push test-app

  3. Get the application's URL.
         
         kf apps

**Note:** The app has set the random-route property.
  4. Open the URL in your browser where you should see the app running.


[ ![Successful app push on Kf](https://docs.cloud.google.com/migrate/kf/docs/images/app-quickstart-success.png)](https://docs.cloud.google.com/static/migrate/kf/docs/images/app-quickstart-success.png)

## Clean up

These steps should return the cluster to the starting state.

  1. Delete the application.
         
         kf delete test-app

  2. Delete the Space.
         
         kf delete-space test-space




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
