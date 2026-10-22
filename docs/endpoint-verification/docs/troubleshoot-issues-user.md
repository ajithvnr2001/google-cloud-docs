---
url: https://docs.cloud.google.com/endpoint-verification/docs/troubleshoot-issues-user/
title: Troubleshoot sync issues with the Endpoint Verification extension \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:46.081079+00:00
---

# Troubleshoot sync issues with the Endpoint Verification extension  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoint-verification/docs/troubleshoot-issues-user/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Endpoint Verification ](https://docs.cloud.google.com/endpoint-verification/docs)
  * [ Guides ](https://docs.cloud.google.com/endpoint-verification/docs/overview)



Send feedback 

#  Troubleshoot sync issues with the Endpoint Verification extension Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how users of an organization can resolve the Endpoint Verification synchronization issues on their devices.

If your issue is not listed in this document, contact your administrator. To help them diagnose your issue, download the Endpoint Verification logs and share them with your administrator:

  1. On your device, open the Chrome browser.
  2. In the Chrome browser toolbar, right-click **Endpoint Verification** and then click **Options > Download Log**.



## Sync issues to due Chrome browser

If the version of your Chrome browser is earlier than 110, you might encounter sync issues because Endpoint Verification is no longer supported on Chrome versions earlier than 110.

Error message: `Failed to sync. A sync will be retried shortly.`

To resolve this issue, update your Chrome browser to version 110 or later.

## Sync issues on macOS

This section lists sync issues that you might encounter on macOS and provides suggestions for how to fix them.

### Can't sync because of a Keychain authorization error

In the Chrome browser, you might get an error that Endpoint Verification can't sync because of a Keychain authorization error.

To resolve this issue, sign out of your computer and then sign in again. If the issue persists, complete the following steps:

  1. On your Mac, open the **Keychain Access** app.
  2. In the **Default keychains** pane, click **login**.

If the icon is locked, right-click **login** and then click **Unlock Keychain "login"**.

**Note:** If you can't unlock the login keychain or get into Access Control, see [Keychain Access User Guide](https://support.apple.com/en-ie/guide/keychain-access/kyca2429/mac).
  3. Click the **Passwords** tab.

  4. In the list of passwords, double-click **Endpoint Verification Safe Storage** and click **Access Control**.

  5. Select **Allow all applications to access this item** and click **Save changes**.

  6. In the Chrome browser toolbar, click **Endpoint Verification > Sync now**.

  7. If the sync is unsuccessful, do the following:

     1. In the list of passwords, right-click **Endpoint Verification Safe Storage** and then click **Delete "Endpoint Verification Safe Storage"**.
     2. In the Chrome browser toolbar, click **Endpoint Verification > Sync now**.



## Sync issues on Windows

This section lists sync issues that you might encounter on Windows OS and provides suggestions for how to fix them.

### Can't sync because of a Data Protection API error

In the Chrome browser, you might get an error that Endpoint Verification can't sync because of a Data Protection API error.

Endpoint Verification stores an encryption key in the Windows Registry during initial device enrollment. Subsequent syncs rely on Windows Data Protection API to access this key. Sync failures can occur if Endpoint Verification encounters errors when decrypting the key, often due to encryption by a different user. This issue might arise from S4U scheduled tasks, outdated Chrome versions, Windows configuration issues, or improper machine or user resets.

To resolve this issue, complete the following steps:

  1. Determine if an S4U task is configured:

     1. Lock the device screen.
     2. Within 15 seconds, unlock the device screen.
     3. Within 15 seconds, in the Chrome browser toolbar, click **Endpoint Verification > Sync now**. If the sync is successful, the error is likely caused by an S4U task.
  2. Identify the S4U tasks:

     1. Open PowerShell and run the following script:

`Get-ScheduledTask | foreach { If (([xml](Export-ScheduledTask -TaskName $_.TaskName -TaskPath $_.TaskPath)).GetElementsByTagName("LogonType").'#text' -eq "S4U") { $_.TaskName } }`

  3. If the output includes one or more lines containing a task name, fix the problem:

     1. On your Windows device, open **Task Scheduler**.
     2. Scroll to **Active Tasks**.
     3. Find the tasks from the output and do the following for each task:

        1. Double-click the task.
        2. Click **Properties**.
        3. Clear the **Do not store password** checkbox and click **Ok**.
     4. Lock the device screen and then unlock it.

     5. Within 15 seconds, in the Chrome browser toolbar, click **Endpoint Verification > Sync now**.




If the issue persists, do the following:

**Warning:** You can make your computer inoperable if you incorrectly configure registry keys. Use this approach only if you're comfortable editing registry keys. Your administrator might contact you because this approach creates duplicate entries for your device in their managed device list.

  1. In the **Windows Start** menu, click **Run**.
  2. In the **Run** box, enter **regedit**.
  3. In **Registry Editor** , find `HKEY_CURRENT_USER\Software\Google\Endpoint Verification\Safe Storage` and delete it.
  4. In the Chrome browser toolbar, click **Endpoint Verification > Sync now**.



If the issue persists, investigate device account administration and contact Windows support for further assistance.

### Can't sync because can't recover data protection key

In the Chrome browser, you might get an error that Endpoint Verification can't recover the data protection key and can't sync. This error can occur when S4U scheduled tasks run on your device and you have an earlier version of the Chrome browser on your device.

On Windows, Endpoint Verification should be able to read information on the device. To do so, Endpoint Verification uses the Windows API and that API needs the device to be trusted for delegation, and the current user account must be configured to allow delegation. The [`SEC_E_DELEGATION_REQUIRED`](https://learn.microsoft.com/en-us/troubleshoot/windows-server/certificates-and-public-key-infrastructure-pki/dpapi-masterkey-backup-failures#resolution) issue can occur in Windows, leading to API operation failures.

To resolve the problem, complete the following steps:

  1. Identify and edit S4U tasks:

     1. On your Windows device, open PowerShell and run the following script:

`Get-ScheduledTask | foreach { If (([xml](Export-ScheduledTask -TaskName $_.TaskName -TaskPath $_.TaskPath)).GetElementsByTagName("LogonType").'#text' -eq "S4U") { $_.TaskName } }`

     2. If the output includes one or more lines containing a task name, then edit these tasks:

        1. Open **Task Scheduler**.
        2. Scroll to **Active Tasks**.
        3. Find the tasks from the output and do the following for each task:

        4. Double-click the task.

        5. Click **Properties**.

        6. Clear the **Do not store password** checkbox and click **Ok**.

  2. Remove the registry key and start a new session


**Warning:** You can make your computer inoperable if you incorrectly configure registry keys. Use this approach only if you're comfortable editing registry keys. Your administrator might contact you because this approach creates duplicate entries for your device in their managed device list.

  1. In the **Windows Start** menu, click **Run**.
  2. In the **Run** box, enter **regedit**.
  3. In **Registry Editor** , find `HKEY_CURRENT_USER\Software\Google\Endpoint Verification\Safe Storage` and delete it.
  4. In the Chrome browser toolbar, click **Endpoint Verification > Sync now**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
