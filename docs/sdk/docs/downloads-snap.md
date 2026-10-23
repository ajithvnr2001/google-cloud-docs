---
url: https://docs.cloud.google.com/sdk/docs/downloads-snap/
title: Installing a Snap package \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:51.362859+00:00
---

# Installing a Snap package  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/docs/downloads-snap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Installing a Snap package Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This installation method is only available on Ubuntu versions that support [snaps](https://docs.snapcraft.io/).

If you prefer automatic updates, you can install the Google Cloud CLI using a snap package on Ubuntu systems. This package contains the gcloud CLI, `gcloud alpha`, `gcloud beta`, `gsutil`, `docker-credential-gcloud`, and `bq` command-line tools only. It doesn't include `kubectl` or the App Engine extensions required to deploy an application using the gcloud CLI. If you need these components, install the [Debian package](https://docs.cloud.google.com/sdk/docs/install#deb) instead. 

  1. If you have the deprecated `google-cloud-sdk` snap package installed, remove it with the following command: 
         
         snap remove google-cloud-sdk

You can't install the `google-cloud-cli` snap package without removing this package because both installations require the same aliases. 
  2. Install the gcloud CLI snap package: 
         
         snap install google-cloud-cli --classic

  3. Optional: To enable command completion, update your profile to source the completion script. 

For Bash shells, run the following command:
         
         echo "source /snap/google-cloud-cli/current/completion.bash.inc" >> ~/.bashrc

For Zsh shells, run the following command:
         
         echo "source /snap/google-cloud-cli/current/completion.zsh.inc" >> ~/.zshrc

You must restart your shell for this change to take effect.

  4. Run [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) to initialize, authorize, and configure the gcloud CLI. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
