---
url: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/install/
title: Install or upgrade Cloud Storage FUSE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:54.849039+00:00
---

# Install or upgrade Cloud Storage FUSE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/install/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Install or upgrade Cloud Storage FUSE Stay organized with collections  Save and categorize content based on your preferences. 

To mount Cloud Storage buckets as local file systems, you first install [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview) on your machine. This document describes how to install Cloud Storage FUSE by using prebuilt Linux binaries or the latest source code, and how to upgrade to the latest version. For information on which frameworks, operating systems, and architectures Cloud Storage FUSE supports, see [Frameworks, operating systems, and architectures](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview#frameworks-os-architectures).

## Install Cloud Storage FUSE by using prebuilt Linux binaries

To install or upgrade Cloud Storage FUSE by using prebuilt Linux libraries, complete the following instructions.

### Configure package manager

### Ubuntu/Debian

If your distribution supports the signed-by option, complete the following instructions:

  1. Install the required packages:
         
         sudo apt-get update
         sudo apt-get install -y curl lsb-release

  2. Add the Cloud Storage FUSE distribution URL as a package source:
         
         export GCSFUSE_REPO=gcsfuse-`lsb_release -c -s`
         echo "deb [signed-by=/usr/share/keyrings/cloud.google.asc] https://packages.cloud.google.com/apt $GCSFUSE_REPO main" | sudo tee /etc/apt/sources.list.d/gcsfuse.list

  3. Import the Google Cloud public key:
         
         curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo tee /usr/share/keyrings/cloud.google.asc




If your distribution is outdated and doesn't support the signed-by option, complete the following instructions:

  1. Add the Cloud Storage FUSE distribution URL as a package source:
         
         export GCSFUSE_REPO=gcsfuse-`lsb_release -c -s`
         echo "deb https://packages.cloud.google.com/apt $GCSFUSE_REPO main" | sudo tee /etc/apt/sources.list.d/gcsfuse.list

  2. Import the Google Cloud public key:
         
         curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -




### CentOS/Red Hat/Rocky Linux

If you're using the CentOS, Red Hat, or Rocky Linux operating system, complete the following instructions:

  1. Configure the Cloud Storage FUSE repository and its associated public key:
         
         sudo tee /etc/yum.repos.d/gcsfuse.repo > /dev/null <<EOF
         [gcsfuse]
         name=gcsfuse (packages.cloud.google.com)
         baseurl=https://packages.cloud.google.com/yum/repos/gcsfuse-el7-x86_64
         enabled=1
         gpgcheck=1
         repo_gpgcheck=0
         gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
               https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
         EOF

  2. If you haven't yet, install [FUSE](https://github.com/libfuse/libfuse) by using the [`YUM` Linux package manager](https://www.redhat.com/sysadmin/how-manage-packages):
         
         sudo yum install fuse




### SUSE Linux

If you're using the SUSE Linux operating system, complete the following instructions:

  1. Configure the Cloud Storage FUSE repository and its associated public key:
         
         sudo tee /etc/zypp/repos.d/gcsfuse.repo > /dev/null <<EOF
         [gcsfuse]
         name=gcsfuse (packages.cloud.google.com)
         baseurl=https://packages.cloud.google.com/yum/repos/gcsfuse-el7-x86_64
         enabled=1
         gpgcheck=1
         repo_gpgcheck=0
         gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
               https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
         EOF

  2. If you haven't yet, install [FUSE](https://github.com/libfuse/libfuse) by using the [`ZYPPER` Linux package manager](https://documentation.suse.com/smart/systems-management/html/concept-zypper/index.html):
         
         sudo zypper install fuse




### Install or upgrade Cloud Storage FUSE

### Ubuntu/Debian

Update the list of available packages and install Cloud Storage FUSE:
    
    
    sudo apt-get update
    sudo apt-get install gcsfuse

### CentOS/Red Hat/Rocky Linux

If you're using the CentOS, Red Hat, or Rocky Linux operating system, run the following commands:

Install Cloud Storage FUSE:
    
    
    sudo yum install gcsfuse

Be sure to answer "yes" to any questions about adding the GPG signing key.

### SUSE Linux

If you're using the SUSE Linux operating system, run the following commands:

Install Cloud Storage FUSE:
    
    
    sudo zypper install gcsfuse

Be sure to answer "yes" to any questions about adding the GPG signing key.

Alternatively, you can download the latest prebuilt package of Cloud Storage FUSE directly from [GitHub](https://github.com/GoogleCloudPlatform/gcsfuse/releases).

To upgrade to the latest version of Cloud Storage FUSE using prebuilt Linux binaries, use the following instructions:

### Ubuntu/Debian

If you're using the Ubuntu or Debian Linux operating system, use the following commands to upgrade to the latest version of Cloud Storage FUSE:
    
    
    sudo apt-get update
    sudo apt-get install --only-upgrade gcsfuse

### CentOS/Red Hat/Rocky Linux

If you're using the CentOS, Red Hat, or Rocky Linux operating system, use the following commands to upgrade to the latest version of Cloud Storage FUSE:
    
    
    sudo apt-get update
    sudo yum -y upgrade gcsfuse

### SUSE Linux

If you're using the SUSE Linux operating system, use the following commands to upgrade to the latest version of Cloud Storage FUSE:
    
    
    sudo zypper refresh
    sudo zypper -n update gcsfuse

## Install or upgrade Cloud Storage FUSE by building the latest source code

To install or upgrade Cloud Storage FUSE by building the [latest source code from GitHub](https://github.com/GoogleCloudPlatform/gcsfuse/tree/master), complete the following instructions:

  1. If you haven't yet, install `fuse`, `git`, and `go` (see [go.mod](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/go.mod) for the latest version of `go`).

  2. Install Cloud Storage FUSE by using the `go install` command:
         
         go install github.com/googlecloudplatform/gcsfuse/v3@master

If successful, a binary named `gcsfuse` is installed to `$GOPATH/bin`. `GOPATH` is an environment variable that's used to find the root of your `go` workspace.




Alternatively, you can also install Cloud Storage FUSE by cloning the git repository to your local file system:

  1. Clone the Cloud Storage FUSE repository:
         
         git clone https://github.com/GoogleCloudPlatform/gcsfuse.git

  2. Switch your current working directory to the `gcsfuse` folder containing the Cloud Storage FUSE repository:
         
         cd gcsfuse

  3. Install Cloud Storage FUSE by using the `go install` command:
         
         go install .

If successful, a binary named `gcsfuse` is installed to `$GOPATH/bin`.




To upgrade to the latest version of Cloud Storage FUSE using source code, re-run the install instructions.

## What's next

  * Learn how to [mount buckets using Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcsfuse-mount).
  * Learn how to [troubleshoot issues installing Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/troubleshooting-cloud-storage-fuse).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
