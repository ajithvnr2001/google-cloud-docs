---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install/
title: Install the gdcloud CLI \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:19:46.262234+00:00
---

# Install the gdcloud CLI  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Install the gdcloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

To install and initialize the Distributed Cloud CLI, [download the CLI bundle](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and complete the following steps.

## Add gdcloud CLI bin directory to path

Google recommends adding the gdcloud CLI `bin` directory to your path.

When the `bin` directory is added to your path:

  * You won't have to specify the entire directory structure with each command.
  * Crucial gdcloud CLI components are installed in the `bin` directory that allow commands like `gdcloud components` to work correctly.

**Note:** The commands in the following sections assume the `google-distributed-cloud-hosted-cli` folder is in the current working directory.

Add the gdcloud CLI `bin` directory to your path:
    
    
    eval echo 'export GDCLOUD_PATH=$(pwd)/google-distributed-cloud-hosted-cli' >> ~/.bashrc
    echo 'export PATH="$GDCLOUD_PATH/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    

## Initialize gdcloud CLI default configuration

Initialize the gdcloud CLI default configuration:
    
    
    gdcloud init
    

Follow the prompted instructions to initialize the configuration. You must provide two properties to complete the initialization:

  * `organization_console_url`: The URL to your current GDC organization's console. This URL can be global or zonal:

    * For a global console URL, use the syntax `https://console.ORG_NAME.SUFFIX`, such as `https://console.org-1.gdch.google.com`.
    * For a zonal console URL, use the syntax `https://console.ORG_NAME.ZONE.SUFFIX`, such as `https://console.org-1.zone-1.gdch.google.com`.

Contact your Infrastructure Operator or Platform Administrator if you don't know your organization's console URL. If you're trying out the gdcloud CLI in [Google Distributed Cloud Sandbox](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/overview), see the GDC Sandbox [CLI setup instructions](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/gdcloud) for your instance's console URL.

  * `project`: The name of your current GDC project.




View these properties using the `gdcloud config list` command.

## Manage gdcloud CLI components

Components are installable parts of the GDC CLI. The gdcloud CLI is installed by default. List, install, and update gdcloud CLI components as needed.

### List components

View the current list of available components:
    
    
    gdcloud components list
    

### Install components

Install a component on the current version of your gdcloud CLI installation:
    
    
    gdcloud components install COMPONENT_ID
    

For example, this command installs the `kubectl` component:
    
    
    gdcloud components install kubectl
    

### Update components

To update all GDC components to the latest version of the gdcloud CLI, see [Upgrade to the latest gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-upgrade).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
