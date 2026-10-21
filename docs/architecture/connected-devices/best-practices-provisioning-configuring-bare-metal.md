---
url: https://docs.cloud.google.com/architecture/connected-devices/best-practices-provisioning-configuring-bare-metal/
title: Best practices for automatically provisioning and configuring edge and bare metal systems and servers \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:17.393411+00:00
---

# Best practices for automatically provisioning and configuring edge and bare metal systems and servers  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/connected-devices/best-practices-provisioning-configuring-bare-metal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Best practices for automatically provisioning and configuring edge and bare metal systems and servers Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-31 UTC

This document suggests best practices for designing and implementing reliable and automated provisioning and configuration processes for devices running at the [edges of your environment](https://www.lfedge.org/2020/08/18/breaking-down-the-edge-continuum/) such as the following:

  * Edge devices, such as [Internet of Things](https://en.wikipedia.org/wiki/Internet_of_things) (IoT) devices, [microcomputers](https://en.wikipedia.org/wiki/Microcomputer) and [microcontrollers](https://en.wikipedia.org/wiki/Microcontroller)
  * [Bare metal systems and servers](https://en.wikipedia.org/wiki/Bare-metal_server)



Read this document if you design provisioning and configuration processes for edge devices and bare metal systems and servers, or if you want to learn more about best practices for provisioning and configuring these device types.

This document doesn't list all of the possible best practices for provisioning and configuring edge and bare metal systems and servers, and it doesn't give you guarantees of success. Instead, it helps you to stimulate discussions about potential changes and improvements to your provisioning and configuration processes.

This document is part of a series of documents that provide information about IoT architectures on Google Cloud. The other documents in this series include the following:

  * [Connected device architectures on Google Cloud overview](https://docs.cloud.google.com/architecture/connected-devices)
  * [Standalone MQTT broker architecture on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/mqtt-broker-architecture)
  * [IoT platform product architecture on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/iot-platform-product-architecture)
  * [Device on Pub/Sub architecture to Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/device-pubsub-architecture)
  * [Best practices for running an IoT backend on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/bps-running-iot-backend-securely)
  * Best practices for automatically provisioning and configuring edge and bare metal systems and servers (this document)



Manually provisioning and configuring a large fleet of devices is prone to human error and doesn't scale as your fleet grows. For example, you might forget to run a critical provisioning or configuration task, or you might be relying on partially or fully undocumented processes. Fully automated and reliable provisioning and configuration processes help solve these issues. They also help you manage the lifecycle of each device from manufacture to decommissioning to disposal.

## Terminology

The following terms are important for understanding how to implement and build automated provisioning and configuration processes for your devices:

  * **Edge device:** A device that you deploy at the edges of your environment that is proximate to the data you want to process.
  * **Provisioning process:** The set of tasks that you must complete to prepare a device for configuration.
  * **Configuration process:** The set of tasks you must complete to make a device ready to operate in a specific environment.
  * **Configuration management:** The set of tasks that you continuously perform to manage the configuration of your environment and devices.
  * **Base image:** A minimal working operating system (OS) or firmware image produced by your company or produced by a device or OS manufacturer.
  * **Golden image:** An immutable OS or firmware image that you create for your devices or prepare from a base image. Golden images include all data and configuration information that your devices need to accomplish their assigned tasks. You can prepare various golden images to accomplish different tasks. Synonyms for golden image types include _flavors_ , _spins_ , and _archetypes_.
  * **Silver image:** An OS or firmware image that you prepare for your devices by applying minimal changes to a golden image or a base image. Devices running a silver image complete their provisioning and configuration upon the first boot, according to the needs of the use cases that those devices must support.
  * **Seed device:** A device that bootstraps your environment without external dependencies.
  * **Network booting:** The set of technologies that lets a device obtain software and any related configuration information from the network, instead of from a storage system that's attached to the device.



To help you set goals and avoid common issues, apply the best practices for provisioning and configuration that are described in the following sections.

## Automate the provisioning and configuration processes

During their first boot, or anytime it's necessary, your devices should be able to provision and configure themselves using only the software image installed inside them.

To avoid implementing the logic you need during the provisioning and configuration processes, you can use tools that give you the primitives needed to orchestrate and implement those processes. For example, you can use [cloud-init](https://cloudinit.readthedocs.io/en/latest/) and its [NoCloud data source](https://cloudinit.readthedocs.io/en/latest/reference/datasources/nocloud.html), together with scripting or a configuration management tool, such as [Ansible](https://www.ansible.com/), [Puppet](https://puppet.com/), or [Chef](https://www.chef.io/), running against the local host.

To design reliable provisioning and configuration processes, ensure that all the steps and tasks performed during those processes are valid, possibly in an automated manner. For example, you can use an automated compliance testing framework, such as [InSpec](https://community.chef.io/tools/chef-inspec), to verify that your provisioning and configuration processes are operating as expected.

This best practice helps you avoid single points of failure and the need for manual intervention when you need to complete device provisioning and configuration.

## Avoid special-purpose devices

When designing your edge devices, minimize their variance in terms of purpose and specialty. This recommendation doesn't mean that all your edge devices must be equal to each other or share the same purpose, but they should be as homogeneous as possible. For example, you might define device archetypes by the workload types they need to support. Then you can deploy and manage your devices according to the properties of those archetypes.

To ensure that you're following this best practice, verify that you can pick a device at random from the ones of a given archetype and then do the following:

  * Treat the device like you would other devices of the same archetype. Doing so shows that you have operational efficiency.
  * Replace the device with devices of the same archetype without additional customizations. Doing so shows that you have correctly implemented those archetypes.



This best practice ensures that you reduce the variance in your fleet of devices, leading to less fragmentation in your environment and in the provisioning and configuration processes.

## Use seed devices to bootstrap your environment

When provisioning and configuring your devices, you might come across a circular dependency problem: your devices need supporting infrastructure to provision and configure themselves, but that infrastructure isn't in place because you still have to provision and configure it.

You can solve this problem with seed devices. Seed devices have a temporary special purpose. After completing the tasks for which the special purpose was designed, the device conforms its behavior and status to the relevant archetype.

For example, if you're using cloud-init to automatically initialize your devices, you might need to configure a cloud-init NoCloud data source in the following ways:

  1. Provide the NoCloud data source data to the seed device through a file system.
  2. Wait for the seed device to complete its own provisioning and configuration with its special purpose, which includes serving the NoCloud data source data to other devices over the network.

The provisioning and configuration processes on the seed device then wait until the conditions to drop the seed device's temporary special purpose are met. Some examples of these conditions are:

     * Are there other devices in the environment that serve the NoCloud data source data over the network?
     * Are there enough nodes in the cluster?
     * Did the first backup complete?
     * Is the disaster recovery site ready?
  3. Provision and configure other devices that download the NoCloud data source data over the network from the seed device. Some devices must be able to serve the NoCloud data source data over the network.

  4. The provisioning and configuration processes on the seed device resume because the conditions to drop the special purpose of the seed device are met: there are other devices in the fleet that serve the NoCloud data source data over the network.

  5. The provisioning and configuration processes on the seed device drop the special purpose, making the seed device indistinguishable from other devices of the same archetype.




This best practice ensures that you can bootstrap your environment even without supporting infrastructure and without contravening the Avoid special-purpose devices best practice.

## Minimize the statefulness of your devices

When designing your edge devices, keep the need to store stateful information at minimum. Edge devices might have limited hardware resources, or be deployed in harsh environments. Minimizing the stateful information that they need to function simplifies the provisioning, configuration, backup, and recovery processes because you can treat such devices homogeneously. If a stateless edge device starts to malfunction and it's not recoverable, for example, you can swap it with another device of the same archetype with minimal disruptions or data loss.

This best practice helps you avoid unanticipated issues due to data loss, or due to your processes being too complex. Most complexity comes from the need to support a fleet of heterogeneous devices.

## Automatically build OS and firmware images

To avoid expensive provisioning and configuration tasks when your devices first boot, and to spare device resources, customize the OS and firmware images before making them available. You could, for example, install dependencies directly in the image instead of installing them when each device boots for the first time.

When preparing the OS and firmware images for your devices, you start from a base image. When you customize the base image, you can do the following:

  * Produce golden images. Golden images contain all dependencies in the image so that your devices don't have to install those dependencies on first boot. Producing golden images might be a complex task, but they enable your devices to save time and resources during provisioning and configuration.
  * Produce silver images. Unlike golden images, devices running silver images complete all provisioning and configuration processes during their first boot. Producing silver images can be less complex than producing golden images, but the devices running a silver image spend more time and resources during provisioning and configuration.



You can customize the OS and firmware images as part of your continuous integration and continuous deployment (CI/CD) processes, and automatically make the customized images available to your devices after validation. The CI/CD processes that you implement with a tool such as [Cloud Build](https://docs.cloud.google.com/build/docs), [GitHub Actions](https://github.com/features/actions), [GitLab CI/CD](https://docs.gitlab.com/ee/ci/), or [Jenkins](https://www.jenkins.io/), can perform the following sequence of tasks:

  1. Perform an automated validation against the customized images.
  2. Publish the customized images in a repository where your devices can obtain them.



If your CI/CD environment and the OS or firmware for which you need to build images use different hardware architectures, you can use tools like [QEMU](https://www.qemu.org/) to emulate those architectures. For example, you can emulate the hardware architecture of the [ARM family](https://en.wikipedia.org/wiki/ARM_architecture) on an [x86_64 architecture](https://en.wikipedia.org/wiki/X86-64).

To customize your OS or firmware images, you need to be able to modify them and verify those modifications in a test environment before installing them in your edge devices. Tools like [chroot](https://en.wikipedia.org/wiki/Chroot) let you virtually change but not physically change the root directory before running a command.

This best practice helps you customize OS and firmware images before making the images available to your devices.

## Reliably orchestrate workloads running on your devices

If your devices support heterogeneous workloads, you can use the following tools to orchestrate those workloads and manage their lifecycle:

  * **A workload orchestration system:** Using a workload orchestration system, such as [Kubernetes](https://kubernetes.io), is suitable for workloads that have complex orchestration or lifecycle management requirements. These systems are also suitable for workloads that span multiple components. In both cases, it means you don't have to implement that orchestration and workload lifecycle management logic by yourself. If your devices are resource-constrained, you can install a lightweight Kubernetes distribution that needs fewer resources than the canonical one, such as [MicroK8s](https://microk8s.io/), [K3s](https://k3s.io/), or [Google Distributed Cloud installed with the edge profile](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/creating-clusters/standalone-cluster-creation).
  * **An init system:** Using an [init system](https://en.wikipedia.org/wiki/Init), like [systemd](https://en.wikipedia.org/wiki/Systemd), is suitable for workloads with the following characteristics:

    * Simple orchestration requirements
    * A lack of resources to support a workload orchestration system
    * Workloads that can't be placed in containers



After you have system in place to orchestrate your workloads, you can also use it to run tasks that are part of your provisioning and configuration processes. If you need to run a configuration management tool as part of your provisioning and configuration processes, for example, you can use the workload orchestration system as you would with any other workload.

This best practice helps ensure that you can orchestrate the workloads running on your devices.

## Verify, authenticate, and connect devices

When you need to verify if your devices need to connect to external systems, such as other devices or to a backend, consider the recommendations in the following subsections.

This best practice helps you:

  * Design secure communication channels for your devices.
  * Avoid potential backdoors that circumvent the security perimeter of your devices.
  * Verify that your devices don't expose unauthorized interfaces that an attacker might exploit.



### Connection practices to enforce

  * Authenticate other parties that are making information requests before exchanging any information.
  * Verify that transmitted information isn't traveling across unexpected channels.
  * Rely on trusted execution environments to handle secrets, such as encryption keys, authentication keys, and passwords.
  * Verify the integrity and the authenticity of any OS or firmware image before use.
  * Verify the validity, the integrity, and the authenticity of any user-provided configuration.
  * Limit the attack surface by not installing unnecessary software and removing any that already exists on your devices.
  * Limit the use of privileged operations and accounts.
  * Verify the integrity of the device's case if that case needs to resist physical manipulation and tampering.



### Connection practices to avoid

  * Don't transmit sensitive information over unencrypted channels.
  * Avoid leaving privileged access open, such as the following: 
    * Virtual or physical [serial ports and serial consoles](https://en.wikipedia.org/wiki/Serial_port) with elevated privileges, even if the ports are accessible only if someone physically tampers with the device.
    * Endpoints that respond to requests coming from the network and that can run privileged operations.
  * Don't rely on hardcoded credentials in your OS or firmware images, configuration, or source code.
  * Don't reveal any information that might help an adversary gather information to gain elevated privileges. For example, you should encrypt data on your devices and turn off unneeded tracing and logging systems on production devices.
  * Don't let users and workloads execute arbitrary code.



## Monitor your devices

Gathering information about the state of your devices without manual intervention is essential for the reliability of your environment. Ensure that your devices automatically report all the data that you need. There are two main reasons to gather and monitor data:

  * To help you ensure that your devices are working as intended.
  * To proactively spot issues and perform preventive maintenance.



For example, you can collect monitoring metrics and events with [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs).

To help you investigate and troubleshoot issues, we recommend that you design and implement processes to gather high resolution diagnostic data, such as detailed monitoring, tracing and debugging information, on top of the processes that monitor your devices during their normal operation. Gathering high resolution diagnostic data and transferring it by using a network can be expensive in terms of device resources, such as computing, data storage, and electrical power. For this reason, we recommend that you enable processes to gather high resolution diagnostic data only when needed, and only for the devices that need further investigation. For example, if one of your devices is not working as intended, and the regular monitoring data that the device reports is not enough to thoroughly diagnose the issue, you can enable high resolution data gathering for that device so it reports more information that can help you investigate the causes of the issue.

This best practice ensures that you don't leave devices in an unknown state, and that you have a enough data to determine whether and how your devices are performing.

## Support unattended booting and upgrades

When you design your provisioning and configuration processes, ensure that your devices are capable of unattended booting and that you have the necessary infrastructure in place. By implementing an unattended booting mechanism that supports both the first boot and the delivery of over-the-air upgrades, you increase the maintainability of your infrastructure. Using unattended booting frees you from manually attending to each device as it boots or upgrades. Manually attending a large fleet of devices is error-prone because operators might miss or incorrectly perform actions, or they might not have enough time to perform the required actions for every device in the fleet.

Also, you don't have to prepare each device in advance to boot the correct OS or firmware image. You can release a new version of an OS or firmware image, for example, and make that version available as one of the options that your devices can choose when they take their boot instructions from the network.

This best practice helps you ensure that your devices can perform boots and upgrades that are automated and unattended.

## Design and implement resilient processes

Even with fully automated provisioning and configuration processes, errors can occur that prevent those processes from correctly completing, thus leaving your devices in an inconsistent state. Help ensure that your devices are able to recover from such failures by implementing retry and fallback mechanisms. When a device fails to complete a task that's part of the provisioning and configuration processes, for example, it should automatically attempt to recover from that failure. After the device recovers from the failure or falls back to a working state, it can resume running processes from the point at which the processes failed.

This best practice helps you design and implement resilient provisioning and configuration processes.

## Support the whole lifecycle of your devices

When designing your provisioning and configuration processes, ensure that those processes can manage the entire device lifecycle. Effectively managing device lifecycles includes planning for termination and disposal, even if your devices are supposed to run for a relatively long time.

If you don't manage the lifecycle of your devices, it could create issues, like the following:

  * **Sustained high costs:** Introducing lifecycle management support after your provisioning and configuration processes are in place can increase costs. By planning this support early in the design, you might lower those costs. If your provisioning and configuration processes don't support the whole lifecycle of your devices, for example, you might have to manually intervene on each device to properly handle each phase of their lifecycle. Manual intervention can be expensive, and often doesn't scale.
  * **Increased rigidity:** Not supporting lifecycle management might eventually lead to the inability to update or manage your devices. If you lack a mechanism to safely and efficiently turn off your devices, for example, it might be challenging to manage their end of life and ultimate disposal.



## What's next

  * Read [Connected device architectures on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). .



## Contributors

Author: [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-31 UTC."],[],[]] 
