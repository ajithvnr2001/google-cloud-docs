---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-compute-disks-create/
title: gdcloud compute disks create \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:29.405418+00:00
---

# gdcloud compute disks create  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-compute-disks-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud compute disks create Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud compute disks create - Create virtual machine disks.

## SYNOPSIS
    
    
    gdcloud compute disks create DISK_NAME [flags]
    

### EXAMPLES
    
    
    To create a disk with a certain image, run:
    
        gdcloud compute disks create example-disk \
        --project example-project \
        --size 10GB \
        --image ubuntu-20.04-server-cloudimg-amd64-1.0 \
        --image-project vm-system
    
    To create a blank disk, run:
    
        gdcloud compute disks create example-disk \
        --project example-project \
        --size 10GB
    

### OPTIONAL FLAGS
    
    
          --image string           The image name for the disk.
                                   The disk will be created from the given image.
                                   If not specified, the created disk will be blank.
                                   To view a list of available image to use, run "gdcloud compute images list".
          --image-project string   The project of the image for the disk.
                                   If specifying one of our public shared images, "image-project" must be provided.
                                   The public shared image project is "vm-system".
                                   If not specified, but "image" is provided, the current default project will be used.
                                   Only public shared images and images in the same project as the instance are supported.
          --size string            The size of the disk.
                                   The value must be a whole number followed by a size unit of GB for gigabyte, or TB for terabyte.
                                   For example, "10GB" will produce a 10 gigabyte disk.
                                   The disk size must be a multiple of 1 GB.
                                   If not specified, the minimum disk size of the boot image will be used.
                                   If the minimum disk size is not set in the image, an error will be thrown.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
