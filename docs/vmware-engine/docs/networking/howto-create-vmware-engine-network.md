---
url: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-create-vmware-engine-network/
title: Create a VMware Engine network \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:48.844126+00:00
---

# Create a VMware Engine network  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-create-vmware-engine-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a VMware Engine network

This document describes how to create a _Standard VMware Engine Network_ using the VMware Engine portal, gcloud CLI, or API. You can create multiple VMware Engine networks to isolate private clouds and define unique VPC network peerings. VMware Engine networks handle connections to and from private clouds according to a [network policy](https://docs.cloud.google.com/vmware-engine/docs/preview/networking/network-policies) that you define separately.

**Note:** Projects created before November 2023 have _Legacy VMware Engine Networks_ that are no longer available in newer projects. Google automatically created these networks for you; as such, these steps are only applicable for standard networks. For more information on legacy and standard networks, review the [Network overview](https://docs.cloud.google.com/vmware-engine/docs/networking/vmware-engine-network).

## Before you begin

### Google Cloud CLI and API requirements

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

## Create a VMware Engine network

Create a VMware Engine network using the Google Cloud console, gcloud CLI, or VMware Engine API:

###  Console 

To create a VMware Engine network using the VMware Engine:

  1. In the Google Cloud console, go to the **VMware Engine networks** page.

[Go to VMware Engine networks](https://console.cloud.google.com/vmwareengine/networks)

  2. Click **Select a project** and then select the organization, folder, or project where you want to create the VMware Engine network.

  3. Click **Create**. A VMware Engine network creation form opens.

  4. Enter a VMware Engine network name.

  5. Enter a description for the network, for example "My standard VEN 1", and then click **Create**.

  6. Optional: Confirm the creation of your network by navigating to the **VMware Engine networks** menu item. All VMware Engine networks are listed in the table on this page.




The following list describes each field during network creation in more detail:

  * **Name:** Permanent unique identifier of the VMware Engine network.
  * **Description:** Additional information that's visible on the details page of the VMware Engine network.
  * **Network type:** Network type identifier used to support networking use cases and standard private cloud deployments.
  * **Region:** This depends on whether you are using Standard VMware Engine or Legacy VMware Engine networks.

    * For legacy networks, this is the region where the network has connectivity.
    * For standard networks, this field is always set to global.



###  gcloud 

To create a VMware Engine network using the gcloud CLI:

  1. Run [`gcloud vmware networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/networks/create):
         
         gcloud vmware networks create NETWORK_ID \
           --type=STANDARD \
           --description="DESCRIPTION"

Replace the following:

     * `NETWORK_ID`: the ID for your VMware Engine network.
     * `DESCRIPTION`: a description for this network.
  2. Optional: If you want to list all VMware Engine networks to confirm the creation of the new network, use the [`gcloud vmware networks list` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/networks/list):
         
         gcloud vmware networks list \
           --location=global




### API

To create a VMware Engine network using the VMware Engine API, do the following:

  1. To create a VMware Engine network, make a `POST` request:
         
         POST "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/vmwareEngineNetworks?vmware_engine_network_id=NETWORKD_ID"
         
         '{
           "type": "standard",
           "description": "DESCRIPTION"
         }'

Replace the following:

     * `PROJECT_ID`: the ID of the project where you want to create the network.
     * `NETWORK_ID`: the ID for your VMware Engine network.
     * `DESCRIPTION`: a description for this network.
  2. Optional: To list all VMware Engine networks to confirm the creation of the new network, make a `GET` request. Replace `PROJECT_ID` with the project ID where the network is located.
         
         GET https://vmwareengine.googleapis.com/v1/projects//locations/global/vmwareEngineNetworks




## Update a VMware Engine network

Update a VMware Engine network using the Google Cloud console, gcloud CLI, or VMware Engine API:

###  Console 

  1. In the Google Cloud console, go to the **VMware Engine networks** page.

[Go to VMware Engine networks](https://console.cloud.google.com/vmwareengine/networks)

  2. Click **Select a project** and then select the organization, folder, or project that contains the VMware Engine network you want to update.

  3. Click the name of the network that you want to update.

  4. On the network details page, edit the description and then click **Save**.

  5. Optional: To view the updated description, navigate to the **VMware Engine networks** menu item and click the network to see the details.




###  gcloud 

To update a VMware Engine network using the gcloud CLI, do the following:

  1. Update the description of a VMware Engine network by running the [`gcloud vmware networks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/networks/update):
         
         gcloud vmware networks update NETWORK_ID \
           --description='DESCRIPTION'

Replace the following:

     * `NETWORK_ID`: the ID for your VMware Engine network.
     * `DESCRIPTION`: an updated description for this network.
  2. Optional: If you want to view the updated attribute, use the [`gcloud vmware networks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/networks/describe):
         
         gcloud vmware networks describe NETWORK_ID




### API

To update a VMware Engine network using the VMware Engine API, do the following:

  1. To update the description of a VMware Engine network, make a `PATCH` request:
         
         PATCH "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/vmwareEngineNetworks/NETWORK_ID?update_mask=description"
         
         '{
           "description":"DESCRIPTION"
         }'
         

Replace the following:

     * `PROJECT_ID`: the project ID where the network is located.
     * `LOCATION`: the location of the network, either `global` for standard networks or the region for legacy networks.
     * `NETWORK_ID`: the ID for your VMware Engine network.
     * `DESCRIPTION`: an updated description for this network.
  2. Optional: If you want to view the updated attribute, make a `GET` request:
         
         GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/vmwareEngineNetworks/NETWORK_ID"




## What's next

  * [Get sign-in credentials for management appliances](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-vsphere-client).
  * [Manage your private cloud resources and activity](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
