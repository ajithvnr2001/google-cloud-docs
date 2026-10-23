---
url: https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-single-node-private-cloud/
title: Create a VMware Engine single node private cloud \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:01.424588+00:00
---

# Create a VMware Engine single node private cloud  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-single-node-private-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a VMware Engine single node private cloud

This document describes how to create a single node private cloud. Single node private clouds help you get started with your Google Cloud VMware Engine experience with non-production usage such as pilots and proof-of-concept evaluations. Single node private clouds contain only one node and one cluster. You can expand your single node private cloud to three nodes at any time to convert it to a standard private cloud.

See [Single node private clouds](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud#single-node) for conceptual information about single node private clouds.

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

## Before you begin

  * [Create a VMware Engine network](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-create-vmware-engine-network) if you haven't done so already.



## Create a single node private cloud

Create a single node private cloud with the following instructions.

###  Console 

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project  
where you want to create the single node private cloud.

  3. Click **Create**.

  4. Select **Standard private cloud**.

  5. Select a location where you want the private cloud deployed.

  6. Select the node type for your primary cluster.

  7. Select **Single node** to create a single node private cloud.

  8. Fill out the rest of the details of your private cloud and click **Save**.




###  gcloud 

To create a single node private cloud using the gcloud CLI:

  1. Optional: If you don't know the names of available regions and zones for your project, you can list them by running the [`gcloud vmware locations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/locations/list):
         
         gcloud vmware locations list
         

  2. To create a single node private cloud, which expires after 60 days, use the [`gcloud vmware private-clouds create` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/create):
         
         gcloud vmware private-clouds create PRIVATE_CLOUD_ID \
            --description= "" \
            --location=ZONE \
            --cluster="CLUSTER_ID" \
            --node-type-config=type=standard-72, count=1 \
            --management-range=IP_ADDRESS \
            --vmware-engine-network="REGION" \
            --type=TIME_LIMITED
         

Replace the following:

     * `PRIVATE_CLOUD_ID`: the name for this private cloud.
     * `CLUSTER_ID`: the cluster ID for this request
     * `ZONE`: the zone for this private cloud
     * `IP_ADDRESS`: the IP address and range for this private cloud, for example `192.168.1.0/24`
     * `REGION`: the region for this private cloud

Output example:
    
    Create in progress for private cloud [projects/PROJECT_ID/locations/ZONE/operations/OPERATION_ID].
    

  3. Optional: If you want to check the status of the private cloud creation, use the [`gcloud vmware operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/operations/describe) and [`gcloud vmware private-clouds list`](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/list) commands.
         
         gcloud vmware operations describe OPERATION_ID \
            --location=ZONE
         
         
         gcloud vmware private-clouds list \
            --location=ZONE
         

The output is similar to the following:
         
         NAME                  PROJECT       LOCATION  CREATE_TIME STATE         VCENTER_FQDN
         PRIVATE_CLOUD_ID      PROJECT_ID    ZONE      2023-03-01T13:08:21.507Z  CREATING VCENTER_FQDN
         

  4. Optional: If you want to check the details of the private cloud, run the [`gcloud vmware private-clouds describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/describe):
         
         gcloud vmware private-clouds describe PRIVATE_CLOUD_ID \
            --location=ZONE
         

  5. Get the vCenter and NSX credentials, respectively, by running [`gcloud vmware private-clouds credentials describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/describe):
         
         gcloud vmware private-clouds vcenter credentials describe PRIVATE_CLOUD_ID \
            --location=ZONE
         
         
         gcloud vmware private-clouds nsx credentials describe PRIVATE_CLOUD_ID \
            --location=ZONE
         




###  REST 

To create a single node private cloud using the VMware Engine API, do the following:

  1. Create a single node private cloud (expires after 60 days) by making a `POST` request:
         
         POST https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds?private_cloud_id=PRIVATE_CLOUD_ID
         
         {
          "description": "my private cloud",
          "network_config": {
            "vmware_engine_network": "projects/PROJECT_ID/locations/REGION/vmwareEngineNetworks/REGION-default",
            "management_cidr": "192.168.0.0/24"
          },
          "management_cluster": {
            "cluster_id": "CLUSTER_ID",
            "node_type_configs": {
              "standard-72": {
                "node_count": 1
              }
            }
          },
          "type": "TIME_LIMITED"
         }
         

Replace the following:

     * `PROJECT_ID`: the project for this request
     * `ZONE`: the zone for this private cloud
     * `PRIVATE_CLOUD_ID`: the private cloud name for this request
     * `REGION`: the region for this private cloud
     * `CLUSTER_ID`: the cluster ID for this request
  2. Optional: Check the status of the private cloud creation (may take up to two hours) by making a `POST` request to the operation:
         
         POST "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/operations/OPERATION_ID
         

List the private clouds in a zone by making a `POST` request:
         
         POST "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds
         

Replace the following:

     * `PROJECT_ID`: the ID for this request
     * `ZONE`: the zone for this private cloud
     * `OPERATION_ID`: the operation ID for this private cloud
  3. Optional: Get details of the private cloud by making a `GET` request:
         
         GET https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID
         

     * `PROJECT_ID`: the ID for this project
     * `PRIVATE_CLOUD_ID`: the ID for this private cloud
     * `ZONE`: the zone for this private cloud
  4. Get the vCenter and NSX credentials, respectively, by making separate `GET` requests:
         
         GET https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID:showVcenterCredentials
         
         
         GET https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID:showNsxCredentials
         




It takes approximately 30 minutes to 2 hours for VMware Engine to create your private cloud and make it available for access from the Google Cloud console.

## What's next

  * [Get sign-in credentials for management appliances](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-vsphere-client).
  * [Manage your private cloud resources and activity](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
