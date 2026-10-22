---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-sudoers-file/
title: Troubleshooting sudoers files \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:40.629933+00:00
---

# Troubleshooting sudoers files  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-sudoers-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting sudoers files Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

The page provides tips on using the `sudo` command-line utility, managing the `sudoers` plugin, and preventing or fixing issues that arise.

## Causes of problems

During each execution of the `sudo` command, the following process takes place to validate the `sudoers` files:

  * The syntax is checked for correctness.
  * The content is analyzed to exclude some of the logical errors.
  * Ownership and permissions are checked.



The validation of the `sudoers` files might fail due to any of the following errors:

###  Syntax errors 

You must follow specific syntax rules when you make changes to the `sudoers` files. Any deviation from this syntax, including but not limited to a missing or extra character or an inappropriate comma, can make the file invalid. Invalidation of the file makes it impossible to use the `sudo` utility.

**Solution**

The solution is to use `visudo` utility to edit the `sudoers` files. It validates the file content before saving and notifies in case of issues. The `visudo` utility was created for editing the file in a safe fashion.

* * *

The following examples shows both correct and incorrect syntax samples:

Correct syntax
    
    
    user   ALL=(ALL) ALL
    

Incorrect syntax
    
    
    user   ALL=(ALL), ALL
    

Syntax error example
    
    
    $ sudo useradd username
    /etc/sudoers:20:17: syntax error
    user   ALL=(ALL), ALL
                    ^
    

###  Logical errors 

Errors of this type can be caused by one of the following:

  * A misunderstanding of the principles of the `sudoers` plugin.
  * Deviations from the correct syntax.



However, logical errors are not recognized during validation, because they do not violate syntax rules and therefore are tricky to detect.

**Solution**

You must carefully read the official documentation and adhere to its principles when you edit the file.

Google also recommends that you use the `visudo` utility to edit the `sudoers` files, as it can detect some types of logical errors, such as:

  * Undefined or unused aliases
  * Cyclic references
  * Duplicate entries



If any issues are detected, you see a warning message.

* * *

The following examples shows both logically correct and incorrect samples:

Logically correct
    
    
    barbara   ALL=(ALL:ALL) /usr/bin/ls
    

Logically incorrect
    
    
    barbara   ALL=(4LL:ALL) /usr/bin/ls
                   ^
    barbara   ALL=(ALL;ALL) /usr/bin/ls
                      ^
    bar6ara   ALL=(ALL:ALL) /usr/bin/1s
       ^                             ^
    

###  Incorrect permissions 

In addition to errors caused by the content of the `sudoers` files, their excessive file permissions or incorrect ownership can also cause the `sudo` utility to fail.

**Solution**

You see a description of these errors in the output of the failed `sudo` command. Read through the error message description and make the necessary corrections.

* * *

The following is an example of the correct file permissions and ownership
    
    
    $ ls -l /etc/sudoers
    -r--r----- 1 root root 700 Jan 1 12:00 /etc/sudoers
    
    $ sudo useradd username
    

The following example shows the error that is displayed when there are redundant permissions for the **all users** permission group:
    
    
    $ ls -l /etc/sudoers
    -r--r---w- 1 root root 700 Jan 1 12:00 /etc/sudoers
    
    $ sudo useradd username
    sudo: /etc/sudoers is world writable
    sudo: no valid sudoers sources found, quitting
    sudo: error initializing audit plugin sudoers_audit
    

The following example shows the error that is displayed for incorrect ownership. In this example, a user with an ID that is not `0` (or a user that is not `root`) is the owner of the file:
    
    
    $ ls -l /etc/sudoers
    -r--r----- 1 user user 700 Jan 1 12:00 /etc/sudoers
    
    $ sudo useradd username
    sudo: /etc/sudoers is owned by uid 1000, should be 0
    sudo: no valid sudoers sources found, quitting
    sudo: error initializing audit plugin sudoers_audit
    

For more information about the configuration of the `sudoers` files, read [Sudoers Manual](https://www.sudo.ws/docs/man/sudoers.man/).

To learn how to manage and use the `visudo` editor, read [Visudo Manual](https://www.sudo.ws/docs/man/visudo.man/).

## Consequences of problems

Issues in the `sudoers` files cause negative effects and can affect the functionality of the entire system.

  * The `sudo` command no longer works.

This is the most noticeable consequence of issues in the `sudoers` files. The consequence of this is the inability to use elevated privileges for users, which blocks their activity on the server.

However, more destructive and unpredictable consequences are failures of the applications that rely on the `sudo` command. In some cases, this may cause the application to fail completely, leading to unexpected behavior, crashes, or data loss. Another example is when the `sudo` command is called by an application during the OS boot sequence and fails. It can lead to OS failure or cause the boot sequence to get stuck.

**Tip:** If there is some kind of problem with the `sudoers` files, we strongly recommended that you stop the workload on the virtual machine (VM) instance, if possible, until the problem is fixed. This can be done in a number of ways, including the following: 
    * Temporarily disabling the startup or shutdown scripts.
    * Pausing the `cron` jobs.
  * Possible unauthorized access to the system.

Another risky consequence is that issues in the `sudoers` files can lead to unauthorized access to the system. This can happen due to a logical error, when rules in the `sudoers` files give some users or groups excessive permissions.

This may also happen because the system owner temporarily disables or weakens the system's defenses in order to log in and fix the problem.

**Tip:** In order to avoid unauthorized access it is recommended to carefully read the official documentation before editing the `sudoers` files. Additionally, during the recovery process, we highly recommended that you don't use unsafe approaches such as the following: 
    * Temporarily setting the password of the `root` user through the startup script.
    * Creating a temporary user with administrator rights and the permissions to log in without a password.



## Recovery in case of problems

If you lose elevated user privileges or can't use the `sudo` command due to problems with the `sudoers` files, then use the superuser account for recovery.

In Unix-like operating systems, the superuser is a special user account with ID equal to 0, that is usually called `root`. The superuser has full access to the system resources, and can perform any administrative task without restrictions. While interacting with the OS on behalf of the superuser is generally considered insecure, it may be the only option for certain tasks such as recovery of the `sudoers` files.

Logging in directly as the superuser exposes the OS to risk. To avoid this risk, Google recommends that you use a startup script functionality, as this script is executed on behalf of the superuser.

Read more about Compute Engine [startup scripts](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/linux).

To recover the `sudoers` files with a startup script, do the following:

  1. Create a backup copy of the current startup script if it's already in use. The backup approach depends on how the startup script is configured.

###  startup-script 

If the script content is set directly in the metadata value, you can copy the script content to the [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/uploading-objects), local file or any other temporary private storage.

**Caution:** Use only trusted storage so that the script doesn't leak during the recovery process.

###  startup-script-url 

If the contents of the script are already in the remote storage and its URL address is used, then you can just temporary remove the `startup-script-url` metadata key to disable the current startup script.

**Caution:** Do not remove the script file itself from the remote storage.

  2. [Update the startup script](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/linux#passing-directly) with the following command sequence:
         
         mv /etc/sudoers /etc/sudoers.backup.$(date +"%s") && echo "%google-sudoers ALL=(ALL:ALL) NOPASSWD:ALL" > /etc/sudoers && chown 0:0 /etc/sudoers && chmod 0440 /etc/sudoers
         

Read more about what the commands does

` mv /etc/sudoers /etc/sudoers.backup.$(date +"%s") `
    

This command creates a copy of the `/etc/sudoers` file with a different name and deletes the original file. The name of the new file contains a timestamp at the end for uniqueness (e.g. `sudoers.backup.1672527600`). 

` echo "%google-sudoers ALL=(ALL:ALL) NOPASSWD:ALL" > /etc/sudoers `
    

This command creates previously deleted file `/etc/sudoers` with a single rule that allows authorized Google Cloud users with access to the VM to execute any commands on behalf of any system user. This rule always exists by default in an additional file `/etc/sudoers.d/google_sudoers`. 

` chown 0:0 /etc/sudoers `
    

This command sets the owner of the `/etc/sudoers` file to a user whose ID is `0` and a group of owners to a group whose ID is `0`. 

` chmod 0440 /etc/sudoers `
    

This command sets permissions for the `/etc/sudoers` file to read-only and allows only its owner and owner group to read the file. 

**Note:** After these manipulations, the `/etc/sudoers` file can still be modified by authorized users of the system using the `visudo` utility. 

  3. [Stop the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance), if it's running. Restart the VM to trigger the execution of the startup script.

  4. [Сonnect to the VM](https://docs.cloud.google.com/compute/docs/connect/standard-ssh) and edit the broken `sudoers` file to recover it.
         
         sudo visudo /etc/sudoers.backup.TIMESTAMP

**Note:** Instead of fixing the `sudoers` file manually, you can [create a new VM instance](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance) with the same boot disk image and copy the correct file from there.
  5. Save the changes and replace the current `/etc/sudoers` file with the file you just edited.
         
         sudo mv /etc/sudoers.backup.TIMESTAMP /etc/sudoers

  6. Make sure that the original issue with using the `sudo` command and elevated privileges has been fixed.

  7. Remove the temporary startup script and restore the original one if it was used.

**Note:** If the temporary startup script remains, the content of the `/etc/sudoers` file is overwritten each time the VM is restarted.

## What's Next?

     * Learn how to [recover an inaccessible or corrupted VM](https://docs.cloud.google.com/compute/docs/disks/recover-vm).
     * Learn how to [add an existing disk to another VM](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#create_disk).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

     * ### Products and pricing

       * [ See all products ](https://cloud.google.com/products/)
       * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
       * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
       * [ Contact sales ](https://cloud.google.com/contact/)
     * ### Support

       * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
       * [ Support ](https://cloud.google.com/support-hub/)
       * [ Release Notes ](https://docs.cloud.google.com/release-notes)
       * [ System status ](https://status.cloud.google.com)
     * ### Resources

       * [ GitHub ](https://github.com/googlecloudPlatform/)
       * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
       * [ Code samples ](https://docs.cloud.google.com/docs/samples)
       * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
       * [ Training and Certification ](https://cloud.google.com/learn/training/)
       * [ Builders Hub ](https://me.developers.google.com/)
     * ### Engage

       * [ Blog ](https://cloud.google.com/blog/)
       * [ Events ](https://cloud.google.com/events/)
       * [ X (Twitter) ](https://x.com/googlecloud)
       * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
       * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)

[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)
     * [ Android ](https://developer.android.com/)
     * [ Chrome ](https://developer.chrome.com/)
     * [ Firebase ](https://firebase.google.com/)
     * [ Google AI ](https://ai.google.com/)
     * [ About Google ](https://about.google/)
     * [ Privacy ](https://policies.google.com/privacy)
     * [ Site terms ](https://policies.google.com/terms?hl=en)
     * [ Google Cloud terms ](https://cloud.google.com/product-terms)
     * Manage cookies 
     * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
     * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)
     * English
     * Deutsch
     * Español
     * Español – América Latina
     * Français
     * Indonesia
     * Italiano
     * Português
     * Português – Brasil
     * עברית
     * 中文 – 简体
     * 中文 – 繁體
     * 日本語
     * 한국어



