---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/virtualmachine/vmm-api-overview/
title: Overview of Virtual Machine Manager API \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:52.034122+00:00
---

# Overview of Virtual Machine Manager API  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/virtualmachine/vmm-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Overview of Virtual Machine Manager API Stay organized with collections  Save and categorize content based on your preferences. 

The Virtual Machine Manager (VMM) of Google Distributed Cloud (GDC) air-gapped appliance uses Kubernetes Resource Model (KRM) APIs in its virtual machine (VM) operations and lifecycle management. 

Use the `kubectl` CLI for the VMM APIs.

## Service endpoint

The API endpoint for the VMM API is `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/virtualmachine.gdc.goog/v1`, where `MANAGEMENT_API_SERVER_ENDPOINT` is the endpoint of the Management API server.

## Discovery document

Use the `kubectl proxy` command to open a proxy to the API server on your local machine. From there, you can access the discovery document at the following URL: `http://127.0.0.1:8001/apis/virtualmachine.gdc.goog/v1`.

## Example of VM KRM

The following `VirtualMachineImageImport` file shows the creation of a disk image from a persistent disk. You choose the persistent disk from a `VirtualMachineDisk` list and select it to create the image and get the `size` parameter of the source. The same example is on the [Create custom images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-custom-images/create-custom-images) page.
    
    
    apiVersion: virtualmachine.gdc.goog/v1
    kind: VirtualMachineImageImport
    metadata:
      name: VM_IMAGE_IMPORT_NAME
      # Name of the VM image you want to import.
    spec:
      source:
        diskRef:
          name: DISK_NAME
          # Name of the source disk that you will use to create your image.
      imageMetadata:
        name: IMAGE_NAME
        # Name of your created VM image.
        operatingSystem: OS_NAME
        # Name of the image OS. Select one of the following four options: ubuntu-2004, windows-2019, rhel-8, or rocky-linux-8.
        minimumDiskSize: MINIMUM_DISK_SIZE
        # Disk size in the VM image. It must be greater than or equal to the source disk size. An example value is 20G.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
