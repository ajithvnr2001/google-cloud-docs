---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-compute/
title: gdcloud compute \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:22.035474+00:00
---

# gdcloud compute  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud compute Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud compute - Read and manipulate GDC air-gapped compute resources.

## SYNOPSIS
    
    
    gdcloud compute GROUP | COMMAND [flags]
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--help`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

### GROUPS

`GROUP` is one of the following:
    
    
    backend-services
        Read and manipulate backend services for load balancers.
    backends
        Read and manipulate the backends. A backend is a zonal object that identifies endpoints for a load balancer.
    disks
        Read and manipulate GDC air-gapped virtual machine disks.
    forwarding-rules
        Read and manipulate traffic forwarding rules for load balancers.
    health-checks
        Probe to attach to a backend service to check the health status of an individual endpoint.
    images
        Read GDC air-gapped virtual machine images.
    instances
        Read and manipulate GDC air-gapped virtual machine instances.
    machine-types
        Read GDC air-gapped virtual machine types.
    

### COMMANDS

`COMMAND` is one of the following:
    
    
    connect-to-serial-port
        Connect to the serial port of a GDC air-gapped virtual machine.
    ssh
        SSH to a GDC air-gapped virtual machine.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
