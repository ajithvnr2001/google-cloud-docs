---
url: https://docs.cloud.google.com/artifact-registry/docs/troubleshoot-remote/
title: Troubleshoot remote repositories \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:28.994127+00:00
---

# Troubleshoot remote repositories  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/troubleshoot-remote/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Troubleshoot remote repositories Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with Artifact Registry remote repositories.

For information on resolving issues with Artifact Registry standard repositories see [General troubleshooting](https://docs.cloud.google.com/artifact-registry/docs/troubleshoot).

## Errors when requesting a package

If an artifact isn't cached in your remote repository, several errors can be returned if there are issues with the upstream repository.

### 404 error

The following issue occurs when the requested artifact doesn't exist in the upstream repository.
    
    
    Received invalid response from external repository; url=URL.
    

To resolve this issue, make sure that the artifact name and version are correct, and are present in the upstream repository.

### 429 error

The following issue occurs when the upstream read limit is exceeded.
    
    
    Resource has been exhausted (e.g. check quota).
    

To resolve this issue, wait for a minute and try again. For more information on upstream read limits, see [Remote repository limits](https://docs.cloud.google.com/artifact-registry/quotas#remote_repository_limits).

### 502 (bad gateway) error

The following issue occurs when the upstream repository responds with an error code. The error message details differ depending on the upstream repository error.
    
    
    Received invalid http status code httpStatusCode from external repository; url=URL.
    
    
    
    Received invalid redirect URL lastRequestedURL from external repository.
    
    
    
    External repository returned unexpected EOF for url=URL.
    
    
    
    Fetch was denied by external repository's robots.txt; url=URL
    
    
    
    Received invalid redirect URL from external repository; url=URL. If the failures persist, your remote repository upstream URI may be misconfigured.
    
    
    
    Received invalid response from external repository; url=URL.
    

To resolve this issue, investigate the cause of the upstream repository error.

### 504 (gateway timeout)

The following issue occurs when the upstream repository is offline or cannot be contacted. The error message details vary depending on when the timeout occurs.
    
    
    Timeout while calling external repository; url=URL.
    
    
    
    Timeout before connecting to external repository; url=URL
    

To resolve this issue, ensure you have the correct upstream URI, or if it is correct, investigate if the upstream source is experiencing an outage.

## OS packages

This section lists remote repository errors that you might encounter for OS packages and provides suggestions for how to fix each of them.

For information resolving issues with standard repositories for OS packages, see [Troubleshoot OS packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/troubleshoot).

### `Can not load` error

The following issue occurs when installing a package using the version or architecture. For example, if you try to install `nano-2.3.1-10.el7.x86_64.rpm`.
    
    
    Can not load RPM file: nano-2.3.1-10.el7.x86_64.rpm
    Could not open: nano-2.3.1-10.el7.x86_64.rpm
    

To resolve this issue, request the package using only the name of the package. For example, install `nano` instead of `nano-2.3.1-10.el7.x86_64.rpm`.

### Yum prioritization

The following issue occurs when packages aren't installed through the remote repository when expected, or are installed when the remote is intended to be used as a backup.

By default, Yum determines which repository to prioritize based on the name of the repository. It will try to install packages from the repository name first in alphabetical order; if it doesn't find the package in that repository, it will continue trying each repository down the alphabet.

The default repository is often called `[base]` or `[baseos]`. If the remote repository is named starting with a numerical character or comes earlier in the alphabet than `[base]`, it will be tried before the default. If the remote repository is named after `[base]` in the alphabet, it will be tried after the default.

To resolve this issue, you can rename your repository, or configure your `yum.conf` file using the flags described in the [`yum.conf` man page](https://linux.die.net/man/5/yum.conf).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
