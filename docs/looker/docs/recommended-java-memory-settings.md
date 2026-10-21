---
url: https://docs.cloud.google.com/looker/docs/recommended-java-memory-settings/
title: Recommended Java memory settings \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:54:03.936481+00:00
---

# Recommended Java memory settings  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/recommended-java-memory-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Recommended Java memory settings Stay organized with collections  Save and categorize content based on your preferences. 

The memory allocated to the Looker application on customer-hosted instances is specified in the Looker startup script.

You can download the latest startup script, `looker`, at the [looker-open-source GitHub repo](https://github.com/looker-open-source/customer-scripts/tree/master/startup_scripts). When you download the startup script, move it into the same directory as the `looker.jar` file (generally `/home/looker/looker`). For more information, see the [Installing the Looker application](https://docs.cloud.google.com/looker/docs/installing-looker-application#install_the_looker_application) documentation page.

The startup script automatically determines how much java memory to allocate to Looker. However, if you would like to customize this value manually, you can follow these instructions.

## Changing Looker's memory allocation

To change the memory allocated to Looker, edit these lines for Java heap and metaspace memory allocation in the startup script:
    
    
    JAVAMEM="2300m"
    METAMEM="800m"
    

Then, restart the application:
    
    
    ./looker restart
    

For smaller instances dedicated to Looker, the memory allocated should be approximately two thirds of the available memory. On larger instances this ratio can be increased.

If too much memory is allocated:

  * Looker may fail to start
  * The system generally may suffer performance issues



If too little memory is allocated:

  * Looker may fail to start
  * Looker specifically may suffer performance issues



## Common instance types

The following table lists the recommended memory settings for a number of common instance sizes:

Instance Specs | Total System Memory | Recommended JAVAMEM | Recommended METAMEM  
---|---|---|---  
2 vCPU / 8 Mem (GiB)  |  7500m  |  3600m  |  800m   
4 vCPU / 16 Mem (GiB)  |  15000m  |  9000m  |  1000m   
8 vCPU / 32 Mem (GiB)  |  30000m  |  20000m  |  1000m   
16 vCPU / 64 Mem (GiB)  |  60000m  |  46000m  |  1000m   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
