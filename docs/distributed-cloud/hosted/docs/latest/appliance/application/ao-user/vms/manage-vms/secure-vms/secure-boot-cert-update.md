---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/secure-vms/secure-boot-cert-update/
title: Update Secure Boot certificates on a VM \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:33.860497+00:00
---

# Update Secure Boot certificates on a VM  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vms/secure-vms/secure-boot-cert-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Update Secure Boot certificates on a VM Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to renew Unified Extensible Firmware Interface (UEFI) Secure Boot certificates on a virtual machine (VM) in Google Distributed Cloud (GDC) air-gapped appliance.

UEFI Secure Boot is a security feature that ensures VM systems run authentic software by verifying the digital signature of all boot components. If verification fails, Secure Boot stops the VM boot process.

Microsoft uses security certificates to support Secure Boot across various operating systems. Some Secure Boot certificates are nearing their expiration date. To avoid system disruption, you must renew these certificates.

This document is for developers in platform administrator or application operator groups that configure Secure Boot on VMs in a GDC air-gapped appliance environment.

## Before you begin

All commands for GDC air-gapped appliance use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment. Ensure you download, install, and configure the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview).

### Get the kubeconfig file

To run commands against the management API server, ensure you have the following resources:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#cli) the kubeconfig file for the management API server if you don't have one.

  2. Use the path to the kubeconfig file of the management API server to replace `MANAGEMENT_API_SERVER` in these instructions.




### Request IAM roles

To update Secure Boot certificates on your VM, contact your Project IAM Admin to request the **Virtual Machine Project Admin** (`project-vm-admin`) role.

All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#verify-user-access) your access.

## Secure Boot certificates

All Secure Boot certificates have an expiration date. VMs with expired certificates will boot normally until you install the first security update for Windows Boot Manager or Linux shim. After any of those updates, the VM will fail to boot until you update the expired certificate.

Any newly created VMs in version 1.0.6 and later will automatically include the new certificates. However, you must perform the certificate renewal annotation process to any existing, long-running VMs created earlier than version 1.0.6.

### Expiring certificates

The following table describes the final expiration date for the old Secure Boot certificates:

Certificate name | Certifcate expiration date  
---|---  
Microsoft Corporation KEK CA 2011 | June 26, 2026  
Microsoft UEFI CA 2011 | June 26, 2026  
Microsoft Windows Production PCA 2011 | October 19, 2026  
  
### New certificates

The following table describes the final expiration date for the new Secure Boot certificates:

Certificate name | Certifcate expiration date  
---|---  
Microsoft UEFI CA 2023 | Jun 13, 2038  
Microsoft Corporation KEK 2K CA 2023 | Mar 2, 2038  
Microsoft Option ROM UEFI CA 2023 | Oct 26, 2038  
Windows UEFI CA 2023 | Jun 13, 2035  
  
## Certificate renewal process

To perform a Secure Boot certificate renewal on a VM, you must opt-in using annotations and a controlled update. All new VMs created with old or new images after the update will have both certificates installed and will boot successfully.

**Warning:** Automated rollout can result in locking BitLocker-enabled VMs. Don't perform an automated rollout unless you have verified you're not using Bitlocker, Luks, or any other disk encryption tool. Follow the steps in the Special Handling: BitLocker & FDE section to perform certificate renewal on BitLocker-enabled VMs.

### Identify VMs and apply annotation

Identify affected VMs within a namespace or project. Once identified, apply the update annotation to the affected VM instances.

  1. Use `kubectl` to check the `enableSecureBoot` status:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER get vms --all-namespaces -o \
             custom-columns="NAMESPACE:.metadata.namespace,NAME:.metadata.name,SECURE_BOOT:.spec.shieldConfig.enableSecureBoot"
         

**Warning:** For VMs with BitLocker, LUKS or any type of FDE enabled, follow the steps in the Special Handling: BitLocker & FDE section before adding an Annotation.
  2. Apply the annotation to the VM custom resource to mark the VM as ready for update. This enrolls certificates during the next VM reboot:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER annotate virtualmachine VM_NAME -n VM_NAMESPACE virtualmachine.gdc.goog/enable-microsoft-2023-sbcert="true" --overwrite
         

Replace the following variables:

     * `VM_NAME`:The name of the VM instance.
     * `VM_NAMESPACE`: The name of the namespace where the VM resides.
  3. Bulk apply the annotation to all VMs in a project:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER annotate virtualmachine --all -n VM_NAMESPACE virtualmachine.gdc.goog/enable-microsoft-2023-sbcert="true" --overwrite
         

You can bulk apply the annotation label across all VMs in an organization as long as disk encryption isn't in use.

At the project-level, project owners can apply the label individually to eligible VMs.

  4. To apply your changes, restart your VM:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER patch VirtualMachine VM_NAME -n VM_NAMESPACE -p '{"spec":{"runningState":"Stopped"}}' --type=merge
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER patch VirtualMachine VM_NAME -n VM_NAMESPACE -p '{"spec":{"runningState":"Running"}}' --type=merge
         




## Special Handling: BitLocker & FDE

**Note:** If you enabled BitLocker, LUKS or any type of FDE on your VM, ensure you have recovery keys and backup data available.

You must perform the following tasks:

  1. Temporarily disable BitLocker, LUKS or any similar encryption solution.
  2. Ensure recovery keys are readily available and backups are current.
  3. Apply the Secure Boot update annotation mentioned in step 2 of the certificate renewal process section.
  4. Reboot the VM to enroll certificates.
  5. Re-enable BitLocker, LUKS, or FDE after you verify the update.



### Disable BitLocker

Before applying the `"virtualmachine.gdc.goog/enable-microsoft-2023-sbcert"` annotation, you must disable BitLocker on your VM. This requires disk decryption. Wait for the decryption process to complete before applying the annotation.

Use the following script to disable BitLocker:

**`disable_bitlocker.ps1`**
    
    
       # Log start time
       Add-Content -Path C:\disable_bitlocker_log.txt -Value "Script started at $(Get-Date)"
    
       # Get all BitLocker volumes
       $BitLockerVolumes = Get-BitLockerVolume
    
       if ($BitLockerVolumes) {
           foreach ($Volume in $BitLockerVolumes) {
               Add-Content -Path C:\disable_bitlocker_log.txt -Value "Processing volume: $($Volume.MountPoint)"
               if ($Volume.ProtectionStatus -eq 'On') {
                   Add-Content -Path C:\disable_bitlocker_log.txt -Value "Disabling BitLocker on $($Volume.MountPoint)"
                   try {
                       Disable-BitLocker -MountPoint $Volume.MountPoint -ErrorAction Stop
                       Add-Content -Path C:\disable_bitlocker_log.txt -Value "Successfully initiated BitLocker disable on $($Volume.MountPoint). Decryption may take time."
                   } catch {
                       Add-Content -Path C:\disable_bitlocker_log.txt -Value "ERROR disabling BitLocker on $($Volume.MountPoint): $($_.Exception.Message)"
                   }
               } else {
                   Add-Content -Path C:\disable_bitlocker_log.txt -Value "BitLocker is already Off or Unprotected on $($Volume.MountPoint)"
               }
           }
       } else {
           Add-Content -Path C:\disable_bitlocker_log.txt -Value "No BitLocker volumes found."
       }
    
       # Log end time
       Add-Content -Path C:\disable_bitlocker_log.txt -Value "Script finished at $(Get-Date)"
    

#### Add the `disable_bitlocker.ps1` script to a VM startup script

To disable BitLocker on VM restart, you can run this script in a running VM, or add it to your startup script. Follow the steps to use this script as startup script.

  1. Base Encode the script and create a kubernetes secret:
         
         # Encode the script
         B64_SCRIPT=$(base64 -w 0 disable_bitlocker.ps1)
         
         # Create Secret YAML
         cat <<EOF > disable_bitlocker_secret.yaml
         apiVersion: v1
         kind: Secret
         metadata:
           name: disable-bitlocker-script
           namespace: VM_NAMESPACE
         type: Opaque
         data:
           script: $B64_SCRIPT
         EOF
         
         # Apply the Secret to the GDCer
         kubectl --kubeconfig MANAGEMENT_API_SERVER -f disable_bitlocker_secret.yaml
         

  2. Patch the VM CR to add the `disable-bitlocker.ps1` script to the startup script `spec` field:
         
         spec:
           # ... other existing spec fields ...
           osType: Windows
           startupScripts:
             - name: disable-bitlocker-ps1 # Note the -ps1 suffix
               scriptSecretRef:
                 name: disable-bitlocker-script
         

  3. Restart the VM:

     * Stop the VM:
           
           kubectl --kubeconfig MANAGEMENT_API_SERVER patch VirtualMachine VM_NAME -n VM_NAMESPACE -p '{"spec":{"runningState":"Stopped"}}' --type=merge
           

     * Start the VM:
           
           kubectl --kubeconfig MANAGEMENT_API_SERVER patch VirtualMachine <vm-name> -n VM_NAMESPACE -p '{"spec":{"runningState":"Running"}}' --type=merge
           




### Check the BitLocker status

**Important:** Ensure the decryption process completes before you apply the Secure Boot update annotation.

To verify that the volume is fully decrypted before proceeding, check the BitLocker status using either one of the following PowerShell commands:

  * Check the status of all drives:
        
        Get-BitLockerVolume
        

  * Check the status of a specific drive:
        
        Get-BitLockerVolume -MountPoint "C:"
        




Alternatively, you can check the status of all drives using the `manage-bde` command:
    
    
    manage-bde -status
    

The output of a disabled BitLocker looks similar to the following image:

![A PowerShell CLI screen with a BitLocker False status after running manage-bde -status](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/images/bitlocker-disabled-PS.png)

### Optional: Verification

If you want to verify the certificates present on your VM, follow the steps for your corresponding OS:

###  Linux 

  1. Use `mokutil` to verify Secure Boot is enabled on your machine:
         
         user@vm1:~$ mokutil --sb-state
         

If Secure Boot is enabled, the output looks similar to the following:
         
         SecureBoot enabled
         

  2. Use the appropriate flag with the `mokutil` command, and narrow your search to the specific certificate year using `grep`.

**2023 certificates** :
         
         user@vm1:~$ mokutil --kek | grep 2023
         

The output is similar to the following:
         
         Not Before: Mar  2 20:21:35 2023 GMT
             Subject: C=US, O=Microsoft Corporation, CN=Microsoft Corporation KEK 2K CA 2023
         
         
         user@vm1:~$ mokutil --db | grep 2023
         

The output is similar to the following:
         
         Not Before: Jun 13 19:21:47 2023 GMT
             Subject: C=US, O=Microsoft Corporation, CN=Microsoft UEFI CA 2023
             Not Before: Jun 13 18:58:29 2023 GMT
             Subject: C=US, O=Microsoft Corporation, CN=Windows UEFI CA 2023
         

**2011 certificates** :
         
         user@vm1:~$ mokutil --kek | grep 2011
         

The output is similar to the following:
         
         Not Before: Jun 24 20:41:29 2011 GMT
             Subject: C=US, ST=Washington, L=Redmond, O=Microsoft Corporation, CN=Microsoft Corporation KEK CA 2011
         
         
         user@vm1:~$ mokutil --db | grep 2011
         

The output is similar to the following:
         
         Not Before: Oct 19 18:41:42 2011 GMT
             Subject: C=US, ST=Washington, L=Redmond, O=Microsoft Corporation, CN=Microsoft Windows Production PCA 2011
             Not Before: Jun 27 21:22:45 2011 GMT
             Subject: C=US, ST=Washington, L=Redmond, O=Microsoft Corporation, CN=Microsoft Corporation UEFI CA 2011
         




###  Windows 

  1. Verify Secure Boot certificates are present on the system:
         
         PS C:\Windows\system32> Confirm-SecureBootUEFI
         

If the certificate is present on your machine, the output is `True`.

  2. Use the `-match` flag to append the command with the applicable certificate year:
         
         PS C:\Windows\system32> [System.Text.Encoding]::ASCII.GetString((Get-SecureBootUEFI KEK).bytes) -match "2023"
         PS C:\Windows\system32> [System.Text.Encoding]::ASCII.GetString((Get-SecureBootUEFI KEK).bytes) -match "2011"
         PS C:\Windows\system32> [System.Text.Encoding]::ASCII.GetString((Get-SecureBootUEFI db).bytes) -match "2011"
         PS C:\Windows\system32> [System.Text.Encoding]::ASCII.GetString((Get-SecureBootUEFI db).bytes) -match "2023"
         




## Troubleshoot renewal issues

If renewal issues occur on an existing VM, rollback your changes by adding an annotation to the VM CR. The VM will boot with its previous, older certificates.

### Rollback changes

  1. Add the following annotation to your VM custom resource:

**Annotation** :
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER annotate virtualmachine VM_NAME -n VM_NAMESPACE virtualmachine.gdc.goog/recover-efi-backup="true" --overwrite
         

  2. Restart the VM to recover older certificates:

     * Stop the VM:
           
           kubectl --kubeconfig MANAGEMENT_API_SERVER patch VirtualMachine VM_NAME -n VM_NAMESPACE -p '{"spec":{"runningState":"Stopped"}}' --type=merge
           

     * Start the VM:
           
           kubectl --kubeconfig MANAGEMENT_API_SERVER patch VirtualMachine VM_NAME -n VM_NAMESPACE -p '{"spec":{"runningState":"Running"}}' --type=merge
           




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
