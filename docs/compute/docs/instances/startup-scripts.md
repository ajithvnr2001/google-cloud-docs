---
url: https://docs.cloud.google.com/compute/docs/instances/startup-scripts/
title: About startup scripts \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:56:19.317449+00:00
---

# About startup scripts  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/startup-scripts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About startup scripts Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

A startup script is a file that contains commands that run when a virtual machine (VM) instance boots. Compute Engine provides support for running startup scripts on Linux VMs and Windows VMs.

## Prerequisites

To run scripts stored in metadata on a VM instance, the [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) must be installed and running.

  * The guest environment includes the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) (for example, google-guest-agent on Linux) that reads the script content or URL from the instance's metadata and initiates execution.
  * All public Compute Engine images come with the guest environment preinstalled.
  * If you create a custom image, you must [manually install the Google Guest Environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment) to ensure scripts from metadata and other Google Cloud features function properly.



The following table contains links to documentation that describes how to use startup scripts.

Startup script task | Best used for | Link to procedure  
---|---|---  
Pass a startup script directly | Scripts up to 256 KB |  | [Linux VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/linux#passing-directly) | [Windows VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows#passing-directly)  
---|---  
Pass a startup script from a local file | Scripts up to 256 KB |  | [Linux VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/linux#passing-local) | [Windows VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows#passing-local)  
---|---  
Pass a startup script from Cloud Storage | Scripts greater than 256 KB |  | [Linux VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/linux#passing-storage) | [Windows VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows#passing-storage)  
---|---  
Access metadata from a startup script | Passing different values to each VM that uses the same script |  | [Linux VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/linux#accessing-metadata) | [Windows VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows#accessing-metadata)  
---|---  
Rerun a startup script | Running a script without restarting the VM |  | [Linux VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/linux#rerunning) | [Windows VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows#rerunning)  
---|---  
View the output from a startup script | Monitoring the progress of a script |  | [Linux VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/linux#viewing-output) | [Windows VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows#viewing-output)  
---|---  
  
## What's next

  * Learn how to [add a shutdown script](https://docs.cloud.google.com/compute/docs/shutdownscript).
  * Learn how to [use startup scripts on Linux VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/linux).
  * Learn how to [use startup scripts on Windows VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
