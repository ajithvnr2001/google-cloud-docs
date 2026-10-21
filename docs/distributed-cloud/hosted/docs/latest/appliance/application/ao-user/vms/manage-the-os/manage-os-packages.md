---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-the-os/manage-os-packages/
title: Manage OS packages \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:08.745537+00:00
---

# Manage OS packages  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-the-os/manage-os-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Manage OS packages Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped appliance provides APT packages for Ubuntu virtual machines (VM) and RPM packages for Rocky Linux VMs. GDC air-gapped appliance provides the packages from the following repositories:

Operating system name | Operating system version | Repository name  
---|---|---  
Ubuntu | 20.04 | `focal main`  
Rocky Linux | 8.8 | `baseos` and `appstream`  
  
The repository `focal main` includes the latest packages from the `focal-security` main and the `focal-updates` main pockets.

These instructions show you how to set up your VM to connect to a GDC air-gapped appliance package repository, and install and update packages from the repository.

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview). All commands for GDC air-gapped appliance use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. Locate the Management API server name, or ask your Platform Administrator (PA) what the server name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  3. Use the path to replace `MANAGEMENT_API_SERVER{"</var>"}}` in these instructions.




## Consume packages from a GDC air-gapped appliance package repository

To consume packages from a package repository, work through the following steps:

###  Ubuntu 

  1. Connect to the VM that needs to consume packages.
  2. Check whether the APT sources point to the GDC air-gapped appliance APT package repository:
         
         if grep -qs "http://pkg.org.internal/ubuntu" /etc/apt/sources.list; then echo "yes"; \
         else echo "no"; fi
         

  3. If the previous command returns `no`, run the following commands to point the APT sources of the VM to the GDC air-gapped appliance APT package repository.

**Note:** The first command removes the existing APT sources file, `/etc/apt/sources.list`. Ensure you backup the file, if needed.
         
         sudo rm -f /etc/apt/sources.list
         
         sudo tee /etc/apt/sources.list << EOF
         # GDC repo for Ubuntu focal main packages.
         # The repo includes packages from focal-updates and focal-security.
         
         deb [trusted=yes] http://pkg.org.internal/ubuntu focal main
         EOF
         
         sudo tee /etc/cloud/cloud.cfg.d/01_gdch_apt_sources.cfg << EOF
         #cloud-config
         # Preserve the sources.list so that it points to the GDC package repo.
         apt:
         preserve_sources_list: true
         EOF
         

  4. Consume packages from the repository:
         
         sudo apt update
         sudo apt install APT_PACKAGE
         

Replace APT_PACKAGE with the name of the package the VM needs to consume.




###  Rocky Linux 

  1. Connect to the VM that needs to consume packages.
  2. Check whether the YUM sources already point to the GDC air-gapped appliance YUM package repository:
         
         if grep -qs "http://pkg.org.internal/rocky" /etc/yum.repos.d/*; then echo "yes"; \
         else echo "no"; fi no
         

  3. If the previous command returns `no`, run the following commands to point the `yum` sources of the VM to the GDC air-gapped appliance YUM package repository:

**Note:** The first command removes the existing `yum` sources files, `/etc/yum.repos.d/*`. Ensure you backup the files, if needed.
         
         sudo rm -rf /etc/yum.repos.d/*
         
         sudo tee /etc/yum.repos.d/Rocky-BaseOS-GDCH.repo << EOF
         # GDC repository for Rocky BaseOS packages.
         
         [baseos-gdch]
         name=Rocky Linux 8 - BaseOS - GDCH
         baseurl=http://pkg.org.internal/rocky/baseos
         gpgcheck=0
         enabled=1
         EOF
         
         sudo tee /etc/yum.repos.d/Rocky-AppStream-GDCH.repo << EOF
         # GDC repository for Rocky AppStream packages.
         
         [appstream-gdch]
         name=Rocky Linux 8 - AppStream - GDCH
         baseurl=http://pkg.org.internal/rocky/appstream
         gpgcheck=0
         enabled=1
         EOF
         

  4. Consume packages from the repository:
         
         sudo dnf update
         sudo dnf install RPM_PACKAGE
         

Replace RPM_PACKAGE with the name of the package the VM needs to consume.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
