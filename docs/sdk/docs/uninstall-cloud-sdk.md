---
url: https://docs.cloud.google.com/sdk/docs/uninstall-cloud-sdk/
title: Uninstalling the Google Cloud CLI \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:46.631214+00:00
---

# Uninstalling the Google Cloud CLI  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/docs/uninstall-cloud-sdk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Uninstalling the Google Cloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

For installations completed using an OS package (such as `apt-get` or `yum`), uninstall gcloud CLI using the OS package manager. 

For Windows installations, execute the `uninstaller.exe` file in your gcloud CLI directory.

To remove the gcloud CLI, follow these instructions:

  1. Locate your installation directory by running:
         
         gcloud info --format='value(installation.sdk_root)'
         

Locate your user config directory (typically `~/.config/gcloud` on MacOS and Linux) by running:
         
         gcloud info --format='value(config.paths.global_config_dir)'
         

  2. Delete both of these directories.

  3. Additionally, remove lines sourcing `completion.bash.inc` and `path.bash.inc` in your `.bashrc` or equivalent shell init file, if you added them during installation.

  4. Review the contents of the `.boto` file in your home directory and remove the sections **[GoogleCompute]** and **[GSUtil]**. In addition, review the sections **[OAuth2]** and **[Credentials]** for settings that are no longer needed.

  5. Some systems may have `Cache` directories such as `~/Library/Caches/` on Mac OS X. Find and delete these directories for your system:
         
         find ~/Library/Caches/ -type d -name "google-cloud-sdk" | xargs -I {} rm -r "{}"
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
