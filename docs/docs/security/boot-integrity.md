---
url: https://docs.cloud.google.com/docs/security/boot-integrity/
title: How Google enforces boot integrity on production machines \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:01.216618+00:00
---

# How Google enforces boot integrity on production machines  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/boot-integrity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  How Google enforces boot integrity on production machines Stay organized with collections  Save and categorize content based on your preferences. 

_This content was last updated in May 2024, and represents the status quo as of the time it was written. Google's security policies and systems may change going forward, as we continually improve protection for our customers._

This document describes the infrastructure controls that Google uses to enforce the integrity of the boot process on production machines that are equipped with [Titan](https://docs.cloud.google.com/docs/security/titan-hardware-chip). These controls, built on top of a _measured boot_ process, help ensure that Google can recover its data center machines from vulnerabilities throughout their boot stack and return the machines from arbitrary boot states to known good configurations.

## Introduction

The security posture of a data center machine is highly dependent on the machine's configuration at boot time. The machine's boot process configures the machine's hardware and initializes its operating system, while keeping the machine safe to run in Google's production environment.

At each step in the boot process, Google implements industry-leading controls to help enforce the boot state that we expect and to help keep customer data safe. These controls help ensure that our machines boot into their intended software, allowing us to remove vulnerabilities that could compromise the initial security posture of the machine.

This document describes the boot process and demonstrates how our controls operate during the boot flow. The key objectives of our controls are the following:

  * Establish trust in machine credentials through hardware roots-of-trust
  * Seal machine credentials to a boot policy that specifies allowed firmware and software versions
  * Enforce the boot policy on machines through a measured boot process



## Background

This section defines and provides context for the terms _machine credentials_ , _hardware root of trust_ , _sealed credentials_ , and _cryptographic sealing_.

### Machine credentials

One of the central components in Google's machine management system is our credential infrastructure, which consists of an internal certificate authority (CA) and other control plane elements that are responsible for coordinating credential rotation flows.

Machines in Google's production fleet perform mutual authentication when establishing secure channels. To perform mutual authentication, each machine possesses Google's CA public keys. Each machine also possesses its own public/private key pair, as well as a certificate for that key pair.

Each machine's public/private key pair, together with the certificate signed by the CA, is known as a _machine credential_ , which the machine uses to authenticate itself to other machines in the fleet. Within the production network, machines check that other machines' public keys are certified by Google's CA before exchanging traffic.

### Hardware roots of trust and cryptographic sealing

As computing devices grow more sophisticated, each device's attack surface also grows. To account for this, devices increasingly feature _hardware roots of trust (RoTs)_ which are small, trusted execution environments that safeguard sensitive data for the machine. RoTs also appear in mobile devices like laptops or cell phones, and in more conventional devices like desktop PCs.

Google's data center machines feature custom, Google-designed hardware roots of trust integrated into each machine's deepest layers, known as [Titan](https://docs.cloud.google.com/docs/security/titan-hardware-chip). We use Titan, along with a mechanism called _cryptographic sealing_ , to ensure that each machine is running the configuration and software versions we expect.

Cryptographic sealing is a service offered by Titan that is used to safeguard secrets. Titan's sealing capabilities are similar to those found in the [Trusted Platform Module (TPM)](https://en.wikipedia.org/wiki/Trusted_Platform_Module) specification, which is published by the [Trusted Computing Group](https://trustedcomputinggroup.org/). Titan's cryptographic sealing has an additional advantage, in that Titan brings a better ability to measure and attest to low-level firmware.

Cryptographic sealing comprises the following two controls:

  * Encryption of sensitive data
  * A policy that must be satisfied before the data can be decrypted



### Sealed credentials

Google's credential infrastructure uses cryptographic sealing to encrypt machine credentials at rest with a key that is controlled by the machine's hardware root of trust. The encrypted credential private key, and the corresponding certificate, is known as a _sealed credential_. In addition to machine credentials, Google uses this sealing mechanism to protect other pieces of sensitive data as well.

Each machine can decrypt and access its machine credential only if it can satisfy a decryption policy that specifies what software the machine must have booted. For example, sealing a machine's credential to a policy that specifies the intended release of the operating system kernel helps ensure that the machine can't participate in its machine cluster unless it booted the intended kernel version.

The decryption policy is enforced through a process called _measured boot_. Every layer in the boot stack measures the next layer, and the machine attests to this chain of measurements at the end of the boot. This measurement is often a cryptographic hash.

## Credential sealing process

This section describes the credential sealing and measured boot process used by Google machines. The following diagram illustrates this flow.

![The credential sealing flow.](https://docs.cloud.google.com/static/docs/security/images/boot-attestation-credential-sealing.svg)

To seal a machine's credentials to a particular boot policy, the following steps happen:

  1. Google's machine automation infrastructure initiates a software update on the machine. It passes the intended software versions to the credential infrastructure.
  2. Google's credential infrastructure requests a sealing key from Titan, policy-bound such that Titan only uses it if the machine boots into its intended software.
  3. The credential infrastructure compares the returned key's policy with the intent communicated to it by the machine automation infrastructure. If the credential infrastructure is satisfied that the policy matches the intent, it issues a certified machine credential to the machine.
  4. The credential infrastructure encrypts this credential using the sealing key that is procured in step 2.
  5. The encrypted credential is stored on disk for decryption by Titan on subsequent boots.



## Measured boot process

Google machines' boot stack consists of four layers, which are visualized in the following diagram.

![The four layers of the measured boot process.](https://docs.cloud.google.com/static/docs/security/images/boot-attestation-boot-layers.svg)

The layers are the following:

  * **Userspace** : applications like daemons or workloads.
  * **System software** : a hypervisor or kernel. The lowest level of software that provides an abstraction over hardware features like networking, the file system, or virtual memory to the userspace.
  * **Boot firmware** : the [firmware](https://en.wikipedia.org/wiki/Bootloader) that initializes the kernel, such as a BIOS and bootloader.
  * **Hardware root of trust** : in Google machines, a Titan chip that cryptographically measures the firmware and other low-level CPU services.



Throughout boot, each layer measures the next layer before passing control to that layer. The machine's sealed credential is only made available to the operating system if all measurements that are captured during boot conform to the sealed credential's decryption policy, as specified by Google's credential infrastructure. Therefore, if the machine can perform operations with its sealed credentials, that is evidence that the machine satisfied its measured boot policy. This process is a form of implicit attestation.

If a machine boots software that deviates from the intended state, the machine cannot decrypt and perform operations with the credentials that it needs to operate within the fleet. Such machines cannot participate in workload scheduling until machine management infrastructure triggers automated repair actions.

## Recovering from vulnerabilities in the kernel

Suppose that a machine is running kernel version A, but security researchers find that this kernel version has a vulnerability. In these scenarios, Google patches the vulnerability and rolls out an updated kernel version B to the fleet.

In addition to patching the vulnerability, Google also issues new machine credentials to each machine in the fleet. As described in Credential sealing process, the new machine credentials are bound to a decryption policy that is only satisfied if kernel version B boots on the machine. Any machine that is not running its intended kernel cannot decrypt its new machine credentials, as the boot firmware measurements won't satisfy the machine's boot policy. As part of this process, the old machine credentials are also revoked.

As a result, these machines are unable to participate in their machine cluster until their kernel is updated to conform to the control plane's intent. These controls help ensure that machines running the vulnerable kernel version A cannot receive jobs or user data until they are upgraded to kernel version B.

## Recovering from vulnerabilities in boot firmware

Suppose that there is a vulnerability in the boot firmware, instead of the operating system kernel. The same controls described in Recovering from vulnerabilities in the kernel help Google recover from such a vulnerability.

Google's Titan chip measures a machine's boot firmware before it runs, so that Titan can determine whether the boot firmware satisfies the machine credential's boot policy. Any machine that is not running its intended boot firmware cannot obtain new machine credentials, and that machine cannot participate in its machine cluster until its boot firmware conforms to the control plane's intent.

## Recovering from vulnerabilities in root-of-trust firmware

RoTs are not immune to vulnerabilities, but Google's boot controls enable recovery from bugs even at this layer of the boot stack, within the RoT's own mutable code.

Titan's boot stack implements a secure and measured boot flow of its own. When a Titan chip powers on, its hardware cryptographically measures Titan's bootloader, which in turn measures Titan's firmware. Similarly to the machine's kernel and boot firmware, Titan firmware is cryptographically signed with a version number. Titan's bootloader validates the signature and extracts the version number of Titan firmware, feeding the version number to Titan's hardware-based key derivation subsystem.

Titan's hardware subsystem implements a versioned key derivation scheme, whereby Titan firmware with version _X_ can obtain chip-unique keys bound to all versions less than or equal to X. Titan hardware allows firmware with version X to access keys that are bound to versions that are less than or equal to X, but that are not greater than X. All secrets sealed to Titan, including the machine credential, are encrypted using a versioned key.

Attestation and sealing keys are unique to each Titan chip. Unique keys let Google trust only those Titan chips that are expected to be running within a Google data center.

The following diagram shows Titan with version keys. The Version X+1 key cannot be accessed by version X firmware, but all keys older than that are accessible.

![Titan versions.](https://docs.cloud.google.com/static/docs/security/images/boot-attestation-titan-versions.svg)

In the event of a severe vulnerability in Titan firmware, Google rolls out a patch with a greater version number, then issues new machine credentials that are bound to the higher Titan firmware version. Any older, vulnerable Titan firmware is unable to decrypt these new credentials. Therefore, if a machine performs operations with its new credentials in production, Google can assert with confidence that the machine's Titan chip booted up-to-date Titan firmware.

## Ensuring root of trust authenticity

The controls described in this document all rest on the functionality of the hardware RoT itself. Google's credential infrastructure relies on signatures emitted by these RoTs to know whether the machine is running intended software.

It is critical, therefore, that the credential infrastructure can determine whether a hardware RoT is authentic and whether the RoT is running up-to-date firmware.

When each Titan chip is manufactured, it is programmed with unique entropy. Titan's low-level boot routine turns that entropy into a device-unique key. A secure element on the Titan manufacturing line endorses this chip-unique key such that Google will recognize it as a legitimate Titan chip.

The following diagram illustrates this endorsement process.

![The Titan endorsement process.](https://docs.cloud.google.com/static/docs/security/images/boot-attestation-titan-endorsement.svg)

When in production, Titan uses its device-unique key to endorse any signature it emits. Titan chips use a flow that is similar to [Device Identifier Composition Engine (DICE)](https://trustedcomputinggroup.org/accurately-attest-the-integrity-of-devices-with-dice/). The endorsement includes Titan firmware's version information. This attestation helps prevent an attacker from impersonating a signature that is emitted by a Titan chip, and from rolling back to older Titan firmware and impersonating newer Titan firmware. These controls help Google verify that signatures received from Titan were emitted by authentic Titan hardware running authentic Titan firmware.

## Building on boot integrity

This paper described mechanisms for ensuring that machines' application processors boot intended code. These mechanisms rely on a measured boot flow, coupled with a hardware root-of-trust chip.

Google's threat model includes attackers who may physically interpose on the bus between the CPU and RoT, with the goal of improperly obtaining the machine's decrypted credential. To help minimize this risk, Google is driving development of a standards-based approach for defeating active interposers, bringing together the [TPM](https://trustedcomputinggroup.org/wp-content/uploads/2019_TCG_TPM2_BriefOverview_DR02web.pdf) and [DPE](https://trustedcomputinggroup.org/wp-content/uploads/TCG-DICE-Protection-Environment-Specification_14february2023-1.pdf) APIs from Trusted Computing Group and the [Caliptra](https://chipsalliance.github.io/Caliptra/) integrated root of trust.

## What's next

  * For information about how Google helps ensure the integrity of complex disaggregated machines' boot stacks, see [Remote attestation of disaggregated machines](https://docs.cloud.google.com/docs/security/remote-attestation).
  * For overview information about Google's security infrastructure, see [Google infrastructure security design overview](https://docs.cloud.google.com/docs/security/infrastructure/design).
  * For more on how Google is contributing Titan security solutions to industry standards, see the [TPM Attested Boot in Big, Distributed Environments](https://youtu.be/z0Joifl7JS0?t=70) talk on the Trusted Computing Group YouTube channel.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
