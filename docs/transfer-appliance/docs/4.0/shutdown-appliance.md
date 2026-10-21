---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/shutdown-appliance/
title: Shut down the appliance \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:18.783033+00:00
---

# Shut down the appliance  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/shutdown-appliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Guides ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide)



Send feedback 

#  Shut down the appliance Stay organized with collections  Save and categorize content based on your preferences. 

You can shut down the appliance to relocate it, or if planned power or facility work will affect the appliance. To ensure that your data is safe, you must power down the appliance before disconnecting power.

## Appliance power controls

The location and type of power controls depend on the appliance model you received:

  * **Rackable (TA300 V2 and TA40 V2)** : Use the button module on the front panel.

![Front panel button module on TA300 V2](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/ta300-button-module.png)

    * **Power On** : Press the **Green Check** button (7).
    * **Power Off** : Long press the **Arrows** (Up/Down) (5).
  * **Freestanding TA40 and TA300** : Open the case lid and press the power button on the top panel.




## Power down

To power down the appliance, run the `shutdown` command from the appliance command line:
    
    
    sudo shutdown now
    

To restart the appliance after powering down, use the power controls described in Appliance power controls.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
