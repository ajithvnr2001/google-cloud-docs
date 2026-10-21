---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-service-accounts-keys-create/
title: gdcloud iam service-accounts keys create \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:00:51.055041+00:00
---

# gdcloud iam service-accounts keys create  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-service-accounts-keys-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud iam service-accounts keys create Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud iam service-accounts keys create - Create an application default credentials JSON file which contains a private key for a service account.

## SYNOPSIS
    
    
    gdcloud iam service-accounts keys create FILE_NAME [flags]
    

## DESCRIPTION

Create a pair of public/private keys for a project's service account and put the private key into a JSON file. The file can be used to exchange for an STS token from AIS.

### EXAMPLES
    
    
      To create an application default credentials JSON file "/tmp/my-key.json" for service account "psa-test" in project "iam-test" using cacert file "/tmp/ca.crt", run:
    
        gdcloud iam service-accounts keys create /tmp/my-key.json --iam-account=psa-test --project=iam-test --ca-cert-path=/tmp/ca.crt
    
    

### REQUIRED FLAGS
    
    
          --iam-account string   Project's service account to create the key for. The flag is required to run the command.
    

### OPTIONAL FLAGS
    
    
          --ca-cert-path string   CA cert path to verify the authentication endpoint. If omitted, then the system cert chain will be used.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
