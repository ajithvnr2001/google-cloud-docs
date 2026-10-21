---
url: https://docs.cloud.google.com/compute/docs/security/ms-secure-boot-certificates-expiration/
title: Microsoft Secure Boot certificates expiration guide \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:59:24.344547+00:00
---

# Microsoft Secure Boot certificates expiration guide  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/security/ms-secure-boot-certificates-expiration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Microsoft Secure Boot certificates expiration guide Stay organized with collections  Save and categorize content based on your preferences. 

Because multiple Microsoft Secure Boot certificates expire in 2026, this document provides guidance on how to update Compute Engine Shielded VM instances to trust the updated Microsoft Secure Boot certificates for UEFI (Unified Extensible Firmware Interface) Secure Boot. The two most critical certificates nearing expiration are the Microsoft Corporation UEFI CA 2011 (expires June 27, 2026), which signs third-party bootloaders such as the Linux Shim, and the Microsoft Windows Production PCA 2011, which expires on October 19, 2026, and signs the Windows bootloader.

UEFI Secure Boot is a security standard that Shielded VMs use to ensure that only trusted software and firmware run during the VM boot process. To support Secure Boot across various operating systems, Microsoft manages UEFI certificates, storing them in the Key Exchange Key (`KEK`) and Allowed Signature Database (`db`) variables within the instance firmware.

## Considerations for Backup and DR Service users

Because Backup and DR Service is a managed service, Google Cloud automatically manages the underlying operating system and Secure Boot certificate updates for your appliances. You don't need to take any action: your existing appliances continue to boot and function normally, and new appliances that you deploy automatically include the updated Secure Boot certificates.

## Secure Boot certificates and expiration dates

Microsoft manages the UEFI Secure Boot certificates used to validate bootloader signatures during the VM boot process. The following sections list the expiring 2011 certificates and the newer 2023 certificates that replace them.

### Expiring certificates

The following table describes the final expiration date for the old Secure Boot certificates:

Certificate name | Role | Expiration date  
---|---|---  
Microsoft Corporation UEFI CA 2011 | Signs third-party bootloaders, such as the Linux Shim | June 27, 2026  
Microsoft Windows Production PCA 2011 | Signs the Windows bootloader | October 19, 2026  
Microsoft Corporation KEK CA 2011 | Used to update the DB and DBX | June 24, 2026  
  
### New certificates

The following table describes the final expiration date for the new Secure Boot certificates:

Certificate name | Role | Expiration date  
---|---|---  
Microsoft UEFI CA 2023 | Signs third-party bootloaders, such as the Linux Shim | Jun 13, 2038  
Windows UEFI CA 2023 | Signs the Windows bootloader | Jun 13, 2035  
Microsoft Corporation KEK 2K CA 2023 | Used to update the DB and DBX | Mar 2, 2038  
Microsoft Option ROM UEFI CA 2023 | Signs UEFI drivers and Option ROMs | Oct 26, 2038  
  
This certificate expiration only affects you if your compute instance meets both of the following mandatory prerequisites:

  1. **Creation date:** You created the compute instance before November 7, 2025 (when Compute Engine updated the default Secure Boot certificates in the UEFI firmware) and you haven't updated it.
  2. **Secure Boot state:** You enabled Secure Boot on the instance. Google Cloud doesn't enable Secure Boot by default when you create a Shielded VM instance.



Instances you create on or after November 7, 2025, already include the updated certificates in their firmware variables, provided they use an image that relies on the default certificate set.

If your instance doesn't meet both prerequisites, the certificate expiration doesn't affect it, and you don't need to take action.

This document explains how to identify affected instances and perform the necessary updates.

Google Cloud finished rolling out the new certificates on November 7, 2025. Instances you create on or after this date from images that rely on the default set of certificates include the updated certificates in their NVRAM/firmware variables (`db` and `KEK`) and don't require further action. However, some instances you created in the weeks before this date might also include the new certificates. To check if your system is current, use the commands in the Verification section of this document.

**Note:** The Secure Boot certificate expiration doesn't affect the following:

  * Instances that don't have Secure Boot enabled. Note that if you use vTPM Platform Configuration Registers (specifically `PCR7`) for secret sealing, any updates to UEFI variables or recreating the instance will still alter `PCR7` measurements even with Secure Boot disabled, though such configurations are very rare.
  * Instances running Container-Optimized OS (COS).
  * Instances where you use custom Secure Boot variables (such as a custom `PK`, `KEK`, or `db`) and your bootloader is signed using your own custom certificate rather than the expiring Microsoft Corporation UEFI CA 2011. If you use custom keys but still rely on the expiring Microsoft CA to sign your bootloader, see Instances with custom PK or KEK configurations for key update requirements.
  * Google Cloud Backup and DR appliances. These are managed appliances. The certificate expiration doesn't affect your appliances' operation, and you don't need to manually update them. Google Cloud automatically manages all certificate updates.



For compute instances created before November 7, 2025 that don't have the updated certificates, follow the [KEK and db update guide](https://docs.cloud.google.com/compute/docs/security/ms-secure-boot-certificates-update) to update the certificates; if for whatever reason you can't do that, consider recreating your instances.

## How Secure Boot certificate expiration affects Shielded VM

If enabled, Shielded VM enforces Secure Boot using UEFI firmware, which maintains a set of trusted certificates (in the `db` variable) to verify boot sequence binaries' signatures. If, for example, an OS update replaces a bootloader with one signed only by Microsoft UEFI CA 2023, and the compute instance's firmware doesn't trust this certificate's authority, Secure Boot verification fails, and Secure Boot stops the boot process.

For more details on this transition, see guidance from Microsoft and other OS vendors:

  * [Windows Secure Boot certificate expiration and CA updates - Microsoft Support](https://support.microsoft.com/en-us/topic/windows-secure-boot-certificate-expiration-and-ca-updates-7ff40d33-95dc-4c3c-8725-a9b95457578e)
  * [Secure Boot Certificate Changes in 2026: Guidance for RHEL Environments - Red Hat Customer Portal](https://access.redhat.com/articles/7128933)



## Operating system impact

If you enabled Secure Boot on a Shielded VM instance created before November 7, 2025, we recommend that you ensure that the 2023 certificates are installed; otherwise, the compute instance will face boot issues if you apply an update containing a bootloader signed only by the Microsoft UEFI CA 2023 certificate (and not dual-signed with the 2011 certificate). If you take no action, you might not be able to apply future bootloader or kernel updates containing binaries signed only with the 2023 certificate. Note that because OS vendors plan to dual-sign bootloader and shim updates with both the 2011 and 2023 certificates for the foreseeable future, boot failures or update blocks are not expected to occur immediately. For compute instances created prior to November 7, 2025: Windows customers might see Event ID 1801 ("Secure Boot CA/keys need to be updated") in the System event log if they haven't applied the certificate updates.

  * **Google-provided public images:** Update DB and KEK certificates by following the [KEK and db update guide](https://docs.cloud.google.com/compute/docs/security/ms-secure-boot-certificates-update). Alternatively, consider recreating any long-running VMs created before November 7, 2025.
  * **Custom or imported images:** The vast majority of custom or imported images rely on default Secure Boot certificates. If you didn't explicitly override the `db` or `KEK` Secure Boot variables when you created the image, the image uses the default key set and requires no action at the image level. Compute Engine automatically provides the updated certificates when you create an instance from any image that relies on these defaults.

You only need to take action if you explicitly defined custom `db` or `KEK` Secure Boot variables (for example, to include a third-party security vendor's certificate alongside the default Microsoft certificates) in the image metadata during your image build process. Because specifying a custom `db` or `KEK` variable overrides the defaults completely (and the system ignores the default public keys), your custom variables might lack the updated "Microsoft UEFI CA 2023" or 2023 KEK certificates. If your custom image configuration excludes these updated certificates, you must recreate or update your Shielded image to include them. For instructions, see [Creating custom Shielded VM images](https://docs.cloud.google.com/compute/shielded-vm/docs/creating-shielded-images).




## Recommended actions

If you have compute instances that were created before November 7, 2025, with Secure Boot enabled, review the following requirements, limitations, and complicating factors before planning your update path:

  * **Pre-update requirements:**
    * **Verify recovery key access:** If your instances use FDE (including BitLocker on Windows or LUKS on Linux), you must ensure you have access to your recovery keys before updating certificates or recreating instances. Modifying UEFI variables alters boot measurements and will trigger recovery prompts.
    * **Manage vTPM secrets:** If your instances use vTPM Platform Configuration Registers (specifically `PCR7`) for secret sealing, you must unseal or back up these secrets before updating to prevent permanently losing access.
  * **Complicating factors and boundaries:**
    * **Update order requirement:** To prevent CA verification failures and system boot loops, you must install the new `db` and `KEK` certificates before you apply new kernel or shim updates.
    * **Firmware rollbacks:** Restoring an instance to a legacy machine image captured before November 7, 2025, restores the old firmware and removes trust for the 2023 certificates. If you roll back, you must re-apply the certificate updates.



For a detailed breakdown of timelines, audit steps, and migration processes, review the following instructions.

### Impact on specific guest configurations

Understand how the certificate expiration affects each configuration only if your instance meets both mandatory prerequisites (you created it before November 7, 2025, and it has Secure Boot enabled):

  * **vTPM PCR secret sealing:**
    * **When it becomes a factor:** When you use vTPM Platform Configuration Registers (specifically `PCR7`) to seal secrets, such as decryption keys.
    * **Impact:** Updating Secure Boot certificates (either by using the [KEK and db update guide](https://docs.cloud.google.com/compute/docs/security/ms-secure-boot-certificates-update) or by recreating the instance from a disk snapshot) modifies UEFI variables, changing the `PCR7` measurement value at the next boot. This change prevents the guest OS or applications from unsealing or decrypting these secrets unless you first unseal or back up the secrets before the update, and then re-seal them to the new `PCR7` value afterward.
    * **When unaffected:** If you created the VM on or after November 7, 2025, from an image relying on the default certificates, you don't need to update the certificates, `PCR7` remains unchanged, and secret sealing behaves normally.
  * **Windows compute instances using BitLocker or Virtual Secure Mode (VSM):**
    * **When it becomes a factor:** When your Windows VMs use BitLocker full disk encryption or VSM, both of which trust UEFI Secure Boot and `PCR7` to seal their encryption keys.
    * **Impact:** Modifying UEFI Secure Boot certificates—or recreating the instance from a snapshot—changes the `PCR7` boot measurements. On the subsequent reboot, BitLocker detects the configuration change, fails to automatically release the key, and boots to a _BitLocker Recovery screen_ requesting the recovery key.
    * **Remediation:** You must verify you have your BitLocker recovery keys available before updating certificates or migrating instances. Afterwards, follow the guidance in [Update db and KEK on Windows](https://docs.cloud.google.com/compute/docs/security/ms-secure-boot-certificates-update#update_db_and_kek_on_windows).
    * **When unaffected:** The certificate expiration doesn't affect Windows instances without BitLocker or VSM enabled, or those without Secure Boot enabled.
  * **Linux VMs using FDE:**
    * **When it becomes a factor:** When your Linux instances use FDE, such as LUKS, where you seal the decryption keys to vTPM PCRs (specifically `PCR7`).
    * **Impact:** Updating the Secure Boot certificates or recreating the VM alters `PCR7`, preventing automated decryption of the boot volume. The system halts during boot and prompts you for a decryption passphrase.
    * **Remediation:** Confirm you have the recovery passphrases or keys before running updates. Unbind or unseal the LUKS keys from the TPM before the update, and re-bind or re-seal them to the new `PCR7` value after completing the update.
    * **When unaffected:** The certificate expiration doesn't affect Linux VMs that don't use FDE or vTPM-sealed LUKS decryption, or those that don't have Secure Boot enabled.
  * **Instances with custom PK or KEK configurations:**
    * **When it becomes a factor:** When your instance uses custom Secure Boot variables (such as a custom `PK` or `KEK`) on the system, but still relies on standard Microsoft certificates in the database (`db`) to sign your bootloader.
    * **Impact:** A standard `db` certificate update is required to boot subsequent bootloader updates signed only by Microsoft UEFI CA 2023. However, because you use custom keys, the standard update files (`DBUpdate3P2023.bin` or `kek2023update.bin`) provided in Google's guide will fail to apply. The UEFI firmware checks the signature and requires updates to be signed by the private key of the `KEK` (or `PK`) present on the system.
    * **Remediation:** You must sign the certificate update files using the private keys associated with your custom `PK` or `KEK` before applying them, or manage these updates through your custom certificate authority.
    * **When unaffected:** If your bootloader is signed with your own custom certificate authority or keys (like a custom `db` certificate, and not the expiring Microsoft Corporation UEFI CA 2011), then the expiration of Microsoft's default certificates doesn't affect you, and you don't need to perform any updates.
  * **Instances that roll back to a pre-November 2025 machine image:**
    * **When it becomes a factor:** When you restore or roll back a VM to a machine image captured before November 7, 2025, with Secure Boot enabled.
    * **Impact:** The rolled-back instance restores the older UEFI firmware configuration and certificate store which lacks the 2023 certificates. This makes the instance vulnerable to future boot failures after subsequent bootloader updates, requiring you to re-apply the certificate updates.
    * **When unaffected:** Rolling back to a machine image doesn't affect the instance if you disable Secure Boot, or if you created the machine image on or after November 7, 2025, from an image relying on the default certificates.



### Identify affected compute instances and plan for update

Throughout 2026, we recommend that you identify the affected compute instances, and take the following steps to prepare for the update:

  1. **Identify instances:** You can use the [`gcloud compute instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list) to identify instances that have Secure Boot enabled and were created before the cutoff date:
         
         gcloud compute instances list \
         --filter="creationTimestamp < '2025-11-07' AND shieldedInstanceConfig.enableSecureBoot=true" \
         --format="table(name, zone, creationTimestamp, shieldedInstanceConfig.enableSecureBoot:label=SECURE_BOOT)"
         

  2. **Check for custom variables (Optional):** If you use custom or imported images, verify if they explicitly define custom `db` or `KEK` Secure Boot variables (which completely override the defaults). If they rely on default certificates, they require no action at the image level:

     * To check a **VM instance** , run:
           
           gcloud compute instances describe INSTANCE_NAME \
               --zone=ZONE \
               --format="yaml(shieldedInstanceInitialState)"
           

     * To check a **source disk image** , run:
           
           gcloud compute images describe IMAGE_NAME \
               --format="yaml(shieldedInstanceInitialState)"
           

If the output is empty or returns `null`, the instance or image uses the default certificates and requires no action at the image level.

  3. **Ensure data integrity:** Ensure you have recent data backups and access to FDE or BitLocker recovery keys before you proceed with any changes.

  4. **Update certificates:** Update DB and KEK certificates by following the [KEK and db update guide](https://docs.cloud.google.com/compute/docs/security/ms-secure-boot-certificates-update). Alternatively, migrate to a compute instance that you create on or after November 7, 2025, which includes the 2023 certificates (provided the new instance uses an image that relies on the default certificates), by following the instructions in Recreate a compute instance from a disk snapshot.




### Recreate a compute instance from a disk snapshot

When you take a disk snapshot and create a new instance from it, the new compute instance inherits a fresh firmware (vTPM/NVRAM) state that trusts the updated defaults and clears out old certificates.

Before recreating a compute instance from a snapshot, ensure that the guest OS has all the necessary updates installed (such as relevant Microsoft KBs for Windows, or the latest Shim for Linux distributions) to trust the 2023 certificates.

You can use the following sequence of `gcloud` commands to manage this migration:

  1. **Identify the boot disk:** Determine the name of the boot disk attached to your source compute instance:
         
         SOURCE_DISK=$(gcloud compute instances describe SOURCE_INSTANCE_NAME \
             --zone=ZONE \
             --format="value(disks[0].source.basename())")
         

  2. **Create a disk snapshot:** Take a snapshot of that boot disk. For optimal data integrity, stop the compute instance before running this command:
         
         gcloud compute disks snapshot $SOURCE_DISK \
             --snapshot-names="migration-snapshot-$(date +%s)" \
             --zone=ZONE \
             --storage-location=REGION
         

  3. **Create a new compute instance:** Provision a fresh compute instance by using the snapshot as the boot source. If Secure Boot is enabled on the source instance, include the `--shielded-secure-boot` flag to enable Secure Boot on the new instance.
         
         gcloud compute instances create NEW_INSTANCE_NAME \
             --zone=ZONE \
             --machine-type=MACHINE_TYPE \
             --create-disk=name=NEW_DISK_NAME,source-snapshot=SNAPSHOT_NAME,boot=yes \
             --shielded-secure-boot
         




**Note:** Instances provisioned using this approach receive new internal and external IP addresses unless statically allocated and specifically reassigned. Instance-level metadata, tags, and service accounts aren't automatically replicated and must be configured explicitly during recreation.

## Verification

After updating the firmware and OS for your compute instances, you can verify that the 2023 certificates are present. If both the `KEK` and `db` variables show the 2023 certificates are present, your instance is up to date and no further action is required.

Regardless of which tool was used to apply the updates (such as `fwupd`, `efitools`, or `sbsigntool`), the certificates are stored in the instance's UEFI NVRAM variables. You can verify them directly from the guest operating system.

### Linux

You can verify the signature databases on Linux by using `mokutil` (recommended and available by default on most distributions) or `efi-readvar` (from the `efitools` package).

#### Method 1: Using `mokutil` (Recommended)

`mokutil` is installed by default on most Linux distributions that support UEFI Secure Boot (including Debian, Ubuntu, RHEL, CentOS, Rocky Linux, AlmaLinux, SLES, openSUSE, and Fedora).

Check for the 2023 certificates in the `KEK` and `db` variables:
    
    
    sudo mokutil --kek | grep "KEK 2K CA 2023"
    sudo mokutil --db | grep "UEFI CA 2023"
    

To view full certificate details (such as issuer, subject, and expiration dates), run `sudo mokutil --kek` or `sudo mokutil --db` without filtering.

#### Method 2: Using `efi-readvar`

If you prefer using `efi-readvar`, ensure the `efitools` package is installed:

  * **Debian or Ubuntu**
        
        sudo apt update && sudo apt install efitools -y
        

  * **Fedora** (`efitools` is not available in standard RHEL/CentOS repositories)
        
        sudo yum install efitools -y
        

  * **SLES or openSUSE**
        
        sudo zypper install efitools -y
        




Check for the certificates in the `KEK` and `db` variables:
    
    
    sudo efi-readvar -v KEK | grep "KEK 2K CA 2023"
    sudo efi-readvar -v db | grep "UEFI CA 2023"
    

### Windows (PowerShell)

Run the following in an administrator PowerShell prompt. Each command should return `True`.
    
    
    # Check for Microsoft KEK 2K CA 2023
    [System.Text.Encoding]::ASCII.GetString((Get-SecureBootUEFI KEK).bytes) -match 'Microsoft Corporation KEK 2K CA 2023'
    
    # Check for UEFI CA 2023
    [System.Text.Encoding]::ASCII.GetString((Get-SecureBootUEFI db).bytes) -match 'UEFI CA 2023'
    
    # Confirm general Secure Boot enrollment state
    Confirm-SecureBootUEFI
    

## Troubleshooting

If an instance fails to boot due to a Secure Boot error after June 2026, try one of the following options to recover it:

  * **Temporarily disable Secure Boot:** This lets you boot the instance to apply updates.

**Caution:** Disabling Secure Boot changes the PCR values, specifically `PCR7`, which might affect secret sealing or disk encryption functionality.

To disable Secure Boot, run the following command:
        
        gcloud compute instances update INSTANCE_NAME --no-shielded-secure-boot
        

After applying necessary updates to the bootloader/shim, re-enable Secure Boot:
        
        gcloud compute instances update INSTANCE_NAME --shielded-secure-boot
        

  * **Restore from backup:** Restore the instance from a machine image created before boot issues began.

  * **Recreate instance:** Recreate the instance and recover data from a snapshot.




If you continue to encounter issues or need help, contact Cloud Customer Care.

## Frequently asked questions (FAQ)

This section provides answers to common questions about the Microsoft Secure Boot certificate expiration.

### When do Secure Boot certificates expire?

Microsoft's Secure Boot certificates are expiring in 2026. Specifically:

  * The two most critical certificates nearing their end of life are the Microsoft Corporation UEFI CA 2011 (expires in June 2026), which signs third-party bootloaders such as the Linux Shim, and the Microsoft Windows Production PCA 2011, which expires in October 2026 and signs the Windows bootloader.



### Who is affected by the certificate expiration?

This certificate expiration only affects you if your compute instance meets both of the following mandatory prerequisites:

  1. You created the instance before November 7, 2025—when Compute Engine updated the default Secure Boot certificates in the UEFI firmware—and you haven't updated it.
  2. You enabled Secure Boot on the instance.



Instances you create on or after November 7, 2025, aren't affected, provided you create them from an image that relies on the default certificate set.

If your instance meets both prerequisites, the certificate expiration affects the following configurations under specific circumstances:

  * **vTPM PCR secret sealing:** If the instance uses Virtual Trusted Platform Module (vTPM) Platform Configuration Registers (specifically `PCR7`) to seal encryption keys or secrets.
  * **Windows BitLocker / VSM:** If your Windows instance uses BitLocker disk encryption or Virtual Secure Mode (VSM) with Secure Boot.
  * **Linux FDE:** If your Linux instance uses FDE that you seal to vTPM PCRs (specifically `PCR7`).
  * **Rollback instances:** If you restore or roll back the VM to a machine image that you created before November 7, 2025.



For a detailed breakdown of the impact and remediation steps for each of these configurations, see Impact on specific guest configurations.

### Who is not affected by the certificate expiration?

The certificate expiration doesn't affect you if any of the following apply:

  * **Secure Boot is disabled:** If Secure Boot isn't enabled on your Shielded VM instance, it doesn't validate or use the UEFI certificates that are expiring. Secure Boot is disabled by default. However, note that if you use vTPM Platform Configuration Registers (specifically `PCR7`) for secret sealing, any updates to UEFI variables or recreating the instance will still alter `PCR7` measurements even with Secure Boot disabled, though such configurations are very rare.
  * **Created on or after November 7, 2025:** You created the instance on or after this date, so its firmware already includes the updated 2023 certificates, provided you created it from an image that relies on the default certificate set.
  * **Running Container-Optimized OS (COS):** These certificate updates don't affect COS environments.
  * **Custom PK, KEK, or db variables:** If you explicitly define and manage your own custom Secure Boot `PK`, `KEK`, or `db` variables without relying on the default Microsoft UEFI certificates (for example, if your bootloader is signed using your own custom `db` certificate rather than the expiring Microsoft Corporation UEFI CA 2011), the expiration of default certificates doesn't affect you.

If your custom configuration still relies on the expiring Microsoft certificate to sign your bootloader, you are affected by the expiration. However, because you use a custom `PK` or `KEK`, the standard update files (`DBUpdate3P2023.bin` or `kek2023update.bin`) provided in this guide will fail because UEFI requires updates to be signed by the private key of the `KEK` (or `PK`) present on the system. You must sign the certificate update files with the private keys of your custom `PK` or `KEK` to apply them.




### Does this expiration affect Managed Service for Apache Spark (formerly Dataproc), Dataflow, or Vertex AI Workbench instances?

This certificate expiration doesn't affect Dataflow because its instances run on Container-Optimized OS (COS) by default. These certificate updates don't affect COS environments.

For Managed Service for Apache Spark (formerly Dataproc) and Vertex AI Workbench instances, this expiration only affects you if your instances meet both of the following mandatory prerequisites:

  1. You created the instances before November 7, 2025.
  2. You enabled Secure Boot on the instances. These services don't enable Secure Boot by default.



If your instances meet both prerequisites, the certificate expiration affects them. However, there is no immediate impact because OS vendors plan to dual-sign bootloader and shim updates for the foreseeable future. Your instances are unaffected unless you install a future update that is signed only with the 2023 certificate.

### What happens if I take no action?

If you take no action, your instance continues to boot and operate as normal with its existing binaries. However, you might not be able to apply future bootloader or kernel updates containing binaries signed only with the 2023 certificate. Note that because OS vendors dual-sign bootloader and shim updates with both the 2011 and 2023 certificates, boot failures or update blocks are not expected to occur immediately.

### Will failing to update certificates prevent Windows instances from booting?

No. Failure to remediate won't prevent Windows system startup. However, you might see Event ID 1801 ("Secure Boot CA/keys need to be updated") in the System event log, and you won't be able to apply new kernel or bootloader security updates containing binaries signed only with the new 2023 certificate.

### What specific conditions trigger boot failures on Linux?

A boot failure may happen on Linux under specific conditions:

  * The instance has Secure Boot enabled.
  * The db UEFI variable isn't updated to trust the "Microsoft UEFI CA 2023" certificate.
  * The OS updates a bootloader (or shim) that relies strictly on that certificate (and is not dual-signed with the 2011 certificate).



If you don't apply certificate updates or shim updates that reference the new certificates, your Linux instance will continue to boot successfully.

### How do I determine if my instance has the updated certificates?

To determine if your instance includes the new certificates in its firmware, refer to the commands outlined in the Verification section. If certificates are missing, you can update them by following the [KEK and db update guide](https://docs.cloud.google.com/compute/docs/security/ms-secure-boot-certificates-update), or recreate the instance.

### Does restarting or rebooting an affected instance solve the issue?

No. Restarting or rebooting a compute instance doesn't update its secure boot certificates, but the instance continues to boot and operate normally with its existing certificates until a bootloader or kernel update is applied that contains binaries signed only with the 2023 certificate. If you restart the compute instance, it retains the old certificates if it was originally created before November 7, 2025. The certificates are part of the instance's firmware (vTPM/NVRAM). Therefore, you need to follow the [KEK and db update guide](https://docs.cloud.google.com/compute/docs/security/ms-secure-boot-certificates-update) or recreate the instance to apply the new certificates.

### How should I prepare for the certificate expiration?

To prepare, take the following steps:

  * **Identify:** Audit your usage of Shielded VMs, Secure Boot, FDE, BitLocker, or any software that relies on vTPM PCRs.
  * **Recovery keys & backups:** Ensure prompt availability of recovery keys (for FDE/BitLocker) and latest data backups.
  * **Manage images:** Identify legacy custom images and discontinue their usage or ensure they include the new certificates.
  * **Update or migrate:** If you want to update certificates, refer to the [KEK and db update guide](https://docs.cloud.google.com/compute/docs/security/ms-secure-boot-certificates-update). Alternatively, consider recreating any long-running compute instances that you created prior to November 7, 2025, as new instances already include the necessary certificates (provided you create the new instance from an image that relies on the default certificates).



### What are the recommended methods for recreating or migrating affected instances?

Standard disk snapshots provide the most reliable method. A snapshot is a block-level copy of the disk and contains no UEFI variables or instance-level metadata. To restore using a snapshot, do the following:

  1. Create a snapshot of the instance's boot disk.
  2. Create a new compute instance and select the snapshot as the source for the boot disk.



You shouldn't use machine images, instance cloning, or Backup and DR Service backups for this migration because they replicate the instance firmware and retain the old certificates for any source compute instance created before November 7, 2025.

### What should I do if my system stops booting after June 2026?

If you believe this issue caused a boot failure, see Troubleshooting.

### How is Google Cloud handling the Microsoft Secure Boot certificates expiration?

Google Cloud automatically included the new certificates for compute instances created after November 7, 2025. Only customers who want to keep their pre-November 7, 2025, compute instances running might need to apply a future update, but we recommend migrating to an instance you create on or after November 7, 2025 (relying on default certificates).

## What's next

  * Learn more about [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm).
  * Learn how to [modify Shielded VM options](https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm).
  * Learn more about [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
