---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/precog-enableapi/
title: Step 1: Enable APIs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:16.020682+00:00
---

# Step 1: Enable APIs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/precog-enableapi/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 1: Enable APIs Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/precog-enableapi.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-enableapi.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/precog-enableapi.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/precog-enableapi.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/precog-enableapi.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/precog-enableapi.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/precog-enableapi.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/precog-enableapi.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/precog-enableapi.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/precog-enableapi.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/precog-enableapi.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/precog-enableapi.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/precog-enableapi.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/precog-enableapi.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/precog-enableapi.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/precog-enableapi.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/precog-enableapi.html)



Apigee hybrid requires certain [Google Cloud service APIs](https://docs.cloud.google.com/service-usage/docs/enable-disable). In this step, you will enable the APIs that are required for your installation platform.

Use `gcloud` to enable the required APIs as explained in the following steps. If you prefer, you can use the [Cloud Console](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api) to enable the APIs. 

**Note:** The Apigee hybrid installation steps are written for the Linux/UNIX/Mac command shell. If you are using Windows, substitute the equivalent Windows command line syntax. 

  1. Complete the [Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/prerequisites), and be sure you have the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install) installed in your local shell: 
         
         gcloud --help

  2. Create a `PROJECT_ID` environment variable where the value is the ID of the Google Cloud project you plan to use for Apigee hybrid. A project ID is a unique string used to differentiate your project from all others in Google Cloud. If needed, see [Locate the project ID](https://support.google.com/googleapi/answer/7014113): 
         
         export PROJECT_ID=YOUR_PROJECT_ID

**Note:** Be sure the project ID is correct. This variable is used throughout the hybrid installation instructions. Do not include a period after the project ID. 
  3. Select the tab for your intended installation to see the command to enable the APIs: 

### OpenShift

If you will be running your clusters on OpenShift, enable the APIs with the following command: 

#### _Click to see details on the APIs_

Name | Title | Description |  apigee.googleapis.com  |  Apigee API  |  Provides communication between your project and other hybrid services and Google Cloud APIs.   
---|---|---  
apigeeconnect.googleapis.com  |  Apigee Connect API  |  Provides communication between the Apigee management plane and the runtime plane.   
cloudapis.googleapis.com  |  Google Cloud APIs  |  This is a meta service for Google Cloud APIs for convenience (OpenShift-based clusters only)   
cloudresourcemanager.googleapis.com  |  Cloud Resource Manager API  |  Used by hybrid to validate service accounts.   
compute.googleapis.com  |  Compute Engine API  |  Used for cluster management (GKE-based and OpenShift-based clusters only).   
dns.googleapis.com  |  Cloud DNS API  |  Google Cloud DNS is a scalable, reliable, and managed authoritative Domain Name System (DNS) service running on the same infrastructure as Google. (OpenShift-based clusters only).   
iam.googleapis.com  |  Identity and Access Management (IAM) API  |  Manages identity and access control for Google Cloud Platform resources, including the creation of service accounts, which you can use to authenticate to Google and make API calls. (OpenShift-based clusters only).   
iamcredentials.googleapis.com  |  IAM Service Account Credentials API  |  Service Account Credentials API allows developers to create short-lived, limited-privilege credentials for their service accounts on Google Cloud Platform. (OpenShift-based clusters only).   
pubsub.googleapis.com  |  Cloud Pub/Sub API  |  Required for the Apigee quota feature to operate.   
servicemanagement.googleapis.com  |  Service Management API  |  Google Service Management allows service producers to publish their services on Google Cloud Platform so that they can be discovered and used by service consumers. (OpenShift-based clusters only).   
serviceusage.googleapis.com  |  Service Usage API  |  Enables services that service consumers want to use on Google Cloud Platform, lists the available or enabled services, or disables services that service consumers no longer use. (OpenShift-based clusters only).   
storage-api.googleapis.com  |  Google Cloud Storage JSON API  |  Lets you store and retrieve potentially-large, immutable data objects (OpenShift-based clusters only).   
storage-component.googleapis.com  |  Cloud Storage  |  Google Cloud Storage is a RESTful service for storing and accessing your data on Google's infrastructure. (OpenShift-based clusters only).   
           
         gcloud services enable \
             apigee.googleapis.com \
             apigeeconnect.googleapis.com \
             cloudapis.googleapis.com \
             cloudresourcemanager.googleapis.com \
             compute.googleapis.com \
             dns.googleapis.com \
             iam.googleapis.com \
             iamcredentials.googleapis.com \
             pubsub.googleapis.com \
             servicemanagement.googleapis.com \
             serviceusage.googleapis.com \
             storage-api.googleapis.com \
             storage-component.googleapis.com  --project **$PROJECT_ID**
         

### Other Platforms

If you will be running your clusters on one of the following platforms run the command below to enable the required APIs:

     * GKE on-prem
     * Anthos on bare metal
     * AKS
     * GKE on AWS
     * EKS

#### _Click to see details on the APIs_

Name | Title | Description |  apigee.googleapis.com  |  Apigee API  |  Provides communication between your project and other hybrid services and Google Cloud APIs.   
---|---|---  
apigeeconnect.googleapis.com  |  Apigee Connect API  |  Provides communication between the Apigee management plane and the runtime plane.   
pubsub.googleapis.com  |  Cloud Pub/Sub API  |  Required for the Apigee quota feature to operate.   
cloudresourcemanager.googleapis.com  |  Cloud Resource Manager API  |  Used by hybrid to validate service accounts.   
      
    gcloud services enable \
        apigee.googleapis.com \
        apigeeconnect.googleapis.com \
        cloudresourcemanager.googleapis.com \
        pubsub.googleapis.com  --project **$PROJECT_ID**

### GKE on Google Cloud

If you will be running your clusters on Google Kubernetes Engine (GKE), run this command to enable the required APIs: 

#### _Click to see details on the APIs_

Name | Title | Description |  apigee.googleapis.com  |  Apigee API  |  Provides communication between your project and other hybrid services and Google Cloud APIs.   
---|---|---  
apigeeconnect.googleapis.com  |  Apigee Connect API  |  Provides communication between the Apigee management plane and the runtime plane.   
pubsub.googleapis.com  |  Cloud Pub/Sub API  |  Required for the Apigee quota feature to operate.   
cloudresourcemanager.googleapis.com  |  Cloud Resource Manager API  |  Used by hybrid to validate service accounts.   
container.googleapis.com  |  Kubernetes Engine API  |  Enable if you plan to use Google Kubernetes Engine (GKE), or GKE on-prem (Anthos) for your hybrid runtime installation.   
compute.googleapis.com  |  Compute Engine API  |  Used for cluster management (GKE-based and OpenShift-based clusters only).   
      
    gcloud services enable \
          apigee.googleapis.com \
          apigeeconnect.googleapis.com \
          cloudresourcemanager.googleapis.com \
          compute.googleapis.com \
          container.googleapis.com \
          pubsub.googleapis.com --project **$PROJECT_ID**
      

  4. (Optional) To verify that the required APIs are enabled, execute this command. If the required APIs are in the returned list, then they are enabled. 
         
         gcloud services list --project **$PROJECT_ID**




##  Next step 

Go to Step 2: [Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/precog-provision). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
