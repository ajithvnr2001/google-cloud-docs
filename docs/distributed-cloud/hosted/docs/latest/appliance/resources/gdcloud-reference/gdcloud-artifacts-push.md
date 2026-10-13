---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-artifacts-push/
title: gdcloud artifacts push \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:17.968223+00:00
---

# gdcloud artifacts push  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-artifacts-push/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud artifacts push Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud artifacts push - Push OCI packages to a registry.

## SYNOPSIS
    
    
    gdcloud artifacts push SOURCE DESTINATION [flags]
    

### EXAMPLES
    
    
    To push a OCI packages to a registry, run:
    
                gdcloud artifacts push SOURCE DESTINATION
    
            To push a single manifest of the repository to the registry, run:
    
                gdcloud artifacts push SOURCE DESTINATION --single-manifest-repo
    
            To push OCI packages to a registry without adhering to TLS protocols, run:
    
                gdcloud artifacts push SOURCE DESTINATION --insecure
    
            The SOURCE path must point to a directory containing the OCI bundle.
            The DESTINATION is a reference of a remote OCI image. For example, gcr.io/cloud-marketplace/google/nginx:1.25.
            This command writes the extracted image to the output path specified in SOURCE. This output path must point to an empty directory.
    

### OPTIONAL FLAGS
    
    
          --ca-cert-path string    Absolute file path to the user-provided CA certificate file that is used to push a manifest over a HTTPS connection.
          --insecure               Allow pushing to the registry, and establish a connection to the server, even for server connections otherwise considered insecure.
          --single-manifest-repo   Tag and push the single manifest of the repository, as opposed to the image index, to the registry.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
