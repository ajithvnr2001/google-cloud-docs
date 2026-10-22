---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/gdcloud/
title: Use the gdcloud CLI \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:43.837266+00:00
---

# Use the gdcloud CLI  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/gdcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Use the gdcloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

The gdcloud CLI is a set of tools to create and manage Google Distributed Cloud (GDC) air-gapped resources. Use these tools to perform common tasks from the command line or through scripts and automation. The gdcloud CLI lets you bootstrap infrastructure, manage authentication, and customize local configurations.

This document is for all audience groups that need to set up GDC's dedicated CLI to manage their air-gapped hardware and software workflows. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

  * Confirm that you have access to the GDC console and note your organization's URL. For more information, see [GDC console access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/console).

  * Confirm that you have a Certificate Authority (CA) certificate that is installed in your system's trusted certificates store. For more information, see [Fetch GDC trust bundles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/fetch-trust-bundles).

  * Verify that you have an organization network policy that allows traffic from a specific CIDR outside your organization to the artifact registry. For example, configure service name `all` in the `OrganizationNetworkPolicy` resource. For more information, see [Create organization network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag//platform/pa-user/org-network-policy).

  * Confirm that you have a browser installed on your device.




## Set up the gdcloud CLI

To set up the gdcloud CLI, complete the following:

  1. Open the GDC console by inputting your organization's global or zonal URL in your browser.

  2. From the home page, select **Download CLI Bundle**.

  3. Select the Linux platform and the gdcloud CLI bundle version that corresponds with your GDC environment.

When choosing non-Linux platforms, the configuration steps might vary slightly. Also be aware that some non-Linux gdcloud CLI bundles only provide a subset of gdcloud commands. For more information, see [Available gdcloud CLI bundles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview#cli-support).

  4. Click **Download**.

  5. From your device, navigate to the `Downloads` folder:
         
         cd ~/Downloads
         

  6. Extract the contents of the gdcloud CLI bundle:
         
         tar -xf ./gdcloud_cli.tar.gz
         

  7. Add the gdcloud CLI bundle to your path:
         
         eval echo 'export GDCLOUD_PATH=$(pwd)/google-distributed-cloud-hosted-cli' >> ~/.bashrc
         echo 'export PATH="$GDCLOUD_PATH/bin:$PATH"' >> ~/.bashrc
         source ~/.bashrc
         

  8. Confirm the gdcloud CLI is installed correctly:
         
         gdcloud version
         

The output is similar to the following:
         
         gdcloud version: 1.15.0-gdch.380608
         

  9. Initialize the gdcloud CLI:
         
         gdcloud init
         

  10. Provide the two prompted properties to complete the initialization:

     * `organization_console_url`: the URL to your current GDC organization's console. This URL can be global or zonal. For example, `https://console.org-1.google.gdch.test/`.

     * `project`: the name of your GDC project. If you don't have an existing project, use `default`.

To update your gdcloud CLI configurations after initialization, see [Manage gdcloud CLI configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-manage-configurations).

  11. Install the `gdcloud-k8s-auth-plugin` component:
         
         gdcloud components install gdcloud-k8s-auth-plugin
         

  12. Authenticate with the gdcloud CLI to sign in:
         
         gdcloud auth login
         

You're redirected to the browser to choose your identity and sign in.

  13. Confirm your gdcloud CLI setup is connected to your GDC environment:
         
         gdcloud compute images list
         

The output is similar to the following:
         
         METADATA.NAME               METADATA.NAMESPACE SPEC.OPERATINGSYSTEM.NAME SPEC.MINIMUMDISKSIZE
         rocky-8-v20250809-gdch      vm-system          rocky-linux-8             12G
         ubuntu-20.04-v20250809-gdch vm-system          ubuntu-2004               12G
         ubuntu-22.04-v20250809-gdch vm-system          ubuntu-2204               12G
         ubuntu-24.04-v20250809-gdch vm-system          ubuntu-2404               12G
         




## What's next

  * [gdcloud CLI overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview)
  * [gdcloud CLI authentication](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth)
  * [Manage gdcloud CLI properties](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-manage-properties)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
