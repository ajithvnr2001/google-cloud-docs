---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/online-transfer/
title: Enable or disable online transfer \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:17.018324+00:00
---

# Enable or disable online transfer  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/online-transfer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Guides ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide)



Send feedback 

#  Enable or disable online transfer Stay organized with collections  Save and categorize content based on your preferences. 

The Transfer Appliance has two modes:

  * **Offline transfer** : Data is copied to the appliance until it is full. The appliance is shipped back to Google and the copied data is moved to your Cloud Storage bucket.

  * **Online transfer** : Data copied to the appliance is streamed to your Cloud Storage bucket. After the data is uploaded to your Cloud Storage bucket, it is removed from the appliance. Online transfer compresses and encrypts the data in transit and accelerates data transfer compared to the gcloud CLI and other command-line tools.




You can toggle between offline and online mode.

## Download Appliance Service Account Key

Once the [project setup](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide#project-setup-and-key-download) is completed, prepare a service account key:

  1. [Create a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#iam-service-account-keys-create-console) for the appliance service account. This is a one time download key.

  2. Rename the key to `key.json`, and save it to a safe location.

  3. Once you've received your appliance, upload `key.json` to the `/tmp` directory on the appliance.




## Set to online mode

Before enabling online transfer mode for the first time, follow the instructions to complete [project setup](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide#project-setup-and-key-download).

Outbound connectivity is required in order to enable and use online mode. To enable online transfer mode, follow the instructions below:

  1. Verify your outbound connectivity from the appliance to the HTTPS endpoints listed below:

     * https://gcr.io

     * https://storage.googleapis.com

     * https://oauth2.googleapis.com

     * https://storagetransfer.googleapis.com

     * https://pubsub.googleapis.com

Run the following command using each of the HTTPS endpoints:
    
    ping URL
    

If the command fails, it may indicate that DNS is misconfigured on the appliance. If the appliance was configured to use a static IP address, update it to use DHCP:
    
    ta config --data_port=PORT --ip=dhcp
    

Replace `PORT` with the data port you are using on the appliance, either `RJ45` or `QSFP`.

  2. Copy the service key downloaded in Download Appliance Service Account Key to the appliance's `tmp` folder, by doing the following:

### Windows

     1. Using the SCP tool, connect to the appliance using the following settings:

        * **File protocol** : SFTP
        * **Host name** : The IP address for the appliance.
        * **Port number** : 22
        * **Username** : The appliance username provided by the Transfer Appliance Team.
        * **Password** : The appliance password provided by the Transfer Appliance Team.
     2. Copy the file to the `/tmp` folder

### Linux

     1. Run the following command:
            
            scp PATH_TO_KEY_FILE/key.json USERNAME@IP_ADDRESS:/tmp
            

Replace the following:

        * `PATH_TO_KEY_FILE`: The path to the key file that you are copying.
        * `USERNAME`: The appliance username provided by the Transfer Appliance Team.
        * `IP_ADDRESS`: The IP address for the appliance.
     2. When prompted, enter the appliance password provided by the Transfer Appliance Team.

### Apple macOS

     1. Run the following command:
            
            scp PATH_TO_KEY_FILE/key.json USERNAME@IP_ADDRESS:/tmp
            

Replace the following:

        * `PATH_TO_KEY_FILE`: The path to the key file that you are copying.
        * `USERNAME`: The appliance username provided by the Transfer Appliance Team.
        * `IP_ADDRESS`: The IP address for the appliance.
     2. When prompted, enter the appliance password provided by the Transfer Appliance Team.

  3. To set the appliance to online mode, run the following command:
         
         ta online
         

The following sample response resembles the output that is returned:
         
         **Starting containers for online transfer...**
         Copied new credentials.          ## Or, Using old credentials
         Running binary to enable online transfer.
         This may take several minutes to finish...
         
         **Containers have been successfully started. You can transfer data in
         online mode.**
         

  4. **Optional:** change the transfer destination bucket and the job object prefix.
         
         ta online --bucket=BUCKET --object_prefix=OBJECT_PREFIX
         

Replace `BUCKET` with the destination bucket and `OBJECT_PREFIX` with the object prefix you are updating to.

If the command is successful, it returns output resembling the output from the step where you run the online transfer without these two arguments.

**Note:** You can update the destination bucket and the object prefix independently. If updating to a new destination bucket, ensure that the required service accounts are [set up for the new bucket](https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-permissions). Additionally, each invocation of this command with at least one of the the two flags triggers a new transfer operation, regardless of whether the appliance is offline or online.




To troubleshoot online mode, see [Troubleshooting online mode](https://docs.cloud.google.com/transfer-appliance/docs/4.0/troubleshoot-online-mode).

## Set to offline mode

To specify offline mode, run the following command:
    
    
    ta offline
    

The following sample response resembles the output that is returned:
    
    
    Putting the appliance in offline mode...
    **Appliance is successfully put into the offline mode.**
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
