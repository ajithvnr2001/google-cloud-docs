---
url: https://docs.cloud.google.com/compute/docs/instances/detect-compute-engine/
title: Detect if a VM is running in Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:09.848262+00:00
---

# Detect if a VM is running in Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/detect-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Detect if a VM is running in Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document shows you how to use the metadata server or an operating system tool to detect whether a VM is running in Compute Engine.

## Use the metadata server to detect if a VM is running in Compute Engine

Depending on the VM's operating system, use one of the following procedures to send a request to the [metadata server](https://docs.cloud.google.com/compute/docs/metadata/overview) and detect if a VM is running in Compute Engine:

###  Linux VM 

  1. From the Linux VM, run the following command:
         
         curl metadata.google.internal -i
         

  2. Verify that `Metadata-Flavor: Google` exists in output similar to the following:
         
         HTTP/1.1 200 OK
         Metadata-Flavor: Google
         Content-Type: application/text
         Date: Tue, 23 Nov 2021 01:27:16 GMT
         Server: Metadata Server for VM
         Content-Length: 22
         X-XSS-Protection: 0
         X-Frame-Options: SAMEORIGIN
         
         0.1/
         computeMetadata/
         

The existence of `Metadata-Flavor: Google` in the output indicates that a Compute Engine VM sent the request.




###  Windows VM 

  1. From the Windows VM, run the following command:
         
         curl metadata.google.internal -i
         

  2. Verify that `Metadata-Flavor: Google` exists in output similar to the following:
         
         HTTP/1.1 200 OK
         Metadata-Flavor: Google
         Content-Type: application/text
         Date: Tue, 23 Nov 2021 20:48:50 GMT
         Server: Metadata Server for VM
         Content-Length: 22
         X-XSS-Protection: 0
         X-Frame-Options: SAMEORIGIN
         
         0.1/
         computeMetadata/
         

The existence of `Metadata-Flavor: Google` in the output indicates that a Compute Engine VM sent the request.




## Use operating system tools to detect if a VM is running in Compute Engine

Depending on the VM's operating system, use one of the following procedures to use a tool that is specific to the VM's operating system to detect if the VM is running in Compute Engine:

###  Linux VM 

  1. From the Linux VM, run the following [`dmidecode`](http://www.nongnu.org/dmidecode/) command:
         
         sudo dmidecode -s system-product-name | grep "Google Compute Engine"
         

This `dmidecode` command directly accesses the System Management BIOS information in `/proc/mem`.

  2. Verify that `Google Compute Engine` exists in the output.




###  Windows VM 

  1. From the Windows Command Prompt, run the [WMI command-line utility](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmic):
         
         wmic.exe computersystem get model,manufacturer
         

  2. Verify that the `System Manufacturer` is `Google` and the `System Model` is `Google Compute Engine`.




For information about how to programmatically determine whether a Windows VM is running Compute Engine, see the following:

  * [Create a WMI application using C++](http://msdn.microsoft.com/library/windows/desktop/aa389762%28v=vs.85%29.aspx)
  * [Getting manufacturer and model from the Windows registry in C++](http://stackoverflow.com/questions/12300442/how-to-get-computer-manufacturer-and-model-from-windows-registry-in-c)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
