---
url: https://docs.cloud.google.com/container-optimized-os/docs/resources/sources/
title: Access source code \u00a0|\u00a0 Container-Optimized OS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:41.327833+00:00
---

# Access source code  |  Container-Optimized OS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/resources/sources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Resources ](https://docs.cloud.google.com/container-optimized-os/docs/resources)



Send feedback 

#  Access source code Stay organized with collections  Save and categorize content based on your preferences. 

This page provides details on Container-Optimized OS source code, including how to access Container-Optimized OS image source, source for related container tools, and how to build from source.

## Container-Optimized OS image source

Container-Optimized OS from Google is a fork of the [Chromium OS](https://www.chromium.org/chromium-os) open-source project. You can find the majority of the source code for Container-Optimized OS in the COS repositories <https://cos.googlesource.com>.

Some of the useful resources that can help you determine the source code used to build the image include:

  * Inside the OS image, the `/opt/google/chrome/resources/about_os_credits.html` file contains version and license information for all the packages used to build that image.

  * Kernel source: <https://cos.googlesource.com/third_party/kernel/+/cos-5.15>.  
Kernel config (x86): <https://cos.googlesource.com/third_party/kernel/+/refs/heads/cos-5.15/arch/x86/configs/lakitu_defconfig>.  
Kernel config (Arm): <https://cos.googlesource.com/third_party/kernel/+/refs/heads/cos-5.15/arch/arm64/configs/lakitu_defconfig>.  
The commit SHA1 of the kernel source used to build a particular version is also provided in the [release-notes](https://docs.cloud.google.com/container-optimized-os/docs/resources/release-notes) for that version.

  * Additional image artifacts, including archived **kernel sources** and **kernel headers** , are also available in a public Google Cloud Storage bucket under `gs://cos-tools/<build-number>/`. For example, artifacts for `cos-dev-105-17228-0-0` are under `gs://cos-tools/17228.0.0/`.



    
    
             gcloud storage ls gs://cos-tools/17228.0.0/
             gs://cos-tools/17228.0.0/about_os_credits.html
             gs://cos-tools/17228.0.0/about_os_credits.html.md5
             gs://cos-tools/17228.0.0/cos-package-info.json
             gs://cos-tools/17228.0.0/cos-package-info.json.md5
             gs://cos-tools/17228.0.0/cos_full_payload_dev.bin
             gs://cos-tools/17228.0.0/gpu_R470_version
             gs://cos-tools/17228.0.0/gpu_R470_version.md5
             gs://cos-tools/17228.0.0/gpu_default_version
             gs://cos-tools/17228.0.0/gpu_default_version.md5
             gs://cos-tools/17228.0.0/gpu_latest_version
             gs://cos-tools/17228.0.0/gpu_latest_version.md5
             gs://cos-tools/17228.0.0/kernel-headers.tgz
             gs://cos-tools/17228.0.0/kernel-headers.tgz.md5
             gs://cos-tools/17228.0.0/kernel-src.tar.gz
             gs://cos-tools/17228.0.0/kernel-src.tar.gz.md5
             gs://cos-tools/17228.0.0/kernel_commit
             gs://cos-tools/17228.0.0/kernel_commit.md5
             gs://cos-tools/17228.0.0/kernel_info
             gs://cos-tools/17228.0.0/kernel_info.md5
             gs://cos-tools/17228.0.0/manifest.xml
             gs://cos-tools/17228.0.0/manifest.xml.md5
             gs://cos-tools/17228.0.0/toolchain.tar.xz
             gs://cos-tools/17228.0.0/toolchain.tar.xz.gcs
             gs://cos-tools/17228.0.0/toolchain.tar.xz.md5
             gs://cos-tools/17228.0.0/toolchain_env
             gs://cos-tools/17228.0.0/toolchain_env.md5
             gs://cos-tools/17228.0.0/vmlinux
             gs://cos-tools/17228.0.0/vmlinux.md5
             gs://cos-tools/17228.0.0/lakitu-arm64/
             gs://cos-tools/17228.0.0/lakitu/
    

  * Image artifacts for Arm-based images are available in the public Cloud Storage bucket under `gs://cos-tools/<build-number>/lakitu-arm64/`. For example, artifacts for `cos-arm64-dev-105-17228-0-0` are under `gs://cos-tools/17228.0.0/lakitu-arm64/`.


    
    
            gcloud storage ls gs://cos-tools/17228.0.0/lakitu-arm64/
            gs://cos-tools/17228.0.0/lakitu-arm64/about_os_credits.html
            gs://cos-tools/17228.0.0/lakitu-arm64/about_os_credits.html.md5
            gs://cos-tools/17228.0.0/lakitu-arm64/cos-package-info.json
            gs://cos-tools/17228.0.0/lakitu-arm64/cos-package-info.json.md5
            gs://cos-tools/17228.0.0/lakitu-arm64/gpu_R470_version
            gs://cos-tools/17228.0.0/lakitu-arm64/gpu_R470_version.md5
            gs://cos-tools/17228.0.0/lakitu-arm64/gpu_default_version
            gs://cos-tools/17228.0.0/lakitu-arm64/gpu_default_version.md5
            gs://cos-tools/17228.0.0/lakitu-arm64/gpu_latest_version
            gs://cos-tools/17228.0.0/lakitu-arm64/gpu_latest_version.md5
            gs://cos-tools/17228.0.0/lakitu-arm64/kernel-headers.tgz
            gs://cos-tools/17228.0.0/lakitu-arm64/kernel-headers.tgz.md5
            gs://cos-tools/17228.0.0/lakitu-arm64/kernel-src.tar.gz
            gs://cos-tools/17228.0.0/lakitu-arm64/kernel-src.tar.gz.md5
            gs://cos-tools/17228.0.0/lakitu-arm64/kernel_commit
            gs://cos-tools/17228.0.0/lakitu-arm64/kernel_commit.md5
            gs://cos-tools/17228.0.0/lakitu-arm64/kernel_info
            gs://cos-tools/17228.0.0/lakitu-arm64/kernel_info.md5
            gs://cos-tools/17228.0.0/lakitu-arm64/manifest.xml
            gs://cos-tools/17228.0.0/lakitu-arm64/manifest.xml.md5
            gs://cos-tools/17228.0.0/lakitu-arm64/toolchain.tar.xz
            gs://cos-tools/17228.0.0/lakitu-arm64/toolchain.tar.xz.gcs
            gs://cos-tools/17228.0.0/lakitu-arm64/toolchain.tar.xz.md5
            gs://cos-tools/17228.0.0/lakitu-arm64/toolchain_env
            gs://cos-tools/17228.0.0/lakitu-arm64/toolchain_env.md5
            gs://cos-tools/17228.0.0/lakitu-arm64/vmlinux
            gs://cos-tools/17228.0.0/lakitu-arm64/vmlinux.md5
    

  * Those familiar with Chromium OS build system may also find the build recipes under <https://cos.googlesource.com/cos/overlays/board-overlays/+/master/project-lakitu/> useful.

  * Actual source code archives for individual packages can also be found under one of the package mirrors maintained by Chromium OS build system. You can access them by appending the correct tarball name to one of the following URLs:

    * `https://storage.googleapis.com/chromeos-mirror/gentoo/distfiles/`
    * `https://storage.googleapis.com/chromeos-localmirror/distfiles/`

For example, to download kubernetes version 1.19.2, use `https://storage.googleapis.com/chromeos-localmirror/distfiles/kubernetes-server-linux-amd64-1.19.2.tar.gz`.




The [Chromium OS Build FAQ](http://www.chromium.org/chromium-os/how-tos-and-troubleshooting/portage-build-faq) and other [Chromium OS Build](http://www.chromium.org/chromium-os/build) documentation explains how the build system and package mirrors work.

## Container source

Container-Optimized OS from Google ships with some tools that download containers at runtime. Those containers are also open sourced. The following table lists the containers, their source location and release location.

Containers | Release Location  
---|---  
[Toolbox](https://cos.googlesource.com/cos/tools/+/refs/heads/master/src/cmd/toolbox/) | Container Registry `gcr.io/cos-cloud/toolbox`  
[Cos-gpu-installer](https://cos.googlesource.com/cos/tools/+/refs/heads/master/src/cmd/cos_gpu_installer/) | Container Registry `gcr.io/cos-cloud/cos-gpu-installer`  
[Cloud logging agent](https://github.com/GoogleCloudPlatform/google-fluentd) | Container Registry `gcr.io/stackdriver-agents/stackdriver-logging-agent`  
[Konlet agent](https://github.com/GoogleCloudPlatform/konlet) | Container Registry `gcr.io/gce-containers/konlet`  
  
## Building from source

Follow the instructions on [Building from Open Source](https://docs.cloud.google.com/container-optimized-os/docs/how-to/building-from-open-source) to build a Container-Optimized OS disk image from the source.

## Source code contributions

Container-Optimized OS does not accept direct contributions from the public.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
