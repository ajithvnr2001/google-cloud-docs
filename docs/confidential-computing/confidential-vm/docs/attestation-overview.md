---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/attestation-overview/
title: Remote attestation overview \u00a0|\u00a0 Confidential VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:15.615653+00:00
---

# Remote attestation overview  |  Confidential VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/attestation-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)



Send feedback 

#  Remote attestation overview Stay organized with collections  Save and categorize content based on your preferences. 

Remote attestation is the process of verifying that a Confidential VM instance's identity is legitimate, and that it's operating in an expected state. Attestation can help you to assess a system's trustworthiness before you give it access to your protected resources.

## Attestation parties and models

There are usually three parties in the attestation process:

  * **An attester**. On Google Cloud, this is a workload on a Confidential VM instance that requires access to protected resources. To increase trust that the Confidential VM instance hasn't been compromised and isn't an imposter, the VM and its host take measurements of the VM's virtual hardware and software state during the boot process.

  * **A verifier**. A verifier is an external system that validates the evidence from a Confidential VM instance, and checks it against its attestation policy to make sure that the VM configuration is as expected. If the evidence passes the required checks, the verifier returns a signed version of the evidence known as an _attestation result_.

A verifier can be a pre-existing service such as [Google Cloud Attestation](https://docs.cloud.google.com/confidential-computing/docs/attestation) or [Intel Trust Authority](https://docs.trustauthority.intel.com/main/articles/articles/ita/introduction.html), or something you've built yourself.

  * **A relying party**. The relying party controls access to protected resources that the attester needs. Upon receiving an attestation result, the relying party checks the values in the evidence against its access policy. If the values match, the attester is allowed access to the resources.

On Google Cloud the relying party is often a [workload identity pool](https://docs.cloud.google.com/iam/docs/manage-workload-identity-pools-providers), with the verifier added as an OpenID Connect (OIDC) provider.




How the parties interact depends on the attestation model your architecture follows. The [Remote ATtestation procedureS (RATS) Architecture RFC](https://datatracker.ietf.org/doc/rfc9334/) defines two major attestation models: the passport model and the background check model. The main difference between the two is which party has possession of the attester's verified identity: the attester or the relying party.

### Passport model

The passport model uses the following process to confirm an attester's identity and grant access to requested resources:

  1. The attester sends evidence of its identity to a verifier.

  2. If the evidence is deemed trustworthy, the verifier sends the attester the attestation result, which might take the form of an _attestation token_.

  3. The attester sends the attestation result to a relying party.

  4. The relying party checks that the attestation result meets certain conditions. If the result meets expectations, the relying party allows the attester to access the requested resources.




In the passport model, the attester and relying party need to agree on what the attestation results should look like, which means they need to agree on a verifier.

![Attestation passport model](https://docs.cloud.google.com/static/confidential-computing/confidential-vm/docs/images/attestation-model-passport.svg)

### Background check model

The background check model uses the following process to confirm an attester's identity and grant access to requested resources:

  1. The attester sends evidence of its identity to a relying party.

  2. The relying party forwards the evidence to a verifier.

  3. If the evidence is deemed trustworthy, the verifier sends the relying party the attestation result, often as an attestation token.

  4. The relying party checks that the attestation result meets certain conditions. If the result meets expectations, the relying party allows the attester to access the requested resources.




![Attestation background check model](https://docs.cloud.google.com/static/confidential-computing/confidential-vm/docs/images/attestation-model-background-check.svg)

With the background check model, a relying party determines the attestation evidence it requires, and chooses the verifier.

## Attester architecture and evidence

This section covers how a Confidential VM instance as an attester provides tamper-resistant evidence of its identity.

### Roots of trust

In a trusted execution environment (TEE) such as a Confidential VM instance, a _root of trust_ is a foundational security component from which other trust is established. A root of trust provides cryptographic functions, is tamper-resistant, and can't be modified by a host operating system.

Roots of trust belong inside a trust boundary within a TEE known as the _Trusted Computing Base_ (TCB). The TCB is a collection of hardware and software across a guest VM and its host that are responsible for duties such as environment isolation (through mechanisms such as memory encryption and hypervisor isolation) and taking measurements to maintain the environment's integrity.

A TEE supports roots of trust for measurement, storage, and reporting functions:

  * The _root of trust for measurement_ is the code that initiates the measurements of the TEE boot process.

  * The _root of trust for storage_ provides shielded memory for measurements in the form of _measurement registers_.

  * The _root of trust for reporting_ provides integrity and authenticity protection for the measurement chain. It retrieves measurements from the root of trust for storage and bundles them into a signed evidence package called a quote or attestation report. This package is signed with a TEE-resident _attestation key_ , and can include a cryptographic nonce to ensure the evidence is fresh and protected against replay attacks.

**Key Term:** A _replay attack_ is when a bad actor copies evidence that verifies an identity, and uses that evidence to illegitimately gain access to resources. One way to combat replay attacks is with a _nonce_ : a one-time, short-lived, random number provided by one of the parties protecting the resources—in the case of Confidential Computing, the verifier. The entity proving its identity must incorporate the nonce into its evidence before that evidence is sent. If a bad actor tries to use stolen evidence to access resources, it's likely to fail because the nonce that's included in the evidence has already been used or has expired.



The following information details the different approaches to roots of trust for different Confidential Computing technologies.

###  AMD SEV 

A Confidential VM instance with AMD SEV attests to its environment and configuration by using [Shielded VM vTPM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm)-based measurements. The AMD Secure Processor and AMD SEV are used solely for memory encryption.

The roots of trust are as follows:

  * **Root of trust for measurement** : VM instance firmware

  * **Root of trust for storage** : Shielded VM vTPM

  * **Root of trust for reporting** : Shielded VM vTPM, which uses a private attestation key to sign attestation reports




![SEV root of trust](https://docs.cloud.google.com/static/confidential-computing/confidential-vm/docs/images/vtpm-measurements-boundaries.svg)

To learn what measurements are recorded where in the Shielded VM vTPM, see [vTPM platform configuration registers](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/measurement-register-contents#vtpm).

###  AMD SEV-SNP 

A Confidential VM instance with AMD SEV-SNP primarily attests to its environment and configuration through the AMD Secure Processor, which handles the initial launch measurements.

For bootloader, kernel, and userspace measurements, [Shielded VM vTPM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm)-based measurements can be used.

The roots of trust are as follows:

  * **Root of trust for measurement** : AMD Secure Processor + VM instance firmware

  * **Root of trust for storage** : AMD Secure Processor + Shielded VM vTPM

  * **Root of trust for reporting** :

    * **Initial launch measurements** : The AMD Secure Processor, which uses the chip-resident Version Chip Endorsement Key (VCEK) to sign attestation reports

    * **Bootloader, kernel, and userspace measurements** : Shielded VM vTPM




![SNP root of trust](https://docs.cloud.google.com/static/confidential-computing/confidential-vm/docs/images/snp-vtpm-measurements-boundaries.svg)

To learn what measurements are recorded in the AMD Secure Processor, see [AMD SEV-SNP measurement register](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/measurement-register-contents#snp).

To learn what measurements are recorded where in the Shielded VM vTPM, see [vTPM platform configuration registers](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/measurement-register-contents#vtpm).

###  Intel TDX 

A Confidential VM instance with Intel TDX attests to its environment and configuration through the Intel TDX module. The Intel TDX module measures the VM guest's firmware within an isolated _trust domain_ , and stores those measurements in the Measurement of the Trust Domain (MRTD). Subsequent measurements in the boot chain are measured into the Run-Time Measurement Registers (RTMR).

The roots of trust are as follows:

  * **Root of trust for measurement** : Intel TDX module

  * **Root of trust for storage** : Measurement of the Trust Domain (MRTD) and Run-Time Measurement Registers (RTMR)

  * **Root of trust for reporting** : The Trust Domain Quoting Enclave (TDQE) inside the Intel TDX module, which generates an attestation key to sign attestation quotes




![TDX root of trust](https://docs.cloud.google.com/static/confidential-computing/confidential-vm/docs/images/tdx-measurements-boundaries.svg)

To learn what measurements are recorded where in the TDX measurement registers, see [Intel TDX measurement registers](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/measurement-register-contents#tdx).

#### Software and hardware attestation

Confidential Computing technologies in Google Cloud can be thought of as either software or hardware attested, depending on their roots of trust.

_Software attested_ means that the roots of trust are based on software: the virtual firmware is the root of trust for measurement, and the root of trust for storage is the Shielded VM vTPM. The vTPM is managed by the host's hypervisor, while the firmware is managed by the guest VM. On Google Cloud, both of these components are controlled by Google.

_Hardware attested_ means that measurements are managed and protected by dedicated hardware outside of your service provider's control. On Google Cloud, this hardware includes the AMD Secure Processor for AMD SEV-SNP (for launch measurements only), and the Intel TDX Module for Intel TDX.

Hardware attestation removes the service provider's hypervisor from the root of trust for measurement and storage, and isolates measurements in dedicated hardware. Even if a malicious actor gains control over the host's hypervisor, they can't forge an attestation report or quote as they don't have access to modify the dedicated hardware's registers.

The Confidential Computing technologies provided by Google Cloud are categorized as follows:

  * **AMD SEV** : Software attested. The virtual firmware measures itself, and the measurements are stored in the Shielded VM vTPM.

  * **AMD SEV-SNP** : Hybrid hardware and software attested. Launch measurements, including measurements of the virtual firmware, are recorded by and stored in the AMD Secure Processor, which makes them hardware attested. Bootloader, kernel, and userspace measurements are stored in the Shielded VM vTPM, making them software attested. You can choose to only use the hardware attested measurements, the software attested measurements, or both.

  * **Intel TDX** : Hardware attested. The TDX module measures the virtual firmware, and all measurements are stored in the Intel TDX module. The Shielded VM vTPM is still part of the system, however it's not part of the TCB unless you run software that needs a TPM interface.




### Measurement registers

The roots of trust for Confidential VM provide shielded, tamper-resistant storage for measurements in the form of measurement registers (MRs). What those measurement registers are called changes depending on the Confidential Computing technology in use:

  * **AMD SEV** : Platform configuration registers (PCRs). These are situated inside the Shielded VM vTPM.

Shielded VM vTPMs use three banks of PCRs that store the same measurements, but are hashed with different algorithms: SHA-1, SHA-256, and SHA-384.

  * **AMD SEV-SNP** : The launch `MEASUREMENT` register. This is situated inside the AMD Secure Processor.

The PCRs inside the Shielded VM vTPM are also used to store the bootloader, kernel, and userspace measurements.

  * **Intel TDX** : The build-time Measurement of the Trust Domain (MRTD) and Run-Time Measurement Registers (RTMR).

Measurements are also available in the Shielded VM vTPM PCRs for software that expects a TPM interface.




Only a root of trust can change a register value. Measurement registers typically hold a single cryptographic digest, which represents either a single event or a set of events.

For single events, such as the launch measurement or build-time measurement of a VM, a root of trust typically writes directly to the register and makes the register immutable for the rest of the TEE's lifetime.

Components loaded later in the boot chain such as the bootloader, kernel, and userspace might record measurements for multiple events into a single register. To store the measurements for sets of events, measurement registers expose an `extend` command that concatenates the existing register value with a new event digest, hashes the concatenated value, and then stores the resulting digest. This process is represented by the following formula:

\\(MR_{new}=hash(MR_{old}\;∥\;hash(measured\;data))\\) 

Since hash functions are one way, replicating the same measurement register values without providing the same measurements in the same order is difficult. While this property helps with determining VM integrity, it can make basing policy on specific measurement register values challenging. This is because small changes in measurement inputs—such as software or firmware updates, or a change in measurement order—result in different register values, making them potentially unstable criteria to base policies on and increasing maintenance burden. If you need to base policy on measurement register values, try to select more stable register values such as [PCR 0 or PCR 7 on vTPMs](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/measurement-register-contents#vtpm).

**Tip:** To base policy on stable individual measurements instead of measurement register values, you can use an event log that's generated by your TCB. A verifier first needs to perform an _event log replay_ to verify log integrity against measurement registers, and after successful verification can parse the events to extract meaningful measurements.

### Event logs

As measurements are written or extended into measurement registers, one or more logs are written to the guest operating system's file system that record the measurement events that take place.

These event logs serve the following purposes:

  * A verifier can replay event logs to step through the Confidential VM instance's measurement process using simulated measurement registers. If the final digests calculated by the verifier match the final digests reported by the attester, this can increase trust that both the event log and the Confidential VM instance's boot process haven't been tampered with.

  * After replaying, a verifier can parse event logs to compare evidence against attestation policies. A verifier might require an attester to pass certain criteria such as having secure boot enabled, or using a specific Confidential Computing technology before a successful attestation result is returned.




Event logs are stored in the guest operating system's file system at the following locations:

Confidential Computing technology | MRs to verify | Log type | Guest OS path for event log replay  
---|---|---|---  
AMD SEV, AMD SEV-SNP, Intel TDX | vTPM platform configuration registers (PCRs) | Trusted Computing Group (TCG) Event Log | `/sys/kernel/security/tpm0/binary_bios_measurements`  
Intel TDX | `RTMR[0]`, `RTMR[1]`, `RTMR[2]` | Confidential Computing Event Log (CCEL) | `/sys/firmware/acpi/tables/data/CCEL`  
  
Learn more about event log replays and parsing.

### Quotes and attestation reports

The root of trust for reporting provides integrity and authenticity protection for the digests stored in the measurement register by signing their measurements with an attestation key. The resulting binary blob is known as a _PCR quote_ for vTPMs, an _attestation report_ for AMD SEV-SNP, and a _quote_ for Intel TDX.

What's in the binary blob is different for the different Confidential Computing technologies:

  * **AMD SEV** : The Shielded VM vTPM reads the values from one of its PCR banks (either SHA-1, SHA-256, or SHA-384), concatenates those values in numerical order, and then hashes the result with the same hashing algorithm as used for the PCR bank to create a summary digest. This summary digest, along with an optional nonce provided by a verifier, is placed into a `TPMS_ATTEST` structure and signed by the vTPM's private attestation key to create a PCR quote.

For details on the `TPMS_ATTEST` structure, see [Trusted Platform Module Library, Part 2: Structures (PDF)](https://trustedcomputinggroup.org/wp-content/uploads/TCG_TPM2_r1p59_Part2_Structures_pub.pdf).

  * **AMD SEV-SNP** : The AMD Secure Processor generates a SHA-384 digest, based on its initial [launch measurements](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/measurement-register-contents#snp) taken before the Confidential VM instance UEFI executes.

This digest, other VM data, and an optional nonce provided by a verifier are placed into an `ATTESTATION_REPORT` structure which is signed by the AMD Secure Processor's Version Chip Endorsement Key (VCEK) to create an attestation report.

For details on the `ATTESTATION_REPORT` structure, see [SEV Secure Nested Paging Firmware ABI Specification (PDF)](https://www.amd.com/content/dam/amd/en/documents/developer/56860.pdf).

  * **Intel TDX** : The TDX module places the MRTD and RTMR values, other VM data, and an optional nonce provided by a verifier into a `TDREPORT_STRUCT` structure.

Creating a quote is a multi-step process. First, the Provisioning Certification Enclave inside the CPU derives a provisioning certification key (PCK) from cryptographic secrets fused into the CPU. Then, the Quoting Enclave inside the CPU generates a private attestation key, which is signed with the provisioning certification key. The `TDREPORT_STRUCT` is then signed with the private attestation key to create a quote.

For details on the `TDREPORT_STRUCT` structure, see [Intel Trust Domain Extensions (Intel TDX) Module Base Architecture Specification (PDF)](https://cdrdv2-public.intel.com/853286/intel-tdx-module-base-spec-348549006.pdf).




### Endorsements

Different types of endorsements are used as evidence that a Confidential VM instance is running on expected hardware, vTPM, and firmware configurations.

#### Certificates

X.509 v3 certificates are used as evidence of genuine AMD or Intel hardware being used in the host, or that the Confidential VM instance is using a Shielded VM vTPM.

The name of the certificate is different for each of the Confidential Computing technologies:

  * **AMD SEV** : Attestation key (AK) certificate

  * **AMD SEV-SNP** : Version Chip Endorsement Key (VCEK) certificate

  * **Intel TDX** : Provisioning Certification Key (PCK) certificate




For AMD SEV, the certificate verifies the Shielded VM vTPM. The host makes a request to Google's certificate authority server, and auto-provisions the certificate directly into a Confidential VM instance's vTPM non-volatile storage. A guest can retrieve this certificate individually by requesting it from the vTPM with software such as [`go-tpm-tools`](https://github.com/google/go-tpm-tools).

For AMD SEV-SNP and Intel TDX, the host extracts hardware evidence from the CPU and presents it to a Google-managed cache. This cache stores certificates previously pulled from the AMD key distribution service and Intel provisioning certificate service. After successfully presenting the hardware evidence, the certificates are cached to the host's disk, and shared with the guest. A guest can retrieve these certificates individually to validate hardware with software such as [`go-sev-guest`](https://github.com/google/go-sev-guest) and [`go-tdx-guest`](https://github.com/google/go-tdx-guest).

The certificates contain the following information:

  * The certificate issuer identity, either AMD, Google, or Intel.

  * The public attestation key, which verifies the signature on PCR quotes (vTPM), attestation reports (SEV-SNP), and attestation quotes (Intel TDX).

  * Hardware attestation only: the hardware microcode and firmware TCB versions the host's firmware is running on.

  * Hardware attestation only: evidence that binds the certificate to a specific physical processor, which has been signed with a private key in the processor and can't be exfiltrated. For AMD SEV-SNP, this evidence is the _platform ID_. For Intel TDX, the evidence is the _platform manifest_.




#### Firmware

For hardware attestation, firmware _launch endorsements_ are available directly from VM instances or can be downloaded online. Launch endorsements are signed binary-serialized protocol buffers that are used to confirm that a Confidential VM instance's virtual firmware hasn't been tampered with.

When a VM starts, the AMD Secure Processor or Intel TDX module hashes the firmware binary before it executes. This SHA-384 digest is stored in the `MEASUREMENT` field for AMD SEV-SNP, and in the MRTD for Intel TDX.

You can use that digest to download a launch endorsement from Google, verify that the signature is rooted to Google with a tool such as [`gcetcbendorsement`](https://github.com/google/gce-tcb-verifier/tree/main/gcetcbendorsement/), and then verify that the SHA-384 digests match between the firmware measurement and what's recorded in the endorsement.

Beyond firmware verification, you might use certain properties in a launch endorsement to enforce an access policy, such as the minimum security version number (SVN), vCPU count, memory configuration, or the family ID of the UEFI.

For more information, see [Verify a Confidential VM instance's firmware](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/verify-firmware).

## Verifier event log replay and parsing

In addition to directly verifying evidence provided by an attester, a verifier can replay an event log provided by the attester to verify its integrity against its measurement register values.

To do so, the verifier creates a simulated version of each measurement register it needs to check as part of its attestation policy. It then populates that simulated register using events from an event log. If the final value of the simulated register matches the value stored in the equivalent, real measurement register, this increases trust that both the event log and the Confidential VM instance's boot process haven't been tampered with.

After a log has been verified in this way, it can be parsed for individual measurements that a verifier or relying party can base policy on.

### Build your own event log replay and parse tools

While you can build your own software to replay and parse event logs, we recommend you use established software like [`go-eventlog`](https://github.com/google/go-eventlog) to help you to avoid common pitfalls such as the [`EventType` vulnerability](https://github.com/google/go-attestation/blob/master/docs/event-log-disclosure.md) for the Trusted Computing Group and Confidential Computing Event Log formats.

If you still want to build your own replay and parse software, the following vTPM-based examples can help your initial understanding, although you should base your implementation off the event log generated by your own Confidential VM instance.

The following example has select events from an Ubuntu 24.04 vTPM event log, which measure into PCR 0. The event log has been converted from binary to ASCII with [`tpm2_eventlog`](https://github.com/tpm2-software/tpm2-tools) using the following command:
    
    
    sudo tpm2_eventlog /sys/kernel/security/tpm0/binary_bios_measurements
    

The PCR 0 events from the log are as follows:
    
    
    ---
    version: 1
    events:
    **- EventNum: 0**
      PCRIndex: 0
      EventType: EV_NO_ACTION
      Digest: "0000000000000000000000000000000000000000"
      EventSize: 41
      SpecID:
      - Signature: Spec ID Event03
        platformClass: 0
        specVersionMinor: 0
        specVersionMajor: 2
        specErrata: 0
        uintnSize: 2
        numberOfAlgorithms: 3
        Algorithms:
        - Algorithm[0]:
          algorithmId: sha1
          digestSize: 20
        - Algorithm[1]:
          algorithmId: sha256
          digestSize: 32
        - Algorithm[2]:
          algorithmId: sha384
          digestSize: 48
        vendorInfoSize: 0
    **- EventNum: 1**
      PCRIndex: 0
      EventType: EV_NO_ACTION
      DigestCount: 3
      Digests:
      - AlgorithmId: sha1
        Digest: "0000000000000000000000000000000000000000"
      - AlgorithmId: sha256
        Digest: "0000000000000000000000000000000000000000000000000000000000000000"
      - AlgorithmId: sha384
        Digest: "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
      EventSize: 160
      Event: "53503830302d313535204576656e7433792b000056aca511a145224ba54128607dac543b0d476f6f676c652c20496e632e0016476f6f676c6520436f6d7075746520456e67696e650001000d476f6f676c652c20496e632e00792b000004322e37000300000028000000468e85a27fa36a458c790c1fe48b65ff4600690072006d007700610072006500520049004d0000000000000000000000000000000000"
    **- EventNum: 2**
      PCRIndex: 0
      EventType: EV_NO_ACTION
      DigestCount: 3
      Digests:
      - AlgorithmId: sha1
        Digest: "0000000000000000000000000000000000000000"
      - AlgorithmId: sha256
        Digest: "0000000000000000000000000000000000000000000000000000000000000000"
      - AlgorithmId: sha384
        Digest: "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
      EventSize: 288
      Event: "53503830302d313535204576656e7433792b000056aca511a145224ba54128607dac543b0d476f6f676c652c20496e632e0016476f6f676c6520436f6d7075746520456e67696e650001000d476f6f676c652c20496e632e00792b000004322e370001000000a800000068747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f6763655f7463625f696e746567726974792f6f766d665f7836345f63736d2f3834383939616564336339653837363735666638303966356665613365366638383733353533643166303130306464623961653333323639323832356163636537333866343562646563323738613430393864316332376534393533373134332e66642e7369676e65640000000000000000000000000000"
    **- EventNum: 3**
      PCRIndex: 0
      EventType: EV_S_CRTM_VERSION
      DigestCount: 3
      Digests:
      - AlgorithmId: sha1
        Digest: "4031fe1129fb826f12dcad169992cca9f4f56aa3"
      - AlgorithmId: sha256
        Digest: "fa129a8f82b65bcbce8f9e8e5f6de509beff9b1df33714116bf918c5a3bba45d"
      - AlgorithmId: sha384
        Digest: "21d340a4a30bb8865486d150cd9ceb46100662b92f336d38b87d70b373ca15c4c60878336924baa818dc2aceaeb40ea6"
      EventSize: 48
      Event: "47004300450020005600690072007400750061006c0020004600690072006d0077006100720065002000760032000000"
    **- EventNum: 4**
      PCRIndex: 0
      EventType: EV_NONHOST_INFO
      DigestCount: 3
      Digests:
      - AlgorithmId: sha1
        Digest: "2b106cedd1631981619790bbc1afaa80cc6ecd3e"
      - AlgorithmId: sha256
        Digest: "6ac9241348a80c5755a63bcd1865b9f6d5720f6e925dc869bb4694281c1510c5"
      - AlgorithmId: sha384
        Digest: "1167e32c3814259ea4809234cccfbd2785c32bde882833bb199d6df6bd989a49f45663e63ce11699fcd01250050f042c"
      EventSize: 32
      Event: "474345204e6f6e486f7374496e666f0001000000000000000000000000000000"
    **- EventNum: 19**
      PCRIndex: 0
      EventType: EV_SEPARATOR
      DigestCount: 3
      Digests:
      - AlgorithmId: sha1
        Digest: "9069ca78e7450a285173431b3e52c5c25299e473"
      - AlgorithmId: sha256
        Digest: "df3f619804a92fdb4057192dc43dd748ea778adc52bc498ce80524c014b81119"
      - AlgorithmId: sha384
        Digest: "394341b7182cd227c5c6b07ef8000cdfd86136c4292b8e576573ad7ed9ae41019f5818b4b971c9effc60e1ad9f1289f0"
      EventSize: 4
      Event: "00000000"
    

When the Confidential VM instance is reset, its PCRs are initialized to zero. As events occur, the value in the SHA-256 bank of PCR 0 (`PCRIndex: 0`) changes as follows (`EV_NO_ACTION` events don't extend the register):

  1. The value of the register is concatenated with the SHA-256 digest of the next event assigned to PCR 0, `EV_S_CRTM_VERSION`. The concatenated result is SHA-256 hashed again, and then stored in the register. The SHA-256 hexdigest of PCR 0 is now `0c3684a7571193d76a68e489ded7bf186fc2fb1efe0c6dd9ce147960bbc57365`.

  2. The same process is used for the `EV_NONHOST_INFO` event. The SHA-256 hexdigest of PCR 0 is now `509f590b71fb22c9a6eef647e3c23611d13e599a6e15fdbb4db56ea4c2cb878d`.

  3. The same process is used for an `EV_SEPARATOR` event, which indicates the measurement extensions into a specific register are complete. The `EV_SEPARATOR` is a 32-bit zero value (`\x00*4`). This makes the final SHA-256 hexdigest of PCR 0 `a0b5ff3383a1116bd7dc6df177c0c2d433b9ee1813ea958fa5d166a202cb2a85`.




The following Python code demonstrates the previous procedure by creating a simulated Compute Engine PCR 0. The code isn't an event log replay, because it derives its event digests from known values. When creating a proper event log replay, you must read the digests in from your VM instance's event log instead.
    
    
    import hashlib
    
    def CalculatePCR0(version_num: int, mem_encrypt_enum: int):
      """Calculates the expected SHA-256 PCR 0 value given the
      Compute Engine firmware version and Confidential Computing technology
      that's in use.
    
      This code uses derived values for events instead of reading digests from an
      event log. It's intended to demonstrate how to simulate the extend function
      used in measurement registers.
    
      While the code should provide correct values for PCR 0 in
      Compute Engine VM instances, for other PCRs and true event log replay
      you should read in digests from an event log instead of using derived values.
    
      PCR 0 measurements include:
        * EV_S_CRTM_VERSION: The firmware version string, in UTF-16 little-endian
          form. This value remains stable as long as the firmware version stays the
          same.
        * EV_NONHOST_INFO: This value changes based on the Confidential Computing
          technology that's in use.
        * EV_SEPARATOR: A 32-bit zero value to split UEFI and bootloader
          measurements.
    
      Args:
        version_num (int): The Compute Engine firmware version number. The
          value is 2.
    
        mem_encrypt_enum (int): The type of Confidential Computing technology used
          on the VM:
    
          0: None
          1: AMD SEV
          2: AMD SEV-ES
          3: Intel TDX
          4: AMD SEV-SNP
    
      Returns:
        A hexstring representing the expected PCR 0 digest.
      """
      # Create a hash object to act as PCR 0, and initialize it with zeroes.
      h = hashlib.sha256()
      h.update(b'\x00' * h.digest_size)
    
      # Update the hash object with the EV_S_CRTM_VERSION event, with a hard-coded
      # firmware version `version_num`.
      #
      # This code uses derived values for events. To use the digest supplied in an
      # event log for event log replay, you need to read in the event digest, and
      # then convert it to bytes before updating the hash object, similar to the
      # following:
      #
      # h.update(bytes.fromhex('fa129a8f82b65bcbce8f9e8e5f6de509beff9b1df33714116bf918c5a3bba45d'))
      #
      h.update(
              hashlib.sha256(
                  # The firmware uses UCS-2 encoding, so we match it by encoding to
                  # the equivalent UTF-16 little-endian. An extra null byte is
                  # needed to match the required byte length.
                  f'GCE Virtual Firmware v{version_num}\x00'.encode('utf-16-le')).digest()
              )
    
      # Create a new hash object to act as PCR 0 and update it with the previous
      # hash object's digest. This simulates the first part of the register EXTEND
      # function.
      h2 = hashlib.sha256()
    
      h2.update(h.digest())
    
      # Update the hash object with the EV_NONHOST_INFO event, which includes
      # `mem_encrypt_enum`, the Confidential Computing technology in use. Performing
      # this update completes the simulated EXTEND function.
    
      h2.update(
              hashlib.sha256(
                  b'GCE NonHostInfo\x00'
                  + (mem_encrypt_enum).to_bytes(1, byteorder='little')
                  + (b'\x00' * 15)
                  ).digest()
              )
    
      # Create a new hash object to act as PCR 0 and update it with the previous
      # hash object's digest. This simulates the first part of the register EXTEND
      # function.
      h3 = hashlib.sha256()
      h3.update(h2.digest())
    
      # Update the hash object with the EV_SEPARATOR event. Performing this update
      # completes the simulated EXTEND function.
      h3.update(hashlib.sha256(b'\x00' * 4).digest())
    
      # There are more PCR 0 events, but they're all `EV_NO_ACTION` and don't
      # affect the register value. Return the final simulated register value.
      digest = h3.hexdigest()
      return digest
    
    print('\nPCR 0 simulation')
    print('\nConfidential Computing type\tDigest')
    # Compute Engine firmware version 2, no Confidential Computing
    # Expected hexdigest: d0c70a9310cd0b55767084333022ce53f42befbb69c059ee6c0a32766f160783
    print(f'None\t\t\t\t{CalculatePCR0(2, 0)}')
    
    # Compute Engine firmware version 2, AMD SEV
    # Expected hexdigest: a0b5ff3383a1116bd7dc6df177c0c2d433b9ee1813ea958fa5d166a202cb2a85
    print(f'AMD SEV\t\t\t\t{CalculatePCR0(2, 1)}')
    
    # Compute Engine firmware version 2, AMD SEV-SNP
    # Expected hexdigest: 50597a27846e91d025eef597abbc89f72bff9af849094db97b0684d8bc4c515e
    print(f'AMD SEV-SNP\t\t\t{CalculatePCR0(2, 4)}')
    
    # Compute Engine firmware version 2, Intel TDX
    # Expected hexdigest: 0cca9ec161b09288802e5a112255d21340ed5b797f5fe29cecccfd8f67b9f802
    print(f'Intel TDX\t\t\t{CalculatePCR0(2, 3)}')
    
    print()
    

## Relying party configuration

Depending on whether the passport model or background check model is used, the relying party receives the attestation results from either the attester or the verifier.

The relying party then verifies that the claims that it has received in the attestation results match the expected values. If the values match, the relying party allows the attester to access resources as a local identity.

A common pattern for configuring a relying party in Google Cloud is to use Workload Identity Federation, and treat the attester as a federated identity:

  1. Add your verifier as an OIDC provider to a [workload identity pool](https://docs.cloud.google.com/iam/docs/manage-workload-identity-pools-providers). After this, the service account attached to your Confidential VM instance workload can act as a federated identity and access the required resources.

  2. Define the values that the verifier attestation claims must match for the attester to be granted access to resources.

In Google Cloud, this involves [mapping attestation claims to attributes](https://docs.cloud.google.com/iam/docs/workload-identity-federation#mapping) so that Identity and Access Management (IAM) can process them as [conditions](https://docs.cloud.google.com/iam/docs/workload-identity-federation#conditions) that a federated identity must pass to authenticate as a principal.

You can then give the attester direct access to resources by adding a role binding for its federated principal to the [allow policies](https://docs.cloud.google.com/iam/docs/allow-policies) of the needed resources. For [services that don't support federated identities](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services), you can provide access to resources through [service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation).




As an alternative to Workload Identity Federation, you can write code to parse an [attestation token's claims](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/token-claims) directly. For an example, see [vTPM Remote Attestation on Confidential Virtual Machine](https://codelabs.developers.google.com/codelabs/vtpm-remote-attestation-on-confidential-virtual-machine).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
