---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/chassis-firmware-upgrade/
title: Upgrade HPE Chassis Manager firmware \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:22.182344+00:00
---

# Upgrade HPE Chassis Manager firmware  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/chassis-firmware-upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Upgrade HPE Chassis Manager firmware Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps to upgrade the HPE Chassis Manager firmware to version 2.10.12 or later on your Google Distributed Cloud (GDC) air-gapped appliance.

## Before you begin

Before initiating the firmware upgrade, complete the following prerequisites:

  1. **Ensure power redundancy** : connect and verify both power cables to the appliance chassis power supplies to prevent accidental power loss during firmware flashing.

**Caution:** To prevent Chassis Manager firmware corruption, connect both power supply cables to the chassis for power redundancy and don't interrupt power during the upgrade process. A power loss while flashing eMMC partitions can corrupt the firmware.
  2. **Verify network access** : ensure the workstation or laptop is connected to the appliance management network and can reach the blade iLO and Chassis Manager IP addresses. You will connect to any compute blade iLO to mount the update ISO and to the Chassis Manager to verify firmware and set credentials:

     * **Node 1 (bm01) iLO** : `https://198.18.0.7`
     * **Node 2 (bm02) iLO** : `https://198.18.0.8`
     * **Node 3 (bm03) iLO** : `https://198.18.0.9`
     * **Chassis Manager** : `https://198.18.0.2`

If the endpoints are unreachable, ensure your workstation is configured with a static IP on the management subnet (see [Connect the laptop to the switch](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/connect-the-device)) or see [Troubleshoot appliance access issues](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-troubleshooting/appliance-inaccessibility).

  3. **Verify current firmware version** : query the Chassis Manager Redfish API (or check the web interface sign-in screen) to confirm whether the current version is older than `2.10.12` (such as factory version `2.2-b11`):
         
         curl -k -s "https://198.18.0.2/redfish/v1/" | jq -r '.Oem.Hpe.Manager[0].ManagerFirmwareVersion'
         

  4. **Locate or get the HPE hybrid update ISO** : verify that the bootstrapper is hosting the firmware update image:
         
         curl -I -s http://198.18.0.30:8080/gdch-hpe-firmware/el8000cm.flash | head -n 1
         

Expected output: `HTTP/1.1 200 OK`

_Alternative fallback:_ If unavailable, manually download the official update image to your local workstation from HPE: [EL8000CM_Updater_BI_2.10.12_App_2.10.12.hybrid.iso](https://support.hpe.com/connect/s/softwaredetails?language=en_US&collectionId=MTX-87e91973f2884613&tab=revisionHistory&softwareId=MTX_701e2fed1bc44f0381c5cbaee8).

  5. **Retrieve credentials** : get the administrator credentials for the server blade iLO:

     * **Unbootstrapped appliances** : retrieve the `server_bmc_username` and `server_bmc_password` from the `/root/gdch/support/devices.csv` file (see [Common bootstrapping issues](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/install/common-bootstrapping-issues#chassis-install-failure)).
     * **Bootstrapped appliances (upgrades)** : retrieve the iLO credentials from the `bmc-credentials-*` Kubernetes secrets in the `gpc-system` namespace (see [Shut down a blade](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/shutdown-a-blade) or [Shut down the device](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/shutdown)).



## Upgrade the Chassis Manager firmware

Follow these steps to flash the Chassis Manager firmware from a compute blade:

### Connect to blade iLO HTML5 console

  1. Open a web browser and navigate to any configured compute blade iLO (for example, `https://198.18.0.8`).
  2. Sign in using the administrator credentials.
  3. From the left navigation menu, click **Remote Console & Media** and launch the **HTML5 Remote Console**.

**Note:** If the remote console is disabled, go to the **Access Settings** page to enable the remote console feature before proceeding.



### Mount the HPE hybrid update ISO

  1. In the HTML5 Remote Console window, click **Virtual Media** in the top menu bar.
  2. Select **CD/DVD** and choose your preferred mounting method: 
     * **Primary method (GDCH Artifact Server)** : Select **Scripted Media URL** and enter the bootstrapper's artifact URL: `http://198.18.0.30:8080/gdch-hpe-firmware/el8000cm.flash`
     * **Alternative method (Local Upload)** : Select **Local *.iso File** , click **Browse** , and select the `EL8000CM_Updater_BI_2.10.12_App_2.10.12.hybrid.iso` file that you manually downloaded from HPE in the prerequisites.
  3. Ensure **Boot on Next Reset** is selected.
  4. Click **Insert Media**.
  5. Verify that the virtual media status shows **Connected**.



### Restart server blade and execute firmware update

  1. Restart the compute blade using the OS or using the iLO Power Controls (**Power & Thermal** > **Server Power** > **Reset** button).
  2. Open the console by clicking **Remote Console** > **Launch** > **HTML5 Console**.
  3. When prompted by the GNU GRUB bootloader menu, select **Live system (amd64)** and press **Enter** to begin the firmware update execution.

**Note:** To prevent corrupting the firmware during the 3-to-5-minute partition flashing process, don't interrupt power. Update progress is displayed live in the console.



### Reboot server blade and reset password

  1. When the installation completion screen appears, type `reboot` in the console to reboot the server blade.
  2. From the console menu, click **Virtual Media** and eject the CD-ROM.
  3. Wait approximately 2 to 3 minutes for the Chassis Manager internal ARM processor to complete initialization.
  4. Sign in to the Chassis Manager web interface at `https://198.18.0.2` or using SSH at `198.18.0.2` using default credentials (`Administrator` / `password`) and set the administrative password.



### Return to bootstrapping or appliance upgrade

After the Chassis Manager finishes rebooting and you set the administrative password, return to your original workflow:

  * **If resuming a failed bootstrap** : return to the bootstrapper terminal. You don't need to repeat bootstrapper preparation or clean up existing files. Run `/usr/bin/prod-appliance.sh` to resume the bootstrapping process:
        
        /usr/bin/prod-appliance.sh
        

  * **If performing as a prerequisite before bootstrapping** : return to [Bootstrap the appliance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/install/lowside-setup) and follow the step-by-step instructions to begin the bootstrap process.

  * **If performing before or during an appliance upgrade** : return to [Update and patch device](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/update-patch) and proceed with the upgrade process using `gdcloud appliance upgrade`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
