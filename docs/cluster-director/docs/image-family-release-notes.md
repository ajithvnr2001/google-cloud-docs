---
url: https://docs.cloud.google.com/cluster-director/docs/image-family-release-notes/
title: Image family release notes \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:11.277940+00:00
---

# Image family release notes  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/image-family-release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Resources ](https://docs.cloud.google.com/cluster-director/docs/resources)



Send feedback 

#  Image family release notes Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the available operating system (OS) image families that you can use in Cluster Director, their end of support (EOS) dates, and their patch release notes.

To help ensure that your clusters run smoothly and receive security updates, you must periodically update the node sets in your clusters to use a supported image family. For more information about the lifecycle of an image family in Cluster Director, see [Image family lifecycle](https://docs.cloud.google.com/cluster-director/docs/os-images#lifecycle).

## Supported image families

The following table lists the supported image families for the compute and login nodes in a cluster:

Image family | Supported machine series | End of support | Release notes  
---|---|---|---  
`a4x-ubuntu-2404-arm64-nvidia-595-slurm-2605-v20260903` | A4X and C4A | September 15, 2027 | View notes  
`a4x-ubuntu-2404-arm64-nvidia-580-slurm-2505-v20251118` | A4X and C4A | May 15, 2027 | View notes  
`common-ubuntu-2404-amd64-nvidia-595-slurm-2605-v20260903` | A4, A3 Ultra, and N2 | September 15, 2027 | View notes  
`common-ubuntu-2204-amd64-nvidia-580-slurm-2505-v20251113` | A4, A3 Ultra, and N2 | May 15, 2027 | View notes  
`common-ubuntu-2204-amd64-nvidia-570-slurm-2505-v20250918` | A4, A3 Ultra, and N2 | May 15, 2027 | View notes  
`a3-h100-ubuntu-2204-amd64-nvidia-580-slurm-2505-v20260805` | A3 Mega | May 15, 2027 | View notes  
`a3m-ubuntu-2204-amd64-nvidia-580-slurm-2505-v20260714` | A3 Mega | May 15, 2027 | View notes  
`a3m-ubuntu-2204-amd64-nvidia-570-slurm-2505-v20251114` | A3 Mega | May 15, 2027 | View notes  
`a3m-ubuntu-2204-amd64-nvidia-570-slurm-2505-v20250918` | A3 Mega | May 15, 2027 | View notes  
  
## Image families for A4X and C4A

The following sections list the patch release notes for the image families that support the A4X and C4A machine series.

### `a4x-ubuntu-2404-arm64-nvidia-595-slurm-2605-v20260903`

The following list details the patch release history for the `a4x-ubuntu-2404-arm64-nvidia-595-slurm-2605-v20260903` image family:

  * **v01 (September 15, 2026)** :

    * Upgraded to NVIDIA driver version 595 and Slurm 26.05.



### `a4x-ubuntu-2404-arm64-nvidia-580-slurm-2505-v20251118`

The following list details the patch release history for the `a4x-ubuntu-2404-arm64-nvidia-580-slurm-2505-v20251118` image family:

  * **v09 (August 27, 2026)** :

    * Updated the Slurm `sbcast` tool to address a vulnerability (CVE-2026-65107).
  * **v08 (May 20, 2026)** :

    * Updated the `gcsfuse_spank.so` plugin to include recent [slurm-gcp fixes](https://github.com/GoogleCloudPlatform/slurm-gcp/commit/bd4852d56b82399276cbd24a15a48bf9ab970149).
  * **v07 (April 3, 2026)** :

    * Updated `libssl3` and `libtasn1-6` to address vulnerabilities (CVE-2025-15467, CVE-2021-46848, CVE-2025-13151).

    * Removed the unused Node.js packages `minimatch` and `flatted` to address vulnerabilities (CVE-2026-27904, CVE-2026-32141).

  * **v06 (March 3, 2026)** :

    * Removed the unused `munge` package to address a vulnerability (CVE-2026-25506).
  * **v05 (February 13, 2026)** :

    * Disabled Data Center GPU Manager (DCGM) hang detection to resolve a known issue.



## Image families for A4, A3 Ultra, and N2

The following sections list the patch release notes for the common Ubuntu image families that support the A4, A3 Ultra, and N2 machine series.

### `common-ubuntu-2404-amd64-nvidia-595-slurm-2605-v20260903`

The following list details the patch release history for the `common-ubuntu-2404-amd64-nvidia-595-slurm-2605-v20260903` image family:

  * **v02 (September 15, 2026)** :

    * Upgraded to Ubuntu 24.04 LTS, NVIDIA driver version 595, and Slurm 26.05.



### `common-ubuntu-2204-amd64-nvidia-580-slurm-2505-v20251113`

The following list details the patch release history for the `common-ubuntu-2204-amd64-nvidia-580-slurm-2505-v20251113` image family:

  * **v07 (August 27, 2026)** :

    * Updated the Slurm `sbcast` tool to address a vulnerability (CVE-2026-65107).
  * **v06 (May 20, 2026)** :

    * Updated the `gcsfuse_spank.so` plugin to include recent [slurm-gcp fixes](https://github.com/GoogleCloudPlatform/slurm-gcp/commit/bd4852d56b82399276cbd24a15a48bf9ab970149).
  * **v05 (April 3, 2026)** :

    * Updated `libssl3` and `libtasn1-6` to address vulnerabilities (CVE-2025-15467, CVE-2021-46848, CVE-2025-13151).

    * Removed the unused Node.js packages `minimatch` and `flatted` to address vulnerabilities (CVE-2026-27904, CVE-2026-32141).

  * **v04 (March 3, 2026)** :

    * Removed the unused `munge` package to address a vulnerability (CVE-2026-25506).
  * **v03 (February 13, 2026)** :

    * Disabled Data Center GPU Manager (DCGM) hang detection to resolve a known issue.



### `common-ubuntu-2204-amd64-nvidia-570-slurm-2505-v20250918`

The following list details the patch release history for the `common-ubuntu-2204-amd64-nvidia-570-slurm-2505-v20250918` image family:

  * **v04 (April 3, 2026)** :

    * Updated `libssl3` and `libtasn1-6` to address vulnerabilities (CVE-2025-15467, CVE-2021-46848, CVE-2025-13151).

    * Removed the unused Node.js packages `minimatch` and `flatted` to address vulnerabilities (CVE-2026-27904, CVE-2026-32141).

  * **v03 (March 3, 2026)** :

    * Removed the unused `munge` package to address a vulnerability (CVE-2026-25506).
  * **v02 (February 10, 2026)** :

    * Upgraded `open-vm-tools` to version `2:12.3.5-3~ubuntu0.22.04.3` to address a vulnerability (CVE-2025-41244).



## Image families for A3 Mega

The following sections list the patch release notes for the image families that support the A3 Mega machine series.

### `a3-h100-ubuntu-2204-amd64-nvidia-580-slurm-2505-v20260805`

The following list details the patch release history for the `a3-h100-ubuntu-2204-amd64-nvidia-580-slurm-2505-v20260805` image family:

  * **v01 (August 27, 2026)** :

    * Updated the Slurm `sbcast` tool to address a vulnerability (CVE-2026-65107).

    * Pre-installed GPUDirect-TCPXO container images (`nccl-plugin` and `rxdm`).




### `a3m-ubuntu-2204-amd64-nvidia-580-slurm-2505-v20260714`

The following list details the patch release history for the `a3m-ubuntu-2204-amd64-nvidia-580-slurm-2505-v20260714` image family:

  * **v01 (August 27, 2026)** :

    * Updated the Slurm `sbcast` tool to address a vulnerability (CVE-2026-65107).
  * **v00 (July 14, 2026)** :

    * Upgraded to NVIDIA driver version 580 and CUDA 13.



### `a3m-ubuntu-2204-amd64-nvidia-570-slurm-2505-v20251114`

The following list details the patch release history for the `a3m-ubuntu-2204-amd64-nvidia-570-slurm-2505-v20251114` image family:

  * **v06 (May 20, 2026)** :

    * Updated the `gcsfuse_spank.so` plugin to include recent [slurm-gcp fixes](https://github.com/GoogleCloudPlatform/slurm-gcp/commit/bd4852d56b82399276cbd24a15a48bf9ab970149).
  * **v05 (April 3, 2026)** :

    * Updated `libssl3` and `libtasn1-6` to address vulnerabilities (CVE-2025-15467, CVE-2021-46848, CVE-2025-13151).

    * Removed the unused Node.js packages `minimatch` and `flatted` to address vulnerabilities (CVE-2026-27904, CVE-2026-32141).

  * **v04 (March 3, 2026)** :

    * Removed the unused `munge` package to address a vulnerability (CVE-2026-25506).
  * **v03 (February 13, 2026)** :

    * Disabled Data Center GPU Manager (DCGM) hang detection to resolve a known issue.



### `a3m-ubuntu-2204-amd64-nvidia-570-slurm-2505-v20250918`

The following list details the patch release history for the `a3m-ubuntu-2204-amd64-nvidia-570-slurm-2505-v20250918` image family:

  * **v04 (April 3, 2026)** :

    * Updated `libssl3` and `libtasn1-6` to address vulnerabilities (CVE-2025-15467, CVE-2021-46848, CVE-2025-13151).

    * Removed the unused Node.js packages `minimatch` and `flatted` to address vulnerabilities (CVE-2026-27904, CVE-2026-32141).

  * **v03 (March 3, 2026)** :

    * Removed the unused `munge` package to address a vulnerability (CVE-2026-25506).
  * **v02 (February 10, 2026)** :

    * Upgraded `open-vm-tools` to version `2:12.3.5-3~ubuntu0.22.04.3` to address a vulnerability (CVE-2025-41244).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
