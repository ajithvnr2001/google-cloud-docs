---
url: https://docs.cloud.google.com/kms/docs/crypto/
title: Including the Pyca cryptography library \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:30.749730+00:00
---

# Including the Pyca cryptography library  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/crypto/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Including the Pyca cryptography library Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to update the Google Cloud CLI to enable support for automatically wrapping keys for secure import into Cloud Key Management Service, by installing the [Pyca cryptography library](https://cryptography.io). Version 2.2.0 or higher adds support for the required `aes_key_wrap_with_padding` wrapping mechanism.

## Before you begin

  * [Install or upgrade the Google Cloud CLI](https://docs.cloud.google.com/sdk/install) to version 253.0.0 or higher.
  * Install the `pip` command if possible. `pip` is the platform-independent command-line interface to the [Python Package Index](https://pypi.python.org/pypi/pip). The package manager provided by your operating system may not provide version 2.2.0 or higher of the Pyca cryptographic library.

**Important:** If you specified your Python version with the [CLOUDSDK_PYTHON environment variable](https://cloud.google.com/sdk/gcloud/reference/topic/startup), ensure that same version is active when you install the Pyca cryptographic library.

## Installing and using pip

You can install and use `pip` on Linux, macOS, or Windows systems.

This command installs the library into your user environment, specifying the minimum version to install. To install system-wide, omit the `--user` flag. You may need to install `pip` as a privileged user.
    
    
    pip install --user "cryptography>=2.2.0"
    

After installing the Pyca cryptographic libraries, you must enable site packages so the gcloud CLI can use the libraries. 

## Installing on Linux using a package manager

Follow these instructions on Linux systems if you can't use the `pip` command.

### Debian or Ubuntu

If you use a system based on Debian or Ubuntu, you can install the Pyca cryptographic library using the `apt-get` command.

  1. Check the versions of the `python-cryptography` package available in the package database. Version 2.2.0 or higher is required.
         
         apt policy python-cryptography
         

  2. Install the package.
         
         sudo apt-get install python-cryptography
         

If necessary, specify the version to install.
         
         sudo apt-get install python-cryptography=version
         

**Note:** Use an `=` (equals sign) between the package name and version.



After installing the Pyca cryptographic libraries, you must enable site packages so the gcloud CLI can use the libraries. 

### Red Hat, CentOS, or SUSE

If your system uses RPMs for package management, you can install the Pyca crytographic library using the `yum` command.

  1. Check the versions of `python-cryptography` available in the package database. Version 2.2.0 or higher is required.
         
         yum --showduplicates list python2-cryptography
         

  2. Install the package.
         
         sudo yum install python2-cryptography
         

If necessary, specify the version to install.
         
         sudo yum install python2-cryptography-version
         

**Note:** Use a `-` (hyphen) between the package name and version.



After installing the Pyca cryptographic libraries, you must enable site packages so the gcloud CLI can use the libraries. 

## Enabling site packages

By default, the Google Cloud CLI ignores Python libraries installed on your local system. To allow the Google Cloud CLI to use the Pyca cryptographic library, you need to enable site packages.

To enable site packages, set the `CLOUDSDK_PYTHON_SITEPACKAGES` environment variable to `1`. With site packages enabled, the gcloud CLI can use extra libraries outside of the `google-cloud-sdk/lib` directory.

### Linux
    
    
    export CLOUDSDK_PYTHON_SITEPACKAGES=1
    

### macOS
    
    
    export CLOUDSDK_PYTHON_SITEPACKAGES=1
    

### Windows
    
    
    set CLOUDSDK_PYTHON_SITEPACKAGES=1
    

Enabling site packages may cause some gcloud CLI commands to fail. It is recommended that you disable site packages after importing your keys.

## Disabling site packages

After you finish importing keys, it is recommended that you disable site packages on systems where you use the gcloud CLI. To disable site packages, set `CLOUDSDK_PYTHON_SITEPACKAGES` to `0`.

### Linux
    
    
    export CLOUDSDK_PYTHON_SITEPACKAGES=0
    

### macOS
    
    
    export CLOUDSDK_PYTHON_SITEPACKAGES=0
    

### Windows
    
    
    set CLOUDSDK_PYTHON_SITEPACKAGES=0
    

[ Previous arrow_back  Quantum-safe key import  ](https://docs.cloud.google.com/kms/docs/quantum-safe-key-import)

[ Next Import a key version  arrow_forward  ](https://docs.cloud.google.com/kms/docs/importing-a-key)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
