---
url: https://docs.cloud.google.com/docs/security/remote-attestation/
title: Remote attestation of disaggregated machines \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:40.952900+00:00
---

# Remote attestation of disaggregated machines  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/remote-attestation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Remote attestation of disaggregated machines Stay organized with collections  Save and categorize content based on your preferences. 

_This content was last updated in May 2024, and represents the status quo as of the time it was written. Google's security policies and systems may change going forward, as we continually improve protection for our customers._

This document describes the Google approach to data center machine attestation. The architecture described in this document is designed to be integrated with open standards such as [Trusted Platform Module (TPM)](https://trustedcomputinggroup.org/work-groups/trusted-platform-module/), [Security Protocol and Data Model (SPDM)](https://www.dmtf.org/content/dmtf-releases-security-specification-12), and [Redfish](https://www.dmtf.org/standards/redfish). For new standards or reference implementations that are proposed by Google and related to data center machine attestation, see our [Platform Integrity (PINT)](https://github.com/google/PINT) project in GitHub. This document is intended for security executives, security architects, and auditors.

## Overview

Increasingly, Google designs and deploys disaggregated data center machines. Instead of a single root of trust, many machines contain separate roots of trust, including roots of trust for measurement (RTM), storage, update, and recovery. Each RTM serves a subsection of the entire machine. For example, a machine might have one RTM that measures and attests to what was booted on the main CPU, and another RTM that measures and attests to what was booted on a SmartNIC that is plugged into a PCIe slot. The following diagram shows an example machine.

![An example machine.](https://docs.cloud.google.com/static/docs/security/images/remote-attestation-example-dc.svg)

The complexity of multiple RTMs in a machine adds to the enormous scale and expectations of data center machines, and many complications that can occur because of human, hardware, or software faults. In summary, ensuring firmware integrity of our fleet is a non-trivial endeavor.

The system described in this document is designed to make the problem of remote attestation for disaggregated machines more manageable. This attestation infrastructure is extensible, letting it adapt to serve ever-more-complex machines as they appear in the data center.

By sharing this work, we aim to provide our perspective on how disaggregated machine attestation can be done at scale. Through collaboration with industry partners and contributions to standards bodies such as Distributed Management Task Force (DMTF), Trusted Computing Group (TCG), and Open Compute Project (OCP), we intend to continue supporting security innovation in this space.

## Recommended RTM properties

This section introduces some properties that we recommend for RTMs.

### RTM hardware integration

When a processor is paired with an RTM, the RTM should capture measurements over the first mutable code that runs on that processor. Subsequent mutable code should have its measurements captured and reported to a root of trust before the code runs. This arrangement produces a measured boot chain that allows for robust attestation of the security-critical state of the processor.

### RTM hardware and firmware identity attestation

Each RTM should have a signing key pair that is used to emit attestations for external validation. The certificate chain for this key pair should include cryptographic evidence of the RTM's unique _hardware identity_ and the _firmware identity_ for any mutable code that runs within the RTM. The certificate chain should be rooted in the RTM manufacturer. This approach lets machines recover from critical RTM firmware vulnerabilities.

The [Device Identifier Composition Engine (DICE)](https://trustedcomputinggroup.org/work-groups/dice-architectures) specification is a formalization of the pattern that is used in our attestation solution. The RTM manufacturer certifies a unique device key pair, which certifies an alias key pair that is specific to the RTM's hardware identity and firmware image. The alias key certificate chain contains a measurement of the RTM firmware and the RTM's serial number. Verifiers can be confident that any data signed by a given alias key was emitted from an RTM that is described by the cryptographic hardware and firmware identity measurements that are embedded within that alias key's certificate chain.

## Remote attestation operations

The attestation scheme is designed to ensure that user data and jobs are only issued to machines that are running their intended boot stack, while still allowing fleet maintenance automation to occur at scale to remediate issues. The job scheduler service, hosted in our internal cloud, can challenge the collection of RTMs within the machine, and compare the resulting attested measurements to a policy that is unique to that machine. The scheduler only issues jobs and user data to machines if the attested measurements conform to the machine's policy.

Remote attestation includes the following two operations:

  * Attestation policy generation, which occurs whenever a machine's intended hardware or software is changed.

  * Attestation verification, which occurs at defined points in our machine management flows. One of these points is just before work is scheduled on a machine. The machine only gains access to jobs and user data after attestation verification passes.




## The attestation policy

Google uses a signed machine-readable document, referred to as a _policy_ , to describe the hardware and software that is expected to be running within a machine. This policy can be attested by the machine's collection of RTMs. The following details for each RTM are represented in the policy:

  * The trusted _identity root certificate_ that can validate attestations that are emitted by the RTM.
  * The globally unique _hardware identity_ that uniquely identifies the RTM.
  * The _firmware identity_ that describes the expected version that the RTM should be running.
  * The _measurement expectations_ for each boot stage that is reported by the RTM.
  * An _identifier for the RTM_ , analogous to a [Redfish resource name](https://www.dmtf.org/sites/default/files/standards/documents/DSP2046_2021.1.pdf).
  * An _identifier that links the RTM to its physical location_ within a machine. This identifier is analogous to a [Redfish resource](https://www.dmtf.org/sites/default/files/standards/documents/DSP2046_2021.1.pdf) name, and is used by automated machine repair systems.



In addition, the policy also contains a globally unique revocation serial number that helps prevent unauthorized policy rollback. The following diagram shows a policy.

![An example attestation policy.](https://docs.cloud.google.com/static/docs/security/images/remote-attestation-policy.svg)

The diagram shows the following items in the policy:

  * The signature provides policy authentication.
  * The revocation serial number provides policy freshness to help prevent rollback.
  * The RTM expectations enumerate details for each RTM in the machine.



The following sections describe these items in more detail.

### Policy assembly

When a machine's hardware is assembled or repaired, a hardware model is created that defines the expected RTMs on that machine. Our control plane helps ensure that this information remains current across events such as repairs that involve part swaps or hardware upgrades.

In addition, the control plane maintains a set of expectations about the software that is intended to be installed on a machine, along with expectations about which RTMs should measure which software. The control plane uses these expectations, along with the hardware model, to generate a signed and revocable attestation policy that describes the expected state of the machine.

The signed policy is then written to persistent storage on the machine that it describes. This approach helps reduce the number of network and service dependencies that are needed by the remote verifier when attesting a machine. Rather than query a database for the policy, the verifier can fetch the policy from the machine itself. This approach is an important design feature, as the job schedulers have strict SLO requirements and must remain highly available. Reducing the network dependencies of these machines on other services helps to reduce the risk of outages. The following diagram shows this flow of events.

![Policy assembly flow.](https://docs.cloud.google.com/static/docs/security/images/remote-attestation-control-plane.svg)

The diagram describes the following steps that the control plane completes in the policy assembly process:

  * Derives the attestation policy from the software package assignment and machine hardware model.
  * Signs the policy.
  * Stores the policy on the data center machine.



### Policy revocation

The hardware and software intent for a given machine changes over time. When the intent changes, old policies must be revoked. Each signed attestation policy includes a unique revocation serial number. Verifiers obtain the appropriate public key for authenticating a signed policy, and the appropriate certificate revocation list for ensuring that the policy is still valid.

Interactively querying a key server or revocation database affects the job schedulers' availability. Instead, Google uses an asynchronous model. The set of public keys that are used to authenticate signed attestation policies are pushed as part of each machine's base operating system image. The CRL is pushed asynchronously using the same centralized revocation deployment system that Google uses for other credential types. This system is already engineered for reliable operation during normal conditions, with the ability to perform rapid emergency pushes during incident response conditions.

By using verification public keys and CRL files that are stored locally on the verifier's machine, verifiers can validate attestation statements from remote machines without having any external services in the critical path.

## Retrieving attestation policies and validating measurements

The process of remotely attesting a machine consists of the following stages:

  * Retrieving and validating the attestation policy.
  * Obtaining attested measurements from the machine's RTMs.
  * Evaluating the attested measurements against the policy.



The following diagram and sections describe these stages further.

![Remote attestation stages.](https://docs.cloud.google.com/static/docs/security/images/remote-attestation-stages.svg)

### Retrieving and validating the attestation policy

The remote verifier retrieves the signed attestation policy for the machine. As mentioned in Policy assembly, for availability reasons, the policy is stored as a signed document on the target machine.

To verify that the returned policy is authentic, the remote verifier consults the verifier's local copy of the relevant CRL. This action helps ensure that the retrieved policy was cryptographically signed by a trusted entity and that the policy wasn't revoked.

### Obtaining attested measurements

The remote verifier challenges the machine, requesting measurements from each RTM. The verifier ensures freshness by including cryptographic nonces in these requests. An on-machine entity, such as a baseboard management controller (BMC), routes each request to its respective RTM, gathers the signed responses, and sends them back to the remote verifier. This on-machine entity is unprivileged from an attestation perspective, as it serves only as a transport for the RTM's signed measurements.

Google uses internal APIs for attesting to measurements. We also contribute enhancements to Redfish to enable off-machine verifiers to challenge a BMC for an RTM's measurements by using SPDM. Internal machine routing is done over implementation-specific protocols and channels, including the following:

  * Redfish over subnet
  * Intelligent Platform Management Interface (IPMI)
  * Management Component Transport Protocol (MCTP) over i2c/i3c
  * PCIe
  * Serial Peripheral Interface (SPI)
  * USB



### Evaluating attested measurements

Google's remote verifier validates the signatures that are emitted by each RTM, ensuring that they root back to the RTM's identity that is included in the machine's attestation policy. Hardware and firmware identities that are present in the RTM's certificate chain are validated against the policy, ensuring that each RTM is the correct instance and runs the correct firmware. To ensure freshness, the signed cryptographic nonce is checked. Finally, the attested measurements are evaluated to ensure that they correspond with the policy's expectations for that device.

## Reacting to remote attestation results

After attestation is complete, the results must be used to determine the fate of the machine being attested. As shown in the diagram, there are two possible results: the attestation is successful and the machine is issued task credentials and user data, or the attestation fails and alerts are sent to the repairs infrastructure.

![Remote attestation results.](https://docs.cloud.google.com/static/docs/security/images/remote-attestation-results.svg)

The following sections provide more information about these processes.

### Failed attestation

If attestation of a machine isn't successful, Google doesn't use the machine to serve customer jobs. Instead, an alert is sent to the repairs infrastructure, which attempts to automatically reimage the machine. Although attestation failures might be due to malicious intent, most attestation failures are due to bugs in software rollouts. Therefore, rollouts with rising attestation failures are stopped automatically to help prevent more machines from failing attestation. When this event occurs, an alert is sent to SREs. For machines that aren't fixed by automated reimaging, the rollout is rolled back, or there is a rollout of fixed software. Until a machine undergoes successful remote attestation again, it isn't used to serve customer jobs.

### Successful attestation

If remote attestation of a machine is successful, Google uses the machine to serve production jobs such as VMs for Google Cloud customers or image processing for Google Photos. Google requires meaningful job actions that involve networked services to be gated behind short-lived [LOAS](https://www.usenix.org/system/files/login/articles/login_winter16_05_cittadini.pdf) task credentials. These credentials are granted over a secure connection after a successful attestation challenge, and provide privileges required by the job. For more information about these credentials, see [Application Layer Transport Security](https://docs.cloud.google.com/docs/security/encryption-in-transit/application-layer-transport-security).

Software attestation is only as good as the infrastructure that builds that software. To help ensure that resulting artifacts are an accurate reflection of our intent, we have invested significantly in the integrity of our build pipeline. For more information about a standard that was proposed by Google to address software supply chain integrity and authenticity, see [Software Supply Chain Integrity](https://www.nist.gov/system/files/documents/noindex/2021/06/08/Google%20NIST%20statement%20on%20%285%29%20integrity.pdf).

## What's next

Learn how [BeyondProd](https://docs.cloud.google.com/docs/security/beyondprod) helps Google's data center machines establish secure connections.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
