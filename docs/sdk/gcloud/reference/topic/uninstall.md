---
url: https://docs.cloud.google.com/sdk/gcloud/reference/topic/uninstall/
title: gcloud topic uninstall \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:36.254635+00:00
---

# gcloud topic uninstall  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/topic/uninstall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud topic uninstall Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud topic uninstall - supplementary help for uninstalling Google Cloud CLI 
DESCRIPTION
    
Uninstalling Google Cloud CLI
     Note: For installations completed using an OS package (such as `apt-get`, `yum`, etc.), uninstall Google Cloud CLI via the OS package manager. 

Note: For Windows installations, execute the uninstaller.exe found under your Google Cloud CLI directory. 

To completely remove Google Cloud CLI, follow these instructions: 

  * Locate your installation directory by running: 


    
    
    [gcloud info](https://docs.cloud.google.com/sdk/gcloud/reference/info) --format="value(installation.sdk_root)"

  * Locate your user config directory (typically `~/.config/gcloud` on MacOS and Linux) by running: 


    
    
    [gcloud info](https://docs.cloud.google.com/sdk/gcloud/reference/info) --format="value(config.paths.global_config_dir)"

  * Delete both these directories. 


  * Additionally, remove lines sourcing `completion.bash.inc` and `paths.bash.inc` in your `.bashrc` or equivalent shell init file, if you added them during installation. 


  * Review the contents of the `.boto` file in your home directory and remove the sections '[GoogleCompute]' and '[GSUtil]'. In addition, review the sections '[OAuth2]' and '[Credentials]' for settings that are no longer needed. 


  * Some systems may have `Cache` directories such as `~/Library/Caches/` on Mac OS X. Find and delete these directories for your system: 


    
    
    find ~/Library/Caches/ -type d -name "google-cloud-sdk" | xargs rm -r

NOTES
     These variants are also available: 
    
    
    [gcloud alpha topic uninstall](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/topic/uninstall)
    
    
    [gcloud beta topic uninstall](https://docs.cloud.google.com/sdk/gcloud/reference/beta/topic/uninstall)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
