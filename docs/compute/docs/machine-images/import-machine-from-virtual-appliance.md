---
url: https://docs.cloud.google.com/compute/docs/machine-images/import-machine-from-virtual-appliance/
title: Import machine images from virtual appliances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:45.497728+00:00
---

# Import machine images from virtual appliances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/machine-images/import-machine-from-virtual-appliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Import machine images from virtual appliances Stay organized with collections  Save and categorize content based on your preferences. 

The machine image import feature on Compute Engine is being deprecated and will reach end-of-support (EoS) on July 1st, 2025. We recommend that you use the new [machine image import feature on Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/machine-image-import) to import your machine images to Google Cloud. 

Use a machine image to store all the configuration, metadata, permissions, and data from one or more disks for a VM instance running on Compute Engine. For information about when and how to use machine images, see [Machine images](https://docs.cloud.google.com/compute/docs/machine-images).

This document describes the steps for importing a machine image from a [virtual appliance](https://wikipedia.org/wiki/Virtual_appliance).

## Before you begin

  * If the project that you want to import the machine image in has a [trusted image policy](https://docs.cloud.google.com/compute/docs/images/restricting-image-access) defined, add `projects/compute-image-import` to the allowed list of publishers.
  * If you are importing a virtual appliance from a different project, see [Importing across projects](https://docs.cloud.google.com/compute/docs/import/import-ovf-files#import-across-projects). 
  * Review [source VM and OVF file requirements](https://docs.cloud.google.com/compute/docs/import/import-ovf-files#requirements) in the importing virtual appliances Compute Engine guide.
  * To find out how to meet requirements before importing machine images, see [Prerequisites for importing and exporting VM images](https://docs.cloud.google.com/compute/docs/import/requirements-export-import-images).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Limitations and restrictions

  * You can share a machine image across projects. However, [shared VPC networks](https://docs.cloud.google.com/vpc/docs/shared-vpc) aren't supported.
  * This feature is not supported for projects that are protected with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
  * Machine images can't be created from source VMs that have greater than 200 TB of disks attached.



## Supported operating systems

For operating system support, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#import).

## Import machine images

You can import machine images from virtual appliances using either the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute) or [Cloud Build API](https://docs.cloud.google.com/build/docs/api/reference/rest).

###  gcloud 

Use the [`gcloud compute machine-images import` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/machine-images/import) to import a machine image from virtual appliances.
    
    
    gcloud compute machine-images import MACHINE_IMAGE_NAME \
        --source-uri=gs:SOURCE_URI \
        --os=OS
    

Replace the following:

  * `MACHINE_IMAGE_NAME`: name of the machine image that you want to import.
  * `SOURCE_URI`: path to your OVA or OVF file on Cloud Storage.
  * `OS`: operating system of the OVA file. This flag is optional by default, but it might be required in some cases. We recommend that you provide this flag.



**Example**

For example, you can use the following `gcloud` command to import a machine image called `my-machine-image` from a source OVA file called `my-ova` that is stored in the `gs://my-bucket` directory and runs `centos-7`:
    
    
    gcloud compute machine-images import my-machine-image  \
        --source-uri=gs://my-bucket/my-ova/ \
        --os=centos-7
    

###  REST 

  1. Upload the virtual appliance to [Cloud Storage](https://docs.cloud.google.com/storage/docs/uploading-objects).

  2. Send a `POST` request to the [`projects.builds.create` method](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds/create).

**Note:** Two `timeout` values are required. Default values for these are provided in the following sample requests. These default values work in most scenarios. However, if you need to adjust these values, ensure that the Cloud Build timeout is at least 3% greater than the timeout specified for the arguments (`args`) section.
         
         POST https://cloudbuild.googleapis.com/v1/projects/PROJECT_ID/builds
         {
          "timeout": "7200s",
          "steps":[
            {
              "args":[
                "-machine-image-name=MACHINE_IMAGE_NAME",
                "-ovf-gcs-path=SOURCE_URI",
                "-os=OS",
                "-client-id=api",
                "-timeout=7000s"
              ],
              "name":"gcr.io/compute-image-import/gce_ovf_import:release",
              "env":[
                "BUILD_ID=$BUILD_ID"
              ]
            }
          ],
          "tags":"gce-ovf-machine-image-import"
         }
         

Replace the following:

     * `PROJECT_ID`: project ID for the project that you want to import the OVA file into.
     * `MACHINE_IMAGE_NAME`: name for the machine image to import. For example, `my-machine-image`.
     * `SOURCE_URI`: URI for the OVA file or a directory containing OVF packages that is stored in Cloud Storage. For example, `gs://my-bucket/my-instance.ova`.
     * `OS`: operating system of the OVA file. For example, `ubuntu-1604`. This flag is optional by default, but it might be required in some cases. We recommend that you provide this flag.

For additional `args` values that can be provided, see the optional flags section of the [Compute Engine OVF import GitHub page](https://github.com/GoogleCloudPlatform/compute-image-import/tree/main/cli_tools/gce_ovf_import#optional-flags).




## Import machine images with OVF overrides

When you import a machine image from a virtual appliance, you can override the settings in the OVF file. For example, you can change the CPU or memory configuration, or you can use a custom network.

#### Custom CPU and memory

To override the CPU or memory configuration specified in the OVF file, complete the following steps:

###  gcloud 

To override the CPU or memory configuration specified in the OVF file, follow the Google Cloud CLI steps to import a machine image and specify the `--custom-cpu` and `--custom-memory` flags.

**Example**

A machine image named `my-machine-image` has the following overrides applied to the settings in the OVF file:

  * Operating system: `Ubuntu 1404`
  * CPU: `2 CPUs`
  * Memory: `2048 MB`



To import `my-machine-image` with these overrides, run the following command:
    
    
    gcloud compute machine-images import my-machine-image \
        --os=ubuntu-1404 --source-uri=gs://my-bucket/Ubuntu.ova \
        --custom-cpu=2 --custom-memory=2048MB
    

###  REST 

To override the CPU or memory configuration specified in the OVF file, follow the Compute Engine API steps to import a machine image and specify the `-machine-type` argument. This `-machine-type` represents a [predefined](https://docs.cloud.google.com/compute/docs/machine-resource#predefined-types) or N1 series [custom](https://docs.cloud.google.com/compute/docs/machine-resource#custom-types) machine type to use.

**Example**

A machine image named `my-machine-image` in the `my-project` project has the following overrides applied to the settings in the OVF file:

  * Operating system: `Ubuntu 1404`
  * CPU: `2 CPUs`
  * Memory: `2048 MB`



To import `my-machine-image` with these overrides, make the following request to the Cloud Build API.

**Note:** Two `timeout` values are required. Default values for these are provided in the following sample requests. These default values work in most scenarios. However, if you need to adjust these values, ensure that the Cloud Build timeout is at least 3% greater than the timeout specified for the arguments (`args`) section.
    
    
    POST https://cloudbuild.googleapis.com/v1/projects/my-project/builds
    {
      "timeout":"7200s",
      "steps":[
        {
          "args":[
            "-machine-image-name=my-machine-image",
            "-ovf-gcs-path=gs://my-bucket/Ubuntu.ova",
            "-os=ubuntu-1404",
            "-machine-type=custom-2-2048",
            "-client-id=api",
            "-timeout=7000s"
          ],
          "name":"gcr.io/compute-image-import/gce_ovf_import:release",
          "env":[
            "BUILD_ID=$BUILD_ID"
          ]
        }
      ],
      "tags":"gce-ovf-machine-image-import"
    }
    

#### Custom networks

To override the network configuration specified in the OVF file, complete the following steps:

###  gcloud 

To set up a custom network, follow the Google Cloud CLI steps to import a machine image and specify a `--network` flag. If the network is configured with a custom subnet mode, you must also specify `--subnet` and `--zone` flags.

**Example**

A machine image named `my-machine-image` has the following overrides applied to the settings in the OVF file:

  * Operating system: `Ubuntu 1404`
  * Network: `custom-vpc-network`
  * Subnet: `company-vpc-us-east1-c`
  * Zone: `us-east1-c`



To import `my-machine-image` with these overrides, run the following example command:
    
    
    gcloud compute machine-images import my-machine-image \
        --os=ubuntu-1404 \
        --source-uri=gs://my-bucket/Ubuntu.ova \
        --network=custom-vpc-network \
        --subnet=company-vpc-us-east1-c \
        --zone=us-east1-c
    

###  REST 

To use a custom network, follow the REST steps to import a machine image and specify a `-network` argument. If the network is configured with a custom subnet mode, you must also specify `-subnet` and `-zone` arguments.

**Example**

A machine image named `my-machine-image` has the following overrides applied to the settings in the OVF file:

  * Operating system: `Ubuntu 1404`
  * Network: `custom-vpc-network`
  * Subnet: `company-vpc-us-east1-c`
  * Zone: `us-central1-c`



To import `my-machine-image` with these overrides, make the following request to the Compute Engine API.

**Note:** Two `timeout` values are required. Default values for these are provided in the following sample requests. These default values work in most scenarios. However, if you need to adjust these values, ensure that the Cloud Build timeout is at least 3% greater than the timeout specified for the arguments (`args`) section.
    
    
    POST https://cloudbuild.googleapis.com/v1/projects/PROJECT_ID/builds
    {
      "timeout":"7200s",
      "steps":[
        {
          "args":[
            "-machine-image-name=my-machine-image",
            "-ovf-gcs-path=gs://my-bucket/Ubuntu.ova",
            "-os=ubuntu-1404",
            "-zone=us-central1-c",
            "-network=custom-vpc-network",
            "-subnet=company-vpc-us-east1-c",
            "-client-id=api",
            "-timeout=7000s"
          ],
          "name":"gcr.io/compute-image-import/gce_ovf_import:release",
          "env":[
            "BUILD_ID=$BUsILD_ID"
          ]
        }
      ],
      "tags":"gce-ovf-machine-image-import"
    }
    

Replace `PROJECT_ID` with your project ID.

## Import a machine image within a network that does not allow external IP

To import a machine image using a network that does not allow external IP addresses, complete the following steps:

  1. Add the virtual appliance to [Cloud Storage](https://docs.cloud.google.com/storage/docs/uploading-objects).

  2. The import process requires package managers to be installed on the operating system for the machine image. These package managers might need to make requests to package repositories that are outside Google Cloud. To allow access for these updates, you need to configure Cloud NAT. For more information, see [Create a NAT configuration using Cloud Router](https://docs.cloud.google.com/nat/docs/gce-example#create-nat).

  3. Configure [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access). For more information, see [Configuring Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

  4. Import the machine image using either the Google Cloud CLI or the Cloud Build API.

When you import a machine image from a virtual appliance, temporary VMs are created in your project. To ensure that these temporary VMs are not assigned external IP addresses, you must specify an additional flag or argument.

For more information about the required flag or argument, click the following tabs:




###  gcloud 

Use the [`gcloud compute machine-images import` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/machine-images/import) with the `--no-address` flag .
    
    
    gcloud compute machine-images import MACHINE_IMAGE_NAME \
        --source-uri=SOURCE_URI \
        --os=OS \
        --zone=ZONE \
        --no-address
    

Replace the following:

  * `MACHINE_IMAGE_NAME`: name of the machine image that you want to import.
  * `SOURCE_URI`: URI for your OVA or OVF file on Cloud Storage. For example, `gs://my-bucket/Ubuntu.ova`.
  * `OS`: operating system of the OVA file. This flag is optional by default, but it might be required in some cases. We recommend that you provide this flag. For a list of supported values, see [`--os` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--os) options for the `gcloud compute machine-images import` command.
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#locations) in which to import the machine image. If left blank, the default zone for the project is used.



###  REST 

Send a `POST` request to the [`projects.builds.create` method](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds/create) using the [Cloud Build API](https://docs.cloud.google.com/build/docs/api/reference/rest). Specify the `-no-external-ip` argument.

**Note:** Two `timeout` values are required. Default values for these are provided in the following sample requests. These default values work in most scenarios. However, if you need to adjust these values, ensure that the Cloud Build timeout is at least 3% greater than the timeout specified for the arguments (`args`) section.
    
    
     POST https://cloudbuild.googleapis.com/v1/projects/PROJECT_ID/builds
     {
      "timeout":"7200s",
      "steps":[
        {
          "args":[
            "-machine-image-name=MACHINE_IMAGE_NAME",
            "-ovf-gcs-path=SOURCE_URI",
            "-os=OS",
            "-zone=ZONE",
            "-no-external-ip",
            "-client-id=api",
            "-timeout=7000s"
          ],
          "name":"gcr.io/compute-image-import/gce_ovf_import:release",
          "env":[
            "BUILD_ID=$BUILD_ID"
          ]
        }
      ],
      "tags":"gce-ovf-machine-image-import"
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID for the project that you want to import the machine image into.
  * `MACHINE_IMAGE_NAME`: the name for the machine image to import. For example, `my-machine-image`.
  * `SOURCE_URI`: the URI for the OVA file that is stored in Cloud Storage. For example, `gs://my-bucket/my-machine.ova`.
  * `OS`: the operating system of the OVA file. For example, `ubuntu-1604`. This flag is optional by default, but it might be required in some cases. We recommend that you provide this flag. For a list of supported values, see [`--os` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/import#--os) options for the `gcloud compute instances import` command.
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#locations) in which to import the machine image.



## Import a machine image using custom service accounts

During a machine image import, temporary virtual machine (VM) instances are created in your project. The import tool on these temporary VMs must be authenticated.

A [service account](https://docs.cloud.google.com/compute/docs/access/service-accounts) is an identity that is attached to a VM. Service account access tokens can be accessed through the [VM metadata server](https://docs.cloud.google.com/compute/docs/metadata/overview) and used to authenticate the import tool on the VM.

By default, the import process uses the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#compute_engine_service_account). However, if the default Compute Engine service account is disabled in your project or if you want to use a custom Compute Engine service account, then you need to create a service account and specify it for the import process.

###  gcloud 

  1. Add the virtual appliance to [Cloud Storage](https://docs.cloud.google.com/storage/docs/uploading-objects).

  2. Create a service account and assign the minimum roles. For more information about creating service accounts, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).

At minimum, the specified Compute Engine service account needs to have the following roles assigned:

     * `roles/compute.storageAdmin`
     * `roles/storage.objectViewer`

These minimum roles are needed for the service account specified for the `--compute-service-account` flag. For more information, see [Grant required roles to the Compute Engine service account](https://docs.cloud.google.com/compute/docs/import/requirements-export-import-images#required-roles-compute-sa).

  3. Use the [`gcloud compute machine-images import` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/machine-images/import) to import a machine image from virtual appliances.
         
         gcloud compute machine-images import MACHINE_IMAGE_NAME \
             --source-uri=gs:SOURCE_URI \
             --os=OS \
             --compute-service-account=TEMP_SERVICE_ACCOUNT_EMAIL \
             --service-account=SERVICE_ACCOUNT_EMAIL \
             --scopes=SCOPES
         

Replace the following:

     * `MACHINE_IMAGE_NAME`: name of the machine image that you want to import.
     * `SOURCE_URI`: path to your OVA or OVF file on Cloud Storage.
     * `OS`: operating system of the OVA file. This flag is optional by default, but it might be required in some cases. We recommend that you provide this flag.
     * `TEMP_SERVICE_ACCOUNT_EMAIL`: the email address associated with the custom service account created in the previous step. This service account is used by the temporary VMs. If unspecified, the VM uses the default Compute Engine service account.
     * `SERVICE_ACCOUNT_EMAIL`: the email address associated with the custom service account that is to be attached to any VM created from this machine image. There are no permission restrictions for this service account, you can customize this service account as needed. If unspecified, the default Compute Engine service account is attached to the VM.
     * `SCOPES`: specify the level of access for the `--service-account` option. If unspecified, the default scopes are used. For more information, review the [`--scopes` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/import#--scopes).



###  REST 

  1. Add the virtual appliance to [Cloud Storage](https://docs.cloud.google.com/storage/docs/uploading-objects).

  2. Create a service account and assign the minimum roles. For more information about creating service accounts, see [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create).

At minimum, the specified Compute Engine service account needs to have the following roles assigned:

     * `roles/compute.storageAdmin`
     * `roles/storage.objectViewer`

These minimum roles are needed for the service account specified for the `-compute-service-account` argument. For more information, see [Grant required roles to the Compute Engine service account](https://docs.cloud.google.com/compute/docs/import/requirements-export-import-images#required-roles-compute-sa).

  3. Send a `POST` request to the [`projects.builds.create` method](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds/create) using the Cloud Build API.

**Note:** Two `timeout` values are required. Default values for these are provided in the following sample requests. These default values work in most scenarios. However, if you need to adjust these values, ensure that the Cloud Build timeout is at least 3% greater than the timeout specified for the arguments (`args`) section.
         
         POST https://cloudbuild.googleapis.com/v1/projects/PROJECT_ID/builds
         {
         "timeout":"7200s",
         "steps":[
           {
             "args":[
               "-machine-image-name=MACHINE_IMAGE_NAME",
               "-ovf-gcs-path=SOURCE_URI",
               "-os=OS",
               "-zone=ZONE",
               "-compute-service-account=TEMP_SERVICE_ACCOUNT_EMAIL",
               "-service-account=SERVICE_ACCOUNT_EMAIL",
               "-client-id=api",
               "-timeout=7000s"
             ],
             "name":"gcr.io/compute-image-import/gce_ovf_import:release",
             "env":[
               "BUILD_ID=$BUILD_ID"
             ]
           }
         ],
         "tags":"gce-ovf-machine-image-import"
         }
         

Replace the following:

     * `PROJECT_ID`: the project ID for the project that you want to import the machine image into.
     * `MACHINE_IMAGE_NAME`: the name for the machine image to import. For example, `my-machine-image`.
     * `SOURCE_URI`: the URI for the OVA file that is stored in Cloud Storage. For example, `gs://my-bucket/my-machine.ova`.
     * `OS`: the operating system of the OVA file. For example, `ubuntu-1604`. This flag is optional by default, but it might be required in some cases. We recommend that you provide this flag. For a list of supported values, see [`--os` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/import#--os) options for the `gcloud compute instances import` command.
     * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#locations) in which to import the machine image.
     * `TEMP_SERVICE_ACCOUNT_EMAIL`: the email address associated with the custom service account created in the previous step. This service account is used by the temporary VMs. If unspecified, the VM uses the default Compute Engine service account.
     * `SERVICE_ACCOUNT_EMAIL`: the email address associated with the custom service account that is to be attached to any VM created from this machine image. There are no permission restrictions for this service account, you can customize this service account as needed. If unspecified, the default Compute Engine service account is attached to the VM.
     * `SCOPES`: specify the level of access for the `--service-account` option. If unspecified, the default scopes are used. For more information, review the [`--scopes` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/import#--scopes).



## What's next?

  * Learn more about [machine images](https://docs.cloud.google.com/compute/docs/machine-images)
  * [Create VM instances from machine images](https://docs.cloud.google.com/compute/docs/machine-images/create-instance-from-machine-image)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
