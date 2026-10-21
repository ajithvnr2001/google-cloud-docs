---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/download-api-proxies/
title: Downloading and uploading an API proxy configuration bundle \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:10.489793+00:00
---

# Downloading and uploading an API proxy configuration bundle  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/download-api-proxies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Downloading and uploading an API proxy configuration bundle Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

You may want to download an API proxy configuration bundle (as a zip file) from Apigee to perform one of the following tasks:

  * Import an API proxy using the API proxy configuration bundle to another organization, as described in [Importing an API proxy from an API proxy bundle](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-simple-api-proxy#importinganapiproxyfromanapiproxybundle). 
  * Unzip the API proxy to your local system. This is useful for setting up file-based API proxy development in source control or viewing the file-based version of the resources. If you modify the API proxy configuration locally, you can upload your changes as a new revision of your API proxy.



The following sections describe how to download and upload an API proxy configuration bundle. For information about the expanded contents of the zip file, see [API proxy configuration directory structure](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference).

##  Video 

**Note:** This video was recorded with a previous version of the Apigee UI; however, the concepts are still valid. 

Watch the following video to learn more about downloading and uploading an API proxy configuration bundle.

Video | Description  
---|---  
[Download API proxy (Apigee)](https://www.youtube.com/watch?v=acVv859BlsM) | Download an API proxy using the Apigee UI and API.  
  
##  Downloading an API proxy configuration bundle 

Download an API proxy configuration bundle, as described in the following sections. 

### Apigee UI

To download an API proxy configuration bundle using the Google Cloud console:

  1. In the Google Cloud console, go to the **Apigee > Proxy development > API proxies** page.

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

  2. Select the desired API proxy.
  3. Click the **Develop** tab.
  4. Select the API proxy revision that you want to download in the **Revision** menu.
  5. Click  more_vert **More revision actions > Export revision n**, where n specifies the selected revision.



### Apigee API

To download an API proxy configuration bundle using the API, see [Get API proxy revision](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/get). 

To view the contents of the API proxy configuration bundle, create a new directory and expand the zip file using a utility such as `unzip`, as shown in the following example:
    
    
    mkdir myappdir
    unzip ./my-app_app_rev3_2019_04_20.zip -d myappdir

For more information about the expanded contents of the zip file, see [API proxy configuration directory structure](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#apiproxystructure).

##  Uploading an API proxy configuration bundle 

Before you upload an API proxy configuration bundle, re-archive the API proxy configuration bundle directory if you have modified it, including any new or changed files. You can use a utility such as `zip`, as the following example shows: 
    
    
    zip my-new-proxy.zip -r .

The top-level directory in the zip file must be `/apiproxy`. For more information about the required directory structure, see [API proxy configuration directory structure](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#apiproxystructure).

**Note:** There are no special requirements for the zip file name. For example, you do not need to increment the revision number or specify the date in the file name, unless you find it useful for debugging or source control.

Upload an API proxy configuration bundle, as described in the following sections. 

### Apigee UI

To upload an API proxy configuration bundle and create a **new revision of an existing API proxy** : 

  1. In the Google Cloud console, go to the **Apigee > Proxy development > API proxies** page.

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

  2. Select the desired API proxy.
  3. Click the **Develop** tab.
  4. Click  more_vert **More revision actions > Import revision **.
  5. Click **Browse** and navigate to the zip file in your local directory and click **Open**.
  6. Click **Import**.



### Apigee API

To upload an API proxy configuration using the API, see [Update an existing API proxy revision](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/updateApiProxyRevision)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
