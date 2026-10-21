---
url: https://docs.cloud.google.com/container-optimized-os/docs/how-to/osconfig/
title: Configuring instances with user-defined guest policies \u00a0|\u00a0 Container-Optimized OS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:16:41.248841+00:00
---

# Configuring instances with user-defined guest policies  |  Container-Optimized OS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/how-to/osconfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Guides ](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance)



Send feedback 

#  Configuring instances with user-defined guest policies Stay organized with collections  Save and categorize content based on your preferences. 

Container-Optimized OS includes the [OS Config](https://docs.cloud.google.com/compute/docs/vm-manager) agent. You can use OS Config's [guest policies](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies#resource:-guestpolicy) to configure your instance. `packages` and `packageRepositories` features of guest policies are not supported on Container-Optimized OS.

To enable OS Config and create a guest policy, see [Enable OS Config agent](https://docs.cloud.google.com/compute/docs/manage-os#overview) and [Create a guest policy](https://docs.cloud.google.com/compute/docs/os-config-management/create-guest-policy), respectively.

Here is an example that shows how users can use `assignment` and `recipes` features of guest policies to create a file on instances located at us-central1-a.
    
    
    assignment:
      zones:
      - us-central1-a
    recipes:
    - name: recipe-runscript
      desiredState: INSTALLED
      installSteps:
      - scriptRun:
          interpreter: SHELL
          script: touch /tmp/TOUCH_FILE
    

**Note:** While it is optional to provide an `interpreter` on other distros, Container-Optimized OS requires `interpreter` to execute the given script.**Note:** While `recipes` are run once-per-instance on other distros, on Container-Optimized OS, `recipes` are run on every boot. This is because most of the directories are stateless; therefore, changes made by `recipes` will not persist across reboots. See [Disks and Filesystem](https://docs.cloud.google.com/container-optimized-os/docs/concepts/disks-and-filesystem) for more information on Container-Optimized OS's filesystem.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
