---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-requirements-for-centos/
title: Perform a major upgrade using installer for CentOS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:55.786881+00:00
---

# Perform a major upgrade using installer for CentOS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-requirements-for-centos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Perform a major upgrade using installer for CentOS 

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to perform a major upgrade for an existing Remote Agent using the installer for CentOs 7.9 or later.

This procedure involves installing and configuring prerequisite packages before executing the upgrade script.

For more information on how to install an agent on a new deployment, see [ Create an agent using installer on CentOS](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/create-agent-with-installer-on-centos).

**Note** : To install all the packages, you must have superuser privileges. However, to ensure some dependencies remain accessible to non-root users, don't change the root user's `umask` from the default value of `0022`.

Install and configure required packages to upgrade Remote Agents with version 2.0.0 and higher.

**Important** : Keep the shell session open until you finish all steps.

To install and configure required packages, follow these steps:

  1. Run the following command to install Linux packages:
         
         yum install perl-core -y

  2. Run the following commands separately to install OpenSSL 3.0.7:
         
         cd /usr/local/src
             wget https://www.openssl.org/source/openssl-3.0.7.tar.gz
             tar -xf openssl-3.0.7.tar.gz
             cd openssl-3.0.7
             ./config --prefix=/usr/local/ssl --openssldir=/usr/local/ssl shared zlib
             make -j$((`nproc`+1))
             make install

  3. Run the following commands separately to configure OpenSSL environment variables:
         
         cd /etc/ld.so.conf.d/
             echo /usr/local/ssl/lib64 > openssl-3.0.7.conf
             ldconfig -v
             echo PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/ssl/bin" > /etc/environment
             source /etc/environment
             ln -sf  /usr/local/ssl/bin/openssl /usr/bin/openssl
             export LDFLAGS="$LDFLAGS -L/usr/local/ssl/lib64"
             export LD_LIBRARY_PATH=/usr/local/ssl/lib64




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
