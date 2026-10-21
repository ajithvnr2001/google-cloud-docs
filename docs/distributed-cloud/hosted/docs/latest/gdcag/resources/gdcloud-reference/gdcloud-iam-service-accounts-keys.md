---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-service-accounts-keys/
title: gdcloud iam service-accounts keys \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:57:07.944096+00:00
---

# gdcloud iam service-accounts keys  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-service-accounts-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud iam service-accounts keys Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud iam service-accounts keys - Manage keys for a project's service account.

## SYNOPSIS
    
    
    gdcloud iam service-accounts keys COMMAND [flags]
    

## DESCRIPTION

Create, list, or delete credentials for a project's service account. You must have the "project-iam-admin" role in a project to manage the service accounts' keys for that project.

### EXAMPLES
    
    
      To create an application default credentials JSON file "/tmp/my-key.json" for service account "psa-test" in project "iam-test" using cacert file "/tmp/ca.crt", run:
    
        gdcloud iam service-accounts keys create /tmp/my-key.json --iam-account=psa-test --project=iam-test --ca-cert-path=/tmp/ca.crt
    
      To list all the public keys for service account "psa-test" in project "iam-test", run:
    
        gdcloud iam service-accounts keys list --iam-account=psa-test --project=iam-test
    
      To delete a public key with ID "ab98fa9a-dae0-401f" from service account "psa-test" in project "iam-test", run:
    
        gdcloud iam service-accounts keys delete ab98fa9a-dae0-401f --iam-account=psa-test --project=iam-test
    
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--help`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

### COMMANDS

`COMMAND` is one of the following:
    
    
    create
        Create an application default credentials JSON file which contains a private key for a service account.
    delete
        Delete a public key from a service account.
    list
        List all the public keys for a service account.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
