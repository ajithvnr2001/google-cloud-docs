---
url: https://docs.cloud.google.com/compute/docs/deprecations/serial-console-ssh-host-key-endpoint/
title: Serial console SSH host key endpoint deprecation \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:16.255821+00:00
---

# Serial console SSH host key endpoint deprecation  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/deprecations/serial-console-ssh-host-key-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  Serial console SSH host key endpoint deprecation Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine provides the [interactive serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console) for troubleshooting malfunctioning instances. When you connect to the serial console using an SSH client, Compute Engine provides an SSH key so that you can authenticate the connection.

As of March 31, 2025, the serial console SSH key endpoint is deprecated and a new serial SSH key endpoint is available.

  * **Deprecated endpoint** : `https://www.gstatic.com/vm_serial_port/REGION/REGION.pub`
  * **New endpoint** : `https://www.gstatic.com/vm_serial_port_public_keys/REGION/REGION.pub`



To use the new endpoint, do one of the following, depending on how you connect to the serial console:

  * **Connect using the Google Cloud console** : no action is required. Connections from Google Cloud console don't use the endpoint.

  * **Connect using the Google Cloud CLI** : [update gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) to version 515.0.0 or later.

  * **Connect using third-party SSH clients** : use the new endpoint, as described in [Validate third-party SSH client connections](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console#host-keys).




You cannot use the deprecated endpoint after March 31, 2026.

## Shutdown schedule

The following table lists the shutdown schedule for the `https://www.gstatic.com/vm_serial_port/REGION/REGION.pub` server SSH key endpoint.

Date | Event  
---|---  
**March 31, 2025** | The `https://www.gstatic.com/vm_serial_port/REGION/REGION.pub` server SSH key endpoint was deprecated.  
**March 31, 2026** | The `https://www.gstatic.com/vm_serial_port/REGION/REGION.pub` server SSH key endpoint shutdown.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
