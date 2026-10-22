---
url: https://docs.cloud.google.com/deep-learning-vm/docs/release-notes/
title: Deep Learning VM release notes \u00a0|\u00a0 Deep Learning VM Images \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:27.502245+00:00
---

# Deep Learning VM release notes  |  Deep Learning VM Images  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deep-learning-vm/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Deep Learning VM Images ](https://docs.cloud.google.com/deep-learning-vm/docs)
  * [ Resources ](https://docs.cloud.google.com/deep-learning-vm/docs/release-notes)



Send feedback 

#  Deep Learning VM release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Deep Learning VM Images. We recommend that Deep Learning VM developers periodically check this list for any new announcements. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/deeplearningvm-release-notes.xml) directly. 

## April 13, 2026

Breaking

Images with Nvidia 570 drivers have been deprecated as Nvidia officially stopped supporting these versions. You can use images with Nvidia 580 drivers instead.

## April 08, 2026

Feature

**M132 release**

  * Ubuntu 22.04 and Ubuntu 24.04 images with Nvidia 580 drivers and CUDA 12.9 stack are now available for Common and PyTorch 2.9 images.



## December 08, 2025

Feature

**M131 release**

  * Ubuntu 24.04 images with CUDA 12.8 and PyTorch 2.7 stack are now available for Common and PyTorch images.



## July 31, 2025

Feature

**M130 release**

  * Ubuntu 22.04 images with CUDA 12.8 and PyTorch 2.7 stack are now available for Common and PyTorch images.



## July 14, 2025

Breaking

The following framework versions have reached their end of patch and support dates:

  * Base versions with CUDA 12.4 and earlier
  * Tensorflow versions 2.17 and earlier
  * PyTorch versions 2.3 and earlier



To view the end of patch and support dates, see [Supported framework versions](https://docs.cloud.google.com/deep-learning-vm/docs/images#supported-frameworks).

For more information on what the end of patch and support date means, see [Support policy schedule](https://docs.cloud.google.com/deep-learning-vm/docs/framework-support-policy#support_policy_schedule).

If you must use an image after deprecation against Google security recommendations and at your own risk, see [After deprecation](https://docs.cloud.google.com/deep-learning-vm/docs/images#after-deprecation).

## April 16, 2025

Feature

**M129 release**

  * Updated the Dataproc JupyterLab plugin to version 0.1.85.



## March 12, 2025

Feature

**M128 release**

  * Except for TensorFlow images, new images don't include conda. This change was made to improve size, performance, and vulnerability management. The existing image names and image family names now point to images and image families that don't include conda (for example: the image name `common-cpu-v20250310-debian-11-py310` and corresponding image family name `common-cpu-debian-11-py310`).
  * Images that include conda will be available until at least September 30, 2025. These images now have `-conda` appended to the name (for example: the image name `common-cpu-v20250310-debian-11-py310-conda` and corresponding image family name `common-cpu-debian-11-py310-conda`).
  * All TensorFlow images and image families still include conda, but M128 image names and image family names have `-conda` appended. Specifying images or image families without `-conda` appended references older images, which also include conda.



## January 16, 2025

Feature

**M127 release**

  * Fixed an issue related to ownership of the home directory when using authorized ssh keys.



Breaking

The following framework versions have reached their end of patch and support dates:

  * Tensorflow versions 2.15 and earlier
  * PyTorch versions 2.1 and earlier
  * Base versions with CUDA 12.2 and earlier



To view the end of patch and support dates, see [Supported framework versions](https://docs.cloud.google.com/deep-learning-vm/docs/images#supported-frameworks). To create a VM instance using an image family that has reached its end of patch and support date, you must specify an image from the image family when you create the VM instance. To list images from an image family name after its end of patch and support date, include the `--show-deprecated flag` in your `gcloud compute images list` command, or select **Show deprecated images** when creating an instance in the Google Cloud console.

## November 20, 2024

Feature

**M126 release**

  * CUDA 12.4 VM images are now available.
  * PyTorch 2.4.0 with CUDA 12.4 and Python 3.10 VM images are now available.
  * Upgraded R from 4.4.1 to 4.4.2 for R VM images.



Breaking

One or more framework versions have reached their end of patch and support dates. To view end of patch and support dates, see [Supported framework versions](https://docs.cloud.google.com/deep-learning-vm/docs/images#supported-frameworks). To create a VM instance using an image family that has reached its end of patch and support date, you must specify an image from the image family when you create the VM instance. To list images from an image family name after its end of patch and support date, include the `--show-deprecated` flag in your `gcloud compute images list` command, or select **Show deprecated images** when creating an instance in the Google Cloud console.

## September 26, 2024

Feature

**M125 release**

  * TensorFlow 2.17 VM images are now available.



## August 20, 2024

Feature

**M124 release**

  * Pytorch 2.3.0 with CUDA 12.1 and Python 3.10 VM images are now available.



## July 16, 2024

Feature

**M123 release**

  * TensorFlow 2.16 images are now available.



## June 21, 2024

Feature

**M122 release**

  * Updated Nvidia drivers to version 550.90.07 to fix vulnerabilities.



## May 17, 2024

Feature

**M121 release**

  * CUDA 12.2 images are now available.
  * Updated TensorFlow 2.15 images from CUDA 12.1 to CUDA 12.2.
  * Re-enabled `common-gpu` Deep Learning VM releases that were erroneously deactivated in M117.
  * Updated Nvidia drivers to 550.54.15 to fix an issue where Nvidia drivers failed to install on startup after Debian 11 images upgraded kernel to `linux-image-5.10.0-29-cloud-amd64`.
  * The `linux-headers-cloud-amd64` metapackage is now installed for faster driver recompiling on kernel upgrades.
  * TensorFlow 2.6 CPU and GPU images are deprecated. There will be no further updates to these images in future releases.



## April 25, 2024

Feature

**M120 release**

  * Upgraded TensorFlow 2.15 images to TensorFlow 2.15.1.
  * Added Ubuntu 22.04 support for CPU images, and for GPU images using CUDA 12.1 or higher.



## March 29, 2024

Fixed

**M119 release**

  * Fixed an issue wherein Dataproc extensions caused JupyterLab to crash when remote kernels weren't available.



## March 18, 2024

Feature

**M118 release**

  * Restored legacy gpu image families for TensorFlow 2.12 through 2.14, and for PyTorch 2.0.
  * PyTorch 2.1.0 with CUDA 12.1 and Python 3.10 VM images are now available.
  * PyTorch 2.2.0 with CUDA 12.1 and Python 3.10 VM images are now available.
  * R images (Experimental) updated to R 4.3.3.
  * Updated Nvidia drivers of older Deep Learning VM images to R535.



## February 28, 2024

Feature

**M117 release**

  * Added the CUDA version (CUDA 11.8) to the TensorFlow 2.12, 2.13, and 2.14 image names and image family names. For example, `tf-2-12-gpu` is renamed `tf-2-12-cu118`.



## February 08, 2024

Feature

**M116 release**

  * Added the CUDA version to the TensorFlow 2.15 image family name, for this release and future releases. For example, `tf-2-15-gpu` is renamed to `tf-2-15-cu121`.
  * Deprecated the `tf-2-15-gpu` image family in favor of `tf-2-15-cu121`.



## January 19, 2024

Feature

**M115 release**

  * TensorFlow 2.15 with CUDA 12.1 and Python 3.10 images are now available.
  * TensorFlow 2.14 with CUDA 11.8 and Python 3.10 images are now available.



## December 14, 2023

Feature

**M114 release**

  * Starting with this release, Debian 10 Python 3.7 images are no longer available.
  * Upgraded R to 4.3 on Debian 11 Python 3.10 images.



## November 16, 2023

Feature

**M113 release**

  * Miscellaneous bug fixes and improvements in Python 3.10 images.



## October 10, 2023

Feature

**M112 release**

  * CUDA 12.1 VM images are available with the following image names:
    * `common-cu121-debian-11-py310`
    * `common-cu121-ubuntu-2004-py310`
  * Miscellaneous bug fixes and improvements.



## September 14, 2023

Feature

**M111 release**

  * PyTorch 2.0 images now include PyTorch XLA 2.0.
  * Miscellaneous software updates.



## August 10, 2023

Feature

**M110 release**

  * Added support for TensorFlow 2.13 with Python 3.10 on Debian 11.
  * Added support for TensorFlow 2.8 with Python 3.10 on Debian 11.
  * Miscellaneous software updates.



Deprecated

TensorFlow 2.9 images are deprecated.

## June 26, 2023

Feature

**M109 release**

  * PyTorch 2.0 on Debian 11 with Python 3.10 and CUDA 11.8 images are now available.
  * GPU-based Deep Learning VM Images now installs Nvidia drivers with the new [open kernel modules](https://github.com/NVIDIA/open-gpu-kernel-modules) if started on an A2 or G2 machine instead of the proprietary kernel modules.
  * Miscellaneous software updates.



## May 09, 2023

Feature

**M108 update**

This update of the M108 release includes the following:

  * The following Deep Learning VM images are now available: 
    * Tensorflow 2.12 CPU with CUDA 11.8 and Python 3.10 (`tf-2-12-cpu-debian-11-py310`)
    * Tensorflow 2.12 GPU with CUDA 11.8 and Python 3.10 (`tf-2-12-gpu-debian-11-py310`)



## May 04, 2023

Feature

**M108 release**

  * The image name `common-container-experimental` was changed to `common-container`. The related image family name wasn't changed. 
  * Miscellaneous software updates.



## April 13, 2023

Feature

**M107 release**

  * Miscellaneous software updates.



## April 06, 2023

Feature

**M106 release**

  * Rolled back a previous change in which Jupyter dependencies were located in a separate Conda environment.
  * Miscellaneous software updates.



## March 31, 2023

Feature

**M105 release**

  * The following Deep Learning VM images are now available with Python 3.10 on Debian 11:

    * TensorFlow 2.11 CPU (`tf-2-11-cpu-debian-11-py310`)
    * TensorFlow 2.11 GPU with Cuda 11.3 (`tf-2-11-cu113-debian-11-py310`)
    * PyTorch 1.13 with Cuda 11.3 (`pytorch-1-13-cu113-debian-11-py310`)
    * Base CPU (`common-cpu-debian-11-py310`)
    * Base GPU with Cuda 11.3 (`common-cu113-debian-11-py310`)
  * The following Deep Learning VM images are now available with Python 3.9 on Debian 11:

    * TensorFlow 2.6 CPU (`tf-2-6-cpu-debian-11-py39`)
    * TensorFlow 2.6 GPU with Cuda 11.3 (`tf-2-6-cu113-debian-11-py39`)
  * Jupyter-related libraries have been moved to a different Conda environment, separate from the one containing machine learning frameworks and base software libraries.

  * Miscellaneous bug fixes and improvements.




## March 16, 2023

Feature

**M104 release**

  * Added the following packages: 
    * google-cloud-artifact-registry
    * google-cloud-bigquery-storage
    * google-cloud-language
    * keyring
    * keyrings.google-artifactregistry-auth
  * Fixed a bug in which curl could not find the right SSL certificate path by default.



Breaking

TensorFlow Enterprise 2.1 has reached the end of its support period. See [Version details](https://docs.cloud.google.com/tensorflow-enterprise/docs/overview#version_details).

## January 30, 2023

Feature

**M103 release**

  * Upgraded PyTorch to 1.13.1.
  * Minor bug fixes and improvements.



## December 15, 2022

Feature

**M102 release**

  * TensorFlow 2.11 is now available.
  * PyTorch 1.13 is now available.
  * Added support for [Jupyter[Lab] Language Server Protocol](https://jupyterlab-lsp.readthedocs.io/en/latest/).
  * Regular security patches and package upgrades.



## December 09, 2022

Feature

**M101 release**

  * TensorFlow patch version upgrades: 
    * From 2.8.3 to 2.8.4.
    * From 2.9.2 to 2.9.3.
    * From 2.10.0 to 2.10.1.
  * TensorFlow 1.15 Deep Learning VM images are now deprecated.
  * Regular security patches and package upgrades.



## November 08, 2022

Feature

**M100 release**

  * Migrated the Docker proxy agent to use a systemctl service.
  * Regular package updates.



## November 02, 2022

Feature

**M99 release**

  * Fixed a bug where Jupyter widgets through `ipywidgets` were causing errors and not displaying.
  * Updated TPU versions for TensorFlow 2.8, 2.9, and 2.10 Deep Learning VMs.
  * Improved error messages for debugging custom container Deep Learning VMs that were instantiated with a GPU but without installing NVIDIA drivers.
  * Regular package updates.



## October 18, 2022

Feature

**M98 release**

  * Upgraded JupyterLab from 3.2 to 3.4.
  * Upgraded R from 4.1 to 4.2.
  * Removed the requirement to have the `compute.instances.get` permission in the Service Account attached to the VM introduced in m97.
  * Added support for the `notebook-enable-debug` metadata flag for JupyterLab low level debugging, which sets: `c.Application.log_level = 0`. The default value is 30.
  * Added support for the `disable-check-xsrf` metadata flag, which sets: `c.ServerApp.disable_check_xsrf = True`. The default value is false.
  * Fixed a bug in which Cloud Marketplace was deploying an older version of Deep Learning VM images.
  * Miscellaneous bug and display fixes.
  * Regular package updates.



## September 29, 2022

Feature

**M97 release**

  * Improved the startup time for Ubuntu GPU images.
  * Regular package updates.



Breaking

Proxy registration fails if the Service Account attached to the VM does not have the `compute.instances.get` permission

## September 20, 2022

Feature

**M96 release**

  * TensorFlow 2.10.0 is now available.
  * TensorFlow patch updates for 2.9.2 and 2.8.3 are now available.
  * The PyTorch patch update for 1.12.1 is now available.
  * The Diagnostic tool supports DNS resolution check.
  * Docker is updated to 20.10.
  * Miscellaneous bug fixes.



## August 12, 2022

Feature

**M95 release**

  * Tensorflow has been updated to 2.9.1, 2.8.1, and 2.6.5 to include upstream changes.
  * Updated to the latest NVIDIA driver version: 510.47.03. 
  * The latest NVIDIA driver version does not support K80 GPUs. To use K80 GPUs, you must use an M94 or earlier environment.
  * Fixed bug in which the user is prompted with the warning `JupyterLab build is suggested` on startup for TensorFlow Deep Learning VMs.
  * Regular package refreshment and bug fixes.



Issue

`n1-standard-1` Compute instances that use the `tensorflow-gpu` family fail to boot if they were created with a single disk and no accelerator.

Please use the `tf-latest-cpu` image family for instances without accelerators, or increase the machine type to at least `n1-standard-2`.

## July 06, 2022

Feature

**M94 release**

  * Added support for PyTorch 1.12.
  * Added more system libraries to the R Deep Learning VM image.



## May 27, 2022

Feature

**M93 release**

Fixed

  * Fixed a bug that prevented kernels from shutting down properly in Vertex AI Workbench managed notebooks.



## May 16, 2022

Feature

**M92 release**

  * TensorFlow Enterprise 2.9 is now available. Note that this TensorFlow Enterprise version does not include [Long Term Version Support](https://docs.cloud.google.com/tensorflow-enterprise/docs/overview#long_term_version_support).
  * Starting with PyTorch 1.11, PyTorch environments now support XLA by default.
  * TensorFlow Enterprise patch releases: 2.6.4 and 2.8.1.



Fixed

  * Fixed an issue in the Cloud Storage backup and restore feature. This fix helps prevent the deletion of local files after a reboot when the VM loses connectivity to the configured Cloud Storage backup bucket.



## March 21, 2022

Feature

**M91 release**

  * PyTorch 1.11 and PyTorch XLA 1.11 are now available in both Deep Learning VM Images and Deep Learning Containers.
  * Updated NVIDIA drivers to 470.57.02.
  * Upgraded Compute Engine Virtual Ethernet (GVE) to 1.3.0.



## February 28, 2022

Issue

In M90 release instances, gRPC 1.44.0 can generate spurious error logs, though this doesn't affect the VM's ability to boot up. A fix is planned for the next release.

Feature

**M90 release**

  * Vertex AI sample notebooks are now included in the `/usr/share/tutorials` folder.
  * Instances now allow the Jupyter options for disabling terminals and deleting files instead of sending them to the trash or recycling bin.



## February 02, 2022

Feature

**M89 release**

  * TensorFlow Enterprise 2.8 is now available and includes [Long Term Version Support](https://docs.cloud.google.com/tensorflow-enterprise/docs/overview#long_term_version_support). TensorFlow Enterprise 2.8 is available in both Deep Learning VM Images and [Deep Learning Containers](https://docs.cloud.google.com/deep-learning-containers). 
  * Upgraded TensorFlow Enterprise 2.6.2 to 2.6.3.



## December 20, 2021

Fixed

**M88 release**

  * To help address the Apache Log4j 2 vulnerability, H2O has been updated to 3.34.0.6 in the R and Theia images. This addresses [CVE-2021-44228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228) and [CVE-2021-45046](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45046). See the [official H2O update](https://www.h2o.ai/security/bulletins/h2o-2021-001/).



Change

  * As previously announced in the [M87 release](https://docs.cloud.google.com/deep-learning-vm/docs/release-notes#December_06_2021) and [M71 release](https://docs.cloud.google.com/deep-learning-vm/docs/release-notes#June_02_2021), the previous format of TensorFlow 2.x image names, `tf2-xxx-2-y-zzz`, is unavailable starting with this release. Please use the current format of `tf-xxx-2-y-zzz` for image names.



Issue

  * Images from the M88 release mistakenly have M87 metadata stored in the images. For example, the welcome message upon terminal login for the base CPU image shows "Version: common-cpu.m87". This mistaken metadata is also shown in the `version` field in notebook `Custom metadata`. Users can verify they are actually using the M88 images by looking for `v20211219` in the image name of the boot disk. After clicking the image, users can also verify if the image has the label `release : m88`. Other than the mistaken metadata, users can use the M88 images as normal.



Feature

  * Starting with this release, the Python packages that are installed on each image are listed in files that are available on Cloud Storage.



## December 06, 2021

Feature

**M87 release**

  * Added Artifact Registry's [Python keyring authentication library](https://docs.cloud.google.com/artifact-registry/docs/python/authentication#keyring) to deep learning vm environments.



Change

  * The M87 release is the last release in which TensorFlow 2.x image names are available in two formats: the current standard, `tf-xxx-2-y-zzz` and the previous standard, `tf2-xxx-2-y-zzz`. For example, both `tf-ent-2-7-cpu` and `tf2-ent-2-7-cpu` are available although they are the same images. The next release will only contain TensorFlow 2 images named with the current standard, as originally announced in the [M71 release notes from June 2021](https://docs.cloud.google.com/deep-learning-vm/docs/release-notes#June_02_2021).



## November 18, 2021

Feature

**M86 release**

  * Upgraded all Ubuntu 18.04 LTS Deep Learning VM images to Ubuntu 20.04 LTS (see [What is an Ubuntu LTS release?](https://ubuntu.com/blog/what-is-an-ubuntu-lts-release)).
  * Released PyTorch/XLA 1.10.
  * Upgraded TensorFlow Enterprise image to the latest patch version: 2.6.2
  * Deprecated CUDA 10.x environments.
  * Locked JupyterLab version to 3.2.



## November 08, 2021

Feature

**M85 release**

  * CUDA 11.3 Debian-10 image is available.
  * Regular package refreshment and bug fixes.



## November 05, 2021

Feature

**M84 release**

  * TensorFlow Enterprise 2.7 is now available with CUDA 11.3 support. Note that this TensorFlow Enterprise version does not include [Long Term Version Support](https://docs.cloud.google.com/tensorflow-enterprise/docs/overview#long_term_version_support).



## October 28, 2021

Feature

**M83 release**

  * PyTorch 1.10 is now available.



## October 26, 2021

Change

  * Theia IDE (experimental) images were refreshed. PyTorch has been removed from Theia IDE images.



Feature

**M82 release**

  * The [Vertex SDK for Python](https://googleapis.dev/python/aiplatform/latest/index.html) is available across all deep learning environment products; it was previously available only in TensorFlow images.



## October 12, 2021

Feature

**M81 release**

  * Upgraded R to 4.1.
  * Improved Cloud Storage sync logic so that only newer files sync.



Fixed

  * Fixed bug that prevented R kernels from working properly.



## September 24, 2021

Breaking

Starting with the M80 image release, all environments will include JupyterLab 3.x by default. To continue using an existing environment's JupyterLab 1.x version, disable [auto-upgrade](https://docs.cloud.google.com/notebooks/docs/upgrade#create_a_new_instance_with_auto_upgrade_enabled) (if enabled) and do not manually upgrade the environment to a new environment version. To create new instances using older images that have JupyterLab 1.x installed, see [creating specific versions of instances](https://docs.cloud.google.com/notebooks/docs/create-specific-version).

Feature

**M80 release**

  * Updated JupyterLab from 1.x to 3.x.
  * Added [Jupytext](https://jupytext.readthedocs.io/en/latest/index.html).



Fixed

  * Deep Learning VM Images in Cloud Marketplace have been updated. They were not updated in the last release.



## September 09, 2021

Feature

**M79 release**

  * Updated Pytorch 1.9 images (they were not refreshed in the last release).
  * Updated Theia IDE (experimental) images.
  * Node.js is pinned to `>=12.14.1,<13`.



Breaking

  * M79 is the last release version that has JupyterLab 1.x installed. For the next release (M80), JupyterLab will be upgraded to 3.x for all Deep Learning VM Images, Deep Learning Containers, and Notebooks.



Issue

  * Deep Learning VM Images in Cloud Marketplace have not been updated. They are planned to be refreshed during the next release.



Fixed

  * Fixed a bug in which the home folder in custom container VMs was owned by the root instead of Jupyter.



## August 18, 2021

Feature

**M78 release**

  * Updated TensorFlow Enterprise patch version 2.3.3 to 2.3.4.



Fixed

  * Fixed a bug that prevented users from exporting a notebook as a PDF.
  * Fixed a bug that caused some users to be unable to SSH into their host machines.



Deprecated

**TensorFlow Enterprise 2.5**

  * TensorFlow Enterprise 2.5 Deep Learning VM images are now deprecated.



## August 11, 2021

Feature

**M77 release**

[TensorFlow Enterprise](https://docs.cloud.google.com/tensorflow-enterprise/docs/overview) 2.6.0 is now available and includes [Long Term Version Support](https://docs.cloud.google.com/tensorflow-enterprise/docs/overview#long_term_version_support).

## August 02, 2021

Feature

**M76 release**

  * Added the [Vertex SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries).
  * Regular package refreshment and bug fixes.



## July 15, 2021

Feature

**M75 release**

  * Improved the clarity of error messages for custom container users.



## July 07, 2021

Fixed

**M74 release**

  * Re-released all CUDA 11 images to fix an issue in which [VM instances are unable to detect GPU accelerators after a reboot](https://issuetracker.google.com/issues/191551132). If you have not experienced this issue, no action is needed. If your GPU is disconnected from your instance after a reboot, [see these resolution options](https://groups.google.com/g/google-dl-platform/c/iUQXJN3I8RM).



Feature

  * In Debian 10 GPU images, updated NVIDIA drivers to 460.73.01 and CUDA to 11.0.3.
  * Added support for controlling the Cloud Storage backup synchronization time and reducing the output of synchronization.
  * Preinstalled the table of contents extension in JupyterLab.
  * Added fastai 2.4 to the PyTorch 1.9 GPU image.



## June 22, 2021

Feature

**M73 release**

  * Upgraded TensorFlow Enterprise 2.1.3 to 2.1.4.
  * Upgraded TensorFlow Enterprise 2.3.2 to 2.3.3.
  * Disabled automatic updates for Ubuntu to be in line with the behavior in Debian images.
  * Miscellaneous bug fixes and updates.



## June 17, 2021

Feature

**M72 release**

  * Added PyTorch 1.9 and PyTorch/XLA 1.9 images.



## June 02, 2021

Change

  * TensorFlow 2.x image names are now available in two formats: `tf-xxx-2-y-zzz` (the new standard format) `tf2-xxx-2-y-zzz` (the previous standard format). Image names in the previous standard format will be deprecated in a future release.



Feature

**M71 release**

  * Refreshed the Debian-10 images (Ubuntu images not refreshed in this release).
  * Upgraded [TensorFlow Probability](https://www.tensorflow.org/probability), [TensorFlow I/O](https://www.tensorflow.org/io), and TensorFlow Estimator in TensorFlow 2.5 images.
  * Added support for a Post Startup script and provided status in guest attributes.



## May 14, 2021

Feature

**M70 release**

  * Added TensorFlow Enterprise 2.5 images. Note this is an Enterprise version but not a Long Term Support (LTS) version.



## May 13, 2021

Feature

**M69 release**

  * Migrated Collection Agent to Cloud Monitoring version 2.



## May 05, 2021

Feature

**M68 release**

  * Upgraded R Images from 3.6 to 4.0.
  * Added xai-tabular-widget onto all TensorFlow images.
  * Miscellaneous bug fixes and updates.



## April 19, 2021

Feature

**M67 release**

  * GPU support added for Beam Notebooks.
  * Added Horovod to TensorFlow GPU Deep Learning VMs.
  * Regular package refreshment and bug fixes.



## March 31, 2021

Feature

**M66 release**

  * PyTorch 1.8 support in deep learning environments ([Deep Learning VM Image](https://docs.cloud.google.com/ai-platform/deep-learning-vm/docs) and [Deep Learning Containers](https://docs.cloud.google.com/ai-platform/deep-learning-containers/docs)) is available.
  * Fixed scope allocator optimization issue with the TensorFlow Enterprise 2.3/2.1 MKL build.
  * Regular package refreshment and bug fixes.



## March 05, 2021

Feature

**M65 release**

  * Added support for DooD (Docker outside of Docker) in Dataflow notebooks container images.

  * Upgraded tensorflow-cloud to 0.1.13.

  * Regular package refreshment and bug fixes.




## February 19, 2021

Feature

**M64 release**

  * Upgraded TensorFlow 2.4 to 2.4.1.

  * Upgraded TFX and [Fairness Indicators](https://www.tensorflow.org/responsible_ai/fairness_indicators/guide) from 0.26.0 to 0.27.0.

  * Added the Fast.ai book tutorials to Pytorch images.

  * Enabled [gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) for all DLVM images.

  * Miscellaneous bug fixes and updates.




Deprecated

**Swift For TensorFlow**

  * The Swift For TensorFlow project is entering archive mode. Swift images will be deprecated and will no longer receive updates after this release.



## February 08, 2021

Feature

**M63 release**

  * Nvidia driver is upgraded to 450.80.02.
  * TFX version is upgraded to 0.26.1.
  * Regular package refreshment and bug fixes.



## January 25, 2021

Deprecated

**Python 2**

Python 2 is no longer supported in Deep Learning VM Image. Read more about [Python 2 support on Google Cloud](https://docs.cloud.google.com/python/docs/python2-sunset#:%7E:text=The%20Python%20community%20announced%20that,as%20soon%20as%20they%20can.&text=Managed%20compute%20services%2C%20such%20as,runtime%20beyond%20January%201%2C%202020.).

Feature

**M62 release**

  * Upgraded TensorFlow 2.3 to 2.3.2
  * Upgraded TensorFlow 2.1 to 2.1.3
  * Miscellaneous bug fixes and updates



## December 16, 2020

Feature

**M60 release**

  * Added TensorFlow 2.4 Deep Learning VM Images



## November 12, 2020

Fixed

**M59 release**

  * Miscellaneous bug fixes.



Change

  * `tensorflow_enterprise_addon` package is renamed to `tensorflow-cloud`



## October 27, 2020

Feature

**M58 release**

  * Added PyTorch 1.6 CUDA 11 images that support [A100 GPU](https://cloud.google.com/blog/products/compute/announcing-google-cloud-a2-vm-family-based-on-nvidia-a100-gpu) accelerators. This special PyTorch build provides another option to add to our A100-compatible TensorFlow Enterprise builds.
  * Added the [PyTorch/XLA](https://github.com/pytorch/xla) package.
  * Added the [Swift for TensorFlow](https://www.tensorflow.org/swift) framework.
  * Added the Ubuntu 18.04 OS.



Change

  * TensorFlow Enterprise updated to [2.3.1](https://github.com/tensorflow/tensorflow/releases/tag/v2.3.1) from 2.3.0.
  * Debian 10 is now the default OS for Deep Learning VM images.



## September 24, 2020

Feature

**M56 release**

  * Bug fixes for TensorFlow 2.3 add-ons
  * Fixes bug affecting BigQuery magic commands in some environments
  * Adds a diagnostics tool for AI Platform Notebooks



## August 26, 2020

Change

**M55 release**

  * Restricts Jupyter memory usage to fix 5* issues
  * Updates TensorFlow 2.3 dependencies
  * Uses CUDA 11.0 in TensorFlow deep learning images
  * Adds support for the us-east4 region



## August 10, 2020

Feature

**M54 release**

  * Added support for the europe-west3 region
  * Updated the Explainable AI sdk and added explainers
  * Fixed llvm-openmp support
  * Added support for instance auto upgrade
  * Made Deep Learning VM images and Deep Learning Containers more consistent for TPU
  * Updated NCCL to 2.7.6 in CU110 images
  * Added the scikit-learn package and container
  * Added JRE to R images
  * Limited custom container memory utilization



## August 06, 2020

Feature

**M53 release**

TensorFlow Enterprise 2.3 images, including images that support CUDA 11.0, are now available.

## July 13, 2020

Feature

**M51 release**

Allow removing `sudo` access from Deep Learning Containers.

Debian-10-based images are released. You can create [Shielded VM instances](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) from these images.

## June 23, 2020

Fixed

**M50 release**

Miscellaneous bug fixes.

## June 11, 2020

Feature

**M49 release**

TensorFlow Enterprise images updated to 1.15.3 and 2.1.1.

The [tensorflow-enterprise-addons](https://pypi.org/project/tensorflow-enterprise-addons/) package is now available in all deep learning environments.

XGBoost, MXNet, R, PyTorch, CNTK, and Caffe images have been updated with library upgrades and bug fixes.

## May 18, 2020

Feature

**M48 release**

TensorFlow 2.2 images have been added. The new TensorFlow 2.2 image families are `tf2-2-2-cpu` and `tf2-2-2-cu101`. See the [available image families](https://docs.cloud.google.com/deep-learning-vm/docs/images).

## May 12, 2020

Fixed

**M47 release**

Fixed an OS login issue under single user mode for a user external to an organization.

Fixed a git extensions plugin issue in TensorFlow 2 images.

## January 21, 2020

Feature

**M41 release**

[TensorFlow Enterprise](https://docs.cloud.google.com/tensorflow-enterprise/docs) 2.1 images are now available.

MXNet upgraded to 1.5.1.

PyTorch upgraded to 1.4.0.

XGBoost upgraded to 0.90.

## November 01, 2019

Feature

You can now create a TensorFlow Enterprise Deep Learning VM Image. TensorFlow Enterprise image families provide users with a Google Cloud Platform optimized distribution of TensorFlow with [long-term version support](https://docs.cloud.google.com/tensorflow-enterprise/docs/overview#long_term_support_lts). To learn more about TensorFlow Enterprise, read the [TensorFlow Enterprise overview](https://docs.cloud.google.com/tensorflow-enterprise/docs/overview).

## October 11, 2019

Feature

**M36 release**

The TensorFlow 2.0 image is out of experimental.

Change

[What-If Tool (`witwidget`)](https://pair-code.github.io/what-if-tool/) upgraded to 1.4.2 for TensorFlow 1.x images.

## August 26, 2019

Feature

**M34 release**

JupyterLab upgraded to 1.0 on all images.

PyTorch upgraded to 1.2.

## July 12, 2019

Feature

**M30 release**

R upgraded to version 3.6.

TensorFlow: added support for using Python 3.7.

R Notebooks are no longer dependent on a Conda environment.

Fixed

Fix for the bug when Nvidia driver is not installed if the user does not have the Google Cloud Storage API enabled.

[What-If Tool (`witwidget`)](https://pair-code.github.io/what-if-tool/) fixes for TensorFlow 1.14.

Miscellaneous bug fixes.

## July 01, 2019

Feature

**M28 release**

[What-If Tool (`witwidget`)](https://pair-code.github.io/what-if-tool/) added to DLVM.

Fixed

Fixed TensorFlow 1.14 issues.

Miscellaneous bug fixes.

## June 20, 2019

Feature

**M27.1 release updates**

TensorFlow upgraded to: 1.14.0.

TensorFlow 2.0 upgraded to: Beta 1.

Fixed

Miscellaneous bug fixes.

## June 17, 2019

Feature

**M27 release**

New ML framework added: CNTK 2.7 from Microsoft.

New ML framework added: Caffe 1.0 BVLC from UC Berkeley.

Updated TensorFlow 2.0 Beta0.

Fixed

Miscellaneous bug fixes.

## May 29, 2019

Feature

**M26 release**

RAPIDS updated to 0.7.

Faster driver installation time for common TensorFlow and PyTorch images.

You can now use Deep Learning VMs without a public IP address if you have enabled Google Private Access.

Fixed

Miscellaneous bug fixes.

## May 03, 2019

Feature

**M25 release**

New image added: CUDA 10.1.

PyTorch upgraded to 1.1.0.

fastai upgraded to 1.0.52.

MXNet upgraded to 1.4.0 (and now based on CUDA 10.0 images).

Chainer upgraded to 5.4.0.

## April 26, 2019

Feature

**M24 release**

We now support two authorization modes in the new release: single user mode and service account mode3.

rpy2 is now pre-installed in the R image.

A plugin for editing metadata of cells is now pre-installed.

jupyterlab-celltags JupyterLab extension is now pre-installed.

Fixed

Fixed bug with sudo (now you can use sudo from the JupyterLab terminal).

Downloading files from JupyterLab file browser is now working.

## March 15, 2019

Feature

**M22 release**

Tensorflow upgraded to version 1.13.

Issue

Due to incompatibilities between Tensorflow 1.13 (which requires Numpy 1.16.2 or greater) and the latest Intel optimized version of Numpy (which is 1.15) we are not using the intel optimized versions of Numpy and Scipy for this release.

Feature

[Fairing](https://github.com/kubeflow/fairing) now preinstalled.

Fixed

More descriptive serial logs to help customers debug common issues.

Feature

cookiecutter and seaborn now preinstalled.

Fixed

Misc bug fixes.

## February 21, 2019

Feature

**M20 release**

TensorFlow and Pytorch GPU images switch between CPU-only/GPU-enabled binaries at startup depending on whether GPUs are attached.

Issue

Due to incompatibilities between the latest kernel update (Debian 9.8) and Docker, we have put a hold on the kernel updates for this release (that is, `apt-mark hold linux-image-4.9.0-8-amd64`). If you require the latest kernel, you can run `sudo apt-mark unhold linux-image-4.9.0-8-amd64 && sudo apt upgrade`, but we cannot guarantee that Docker or our direct JupyterLab link from [Marketplace](https://console.cloud.google.com/marketplace/details/click-to-deploy-images/deeplearning) will function correctly if you force the upgrade.

Fixed

SSH is not disabled during NVIDIA driver installation on GPU images.

## January 29, 2019

Feature

**M19 release**

New TensorFlow 2.0 (experimental) flavor is added.

New experimental ability to use Deep Learning VMs with special Web proxy, instead of SSHing to the VM.

## January 14, 2019

Feature

**M16 release**

New MXNet 1.3 (experimental) flavor is added.

## December 19, 2018

Feature

**General Availability**

Launched the new 1.0 version of AI Platform Deep Learning VM Image.

Change

fastai updated to the latest version 1.0.38.

Feature

**M15 release**

BigQuery magic plugin now preloaded all the time.

Jupyter SQL integration now pre-installed and SQL plugin now preloaded.

TensorFlow images now include bazel pre-installed.

Python Dataproc client now pre-installed on all our images.

## December 10, 2018

Fixed

**M14 release**

Fixed bug that was resulting in a broken Git UI in some cases.

Feature

Fast.Ai updated to 1.0.36.

## December 05, 2018

Fixed

**M13 release**

Integrates fix for speed regression in linear models when using TensorFlow with Intel® MKL DNN.

Feature

Adds Git-Jupyter integration.

## November 20, 2018

Change

**M12 release**

Chainer is now upgraded to 5.0.0 (and CuPy to 5.0.0).

CuDNN updated to 7.4.

TensorRT5 updated to GA.

XGBoost updated to 0.81.

Images now have papermill pre-installed.

Ability to change Jupyter UI that is running on the port 8080, currently supported: Lab and Notebook.

## November 13, 2018

Fixed

**M11.1 release**

Fixed an issue where users were locked out of `apt` after startup due to a package needing configuration. If you are using an M11 image and are experiencing issues with apt, please either recreate your VM or run `sudo dpkg --configure -a` to clear the lock.

## November 08, 2018

Change

**M11 release**

All GPU images install NVIDIA driver 410.72.

TensorFlow updated to v1.12.0.

PyTorch 0.4 image now uses conda for package management.

## October 23, 2018

Change

**M10 release**

PyTorch 1.0 updated to the latest build as of October 23.

`fastai` updated to 1.0.12.

`fastai` course materials are now available at `$HOME/tutorials/fastai/`.

Chainer UI updated to 0.6.0.

Chainer MN updated to 1.3.1.

Fixed

Fixed a bug that was causing Intel packages to be overwritten.

## October 10, 2018

Feature

**M9 release**

Intel Optimized Python packages are installed in all distributions:

  * NumPy
  * SciPy
  * `scikit-learn`
  * TensorFlow (when applicable)



PyTorch 1.0 (Experimental) images include support for `[conda](https://conda.io/)` and `[fastai](http://fast.ai/)`.

Change

Chainer updated from v4.4.0 to v4.5.0.

## September 27, 2018

Feature

**M8 release**

New XGBoost images:

  * `xgboost-<var>VERSION</var>-cu92-experimental`
  * `xgboost-<var>VERSION</var>-cpu-experimental`



New CUDA 10.0 image (common-cu100) with the following NVIDIA stack in it:

  * CuDNN 7.3
  * NCCL 2.3.4
  * Driver 410.48
  * TensorRT 5



Change

TensorFlow updated from v1.10.1 to v1.11.0.

TensorFlow now compiled with CUDA 10.0 and CuDNN 7.3.

Common CUDA 9.2 image now has latest NCCL 2.3.4

Common CUDA 9.0 image now has:

  * latest NCCL 2.3.4
  * latest CuDNN 7.3
  * TensorRT 5.0.0



Following packages are now pre-installed on the images:

  * `htop`
  * `protobuf-compiler`
  * `tree`



After SSHing to the instance you now will see the exact revision of the image in the header.

## September 18, 2018

Feature

**M7.1 release**

Introducing new experimental images with PyTorch 1.0RC. New image families are:

  * `pytorch-1-0-cu92-experimental`
  * `pytorch-1-0-cpu-experimental`



## September 12, 2018

Change

**M7 release**

Chainer updated from v4.3.0 to v4.4.0.

Better integration with BigQuery.

Pillow has been replaced with the faster Pillow-SIMD package.

`minikube` is now pre-installed.

New simplified image families introduced:

  * `tf-latest-gpu`
  * `pytorch-latest-gpu`
  * `chainer-latest-gpu-experimental`



Fixed

Jupyter now running on behalf of its own user (not root).

## August 30, 2018

Feature

**M6 release**

Introducing experimental images: these images bring new frameworks for you to try out, but they come with no guarantees of future support. Current experimental images:

  * Chainer (4.3)



Feature

All images now have `kubectl` installed.

Change

TensorFlow updated from v1.10.0 to v1.10.1.

## August 14, 2018

Feature

**M5 release**

All images now have Docker and/or NVIDIA Docker pre-installed.

TensorFlow and PyTorch images now include pre-baked tutorials.

GPU flavors of TensorFlow and PyTorch images now swap binaries to the CPU optimized binaries during the first boot if the instance does not have a GPU.

## July 31, 2018

Feature

**M4 release**

Includes Tensorfow Serving: model server binary at /usr/local/bin/tensorflow_model_server and tensorflow-serving-api preinstalled.

Integration with Colab: default JupyterLab instance can be connected as a Colab backend.

Upgraded to support CUDA 9.2 (note this changes the pytorch family name).

Fixed

Fixed an issue with CUDA linking in the build process, binaries up to 10% faster now.

## July 17, 2018

Feature

**M3 release**

New common image with CUDA 9.0 has been introduced.

Change

The following changes are included in this release:

  * All images now include [OpenMPI](https://www.open-mpi.org).
  * TensorFlow GPU images now include [Horovod](https://github.com/uber/horovod).
  * CUDA 9.2 stack now includes latest NCCL 2.2.13.



Fixed

Bug that was preventing Jupyter Notebook from working correctly has been resolved.

## July 11, 2018

Feature

**M2 release**

TensorFlow updated to version 1.9.0.

New public Google Group for users: [google-dl-platform](https://groups.google.com/forum/#!forum/google-dl-platform)

## July 02, 2018

Feature

**Beta launch**

AI Platform Deep Learning VM Image is available as a beta release.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
