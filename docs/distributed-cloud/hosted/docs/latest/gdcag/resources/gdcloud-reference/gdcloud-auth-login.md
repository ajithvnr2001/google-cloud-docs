---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-auth-login/
title: gdcloud auth login \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:41.231203+00:00
---

# gdcloud auth login  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-auth-login/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud auth login Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud auth login - Authorize the gdcloud CLI to sign in with the configured identity provider.

## SYNOPSIS
    
    
    gdcloud auth login [flags]
    

## DESCRIPTION

Authorize the gdcloud CLI to sign in with the configured identity provider. The command authenticates with the current organization. Run the command again after switching organizations. It requires that the certificate authority (CA) certificate for the login config is installed in the trusted certificates store. If the CA certificate is not installed, use the --login-config-cert flag to specify the path to find the CA certificate. It requires a browser to exist on the device.

### EXAMPLES
    
    
    To sign in with the configured identity provider, run:
    
        gdcloud auth login
    

### OPTIONAL FLAGS
    
    
          --login-config-cert string   (Optional) Absolute file path to the CA certificate file to be used for fetching login-config over HTTPS connection.
          --no-browser                 (Optional) Use this flag to authenticate the gdcloud CLI on a machine without a web browser.
          --skip-kubeconfig-update     (Optional) Skip updating the kubeconfig file for management API servers.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
