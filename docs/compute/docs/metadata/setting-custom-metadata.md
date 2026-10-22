---
url: https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata/
title: Set and remove custom metadata \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:15.097344+00:00
---

# Set and remove custom metadata  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Set and remove custom metadata Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Each metadata entry is stored on the metadata server as key-value pairs. Metadata keys are case sensitive. Your keys can be either predefined or custom metadata keys. 

Custom metadata enables you to create and use your own metadata key-value pairs on an individual VM or a project. You can add new custom metadata keys, update the values of your existing keys, and remove any custom metadata entries when you don't need them. Setting custom metadata is useful for passing in arbitrary values to VMs in a project. It is also useful for creating [startup](https://docs.cloud.google.com/compute/docs/startupscript) and [shutdown](https://docs.cloud.google.com/compute/docs/shutdownscript) scripts. 

This document provides information about how to do the following:

  * Add or update custom metadata on VMs
  * Remove custom metadata from VMs



## Before you begin

  * Review the basics of how VM metadata for Compute Engine is defined, categorized, and arranged. For more information, see [About VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview).
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

To get the permissions that you need to set or remove custom metadata on VMs, ask your administrator to grant you the following IAM roles: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on the VM or project
  * If your VMs use service accounts: [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service account or project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to set or remove custom metadata on VMs. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to set or remove custom metadata on VMs:

  * If your VMs use service accounts: `iam.serviceAccounts.actAs` on the service accounts or project 
  * To add, update, or remove custom project metadata: 
    * `compute.projects.get` on the project
    * `compute.projects.setCommonInstanceMetadata` on the project
  * To add, update, or remove custom zonal metadata: 
    * `compute.instanceSettings.get` on the instance settings in the required zone in the project
    * `compute.instanceSettings.update` on the instance settings in the required zone in the project
  * To add, update, or remove custom instance metadata: 
    * `compute.instances.get` on the VM
    * `compute.instances.setMetadata` on the VM



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

VM metadata entries have the following limitations.

### Size limitations

Compute Engine enforces a combined total limit of 512 KB for all metadata entries. Maximum size limits are also applied to each `key` and `value` in the following way:

  * Each metadata `key` has a maximum limit of 128 bytes.
  * Each metadata `value` has a maximum limit of 256 KB.



For example, SSH keys are stored as custom metadata under the `ssh-keys` key. If your metadata content or `value` for this key exceeds the 256 KB limit, you won't be able to add more SSH keys. If you run into this limit, consider [removing unused keys](https://docs.cloud.google.com/compute/docs/connect/restrict-ssh-keys#remove-metadata-key) to free up metadata space for new keys.

Also, if you provide the startup or shutdown script contents directly, then the contents of these startup and shutdown script contents might also be stored as custom metadata and count toward these size limitations. To avoid this, store your startup or shutdown script as a file hosted at an external location, such as Cloud Storage, and provide the startup script URL when creating a VM. This way, these files are downloaded onto the VM, rather than stored in the metadata server.

### String case limitations

  * Each metadata `key` is case sensitive.

  * Each metadata `value` is case sensitive except for boolean values.




### Zonal metadata limitations

  * You can set and remove zonal metadata only by using the gcloud CLI or REST.

  * You can't create two separate metadata keys with the same string, even if the keys are written in different cases. For example, if a custom metadata key named `zonal-metadata-key` already exists for zonal metadata within a specific zone, then you can't create new zonal metadata keys that are variations of the same string, such as `Zonal-Metadata-Key` or `ZONAL-METADATA-KEY`.

  * You can't set zonal metadata values for SSH keys, which are stored as custom metadata under the `ssh-keys` key.




## Boolean values

For fields that accept boolean values, `TRUE` or `FALSE`, the following values can also be used:

Status | Alternative values  
---|---  
`TRUE` | `Y`, `Yes`, `1`  
`FALSE` | `N`, `No`, `0`  
  
Boolean values are not case-sensitive. For example, you can use `False`, `false`, or `FALSE` to disable a feature.

## Set custom metadata on VMs

This section explains how to add new custom metadata, or update existing custom metadata values, for your Compute Engine VMs in one of the following ways:

  * Set custom project metadata to add or update custom project metadata for all VMs in your project.
  * Set custom zonal metadata to add or update custom metadata with a zonal scope for VMs within the project.
  * Set custom instance metadata to add or update custom instance metadata for a specific VM.



### Set custom project metadata

You can add or update the custom metadata for all instances in a project by using the Google Cloud console, the Google Cloud CLI, or REST.

Use these instructions to apply metadata settings to all VMs in the project. For example, if you define a project metadata pair of `baz=bat`, that metadata pair is automatically applied to all VMs in the project.

###  Console 

  1. In the Google Cloud console, go to the **Metadata** page. 

[Go to the Custom metadata page](https://console.cloud.google.com/compute/metadata)

  2. Click edit **Edit** at the top of the page.

  3. To add new custom project metadata entries, do the following:

     1. Navigate to the bottom of the page and click add_box **Add item**.
     2. In the **Key** field, enter the name of your custom metadata key.
     3. In the **Value** field, enter the custom project metadata value.
     4. Optional. To add more custom project metadata entries, repeat the preceding steps for each metadata entry that you want to add.
     5. To finish adding your custom project metadata entries, click **Save**.
  4. To edit existing custom project metadata entries, do the following:

     1. Navigate to that metadata entry that you want to edit.
     2. To update the name of a specific custom metadata key, in the **Key** field for that entry, enter the new name.
     3. To update the value of a custom project metadata entry, in the **Value** field for that entry, enter the new value.
     4. Optional. To remove a specific custom project metadata entry, click the delete delete icon next to the metadata entry.
     5. To edit multiple custom project metadata entries, repeat the preceding steps for each metadata entry that you want to edit.
     6. To finish editing your custom project metadata entries, click **Save**.



###  gcloud 

Use the [`project-info add-metadata` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata).
    
    
    gcloud compute project-info add-metadata \
        --metadata=KEY=VALUE

Replace the following:

  * `KEY`: the name of your metadata key
  * `VALUE`: the value stored for this key



**Example**

For example to set two new entries `foo=bar` and `baz=bat` on a project, run the following command:
    
    
    gcloud compute project-info add-metadata \
        --metadata=foo=bar,baz=bat
    

You can optionally specify one or more files from which to read metadata by using the `--metadata-from-file` flag.

###  REST 

**Note:** If using `curl` or `Invoke-RestMethod` to set project metadata, then add the `Content-Type:application/json` header to the request.

  1. Optional. To perform optimistic locking, you can provide a fingerprint.

A fingerprint is a random string of characters generated by Compute Engine. The fingerprint changes after each request, and if you provide a mismatched fingerprint, your request is rejected.

If you don't provide a fingerprint, no check for consistency is performed, and the `projects().setCommonInstanceMetadata` request succeeds. This behaviour is different from `instances().setMetadata` and `instanceSettings().patch` methods, where a fingerprint is always required.

To get the current fingerprint of a project, call the [`project().get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/get).
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID
         

The output is similar to the following:
         
         {
           "name": "myproject",
           "commonInstanceMetadata": {
             "kind": "compute#metadata",
             "fingerprint": "FikclA7UBC0=",
             ...
           }
         }
         

  2. Make a request to the [`projects().setCommonInstanceMetadata` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/setCommonInstanceMetadata) and set your custom metadata key-value pairs:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/setCommonInstanceMetadata
         
         {
           "fingerprint": "FikclA7UBC0=",
           "items": [
             {
             "key": "foo",
             "value": "bar"
             }
           ]
         }
         




Replace `PROJECT_ID` with your project ID.

### Set custom zonal metadata

When you set custom zonal metadata, you add or update the zonal metadata entries for your VMs in a specific zone in a project. You can do the following by setting custom zonal metadata:

  * Create new custom metadata keys for a specific zone in a project and set metadata for all VMs in that zone in that project.
  * Update the values of existing custom zonal metadata entries for all VMs in a specific zone in a project.
  * For existing custom metadata keys that have project metadata values, override those project metadata values in specific zones and instead set zonal metadata. After you set zonal metadata for those keys in a specific zone, all VMs in that zone in that project use the zonal metadata values for those keys.



#### Things to note before you set custom zonal metadata

Project and zonal metadata entries are stored in the same `project/` directory. If you set different values for the same custom metadata keys for VMs on a project level and on a zonal level, then the zonal metadata values for those keys take precedence over the project metadata values in the respective zones. 

  * If you add a zonal metadata value for a metadata key that already has a project metadata value, then Compute Engine overrides the project metadata value for the VMs in this specified zone and updates the `/project` directory with the zonal value.
  * If you add a new project metadata value for a metadata key that already has a zonal metadata value, then nothing changes. Compute Engine retains the zonal metadata value in the `/project` directory in the specific zone.
  * If you don't specify a zonal metadata value for a custom metadata key in a specific zone, but the key has a project metadata value, then your VMs continue to have the project metadata values in those zones.



#### Procedure

You can add or update the custom zonal metadata in a specific zone in a project by using the Google Cloud CLI or REST.

###  gcloud 

  * To add or update custom zonal metadata, use the [`gcloud compute project-zonal-metadata add` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/add).
        
        gcloud compute project-zonal-metadata add \
          --zone=ZONE \
          --project=PROJECT_ID  \
          --metadata=KEY1=VALUE1,KEY2=VALUE2,...

Replace the following:

    * `PROJECT_ID`: your project ID
    * `ZONE`: the zone where you want to add or update zonal metadata.
    * `KEY1`, `KEY2`...: the custom metadata keys for which you want to add or update zonal metadata values.
    * `VALUE1`, `VALUE2`...: the zonal metadata values that you want to set for your existing and new custom metadata keys. Depending on your custom metadata key and value, one of the following happens:

    * If the corresponding custom metadata key is an existing key that has project metadata, then, in the specified zone, Compute Engine overrides the key's project metadata value with your specified zonal metadata value. All VMs in the specified zone in the project inherit this newly specified zonal metadata for that key and VMs in other zones continue to retain their prevailing project or zonal metadata values. If you make any future updates to the project metadata value for this key, then VMs in this zone in the project remain unaffected and continue to use the zonal metadata value for this key.

    * If the corresponding custom metadata key is a new metadata key that is not used for existing project or zonal metadata, then Compute Engine creates the custom metadata key and sets this value as the zonal metadata in the specified zone.

    * If the corresponding custom metadata key is an existing metadata key with a zonal metadata value in the specified zone:

      * If the specified metadata value is a different from the existing value, then Compute Engine updates the zonal metadata entry with the new value.
      * If the specified metadata value is same as the existing value, then the zonal metadata entry remains unchanged.



#### Example: Add a new custom zonal metadata entry

For example, consider a project called `my-project` with the following custom metadata:

  * Project metadata: `"key-1":"value-a"`, `"key-2":"value-b"`, and `"key-3":"value-c"`
  * Zonal metadata in `us-central1-a` zone: `"key-1":"value-1"` and `"key-2":"value-2"`



To add `"key-4":"value-4"` as a new custom zonal metadata pair in the `us-central1-a` zone, run the following command
    
    
    gcloud compute project-zonal-metadata add \
        --metadata=key-4=value-4 \
        --project=my-project \
        --zone=us-central1-a
    

#### Example: Update the values of an existing custom zonal metadata entry

Consider the same example project `my-project`, which now has the following custom metadata:

  * Project metadata: `"key-1":"value-a"`, `"key-2":"value-b"`, and `"key-3":"value-c"`
  * Zonal metadata in `us-central1-a` zone: `"key-1":"value-1"`, `"key-2":"value-2"`, and `"key-4":"value-4"`



To update the zonal metadata values of `key-1` and `key-4` in `us-central1-a` zone with new values, run the following command.
    
    
    gcloud compute project-zonal-metadata add \
        --metadata=key-1=new-value-1,key-4=new-value-4 \
        --project=my-project \
        --zone=us-central1-a
    

**Note:** For `key-1`, which has different values set at project and zonal levels, only the zonal metadata value gets updated after you run the command. The project metadata value for `key-1` remains unchanged. In the future, if you delete the zonal metadata entry for `key-1`, then the VMs in the zone inherit the project metadata value for this key.

#### Example: Override the project metadata value for a key and use a zonal metadata value

Consider the same example project `my-project`, which now has the following custom metadata:

  * Project metadata: `"key-1":"value-a"`, `"key-2":"value-b"`, and `"key-3":"value-c"`
  * Zonal metadata in `us-central1-a` zone: `"key-1":"new-value-1"`, `"key-2":"value-2"`, and `"key-4":"new-value-4"`



In this example project, consider `key-3`, which has a project metadata value of `value-c`. Suppose you want to set a zonal metadata value `value-3` for this key for all VMs in the `us-central1-a` zone. When you perform the operation, for all the VMs in the `us-central1-a` zone, Compute Engine overrides the project metadata values and uses the zonal metadata values. VMs in all other zones of the project retain their prevailing project or zonal metadata values for `key-3`.

To override the project metadata value for `key-3` and set a zonal metadata value, run the following command:
    
    
    gcloud compute project-zonal-metadata add \
        --metadata=key-3=value-3 \
        --project=my-project \
        --zone=us-central1-a
    

**Note:** If you subsequently update the value for `key-3` on a project level, then your update doesn't get added to the `/project/attributes` directory of the metadata server in the `us-central1-a` zone. If you want your future project metadata value update for `key-3` to get posted to the `/project/attributes` folder in the `us-central1-a` zone, then you must first remove the zonal metadata entry.

###  REST 

**Note:** If you're using `curl` or `Invoke-RestMethod` to set zonal metadata, then add the `Content-Type:application/json` header to the request.

  1. Get the current fingerprint and view any existing key-value pairs for the project in that zone.

To perform optimistic locking, you must provide a fingerprint. A fingerprint is a random string of characters generated by Compute Engine. The fingerprint changes every time you make a request to add, update, or remove zonal metadata, and if you provide a mismatched fingerprint, Compute Engine rejects your request.

If you don't provide a fingerprint, a check for consistency is performed and your update request doesn't succeed. This works so that only one request can be made at a time, preventing collisions. This behavior matches `instances().setMetadata`, where a fingerprint is always required.

To get the current fingerprint of the zonal metadata, make a `GET` request to the [`instanceSettings().get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceSettings/get).
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceSettings
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `ZONE`: the zone where you want to set the zonal metadata.

The following is an example output for this request:
    
    {
          "fingerprint": "VlRIl8dx9vk=",
          "metadata": {
            ...
          }
        }
    

  2. To add or update the zonal metadata, make a `PATCH` request to the [`instanceSettings().patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceSettings/patch). You must provide the following with your request:

     * An update mask. Use the `update_mask` query parameter. The update mask must contain the metadata keys for the following:

       * The new custom zonal metadata that you want to add
       * The existing custom zonal metadata for which you want to update values

You must add the string `metadata.items.` as a prefix for each key—for example, `metadata.items.key1,metadata.items.key3`.

**Important:** The update mask must be in lower case.
     * In the request body, provide the following:

       * The metadata keys and values for the new custom zonal metadata that you want to add
       * The metadata keys and values for the existing custom zonal metadata that you want to update
       * The current fingerprint value

**Caution:** If you specify any existing custom zonal metadata keys in the update mask but don't include them in the request body, then Compute Engine removes those zonal metadata entries. For more information, see Remove custom zonal metadata.
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceSettings?**update_mask** =PREFIXED_METADATA_KEYS
    {
      "fingerprint": "FINGER_PRINT",
      "metadata": {
        "items": {
          "KEY1": "VALUE1",
          "KEY2": "VALUE2",
          ...
        }
      }
    }
    

Replace the following:

     * `PROJECT_ID`: the ID of the project.
     * `ZONE`: the zone where you want to set the zonal metadata.
     * `PREFIXED_METADATA_KEYS`: the list of metadata keys for the following, where each key is prefixed with the string `metadata.items.` :

       * The new custom zonal metadata that you want to add
       * The existing custom zonal metadata for which you want to update values

For example, suppose your current zonal metadata keys in a specific zone are `key-1` and `key-2`. If you want to add a new key, `key-3`, for zonal metadata in that zone and also update the zonal metadata for one of the existing keys, `key-1`, then your update mask must have the following string:

`metadata.items.key1,metadata.items.key3`

     * `FINGER_PRINT`: the current fingerprint value.

     * `KEY1`, `KEY2`...: the custom zonal metadata keys for which you want to add or update values. Specify all the custom zonal metadata keys that you specified in the update mask.

**Caution:** If you specify any existing custom zonal metadata keys in the update mask but don't include them in the request body, then Compute Engine removes those zonal metadata entries. For more information, see Remove custom zonal metadata.

     * `VALUE1`, `VALUE2`...: the zonal metadata values that you want to set for your existing and new custom metadata keys. Depending on your custom metadata key and value, one of the following happens:

       * If the corresponding custom metadata key is an existing key that has project metadata, then, in the specified zone, Compute Engine overrides the key's project metadata value with your specified zonal metadata value. All VMs in the specified zone in the project inherit this newly specified zonal metadata for that key and VMs in other zones continue to retain their prevailing project or zonal metadata values. If you make any future updates to the project metadata value for this key, then VMs in this zone in the project remain unaffected and continue to use the zonal metadata value for this key.
       * If the corresponding custom metadata key is a new metadata key that is not used for existing project or zonal metadata, then Compute Engine creates the custom metadata key and sets this value as the zonal metadata in the specified zone.
       * If the corresponding custom metadata key is an existing metadata key with a zonal metadata value in the specified zone:

       * If the specified metadata value is a different from the existing value, then Compute Engine updates the zonal metadata entry with the new value.

       * If the specified metadata value is same as the existing value, then the zonal metadata entry remains unchanged.




#### Example: Add a new custom zonal metadata entry

For example, consider a project called `my-project` with the following custom metadata:

  * Project metadata: `"key-1":"value-a"`, `"key-2":"value-b"`, and `"key-3":"value-c"`
  * Zonal metadata in `us-central1-a` zone: `"key-1":"value-1"` and `"key-2":"value-2"`



To add `"key-4":"value-4"` as a new custom zonal metadata pair in the `us-central1-a` zone, make the following `PATCH` request:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instanceSettings?update_mask=metadata.items.key-4
    {
      "fingerprint": "VlRIl8dx9vk=",
      "metadata": {
      "items": {
        "key-4": "value-4"
        }
      }
    }
    

#### Example: Update the values of an existing custom zonal metadata entry

Consider the same example project `my-project`, which now has the following custom metadata:

  * Project metadata: `"key-1":"value-a"`, `"key-2":"value-b"`, and `"key-3":"value-c"`
  * Zonal metadata in `us-central1-a` zone: `"key-1":"value-1"`, `"key-2":"value-2"`, and `"key-4":"value-4"`



To update the zonal metadata values of `key-1` and `key-4` in `us-central1-a` zone with new values, make the following `PATCH` request:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instanceSettings?update_mask=metadata.items.key-1,metadata.items.key-4
    {
      "fingerprint": "VlRIl8dx9vk=",
      "metadata": {
      "items": {
        "key-1": "new-value-1",
        "key-4": "new-value-4"
        }
      }
    }
    

**Note:** For `key-1`, which has different values set at project and zonal levels, only the zonal metadata value gets updated after you run the command. The project metadata value for `key-1` remains unchanged. In the future, if you delete the zonal metadata entry for `key-1`, then the VMs in the zone inherit the project metadata value.

#### Example: Override the project metadata value for a key and set a zonal metadata value

Consider the same example project `my-project`, which now has the following custom metadata:

  * Project metadata: `"key-1":"value-a"`, `"key-2":"value-b"`, and `"key-3":"value-c"`
  * Zonal metadata in `us-central1-a` zone: `"key-1":"new-value-1"`, `"key-2":"value-2"`, and `"key-4":"new-value-4"`



In this example project, consider `key-3`, which has a project metadata value of `value-c`. Suppose you want to set a zonal metadata value `value-3` for this key for all VMs in the `us-central1-a` zone. When you perform the operation, for all the VMs in the `us-central1-a` zone, Compute Engine overrides the project metadata values and uses the zonal metadata values. VMs in all other zones of the project retain their prevailing project or zonal metadata values for `key-3`.

To override the project metadata value for `key-3` and use the zonal metadata value `value-3` instead, make the following `PATCH` request:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instanceSettings?update_mask=metadata.items.key-3
    {
      "fingerprint": "VlRIl8dx9vk=",
      "metadata": {
      "items": {
        "key-3": "value-3"
        }
      }
    }
    

**Note:** If you subsequently update the value for `key-3` on a project level, then your update doesn't get added to the `/project/attributes` directory of the metadata server in the `us-central1-a` zone. If you want your future project metadata value update for `key-3` to get posted to the `/project/attributes` folder in the `us-central1-a` zone, then you must first remove the zonal metadata entry.

### Set custom instance metadata

You can add or update the custom metadata for a single VM instance by using the Google Cloud console, the Google Cloud CLI, or REST.

You can set custom instance metadata in one of the following ways:

  * For new VMs, you can add custom metadata when the VM is being created.
  * For existing VMs, you can add or update custom metadata when the VM is running.



#### Add custom instance metadata during VM creation

Use these instructions to add metadata on a specific VM instance at the time of its creation.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. Specify the VM details.

  3. Expand the **Advanced options** section, and do the following:

     1. Expand the **Management** section.
     2. To add multiple key-value pairs for your custom metadata, in the **Metadata** section, click **Add item**.
  4. To create the VM, click **Create**.




###  gcloud 

To set custom metadata, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--metadata` flag.
    
    
    gcloud compute instances create VM_NAME \
    --zone=ZONE \
    --image-project=IMAGE_PROJECT \
    IMAGE_FLAG \
    --metadata=KEY=VALUE

Replace the following:

  * `VM_NAME`: the name of your VM
  * `ZONE`: the zone to create the VM in
  * `IMAGE_PROJECT`: the [project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) containing the image to use for the VM
  * `IMAGE_FLAG`: specify one of the following:

    * Use the `--image IMAGE_NAME` flag to specify a specific version of a public image.

For example, `--image debian-12-bookworm-v20241112`.

    * Use the `--image-family IMAGE_FAMILY_NAME` flag to specify an [image family](https://docs.cloud.google.com/compute/docs/images/os-details#general-info).

This creates the VM from the most recent non-deprecated OS image in the image family. For example, if you specify `--image-family debian-12`, Compute Engine uses the latest version of the OS image in the Debian 12 image family.

  * `KEY`: the name of your metadata key

  * `VALUE`: the value stored for this key




**Example**

For example to set a new key `env` that has a value `test` on a VM named `example-instance`, run the following command:
    
    
     gcloud compute instances create example-instance \
       --zone=us-central1-a --image-project=debian-cloud \
       --image-family=debian-12 \
       --metadata=env=test

###  REST 

Use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) and provide the custom metadata as part of the `metadata` property in your request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "machineType": "zones/MACHINE_TYPE_ZONE/machineTypes/MACHINE_TYPE",
      "name": "VM_NAME",
      "...": [
        {
        }
        ],
      "metadata": {
        "items": [
          {
            "key": "KEY",
            "value": "VALUE"
          }
        ]
      },
      ..
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `ZONE`: zone to create the VM in
  * `MACHINE_TYPE`: machine type, [predefined](https://docs.cloud.google.com/compute/docs/machine-resource#predefined-types) or [custom](https://docs.cloud.google.com/compute/docs/machine-resource#custom-types), for the new VM
  * `VM_NAME`: [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the new VM
  * `KEY`: the name of your metadata key
  * `VALUE`: the value stored for this key



#### Add or update custom instance metadata on an existing VM

Use these instructions to update metadata on a specific VM instance that already exists.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click the instance for which you want to update metadata.
  3. Click the **Edit** button at the top of the page.
  4. Under **Custom metadata** , click **Add item** or edit the existing metadata entries.
  5. Save your changes.



###  gcloud 

Updating VM metadata with the gcloud CLI is an additive action. Specify only the metadata keys that you want to add or change. If a key that you provided already exists, the value for that key is updated with the new value.

Use the [`instances add-metadata` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata):
    
    
    gcloud compute instances add-metadata VM_NAME \
        --metadata=KEY=VALUE,KEY=VALUE
    

Replace the following:

  * `VM_NAME`: the name of your VM
  * `KEY`: the name of your metadata key
  * `VALUE`: the value stored for this key



**Examples**

If you want to add the `foo=bar` entry, use:
    
    
    gcloud compute instances add-metadata VM_NAME \
        --metadata=foo=bar
    

If you want to change the `foo=bar` entry to `foo=bat`, use:
    
    
    gcloud compute instances add-metadata VM_NAME \
        --metadata=foo=bat
    

###  REST 

**Note:** If using `curl` or `Invoke-RestMethod` to update metadata on a VM, then add the `Content-Type:application/json` header to the request.

  1. Get the current fingerprint and view any existing key-value pairs for the VM. To do this, call the [`instances().get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get).

A fingerprint is a random string of characters generated by Compute Engine and is used to perform optimistic locking. To update the VM, you need to provide the matching fingerprint value. The fingerprint changes after each request, and if you provide a mismatched fingerprint, your request is rejected. This works so that only one update can be made at a time, preventing collisions.
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `ZONE`: the zone where your VM is located
     * `VM_NAME`: name of your VM

The output is similar to the following:
    
    {
      ...
      "name": "example-instance",
      "metadata": {
        "kind": "compute#metadata",
        "fingerprint": "zhma6O1w2l8="
        "items": [
          {
            "key": "foo",
            "value": "bar"
          }
        ]
        },
      ...
    }
    

  2. Make a request to the [`instances().setMetadata` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/setMetadata). Provide a list of the new metadata values and the current `fingerprint` value.

If the VM has existing key-value pairs that you want to keep, you must include them in this request with the new key-value pairs.

**Example**
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setMetadata
         
         {
         "fingerprint": "zhma6O1w2l8=",
         "items": [
           {
             "key": "foo",
             "value": "bar"
           },
           {
             "key": "baz",
             "value": "bat"
           }
         ]
         }
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `ZONE`: the zone where your VM is located
     * `VM_NAME`: name of your VM



## Remove custom metadata from VMs

This section provides information about how to remove custom metadata entries for your Compute Engine VMs in one of the following ways:

  * Remove custom project metadata, to remove custom metadata that was set for all VMs in a project.
  * Remove custom zonal metadata to remove custom metadata that was set for all VMs in a specific zone in a project.
  * Remove custom instance metadata to remove VM metadata that was set for a specific VM.



### Remove custom project metadata

You can remove custom project metadata by using the Google Cloud console or the Google Cloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **Metadata** page.

[Go to the Metadata page](https://console.cloud.google.com/compute/metadata)

  2. Click edit **Edit** at the top of the page.

  3. Navigate to the metadata entry that you want to remove and click the delete delete button next to that entry.

Repeat this step for each metadata entry that you want to remove.

  4. To finish removing the custom project metadata entries, click **Save**.




###  gcloud 

To remove custom project metadata, use the [`gcloud compute project-info remove-metadata` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-info/remove-metadata).

  * If you want to remove the custom metadata entries for specific keys, specify those keys by using the `--keys` flag, and exclude the values of those keys.


    
    
    gcloud compute project-info remove-metadata \
        **--keys= KEY1,KEY2,...**
    

  * If you want to remove all custom metadata for the VM, specify the `--all` flag.


    
    
    gcloud compute project-info remove-metadata \
        **--all**
    

Replace the following:

  * `KEY1`, `KEY2`...: the custom instance metadata keys that you want to remove.



### Remove custom zonal metadata

You can remove custom zonal metadata by using the Google Cloud CLI or REST.

###  gcloud 

To remove custom zonal metadata, use the [`gcloud compute project-zonal-metadata remove` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/remove) and specify all the metadata keys that you want to remove by using the `--keys` flag.
    
    
    gcloud compute project-zonal-metadata remove \
        --project=PROJECT_ID  \
        --zone=ZONE \
        --keys=KEY1,KEY2,...

Replace the following:

  * `PROJECT_ID`: your project ID
  * `ZONE`: the zone where you want to remove the zonal metadata.
  * `KEY1`, `KEY2`...: the custom zonal metadata keys that you want to remove.



After you run the command, if any of the specified keys have project metadata values available, then the VMs in the specified zone inherit those project metadata values. If the metadata entry was set only at a zonal level and there isn't a corresponding project metadata value for that key, then VMs in that zone lose that metadata information.

#### Example:

Consider an example project `my-project`, which has the following custom project metadata:

  * Project metadata: `"key-1":"value-a"`, `"key-2":"value-b"`, and `"key-3":"value-c"`
  * Zonal metadata in `us-central1-a` zone: `"key-1":"new-value-1"`, `"key-2":"value-2"`, `"key-3":"value-3"`, and `"key-4":"new-value-4"`



To remove all the zonal metadata in the `us-central1-a` zone, run the following command.
    
    
    gcloud compute project-zonal-metadata remove \
        --metadata=key-1,key-2,key-3,key-4 \
        --project=my-project \
        --zone=us-central1-a
    

After you run the command, VMs in the `us-central1-a` zone possess the following custom project metadata entries:

  * `"key-1":"value-a"`
  * `"key-2":"value-b"`
  * `"key-3":"value-c"`



###  REST 

  1. Get the current fingerprint and view any existing key-value pairs for the project in that zone.

To perform optimistic locking, you must provide a fingerprint. A fingerprint is a random string of characters generated by Compute Engine. The fingerprint changes every time you make a request to add, update, or remove zonal metadata, and if you provide a mismatched fingerprint, Compute Engine rejects your request.

If you don't provide a fingerprint, a check for consistency is performed and your deletion request doesn't succeed. This works so that only one request can be made at a time, preventing collisions. This behavior matches `instances().setMetadata`, where a fingerprint is always required.

To get the current fingerprint of a project, make a call the [`instanceSettings().get` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/instanceSettings/get).
         
         GET https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/instanceSettings
         

Replace the following:

     * `PROJECT_ID`: your project ID
     * `ZONE`: the zone where you want to remove the zonal metadata.

The following is an example output for this request:
    
    {
          "fingerprint": "FikclA7UBC0=",
          "metadata": {
            ...
          }
        }
    

  2. To remove custom zonal metadata, make a `PATCH` request to the [`instanceSettings().patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/instanceSettings/patch) by excluding the metadata keys, for which you want to remove the zonal metadata, from the request body. You must provide the following with your request:

     * An update mask. Use the `update_mask` query parameter. The update mask must contain all the existing custom metadata keys for which you want to remove the zonal metadata. You must add the string `metadata.items.` as a prefix for each key—for example, `metadata.items.key1,metadata.items.key3`.

**Important:** The update mask must be in lower case.
     * In the request body, provide only the current fingerprint value. Exclude all the custom metadata keys that you specified in the update mask. If you include any of the metadata keys in both the update mask and the request body, then Compute Engine doesn't remove the zonal metadata for those keys. 
    
    PATCH https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/instanceSettings?**update_mask** =PREFIXED_METADATA_KEYS
    {
      "fingerprint": "FINGER_PRINT",
      "metadata": {
        "items": {
        }
      }
    }
    

Replace the following:

     * `PROJECT_ID`: the ID of the project.
     * `ZONE`: the zone where you want to remove the zonal metadata.
     * `PREFIXED_METADATA_KEYS`: the list of all the existing custom metadata keys for which you want to remove zonal metadata, where each key is prefixed with the string `metadata.items.` . To ensure that your deletion request is successful, exclude these metadata keys from the request body. If you include any of the metadata keys in both the update mask and the request body, then Compute Engine doesn't remove the zonal metadata for those keys. 

For example, suppose your current metadata keys with zonal metadata are `key-1`, `key-2`, `key-3`, and `key-4`, and you want to remove the zonal metadata entries for `key-1` and `key-2`, then your update mask must have the following string:

`metadata.items.key1,metadata.items.key2`

     * `FINGER_PRINT`: the current fingerprint value.




After you make the request, if any of the specified keys have project metadata values available, then the VMs in the specified zone inherit those project metadata values. If the metadata key was set only at a zonal level and there isn't a corresponding project metadata value for that key, then VMs in that zone lose that metadata information.

#### Example:

Consider an example project `my-project`, which has the following custom project metadata:

  * Project metadata: `"key-1":"value-a"`, `"key-2":"value-b"`, and `"key-3":"value-c"`
  * Zonal metadata in `us-central1-a` zone: `"key-1":"new-value-1"`, `"key-2":"value-2"`, `"key-3":"value-3"`, and `"key-4":"new-value-4"`



To remove the zonal metadata for `key-1` and `key-2` in the `us-central1-a` zone, make the following `PATCH` request.
    
    
    PATCH https://compute.googleapis.com/compute/beta/projects/my-project/zones/us-central1-a/instanceSettings?update_mask=metadata.items.key-1,metadata.items.key-2
    {
      "fingerprint": "FikclA7UBC0=",
      "metadata": {
      "items": {
        }
      }
    }
    

After this request goes through, VMs in the `us-central1-a` zone possess the following custom metadata. VMs inherit the project metadata values for `key-1` and `key-2`, but retain the zonal metadata for `key-3` and `key-4`.

  * Project metadata: `"key-1":"value-a"` and `"key-2":"value-b"`
  * Zonal metadata in `us-central1-a` zone: `"key-3":"value-3"` and `"key-4":"new-value-4"`



### Remove custom instance metadata

You can remove custom instance metadata by using the Google Cloud console, the Google Cloud CLI or REST.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of the VM for which you want to remove metadata.
  3. Click edit  **Edit** at the top of the page.
  4. In the **Metadata** section, click delete **Delete item** for each of the metadata entries that you want to remove.
  5. To confirm your changes and remove the custom instance metadata, click **Save**.



###  gcloud 

To remove custom instance metadata, use the [`gcloud compute instances remove-metadata` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/remove-metadata).

  * If you want to remove the custom metadata entries for specific keys, specify those keys by using the `--keys` flag, and exclude the values of those keys.


    
    
    gcloud compute instances remove-metadata VM_NAME \
        --zone=ZONE  \
        **--keys= KEY1,KEY2,...**
    

  * If you want to remove all custom metadata for the VM, specify the `--all` flag.


    
    
    gcloud compute instances remove-metadata VM_NAME \
        --zone=ZONE  \
        **--all**
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `ZONE`: the zone of your VM.
  * `VM_NAME`: name of your VM
  * `KEY1`, `KEY2`...: the custom instance metadata keys that you want to remove.



###  REST 

  1. Get the current fingerprint and view any existing key-value pairs for the VM. To do this, call the [`instances().get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get).

A fingerprint is a random string of characters generated by Compute Engine and is used to perform optimistic locking. To update the VM, you need to provide the matching fingerprint value. The fingerprint changes after each request, and if you provide a mismatched fingerprint, your request is rejected. This works so that only one update can be made at a time, preventing collisions.
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME
         

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `ZONE`: the zone of your VM.
     * `VM_NAME`: name of your VM

The output is similar to the following:
    
    {
      ...
      "name": "example-instance",
      "metadata": {
        "kind": "compute#metadata",
        "fingerprint": "zhma6O1w2l8="
        "items": [
        {
          "key": "key-1",
          "value": "value-1"
        }
        {
          "key": "key-2",
          "value": "value-2"
        }
        ]
      },
      ...
    }
    

  2. Make a request to the [`instances().setMetadata` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/setMetadata). You must include the current metadata fingerprint value for your request to succeed.

     * To remove all custom metadata key-value pairs from a VM, in the `items` property, exclude the metadata keys for which you want to remove metadata values.
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setMetadata
           
           {
           "fingerprint": "FINGER_PRINT"
           "items": [
             {
               "key": "KEY1"
               "value": "VALUE1"
             }
             {
               "key": "KEY2"
               "value": "VALUE2"
             }
             ...
           ]
           }
           

     * To remove all custom instance metadata on the VM, exclude the `items` property altogether.
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setMetadata
           
           {
           "fingerprint": FINGER_PRINT
           }
           

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `ZONE`: the zone of your VM.
     * `VM_NAME`: name of your VM
     * `FINGER_PRINT`: the current fingerprint value.
     * `KEY1`, `KEY2`...: the custom instance metadata keys that you want to remove.
     * `VALUE1`, `VALUE2`...: the values of the custom instance metadata keys that you want to remove.



## What's next

  * Learn how to [view and query metadata](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata).
  * Learn more about [running startup scripts](https://docs.cloud.google.com/compute/docs/instances/startup-scripts) or [shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript) in the metadata server.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
