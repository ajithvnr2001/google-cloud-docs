---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/erase-data/
title: Erase data \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:36.993729+00:00
---

# Erase data  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/erase-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Erase data Stay organized with collections  Save and categorize content based on your preferences. 

When you no longer need the device and you want to return it, erase the data from the device.

## Erase data from device

**Important:** To access the URLs on this page, you must connect to the internet. The URLs are provided for use when you have such access.

Erase any remaining data using the HPE One-button secure erase feature in the iLO interface. For more information on the secure erase procedure, see the [HPE documentation](https://support.hpe.com/hpesc/public/docDisplay?docId=a00026171en_us&page=GUID-8A7C60B7-A3A1-42C6-BEA5-0252F945B7C9.html#GUID-8A7C60B7-A3A1-42C6-BEA5-0252F945B7C9).

### Before you begin

Many of the prerequisites listed in the preceding HPE documentation are irrelevant to the GDC air-gapped appliance device, or managed by Google.

  * The Administrator account has all the privileges and must be used to initiate the secure erase process.
  * The device already has an advanced iLO License.
  * Server Configuration Lock, Smart Array Encryption, and Intel VROC Encryption are not used in the device at this time.
  * The device is not a c-Class and HPE Synergy system.
  * The storage drives used in the device are nVME drives supporting nVME FORMAT.
  * LDAP Directory Authentication with the HPE Extended Schema is not in use on the device.
  * If secure erase option is not available, update the iLO firmware using the following update firmware section.



### Update firmware

If the device's one secure erase button is not available, update the firmware to the latest version:

  1. Download the [GDC tar](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/iotool-setup#download-gdc-tar).

  2. Extract this downloaded tar:
         
         tar -I pigz -xvf gdch.tar.gz -C GDC_ROOT
         

Replace `GDC_ROOT` with the path to extract the tar.

  3. Download the firmware upgrade image:
         
         ./gdcloud artifacts extract GDCH_ROOT/release/oci/ /FILE_PATH --image-name gdch-hpe-firmware/ilo:ilo5
         

Replace `FILE_PATH` with the path to a newly created folder.

  4. Use the HPE support runbook at [https://support.hpe.com/hpesc/public/docDisplay?docId=a00026171en_us&docLocale=en_US&page=GUID-85EB0D20-5FBC-4DD6-BCCF-73CC9F78BE52.html](https://support.hpe.com/hpesc/public/docDisplay?docId=a00026171en_us&docLocale=en_US&page=GUID-85EB0D20-5FBC-4DD6-BCCF-73CC9F78BE52.html) to update the firmware.




### Reset switch post secure erase

There are two ways to reset the switch:

  1. Use the physical button on the switch to reset the switch.
  2. Follow this [Switch Serial Console Access Runbook](https://cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/appl/guides/appl-g0002).
         
         switch-86fe3e [standalone: master] > en
         switch-86fe3e [standalone: master] # conf t
         switch-86fe3e [standalone: master] (config) # reset factory
         Warning - confirming will cause system reboot.
         Type 'YES' to confirm reset: YES
         Resetting and rebooting the system -- please wait...
         HPE Management Console
         




### Disconnect storage devices which shouldn't be erased

If any additional drives are connected, you must erase them if they remain connected. These drives may or may not support a built-in sanitization method. Therefore, their state after the secure erase procedure cannot be guaranteed.

### Optionally configure SNMP, AlertMail, or iLO RESTful API alerts

If an error occurs during the secure erase process, an IML entry is logged. Alerts send a notification, allowing for faster recovery.

### Begin the secure erase process

  1. In the iLO interface, click **Lifecycle Management** and then the **Decommission** tab.
  2. Click **Erase System** and confirm.



## Gather logs

Gather the logs produced during the secure erase procedure, and bring the system back to a usable state.

### Regain access to the iLO interface

If the Administrator account is unchanged, you can use the account to access the iLO interface, and the logs from the last secure erase can be acquired. Otherwise, the logs are lost when the iLO password is reset.

Because account rotation is used in most cases, the iLO must be reset. Reset the iLO by using the iLO 5 Configuration Utility, as described at [https://support.hpe.com/hpesc/public/docDisplay?docLocale=en_US&docId=a00026113en_us](https://support.hpe.com/hpesc/public/docDisplay?docLocale=en_US&docId=a00026113en_us).

If the BIOS password has changed, the entire system can be factory reset using the System Maintenance Switch, as described at <https://techlibrary.hpe.com/docs/iss/DL380_Gen10/setup_install/GUID-561C370B-8FA9-468E-9B0A-BDEE7F82927E.html>.

### View the report

If the iLO logs are still accessible from when the device was erased, or if you ran the secure erase procedure again after iLO access was regained, view the logs in the iLO interface as follows:

Go to **Lifecycle Management > Decommission > View Last Erase Report**.

### Save the report

  1. Go to **Lifecycle Management > Decommission** and click the document icon with the **CSV** label.
  2. Click **Save** and follow the browser prompts to save the secure erase report. Save the secure erase report as a record in a tracking system to show that it was completed. 



### Delete the secure erase report

  1. Go to **Lifecycle Management > Decommission > View Last Erase Report**.
  2. Click the trash can icon.



The event log, IML, security log, and configuration settings made up to this point are reset to the factory default settings. iLO might attempt an auto-restore operation when it starts.

## Destroy YubiKeys

To wipe the data from the device, follow these steps:

  1. Remove the YubiKeys from the device.
  2. Destroy the YubiKeys by following your company's process to sanitize or destroy physical media.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
