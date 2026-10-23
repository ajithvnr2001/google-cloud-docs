---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-fgpp/
title: Configure fine-grained password policies \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:02.125675+00:00
---

# Configure fine-grained password policies  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-fgpp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Configure fine-grained password policies Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use [fine-grained password policies (FGPP)](https://docs.cloud.google.com/managed-microsoft-ad/docs/fgpp-concepts) in Managed Service for Microsoft Active Directory.

To configure and manage FGPP in Managed Microsoft AD, you can use the standard Active Directory tools. For information about how to use the standard Active Directory tools in Managed Microsoft AD, see [Manage Active Directory objects](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-active-directory-objects).

## Delegate permissions to manage policies

By default, the [delegated administrator account](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-delegated-admin) has the ability to manage policies in Managed Microsoft AD.

To delegate the ability to manage policies, you can add users to the `Cloud Service Fine Grained Password Policy Administrators` group. To add users to this group, run the following command in PowerShell.
    
    
    Add-ADGroupMember -Identity 'Cloud Service Fine Grained Password Policy Administrators' \
      -Members USER_1,USER_2
    

Replace USER_1,USER_2 with the name of the users or groups for which you want to delegate permissions to manage the password policies. For example, `myuser`.

Learn more about [`Add-ADGroupMember`](https://docs.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember).

### Remove permissions to manage policies

To remove the ability to manage policies, you can remove the user from the `Cloud Service Fine Grained Password Policy Administrators` group. To remove users from this group, run the following command in PowerShell.
    
    
    Remove-ADGroupMember -Identity 'Cloud Service Fine Grained Password Policy Administrators' \
      -Members USER_1,USER_2
    

Replace USER_1,USER_2 with the name of the users or groups for which you want to remove the permissions provided to manage the password policies. For example, `myuser`.

Learn more about [`Remove-ADGroupMember`](https://docs.microsoft.com/en-us/powershell/module/activedirectory/remove-adgroupmember).

## Modify a pre-created password policy

You can modify the [policy settings](https://docs.cloud.google.com/managed-microsoft-ad/docs/fgpp-concepts#policy_settings) of a FGPP. You can decide which policy settings you want to modify and use only the required properties in the following command.

**Note:** The following command only illustrates how to modify the policy settings of a FGPP. Before you modify these policy settings, we recommend that you read the [Microsoft documentation](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc770394\(v=ws.10\)) and understand how these policy settings affect the effective password policy.

To modify a pre-created password policy, run the following command in PowerShell.
    
    
    Set-ADFineGrainedPasswordPolicy -Identity PSO -LockoutThreshold THRESHOLD -LockoutDuration DURATION_TIME \
       -LockoutObservationWindow OBSERVATION_TIME -ComplexityEnabled COMPLEXITY_BOOLEAN \
       -ReversibleEncryptionEnabled ENCRYPTION_BOOLEAN -MinPasswordLength LENGTH \
       -MaxPasswordAge PASSWORD_AGE -PasswordHistoryCount PASSWORD_COUNT
    

Replace the following:

  * PSO: Name of the PSO for which you want to modify the policy settings. For example, `PSO-10`.

  * THRESHOLD: Specify the number of failed login attempts after which a user must be locked.

  * DURATION_TIME: Specify the length of time for which a user must be locked after the specified number of failed login attempts.

  * OBSERVATION_TIME: Specify the length of time during which a user must reach the threshold for failed login attempts to get the user locked.

  * COMPLEXITY_BOOLEAN: Specify whether password complexity must be enabled for the password policy.

  * ENCRYPTION_BOOLEAN: Specify whether the passwords must be stored using reversible encryption.

  * LENGTH: Specify the minimum number of characters that the passwords must have.

  * PASSWORD_AGE: Specify the length of time that a user can have the same password. A user must change the password after this time period.

  * PASSWORD_COUNT: Specify the number of previous passwords to save in a user's password history. A user cannot reuse a password saved in their password history.




Learn more about [`Set-ADFineGrainedPasswordPolicy`](https://docs.microsoft.com/en-us/powershell/module/activedirectory/set-adfinegrainedpasswordpolicy).

## Add a user or group to a password policy

Add a user or group to a password policy to enforce the FGPP.

To apply a password policy to a user or group, run the following command in PowerShell.
    
    
    Add-ADFineGrainedPasswordPolicySubject PSO -Subjects USER_1,USER_2
    

Replace the following:

  * PSO: Name of the password setting object (PSO) to which you want to add the user or group. For example, `PSO-10`.

  * USER_1,USER_2: Name of the users or groups for which you want to enforce the FGPP. For example, `myuser`.




Learn more about [`Add-ADFineGrainedPasswordPolicySubject`](https://docs.microsoft.com/en-us/powershell/module/activedirectory/add-adfinegrainedpasswordpolicysubject).

## Check which password policy applies to a user

You can apply several password policies to a user or a group. The policy with the lowest precedence setting is the effective policy. For information about the precedence settings of PSOs, see [Password settings objects](https://docs.cloud.google.com/managed-microsoft-ad/docs/objects#password_settings_objects).

To see the effective policy on a user, run the following command in PowerShell.
    
    
    Get-ADUserResultantPasswordPolicy -Identity USER
    

Replace USER with the name of the user for which you want to check the password policies applied. For example, `myuser`.

Learn more about [`Get-ADUserResultantPasswordPolicy`](https://docs.microsoft.com/en-us/powershell/module/activedirectory/get-aduserresultantpasswordpolicy).

## Remove a user or group from a password policy

Remove a user or group from a password policy to stop enforcing the FGPP.

To remove a user or group from a password policy, run the following command in PowerShell.
    
    
    Remove-ADFineGrainedPasswordPolicySubject PSO -Subjects USER_1,USER_2
    

Replace the following:

  * PSO: Name of the PSO from which you want to remove the user or group. For example, `PSO-10`.

  * USER_1,USER_2: Name of the users or groups for which you want to stop enforcing the FGPP. For example, `myuser`.




Learn more about [`Remove-ADFineGrainedPasswordPolicySubject`](https://docs.microsoft.com/en-us/powershell/module/activedirectory/remove-adfinegrainedpasswordpolicysubject).

## Unlock a user

Active Directory suspends or locks access for a user when the number of incorrect password entries exceeds the maximum number allowed by the password policy.

To unlock a user, run the following PowerShell command. Note that you must be a member of the `Cloud Service All Administrators` group.
    
    
    Unlock-ADAccount -Identity USER
    

Replace USER with the name of the user who you want to unlock. For example, `myuser`.

Learn more about [`Unlock-ADAccount`](https://docs.microsoft.com/en-us/powershell/module/activedirectory/unlock-adaccount).

The user is automatically unlocked after the [lockout duration](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/hh994569\(v=ws.10\)) configured in the password policy.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
