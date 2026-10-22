---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-pull/
title: gdcloud artifacts pull \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:14.412560+00:00
---

# gdcloud artifacts pull  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-artifacts-pull/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud artifacts pull Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud artifacts pull - Pull OCI packages from a registry.

## SYNOPSIS
    
    
    gdcloud artifacts pull SOURCE DESTINATION [flags]
    

### EXAMPLES
    
    
    To pull OCI packages from a registry, run:
    
                gdcloud artifacts pull SOURCE DESTINATION
    
            To pull a single manifest repository from the registry, run:
    
                gdcloud artifacts pull SOURCE DESTINATION --single-manifest-repo
    
            To pull OCI packages from a registry without adhering to TLS protocols, run:
    
                gdcloud artifacts pull SOURCE DESTINATION --insecure
    
                The SOURCE is a reference of a remote OCI image. For example, gcr.io/cloud-marketplace/google/nginx:1.25.
                The DESTINATION path specified must point to an empty directory.
                This command writes the extracted image to the output path specified in SOURCE. This output path must point to an empty directory.
    

### OPTIONAL FLAGS
    
    
          --insecure               Allow pulling from the registry, and establishing a connection to the server, even for server connections otherwise considered insecure.
          --single-manifest-repo   Pull a single-manifest repository from the registry, where the source is the reference for manifest instead of the image index.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
