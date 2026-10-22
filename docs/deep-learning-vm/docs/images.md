---
url: https://docs.cloud.google.com/deep-learning-vm/docs/images/
title: Choose an image \u00a0|\u00a0 Deep Learning VM Images \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:50.193651+00:00
---

# Choose an image  |  Deep Learning VM Images  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deep-learning-vm/docs/images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Deep Learning VM Images ](https://docs.cloud.google.com/deep-learning-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/deep-learning-vm/docs/introduction)



Send feedback 

#  Choose an image Stay organized with collections  Save and categorize content based on your preferences. 

Specific Deep Learning VM Images images are available to suit your choice of framework and processor. There are currently images supporting PyTorch and generic high-performance computing, with versions for GPU-enabled workflows. To find the image that you want, see the table below.

## Deciding on an image family

Choose a Deep Learning VM image family based on the framework and processor that you need. The following table lists the most recent versions of image families, organized by framework type. To get the most recent version of an image, create an instance by referencing an image family with `latest` in the name. If you need a specific framework version, skip to Supported framework versions.

Framework | Processor | Image family name(s)  
---|---|---  
Base | GPU |  `common-cu129-ubuntu-2404-nvidia-580`  
`common-cu129-ubuntu-2204-nvidia-580`  
  
PyTorch | GPU |  `pytorch-2-9-cu129-ubuntu-2404-nvidia-580`  
`pytorch-2-9-cu129-ubuntu-2204-nvidia-580`  
  
  
### Choosing an operating system

Ubuntu 22.04 and 24.04 are supported OS versions, and the images come with the NVIDIA driver version 580. They are denoted by the `-ubuntu-2204-nvidia-580` and `-ubuntu-2404-nvidia-580` suffixes in the image family name (see Listing all available versions). Debian images have all been deprecated.

All active images support A3 Ultra GPU accelerators.

### PyTorch images

PyTorch image families provide a Google Cloud optimized distribution of PyTorch and PyTorch Lightning.

## Specifying an image version

You can reuse the same image even if the latest image is newer. This can be useful, for instance, if you are trying to create a cluster and you want to ensure that any images that are used to create new instances are always the same. You should not use the name of the image family in this situation because, if the latest image is updated, you'll have different images on some instances in your cluster.

Instead, you can determine what the exact name of the image is, incorporate the version number, and then use that specific image to spawn new instances in your cluster.

To find out the exact name of the latest image, use the following command in the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) with your preferred terminal or in [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell). Replace IMAGE_FAMILY with the image family name for which you want to find out the latest version number.
    
    
    gcloud compute images describe-from-family IMAGE_FAMILY \
            --project deeplearning-platform-release

Look for the `name` field in the output and use the image name given there when creating new instances.

## Supported framework versions

Deep Learning VM supports each framework version based on a schedule to minimize security vulnerabilities. Review the [Deep Learning VM framework support policy](https://docs.cloud.google.com/deep-learning-vm/docs/framework-support-policy) to understand the implications of the end-of-support and end-of-availability dates.

If you need a specific framework or CUDA version, see the following tables. To find a specific `VERSION_DATE` for an image, see Listing the available versions.

### Base versions

All CPU-based images have been deprecated.

ML framework version | Current patch version | Supported accelerators | End of patch and support date | End of availability date | Image family name  
---|---|---|---|---|---  
Base-cu129 (Python 3.12 / Ubuntu 24.04) | CUDA 12.9 | GPU (CUDA 12.9) | August 4, 2028 | August 4, 2028 | `common-cu129-ubuntu-2404-nvidia-580-VERSION_DATE`  
Base-cu129 (Python 3.12 / Ubuntu 22.04) | CUDA 12.9 | GPU (CUDA 12.9) | August 4, 2028 | August 4, 2028 | `common-cu129-ubuntu-2204-nvidia-580-VERSION_DATE`  
Base-cu128 (Python 3.10 / Ubuntu 22.04) | CUDA 12.8 | GPU (CUDA 12.8) | April 13, 2026 | April 13, 2027 | `common-cu128-ubuntu-2204-nvidia-570-VERSION_DATE`  
Base-CPU (Python 3.10 / Debian 11) | Not applicable (N/A) | CPU only | Jul 1, 2024 | Jul 1, 2025 | `common-cpu-VERSION_DATE-debian-11`  
Base-cu124 (Python 3.10) | CUDA 12.4 | GPU (CUDA 12.4) | April 1, 2025 | April 1, 2026 | `common-cu124-VERSION_DATE-debian-11-py310`  
Base-cu123 (Python 3.10) | CUDA 12.3 | GPU (CUDA 12.3) | Oct 19, 2024 | Oct 19, 2025 | `common-cu123-VERSION_DATE-debian-11-py310`  
Base-cu122 (Python 3.10) | CUDA 12.2 | GPU (CUDA 12.2) | June 28, 2024 | June 28, 2025 | `common-cu122-VERSION_DATE-debian-11-py310`  
Base-cu121 (Python 3.10) | CUDA 12.1 | GPU (CUDA 12.1) | Feb 28, 2024 | Feb 28, 2025 | `common-cu121-VERSION_DATE-debian-11-py310`  
Base-cu118 (Python 3.10) | CUDA 11.8 | GPU (CUDA 11.8) | Jul 1, 2024 | Jul 1, 2025 | `common-cu118-VERSION_DATE-debian-11-py310`  
Base-cu113 (Python 3.10) | CUDA 11.3 | GPU (CUDA 11.3) | Jan 1, 2024 | Jan 1, 2025 | `common-cu113-VERSION_DATE-debian-11-py310`  
Base-cu113 (Python 3.7) | CUDA 11.3 | GPU (CUDA 11.3) | Sep 1, 2023 | Sep 1, 2024 | `common-cu113-VERSION_DATE-py37`  
Base-cu110 (Python 3.7) | CUDA 11.0 | GPU (CUDA 11.0) | Sep 1, 2023 | Sep 1, 2024 | `common-cu110-VERSION_DATE-py37`  
Base-CPU (Python 3.7) | Not applicable (N/A) | CPU only | Sep 1, 2023 | Sep 1, 2024 | `common-cpu-VERSION_DATE-debian-10`  
  
### PyTorch versions

ML framework version | Current patch version | Supported accelerators | End of patch and support date | End of availability date | Image family name  
---|---|---|---|---|---  
2.9 (Python 3.12 / Ubuntu 24.04) | 2.9.0 | CUDA 12.9 | August 4, 2028 | August 4, 2028 | `pytorch-2-9-cu129-ubuntu-2404-nvidia-580-VERSION_DATE`  
2.9 (Python 3.12 / Ubuntu 22.04) | 2.9.0 | CUDA 12.9 | August 4, 2028 | August 4, 2028 | `pytorch-2-9-cu129-ubuntu-2204-nvidia-580-VERSION_DATE`  
2.7 (Python 3.10) | 2.7.1 | CUDA 12.8 | April 13, 2026 | April 13, 2027 | `pytorch-2-7-cu128-ubuntu-2204-nvidia-570-VERSION_DATE`  
2.4 (Python 3.10) | 2.4.0 | CUDA 12.4 | Jul 24, 2025 | Jul 24, 2026 | `pytorch-2-4-VERSION_DATE-py310`  
2.3 (Python 3.10) | 2.3.0 | CUDA 12.1 | Apr 24, 2025 | Apr 24, 2026 | `pytorch-2-3-VERSION_DATE-py310`  
2.2 (Python 3.10) | 2.2.0 | CUDA 12.1 | Jan 30, 2025 | Jan 30, 2026 | `pytorch-2-2-VERSION_DATE-py310`  
2.1 (Python 3.10) | 2.1.0 | CUDA 12.1 | Oct 4, 2024 | Oct 4, 2025 | `pytorch-2-1-VERSION_DATE-py310`  
2.0 (Python 3.10) | 2.0.0 | CUDA 11.8 | Mar 15, 2024 | Mar 15, 2025 | `pytorch-2-0-VERSION_DATE-py310`  
1.13 (Python 3.10) | 1.13.1 | CUDA 11.3 | Dec 8, 2023 | Dec 8, 2024 | `pytorch-1-13-VERSION_DATE-py310`  
1.13 | 1.13.1 | CUDA 11.3 | Dec 8, 2023 | Dec 8, 2024 | `pytorch-1-13-VERSION_DATE-py37`  
1.12 | 1.12.1 | CUDA 11.3 | Sep 1, 2023 | Sep 1, 2024 | `pytorch-1-12-VERSION_DATE-py310`  
  
### TensorFlow versions

All TensorFlow images have been deprecated.

ML framework version | Current patch version | Supported accelerators | End of patch and support date | End of availability date | Image family name  
---|---|---|---|---|---  
2.17 (Python 3.10) | 2.17.0 | CPU only | Jul 11, 2025 | Jul 11, 2026 | `tf-2-17-cpu-VERSION_DATE-py310`  
2.17 (Python 3.10) | 2.17.0 | GPU (CUDA 12.3) | Jul 11, 2025 | Ju1 11, 2026 | `tf-2-17-cu123-VERSION_DATE-py310`  
2.16 (Python 3.10) | 2.16.2 | CPU only | Jun 28, 2025 | Jun 28, 2026 | `tf-2-16-cpu-VERSION_DATE-py310`  
2.16 (Python 3.10) | 2.16.2 | GPU (CUDA 12.3) | Jun 28, 2025 | Jun 28, 2026 | `tf-2-16-cu123-VERSION_DATE-py310`  
2.15 (Python 3.10) | 2.15.0 | CPU only | Nov 14, 2024 | Nov 14, 2025 | `tf-2-15-cpu-VERSION_DATE-py310`  
2.15 (Python 3.10) | 2.15.0 | GPU (CUDA 12.2) | Nov 14, 2024 | Nov 14, 2025 | `tf-2-15-cu122-VERSION_DATE-py310`  
2.14 (Python 3.10) | 2.14.0 | CPU only | Sep 26, 2024 | Sep 26, 2025 | `tf-2-14-cpu-VERSION_DATE-py310`  
2.14 (Python 3.10) | 2.14.0 | GPU (CUDA 11.8) | Sep 26, 2024 | Sep 26, 2025 | `tf-2-14-cu118-VERSION_DATE-py310`  
2.13 (Python 3.10) | 2.13.0 | CPU only | Jul 5, 2024 | Jul 5, 2025 | `tf-2-13-cpu-VERSION_DATE-py310`  
2.13 (Python 3.10) | 2.13.0 | GPU (CUDA 11.8) | Jul 5, 2024 | Jul 5, 2025 | `tf-2-13-cu118-VERSION_DATE-py310`  
2.12 (Python 3.10) | 2.12.0 | CPU only | June 30, 2024 | June 30, 2025 | `tf-2-12-cpu-VERSION_DATE-py310`  
2.12 (Python 3.10) | 2.12.0 | GPU (CUDA 11.8) | June 30, 2024 | June 30, 2025 | `tf-2-12-cu113-VERSION_DATE-py310`  
2.11 (Python 3.10) | 2.11.0 | CPU only | Nov 15, 2022 | Nov 15, 2023 | `tf-2-11-cpu-VERSION_DATE-py310`  
2.11 (Python 3.10) | 2.11.0 | GPU (CUDA 11.3) | Nov 15, 2022 | Nov 15, 2023 | `tf-2-11-cu113-VERSION_DATE-py310`  
2.11 | 2.11.0 | CPU only | Nov 15, 2023 | Nov 15, 2024 | `tf-2-11-cpu-VERSION_DATE-py37`  
2.11 | 2.11.0 | GPU (CUDA 11.3) | Nov 15, 2023 | Nov 15, 2024 | `tf-2-11-cu113-VERSION_DATE-py37`  
2.10 | 2.10.1 | CPU only | Nov 15, 2023 | Nov 15, 2024 | `tf-2-10-cpu-VERSION_DATE-py37`  
2.10 | 2.10.1 | GPU (CUDA 11.3) | Nov 15, 2023 | Nov 15, 2024 | `tf-2-10-cu113-VERSION_DATE-py37`  
2.9 | 2.9.3 | CPU only | Nov 15, 2023 | Nov 15, 2024 | `tf-2-9-cpu-VERSION_DATE-py37`  
2.9 | 2.9.3 | GPU (CUDA 11.3) | Nov 15, 2023 | Nov 15, 2024 | `tf-2-9-cu113-VERSION_DATE-py37`  
2.8 | 2.8.4 | CPU only | Nov 15, 2023 | Nov 15, 2024 | `tf-2-8-cpu-VERSION_DATE-py37`  
2.8 | 2.8.4 | GPU (CUDA 11.3) | Nov 15, 2023 | Nov 15, 2024 | `tf-2-8-cu113-VERSION_DATE-py37`  
2.6 (py39) | 2.6.5 | CPU only | Sep 1, 2023 | Sep 1, 2024 | `tf-2-6-cpu-VERSION_DATE-py39`  
2.6 (py39) | 2.6.5 | GPU (CUDA 11.3) | Sep 1, 2023 | Sep 1, 2024 | `tf-2-6-cu110-VERSION_DATE-py39`  
2.6 (py37) | 2.6.5 | CPU only | Sep 1, 2023 | Sep 1, 2024 | `tf-2-6-cpu-VERSION_DATE-py37`  
2.6 (py37) | 2.6.5 | GPU (CUDA 11.3) | Sep 1, 2023 | Sep 1, 2024 | `tf-2-6-cu110-VERSION_DATE-py37`  
2.3 | 2.3.4 | CPU only | Sep 1, 2023 | Sep 1, 2024 | `tf-2-3-cpu`  
2.3 | 2.3.4 | GPU (CUDA 11.3) | Sep 1, 2023 | Sep 1, 2024 | `tf-2-3-cu110-VERSION_DATE`  
  
## After deprecation

When images reach the **End-of-patch and support date** , they are deprecated. Deprecation means that these images are removed from public visibility and it's encouraged to use supported images to help ensure security and performance.

If your Deep Learning VM image is deprecated or reaches its end of availability, we highly recommend that you migrate to a newer, supported image. This helps make sure you continue to receive critical security patches and the latest features. Consider the following forms of migration:

  * If there is a newer, supported image in the same image family, we recommend upgrading your image to a supported version of the same image family.
  * If there are no newer, supported images in the same image family, consider a newer, supported framework from a different VM image family.



### Use an image after deprecation

If you must use an image after deprecation _against Google security recommendations and at your own risk_ , you must specify an image from the image family when you create the VM instance.

To list images from an image family name after its end of patch and support date, include the `--show-deprecated` flag in your `gcloud compute images list` command, or select **Show deprecated images** when creating an instance in the Google Cloud console. See List all available versions using gcloud CLI.

To create a Deep Learning VM instance that uses a deprecated image, see the following example gcloud CLI command:
    
    
    gcloud compute instances create deprecated-tf-vm \
        --image=projects/deeplearning-platform-release/global/images/IMAGE_NAME \
        --machine-type=n1-standard-4 \
        --zone=us-east1-c

Replace IMAGE_NAME with the name of the image, as follows:

  * To use a specific image in the image family, use the image name, for example: `pytorch-2-9-cu129-ubuntu-2204-nvidia-580-v20260416`.



## List all available versions using gcloud CLI

You can also list all available Deep Learning VM images using the following [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) command:
    
    
    gcloud compute images list \
        --project deeplearning-platform-release \
        --format="value(NAME)" \
        --no-standard-images

**Note:** The output of this command includes some image family framework types that aren't mentioned in the previous table of family names. These are image families that aren't updated anymore.

Image families are named in the format `FRAMEWORK-CUDA_VERSION-OS`, where `FRAMEWORK` is the target library, `CUDA_VERSION` is the version of the CUDA stack, and `OS` denotes the operation system with the pre-installed NVIDIA driver.

For example, an image from the family `pytorch-2-9-cu129-ubuntu-2204-nvidia-580` has PyTorch 2.9, CUDA 12.9, and the OS is Ubuntu 22.04 with NVIDIA driver 580 pre-installed.

## What's next

Create a new Deep Learning VM instance [using the Cloud Marketplace](https://docs.cloud.google.com/deep-learning-vm/docs/cloud-marketplace) or [using the command line](https://docs.cloud.google.com/deep-learning-vm/docs/cli).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
