---
url: https://docs.cloud.google.com/compute/docs/networking/using-internal-dns/
title: Access VMs using internal DNS \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:25.282482+00:00
---

# Access VMs using internal DNS  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/networking/using-internal-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Access VMs using internal DNS Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

VMs in the same Virtual Private Cloud network can access each other by using internal DNS names instead of IP addresses.

## Before you begin

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




## Determine the internal DNS name for a VM

Use the following procedure to read the internal DNS name assigned to a VM instance. You can get the internal DNS name by querying the `hostname` metadata entry.

  1. [Connect to the VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).
  2. Query the `hostname` metadata:

###  Linux VMs
         
         curl "http://metadata.google.internal/computeMetadata/v1/instance/hostname" \
           -H "Metadata-Flavor: Google"
         

###  Windows VMs
         
         Invoke-RestMethod `
           -Headers @{"Metadata-Flavor" = "Google"} `
           -Uri "http://metadata.google.internal/computeMetadata/v1/instance/hostname"
         




The metadata server returns the VM's hostname in one of the following formats, which shows the type of internal DNS name that the VM uses:

  * **Zonal DNS** : `VM_NAME`.`ZONE`.`c`.`PROJECT_ID`.`internal`
  * **Global DNS** : `VM_NAME`.`c`.`PROJECT_ID`.`internal`



In the output:

  * `VM_NAME`: the name of the VM
  * `ZONE`: the zone where the VM is located
  * `PROJECT_ID`: the project to which the VM belongs



## Access VMs by internal DNS name

To access the VM, use the internal DNS name in place of the IP address.

The following example uses `ping` to contact a VM that uses [zonal DNS](https://docs.cloud.google.com/compute/docs/networking/zonal-dns). This method works, provided that you have created a [firewall rule](https://docs.cloud.google.com/vpc/docs/firewalls) that allows incoming ICMP traffic to the instance.
    
    
    $ ping VM_NAME.ZONE.c.PROJECT_ID.internal -c 1
    
    PING VM_NAME.ZONE.c.PROJECT_ID.internal (10.240.0.17) 56(84) bytes of data.
    64 bytes from VM_NAME.ZONE.c.PROJECT_ID.internal (10.240.0.17): icmp_seq=1 ttl=64 time=0.136 ms
    

Replace the following:

  * `VM_NAME`: the name of the VM
  * `ZONE`: the zone where the VM is located
  * `PROJECT_ID`: the project to which the VM belongs



## What's next

  * Migrate to [zonal DNS](https://docs.cloud.google.com/compute/docs/networking/zonal-dns)
  * Learn more about [internal DNS names for Compute Engine](https://docs.cloud.google.com/compute/docs/internal-dns).
  * [Configure static IP addresses for your VM](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
