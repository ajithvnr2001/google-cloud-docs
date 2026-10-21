---
url: https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies/
title: Install dependencies \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:43:44.062896+00:00
---

# Install dependencies  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Install dependencies Stay organized with collections  Save and categorize content based on your preferences. 

To create a cluster using the Cluster Toolkit, you can use either Cloud Shell, or a workstation that is running Linux or macOS.

If you use Cloud Shell, then you don't need to install the dependencies in this document. Proceed to the instructions in [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).

If you want to work from a Linux or macOS client or workstation, then complete the steps in this document.

## Install Cluster Toolkit dependencies

**Important:** If you use [Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell), the Cluster Toolkit dependencies are already pre-installed. If you are using an alternative to Cloud Shell, such as using a workstation that is running Linux or macOS, you must follow the instructions in [Install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies).

###  Linux 

  1. Install the Google Cloud CLI, see [Installing the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  2. Install Terraform version 1.12.2 or later. For instructions, see [Download Terraform](https://www.terraform.io/downloads).

**Note:** Terraform versions 1.6.0 and later (including version 1.12.2) are distributed under the [Business Source License (BSL)](https://www.hashicorp.com/en/bsl) and have usage restrictions. Versions 1.5.7 and earlier were distributed as open source under the Mozilla Public License (MPL) and don't have these restrictions. Before you upgrade to Terraform version 1.6.0 or later, you must ensure that you can adhere to the [HashiCorp Terraform License](https://www.hashicorp.com/en/license-faq) terms.
  3. Install Packer version 1.15.3 or later. For instructions, see [Download Packer](https://www.packer.io/downloads).

  4. Install a [supported Go release](https://go.dev/doc/devel/release#policy). For install instructions, see [Download and install Go](https://go.dev/doc/install).

Also set up a `GOPATH` by running the following command:
         
         export PATH=$PATH:$(go env GOPATH)/bin

  5. Install Git. For instructions, see [Install Git](https://github.com/git-guides/install-git).

  6. Check that a Python 3 release of `pip` is installed by running `pip3`. If `pip3` is not available, review the [Python documentation](https://docs.python.org/3/installing/index.html).

  7. Install Make.

###  CentOS/RHEL 
         
         yum install -y make

###  Debian/Ubuntu 
         
         apt-get -y install make




###  macOS 

  1. Install the Google Cloud CLI, see [Installing the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  2. Install Terraform version 1.12.2 or later. For instructions, see [Download Terraform](https://www.terraform.io/downloads).

**Note:** Terraform versions 1.6.0 and later (including version 1.12.2) are distributed under the [Business Source License (BSL)](https://www.hashicorp.com/en/bsl) and have usage restrictions. Versions 1.5.7 and earlier were distributed as open source under the Mozilla Public License (MPL) and don't have these restrictions. Before you upgrade to Terraform version 1.6.0 or later, you must ensure that you can adhere to the [HashiCorp Terraform License](https://www.hashicorp.com/en/license-faq) terms.
  3. Install Packer version 1.15.3 or later. For instructions, see [Download Packer](https://www.packer.io/downloads).

  4. Install a [supported Go release](https://go.dev/doc/devel/release#policy). For install instructions, see [Download and install Go](https://go.dev/doc/install).

Also set up a `GOPATH` by running the following command:
         
         export PATH=$PATH:$(go env GOPATH)/bin

  5. Install Git. For instructions, see [Install Git](https://github.com/git-guides/install-git).

  6. Check that a Python 3 release of `pip` is installed by running `pip3`. If `pip3` is not available, [download and install](https://www.python.org/downloads/) the package.

  7. Install Make. On macOS, `make` is packaged with the Xcode command line developer tools. To install Xcode, run the following command:
         
         xcode-select --install




## What's next

  * Set up [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * Review [Deploy a cluster with blueprints](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/deploy-cluster-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
