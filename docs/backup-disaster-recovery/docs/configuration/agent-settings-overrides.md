---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/agent-settings-overrides/
title: Override Backup and DR agent settings for vCenter and ESX servers in the appliance management console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:10.297123+00:00
---

# Override Backup and DR agent settings for vCenter and ESX servers in the appliance management console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/agent-settings-overrides/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Override Backup and DR agent settings for vCenter and ESX servers in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

Appliance connections can be overridden from the appliance management console. These include the port over which you connect to the Backup and DR agent and the credentials for the connection.

Host type | Connection type  
---|---  
ESX server | The default ESX server management port is 902. If you use a  
| different port, then enter it here.  
| If the ESX server username and password have changed, then  
| change them here. If you don't need to override the default  
| settings, then enter nothing here.  
vCenter server | A vCenter can have both vCenter settings and  
| Backup and DR agent settings, because a vCenter  
| might also have the Backup and DR agent installed  
| on it.  
| The default vCenter management port is 443. If you use a  
| different port, then enter it here.  
| If the vCenter username and password have changed, then  
| change them here. If you don't need to override the default  
| settings, then enter nothing here.  
| You must have the proper permissions on the vCenter to make  
| any changes, otherwise you will see an error when you enter  
| the updated login credentials. The vCenter checks for login  
| credentials as well as permissions before it lets you make  
| any changes.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
