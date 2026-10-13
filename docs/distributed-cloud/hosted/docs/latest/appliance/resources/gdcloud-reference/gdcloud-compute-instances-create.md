---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-compute-instances-create/
title: gdcloud compute instances create \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:29.627833+00:00
---

# gdcloud compute instances create  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-compute-instances-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud compute instances create Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud compute instances create - Create virtual machine instances.

## SYNOPSIS
    
    
    gdcloud compute instances create INSTANCE_NAME [flags]
    

### EXAMPLES
    
    
    To create an instance with the out-of-the-box Ubuntu image, run:
    
        gdcloud compute instances create example-instance \
        --project example-project \
        --machine-type n2-standard-2-gdc \
        --boot-disk-size 10GB \
        --image-name ubuntu-20.04-server-cloudimg-amd64-1.0 \
        --image-project vm-system
    
    To create an instance with an existing disk, run:
    
        gdcloud compute instances create example-instance \
        --project example-project \
        --machine-type n2-standard-2-gdc \
        --disk=name=example-disk,boot=true
    

### OPTIONAL FLAGS
    
    
          --boot-disk-size string      The size of the boot disk.
                                       Can only be specified if a new boot disk is being created by providing the "image"
                                       (as opposed to mounting an existing disk).
                                       The value must be a whole number followed by a size unit of GB for gigabyte, or TB for terabyte.
                                       For example, "10GB" will produce a 10 gigabyte disk.
                                       The disk size must be a multiple of 1 GB.
                                       If not specified, the minimum disk size of the boot image will be used.
                                       If the minimum disk size is not set in the image, an error will be thrown.
          --custom-cpu uint32          A whole number value specifying the number of cores to configure for the virtual machine instance.
                                       Must be specified if "machine-type" is empty.
          --custom-memory string       A whole number value indicating how much memory to configure for the virtual machine instance.
                                       A size unit should be provided (eg. 8GB).
                                       Must be specified if "machine-type" is empty.
          --description string         The description of the virtual machine instance.
          --disk stringArray           Attaches persistent disks to the virtual machine instance. The disks specified must already exist.
                                       For each disk that is to be attached, the following attributes must be specified as key=value pairs:
                                       name:        The name of the disk to attach to the virtual machine instance
                                       boot:        If set to true, this disk will be used as the boot disk (default false)
                                       auto-delete: If set to true, this disk will be automatically deleted when
                                                    the virtual machine instance is deleted (default false)
                                       read-only:   Whether the disk should be attached to the VM in read-only mode (default false)
                                       For example, "--disk name=disk1,boot=true --disk name=disk2".
          --enable-external-access     Indicate whether the virtual machine instance should have networking ingress and egress NAT enabled.
          --image string               The boot image name for the instance.
                                       A new boot disk will be created from the given image.
                                       To view a list of available image to use, run "gdcloud compute images list".
          --image-project string       The project of the boot image for the instance.
                                       If specifying one of our public shared images, "image-project" must be provided.
                                       The public shared image project is "vm-system".
                                       If not specified, but "image" is provided, the current default project will be used.
                                       Only public shared images and images in the same project as the instance are supported.
          --labels stringToString      List of comma-separated KEY=VALUE labels to add to the virtual machine instance.
                                       For example, "--labels key1=val1,key2=val2". (default [])
          --machine-type string        The name of the predefined machine type to be used to create the virtual machine instance.
                                       Must be specified if one of "custom-cpu" and "custom-memory" is empty.
                                       To view a list of available machine types, run "gdcloud compute machine-types list"
          --no-boot-disk-auto-delete   Disable automatically deleting the boot disk when the instance is deleted
                                       (automatic deletion is enabled by default).
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
