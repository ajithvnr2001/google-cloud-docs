---
url: https://docs.cloud.google.com/compute/docs/gcloud-compute/transition-gcloud-gcutil/
title: Transitioning from gcutil to gcloud compute \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:20:38.853775+00:00
---

# Transitioning from gcutil to gcloud compute  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gcloud-compute/transition-gcloud-gcutil/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)



Send feedback 

#  Transitioning from gcutil to gcloud compute Stay organized with collections  Save and categorize content based on your preferences. 

With `gcloud compute` in General Availability, Compute Engine recommends that all users transition to the `gcloud compute` tool from `gcutil`. `gcloud compute` is a unified command-line tool that features a number of improvements over `gcutil`, including:

  * Tab completion
  * In-place upgrading
  * Extensive man-page style help
  * Choice of different output formats



To help users transition from `gcutil` to `gcloud compute`, this guide briefly describes the major changes between the two tools. For a detailed description of the `gcloud compute` tool, see the [`gcloud compute`](https://docs.cloud.google.com/compute/docs/gcloud-compute) documentation.

## New gcloud commands

All existing `gcutil` commands have equivalent commands in the `gcloud compute` tool, with a few exceptions. You can get a full list of the `gcloud` commands by visiting the [reference pages](https://docs.cloud.google.com/sdk/gcloud/reference/compute) or by running `gcloud compute --help`. The table below briefly outlines the changes from popular `gcutil` commands.

gcutil command | gcloud compute command  
---|---  
      
    
    gcutil addinstance INSTANCE

| 
    
    
    gcloud compute instances create INSTANCE  
  
###### Notes

Creates an instance.

  * Default zone/region can be set, otherwise `gcloud compute` prompts for a zone/region.
  * Creates virtual machines with default properties, such as: 
    * machine-type: n1-standard-1
    * image: debian-10

See [Creating and starting an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).   
gcutil command | gcloud compute command  
---|---  
      
    
    gcutil deleteinstance INSTANCE

| 
    
    
    gcloud compute instances delete INSTANCE \
           [--keep-disks {boot,all,none}]  
  
###### Notes

Deletes instances. See [Deleting an instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).  
gcutil command | gcloud compute command  
---|---  
      
    
    gcutil ... --cache_flag_values

| 
    
    
    gcloud configs set project PROJECT
    gcloud configs set compute/zone ZONE
    gcloud configs set compute/region REGION
      
  
###### Notes

Sets the default values for project, zone, and region. See [Setting a default zone and region](https://docs.cloud.google.com/compute/docs/gcloud-compute#default-properties).  
gcutil command | gcloud compute command  
---|---  
      
    
    gcutil push/pull

| 
    
    
    gcloud compute scp  
  
###### Notes

Copies files between a local computer and a virtual machine. See [Transfer files using the Google Cloud CLI](https://docs.cloud.google.com/compute/docs/instances/transfer-files#transfergcloud).  
gcutil command | gcloud compute command  
---|---  
      
    
    gcutil deleteRESOURCE

| 
    
    
    gcloud compute RESOURCES delete  
  
###### Notes

Deletes resources, for example: 
    
    
    gcloud compute instances delete example-instance  
  
gcutil command | gcloud compute command  
---|---  
      
    
    gcutil getRESOURCES

| 
    
    
    gcloud compute RESOURCES describe  
  
###### Notes

Describes a single resource, for example: 
    
    
    gcloud compute instances describe example-instance  
  
gcutil command | gcloud compute command  
---|---  
      
    
    gcutil listRESOURCES

| 
    
    
    gcloud compute RESOURCES list  
  
###### Notes

List all resources of that type. For example, to list instances: 
    
    
    gcloud compute instances list  
  
gcutil command | gcloud compute command  
---|---  
      
    
    gcutil setmetadata

| 
    
    
    gcloud compute instances add-metadata
    gcloud compute instances remove-metadata
    gcloud compute project-info add-metadata
    gcloud compute project-info remove-metadata  
  
###### Notes

Optimistic locking is now done by the tool, so there is no need to specify a fingerprint manually. See [Setting custom instance metadata](https://docs.cloud.google.com/compute/docs/metadata#updatinginstancemetadata).  
gcutil command | gcloud compute command  
---|---  
      
    
    gcutil … --dump_request_response

|  Not yet available.  
gcutil command | gcloud compute command  
---|---  
      
    
    gcutil … --log_level=DEBUG

| 
    
    
    gcloud … --verbosity debug  
  
###### Notes

Also, logs are stored in files for every command in ~/.config/gcloud/logs.  
gcutil command | gcloud compute command  
---|---  
      
    
    gcutil ssh INSTANCE --ssh_user

| 
    
    
    gcloud compute ssh USER@INSTANCE  
  
###### Notes

See [Connecting to an Instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).  
gcutil command | gcloud compute command  
---|---  
      
    
    gcutil … \
    --image=projects/project-id/global/images/image
    

| 
    
    
    gcloud compute … --image image-name \
           --image-project image-project  
  
###### Notes

See [Starting an instance from an image](https://docs.cloud.google.com/compute/docs/images#starting_an_instance_from_an_image).  
gcutil command | gcloud compute command  
---|---  
      
    
    gcutil deleteinstances --[no]delete_pd
    gcutil deleteinstances --[no]delete_boot_pd
    

| 
    
    
    gcloud compute instances delete … \
           --delete-disks {all,none,boot}
    gcloud compute instances delete … \
           --keep-disks {all,none,boot}
      
  
###### Notes

If a disk is marked to be auto-deleted, it will be automatically deleted unless specified using the `--keep-disks` flag.  
  
## Default instance settings

Creating an instance in `gcloud compute` now has several default values provided for the image and machine type of your virtual machine. You can choose to use these default values by omitting the `--image` and `--machine-type` flags, or you can override the settings by providing the appropriate flags. The default virtual machine settings are:

  * Default image: latest debian-10 image
  * Default machine type: n1-standard-1



For example, you can simply run:
    
    
    gcloud compute instances create example-instance --zone us-central1-a
    

And the `gcloud compute` will create the instance using the image and machine type described above.

## Output formatting

The default output formatting has changed and differs depending on the command you run. For example, if you run the `describe` command to get information about a single resource, the response output is in YAML format. You can return the response in different output formats, like JSON or text, using the `--format` flag:
    
    
    gcloud compute instances list --format {json,yaml,text}
    

## Updating metadata is now additive

When setting or updating metadata, you no longer need to provide a fingerprint. By default, all metadata changes are considered additive. You can add single metadata entries or update entries without performing a batch update of all of the metadata. Only metadata keys that are passed in will be mutated.
    
    
    gcloud compute instances add-metadata example-instance \
             --metadata cookies=chocolate
    

## Specifying image projects

Previously, to specify an exact image, you needed to provide a partial image URI, which included the project name, like so:
    
    
    gcutil addinstance example-instance \
             --image=projects/debian-cloud/global/images/debian-9
    

In `gcloud compute`, you must now specify the image project using a new `--image-project` flag:
    
    
    gcloud compute instances create example-instance \
             --image debian-9-stretch-vYYYMMDD
             --image-project debian-cloud
    

You can also provide the full URI:
    
    
    gcloud compute instances create example-instance \
             --image https://compute.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-9-stretch-vYYYMMDD
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
