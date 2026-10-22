---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/verify-confidential-computing-enabled/
title: Verify Confidential Computing is enabled \u00a0|\u00a0 Confidential VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:13.266476+00:00
---

# Verify Confidential Computing is enabled  |  Confidential VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/verify-confidential-computing-enabled/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)



Send feedback 

#  Verify Confidential Computing is enabled Stay organized with collections  Save and categorize content based on your preferences. 

There are multiple ways to verify that Confidential Computing is enabled for a VM instance.

### gcloud

Run the following command to determine which Confidential Computing technology your Confidential VM is using:
    
    
    gcloud compute instances describe INSTANCE_NAME \
        --zone=ZONE_NAME \
        --format="yaml(confidentialInstanceConfig)"
    

Provide the following values:

  * `INSTANCE_NAME`: The Confidential VM instance name.

  * `ZONE_NAME`: The zone the Confidential VM instance is operating in.




You receive one of the following responses if your VM instance is using AMD SEV:
    
    
    confidentialInstanceConfig:
      enableConfidentialCompute: true
    
    
    
    confidentialInstanceConfig:
      confidentialInstanceType: SEV
    

You receive one of the following responses if your VM instance is using AMD SEV-SNP or Intel TDX:
    
    
    confidentialInstanceConfig:
      confidentialInstanceType: SEV_SNP
    
    
    
    confidentialInstanceConfig:
      confidentialInstanceType: TDX
    

### dmesg

To determine which Confidential Computing technology your Confidential VM is using, you might be able to use the `dmesg` logs on your VM.

**Note:** Depending on the Linux distribution and other software installed on the guest, `dmesg` logs might be maintained differently. For definitive guidance about how to query `dmesg` logs, refer to your Linux distribution's documentation.

To check if your `dmesg` logs contain Confidential Computing information, use SSH to connect to your VM and run `dmesg`:

  1. In the Google Cloud console, go to the **VM Instances** page.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  2. In the table on the **Instances** tab, find the row for your Confidential VM instance.

  3. To open a terminal window for interacting with your Confidential VM instance, click **SSH** in the same row.

  4. Run the following command:
         
         sudo dmesg | grep -i "Encryption Features active"
         




If your VM is using AMD SEV, the response should be similar to the following example:
    
    
    Memory Encryption Features active: SEV
    

If your VM is using AMD SEV-SNP, the response should be similar to the following example:
    
    
    Memory Encryption Features active: SEV SEV-ES SEV-SNP
    

If your VM is using Intel TDX, the response should be similar to the following example:
    
    
    Memory Encryption Features active: Intel TDX
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
