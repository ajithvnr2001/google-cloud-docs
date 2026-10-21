---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/security/
title: Security best practices \u00a0|\u00a0 Google Distributed Cloud connected, version 1.8.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:30:38.576189+00:00
---

# Security best practices  |  Google Distributed Cloud connected, version 1.8.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/security/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/overview)



Send feedback 

#  Security best practices Stay organized with collections  Save and categorize content based on your preferences. 

This page describes best practices for securing your Google Distributed Cloud installation.

## Physical hardware security

You are responsible for the physical security of the Distributed Cloud connected hardware, such as limiting access to authorized personnel.

The Distributed Cloud connected tack form factor has the following security features:

  * Access to the hardware installed on the rack is possible only through the front and back rack doors.
  * The rack cannot be easily disassembled. There are no externally accessible structural fasteners such as screws, nuts, latches, or rivets.
  * The rack doors are equipped with key locks. Google supplies you with a copy of the key and retains a copy for safe keeping.
  * For multi-rack installations, all rack locks are keyed identically.
  * The rack doors have perforated tamper-proof metal mesh for ventilation.
  * During installation, the rack is securely bolted to the installation site floor by using its shipping braces and brackets.



The Distributed Cloud connected server form factor has the following security features:

  * An intrusion sensor. If an unauthorized party physically opens the machine, you and Google are immediately notified of the physical intrusion.



If you have further questions about the security of the physical rack, contact your Google Cloud sales representative.

## Platform security

The Distributed Cloud connected hardware platform has the following security features:

  * **Trusted Platform Module (TPM)**. The TPM is the root of trust that generates and stores encryption keys for all data stored on as well as received and transmitted by Distributed Cloud connected.

  * **Platform certificate**. The platform certificate is a cryptographically secure record of manufacturing and TPM identity. The certificate acts as proof of supply chain integrity for Distributed Cloud connected hardware.

  * **Port lockdown**. All external and internal ports other than Ethernet ports, such as USB and RS-232 console ports are disabled at the firmware level and only enabled for servicing.




## Local storage security

Distributed Cloud connected hardware ships with the following types of internal storage depending on the form factor:

  * Distributed Cloud connected racks ship with Solid State Disk (SSD) drives.
  * Distributed Cloud connected servers ship with Self-Encrypting Disk (SED) drives.



Distributed Cloud connected uses Linux Unified Key Setup (LUKS) to encrypt the logical volumes on each Distributed Cloud connected node. You have the option to use customer-managed encryption keys (CMEK) or Google-owned and managed keys to wrap the LUKS disk encryption key (DEK). When you assign a node to a node pool, the node generates a LUKS DEK and wraps it in either a Google-managed LUKS passphrase, also known as the key encryption key (KEK), or one provided by you through Cloud KMS. You can choose whether to use Cloud KMS when creating a node pool. Distributed Cloud connected integrates with Cloud KMS by using the [envelope encryption model](https://docs.cloud.google.com/kms/docs/envelope-encryption).

Distributed Cloud connected automatically rotates the LUKS and SED passphrases on a regular schedule.

Additionally, each Distributed Cloud connected machine does the following on every cold start:

  * If you are not using Cloud KMS, the machine generates a new KEK (LUKS passphrase) and sets up encrypted storage from the beginning.

  * If you are using Cloud KMS, the machine fetches the KEK from Cloud KMS and unlocks the existing logical volumes that hold your data.




### Configure support for customer-managed encryption keys (CMEK) for local storage

By default, Google Distributed Cloud connected, version 1.8.0 encrypts customer content at rest. Distributed Cloud connected handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Distributed Cloud connected. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Distributed Cloud connected resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

To enable Cloud KMS integration with Distributed Cloud connected, complete the following steps:

  1. Create a keyring, a symmetric key, and one or more key versions to use with Distributed Cloud connected. You must create these artifacts in the same Google Cloud region as your Distributed Cloud connected installation. For instructions, see [Create a key](https://docs.cloud.google.com/kms/docs/create-key).

  2. Grant the [Cloud KMS CryptoKey Encrypter/Decrypter role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) to the Distributed Cloud connected Service Account in your Google Cloud project. You must do this for each key version that you want to use with Distributed Cloud connected. If you revoke this role after you integrate your Distributed Cloud connected installation with Cloud KMS, **you lose access to data stored on the Distributed Cloud connected machines**.

  3. [Create a node pool](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/nodepools#create) by using the `--local-disk-kms-key` flag, and provide the full path to the key version that you want to use with that node pool.

  4. [Create a cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/clusters#create) by using the `--control-plane-kms-key` flag, and provide the full path to the key version that you want to use with the node running the cluster's control plane.

  5. Optionally, use the `--offline-reboot-ttl` flag when creating your cluster to specify a time window during which nodes that have been rebooted can rejoin the cluster while the cluster is running in survivability node. If you don't specify this window, rebooted nodes cannot rejoin the cluster until it exits survivability mode.

CAUTION: If you specify a reboot timeout window, nodes that have gone offline can reboot and rejoin the cluster even if you disable or delete the storage key for the specified time.




To revert a cluster or a node pool to use a Google-owned and Google-managed encryption key, use the `--use-google-managed-key` flag as described in one of the following:

  * [Modify a cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/clusters#modify)
  * [Modify a node pool](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/nodepools#modify)



For more information, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) in the Cloud KMS documentation.

### Data recovery and backups

You are responsible for maintaining functioning redundant backups of all the data that you choose to store on Distributed Cloud connected hardware and exporting that data when you choose to return Distributed Cloud connected hardware to Google or the Google-certified System Integrator (SI) that sold you the hardware.

If a failure of Distributed Cloud connected hardware occurs and Google or a Google-certified SI performs on-site repairs, all storage media is removed from the Distributed Cloud connected machine being serviced and is either placed into your custody for the duration of the repair or securely wiped and then sent for destruction.

If you purchased the Distributed Cloud hardware from a Google-certified SI and are no longer using Distributed Cloud but chose to keep and repurpose the hardware, the SI will wipe all Google software and your data from the Distributed Cloud hardware during decommissioning.

## Network security

Network traffic between Distributed Cloud connected hardware and Google Cloud is encrypted using either MASQUE tunnels or TLS that use per-machine certificates. Distributed Cloud connected automatically rotates these certificates on a regular schedule.

Your business requirements and your organization's network security policy dictate the steps necessary to secure network traffic that flows in and out of your Distributed Cloud connected installation. In addition, we recommend the following:

  * Allow only inbound connections to virtual IP address pools exposed by the Distributed Cloud connected built-in load balancer and to Distributed Cloud subnetworks.

  * Disallow inbound connections from external network resources to subnetworks that serve the [system management](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/how-it-works#network-layers) and [service management](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/how-it-works#network-layers) layers.

  * Disallow inbound connections from external network resources to IP addresses of local control plane endpoints. For more information, see [Survivability mode](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/survivability).




For more information about how to prepare your local network for connecting Distributed Cloud hardware, see [Networking](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/requirements#networking).

## MAC-level physical network link security for multi-rack deployments

For multi-rack deployments, Distributed Cloud connected supports Layer 2 Media Access Control (MAC) security (L2 MACsec) at the Ethernet frame level between the aggregator switches in your base rack and the ToR switches in your standalone racks.

You must request this feature when ordering your Distributed Cloud connected hardware. It cannot be enabled after Distributed Cloud connected has been deployed on your premises.

Distributed Cloud connected uses MACsec to authenticate Ethernet devices, verify the integrity of each transmitted Ethernet frame, and encrypt each transmitted frame.

This involves establishing a set of keys which are verified between all devices involved in an Ethernet transport session before Ethernet traffic is allowed to flow. Once key agreement has been verified, the sender starts tagging each transmitted Ethernet frame with security tags and integrity check values that the receiver verifies upon receipt of each frame.

Each MACsec-configured device must be authenticated by and associated with a Connectivity Association (CA). CA members use long-life CA keys (CAKs) to identify themselves on the network. The CAK is used to generate session encryption keys every time a CA member needs to exchange data with another CA member on the network.

### Distributed Cloud connected MACsec policies

Distributed Cloud connected enforces the following MACsec policies on all Ethernet links between base rack aggregator switches and standalone rack ToR switches. These policies cannot be modified or disabled.

#### MACsec configuration

All Distributed Cloud connected MACsec configuration, including encryption keys, is managed by Google.

#### MACsec link security

Distributed Cloud connected disallows unencrypted packets on all internal Ethernet links. If a MACsec session cannot be successfully negotiated, the affected Ethernet link goes down automatically.

#### MACsec keychain

A MACsec keychain is the key store holding all of the required keys for a specific Ethernet link. A unique keychain is created for a bundle interface. Each keychain holds 4 primary keys plus a fallback key. Each primary key has 25% validity. 

#### MACsec fallback

Distributed Cloud connected configures a MACsec fallback key in addition to 4 primary keys for each internal Ethernet link. If Distributed Cloud connected cannot negotiate a MACsec session using the primary keys, it attempts to negotiate a fallback session using the fallback key. The fallback key does not expire.

#### MACsec key rotation

Distributed Cloud connected aggregator and ToR switches rotate their primary MACsec keys immediately when those keys expire. To ensure safe key rotation, each previous and next key in rotation have a lifespan overlap of 5 days.

#### MACsec Secure Association Key

Distributed Cloud connected uses a randomly generated MACsec Secure Association Key (SAK) to encrypt all Ethernet frames carried by internal Ethernet links. Distributed Cloud connected performs volume-based rekeying using Extended Packet Numbering (XPN). The SAK is re-generated every 6 hours.

### Check the MACsec status of a Distributed Cloud connected rack link

Use the following command to check the MACsec status of a specific Ethernet link between a base rack aggregator switch and a ToR switch in a standalone rack:
    
    
    gcloud edge-cloud networking networks get-status default --location=REGION --zone=us-ZONE_NAME
    

Replace the following:

  * `REGION`: the Google Cloud region in which the target Google Cloud project has been created.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



The command returns an output similar to the following:
    
    
    result:
      macsecStatusInternalLinks: SECURE
    

The possible link status values are:

  * **`SECURE`** \- MACsec session is up on the target link.
  * **`UNSECURE`** \- MACsec session is down on the target link.



## What's next

  * [Ensure high availability for your Distributed Cloud connected installation](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/availability)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
