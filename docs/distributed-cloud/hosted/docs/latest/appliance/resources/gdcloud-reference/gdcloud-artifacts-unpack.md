---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-artifacts-unpack/
title: gdcloud artifacts unpack \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:20.965323+00:00
---

# gdcloud artifacts unpack  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-artifacts-unpack/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud artifacts unpack Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud artifacts unpack - Unpack a GDC air-gapped OCI bundle from a remote registry, or local directory, to a destination remote registry.

## SYNOPSIS
    
    
    gdcloud artifacts unpack OCI_BUNDLE DESTINATION [flags]
    

### EXAMPLES
    
    
    To unpack a GDC air-gapped OCI bundle to a destination registry, run:
    
                gdcloud artifacts unpack OCI_BUNDLE DESTINATION
    
            The OCI_BUNDLE is a path to a local directory containing an OCI bundle, or a reference to an OCI image in a remote registry.
            The DESTINATION is a reference to a remote registry where the unpacked OCI bundle exists when the unpack operation is complete.
    

### OPTIONAL FLAGS
    
    
          --all                           Tag all manifests in the OCI bundle.
          --ca-cert-path string           Absolute file path to the user-provided CA certificate file that is used to unpack the manifest over a HTTPS connection
          --insecure                      Allow unpacking an OCI image from registry, and establishing a connection to the server, even for server connections otherwise considered insecure.
          --output-manifest-path string   Output the manifest unpacked from an OCI image bundle.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
