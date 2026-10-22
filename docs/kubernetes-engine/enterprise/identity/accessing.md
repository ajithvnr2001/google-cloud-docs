---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/accessing/
title: Choose an access method to log in to fleet member clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:28.771575+00:00
---

# Choose an access method to log in to fleet member clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/accessing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Choose an access method to log in to fleet member clusters Stay organized with collections  Save and categorize content based on your preferences. 

This document is for developers and other users who have identities from third-party providers and need to access fleet member clusters from the command line.

## Before you begin

  * Log in from the command line

If you want to use one of the command line login options, do the following:

    1. Ensure that you have the following command line tools installed:

       * The latest version of the Google Cloud CLI, which includes `gcloud`, the command line tool for interacting with Google Cloud. If you need to install the Google Cloud CLI, see the [installation guide](https://docs.cloud.google.com/sdk/docs/install).
       * `kubectl` for running commands against Kubernetes clusters. If you need to install `kubectl`, see the [installation guide](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl).
    2. Run the following commands to install or update the `anthos-auth` component:
           
           gcloud components update
           gcloud components install anthos-auth

    3. Verify that the component was installed successfully by running the following command:
           
           gcloud anthos auth version

If a version is returned, your installation was successful.

  * Log in from the Google Cloud console

For OIDC and AzureAD providers only, you can also log in to clusters from the Google Cloud console without a configuration file or FQDN. For more information, see [Work with clusters from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console).




## Access methods to log in to clusters

To log in to your configured clusters, use one of the following access methods:

  * **Log in from the command line with FQDN access** : If you need to log in to your clusters using a fully qualified domain name, see [FQDN access](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/authenticate-fqdn-access).
  * **Log in from the command line with file-based access** : If you need to log in to your clusters with a configuration file, see [file-based access](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/authenticate-file-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
