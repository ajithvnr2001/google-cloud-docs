---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/troubleshoot-conflicts-when-adding-appliances/
title: Troubleshoot conflicts when adding backup/recovery appliances \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:45.067578+00:00
---

# Troubleshoot conflicts when adding backup/recovery appliances  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/troubleshoot-conflicts-when-adding-appliances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Troubleshoot conflicts when adding backup/recovery appliances Stay organized with collections  Save and categorize content based on your preferences. 

If you encounter a conflict when adding a new backup/recovery appliance, resolve the conflict on the appliance that is experiencing the issue. For example, based on the identified conflict you can do the following:

  * Rename conflicting backup templates on the appliance.
  * Modify a conflicting backup template on the appliance to add the missing policies or remove the extra policies.
  * Modify the attributes in the differing policy (or policies) in the conflicting backup template on the appliance to make the attributes the same.
  * Modify the services or rights associated with the conflicting role identified on the appliance to make the services or rights the same.



Imported backup templates, users, and roles that already exist in the appliance management console (that have the same name) are addressed as follows:

  * **Backup templates** : Templates go through a conflict-resolution process by appliance management console described as follows.
  * **Users** : Users that already exist in appliance management console are ignored and are not imported from the appliance.
  * **Roles** : Roles go through a conflict-resolution process by the management console described as follows.



## Template ownership

Imported backup templates—and associated policies—managed by the appliance management console can be modified from the appliance management console. After you add an appliance to the appliance management console, don't create additional policy templates in the managed appliance after performing the initial import. If you do create additional policy templates on that same appliance post-import, when the appliance is synchronized with the appliance management console and the non-management console template is added to appliance management console, the template is considered to be a free-standing template. In this case, the template can only be used to capture application data from the originating appliance and cannot be shared with other appliances managed by the appliance management console.

## Invalid IP address or fully qualified domain name (FQDN) of backup/recovery appliance

The appliance management console displays an error condition if you:

  * Enter an invalid IP address or FQDN of the appliance to add to the appliance management console.
  * Attempt to promote the dependent appliance before the primary appliance.
  * Attempt to add an appliance that is already managed by another management console. Backup/recovery appliances can only be managed by a single appliance management console.



In the following example an invalid IP address has been entered for an appliance and the **Import Status** is **Failure**.

If you encounter an issue with an incorrect IP address or FQDN, check that you are entering the correct IP address or appliance hostname. You must enter the correct information for the appliance to be able to add it as a managed device by the appliance management console.

If the appliance that you are trying to add to the appliance management console is joined in sharing mode, the primary appliance must always be added first to the appliance management console. The primary appliance is used as the source for importing objects into the appliance management console, and the dependent appliance's shared objects is the same as the primary appliance. Ensure that you add the primary appliance first, followed by the dependent appliance. This order of adding appliances that are joined in shared mode is very important.

If the import fails because the appliance is managed by another appliance management console, keep in mind that you cannot add the same appliance to multiple appliance management consoles. If it is critical that this appliance be managed by a different appliance management console, your solution is to first remove the appliance from the original appliance management console and then add it to a different appliance management console.

## Conflict with imported objects from the appliance

When you add a new appliance to the appliance management console, during the dry-run phase of the import process a log appears to outline all import actions and decisions. The log includes a summary of the objects imported and added to the management console (templates, roles, and users) as well as any areas of conflict in backup templates or roles with the incoming appliance that exist in the appliance management console.

Object conflicts during the import process can occur under the following conditions:

  * Backup templates of the same name have a different number of policies or defined attributes between the appliance and the appliance management console.
  * Roles of the same name have differences in services or access control level (ACL) rights between the appliance and the appliance management console.



For example, the log example shown outlines the following:

  * Policies are missing from the standard and enterprise templates found in the in-coming appliance and the appliance management console.
  * Specific rights are missing from the basic role found in the in-coming appliance and the appliance management console.



If you encounter a conflict, resolve the conflict on the appliance as outlined in the following table.

**Note:** When you encounter a conflict with a backup template, we recommend that you make the necessary changes to the backup template on the appliance.Conflict | Problem source | Possible resolution  
---|---|---  
Backup templates | Backup templates of the same name have a different number of policies between the appliance and the appliance management console. | On the appliance, perform one of the following actions: 
* Rename the conflicting backup template.
* Modify the conflicting backup template to either add the missing policies or remove the extra policies.  
Backup templates | Backup plan policies of the same named template have different defined attributes—including policy type—between the appliance and the appliance management console. | On the appliance, perform one of the following actions: 
* Rename the conflicting backup template.
* Modify the attributes in the differing policy, or policies, in the conflicting backup template to make them the same.  
Roles | Roles of the same name have differences in services or access control level (ACL) rights between the appliance and the appliance management console. | On the appliance, modify the services or rights associated with the conflicting role to make them the same.  
Roles | Differences are detected in role-right assignments between the appliance and the appliance management console. | On the appliance management console, delete the problematic role and then retry adding the appliance to the appliance management console.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
