---
url: https://docs.cloud.google.com/compute/docs/machine-images/create-instance-from-machine-image/
title: Create an instance or a disk from a machine image \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:44.403627+00:00
---

# Create an instance or a disk from a machine image  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/machine-images/create-instance-from-machine-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create an instance or a disk from a machine image Stay organized with collections  Save and categorize content based on your preferences. 

After you create a machine image, you can use it to make copies of the source compute instance. For more information about the uses of machine images, see [when to use a machine image](https://docs.cloud.google.com/compute/docs/machine-images#when-to-use).

A machine image contains most of the information and data needed for cloning an instance.

A machine image is unchangeable. However, you can override almost all the properties of the machine image when creating an instance from the machine image.

You can also create copies of individual disks that are within the machine image without creating a new instance.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

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




### Required roles

To get the permissions that you need to create Compute Engine instances from machine images, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the compute instance or project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Required permissions

The following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions) are required to create an instance from a machine image:

  * `compute.instances.create` on the project
  * `compute.machineImages.useReadOnly` on the machine image
  * Any additional permissions needed to set attributes on the instance, for example, the `setTags` permission.



## Restrictions

The following restrictions apply when you create instances from machine images:

  * You can create at most 6 instances from a source machine image in 60 minutes. If you exceed this limit, the instance create operation fails and returns an error similar to the following:
        
        Operation rate exceeded for resource 'projects/test/global/machineImages/machine-image-1'.
        Too frequent operations from the source resource.
        

To create more instances than the defined limit (6 instances in 60 minutes), create additional machine images from the source instance, or create short-lived machine images from the new instances. You can then create the required number of instances from the new machine images.

  * If you use the gcloud CLI or REST to create an instance from a machine image with CMEK-encrypted disks, the disks on the new instance are encrypted using default encryption unless you specify the CMEK keys. If you use the Google Cloud console, CMEK encryption is inherited automatically.

  * You cannot create instances from machine images with attached regional disks using the Google Cloud console. Use the Google Cloud CLI or REST and specify the `replicaZones` and `deviceName` parameters for each attached regional disk. For more information, see Create an instance from a machine image with property overrides.

  * If you choose to create a disk from a machine image (Preview), the following restrictions apply:

    * Both the `source_machine_image` and `source_machine_image_disk_device_name` must be specified.

    * The source machine image must be in a _READY_ state.

    * You cannot specify multiple data sources.




## Create an instance from a machine image (no override)

You can create instances from machine images using either the [Google Cloud console](https://console.cloud.google.com/), the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or [REST](https://docs.cloud.google.com/compute/docs/reference/rest/v1).

If you want to create an instance that is fully based on the machine image with no changes to the properties, use this method.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the auto_awesome **Create VM from ...** menu, select **Machine images**.

  3. In the **Create VM from machine image** window that appears, do the following:

     1. Select a machine image.

     2. To create and start the instance, click **Create**.




###  gcloud 

Use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) to create an instance from a machine image.
    
    
    gcloud compute instances create INSTANCE_NAME \
        --zone=ZONE \
        --source-machine-image=SOURCE_MACHINE_IMAGE_NAME
    

Replace the following:

  * `INSTANCE_NAME`: the name for the instance
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) for the instance
  * `SOURCE_MACHINE_IMAGE_NAME`: the machine image to create the instance from



**Example**

For example, you can use the following `gcloud` command to create an instance named `my-instance` in the `us-east1-b` zone, from a machine image called `my-machine-image`.
    
    
    gcloud compute instances create my-instance \
        --zone=us-east1-b \
        --source-machine-image=my-machine-image
    

After the instance is created, the output resembles the following:
    
    
    Created [https://www.googleapis.com/compute/v1/projects/project-12345/zones/us-east1-b/instances/my-instance].
    NAME               ZONE        MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP   STATUS
    my-instance        us-east1-b  e2-standard-2               192.0.2.1   203.224.0.113  RUNNING
    

**Note on CMEK Encryption** : When creating a VM from a machine image encrypted with a Customer-Managed Encryption Key (CMEK), the gcloud CLI defaults to using Google-managed encryption for the new VM's disks. This differs from the Google Cloud console, which automatically inherits the CMEK from the source machine image.

To ensure the new VM's disks inherit the CMEK from the source machine image (replicating the Google Cloud console's behavior), you must explicitly provide the disk configuration using the `--create-disk` flag for each disk that you want to preserve CMEK encryption on. The `device-name` specified in the flag must exactly match the device name of the disk within the source machine image.

Use the following command structure to preserve CMEK encryption. The following example shows how to preserve CMEK encryption for a boot disk (`boot=yes`) and a non-boot disk (`boot=no`).
    
    
    gcloud compute instances create INSTANCE_NAME \
        --zone=ZONE \
        --source-machine-image=SOURCE_MACHINE_IMAGE \
        --create-disk=auto-delete=yes,boot=yes,device-name=DEVICE_NAME_IN_IMAGE,kms-key=KMS_KEY,kms-project=KMS_PROJECT,kms-location=KMS_LOCATION,kms-keyring=KMS_KEYRING \
        --create-disk=auto-delete=yes,boot=no,device-name=DEVICE_NAME_IN_IMAGE,kms-key=KMS_KEY,kms-project=KMS_PROJECT,kms-location=KMS_LOCATION,kms-keyring=KMS_KEYRING
    

Replace the following:

  * `INSTANCE_NAME`: The name for your new VM instance.
  * `ZONE`: The zone for the new VM instance.
  * `SOURCE_MACHINE_IMAGE`: The name of the source machine image.
  * `DEVICE_NAME_IN_IMAGE`: The device name of the disk (boot or non-boot) as defined in the source machine image.
  * `KMS_KEY`: The name of your CMEK key.
  * `KMS_PROJECT`: The project where your key is located.
  * `KMS_LOCATION`: The location of the key.
  * `KMS_KEYRING`: The key ring for the key.



###  REST 

In the API, construct a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). In the request body, include the following parameters:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "name": "INSTANCE_NAME",
      "sourceMachineImage": "SOURCE_MACHINE_IMAGE_URL"
    }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) for the instance.
  * `INSTANCE_NAME`: a name for the instance.
  * `SOURCE_MACHINE_IMAGE_URL`: the full or partial URL of the machine image that you want to use to create the instance. For example, if you have a machine image called `my-machine-image` in a project called `myProject`. The following URLs are valid:

    * `https://www.googleapis.com/compute/v1/projects/myProject/global/machineImages/my-machine-image`
    * `projects/myProject/global/machineImages/my-machine-image`
    * `global/machineImages/my-machine-image`



**Note on CMEK Encryption** :

When creating a VM from a machine image encrypted with a Customer-Managed Encryption Key (CMEK), a default `instances.insert` request will result in the new VM's disks being encrypted with Google-managed encryption.

To ensure the new VM and its disks are created with the same CMEK as the source machine image (replicating the behavior of the Google Cloud console), you must override the `disks` property to specify the `diskEncryptionKey` for each disk (boot or non-boot) that you want to preserve CMEK encryption on.

The following example shows a request body that preserves the CMEK encryption from the source machine image. Note that because `disks` is a repeated field, you must specify the configuration for all disks being created from the image.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "name": "INSTANCE_NAME",
      "sourceMachineImage": "SOURCE_MACHINE_IMAGE_URL",
      "disks": [
        {
          "boot": true,
          "autoDelete": true,
          "deviceName": "DEVICE_NAME_IN_IMAGE",
          "diskEncryptionKey": {
            "kmsKeyName": "projects/KMS_PROJECT/locations/KMS_LOCATION/keyRings/KMS_KEYRING/cryptoKeys/KMS_KEY"
          }
        },
        {
          "boot": false,
          "autoDelete": true,
          "deviceName": "DEVICE_NAME_IN_IMAGE",
          "diskEncryptionKey": {
            "kmsKeyName": "projects/KMS_PROJECT/locations/KMS_LOCATION/keyRings/KMS_KEYRING/cryptoKeys/KMS_KEY"
          }
        }
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) for the instance.
  * `INSTANCE_NAME`: The name for your new VM instance.
  * `SOURCE_MACHINE_IMAGE_URL`: the full or partial URL of the machine image that you want to use to create the instance. For example, if you have a machine image called `my-machine-image` in a project called `myProject`. The following URLs are valid:

    * `https://www.googleapis.com/compute/v1/projects/myProject/global/machineImages/my-machine-image`
    * `projects/myProject/global/machineImages/my-machine-image`
    * `global/machineImages/my-machine-image`
  * `DEVICE_NAME_IN_IMAGE`: The device name of the disk (boot or non-boot) as defined in the source machine image.

  * `KMS_PROJECT`: The project where your key is located.

  * `KMS_LOCATION`: The location of the key.

  * `KMS_KEYRING`: The key ring for the key.

  * `KMS_KEY`: The name of your CMEK key.




## Create an instance from a machine image with property overrides

If you want to create an instance primarily based on the machine image but with a few changes, you can use the override behavior. To use the override behavior, you pass in attributes to override existing machine image properties when creating the instance.

When you use the override feature, take the following notes into consideration:

  * You can't override any properties of the attached disk other than the name of the disk while creating an instance from the machine image.
  * You must specify the `replicaZones` parameter for each attached regional disk along with the regional disk's `deviceName` from the machine image.

  * If the source instance (used to generate the machine image) and the new instance belong to the same project and the same region, the following applies:

    * Most of the properties of source instance and the new instance are the same. Properties that differ are those such as the ephemeral IP addresses that are auto assigned.
    * If the source instance still exists when you create a new instance, then the new instance cannot use the same name and the same zone as the source instance.
  * If the source instance used to generate the machine image and the new instance belong to the same project but different regions, the following applies:

    * You must override all zonal and regional resources for the new instance. For example, if you create an instance from a machine image whose source instance belonged to a different region, you need to override regional resources such as the subnetwork and regional firewall rules. However, global resources such as load balancers and service accounts don't need an override, unless you want to modify these.



###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the auto_awesome **Create VM from ...** menu, select **Machine images**.

  3. In the **Create VM from machine image** window that appears, select a template, and then click edit **Customize**.

  4. Optional: Specify other configuration options. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

  5. To create and start the instance, click **Create**.




###  gcloud 

Use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) to create an instance from a machine image and add the properties you want to override.

For example, you can use the following `gcloud` command to create a VM called `my-instance` in the `us-east1-b` zone, from a machine image called `my-machine-image`. In this example overrides are applied to change the machine type, stop the host maintenance policy, and configure a regional persistent disk with the name `regional-disk-0`.
    
    
    gcloud compute instances create my-instance \
        --zone=us-east1-b \
        --source-machine-image=my-machine-image \
        --machine-type=e2-standard-2 \
        --maintenance-policy=TERMINATE \
        --create-disk=device-name=boot-device-0,boot=true,auto-delete=true \
        --create-disk=device-name=regional-disk-0,\
          replica-zones=^:^us-east1-b:us-east1-c,boot=false
    

###  REST 

To override machine image properties during instance creation, construct a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). In the request body, include the `sourceMachineImage` parameter and any overrides that you need. You can add any property that you would normally set during [instance creation](https://docs.cloud.google.com/compute/docs/instances/create-start-instance). For example, to override the machine type, your API call would include the `machineType` parameter.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "name": "INSTANCE_NAME",
      "machineType": "zones/ZONE/machineTypes/NEW_MACHINE_TYPE",
      "sourceMachineImage": "SOURCE_MACHINE_IMAGE_URL"
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) for the instance.
  * `INSTANCE_NAME`: a name for the instance.
  * `NEW_MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) that you want to use for the instance.
  * `SOURCE_MACHINE_IMAGE_URL`: the full or partial URL of the machine image that you want to use to create the instance. For example, if you have a machine image called `my-machine-image` in a project called `myProject`. The following URLs are valid:

    * `https://www.googleapis.com/compute/v1/projects/myProject/global/machineImages/my-machine-image`
    * `projects/myProject/global/machineImages/my-machine-image`
    * `global/machineImages/my-machine-image`



### Override behavior

The override behavior in the Compute Engine API follows the JSON merge patch rules, described by [RFC 7396](https://datatracker.ietf.org/doc/html/rfc7396). In summary, the following rules apply:

  * If you override a basic field, the corresponding basic field in the machine image is replaced with the basic field value in the request. Basic fields include parameters such as `machineType` and `name`.
  * If you override a repeated field, all repeated values for that property are replaced with the corresponding values provided in the request. Repeated fields are generally properties of type `list`. For example, `disks` and `networkInterfaces` are repeated fields.
  * If you override a `nested object`, the object in the machine image is merged with the corresponding object specification in the request. Note that if a nested object is within a repeated field, the field is treated according to rules for repeated fields. Labels are an exception to this rule, and are treated as a repeated field even though labels are of type `object`.



For example, if you want to create a VM from a machine image, and create regional disks with the VM, use an override for the disks so you can specify the `replicaZones` option. Because the `disks` field is a repeated field, you must specify the disk configuration for all attached disks and the boot disk, not just the regional disks.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/my-proj/zones/us-west1-a/instances
    {
      "name": "vm-from-image",
      "sourceMachineImage": "global/machineImages/my-machine-image",
      "disks": [
        {
          "kind": "compute#attachedDisks",
          "boot": true,
          "autoDelete": true,
          "deviceName": "boot-device",
          "initializeParams": {
            "sourceImage": "projects/my-proj/global/images/my-image",
            "diskType": "projects/my-proj/zones/us-west1-a/diskTypes/pd-standard",
          }
        },
        {
          "kind": "compute#attachedDisk",
          "boot": false,
          "autoDelete": true,
          "deviceName": "regional-device-0",
          "initializeParams": {
             "diskType": "projects/my-proj/zones/us-west1-a/diskTypes/pd-standard",
             "replicaZones": [
                "projects/my-proj/zones/us-west1-a",
                "projects/my-proj/zones/us-west1-c"
             ]
          }
        }
      ]
    }
    

## Create an instance using a machine image from a different project

When you create an instance by using a machine image from a different project, you might not have access to the service account attached to that source project. If you want to create an instance from a machine image that is located in a different project, you need to ensure that you have access to the machine image and override the service account property on the new instance.

If you share a machine image across projects that use a Shared VPC network, you must explicitly specify the Shared VPC details when you create an instance from the machine image. For example, when you create an instance in a non-host project, provide the Shared VPC details of the host project using the `--network`, `--subnet`, or `--network-interface` flags.

The following sections outlines how to create an instance from a machine image located in a different project by using the Google Cloud CLI.

  1. [Grant access](https://docs.cloud.google.com/deployment-manager/docs/configuration/using-images-from-other-projects-for-vm-instances#granting_access_to_images) to the machine image that is stored in a different project.

Permissions can be granted on either the source project or the machine image. Use the [`gcloud compute machine-images add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/machine-images/add-iam-policy-binding) to grant the permissions on the machine image.
         
         gcloud compute machine-images add-iam-policy-binding MACHINE_IMAGE_NAME \
             --project=MACHINE_IMAGE_PROJECT \
             --member='ACCOUNT_EMAIL' \
             --role='roles/compute.admin'
         

Replace the following:

     * `MACHINE_IMAGE_PROJECT`: the project ID for the project that contains the source machine image.
     * `MACHINE_IMAGE_NAME`: the name of the machine image that you want to add the permission binding to.
     * `ACCOUNT_EMAIL`: the email address of the `serviceAccount` or `user` that is creating the instance. Ensure that the email is formatted to include the required prefix. The prefix must be one of the following:

       * `user:` specify this if the email address is associated with a user account. For example, `user:user@example.com`.
       * `serviceAccount:` specify this if the email address is associated with a service account. For example, `serviceAccount:123456789000-compute@developer.gserviceaccount.com`.

**Example**

For example, to add a `compute.admin` binding to the machine image called `my-machine-image` to the service account email `123456789000-compute@developer.gserviceaccount.com`, use the following `gcloud CLI` command:
    
    gcloud compute machine-images add-iam-policy-binding my-machine-image \
        --project=machine-image-project \
        --member='serviceAccount:123456789000-compute@developer.gserviceaccount.com' \
        --role='roles/compute.admin'
    

  2. Grant the user who runs the `gcloud compute instances create` command the [Service Account User role](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) (`roles/iam.serviceAccountUser`) on the service account associated with the machine image.

  3. Use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) to create an instance from a machine image.
         
         gcloud compute instances create INSTANCE_NAME \
             --project=INSTANCE_PROJECT_ID \
             --zone=ZONE \
             --source-machine-image=projects/MACHINE_IMAGE_PROJECT/global/machineImages/MACHINE_IMAGE_NAME \
             --service-account=SERVICE_ACCOUNT_EMAIL \
             --subnet=SUBNET
         

Replace the following:

     * `INSTANCE_PROJECT_ID`: the project ID for the project that you want to create the instance in
     * `INSTANCE_NAME`: a name for the instance
     * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) for the instance
     * `MACHINE_IMAGE_PROJECT`: the project ID of the project where the machine image is located
     * `MACHINE_IMAGE_NAME`: the machine image to create the instance from
     * `SERVICE_ACCOUNT_EMAIL`: the email address of the service account that you want to attach to your instance
     * `SUBNET`: if the subnet and instance are in the same project, replace SUBNET with the name of a subnet that is in the same region as the instance

To specify a subnet in a Shared VPC network, replace `SUBNET` with a string in the following format:
           
           projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME
           

Replace the following: 

       * `HOST_PROJECT_ID`: the project ID of the Shared VPC host project
       * `REGION`: the region of the subnet
       * `SUBNET_NAME`: the name of the subnet

**Example**

For example, the following command creates a VM called `my-instance` in `vm-project`, in the `us-east1-b` zone, from a machine image called `my-machine-image`.

The `--service-account` flag specifies the service account that you want to attach to the newly created VM. If you don't provide this flag, the source service account cannot be shared across both projects and the operation fails.
    
    gcloud compute instances create my-instance \
     --project=vm-project \
     --zone=us-east1-b \
     --source-machine-image=projects/machine-image-project/global/machineImages/my-machine-image \
     --service-account=000123456789-compute@developer.gserviceaccount.com
    

After the VM is created, the output resembles the following:
    
    Created [https://www.googleapis.com/compute/v1/projects/project-12345/zones/us-east1-b/instances/my-instance].
    NAME               ZONE        MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP   STATUS
    my-instance        us-east1-b  e2-standard-2               192.0.2.1   203.224.0.113  RUNNING
    




## Create a disk from a machine image (Preview)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you backed up a Compute Engine instance by using a machine image, you can create a new disk by restoring a specific disk from that machine image.

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Create a disk** page.

[Go to the Create a disk page](https://console.cloud.google.com/compute/disksAdd)

  2. Click **Create disk**.

  3. Under **Disk source type** , select **Machine image**.

  4. Select the source machine image you want.

  5. From the drop-down list of disks within the machine image, choose the specific source disk.

  6. If the machine image is CSEK-encrypted, an input field appears to enter the key.

  7. Configure other disk properties such as name, zone, type, size.




###  Google Cloud CLI 

To create a disk from a specific disk in a machine image, run the following command:
    
    
    gcloud beta compute disks create DISK_NAME \
    --zone=ZONE \
    --source-machine-image=SOURCE_MACHINE_IMAGE_NAME \
    --source-machine-image-disk-device-name=SOURCE_DISK_DEVICE_NAME \
    --type=pd-balanced
    

To create a disk from a CSEK-encrypted machine image, run the following command:
    
    
    gcloud beta compute disks create CSEK_DISK_NAME \
    --zone=ZONE \
    --source-machine-image=CSEK_MACHINE_IMAGE_NAME \
    --source-machine-image-disk-device-name=SOURCE_DISK_DEVICE_NAME \
    --source-machine-image-encryption-key-file=/PATH/TO/KEY.json
    

Replace the following:

  * `DISK_NAME`: the name of the new disk.

  * `ZONE`: the zone where you want to create the disk.

  * `SOURCE_MACHINE_IMAGE_NAME`: the name of the source machine image.

  * `SOURCE_DISK_DEVICE_NAME`: the device name of the specific disk within the source machine image that you want to use as the source for the new disk.

  * `CSEK_DISK_NAME`: the name of the new disk created from a CSEK-encrypted machine image.

  * `CSEK_MACHINE_IMAGE_NAME`: the name of the CSEK-encrypted source machine image.

  * `/PATH/TO/KEY.json`: the path to the JSON file containing the customer-supplied encryption key (CSEK) used to decrypt the machine image. For information about the key file format, see [Key file format](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#key_file_format).




###  REST 

To create a disk from a machine image, make a `POST` request to the [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/disks/insert):
    
    
    POST https://compute.googleapis.com/compute/beta/projects/PROJECT_NAME/zones/ZONE/disks
    

In the request body, specify the disk configuration and the URL for the source machine image:
    
    
    {
      "name": "DISK_NAME",
      "sourceMachineImage": "projects/PROJECT_NAME/global/machineImages/SOURCE_MACHINE_IMAGE_NAME",
      "sourceMachineImageDiskDeviceName": "SOURCE_DISK_DEVICE_NAME",
      "type": "projects/PROJECT_NAME/zones/ZONE/diskTypes/pd-balanced"
    }
    

To create a disk from a CSEK-encrypted machine image, include the encryption key in the request body:
    
    
    {
      "name": "CSEK_DISK_NAME",
      "sourceMachineImage": "projects/PROJECT_NAME/global/machineImages/CSEK_MACHINE_IMAGE_NAME",
      "sourceMachineImageDiskDeviceName": "SOURCE_DISK_DEVICE_NAME",
      "sourceMachineImageEncryptionKey": {
        "rawKey": "BASE64_ENCODED_KEY"
      }
    }
    

Replace the following:

  * `PROJECT_NAME`: the name of your project.

  * `ZONE`: the zone where you want to create the disk.

  * `DISK_NAME`: the name of the new disk.

  * `SOURCE_MACHINE_IMAGE_NAME`: the name of the source machine image.

  * `SOURCE_DISK_DEVICE_NAME`: the device name of the specific disk within the source machine image that you want to use as the source for the new disk.

  * `CSEK_DISK_NAME`: the name of the new disk created from a CSEK-encrypted machine image.

  * `CSEK_MACHINE_IMAGE_NAME`: the name of the CSEK-encrypted source machine image.

  * `BASE64_ENCODED_KEY`: the `base64`-encoded customer-supplied encryption key (CSEK) used to decrypt the machine image.




### Inherited properties

The following properties are inherited from the source machine image:

  * Size

  * Licenses

  * Guest operating system features

  * CPU architecture

  * Type




## What's next?

  * Learn more about [machine images](https://docs.cloud.google.com/compute/docs/machine-images)
  * Learn more about [creating Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances/create-start-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
