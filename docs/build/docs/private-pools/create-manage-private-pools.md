---
url: https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools/
title: Create and manage private pools \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:03.682810+00:00
---

# Create and manage private pools  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Create and manage private pools Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create, update, view, and delete Cloud Build private pools. If you're not familiar with private pools, read [Private pools overview](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview).

## Before you begin

  1. Create a [new Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project) or choose an existing project. You'll use this project to create the private pool.

  2. Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com&redirect=%7B%7Bdynamic_data.site_values.console_url%7D%7Dbuild/docs/private-pools/set-up-private-pool-environment)

  3. To use the command-line examples in this guide, install and configure the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).

**Note:** If you've installed gcloud CLI previously, make sure you have the latest available version by running `gcloud components update`.
  4. Optional: For builds to access private resources from your Virtual Private Cloud network, you must set up a peering connection between your Virtual Private Cloud network and the Virtual Private Cloud network where private pools reside. For instructions, see [set up your environment to create private pools](https://docs.cloud.google.com/build/docs/private-pools/set-up-private-pool-environment#setup-private-connection).

  5. Optional: Familiarize yourself with machine type configurations and regional availability. For more information, see [`workerconfig`](https://docs.cloud.google.com/build/docs/private-pools/private-pool-config-file-schema#workerconfig) in the private pool configuration file schema documentation.




## Create a private pool

To ensure that has the necessary permissions to create a private pool, ask your administrator to grant the [Cloud Build WorkerPool Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.workerPoolOwner) (`roles/cloudbuild.workerPoolOwner`) IAM role to on your service account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You can create up to 10 private pools per Google Cloud project per region. To create a private pool, do the following:

###  Google Cloud console 

  1. Open the **Worker Pool** page in the Google Cloud console:

[ Open the Cloud Build worker pool page](https://console.cloud.google.com/cloud-build/settings/worker-pool)

  2. Click **Create private pool**.

The **Create private pool** page is displayed.

Enter the following information to create your private pool:

  3. **Name** : Enter a name for your private pool. This value can only contain alphanumeric characters `/[a-z][0-9]/` or dashes `-`. The name of your private pool must be between 1 and 63 characters.

  4. **Region** : Select the region in which you want the private pool to be created.

  5. **Machine configuration** : Configure the following:

     1. **Series** : Choose a machine series.

     2. **Machine type** : This setting shows the machine types, based on the machine series that you selected, that the worker pool can use. The available machine types vary by region.

     3. **Disk size** : Enter a disk size for your private pool. Specify a value greater than or equal to 100 and less than or equal to 4000. If you don't provide a value, then Cloud Build uses a disk size of 100.

     4. **Nested virtualization** : If you selected a C3 series machine, then you can enable [nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview). This feature lets you run virtual machine (VM) instances inside of other VMs so you can create your own virtualization environments.

  6. Under **Worker release** , select **Release channel** , and then one of the following channels:

     * `regular` (default)
     * `stable`
     * `rapid`

Or, select **Release** and choose the [release version](https://docs.cloud.google.com/build/docs/release-channels#available-releases) number you want to use.

See [Cloud Build release channels](https://docs.cloud.google.com/build/docs/release-channels) for a description of each release channel and what it means to select a specific version number.

  7. Under **Network type** , select one of the following options:

     1. **Default network** : Select this option if your instance is accessible through the public internet. When the **Default network** option is selected, your private pool uses the service producer network. For more information, see [Set up environment to use private pools in a VPC network](https://docs.cloud.google.com/build/docs/private-pools/set-up-private-pool-to-use-in-vpc-network).

     2. **Private network** : Select this option if your instance is hosted on a private network, then do the following:

        1. **Project** : Select your Google Cloud project ID.

        2. **Network** : Select your network from the drop-down menu. If you have not created a network, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks) to learn how to create a network.

        3. **IP range** : Enter the internal IP range that the Cloud Build producer network can use to allocate to VMs maintaining a connection with private repositories.

You can specify the range using the Classless Inter-Domain Routing (CIDR) routing notation in the format `STARTING_IP_ADDRESS/SUBNET_PREFIX_SIZE`. For example, `192.0.2.0/24` has a prefix length of 24. The first 24 bits of the IP range are used as the subnet mask (`192.0.2.0`) while the possible hosts addresses range from `192.0.2.0` to `192.0.2.255`.

The value of your prefix length must not exceed `/29`. If no value is specified for the range, a default value of `/24` is automatically assigned. If no value is specified for the prefix length, IP addresses are automatically assigned within the peered VPC network. If no value is specified for the IP address, the IP address is automatically assigned a range within the peered VPC network.

**Note:** You can only specify an **IP range** if you've specified a **Network**. If you've specified a **Network** , the **IP range** is optional.
     3. **Assign external IPs** : This option is selected by default to allow private pools to access the public internet. Clear this box to restrict access to your private network.

  8. Click **Create** to create your private pool.




###  gcloud 

You have two options for creating a new private pool using `gcloud`: you can either pass in your private pool config file to the `gcloud` command, or pass the configuration options directly to the `gcloud` command.

**Pass the private pool config file to the`gcloud` command:**

  1. Create the [private pool config file](https://docs.cloud.google.com/build/docs/private-pools/private-pool-config-file-schema) in the YAML or the JSON format.

  2. Run the following `gcloud` command, where `PRIVATEPOOL_ID` is a unique identifier for your private pool, `PRIVATEPOOL_CONFIG_FILE` is the name of your private pool config file, and `REGION` is the [region](https://docs.cloud.google.com/build/docs/locations) where you want to create your private pool:
         
         gcloud builds worker-pools create PRIVATEPOOL_ID --config-from-file PRIVATEPOOL_CONFIG_FILE --region REGION
         

You should see an output similar to the following:
         
         Created [https://cloudbuild.googleapis.com/v1/projects/gcb-docs-project/locations/us-central1/workerPools/private-pool].
         NAME                 CREATE_TIME                STATUS
         private-pool  2018-11-19T16:08:24+00:00  RUNNING
         




**Pass the configuration options directly to the`gcloud` command:**

Run the following `gcloud` command:
    
    
        gcloud builds worker-pools create PRIVATEPOOL_ID \
            --project=PRIVATEPOOL_PROJECT_ID \
            --region=REGION \
            --peered-network=PEERED_NETWORK \
            --worker-machine-type=PRIVATEPOOL_MACHINE_TYPE \
            --worker-disk-size=PRIVATEPOOL_DISK_SIZE_GB \
            --no-public-egress \
            --worker-release=CHANNEL_OR_VERSION
    

Where:

  * `PRIVATEPOOL_ID`: a unique identifier for your private pool. This value should be 1-63 characters, and valid characters are `[a-zA-Z0-9_-]+`.
  * `PRIVATEPOOL_PROJECT_ID`: the ID of the Google Cloud project where you want to create your private pool.
  * `REGION`: one of the [supported regions](https://docs.cloud.google.com/build/docs/locations).
  * `PEERED_NETWORK`: the network resource URL of the network that is peered to the service producer network. `PEERED_NETWORK` must be of the format `projects/NETWORK_PROJECT_ID/global/networks/NETWORK_NAME`, where `NETWORK_PROJECT_ID` is the project ID of the Google Cloud project that holds your VPC network and `NETWORK_NAME` is the name of your VPC network. If you don't specify a value, Cloud Build uses the service provider network.
  * `PRIVATEPOOL_DISK_SIZE_GB`: the size of the disk attached to the private pool. Specify a value greater than or equal to 100 and less than or equal to 4000. If not provided, Cloud Build uses a disk size of 100. `--worker-disk-size` is overridden if you specify a different disk size using `--disk-size` during `gcloud builds submit`.
  * `PRIVATEPOOL_MACHINE_TYPE`: the machine type of the worker. If left blank, Cloud Build uses the default value of `e2-standard-2`. For a list of supported machine types, see [Private pool config file schema](https://docs.cloud.google.com/build/docs/private-pools/private-pool-config-file-schema#machinetype). `--worker-machine-type` is overridden if you specify a different machine type using `--machine-type` during `gcloud builds submit`.
  * `--no-public-egress`: If this flag is set, the private pool is created without an external IP address. Set this flag if you're [creating the private pool within a VPC Service Controls perimeter](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls).
  * `CHANNEL_OR_VERSION`: the release channel or version of the private pool. For more information, see [Cloud Build release channels](https://docs.cloud.google.com/build/docs/release-channels).



###  API 

  1. [Create your private pool config file](https://docs.cloud.google.com/build/docs/private-pools/worker-pool-config-file-schema) named `workerpool.json`.

  2. Use [cURL](http://curl.haxx.se/) to call the Cloud Build API:
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)"
                 -H "Content-Type: application/json" \
                 https://cloudbuild.googleapis.com/v1/projects/PRIVATEPOOL_PROJECT_ID/locations/REGION/workerPools/?workerPoolId=PRIVATEPOOL_ID -d @workerpool.json
         

Where:

     * `PRIVATEPOOL_PROJECT_ID`: the ID of the Google Cloud project where you want to create your private pool.
     * `PRIVATEPOOL_ID`: the ID for your private pool. This value should be 1-63 characters, and valid characters are `[a-zA-Z0-9_-]+`.
     * `REGION`: one of the [supported regions](https://docs.cloud.google.com/build/docs/locations) to create your private pool.



### Create a private pool within a VPC Service Controls perimeter

To create a private pool with a VPC Service Controls perimeter, see [Using VPC Service Controls](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls).

## Update a private pool

To ensure that has the necessary permissions to create a private pool, ask your administrator to grant the [Cloud Build WorkerPool Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.workerPoolEditor) (`roles/cloudbuild.workerPoolEditor`) IAM role to on your service account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To update the configuration of a private pool, do the following:

###  Console 

  1. Open the **Worker pool** page in the Google Cloud console:

[ Open the Cloud Build worker pool page](https://console.cloud.google.com/cloud-build/settings/worker-pool)

  2. Select the project in which you created the private pool.

  3. Click the private pool name.

  4. In the **Edit private pool** page, update the machine type, disk size, and other settings as needed.

  5. Click **Save**.




###  gcloud 

**By updating the private pool config file:**

  1. Update the field you want to change in your [private pool config file](https://docs.cloud.google.com/build/docs/private-pools/worker-pool-config-file-schema).

  2. Run the following command, where `PRIVATEPOOL_ID` is the unique identifier for your private pool, `REGION` is the region where your private pool is located, and `PRIVATEPOOL_CONFIG_FILE` is the name of your private pool config file:
         
         gcloud builds worker-pools update PRIVATEPOOL_ID \
             --region=REGION \
             --config-from-file=PRIVATEPOOL_CONFIG_FILE
         




**By passing in the value to update directly to the`gcloud builds worker-pools update` command:**
    
    
       gcloud builds worker-pools update PRIVATEPOOL_ID \
           --region=REGION \
           --worker-disk-size=PRIVATEPOOL_DISK_SIZE \
           --worker-machine-type=PRIVATEPOOL_MACHINE_TYPE
           --worker-release=CHANNEL_OR_VERSION
    

Where:

  * `PRIVATEPOOL_ID`: the ID of your existing private pool. You cannot update this value; you must specify an existing private pool ID.
  * `REGION`: the [region](https://docs.cloud.google.com/build/docs/locations) where you created your private pool.
  * `PRIVATEPOOL_DISK_SIZE`: the updated disk size.
  * `PRIVATEPOOL_MACHINE_TYPE` is the updated machine type.
  * `CHANNEL_OR_VERSION`: is the [release channel](https://docs.cloud.google.com/build/docs/release-channels) or version. If not specified, the default value is `stable`.



###  API 

  1. In your [private pool config file](https://docs.cloud.google.com/build/docs/private-pools/worker-pool-config-file-schema), update the disk size and machine type as needed.

  2. Use [cURL](http://curl.haxx.se/) to call the Cloud Build API, replacing the variables with the appropriate values:
         
         curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             https://cloudbuild.googleapis.com/v1/projects/PRIVATEPOOL_PROJECT_ID/locations/REGION/workerPools/PRIVATEPOOL_ID \
             -d @workerpool.json
         

Where:

     * `PRIVATEPOOL_ID`: the ID of your private pool.
     * `PRIVATEPOOL_PROJECT_ID`: the ID of the Google Cloud project that contains your private pool.
     * `REGION`: the [region](https://docs.cloud.google.com/build/docs/locations) where you created your private pool.



## View the details of your private pool

To ensure that has the necessary permissions to create a private pool, ask your administrator to grant the [Cloud Build WorkerPool Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.workerPoolViewer) (`roles/cloudbuild.workerPoolViewer`) IAM role to on your service account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To view the details of a private pool:

###  Console 

  1. Open the **Worker pool** page in the Google Cloud console:

[ Open the Cloud Build worker pool page](https://console.cloud.google.com/cloud-build/settings/worker-pool)

  2. Select the project in which you created the private pool

  3. Click the private pool name.

The **Edit private pool** page is displayed.




###  gcloud 

If you don't know the ID of your private pool, run the following command to list the details of your private pool:
    
    
    gcloud builds worker-pools list --region=REGION --project=PRIVATEPOOL_PROJECT_ID
    

Where:

  * `PRIVATEPOOL_PROJECT_ID` is the ID of the Google Cloud project that contains the private pool.
  * `REGION` is the region of the private pool.



You should see an output similar to the following:
    
    
    NAME                                                                  CREATE_TIME                STATUS
    projects/[PRIVATEPOOL_PROJECT_ID]/locations/us-central1/workerPools/[PRIVATEPOOL_ID]      2018-11-19T16:08:24+00:00  RUNNING
    

If you know your private pool ID, then run the following command to get more information about the private pool:
    
    
    gcloud builds worker-pools describe PRIVATEPOOL_ID \
        --region=REGION \
        --project=PRIVATEPOOL_PROJECT_ID
    

Where

  * `PRIVATEPOOL_ID`: the ID of your private pool.
  * `REGION`: the [region](https://docs.cloud.google.com/build/docs/locations) where you created your private pool.
  * `PRIVATEPOOL_PROJECT_ID`: the ID of the Google Cloud project that contains your private pool.



###  API 

If you don't know the ID of your private pool, then run the following [cURL](http://curl.haxx.se/) command to list the details of your private pool, where `PRIVATEPOOL_PROJECT_ID` is the ID of the Google Cloud project that contains the private pool:
    
    
        curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            https://cloudbuild.googleapis.com/v1/projects/PRIVATEPOOL_PROJECT_ID/locations/REGION/workerPools
    

If you know your private pool ID, run the following curl command to get the details of your private pool:
    
    
        curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            https://cloudbuild.googleapis.com/v1/projects/PRIVATEPOOL_PROJECT_ID/locations/REGION/workerPools/PRIVATEPOOL_ID
    

Where

  * `PRIVATEPOOL_ID`: the ID of your private pool.
  * `PRIVATEPOOL_PROJECT_ID`: the ID of the Google Cloud project that contains your private pool.
  * `REGION`: the [region](https://docs.cloud.google.com/build/docs/locations) where you created your private pool.



## View private pool price estimates

When you create or update a private pool, the **Monthly estimate** sidebar on the **Create private pool** and **Edit private pool** pages shows an estimate of how much your pool will cost to run per month. The calculation is based on the following factors:

  * Number of virtual CPUs
  * Machine type
  * Memory
  * Build minutes
  * Region, for N2D and C3 machines only



The estimated pricing does not include costs for additional disk size beyond the 100 GB included by default. The estimated pricing may be different from final pricing depending on the final build configuration, actual build minutes used, and other factors. For more information, see [Cloud Build pricing](https://cloud.google.com/build/pricing).

## Delete a private pool

To ensure that has the necessary permissions to create a private pool, ask your administrator to grant the [Cloud Build WorkerPool Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.workerPoolOwner) (`roles/cloudbuild.workerPoolOwner`) IAM role to on your service account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To delete a private pool, do the following:

###  Console 

  1. Open the **Worker pool** page in the Google Cloud console:

[ Open the Cloud Build worker pool page](https://console.cloud.google.com/cloud-build/settings/worker-pool)

  2. In the row with your private pool, click the trash icon.




###  gcloud 

To delete a private pool, run the `gcloud builds worker-pools delete` command:
    
    
     gcloud builds worker-pools delete PRIVATEPOOL_ID \
         --region=REGION \
         --project=PRIVATEPOOL_PROJECT_ID
    

Where:

  * `PRIVATEPOOL_ID`: the ID of your private pool.
  * `PRIVATEPOOL_PROJECT_ID`: the ID of the Google Cloud project that contains your private pool.
  * `REGION`: the [region](https://docs.cloud.google.com/build/docs/locations) where you created your private pool.



After the private pool is deleted, you should see an output similar to the following:
    
    
     Deleted [https://cloudbuild.googleapis.com/v1/projects/gcb-docs-project/locations/us-central1/workerPools/[PRIVATEPOOL_ID].
    

###  API 

Use [cURL](http://curl.haxx.se/) to call the Cloud Build API:
    
    
      curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          https://cloudbuild.googleapis.com/v1/projects/PRIVATEPOOL_PROJECT_ID/locations/REGION/workerPools/PRIVATEPOOL_ID
    

Where:

  * `PRIVATEPOOL_ID`: the ID of your private pool.
  * `PRIVATEPOOL_PROJECT_ID`: the ID of the Google Cloud project that contains your private pool.
  * `REGION`: the [region](https://docs.cloud.google.com/build/docs/locations) where you created your private pool.



## What's next

  * Learn how to [run builds in private pools](https://docs.cloud.google.com/build/docs/private-pools/run-builds-in-private-pool).
  * Learn how to [use VPC Service Controls with private pools](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
