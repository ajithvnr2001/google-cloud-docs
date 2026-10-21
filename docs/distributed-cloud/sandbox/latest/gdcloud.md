---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/gdcloud/
title: Set up the gdcloud CLI \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:52:53.544788+00:00
---

# Set up the gdcloud CLI  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/gdcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)



Send feedback 

#  Set up the gdcloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

This page contains an overview of the Distributed Cloud CLI, and instructions on how to download and configure it for usage with GDC Sandbox.

## Overview of the gdcloud CLI

The gdcloud CLI is a set of tools to create and manage Google Distributed Cloud (GDC) air-gapped resources. It is available for Linux only. Use these tools to perform common tasks from the command line or through scripts and automation. The `gdcloud` CLI can be used to bootstrap infrastructure, manage authentication, and customize local configurations. Note that this is distinct from the `gcloud` CLI used to manage Google Cloud.

This page contains simplified instructions that are specific to GDC Sandbox. For more detail on the gdcloud CLI in general, including configuration, upgrade, autocomplete, and accessibility, see the [GDC air-gapped `gdcloud` documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/resources/gdcloud-overview).

## Download the gdcloud CLI

Follow these instructions if you are connecting to the GDC Sandbox using `sshuttle`. If you are connecting to your instance's gateway over remote desktop, there is no need to download the tool, as `gdcloud` is pre-installed on the gateway machine at the path `/usr/share/gdcloud`.

  1. Download the gdcloud CLI bundle from the GDC console. 
     1. Navigate to your GDC console as described in [Connect to your instance](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/connect).
     2. Navigate to the **Connect with CLI** section.
     3. Click **Download CLI Bundle**.
  2. In a terminal window, extract the CLI bundle:
         
         cd ~/Downloads
         tar -xf gdcloud_cli.tar.gz
         

  3. Add the `gdcloud` CLI to your PATH so that you don't have to specify the location with every command. The following command assumes the CLI bundle was downloaded and extracted to the user's `Downloads` directory, and that the user's shell profile lives in `~/.bashrc`.
         
         echo 'export PATH=$PATH:~/Downloads/google-distributed-cloud-hosted-cli/bin' >> ~/.bashrc
         source ~/.bashrc
         

  4. Open a new terminal and run `gdcloud version` to confirm the command worked.

  5. Install the `auth` plugin. This plugin is required for using the kubeconfigs generated through the CLI. 
         
         gdcloud components install gdcloud-k8s-auth-plugin
         




## Configure gdcloud

  1. Configure the CLI by setting the organization URL to the URL of the GDC console.
         
         gdcloud config set core/organization_console_url https://console.org-1.zone1.google.gdch.test
         




### Download the certificate

The gdcloud requires authentication in order to perform commands. To use it with GDC Sandbox, start by downloading a certificate from the GDC Sandbox instance.

  1. Retrieve the certificate to authorize sign in. The following command downloads the certificate to the `/tmp` folder; you can choose to download it wherever you prefer.
         
         echo -n | \
         openssl s_client -showcerts -connect console.org-1.zone1.google.gdch.test:443 | \
         sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > /tmp/org-1-web-tls-ca.cert
         




## Authenticate with gdcloud

  1. Sign in to the gdcloud CLI, using the downloaded certificate. The following example assumes that the cert was downloaded into the `/tmp` folder.
         
         gdcloud auth login --login-config-cert=/tmp/org-1-web-tls-ca.cert
         

This command opens a browser window to the OIDC portal. Select **fake OIDC Provider** , and **Platform Admin** again (or whatever user you want to use for development, make sure you give the right access to the role).

Repeat this authentication step as needed, when the session times out.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
