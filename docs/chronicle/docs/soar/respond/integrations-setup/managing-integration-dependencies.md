---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/managing-integration-dependencies/
title: Manage integration dependencies \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:55.718388+00:00
---

# Manage integration dependencies  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/managing-integration-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage integration dependencies 

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document outlines the process for updating custom integration script dependencies in Google SecOps to support newer Python runtimes. It details the steps required to remove legacy libraries, configure updated dependencies, and resolve common migration errors. 

To upgrade your integration scripts to the current Python runtime, refer to [Upgrade custom integrations to the latest Python version](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/upgrade-python-versions#upgrade-custom-integrations-to-python). 

## How to remove old dependencies and add new ones

  1. Go to **Response > IDE**. Select the target custom integration.
  2. Click more_vert **More > Configure custom integration**.
  3. Under **Script Dependencies** , copy and save the dependency names locally.   
For example, if your script dependencies include: `numpy-1.21.6-cp37-cp37m-manylinux_2_12_x86_64.manylinux2010_x86_64.whl`   
Copy only: `numpy`. 
  4. Delete these dependencies from the **Script Dependencies** list (only in this opened configuration window).
  5. Add the dependencies to the **Libraries** field using one of the following methods: 
     * **Install by dependency name:** Copy each dependency name (excluding version or target OS, e.g., `numpy`) from your file. The platform automatically downloads the dependency with the latest Python version configured (e.g., for 'numpy' in Python 3.11: `numpy-2.3.4-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl`).
     * **Install a specific version:** Enter the dependency name and version (e.g., `numpy==1.21.6`), ensuring it is compatible with your environment.
     * **Upload the target .whl file** (ensure it uses updated dependencies).
  6. Click **Add** and **Save**.



## Troubleshoot migration errors

### Resolving "Unsupported wheel" failures:

  * **Error Identity:** `ERROR: <dependency_name>.whl is not a supported wheel on this platform.`
  * **Root Issue:** When the platform tries to install a legacy `.whl` (for example, Python 3.7) within a modernized Python 3.11 environment.
  * **Solution:** Verify that all legacy wheels were purged and re-added using only base library names (as in the earlier example), allowing the system to fetch version-appropriate resources.

**Note:** Be aware that this exact error can also happen during the import of an integration if the integration package contains `.whl` files that are incompatible with the platform's Python version. If an import fails for this reason, you may need to manually update the dependencies to support the target environment. 

### Handle interface caching:

  * **Error:** The platform reverts to downloading old dependencies despite the Python version being updated in the settings.
  * **Root Issue:** Proceeding to library installation without a refresh may cause the system to use stale runtime parameters.
  * **Solution:** Adopt the best practice of refreshing the browser window immediately after saving the new Python configuration.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
