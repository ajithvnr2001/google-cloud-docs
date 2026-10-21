---
url: https://docs.cloud.google.com/docs/security/physical-to-logical-space/
title: How Google protects the physical-to-logical space in a data center \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:22:37.188035+00:00
---

# How Google protects the physical-to-logical space in a data center  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/physical-to-logical-space/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  How Google protects the physical-to-logical space in a data center Stay organized with collections  Save and categorize content based on your preferences. 

_This content was last updated in May 2024, and represents the status quo as of the time it was written. Google's security policies and systems may change going forward, as we continually improve protection for our customers._

Each Google data center is a large and diverse environment of machines, networking devices, and control systems. Data centers are designed as industrial complexes that require a wide range of roles and skills to manage, maintain, and operate.

In these complex environments, the security of your data is our top priority. Google implements [six layers of physical controls (video)](https://www.youtube.com/watch?v=kd33UVZhnAA) and many [logical controls](https://docs.cloud.google.com/docs/security/infrastructure/design) on the machines themselves. We also continuously model threat scenarios in which certain controls fail or aren't applied.

Some threat scenarios model insider risk and assume that an attacker already has legitimate access to the data center floor. These scenarios reveal a space between physical and logical controls that also requires defense in depth. That space, defined as _arms-length from a machine in a rack to the machine's runtime environment,_ is known as the _physical-to-logical space_.

The physical-to-logical space is similar to the physical environment around your mobile phone. Even though your phone is locked, you only give physical access to people who have a valid reason for access. Google takes the same approach to the machines that hold your data.

## Physical-to-logical controls summary

Within the physical-to-logical space, Google uses three controls that work together:

  * **Hardware hardening:** Reduce each machine's physical access paths, known as the _attack surface_ , in the following ways: 
    * Minimize physical access vectors, like ports.
    * Lock down remaining paths at the firmware level, including the basic input/output system (BIOS), any management controllers, and peripheral devices.
  * **Anomalous event detection:** Generate alerts when physical-to-logical controls detect anomalous events.
  * **System self-defense:** Recognize a change in the physical environment and respond to threats with defensive actions.



Together, these controls provide a defense-in-depth response to security events that occur in the physical-to-logical space. The following diagram shows all three controls that are active on a secure rack enclosure.

![The three controls that are active on a secure rack enclosure.](https://docs.cloud.google.com/static/docs/security/images/rack_protections.svg)

## Hardware hardening

Hardware hardening helps to reduce the physical attack surface to minimize residual risks. 

A conventional enterprise data center has an open floor plan and rows of racks with no barriers between the front panel and people on the data center floor. Such a data center might have machines with many external ports—such as USB-A, Micro-USB, or RJ-45—that increase the risk of an attack. Anyone with physical access to the data center floor can quickly and easily access removable storage or plug a USB stick with malware into an exposed front panel port. Google data centers use _hardware hardening_ as a foundational control to help mitigate these risks.

Hardware hardening is a suite of preventative measures on the rack and its machines that helps reduce the physical attack surface as much as possible. Hardening on machines include the following:

  * Remove or disable exposed ports and lock down remaining ports at the firmware level.
  * Monitor storage media with high-fidelity tamper-detection signals.
  * [Encrypt data at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption#default_encryption_of_data_at_rest).
  * Where supported by the hardware, use device attestation to help prevent unauthorized devices from deploying in the runtime environment.



In certain scenarios, to help ensure that no personnel have physical access to machines, Google also installs secure rack enclosures that help to prevent or deter tampering. The secure rack enclosures provide an immediate physical barrier to passersby and can also trigger alarms and notifications for security personnel. Enclosures, combined with the machine remediations discussed earlier, provide a powerful layer of protection for the physical-to-logical space.

The following images illustrate the progression from fully open racks to secure rack enclosures with full hardware hardening.

  * The following image shows a rack with no hardware hardening:

![A rack with no hardware hardening.](https://docs.cloud.google.com/static/docs/security/images/no-hardware-hardening.png)

  * The following image shows a rack with some hardware hardening:

![A rack with some hardware hardening.](https://docs.cloud.google.com/static/docs/security/images/some-hardware-hardening.png)

  * The following image shows the front and back of a rack with full hardware hardening:

![The front and back of a rack with full hardware hardening.](https://docs.cloud.google.com/static/docs/security/images/full-hardware-hardening.png)




## Anomalous event detection

Anomalous event detection lets security staff know when machines experience unexpected events. 

Industry-wide, organizations can take months or years to discover security breaches, and often only after significant damage or loss has occurred. The critical indicator of compromise (IoC) might be lost in a high volume of logging and telemetry data from millions of production machines. Google, however, uses multiple data streams to help identify potential physical-to-logical security events in real time. This control is called _anomalous event detection_.

Modern machines monitor and record their physical state as well as events that occur in the physical-to-logical space. Machines receive this information through ever-present automated system software. This software may run on miniature computers inside the machine, called _baseboard management controllers (BMCs)_ , or as part of an operating system daemon. This software reports important events such as login attempts, insertion of physical devices, and sensor alarms such as an enclosure tamper sensor.

For machines with hardware root-of-trust, anomalous event detection signals become even stronger. Hardware root-of-trust allows system software, such as BMC firmware, to attest that it booted safely. Google detection systems, therefore, have an even higher degree of confidence that reported events are valid. For more information about independent roots of trust, see [Remote attestation of disaggregated machines](https://docs.cloud.google.com/docs/security/remote-attestation).

## System self-defense

System self-defense lets systems respond to potential compromises with immediate defensive action. 

Some threat scenarios assume that an attacker in the physical-to-logical space can defeat the physical access measures discussed in Hardware hardening. Such an attacker might be targeting user data or a sensitive process that is running on a machine.

To mitigate this risk, Google implements _system self-defense_ : a control that provides an immediate and decisive response to any potential compromise. This control uses the telemetry from the physical environment to act in the logical environment.

Most large-scale production environments have multiple physical machines in one rack. Each physical machine runs multiple workloads, like virtual machines (VMs) or Kubernetes containers. Each VM runs its own operating system using dedicated memory and storage.

To determine which workloads are exposed to security events, Google aggregates the telemetry data from the hardware-hardening controls and anomalous event detection. We then correlate the data to generate a small set of events that are high-risk and require immediate action. For example, the combination of a secure rack door alarm and a machine chassis opening signal might constitute a high-risk event.

When Google detects these events, systems can take immediate action:

  * Exposed workloads can immediately terminate sensitive services and wipe any sensitive data.
  * The networking fabric can isolate the affected rack.
  * The affected workloads can be rescheduled on other machines or even data centers, depending on the situation.



Because of the system self-defense control, even if an attacker succeeds in getting physical access to a machine, the attacker can't extract any data and can't move laterally in the environment.

## What's next

  * For more information about physical controls, read about [data center security](https://www.google.com/about/datacenters/data-security/).
  * For more information about logical controls, read [Google infrastructure security design overview](https://docs.cloud.google.com/docs/security/infrastructure/design).
  * To learn about Google security culture, read [Building secure and reliable systems (O'Reilly book)](https://www.oreilly.com/library/view/building-secure-and/9781492083115/).



  


Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
