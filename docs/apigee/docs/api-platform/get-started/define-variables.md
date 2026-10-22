---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/define-variables/
title: Step 1: Define environment variables \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:49.656779+00:00
---

# Step 1: Define environment variables  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/define-variables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  Step 1: Define environment variables Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ng-saas/chevrons-1-setup.png)

## What you're doing in this step

This section describes how to set several environment variables that are used throughout the documentation (and especially in this configuration tutorial). Google strongly recommends that you use them so that you can enter the commands _as shown_.

This is the first of two steps you will perform at the command line before starting the Apigee provisioning wizard. 

## Perform the step

**To define environment variables on the command line:**

  1. Define the following environment variables for the current project: 
         
         PROJECT_ID="YOUR_PROJECT_ID"
         PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")
         RUNTIME_LOCATION="YOUR_RUNTIME_LOCATION"
         ANALYTICS_REGION="YOUR_ANALYTICS_REGION"
         RUNTIMEDBKEY_LOCATION="RUNTIMEDB_LOCATION"
         APPKEY_KEY_RING_NAME="RUNTIMEDB_KEY_RING_NAME"
         APPKEY_KEY_NAME="RUNTIMEDB_KEY_NAME"
         DISK_KEY_RING_NAME="DISK_KEY_RING_NAME"
         DISK_KEY_NAME="DISK_KEY_NAME"
         

Where:

     * PROJECT_ID is the Cloud project ID that you created as part of the [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites). If you're not sure what your project ID is, use Cloud console or the `gcloud projects list` command to find it.
     * PROJECT_NUMBER is the Cloud project number that you created as part of the [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites). This example issues a `gcloud` command to get the project number for you. Alternatively, you can find it in the [Google Cloud console](https://console.cloud.google.com) project dashboard or you can use the `gcloud projects list` command to find it.
     * RUNTIME_LOCATION is the physical location where your instance is located. Valid values are any Compute Engine _region_ (for paid orgs) or Compute Engine _zone_ (for eval orgs). For more information, see [Compute Engine locations](https://docs.cloud.google.com/compute/docs/regions-zones#locations).

     * ANALYTICS_REGION is the physical location at which you store your analytics data.

Valid values are a subset of the Compute Engine regions. Possible values are:

       * `asia-northeast1`
       * `asia-south1`
       * `europe-west1`
       * `us-central1`
       * `us-east1`
       * `us-west1`
       * `australia-southeast1`
       * `europe-west2`

Both eval and paid accounts use regions for the analytics location. Therefor, for paid orgs its value can be the same as the RUNTIME_LOCATION (also a region). But the value of ANALYTICS_REGION does not have to be the same as RUNTIME_LOCATION. However, there may be a performance benefit if they are the same.

For eval accounts, the analytics location is a region but the runtime location is a zone, so they will not be the same.

     * RUNTIME_LOCATION is the physical location where your application key ring and key are stored. Apigee uses an application key to encrypt application data such as KVMs, cache, and client secrets, which is then stored in the database. 

Similar to the analytics region, valid values are a subset of the Compute Engine regions. The value can be the same as your `$RUNTIME_LOCATION` (also a region) but does not have to be. There may be a performance benefit if they are the same.

     * RUNTIME_LOCATION is the name ofthe key ring the application key is stored in. The key ring's name must be unique to your organization. If you create additional regions, the key ring names for those regions cannot be the same as existing key ring names.
     * APPKEY_KEY_NAME is the name of the application key. Application key names must be unique within a given key ring. 
     * DISK_KEY_RING_NAME is the name of the disk key ring. It The disk key ring name must be different from the application key name. You will create the disk key ring in the same location as your `$RUNTIME_LOCATION`.
     * DISK_KEY_NAME is the name of the disk encryption key, which Apigee uses to encrypt runtime instance data before it is written to disk.

The following example defines environment variables for a paid org. 
    
    PROJECT_ID="my-cloud-project"
    PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")
    RUNTIME_LOCATION="us-west1"
    ANALYTICS_REGION="us-west1"
    RUNTIMEDBKEY_LOCATION="us-west1"
    APPKEY_KEY_RING_NAME="us-west1"
    APPKEY_KEY_NAME="us-west1"
    DISK_KEY_RING_NAME="us-west1"
    DISK_KEY_NAME="us-west1"

**Tip:** This example uses the `gcloud projects describe` command to get the project number. You could view the number in the [Google Cloud console](https://console.cloud.google.com) and assign the variable with the command: `PROJECT_NUMBER="1234567890"`

If this were for an eval org, the `RUNTIME_LOCATION` would be set to a zone instead of a region.

You will use the variable names, such as `$PROJECT_ID` as string literals in your commands.

Note that you might not use all of these environment variables during your provisioning and configuration.

  2. (Optional) Check your work by echoing the values you just set. Note that when you want to use a variable in your commands, precede the variable's name with a dollar sign (**$**). 
         
         echo $PROJECT_ID
         echo $PROJECT_NUMBER
         echo $ANALYTICS_REGION
         echo $RUNTIMEDBKEY_LOCATION
         echo $APPKEY_KEY_RING_NAME
         echo $APPKEY_KEY_NAME
         echo $DISK_KEY_RING_NAME
         echo $DISK_KEY_NAME
         

The responses to your `echo` commands should look like the following:
         
         Authorization: Bearer ya29.a123456678940B63hPSAMPLEsampleKKYVsample0f3pWDWZDuH2-hENkNa
         TvgZ1PD977TMvv6edBQPJezdHw040880Ol_LoD5ZDkt-i-knizia_KhA9L20sSvztL81-SAMPLE42ELPMASk2_
         1CxN
         my-cloud-project
         1234567890
         us-west1
         us-west1
         us-west1
         $RUNTIMEDB_KEY_RING_NAME
         $RUNTIMEDB_KEY_NAME
         $DISK_KEY_RING_NAME
         $DISK_KEY_NAME
         




If you encounter errors during this part of the process, see [Troubleshooting](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/troubleshooting-install).

* * *

## Progress (1/8 ... You're off to a great start!)

[1](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/wizard-select-project) [NEXT: Enable APIs](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/enable-apis) [3](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-org) [4](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-service-networking) [5](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-instance) [6](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-environment) [7](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing) [8](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-sample)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
