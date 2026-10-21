---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts/
title: gdcloud artifacts \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:57.344325+00:00
---

# gdcloud artifacts  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud artifacts Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud artifacts - Create and manage artifacts in a GDC air-gapped environment.

## SYNOPSIS
    
    
    gdcloud artifacts GROUP | COMMAND [flags]
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--help`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

### GROUPS

`GROUP` is one of the following:
    
    
    apt
        Manage artifact apt packages.
    oci
        Command group for building OCI packages
    services
        Create and manage artifact services.
    vm-images
        Manage artifact VM images.
    

### COMMANDS

`COMMAND` is one of the following:
    
    
    extract
        Extract an image from OCI packages and write layers to files.
    list-versions
        List version tags for the root OCI image in a registry. Version tags can be found at gpc-system/gpc-oci.
    patch
        Patch and replace a full release package with a patch package.
    pull
        Pull OCI packages from a registry.
    push
        Push OCI packages to a registry.
    tree
        Print the tree-like structure of an OCI bundle.
    unpack
        Unpack a GDC air-gapped OCI bundle from a remote registry, or local directory, to a destination remote registry.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
