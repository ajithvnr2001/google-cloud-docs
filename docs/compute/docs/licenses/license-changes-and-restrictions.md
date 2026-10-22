---
url: https://docs.cloud.google.com/compute/docs/licenses/license-changes-and-restrictions/
title: License changes and restrictions \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:13.317873+00:00
---

# License changes and restrictions  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/licenses/license-changes-and-restrictions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  License changes and restrictions Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Only certain OS licenses are eligible to be appended, removed, or replaced. License changes are supported for Red Hat Enterprise Linux (RHEL), RHEL for SAP, SUSE Linux Enterprise Server (SLES), SLES for SAP, Ubuntu, Ubuntu Pro, and Windows Server for the following use cases:

  * Changing between BYOS and PAYG billing models for RHEL, RHEL for SAP, SLES, and SLES for SAP
  * Changing a Windows Server BYOL instance to use PAYG billing
  * In-place upgrades from Ubuntu to Ubuntu Pro
  * Adding or removing RHEL ELS add-on licenses



The license owner can change valid license changes for a given license. Before you change a license, confirm that the target license change is valid. This guide outlines how to find the current valid license changes for a particular license. It also outlines any restrictions that apply to changing that license.

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




## Prepare to update a disk's license

**Caution** : Google recommends using reservations to ensure machine availability while the VM is shut down.

To update the disk's license while the disk is attached to a running instance, first either stop the instance or detach the disk.

  * [Stop the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm). Temporarily shuts down the instance before updating the disk's license.
  * [Detach the disk](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#detach_disk). This detaches the disk from the instance before updating the disk's license.



## Review license information

In Cloud Shell, run the following command. Replace LICENSE_URL with the license that you want to investigate. For a list of common license URLs, see the License references table.
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" LICENSE_URL

For example, to examine the RHEL 7 PAYG License:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-7-server

The output is similar to the following:
    
    
    {
      "kind": "compute#license",
      "name": "rhel-7-server",
      "chargesUseFee": true,
      "id": "6080198135500386054",
      "licenseCode": "1000006",
      "creationTimestamp": "2013-08-19T17:17:57.000-07:00",
      "description": "RedHat Enterprise Linux 7",
      "transferable": true,
      "selfLink": "https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-7-server",
      "selfLinkWithId": "https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/6080198135500386054",
      "appendableToDisk": true,
      "removableFromDisk": false,
      "allowedReplacementLicenses": [
        "1492188837615955530",
        "8475125252192923229",
        "601259152637613565",
        "489291035512960571",
        "1270685562947480748"
      ],
      "osLicense": false,
      "soleTenantOnly": false,
      "multiTenantOnly": false,
      "minimumRetention": {
        "seconds": "0",
        "nanos": 0
      },
      "updateTimestamp": ""
    }
    

The response outlines the following key fields:

  * **`removableFromDisk`** : if `true`, the license can be removed from the disk. If `false`, the license cannot be removed without replacing it with a valid license.
  * **`allowedReplacementLicenses`** : this is a list of license codes for licenses that can serve as valid replacements. To find out which license code corresponds to which license, see License references.
  * **`minimumRetention`** : the minimum amount of time that the license needs to be present on the VM before another license change can be applied.



## Example: Replace RHEL 7 PAYG with RHEL 8 PAYG

To replace a RHEL 7 PAYG license with a RHEL 8 PAYG license, use the following information to find the license code and license URL for RHEL 8 PAYG:

License Name | License Code | License URL  
---|---|---  
RHEL 8 PAYG | 601259152637613565 | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-8-server`  
  
Since the license code for RHEL 8 PAYG (601259152637613565) was listed under `allowedReplacementLicenses` for RHEL 7 PAYG, this indicates that a valid license replacement is possible.

To perform the license replacement, use the following command:
    
    
      gcloud compute disks update DISK_NAME
          --replace-license=projects/rhel-cloud/global/licenses/rhel-7-server,projects/rhel-cloud/global/licenses/rhel-8-server
          --zone=DISK_ZONE
    

## License references

License references for RHEL, SLES, Ubuntu, Ubuntu Pro, and Windows Server are listed in the following tables.

### RHEL license information

License Name | License Code | License URL  
---|---|---  
RHEL 6 PAYG | 1000002 | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-6-server`  
RHEL 7 PAYG | 1000006 | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-7-server`  
RHEL 7 ELS | 4646774207868449156 | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-7-els`  
RHEL 8 PAYG | 601259152637613565 | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-8-server`  
RHEL 9 PAYG | 7883559014960410759 | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-9-server`  
RHEL 10 PAYG | 1368031684811063353 | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-10-server`  
RHEL 6 BYOS | 4720191914037931587 | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-6-byos`  
RHEL 7 BYOS | 1492188837615955530 | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-7-byos`  
RHEL 8 BYOS | 8475125252192923229 | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-8-byos`  
RHEL 9 BYOS | 3837518230911135854 | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-9-byos`  
RHEL 10 BYOS | 4907394077439590422 | `https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-10-byos`  
RHEL 8 for SAP PAYG | 1270685562947480748 | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-8-sap`  
RHEL 9 for SAP PAYG | 8291906032809750558 | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-9-sap`  
RHEL 10 for SAP PAYG | 5231023367886504429 | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-10-sap`  
RHEL 8 for SAP BYOS | 489291035512960571 | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-8-sap-byos`  
RHEL 9 for SAP BYOS | 6753525580035552782 | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-9-sap-byos`  
RHEL 10 for SAP BYOS | 4412948736425361424 | `https://www.googleapis.com/compute/v1/projects/rhel-sap-cloud/global/licenses/rhel-10-sap-byos`  
  
### SLES license information

License Name | License Code | License URL  
---|---|---  
SLES 11 PAYG | 1000004 | `https://www.googleapis.com/compute/v1/projects/suse-cloud/global/licenses/sles-11`  
SLES 12 PAYG | 1000008 | `https://www.googleapis.com/compute/v1/projects/suse-cloud/global/licenses/sles-12`  
SLES 15 PAYG | 5422776498422280384 | `https://www.googleapis.com/compute/v1/projects/suse-cloud/global/licenses/sles-15`  
SLES 11 BYOS | 3562683225507985416 | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-11-byos`  
SLES 12 BYOS | 5995918435054614609 | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-12-byos`  
SLES 15 BYOS | 7429287564402499183 | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-15-byos`  
SLES 12 for SAP PAYG | 4079932016749305610 | `https://www.googleapis.com/compute/v1/projects/suse-sap-cloud/global/licenses/sles-sap-12`  
SLES 15 for SAP PAYG | 4764125400812555962 | `https://www.googleapis.com/compute/v1/projects/suse-sap-cloud/global/licenses/sles-sap-15`  
SLES 12 for SAP BYOS | 7194268483061119118 | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-sap-12-byos`  
SLES 15 for SAP BYOS | 6035015651111738499 | `https://www.googleapis.com/compute/v1/projects/suse-byos-cloud/global/licenses/sles-sap-15-byos`  
  
### Ubuntu and Ubuntu Pro license information

License Name | License Code | License URL  
---|---|---  
Ubuntu 16.04 (Xenial Xerus) | 1000201 | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-1604-xenial`  
Ubuntu Pro 16.04 (Xenial Xerus) | 8045211386737108299 | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-1604-lts`  
Ubuntu 18.04 LTS (Bionic Beaver) | 5926592092274602096 | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-1804-lts`  
Ubuntu Pro 18.04 LTS (Bionic Beaver) | 6022427724719891830 | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-1804-lts`  
Ubuntu 20.04 LTS (Focal Fossa) | 2211838267635035815 | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2004-lts`  
Ubuntu Pro 20.04 LTS (Focal Fossa) | 599959289349842382 | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2004-lts`  
Ubuntu 22.04 LTS (Jammy Jellyfish) | 5511465778777431107 | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2204-lts`  
Ubuntu Pro 22.04 LTS (Jammy Jellyfish) | 2592866803419978320 | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2204-lts`  
Ubuntu 24.04 LTS (Noble Numbat) | 3242930272766215801 | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2404-lts`  
Ubuntu Pro 24.04 LTS (Noble Numbat) | 2176054482269786025 | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2404-lts`  
  
### Windows Server license information

License Name | License Code | License URL  
---|---|---  
Windows Server 2008 R2 BYOL | 4551215591257167608 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2008-r2-byol`  
Windows Server 2008 R2 PAYG | 1000000 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2008-r2-dc`  
Windows Server 2012 BYOL | 5559842820536817947 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2012-byol`  
Windows Server 2012 PAYG | 1000015 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2012-dc`  
Windows Server 2012 R2 BYOL | 6738952703547430631 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2012-r2-byol`  
Windows Server 2012 R2 PAYG | 1000017 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2012-r2-dc`  
Windows Server 2016 BYOL | 4322823184804632846 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2016-byol`  
Windows Server 2016 PAYG | 1000213 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2016-dc`  
Windows Server 2019 BYOL | 6532438499690676691 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2019-byol`  
Windows Server 2019 PAYG | 3389558045860892917 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2019-dc`  
Windows Server 2022 BYOL | 2808834792899686364 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2022-byol`  
Windows Server 2022 PAYG | 4079807029871201927 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2022-dc`  
Windows Server 2025 BYOL | 6621875542391421291 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2025-byol`  
Windows Server 2025 PAYG | 7142647615590922601 | `https://www.googleapis.com/compute/v1/projects/windows-cloud/global/licenses/windows-server-2025-dc`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
