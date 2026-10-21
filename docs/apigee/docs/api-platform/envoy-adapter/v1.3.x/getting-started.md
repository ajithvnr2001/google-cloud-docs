---
url: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.3.x/getting-started/
title: Getting started \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:56:51.239629+00:00
---

# Getting started  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.3.x/getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Getting started Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This topic explains how to download and install Apigee Adapter for Envoy. 

##  Overview 

In the following steps, you will download and set up two applications on your system: the **Apigee Remote Service CLI** and the **Apigee Remote Service for Envoy**. 

##  Download and install 

  1. Create a base directory on your system in which to install the Remote Service CLI and the Remote Service. For example: 
         
         mkdir ~/envoy-adapter
         cd ~/envoy-adapter
         export ENVOY_HOME=$PWD

  2. For the remaining steps, be sure you are in the `$ENVOY_HOME` directory: 
         
         cd $ENVOY_HOME

  3. Download the [ latest release](https://github.com/apigee/apigee-remote-service-cli/releases) of the **Apigee Remote Service CLI** into `$ENVOY_HOME`. Be sure to grab the correct package for your operating system. 
  4. Download the [ latest release](https://github.com/apigee/apigee-remote-service-envoy/releases) of the **Apigee Remote Service for Envoy** into `$ENVOY_HOME`. 
  5. Create directories to hold the extracted package contents inside `$ENVOY_HOME`: 
         
         mkdir apigee-remote-service-cli
         mkdir apigee-remote-service-envoy

  6. Extract the tar file contents into the new directories: 
         
         tar -xf apigee-remote-service-cli_version_platform.tar.gz -C apigee-remote-service-cli
         tar -xf apigee-remote-service-envoy_version_platform.tar.gz -C apigee-remote-service-envoy

  7. Delete the tar files.
  8. When you complete these steps, `$ENVOY_HOME` contains two directories: 
         
         ls -1 .
           apigee-remote-service-cli
           apigee-remote-service-envoy

  9. Create the following environment variables for the `apigee-remote-service-cli` and `apigee-remote-service-envoy` directories. You will use these environment variables throughout the documentation: 
         
         export CLI_HOME=$PWD/apigee-remote-service-cli
         export REMOTE_SERVICE_HOME=$PWD/apigee-remote-service-envoy




##  Next steps 

You are now ready to set up and use the Apigee Adapter for Envoy to proxy API calls with Apigee API management. The following examples show you how to use the adapter with Apigee: 

Example | Description  
---|---  
[Istio sidecar with Apigee hybrid](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.3.x/example-hybrid) | Deploy the Remote Service into an Istio service mesh. The remote service provides the endpoints to the Istio sidecar proxies that are installed on your target services. This steup lets you use the Apigee Adapter for Envoy with an Apigee hybrid installation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
