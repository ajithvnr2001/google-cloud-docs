---
url: https://docs.cloud.google.com/migrate/containers/docs/mcdc-vmware-batch-collection-tutorial/
title: Batching guest discovery and data collection \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:30.801221+00:00
---

# Batching guest discovery and data collection  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/mcdc-vmware-batch-collection-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback 

#  Batching guest discovery and data collection Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial walks you through the process of discovering and collecting data on a batch of VMware virtual machine (VM) instances using the Migration Center discovery client CLI guest discovery. Large batches of VMs may be difficult to monitor and troubleshoot. We recommend batching into smaller groups of less than 1,000.

## Objectives

In this tutorial, you will learn how to:

  * Download the `mcdc` CLI.
  * Run a VMWare inventory discovery.
  * Generate a CSV file with all the discovered VMs.
  * Split the CSV file into multiple CSV files containing a subset of the VMs.
  * Run guest discovery on all the VMs in a CSV file.
  * Generate an offline assessment report. 



## Costs

This tutorial uses on-premises resources and incurs no Google Cloud costs.

## Before you begin

  1. Prepare a Linux machine to install and run the `mcdc` CLI. The Linux machine must have the following minimum requirements:

     * `glibc` version 2.25 or later
     * 4 GB RAM and 10 GB disk space
     * Network connectivity to vCenter and ESX hosts
  2. Ensure that you have a vSphere user with the necessary permissions:

     * Read privileges to VMs
     * Read privileges to all the ESX hosts
     * Guest operation modifications
     * Guest operation program execution
     * Guest operation queries



## Download the `mcdc` CLI

  1. Connect to the Linux machine: 
         
         ssh MACHINE_IP

Replace MACHINE_IP with the IP address of your Linux machine.

  2. Download the latest version of the `mcdc` CLI and make it executable: 
         
         curl -O "https://mc-release.storage.googleapis.com/mcdc/$(curl -s https://mc-release.storage.googleapis.com/mcdc/latest)/mcdc"
           chmod +x mcdc

  3. Add the `mcdc` CLI to your shell path: 
         
         PATH=$PATH:`pwd`




## Perform a VMware inventory discovery

  * Run the inventory discovery:
        
        ./mcdc discover vsphere -u USERNAME --url https://VSPHERE_URL
        

Replace the following:

    * USERNAME: your vCenter username
    * VSPHERE_URL: the URL for your vCenter Server instance or the vSphere Client

The output of the `discover` command looks like the following:
    
    [+] Found 528 VMs
    Collecting data...
    528 / 528 [---------------------------------------------------] 100.00% 5 p/s
    [✓] Collection completed.
    




## Generate a CSV file with all the discovered VMs

To generate a CSV file, use the `export` script from the Migrate to Containers repository on GitHub.
    
    
    vms=$(mcdc report --format csv | tail -n +2 | awk -F ',' '{; print $2";"$3";"$4";;;"}')
    printf "%s\n" "Name;Platform VM ID;OS Family;IP;USERNAME;PASSWORD"
    printf "%s\n" "$vms"
    

The script uses the `report` command to generate a CSV file containing all the VMs that were discovered in the previous step.

  1. Download the script:
         
         curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/migrate-to-containers/main/scripts/mcdc/mcdc_discovery_export_guest_tools.sh
         chmod +x mcdc_discovery_export_guest_tools.sh
         

  2. Run the script and save the output to a file:
         
         ./mcdc_discovery_export_guest_tools.sh > VMS_CSV_FILE
         

Replace VMS_CSV_FILE with the name you want for the CSV file.




## Split the CSV file into multiple CSV files with a subset of the VMs

To split the large CSV file into smaller CSV files, use the `splitter` script from the Migrate to Containers repository on GitHub.
    
    
    tail -n +2 $1 | split -d -l $num_of_lines - $2
    for file in $2*
    do
        head -n 1 $1 > tmp_file
        cat "$file" >> tmp_file
        mv -f tmp_file "$file"
    done

  1. Download the script:
         
         curl -O https://raw.githubusercontent.com/GoogleCloudPlatform/migrate-to-containers/main/scripts/mcdc/csv_splitter.sh
         chmod +x csv_splitter.sh
         

  2. Run the script:
         
         ./csv_splitter.sh VMS_CSV_FILE CSV_FILES_PREFIX LINES_PER_FILE VMS_CSV_FILE CSV_FILES_PREFIX
         

Replace the following:

     * VMS_CSV_FILE: the input CSV file to split.
     * CSV_FILES_PREFIX: the prefix for the generated CSV files.
     * LINES_PER_FILE: the number of lines per generated CSV file. The default value is `10`.

The script generates various CSV files.

  3. View the list of generated CSV files:
         
         ls -lrt CSV_FILES_PREFIX*
         




## Run guest discovery on all the VMs in a CSV files

To run the guest discovery for the VMs in a CSV file, use the `collection` script from the Migrate to Containers GitHub repository.

Repeat this step for each CSV file generated in the previous step.
    
    
    url_regex='^https?://[-A-Za-z0-9\+&@#/%?=~_|!:,.;]*[-A-Za-z0-9\+&@#/%=~_|]\.[-A-Za-z0-9\+&@#/%?=~_|!:,.;]*[-A-Za-z0-9\+&@#/%=~_|]$'
    
    read -r -p "CSV file name: " CSV_FILE
    if [[ ! -r "$CSV_FILE" ]]; then
        echo "The file $CSV_FILE does not exist or can not be accessed."
        exit 1
    fi
    
    read -r -p "vSphere URL: " VSPHERE_URL
    if ! [[ $VSPHERE_URL =~ $url_regex ]]; then
        echo "vSphere URL $VSPHERE_URL IS not a valid URL"
        exit 1
    fi
    read -r -p "vSphere username: " VSPHERE_USER
    read -r -s -p "vSphere password: " VSPHERE_PASSWORD
    echo ""
    read -r -p "Default username: " DEFAULT_USER
    read -r -s -p "Default password: " DEFAULT_PASSWORD
    
    echo ""
    
    # CSV fields
    #NAME;PLATFORM VM ID;OS;IP;USERNAME;PASSWORD
    while IFS=";" read -r vm_name vm_id os ip username password
    do
       if [ -z "$username" ]
        then
          username=$DEFAULT_USER
        fi
        if [ -z "$password" ]
        then
              password=$DEFAULT_PASSWORD
        fi
    
        if [ ! -z "$vm_id" ]
        then
          # Note that the below only works for VMWare VMs
          # vm_id after the last slash if prefixed by vSphere IP
          mod_vm_id=$(echo "$vm_id" | sed 's/.*\///')
          mcdc discover vsphere guest --url $VSPHERE_URL -u $VSPHERE_USER -p $VSPHERE_PASSWORD --vm-user $username --vm-password $password $mod_vm_id
        else
          echo "Skipping VM: $vm_name because it has no VM ID"
        fi
     done < <(tail -n +1 $CSV_FILE)
    

The script uses the `discover vsphere guest` command to upload and execute the guest collection script on the VM.

It's best to execute this script in the background and direct the output to a log file. To do so, you need to create a text file which is passed as input to the script.

  1. Create the text file:
         
         cat <<EOF >> INPUT_FILE
         CSV_FILES_PREFIXCSV_FILE_SUFFIX
         VSPHERE_URL
         VSPHERE_USER
         VSPHERE_PASSWORD
         VM_USER
         VM_PASSWORD
         EOF
         

Replace the following:

     * INPUT_FILE: input filename
     * CSV_FILES_PREFIX: CSV filename prefix
     * CSV_FILE_SUFFIX: CSV filename suffix
     * VSPHERE_URL: the URL for your vCenter Server instance or the vSphere Client
     * VSPHERE_USER: vCenter username
     * VSPHERE_PASSWORD: vCenter password
     * VM_USER: VM username
     * VM_PASSWORD: VM password
  2. Run the guest collection script:
         
         nohup ./mcdc_collect_vms_guest_tools.sh <INPUT_FILE > /tmp/mcdc.out 2>&1 &
         

  3. Repeat steps 1 and 2 for each CSV file generated in the previous step.




## Generate an offline assessment report

  * After all the data is collected, you can produce a detailed HTML report:
        
        ./mcdc report --format html --full > REPORT_NAME.html
         




## What's next

  * Learn how to [collect guest data from EC2 instances](https://docs.cloud.google.com/migrate/containers/docs/mcdc-aws-collection-tutorial).
  * Learn more about the [`mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/discovery-client-cli-overview).
  * Look [through scripts samples](https://github.com/GoogleCloudPlatform/migrate-to-containers/tree/main/scripts/mcdc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
