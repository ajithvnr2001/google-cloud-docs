---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-auth-activate-service-account/
title: gdcloud auth activate-service-account \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:35.205222+00:00
---

# gdcloud auth activate-service-account  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-auth-activate-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud auth activate-service-account Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud auth activate-service-account - Authorize access to GDC air-gapped with a service account.

## SYNOPSIS
    
    
    gdcloud auth activate-service-account [flags]
    

## DESCRIPTION

Authorize access to GDC air-gapped with a service account. To allow gdcloud to make requests using service account credentials, use this command to import these credentials from a file that contains a private authorization key, and activate them for use in gdcloud. The "gdcloud auth activate-service-account" serves the same function as the "gdcloud auth login" command, but uses a service account rather than the user credentials.

### EXAMPLES
    
    
    To authorize gdcloud to access GDC air-gapped using an existing service account, run:
    
       gdcloud auth activate-service-account --key-file=/path/key.json
    

### REQUIRED FLAGS
    
    
          --key-file string   Path to the private key file.
    

### OPTIONAL FLAGS
    
    
          --login-config-cert string   (Optional) Absolute file path to the CA certificate file to be used for fetching login-config over HTTPS connection.
          --skip-kubeconfig-update     (Optional) Skip updating the kubeconfig after login.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
