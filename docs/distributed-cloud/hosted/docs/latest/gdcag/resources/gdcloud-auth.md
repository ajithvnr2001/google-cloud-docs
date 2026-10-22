---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth/
title: The gdcloud CLI authentication \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:02.568267+00:00
---

# The gdcloud CLI authentication  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  The gdcloud CLI authentication Stay organized with collections  Save and categorize content based on your preferences. 

This page details how to authenticate with your configured identity provider and get a kubeconfig file for your user identity and cluster.

## Before you begin

Before you can authenticate with your identity provider and generate a kubeconfig file, ensure you have completed the following:

  * Run the `gdcloud init` command. For more information, see the [Initialize gdcloud CLI default configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install#init-default-config) section.

  * Install the authentication plugin, which is required to use a generated kubeconfig file:
        
        gdcloud components install gdcloud-k8s-auth-plugin
        




## Sign in with configured identity provider

Sign in with the configured identity provider:
    
    
    gdcloud auth login
    

Follow the instructions to authenticate with your identity provider.

Consider the following when using the `gdcloud auth login` command:

  * It authenticates with the current organization. Run the `gdcloud auth login` command after switching organizations.
  * It requires that the certificate authority (CA) certificate for the login config is installed in the system's trusted certificates store. For more information, see [Fetch GDC trust bundles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/fetch-trust-bundles).
  * It requires a browser to exist on the device. Use the `--no-browser` flag to log in with a second device.



## Get a kubeconfig file

After authenticating with the identity provider, get a `kubeconfig` file with your user identity:
    
    
    gdcloud clusters get-credentials CLUSTER_NAME
    

This creates or updates the kubeconfig file in the default path `${HOME}/.kube/config` with the authenticated user and cluster.

Consider the following when generating or updating your kubeconfig file:

  * Specify the desired path in the `KUBECONFIG` environment path to save it to a different path.
  * The kubeconfig is a long-lived file, however the token authenticating the user is short-lived. If a kubeconfig file stops working, run the `gdcloud auth login` command to authenticate again.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
