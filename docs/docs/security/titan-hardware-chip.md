---
url: https://docs.cloud.google.com/docs/security/titan-hardware-chip/
title: Titan hardware chip \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:29.631895+00:00
---

# Titan hardware chip  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/titan-hardware-chip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Titan hardware chip Stay organized with collections  Save and categorize content based on your preferences. 

_This content was last updated in January 2025, and represents the status quo as of the time it was written. Google's security policies and systems may change going forward, as we continually improve protection for our customers_.

The Titan chip is a purpose-built chip that establishes the hardware root of trust for platforms in Google Cloud data centers. The Titan chip is a low-power microcontroller that is deployed on platforms such as servers, network infrastructure, and other data center peripherals.

The Titan chip is an important component of the [Titanium hardware security architecture](https://docs.cloud.google.com/docs/security/titanium-hardware-security-architecture), which provides a foundational security layer that helps protect against physical attacks and threats to user data. The Titan chip lets Google securely identify and measure platform firmware and configuration. It is designed to protect against privileged software attacks and rootkits, from the machine boot process forward.

This document describes the chip architecture and security benefits of the Titan chip. The Titan chip supports a minimal trusted computing base (TCB) that lets the chip provide the following benefits:

  * A hardware root of trust that creates a strong identity for a machine
  * Integrity verification of platform firmware, both at boot time and update time
  * [Remote credential sealing](https://docs.cloud.google.com/docs/security/boot-integrity#credential-sealing-process) flows that underpin Google's machine credential management system



## The Titan chip family

The earliest Titan chips were designed in 2014. Later generations incorporated the experience that was gained during iterative manufacturing, integration, and deployment processes. For more information about how Google has contributed our knowledge about the Titan chip to the open-source hardware security community, see [opentitan.org](https://opentitan.org).

Titan chips include the following components:

  * Secure processor
  * AES and SHA cryptographic coprocessor
  * Hardware random number generator
  * Sophisticated key hierarchy
  * Embedded static RAM (SRAM), flash, and ROM



## Titan manufacturing identity

During the Titan chip manufacturing process, chips are moved into a secure room in the Outsourced Semiconductor Assembly and Test (OSAT) facility so that they can be provisioned with their identity. This room meets ISO and Common Criteria standards. It has four redundant (all corner) cameras and a badge reader door that is only meant to be open during operational emergencies. No humans are in the room when the chips are provisioned; the process is fully automated.

Devices enter through an enclosure in one wall and are inserted into an automated handler. Each handler is equipped with a Titan chip that's referred to as a _Scribe_. The Scribe includes provisioning firmware, and has a serial peripheral interface (SPI), reset, and universal asynchronous receiver-transmitter (UART) connections to the device under test (DUT) (which is the Titan chip that's being manufactured). The Scribe is covered in epoxy, with unique tamper-evident markings. The automated handler drives the DUT into a bed of nails, where it powers on. The Scribe releases the DUT from reset, feeds it the execution firmware, and runs the provisioning process.

During the provisioning process, the DUT verifies the provisioning firmware using a public key that's embedded in its mask ROM. The firmware uses the chip's True Random Number Generator (TRNG) to generate an internal device secret, which it burns into the chips fuses. This secret is the root of all key derivations that the chip runs going forward. The Scribe doesn't know this secret. The DUT generates a personalization manifest that includes its unique public key derived from the internal device secret. The personalization manifest is authenticated by a class key embedded in the DUT's Register Transfer Level (RTL). The Scribe harvests the personalization manifest over SPI, then signs it using a key that's unique to that Scribe. The personalization manifest is then uploaded and stored in a Google registry database.

Each Scribe signing key is registered in an in-person ceremony when the Scribe is brought into service. In addition, the Scribe only holds its signing private key in volatile memory, ensuring that if the Scribe is removed from the secure facility, it loses the signing key upon power loss. Each Scribe must fetch a uniquely-wrapped copy of its signing key from a Google service each time that it's powered on. The wrapped copy of a given Scribe's signing key is established when the Scribe was initially registered offline by a k-of-n quorum, and can only be unwrapped by that Scribe.

When Titan-enabled platforms are integrated into the Google production network, the backend systems can verify that these platforms are equipped with authentic Titan chips by verifying the Titan's unique public key against the database of harvested personalization manifests. For more information about how services use the Titan identity system, see [Credential sealing process](https://docs.cloud.google.com/docs/security/boot-integrity#credential-sealing-process).

Titan chips use their device-unique keypairs to attest to their firmware in a manner similar to [Device Identifier Composition Engine (DICE)](https://trustedcomputinggroup.org/what-is-a-device-identifier-composition-engine-dice/). The original Titan chips were certified using a custom Google design, because these chips were manufactured before relevant industry standards were introduced. Google's experience in manufacturing and deploying secure hardware motivates us to increase participation in standards processes, and newer standards such as DICE, Trusted Platform Module (TPM), and Security Protocol and Data Mode (SPDM) include changes that reflect our experience.

## Titan integration

When the Titan chip is integrated into a platform, it provides security protections to an application processor (AP). For example, Titan might be paired with a CPU that runs workloads, a baseboard management controller (BMC), or an accelerator for workloads such as machine learning.

Titan communicates with the AP using the SPI bus. Titan interposes between the AP and the AP's boot firmware flash chip, ensuring that Titan can read and measure every byte of that firmware before the firmware is run at boot time.

The following steps occur when a Titan-enabled platform powers on:

  1. Titan keeps the CPU in reset mode while Titan's internal application processor runs immutable code (the _boot ROM_) from its embedded read-only memory.
  2. Titan runs a built-in self-test to verify that all memory (including the ROM) hasn't been tampered with.
  3. Titan's boot ROM verifies Titan's firmware using public key cryptography and mixes the identity of the verified firmware into Titan's key hierarchy.
  4. Titan's boot ROM loads Titan's verified firmware.
  5. Titan firmware verifies the contents of the AP's boot firmware flash using public key cryptography. Titan blocks the AP's access to its boot firmware flash until the verification process completes successfully.
  6. After verification, the Titan chip releases the AP from reset, allowing the AP to boot.
  7. The AP firmware performs additional configuration, which might include launching further boot images. The AP can capture measurements of these boot images and send the measurements to Titan for secure monitoring.



These steps achieve _first-instruction integrity_ because Google can identify the boot firmware and OS that was booted on the machine from the very first instruction that runs during the startup cycle. For APs with CPUs that accept microcode updates, the boot process also lets Google know which microcode patches were fetched before the boot firmware's first instruction. For more information, see [Measured boot process](https://docs.cloud.google.com/docs/security/boot-integrity#measured-boot-process).

This flow is similar to the boot process that is performed by platforms that are equipped with a TPM. However, Titan chips include features that are not generally available on standard TPMs, such as Titan's internal firmware self-attestation or AP firmware upgrade security, as described in the following sections.

Standard TPM integrations can be vulnerable to physical interposer attacks. Newer Titan integrations at Google mitigate these attacks by using integrated roots of trust. For more information, see [TPM Transport Security: Defeating Active Interposers with DICE (YouTube)](https://www.youtube.com/watch?v=DKfbkOTYzOU).

## Secure Titan firmware upgrade

The Titan chip's firmware is signed by a key that is held in an offline HSM, which is protected by quorum-based controls. Titan's boot ROM verifies Titan firmware's signature whenever the chip boots.

Titan firmware is signed with a security version number (SVN), which conveys the security state of the image. If a firmware image includes a vulnerability fix, the image's SVN is incremented. Titan hardware lets the production network strongly attest to the SVN of Titan's firmware, even if older firmware might have had vulnerabilities. The upgrade process lets us recover from these vulnerabilities at scale, even if they affect Titan's own firmware. For more information, see [Recovering from vulnerabilities in root-of-trust firmware](https://docs.cloud.google.com/docs/security/boot-integrity#recovering_from_vulnerabilities_in_root-of-trust_firmware).

Google contributed to the latest version of the TPM Library specification, which now includes features that let other TPMs provide similar self-attestation assurances. For more information, see the [TPM Firmware-Limited and SVN-Limited Objects section (PDF)](https://trustedcomputinggroup.org/wp-content/uploads/TPM-2.0-1.83-Part-1-Architecture.pdf#page=288) of version 1.83 of the TPM Architecture specification. These TPM features were implemented and deployed on our latest Titan chips.

## Secure AP firmware upgrade

In addition to Titan's firmware, we also cryptographically sign the firmware that runs on the AP. Titan verifies this signature as part of the platform boot process. It also verifies this signature whenever the AP firmware is updated, enforcing that only authentic AP firmware images can be written to the AP's boot firmware flash chip. This verification process mitigates attacks that attempt to install persistent backdoors or render the platform unbootable. Signature verification also provides defense in depth for Google's platforms in the event that a CPU has a vulnerability in its own microcode authentication mechanism.

## What's next

Learn more about our [boot integrity process](https://docs.cloud.google.com/docs/security/boot-integrity).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
