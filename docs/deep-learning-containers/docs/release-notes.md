---
url: https://docs.cloud.google.com/deep-learning-containers/docs/release-notes/
title: Deep Learning Containers release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:14.819915+00:00
---

# Deep Learning Containers release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deep-learning-containers/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Deep Learning Containers ](https://docs.cloud.google.com/deep-learning-containers/docs)
  * [ Resources ](https://docs.cloud.google.com/deep-learning-containers/docs/release-notes)



Send feedback 

#  Deep Learning Containers release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Deep Learning Containers. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/aiplatformdeeplearningcontainers-release-notes.xml) directly. 

## March 12, 2025

Feature

**M128 release**

  * Except for TensorFlow container images, new container images don't include conda. This change was made to improve size, performance, and vulnerability management. The existing container image names now point to container images that don't include conda (for example: `gcr.io/deeplearning-platform-release/base-cpu.py310`).
  * Container images that include conda will be available until at least September 30, 2025. These container images now have `-conda` appended to the name (for example: `gcr.io/deeplearning-platform-release/base-cpu-conda.py310`).
  * All TensorFlow container images still include conda, but M128 container image names have `-conda` appended. Specifying container images without `-conda` appended references older container images, which also include conda.



## January 16, 2025

Feature

**M127 release**

  * The following framework versions have reached their end of patch and support dates:

    * Tensorflow versions 2.15 and earlier
    * PyTorch versions 2.1 and earlier
    * Base versions with CUDA 12.1 and earlier

To view the end of patch and support dates, see [Supported framework versions](https://docs.cloud.google.com/deep-learning-containers/docs/choosing-container). Framework versions remain available for use until their end of availability date, but recent versions are strongly recommended.




## November 20, 2024

Feature

**M126 release**

  * Base CUDA 12.3 container images are now available.
  * Base CUDA 12.4 container images are now available.
  * PyTorch 2.4.0 with CUDA 12.4 and Python 3.10 container images are now available.
  * Upgraded R from 4.4.1 to 4.4.2 for R container images.



## September 26, 2024

Feature

**M125 release**

  * TensorFlow 2.17 container images are now available.



## August 20, 2024

Feature

**M124 release**

  * Pytorch 2.3.0 with CUDA 12.1 and Python 3.10 container images are now available.



## July 16, 2024

Feature

**M123 release**

  * Hugging Face Text Generation Inference 2.1 GPU container images are now available.



## June 21, 2024

Feature

**M122 release**

  * TensorFlow 2.16 container images are now available.
  * PyTorch Inference 2.2 GPU container images are now available.
  * PyTorch Inference 2.2 CPU container images are now available.



## May 17, 2024

Feature

**M121 release**

  * Updated the R CPU container image from R 4.3 to R 4.4. The R 4.3 container image is deprecated. There will be no further updates to this image in future releases.



## April 25, 2024

Feature

**M120 release**

  * Upgraded TensorFlow 2.15 container images to TensorFlow 2.15.1.
  * Added CUDA-specific release tags for all TensorFlow and PyTorch container images, for example, `us-docker.pkg.dev/deeplearning-platform-release/gcr.io/tf-cu121.2-15`.



## March 29, 2024

Fixed

**M119 release**

  * Fixed an issue wherein Dataproc extensions caused JupyterLab to crash when remote kernels weren't available.



## March 18, 2024

Feature

**M118 release**

  * PyTorch 2.1.0 with CUDA 12.1 and Python 3.10 container images are now available.
  * PyTorch 2.2.0 with CUDA 12.1 and Python 3.10 container images are now available.



## February 20, 2024

Feature

**M117 release**

  * Fixed an issue wherein the `latest` container had a `deprecation-public-image` tag. In this release and future releases, this tag will only be on the deprecated containers.
  * Fixed a problem wherein the user couldn't access the vulnerabilities result of each container.



## January 19, 2024

Feature

**M115 release**

  * TensorFlow 2.15 with CUDA 12.1 and Python 3.10 container images are now available.
  * TensorFlow 2.14 with CUDA 11.8 and Python 3.10 container images are now available.



## December 14, 2023

Feature

**M114 release**

  * Starting with this release, Python 3.7 is no longer available.
  * Upgraded R to 4.3 on Python 3.10 containers.
  * Fixed an issue where the PySpark-BigQuery connector didn't work properly on Python 3.10 PySpark container.



## November 16, 2023

Feature

**M113 release**

  * Miscellaneous bug fixes and improvements in Python 3.10 container images.



## October 10, 2023

Feature

**M112 release**

  * Miscellaneous bug fixes and improvements.



## September 14, 2023

Feature

**M111 release**

  * PyTorch 2.0 container images now include PyTorch XLA 2.0.
  * Miscellaneous software updates.



## August 10, 2023

Feature

**M110 release**

  * Added support for TensorFlow 2.13 with Python 3.10 on Debian 11.
  * Added support for TensorFlow 2.8 with Python 3.10 on Debian 11.
  * Miscellaneous software updates.



Deprecated

TensorFlow 2.9 container images are deprecated.

## June 26, 2023

Feature

**M109 release**

  * PyTorch 2.0 with Python 3.10 and CUDA 11.8 container images are now available.
  * Miscellaneous software updates.



## May 09, 2023

Feature

**M108 update**

This update of the M108 release includes the following:

  * The following Deep Learning Containers images are now available: 
    * Tensorflow 2.12 CPU with CUDA 11.8 and Python 3.10 (`us-docker.pkg.dev/deeplearning-platform-release/gcr.io/tf-cpu.2-12.py310:latest`)
    * Tensorflow 2.12 GPU with CUDA 11.8 and Python 3.10 (`us-docker.pkg.dev/deeplearning-platform-release/gcr.io/tf-gpu.2-12.py310:latest`)



## May 04, 2023

Feature

**M108 release**

  * Miscellaneous software updates.



## April 13, 2023

Feature

**M107 release**

  * Miscellaneous software updates.



## April 06, 2023

Feature

**M106 release**

  * Miscellaneous software updates.



## March 31, 2023

Feature

**M105 release**

  * The following Deep Learning Containers images are now available with Python 3.10 on Debian 11:

    * TensorFlow 2.11 CPU (`us-docker.pkg.dev/deeplearning-platform-release/gcr.io/tf-cpu.2-11.py310:latest`)
    * TensorFlow 2.11 GPU with Cuda 11.3 (`us-docker.pkg.dev/deeplearning-platform-release/gcr.io/tf-gpu.2-11.py310:latest`)
    * PyTorch 1.13 with Cuda 11.3 (`us-docker.pkg.dev/deeplearning-platform-release/gcr.io/pytorch-gpu.1-13.py310:latest`)
    * Base CPU (`us-docker.pkg.dev/deeplearning-platform-release/gcr.io/base-cpu.py310:latest`)
    * Base GPU with Cuda 11.3 (`us-docker.pkg.dev/deeplearning-platform-release/gcr.io/base-cu113.py310:latest`)
  * The following Deep Learning Containers images are now available with Python 3.9 on Debian 11:

    * TensorFlow 2.6 CPU (`us-docker.pkg.dev/deeplearning-platform-release/gcr.io/tf-cpu.2-6.py39:latest`)
    * TensorFlow 2.6 GPU with Cuda 11.3 (`us-docker.pkg.dev/deeplearning-platform-release/gcr.io/tf-gpu.2-6.py39:latest`)
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



Change

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
  * Regular security patches and package upgrades.



## December 09, 2022

Feature

**M101 release**

  * TensorFlow patch version upgrades: 
    * From 2.8.3 to 2.8.4.
    * From 2.9.2 to 2.9.3.
    * From 2.10.0 to 2.10.1.
  * TensorFlow 1.15 Deep Learning Containers images are now deprecated.
  * Regular security patches and package upgrades.



## November 08, 2022

Feature

**M100 release**

  * Regular package updates.



## November 02, 2022

Feature

**M99 release**

  * Fixed a bug where Jupyter widgets through `ipywidgets` were causing errors and not displaying.
  * Regular package updates.



## October 18, 2022

Feature

**M98 release**

  * Upgraded JupyterLab from 3.2 to 3.4.
  * Upgraded R from 4.1 to 4.2.
  * Miscellaneous bug and display fixes.
  * Regular package updates.



## September 29, 2022

Feature

**M97 release**

  * Regular package updates.



## September 20, 2022

Feature

**M96 release**

  * TensorFlow 2.10.0 is now available.
  * TensorFlow patch updates for 2.9.2 and 2.8.3 are now available.
  * The PyTorch patch update for 1.12.1 is now available.
  * Miscellaneous bug fixes.



## August 12, 2022

Feature

**M95 release**

  * Tensorflow has been updated to 2.9.1, 2.8.1, and 2.6.5 to include upstream changes.
  * Regular package refreshment and bug fixes.



## July 06, 2022

Feature

**M94 release**

  * Added support for PyTorch 1.12.
  * Added more system libraries to the R Deep Learning Containers image.



## May 27, 2022

Feature

**M93 release**

  * Starting with this release, information on known vulnerabilities for Deep Learning Containers images is now available on Cloud Storage.



## May 16, 2022

Feature

**M92 release**

  * TensorFlow Enterprise 2.9 is now available. Note that this TensorFlow Enterprise version does not include [Long Term Version Support](https://docs.cloud.google.com/tensorflow-enterprise/docs/overview#long_term_version_support).
  * Starting with PyTorch 1.11, PyTorch environments now support XLA by default.
  * TensorFlow Enterprise patch releases: 2.6.4 and 2.8.1.
  * Deep Learning Containers are now available on Artifact Registry.



## March 21, 2022

Feature

**M91 release**

  * PyTorch 1.11 and PyTorch XLA 1.11 are now available in both Deep Learning Containers and Deep Learning VM Images.



Fixed

  * Fixed an R package installation issue for R Deep Learning Containers and Vertex AI Workbench.



## February 28, 2022

Feature

**M90 release**

  * CUDA has been upgraded from 11.3.0 to 11.3.1 to address some NCCL issues.
  * VSlim GPU TensorFlow containers are available and have a significantly smaller size.
  * TensorFlow 2.7 containers are re-released.



## February 02, 2022

Feature

**M89 release**

  * TensorFlow Enterprise 2.8 is now available and includes [Long Term Version Support](https://docs.cloud.google.com/tensorflow-enterprise/docs/overview#long_term_version_support). TensorFlow Enterprise 2.8 is available in both Deep Learning Containers and [Deep Learning VM Images](https://docs.cloud.google.com/deep-learning-vm). 
  * Upgraded TensorFlow Enterprise 2.6.2 to 2.6.3.



## December 20, 2021

Fixed

**M88 release**

  * To help address the Apache Log4j 2 vulnerability, H2O has been updated to 3.34.0.6 in the R container images. This addresses [CVE-2021-44228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228) and [CVE-2021-45046](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-45046). See the [official H2O update](https://www.h2o.ai/security/bulletins/h2o-2021-001/).



Feature

  * Starting with this release, the Python packages that are installed on each container image are listed in files that are available on Cloud Storage.



## December 06, 2021

Change

  * TensorFlow 2.x container image names are available in two formats: the current standard, which includes a `tf-` prefix, and the previous standard, which includes a `tf2-` prefix. For example, both `gcr.io/deeplearning-platform-release/tf-gpu.2-7` and `gcr.io/deeplearning-platform-release/tf2-gpu.2-7` are available although they are the same container images. Starting within approximately six months, releases of TensorFlow 2 container images will only be named with the current standard.



Feature

**M87 release**

  * Added Artifact Registry's [Python keyring authentication library](https://docs.cloud.google.com/artifact-registry/docs/python/authentication#keyring) to deep learning vm environments.



## November 18, 2021

Feature

**M86 release**

  * Upgraded all Ubuntu 18.04 LTS Deep Learning Container images to Ubuntu 20.04 LTS (see [What is an Ubuntu LTS release?](https://ubuntu.com/blog/what-is-an-ubuntu-lts-release)).
  * Released PyTorch/XLA 1.10.
  * Upgraded TensorFlow Enterprise image to the latest patch version: 2.6.2
  * Deprecated CUDA 10.x environments.
  * Locked JupyterLab version to 3.2.



## November 08, 2021

Feature

**M85 release**

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

  * Released CUDA11.3 container images.
  * The [Vertex SDK for Python](https://googleapis.dev/python/aiplatform/latest/index.html) is available across all deep learning environment products; it was previously available only in TensorFlow images.



## October 12, 2021

Feature

**M81 release**

  * Upgraded R to 4.1.



Fixed

  * Fixed bug that prevented R kernels from working properly.



## September 24, 2021

Breaking

Starting with the M80 image release, all environments will include JupyterLab 3.x by default. To continue using an existing environment's JupyterLab 1.x version, disable [auto-upgrade](https://docs.cloud.google.com/notebooks/docs/upgrade#create_a_new_instance_with_auto_upgrade_enabled) (if enabled) and do not manually upgrade the environment to a new environment version. To create new instances using older images that have JupyterLab 1.x installed, see [creating specific versions of instances](https://docs.cloud.google.com/notebooks/docs/create-specific-version).

Feature

**M80 release**

  * Updated JupyterLab from 1.x to 3.x.
  * Added [Jupytext](https://jupytext.readthedocs.io/en/latest/index.html).



## September 09, 2021

Feature

**M79 release**

  * Updated Pytorch 1.9 containers (they were not refreshed in the last release).
  * Updated Theia IDE (experimental) containers.
  * Node.js is pinned to `>=12.14.1,<13`.



Breaking

  * M79 is the last release version that has JupyterLab 1.x installed. For the next release (M80), JupyterLab will be upgraded to 3.x for all Deep Learning VM Images, Deep Learning Containers, and Notebooks.



Fixed

  * Fixed a bug in which the home folder in custom container VMs was owned by the root instead of Jupyter.



## August 18, 2021

Deprecated

**TensorFlow Enterprise 2.5**

  * TensorFlow Enterprise 2.5 Deep Learning Containers are now deprecated.



Feature

**M78 release**

  * Updated TensorFlow Enterprise patch version 2.3.3 to 2.3.4.



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

  * Enhanced environment configurations so it is easier to install additional frameworks in CUDA containers.



## June 22, 2021

Feature

**M73 release**

  * Upgraded TensorFlow Enterprise 2.1.3 to 2.1.4.
  * Upgraded TensorFlow Enterprise 2.3.2 to 2.3.3.
  * Miscellaneous bug fixes and updates.



## June 17, 2021

Feature

**M72 release**

  * Added PyTorch 1.9 and PyTorch/XLA 1.9 containers.



## June 02, 2021

Feature

**M71 release**

  * Upgraded [TensorFlow Probability](https://www.tensorflow.org/probability), [TensorFlow I/O](https://www.tensorflow.org/io), and TensorFlow Estimator in TensorFlow 2.5 containers.



## May 14, 2021

Feature

**M70 release**

  * Added TensorFlow Enterprise 2.5 containers. Note this is an Enterprise version but not a Long Term Support (LTS) version.



## May 13, 2021

Feature

**M69 release**

  * Updated cuDNN from 8.0.4 to 8.0.5.



## May 05, 2021

Feature

**M68 release**

  * Upgraded R containers from 3.6 to 4.0.
  * Added xai-tabular-widget onto all TensorFlow containers.
  * Miscellaneous bug fixes and updates.



## April 19, 2021

Feature

**M67 release**

  * Added Horovod to TensorFlow GPU containers.
  * Regular package refreshment and bug fixes.



## March 31, 2021

Feature

**M66 release**

  * PyTorch 1.8 support in deep learning environments ([Deep Learning VM Image](https://docs.cloud.google.com/ai-platform/deep-learning-vm/docs) and [Deep Learning Containers](https://docs.cloud.google.com/ai-platform/deep-learning-containers/docs)) is available.
  * Fixed scope allocator optimization issue with the TensorFlow Enterprise 2.3/2.1 MKL build.



## March 05, 2021

Feature

**M65 release**

  * Upgraded tensorflow-cloud to 0.1.13.

  * Regular package refreshment and bug fixes.




## February 19, 2021

Feature

**M64 release**

  * Upgraded TensorFlow 2.4 to 2.4.1.

  * Upgraded TFX and [Fairness Indicators](https://www.tensorflow.org/responsible_ai/fairness_indicators/guide) from 0.26.0 to 0.27.0.

  * Miscellaneous bug fixes and updates.




Deprecated

**Swift For TensorFlow**

  * The Swift For TensorFlow project is entering archive mode. Containers will be deprecated and will no longer receive updates after this release.



## February 08, 2021

Feature

**M63 release**

  * SWIFT 0.12 ([experimental](https://docs.cloud.google.com/ai-platform/deep-learning-containers/docs/choosing-container#experimental_images)) containers are available.



## January 25, 2021

Announcement

**General Availability**

AI Platform Deep Learning Containers is now [generally available](https://cloud.google.com/products#product-launch-stages).

Deprecated

**Python 2**

Python 2 is no longer supported in Deep Learning Containers. Read more about [Python 2 support on Google Cloud](https://docs.cloud.google.com/python/docs/python2-sunset#:%7E:text=The%20Python%20community%20announced%20that,as%20soon%20as%20they%20can.&text=Managed%20compute%20services%2C%20such%20as,runtime%20beyond%20January%201%2C%202020.).

Feature

**M62 release**

  * Upgraded TensorFlow 2.3 to 2.3.2

  * Upgraded TensorFlow 2.1 to 2.1.3

  * Miscellaneous bug fixes and updates




## December 16, 2020

Feature

Added TensorFlow 2.4 Deep Learning Containers images.

## October 28, 2020

Feature

  * Added PyTorch 1.6 CUDA 11 environments that support [A100 GPU](https://cloud.google.com/blog/products/compute/announcing-google-cloud-a2-vm-family-based-on-nvidia-a100-gpu) accelerators. This special PyTorch build provides another option to add to our A100-compatible TensorFlow Enterprise builds.



## August 17, 2020

Feature

TensorFlow Enterprise 2.3 environments are now available. These environments include support for A100 GPU accelerators, CUDA 11, and TensorFloat-32 (TF32).

## January 08, 2020

Feature

TensorFlow Enterprise environments are now available. [Use TensorFlow Enterprise with Deep Learning Containers](https://docs.cloud.google.com/tensorflow-enterprise/docs/use-with-deep-learning-containers).

## June 24, 2019

Feature

AI Platform Deep Learning Containers is now available in beta. AI Platform Deep Learning Containers lets you quickly prototype with a portable and consistent environment for developing, testing, and deploying your AI applications.

Visit the [AI Platform Deep Learning Containers overview](https://docs.cloud.google.com/ai-platform/deep-learning-containers/docs/overview) and the guide to [getting started with a local deep learning container](https://docs.cloud.google.com/ai-platform/deep-learning-containers/docs/getting-started-local).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
