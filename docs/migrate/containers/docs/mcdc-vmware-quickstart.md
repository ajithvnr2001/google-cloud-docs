---
url: https://docs.cloud.google.com/migrate/containers/docs/mcdc-vmware-quickstart/
title: Discover, collect, and assess VMware VMs for migration \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:34.433208+00:00
---

# Discover, collect, and assess VMware VMs for migration  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/mcdc-vmware-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Discover, collect, and assess VMware VMs for migration

Learn how to download the Migration Center discovery client CLI and use it to remotely discover, collect, and assess virtual machine (VM) instances running on VMware for migration and containerization.

**Note:** The `mcdc` CLI can discover, collect, and assess up to 10,000 VMs in a single deployment.

You can generate offline assessment reports in a user-friendly HTML format. These reports display the results for each of the migration targets and outlines actions to take to eliminate blockers and risks.

## Before you begin

  1. Provision a Linux machine to download and run the `mcdc` CLI. The Linux machine must have the following minimum requirements:

     * `glibc` version 2.25 or later
     * 4 GB RAM and 10 GB disk space
     * Network connectivity to vCenter and ESX hosts
  2. Ensure that you have a vSphere user with the following permissions:

     * Read privileges to VMs
     * Read privileges to all the ESX hosts
     * Guest operation modifications
     * Guest operation program execution
     * Guest operation queries
  3. Ensure that you have a user with administrator or root rights to all the target guest VMs.




## Download `mcdc` CLI

  1. Connect to the Linux machine:
         
         ssh MACHINE_IP
         

Replace MACHINE_IP with the IP address of your Linux machine.

  2. Download the latest version of the `mcdc` CLI and make it executable:
         
         curl -O "https://mc-release.storage.googleapis.com/mcdc/$(curl -s https://mc-release.storage.googleapis.com/mcdc/latest)/mcdc"
         chmod +x mcdc
         




## Perform VMware inventory discovery

  * Run the inventory discovery:
        
        ./mcdc discover vsphere -u USERNAME --url https://VSPHERE_URL
        

Replace the following:

    * USERNAME: your vCenter username
    * VSPHERE_URL: the URL for your vCenter Server instance or the vSphere Client

The output of the `discover` command looks like the following:
    
    [+] Found 13 VMs
    Collecting data...
    13 / 13 [---------------------------------------------------] 100.00% 5 p/s
    [✓] Collection completed.
    




## Perform guest discovery on all discovered VMs

  * Run the guest discovery:
        
        ./mcdc discover vsphere guest all --url https://VSPHERE_URL \
          -u VCENTER_USER --vm-user VM_USER
        

Replace the following:

    * VCENTER_USER: the vCenter server user
    * VM_USER: the VM user

When prompted, enter the password for the VCENTER_USER and VM_USER.




## Generate reports to visualize the assessment

  * Generate a summary report:
        
        ./mcdc report --format html > Summary_Report.html
        

  * Generate a detailed report:
        
        ./mcdc report --format html --full > Detailed_Report.html
        

HTML files named `Summary_Report.html` and `Detailed_Report.html` are created. Open the reports in a browser.




## Clean up

There are no charges associated with running the `mcdc` CLI. However, you can delete the collected data from the local database.

  * Delete the `mcdc` CLI data:
        
        ./mcdc discover purge-db -db DATABASE_NAME
        

Replace DATABASE_NAME with the path to the database where the collected data is stored. Typically, it is in the same directory where you downloaded the `mcdc` CLI.




## What's next

  * Learn how to [migrate a Linux VM](https://docs.cloud.google.com/migrate/containers/docs/migrate-vm).
  * Learn more about the [`mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/discovery-client-cli-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
