---
url: https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits/
title: Container-Optimized OS Overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:30.016585+00:00
---

# Container-Optimized OS Overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Guides ](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance)



Send feedback 

#  Container-Optimized OS Overview Stay organized with collections  Save and categorize content based on your preferences. 

Container-Optimized OS from Google is an operating system image for your [Compute Engine](https://docs.cloud.google.com/compute) VMs that is optimized for running containers. Container-Optimized OS is maintained by Google and based on the open source Chromium OS project. With Container-Optimized OS, you can bring up your containers on Google Cloud Platform quickly, efficiently, and securely.

## Features and Benefits

Container-Optimized OS provides the following benefits:

  * **Run Containers Out of the Box** : Container-Optimized OS instances come pre-installed with the Docker and containerd runtimes and `cloud-init`. With a Container-Optimized OS instance, you can bring up your container at the same time you create your VM, with no on-host setup required.
  * **Smaller attack surface** : Container-Optimized OS has a smaller footprint, reducing your instance's potential attack surface.
  * **Locked-down by default** : Container-Optimized OS instances include a locked-down firewall and other security settings by default.
  * **Automatic Updates** : Container-Optimized OS instances are configured to automatically download weekly updates in the background; only a reboot is necessary to use the latest updates.



## Limitations

Container-Optimized OS has limited or no support for some of the common features you may be familiar with on other operating systems:

  * Container-Optimized OS does not include a package manager; as such, you'll be unable to install software packages directly on an instance. However, you can use [CoreOS toolbox](https://docs.cloud.google.com/container-optimized-os/docs/how-to/toolbox) to install and run debugging and admin tools in an isolated container.
  * Container-Optimized OS does not support execution of non-containerized applications.
  * The Container-Optimized OS kernel is locked down; you'll be unable to install third-party kernel modules or drivers.
  * Container-Optimized OS is not supported outside of the Google Cloud Platform environment.



## Using Container-Optimized OS

Container-Optimized OS is the default node OS Image in [Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine) and other [Kubernetes](https://kubernetes.io/) deployments on Google Cloud Platform. See the [Kubernetes Engine Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster) for more information on using Container-Optimized OS with Kubernetes Engine.

You can also use Container-Optimized OS to quickly bring up a container on a Compute Engine instance with minimal setup. For more information, see [Creating and Configuring Instances](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance).

You can run tools like `ping`, the Google Cloud CLI, `pstree`, `htop`, `emacs` and more using the [CoreOS toolbox](https://docs.cloud.google.com/container-optimized-os/docs/how-to/toolbox) utility, which is pre-installed in Container-Optimized OS at `/usr/bin/toolbox`. See [Debugging with toolbox](https://docs.cloud.google.com/container-optimized-os/docs/how-to/toolbox) for more information.

## Use cases for Container-Optimized OS

Container-Optimized OS can be used to run most containers. You should consider using Container-Optimized OS as the operating system for your Compute Engine instance if you have the following needs:

  * You need support for containers or Kubernetes with minimal setup.
  * You need an operating system that has a small footprint and is [security hardened](https://docs.cloud.google.com/container-optimized-os/docs/concepts/security) for containers.
  * You need an operating system that is tested and verified for running Kubernetes on your Compute Engine instances.



Container-Optimized OS may not be the right choice for you in the following cases:

  * Your application is not containerized or your containerized application depends on kernel modules, drivers and other additional packages that are not available in Container-Optimized OS.
  * You need professional customer support from a Linux provider (Canonical, Core OS, Redhat, SUSE, etc).
  * You want your image and OS application to be fully supported outside Google Cloud.



See [Containers on Google Cloud](https://docs.cloud.google.com/compute/docs/containers) to learn about other operating systems you can use to run containerized applications on Google Cloud. Compute Engine [provides images](https://docs.cloud.google.com/compute/docs/images) for other popular operating systems, including images that are [optimized for containers](https://docs.cloud.google.com/compute/docs/containers#container_images).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
