---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-artifacts-vm-images-package/
title: gdcloud artifacts vm-images package \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:18.736527+00:00
---

# gdcloud artifacts vm-images package  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-artifacts-vm-images-package/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud artifacts vm-images package Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud artifacts vm-images package - Package a VM image file into an OCI artifact.

## SYNOPSIS
    
    
    gdcloud artifacts vm-images package SOURCE DESTINATION [flags]
    

### EXAMPLES
    
    
    To package a VM image into a format compatible with System Artifact Registry, run:
    
                gdcloud artifacts vm-images package SOURCE DESTINATION \
                --name IMAGE_NAME \
                --version VERSION_NUMBER \
                --os IMAGE_OS
    

### OPTIONAL FLAGS
    
    
          --limit-object-storage-distribution string   Limit the distribution of the image to object storage in specific organizations.
                                                       Set the value to "gdchservices" to only distribute the image to the
                                                       object storage of the "gdchservices" organization.
                                                       Set the value to "none" to prevent the distribution of the image to the
                                                       object storage of any organization.
                                                       If this value is empty, the image is distributed to the
                                                       object storage of all organizations.
          --minimum-disk-size string                   Minimum size of the disk this image can be used on. For example, 10GB.
          --name string                                Name of the VM image.
          --node-vm-image                              If set, the VM image is a GDC air-gapped internal cluster node image.
          --os string                                  Operating system of the image. Must be one of: [rhel-8 rocky-linux-8 rocky-linux-9 ubuntu-2004 ubuntu-2204 ubuntu-2404 windows-10 windows-2019]
          --version string                             Version of the VM image. For example, 0.1.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
