---
url: https://docs.cloud.google.com/compute/docs/security/ms-secure-boot-certificates-update/
title: Update KEK and db certificates \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:13.745051+00:00
---

# Update KEK and db certificates  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/security/ms-secure-boot-certificates-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Update KEK and db certificates Stay organized with collections  Save and categorize content based on your preferences. 

This document provides instructions for updating the Allowed Signature Database (`db`) and Key Exchange Key (`KEK`) variables on compute instances that you created before November 7, 2025 to trust updated certificates for Secure Boot.

KEK and db update is an alternative for customers who don't recreate their affected compute instances.

**Note:** Unlike Windows, Linux doesn't require a system reboot for KEK and db signature updates to write to the UEFI variables. Linux immediately writes updates to the NVRAM or firmware storage upon command execution.

## Before you begin

Before updating your Secure Boot KEK and db certificates, verify whether your instances require an update and complete the following preparations to prevent potential boot or decryption issues:

  * **Prerequisite verification:** [Verify](https://docs.cloud.google.com/compute/docs/security/ms-secure-boot-certificates-expiration#verification) that your instances require a Secure Boot certificates update.
  * **Data integrity and key recovery:** Locate your disk encryption (BitLocker or LUKS FDE) recovery keys and back up critical data. Changing security variables can lock access to disks if the configuration is incorrect.
  * **Linux update sequencing recommendation:** For Linux instances, we recommend updating the `db` UEFI variable to Microsoft UEFI CA 2023 before updating to new shims. This sequencing helps prevent a potential CA mismatch scenario if a shim update signed only with the Microsoft UEFI CA 2023 is applied while the database contains only the 2011 certificate.
  * **Custom PK or KEK configurations** : If your instance uses custom Secure Boot variables (such as a custom `PK` or `KEK`), or if you're running on a system outside of Compute Engine, the standard update files (`DBUpdate3P2023.bin` or `kek2023update.bin`) provided in this document won't apply directly. The UEFI firmware requires update files to be signed by the private key of the `KEK` or `PK` enrolled on the system, and `kek2023update.bin` is signed specifically by the default Compute Engine `PK`. If you use custom keys, you must sign the update binaries with your own private keys or manage the updates through your custom certificate authority. See Troubleshoot KEK update errors for more information.
  * **Google Cloud Backup and DR appliances:** These are managed appliances. You don't need to manually update Secure Boot certificates on these appliances. Google Cloud automatically manages all updates.



## Update db and KEK on Linux

To update the Allowed Signature Database (`db`) and Key Exchange Key (`KEK`), select the option for your operating system:

###  Debian or Ubuntu 

You can update the Secure Boot certificates on Debian or Ubuntu by using `fwupd`, `efitools`, or `sbsigntool`.

#### Option 1: Update using `fwupd` (Recommended)

We recommend using `fwupd` to update your certificates. This method requires `fwupdmgr` version `2.0.10` or later. Verify your version by running `sudo fwupdmgr --version`.

Run the following commands:
    
    
    sudo fwupdmgr refresh
    sudo fwupdmgr update 5bc922b7bd1adb5b6f99592611404036bd9f42d0
    sudo fwupdmgr update b7a1d3d90faa1f6275d9a98da4fb3be7118e61c7
    

#### Option 2: Update using `efitools`

To update the `db` and `KEK` variables by using the `efitools` package, do the following:

##### Update db

  1. Download the Allowed Signature Database (`db`) update binary from Microsoft:
         
         wget https://github.com/microsoft/secureboot_objects/raw/main/PostSignedObjects/Optional/DB/DBUpdate3P2023.bin
         

  2. Update the `db` variable:
         
         sudo chattr -i /sys/firmware/efi/efivars/db-*
          sudo efi-updatevar -a -f DBUpdate3P2023.bin db
          sudo chattr +i /sys/firmware/efi/efivars/db-*
         




##### Update KEK

  1. Download the `.cab` archive containing the certificate update:
         
         wget https://fwupd.org/downloads/1953fae13600a35944e93cd244476a6f6ce5fdbf620709b2f6f378fac2ae3bef-KEK-google_compute_engine.cab
         

  2. Install the `gcab` utility:
         
         sudo apt update && sudo apt install gcab -y
         

  3. Extract the archive and verify that the SHA-256 hash of the extracted `kek2023update.bin` file matches `99e340f5cfd7aa3698f80237b51e460fc6367111876f39b4a9e1d1aa495d5eaf`:
         
         gcab --extract 1953fae13600a35944e93cd244476a6f6ce5fdbf620709b2f6f378fac2ae3bef-KEK-google_compute_engine.cab
          sha256sum kek2023update.bin
         

  4. Apply the update:
         
         sudo chattr -i /sys/firmware/efi/efivars/KEK-*
          sudo efi-updatevar -a -f kek2023update.bin KEK
          sudo chattr +i /sys/firmware/efi/efivars/KEK-*
         




#### Option 3: Update using `sbsigntool`

To update the `db` and `KEK` variables by using the `sbkeysync` utility from the `sbsigntool` package, install `sbsigntool` and `gcab`:
    
    
    sudo apt update && sudo apt install sbsigntool gcab -y
    

##### Update db

  1. Download the `db` update binary from Microsoft:
         
         wget https://github.com/microsoft/secureboot_objects/raw/main/PostSignedObjects/Optional/DB/DBUpdate3P2023.bin
         

  2. Synchronize the key:
         
         sudo mkdir -p /etc/secureboot/keys/db
          sudo cp DBUpdate3P2023.bin /etc/secureboot/keys/db/
          sudo chattr -i /sys/firmware/efi/efivars/db-*
          sudo sbkeysync --verbose
          sudo chattr +i /sys/firmware/efi/efivars/db-*
         




##### Update KEK

  1. Download and extract the KEK certificate update:
         
         wget https://fwupd.org/downloads/1953fae13600a35944e93cd244476a6f6ce5fdbf620709b2f6f378fac2ae3bef-KEK-google_compute_engine.cab
          gcab --extract 1953fae13600a35944e93cd244476a6f6ce5fdbf620709b2f6f378fac2ae3bef-KEK-google_compute_engine.cab
         

  2. Verify that the SHA-256 hash of the extracted `kek2023update.bin` file matches `99e340f5cfd7aa3698f80237b51e460fc6367111876f39b4a9e1d1aa495d5eaf`:
         
         sha256sum kek2023update.bin
         

  3. Synchronize the key:
         
         sudo mkdir -p /etc/secureboot/keys/KEK
          sudo cp kek2023update.bin /etc/secureboot/keys/KEK/
          sudo chattr -i /sys/firmware/efi/efivars/KEK-*
          sudo sbkeysync --verbose
          sudo chattr +i /sys/firmware/efi/efivars/KEK-*
         




###  Red Hat Enterprise Linux (RHEL) 

You can update the Secure Boot certificates on RHEL by using `sbsigntools`. RHEL images might have an older version of `fwupd` that does not support UEFI certificate updates out of the box.

**Note:** If you want to use the `fwupd` method, you must build `fwupd` version `2.0.10` or later from source.

To update the `db` and `KEK` variables by using the `sbkeysync` utility from the `sbsigntools` package, do the following:

  1. Enable the EPEL repository and install `sbsigntools` and `cabextract`:
         
         sudo dnf install epel-release -y
         sudo dnf install sbsigntools cabextract -y
         

  2. To update the `db` variable, do the following:

     1. Download the Allowed Signature Database (`db`) update binary from Microsoft:
            
            wget https://github.com/microsoft/secureboot_objects/raw/main/PostSignedObjects/Optional/DB/DBUpdate3P2023.bin
            

     2. Synchronize the key:
            
            sudo mkdir -p /etc/secureboot/keys/db
            sudo cp DBUpdate3P2023.bin /etc/secureboot/keys/db/
            sudo chattr -i /sys/firmware/efi/efivars/db-*
            sudo sbkeysync --verbose
            sudo chattr +i /sys/firmware/efi/efivars/db-*
            

  3. To update the `KEK` variable, do the following:

     1. Download and extract the KEK certificate update:
            
            wget https://fwupd.org/downloads/1953fae13600a35944e93cd244476a6f6ce5fdbf620709b2f6f378fac2ae3bef-KEK-google_compute_engine.cab
            cabextract -f 1953fae13600a35944e93cd244476a6f6ce5fdbf620709b2f6f378fac2ae3bef-KEK-google_compute_engine.cab
            

     2. Verify that the SHA-256 hash of the extracted `kek2023update.bin` file matches `99e340f5cfd7aa3698f80237b51e460fc6367111876f39b4a9e1d1aa495d5eaf`:
            
            sha256sum kek2023update.bin
            

     3. Synchronize the key:
            
            sudo mkdir -p /etc/secureboot/keys/KEK
            sudo cp kek2023update.bin /etc/secureboot/keys/KEK/
            sudo chattr -i /sys/firmware/efi/efivars/KEK-*
            sudo sbkeysync --verbose
            sudo chattr +i /sys/firmware/efi/efivars/KEK-*
            




###  SUSE Linux Enterprise Server (SLES) 

You can update the Secure Boot certificates on SLES or openSUSE by using `sbsigntools` or `efitools`. SLES images might have an older version of `fwupd` or don't provide it at all.

**Note:** If you want to use the `fwupd` method, you must build `fwupd` version `2.0.10` or later from source.

#### Option 1: Update using `sbsigntools`

To update the `db` and `KEK` variables by using the `sbkeysync` utility from the `sbsigntools` package, enable the SUSE Package Hub and install `sbsigntools` and `cabextract`:
    
    
    sudo SUSEConnect -p PackageHub/15.5/x86_64
    sudo zypper install sbsigntools cabextract -y
    

**Note:** Replace `15.5` with your SLES version if different.

##### Update db

  1. Download the `db` update binary from Microsoft:
         
         wget https://github.com/microsoft/secureboot_objects/raw/main/PostSignedObjects/Optional/DB/DBUpdate3P2023.bin
          ```
         

  2. Synchronize the key:
         
         sudo mkdir -p /etc/secureboot/keys/db
          sudo cp DBUpdate3P2023.bin /etc/secureboot/keys/db/
          sudo chattr -i /sys/firmware/efi/efivars/db-*
          sudo sbkeysync --verbose
          sudo chattr +i /sys/firmware/efi/efivars/db-*
          ```
         




##### Update KEK

  1. Download and extract the KEK certificate update:
         
         wget https://fwupd.org/downloads/1953fae13600a35944e93cd244476a6f6ce5fdbf620709b2f6f378fac2ae3bef-KEK-google_compute_engine.cab
          cabextract -f 1953fae13600a35944e93cd244476a6f6ce5fdbf620709b2f6f378fac2ae3bef-KEK-google_compute_engine.cab
          ```
         

  2. Verify that the SHA-256 hash of the extracted `kek2023update.bin` file matches `99e340f5cfd7aa3698f80237b51e460fc6367111876f39b4a9e1d1aa495d5eaf`:
         
         sha256sum kek2023update.bin
          ```
         

  3. Synchronize the key:
         
         sudo mkdir -p /etc/secureboot/keys/KEK
          sudo cp kek2023update.bin /etc/secureboot/keys/KEK/
          sudo chattr -i /sys/firmware/efi/efivars/KEK-*
          sudo sbkeysync --verbose
          sudo chattr +i /sys/firmware/efi/efivars/KEK-*
          ```
         




#### Option 2: Update using `efitools`

To update the `db` and `KEK` variables by using the `efitools` package, do the following:

##### Update db

  1. Download the Allowed Signature Database (`db`) update binary from Microsoft:
         
         wget https://github.com/microsoft/secureboot_objects/raw/main/PostSignedObjects/Optional/DB/DBUpdate3P2023.bin
          ```
         

  2. Update the `db` variable:
         
         sudo chattr -i /sys/firmware/efi/efivars/db-*
          sudo efi-updatevar -a -f DBUpdate3P2023.bin db
          sudo chattr +i /sys/firmware/efi/efivars/db-*
          ```
         




##### Update KEK

  1. Download the `.cab` archive containing the certificate update:
         
         wget https://fwupd.org/downloads/1953fae13600a35944e93cd244476a6f6ce5fdbf620709b2f6f378fac2ae3bef-KEK-google_compute_engine.cab
          ```
         

  2. Enable the SUSE Package Hub and install the `gcab` utility:
         
         sudo SUSEConnect -p PackageHub/15.5/x86_64
          sudo zypper install gcab -y
          ```
         Note: Replace `15.5` with your SLES version if different.
         

  3. Extract the archive and verify that the SHA-256 hash of the extracted `kek2023update.bin` file matches `99e340f5cfd7aa3698f80237b51e460fc6367111876f39b4a9e1d1aa495d5eaf`:
         
         gcab --extract 1953fae13600a35944e93cd244476a6f6ce5fdbf620709b2f6f378fac2ae3bef-KEK-google_compute_engine.cab
          sha256sum kek2023update.bin
          ```
         

  4. Apply the update:
         
         sudo chattr -i /sys/firmware/efi/efivars/KEK-*
          sudo efi-updatevar -a -f kek2023update.bin KEK
          sudo chattr +i /sys/firmware/efi/efivars/KEK-*
          ```
         




## Update db and KEK on Windows

You don't need to apply these certificate updates if you don't use or plan to use Secure Boot on this instance. Windows operating systems generally ignore attempts to apply these Secure Boot certificate updates if Secure Boot is not enabled because the update is unnecessary.

If you intend to use Secure Boot later, you must first enable Secure Boot on the instance to update the secure boot certificates.

On Windows instances, registry settings and scheduled tasks trigger updates on compatible versions:

  1. Ensure your Windows instances have recent monthly updates applied.
  2. As an Administrator in PowerShell, run:
         
         Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\SecureBoot" -Name "AvailableUpdates" -Value 0x5944
         Start-ScheduledTask -TaskName "\Microsoft\Windows\PI\Secure-Boot-Update"
         

  3. Reboot the instance to permit operations on firmware variables. Some environments require double restarts if virtualization security features are active.




## Verify the update

After applying the updates using `fwupd`, `efitools`, `sbsigntool`, or PowerShell, verify that the 2023 certificates are present in your instance's UEFI variables.

### Linux

Regardless of the tool used to apply the update, the certificates are written to the instance's UEFI NVRAM variables. You can verify them directly using `mokutil` (recommended) or `efi-readvar`:

  * **Using`mokutil` (Recommended):** `mokutil` is installed by default on most Linux distributions.
        
        sudo mokutil --kek | grep "KEK 2K CA 2023"
        sudo mokutil --db | grep "UEFI CA 2023"
        

  * **Using`efi-readvar`:** If you have `efitools` installed, run:
        
        sudo efi-readvar -v KEK | grep "KEK 2K CA 2023"
        sudo efi-readvar -v db | grep "UEFI CA 2023"
        




If both the `KEK` and `db` variables show the 2023 certificates, the update was applied successfully and no further action is required.

### Windows

In an administrator PowerShell prompt, run:
    
    
    # Check for Microsoft KEK 2K CA 2023
    [System.Text.Encoding]::ASCII.GetString((Get-SecureBootUEFI KEK).bytes) -match 'Microsoft Corporation KEK 2K CA 2023'
    
    # Check for UEFI CA 2023
    [System.Text.Encoding]::ASCII.GetString((Get-SecureBootUEFI db).bytes) -match 'UEFI CA 2023'
    
    # Confirm general Secure Boot enrollment state
    Confirm-SecureBootUEFI
    

## Troubleshoot KEK update errors

When updating the `KEK` variable on Linux, the `db` update (`DBUpdate3P2023.bin`) might succeed while the `KEK` update (`kek2023update.bin`) fails with one of the following errors:

  * When using `sbkeysync`:
        
        Inserting key update /etc/secureboot/keys/KEK/kek2023update.bin into KEK
        Error writing key update: Invalid argument
        Error syncing keystore file /etc/secureboot/keys/KEK/kek2023update.bin
        

  * When using `efi-updatevar`:
        
        Cannot write to KEK, wrong filesystem permissions
        




### Cause

In UEFI Secure Boot, `db` updates (`DBUpdate3P2023.bin`) are signed by the Microsoft Corporation KEK CA 2011, which is enrolled by default on most UEFI Secure Boot systems. However, `KEK` updates must be signed by the Platform Key (`PK`) enrolled in the system's firmware. When the firmware rejects the signature on `kek2023update.bin` or prevents writing to the UEFI variable, the Linux kernel returns an error.

This error occurs for one of the following reasons:

  * **The`KEK` UEFI variable is still marked as immutable**: The `chattr -i` command wasn't run before attempting the write operation.
  * **The instance uses a custom`PK`**: The `1953fae13600a35944e93cd244476a6f6ce5fdbf620709b2f6f378fac2ae3bef-KEK-google_compute_engine.cab` archive contains a `kek2023update.bin` binary that is signed exclusively by the default Compute Engine `PK`. If your Compute Engine instance or custom image has a custom `PK` enrolled, the firmware rejects `kek2023update.bin`.
  * **The system isn't a Compute Engine instance** : If you run these commands on physical hardware or a virtual machine outside of Compute Engine, the system's `PK` belongs to the hardware manufacturer or hypervisor vendor rather than Compute Engine, causing the firmware to reject `kek2023update.bin`.



### Resolution

To diagnose and resolve the error, do the following:

  1. Ensure that you remove the immutable attribute from the `KEK` variable immediately before running `sbkeysync` or `efi-updatevar`:
         
         sudo chattr -i /sys/firmware/efi/efivars/KEK-*
         

  2. Inspect the `PK` enrolled on your instance:
         
         sudo mokutil --pk
         

  3. Depending on the `sudo mokutil --pk` output, take one of the following actions:

     * **If the instance uses a custom`PK`**: Sign the `KEK` update binary with the private key corresponding to your custom `PK`, or [recreate the compute instance from a disk snapshot](https://docs.cloud.google.com/compute/docs/security/ms-secure-boot-certificates-expiration#recreate_a_compute_instance_from_a_disk_snapshot) using an image that relies on the default Compute Engine Secure Boot certificates.
     * **If you're updating a non-Compute Engine machine** : Remove `/etc/secureboot/keys/KEK/kek2023update.bin` and obtain the `KEK` update from your hardware manufacturer or platform vendor (for example, by running `sudo fwupdmgr update` if supported by your vendor).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
