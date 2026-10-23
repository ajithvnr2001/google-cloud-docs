---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-management/
title: Accessing management appliances \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:17.418112+00:00
---

# Accessing management appliances  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Accessing management appliances

This page describes the steps to connecting to management appliances for your private clouds.

Before you can connect to management appliances, you need network connectivity from your client machine to the VMware Engine network. Establish network connectivity using one of the following options:

  * Connect from a VM on the VPC network that you used when creating the private cloud. Use the internal IP address or the FQDN of the management appliance.
  * [Connect from your on-premises network to VPC network](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-connect-to-onpremises#connecting-from-your-onpremises-network-to-vpc).



## Google Cloud CLI and API prerequisites

To use the `gcloud` command line tool or the API to manage your VMware Engine resources, we recommend configuring the tools as described below.

###  gcloud 

  1. Set your default project ID:
         
         gcloud config set project PROJECT_ID
         

  2. Set a default region and zone:
         
         gcloud config set compute/region REGION
         
         
         gcloud config set compute/zone ZONE
         




For more information on the `gcloud vmware` tool, [see the Cloud SDK reference docs](https://docs.cloud.google.com/sdk/gcloud/reference/vmware).

###  API 

API examples in this documentation set use the `cURL` command-line tool to query the API. A valid access token is required as part of the `cURL` request. There are many ways to get a valid access token; the following steps use the `gcloud` tool to generate a access token:

  1. Login to Google Cloud:
         
         gcloud auth login
         

  2. Generate access token and export to TOKEN:
         
         export TOKEN=`gcloud auth print-access-token`
         

  3. Verify that TOKEN is set properly:
         
         echo $TOKEN
         




Now, use the authorization token in your requests to the API. For example:
    
    
    curl -X GET -H "Authorization: Bearer \"$TOKEN\"" -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations
    

### Python

Python code samples in this documentation use the [VMware Engine library](https://cloud.google.com/python/docs/reference/vmwareengine/latest) to communicate with the API. To be able to use this approach, the library needs to be installed and the [Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials) should be configured.

  1. Download and install the Python library:
         
         pip install google-cloud-vmwareengine
         

  2. Configure the ADC information by executing those command in your shell:
         
         gcloud auth application-default login
         

Or, use a Service Account key file:
         
         export GOOGLE_APPLICATION_CREDENTIALS="FILE_PATH"
         




For more information about the library, visit the [reference page](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest) or view [code samples on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/vmwareengine/cloud-client).

To access a management appliance of your private cloud, do the following:

## Get connection details for management appliances

###  Console 

To get the URL to a management appliance using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project that contains the private cloud.

  3. Select the private cloud you want to access.

  4. On the private cloud details page, select the **Management appliances** tab.

  5. Click the **URL** column for vCenter Server or NSX Manager.




###  gcloud 

To get the connection details to a management appliance using the Google Cloud CLI, do the following:

  1. To show management appliance URLs, run the [`gcloud vmware private-clouds describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/describe):
         
         gcloud vmware private-clouds describe \
          --private-cloud=PRIVATE_CLOUD_ID \
          --project=PROJECT_ID \
          --location=REGION




Replace the following:

  * `PRIVATE_CLOUD_ID`: the private cloud private cloud ID for this request.
  * `PROJECT_ID`: the project name for this request.
  * `REGION`: the region of the private cloud. If this is stretched private cloud, specify the zone for this private cloud.



###  API 

  1. To show management appliance connection details using the VMware Engine API, make a `GET` request:
         
         GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateCloud/PRIVATE_CLOUD_ID"

Replace the following:

     * `PROJECT_ID`: the project name for this request.
     * `REGION`: the region of the private cloud. If this is stretched private cloud, specify the zone for this private cloud.
     * `PRIVATE_CLOUD_ID`: the private cloud private cloud ID for this request.



## Get credentials for management appliances

After you create a private cloud, you can generate credentials for management appliances of that private cloud, like vCenter Server and NSX Manager. To access those appliances for your private cloud for the first time, you must use the user ID and password generated by the Google Cloud console.

**Note:** By default, the password for management components expires after 365 days. Make sure that you change the password before it expires.

To add additional users to your vCenter Server or NSX Manager appliances, [contact Cloud Customer Care](https://docs.cloud.google.com/vmware-engine/docs/preview/getting-support).

###  Console 

To get the password to a management appliance using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project that contains the private cloud.

  3. Select the private cloud you want to access.

  4. On the private cloud details page, select the **Management appliances** tab.

  5. In the **Login info** column for vCenter Server or NSX Manager, click **Key details**.

  6. Copy the credentials for vCenter Server or NSX Manager from the prompt that appears.




###  gcloud 

To get the password to a management appliance using the Google Cloud CLI, do the following:

  1. To show vCenter user credentials, run the [`gcloud vmware private-clouds vcenter credentials describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/vcenter/credentials/describe):
         
         gcloud vmware private-clouds vcenter credentials describe \
          --private-cloud=PRIVATE_CLOUD_ID \
          --project=PROJECT_ID \
          --location=REGION

  2. To show NSX user credentials, run the [`gcloud vmware private-clouds nsx credentials describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/nsx/credentials/describe):
         
         gcloud vmware private-clouds nsx credentials describe \
          --private-cloud=PRIVATE_CLOUD_ID \
          --project=PROJECT_ID \
          --location=REGION




Replace the following:

  * `PRIVATE_CLOUD_ID`: the private cloud private cloud ID for this request.
  * `PROJECT_ID`: the project name for this request.
  * `REGION`: the region of the private cloud. If this is stretched private cloud, specify the zone for this private cloud.



###  API 

  1. To show vCenter user credentials using the VMware Engine API, make a `GET` request:
         
         GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateCloud/PRIVATE_CLOUD_ID/showVcenterCredentials"

  2. To show NSX user credentials using the VMware Engine API, make a `GET` request:
         
         GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateCloud/PRIVATE_CLOUD_ID/showNsxCredentials"

Replace the following:

     * `PROJECT_ID`: the project name for this request.
     * `REGION`: the region of the private cloud. If this is stretched private cloud, specify the zone for this private cloud.
     * `PRIVATE_CLOUD_ID`: the private cloud private cloud ID for this request.



## Reset access credentials

If you misplace the credentials to vCenter Server or NSX Manager, you can reset the password to your management appliances for your private cloud using the Google Cloud CLI or Google Cloud VMware Engine by doing the following:

**Important:** If you change the password that VMware Engine generates for either vCenter Server or NSX Manager, those changes won't be reflected in the Google Cloud console.

###  Console 

To reset the password to a management appliance using the Google Cloud console, follow these steps:

  1. Follow the steps in the Get credentials for management appliances section.
  2. In the prompt that appears and contains your access credentials, click **Reset Password**.



###  gcloud 

To reset the password to a management appliance using the Google Cloud CLI, do the following:

  1. Reset vCenter user credentials by running the [`gcloud vmware private-clouds vcenter credentials reset` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/vcenter/credentials/reset):
         
         gcloud vmware private-clouds vcenter credentials reset \
          --private-cloud=PRIVATE_CLOUD_ID \
          --project=PROJECT_ID \
          --location=REGION

  2. Reset NSX user credentials by running the [`gcloud vmware private-clouds nsx credentials reset` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/nsx/credentials/reset):
         
         gcloud vmware private-clouds nsx credentials reset \
          --private-cloud=PRIVATE_CLOUD_ID \
          --project=PROJECT_ID \
          --location=REGION




Replace the following:

  * `PRIVATE_CLOUD_ID`: the private cloud private cloud ID for this request.
  * `PROJECT_ID`: the project name for this request.
  * `REGION`: the region of the private cloud. If this is stretched private cloud, specify the zone for this private cloud.



###  API 

  1. To reset vCenter user credentials using the VMware Engine API, make a `GET` request:
         
         GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateCloud/PRIVATE_CLOUD_ID/resetVcenterCredentials"
          

  2. To reset NSX user credentials using the VMware Engine API, make a `GET` request:
         
         GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateCloud/PRIVATE_CLOUD_ID/resetNsxCredentials"
          

Replace the following:

     * `PROJECT_ID`: the project name for this request.
     * `REGION`: the region of the private cloud. If this is stretched private cloud, specify the zone for this private cloud.
     * `PRIVATE_CLOUD_ID`: the private cloud private cloud ID for this request.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
