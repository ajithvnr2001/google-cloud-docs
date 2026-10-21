---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/return-appliance/
title: Return the appliance \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:54.903483+00:00
---

# Return the appliance  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/return-appliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Guides ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide)



Send feedback 

#  Return the appliance Stay organized with collections  Save and categorize content based on your preferences. 

## Finalize copied data

Finalizing prepares the appliance for shipping to Google by removing the decryption key, rendering the data inaccessible until it reaches Google. When the decryption key is removed, you cannot copy additional data to the appliance without deleting all previously copied data.

To finalize the copied data, follow these steps:

  1. [Connect to the appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/receive-appliance#connecting).

  2. Run the `ta finalize` command. Enter the seal password when prompted and note the passcode returned in the output.
         
         ta finalize

The following sample response resembles the output that is returned:
         
         Finalizing prepares the appliance for shipping by removing the decryption
         key, making the data inaccessible until it reaches Google. Appliance local
         storage will be removed during this process. Once finalized, there is no way
         to access your data or add more data without deleting everything on the drive.
         
         **Are you ready to finalize the appliance and ship it back to Google? (y/n) y**
         
         Please enter the seal password to finalize the appliance:
         Unmounted data partition and disabled automount.
         Finalize step is complete.
         
         **This passcode must be used to get a return shipping label: NNNN**
         Enter the passcode returned by the 'ta finalize' command in the form
         included in the email titled Google Transfer Appliance Return Instructions
         sent by the Transfer Appliance Team.
         If you forget your passcode, run 'ta status' to display it again.
         

  3. Enter the passcode returned by the `ta finalize` command in the form included in the email titled _Google Transfer Appliance Return Instructions_ sent by the Transfer Appliance Team.

To view the passcode again, run `ta status`.

The Transfer Appliance Team responds with the shipping label for the Transfer Appliance for the given passcode.

**Note:** The passcode is specific to each appliance. If you have several Transfer Appliances, verify that the session ID printed on the shipping case.
  4. Once you receive the shipping label, turn off the appliance and disconnect all cables to it.




## Package and return the appliance

After transferring and finalizing your data to Transfer Appliance, prepare the appliance for shipping. This includes printing and applying a shipping label, gathering the appliance's cables, packing the appliance, and contacting your shipper to return the appliance.

Use the same shipping case that Transfer Appliance arrived in.

To return the appliance, do the following:

###  Rackable TA40 and TA300 

  1. Print the shipping label that was sent to you by Transfer Appliance Team as part of finalizing your copied data.

  2. Place the following in the shipping case's cable compartment:

Item | Description  
---|---  
![A photo depicting a NEMA 5-15P power cable](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/nema-5-15p-to-c13-power-cable.png) | NEMA 5-15p to C13 power cable (1.8 m / 5.91 ft)  
![A photo depicting a c14 to c13 power cable](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/c14-to-c13-power-cable.png) | C14 to C13 power cable, for connections to the power distribution unit (PDU) (1.5 m / 4.92 ft)  
![A photo depicting a Category 6 network cable](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/cat6-ethernet-cable.png) | Cat 6 network cable (2.1 m / 6.89 ft)  
![A photo depicting a QSFP28 twinaxial copper network cable](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/qsfp-plus-dac-twinax-cable.png) | **TA300 V2 and TA40 V2:** QSFP28 Twinax copper network cable  
![A photo depicting a QSFP28 to SFP28 adapter](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/qsfp28-to-sfp28-adapter.png) | **TA300 V2 and TA40 V2:** QSFP28 to SFP28 adapter  
![A photo depicting a SFP28 to SFP28 network cable](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/sfp28-to-sfp28-cable.png) | **TA300 V2 and TA40 V2:** SFP28 to SFP28 network cable  
![A photo depicting a USB-to-serial adapter cable](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/usb-to-serial-adapter-cable.png) | USB-to-serial adapter cable – use only if instructed by Transfer Appliance Team  
![A photo depicting a pin-to-socket serial adapter](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/pin-to-socket-serial-adapter.png) | Pin-to-socket serial adapter  
![A photo depicting a SFP28 to RJ45 transceiver](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/sfp28-to-rj45-transceiver.jpg) | **TA40 V2:** SFP28 to RJ45 Transceiver  
  3. Place the Transfer Appliance in the shipping case.

  4. Close the lid to the shipping case and secure the latches.

![Shipping case latched](https://docs.cloud.google.com/static/transfer-appliance/docs/images/shipping-container-latched.png)

  5. Secure the shipping case with a wire tamper-evident tag by following these steps:

     1. Insert the wire tamper-evident tag through the shipping case's D-rings.

![Inserting the wire tamper-evident tag through the
shipping case's D-rings](https://docs.cloud.google.com/static/transfer-appliance/docs/images/tamper-evident-tag-d-rings.png)

     2. Insert the end of the wire into the lock.

![Inserting the end of the wire into the lock](https://docs.cloud.google.com/static/transfer-appliance/docs/images/tamper-evident-tag-locked.png)

     3. Draw the tamper-evident tag through the tag lock, until the D-rings are secured.

![D-rings secured by tamper-evident tag](https://docs.cloud.google.com/static/transfer-appliance/docs/images/shipping-container-d-rings-secured.png)

  6. Affix a shipping-label pouch to the case using a tie-on tag.

  7. Insert the shipping return label in the pouch. Ensure that the return address and barcodes are visible.

  8. If necessary, contact your shipper to schedule a pick-up.




###  Freestanding TA40 and TA300 

  1. Print the shipping label that was sent to you by Transfer Appliance Team as part of finalizing your copied data.

  2. Place the following in the shipping case's cable compartment:

Item | Description  
---|---  
![A photo depicting a NEMA 5-15p to c13 power cable](https://docs.cloud.google.com/static/transfer-appliance/docs/images/nema-5-15p-to-c13-power-cable.png) | NEMA 5-15p to C13 power cable  
![A photo depicting a c14 to c13 power cable](https://docs.cloud.google.com/static/transfer-appliance/docs/images/c14-to-c13-power-cable.png) | C14 to C13 power cable, for connections to the power distribution unit (PDU)  
![A photo depicting a Category 6 network cable](https://docs.cloud.google.com/static/transfer-appliance/docs/images/cat6-ethernet-cable.png) | Category 6 (Cat6) network cable  
![A photo depicting a QSFP+ Twinax copper network cable](https://docs.cloud.google.com/static/transfer-appliance/docs/images/qsfp-plus-dac-twinax-cable.png) | QSFP+ Twinax copper network cable  
![A photo depicting a QSFP+ to 4xSFP+ network cable](https://docs.cloud.google.com/static/transfer-appliance/docs/images/qsfp-plus-to-4xsfp-plus.png) | QSFP+ to 4xSFP+ network cable  
![A photo depicting a USB-to-serial adapter cable](https://docs.cloud.google.com/static/transfer-appliance/docs/images/usb-to-serial-adapter-cable.png) | USB-to-serial adapter cable – use only if instructed by Transfer Appliance Team  
![A photo depicting a pin-to-socket serial adapter](https://docs.cloud.google.com/static/transfer-appliance/docs/images/pin-to-socket-serial-adapter.png) | Pin-to-socket serial adapter  
  3. Close the shipping case's lid and secure the latches.

  4. Secure the shipping case with a wire tamper-evident tag:

![Case secured by tamper-evident tags](https://docs.cloud.google.com/transfer-appliance/docs/images/ta-redesign-secured.png)

  5. Affix a shipping-label pouch to the case using a tie-on tag.

  6. Insert the shipping return label in the pouch. Ensure that the return address and barcodes are visible.

  7. If necessary, contact your shipper to schedule a pick-up.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
