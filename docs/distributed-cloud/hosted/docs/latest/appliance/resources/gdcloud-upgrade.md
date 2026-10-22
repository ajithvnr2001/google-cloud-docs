---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-upgrade/
title: Upgrade to the latest gdcloud CLI \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:57.862348+00:00
---

# Upgrade to the latest gdcloud CLI  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Upgrade to the latest gdcloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

Ensure that the latest version of gdcloud CLI and its components are installed on your local workstation.

## Update components

You can update all gdcloud CLI components to the latest version:
    
    
    gdcloud components update
    

The output lists all components the command is about to update, and asks for confirmation before proceeding. By default, this command updates all components to their latest version.

**Note:** Individual component updates are not supported.

## Upgrade gdcloud CLI installation

To check whether your gdcloud CLI installation is using the latest available version, complete the following steps:

  1. Check your current gdcloud CLI version:
         
         gdcloud version
         

Note the version output.

  2. Open the GDC console and, on the **Welcome** page, click **Download CLI Bundle**. Note the latest version available from the prompt.

![Check the CLI bundle version from the Download prompt.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/resources/images/cli-bundle-version.png)

  3. Compare your current version to the latest version available to download. If necessary, download the latest gdcloud CLI bundle and [reinstall](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install) it to upgrade to the latest available version.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
