---
url: https://docs.cloud.google.com/sdk/docs/downloads-interactive/
title: Using the Google Cloud CLI installer \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:51.196418+00:00
---

# Using the Google Cloud CLI installer  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/docs/downloads-interactive/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Using the Google Cloud CLI installer Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud CLI provides an installer for each supported platform and can be deployed interactively or non-interactively.

## Interactive installation

The installer lets you download, install, and set up the latest version of Google Cloud CLI in an interactive mode. When you run the installer, it downloads Google Cloud CLI components and installs them on the local system. It also performs additional setup tasks like adding gcloud CLI components to your `PATH` and enabling command completion in your shell.

**Note:** The installer is designed to make it easy for a user to install the latest version of Google Cloud CLI. If you want to use a script to install a specific version in non-interactive mode — for example, to install the same version automatically every time you build a production system — use a [versioned archive](https://docs.cloud.google.com/sdk/docs/downloads-versioned-archives) of the Google Cloud CLI. Linux and macOS

  1. Run the following command: 
         
         curl https://sdk.cloud.google.com | bash

     * When prompted, choose a location on your file system for the `google-cloud-sdk` subdirectory. The default is your Home directory. 
     * To send anonymous usage statistics to help improve gcloud CLI, answer `Y` when prompted. 
     * To add gcloud CLI command-line tools to your `PATH` and enable command completion, answer `Y` when prompted. 
  2. Restart your shell: 
         
         exec -l $SHELL

  3. Run [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) to initialize, authorize, and configure the gcloud CLI. 

Windows (Installer)

The Google Cloud CLI on Windows requires Windows 8.1 and later, or Windows Server 2012 and later.

  1. Download the [Google Cloud CLI installer](https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe). 

Alternatively, open a PowerShell terminal and run the following PowerShell commands: 
         
         (New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")
         
         & $env:Temp\GoogleCloudSDKInstaller.exe
             

  2. Launch the installer and follow the prompts. The installer is signed by Google LLC.

     * If you're using a screen reader, check the **Turn on screen reader mode** checkbox. This option configures `gcloud` to use status trackers instead of unicode spinners, display progress as a percentage, and flatten tables. For more information, see the [Accessibility features guide](https://docs.cloud.google.com/sdk/docs/enabling-accessibility-features). 
     * Google Cloud CLI requires Python; supported versions are Python 3.10 to 3.15. By default, the Windows version of Google Cloud CLI comes bundled with Python 3. To use Google Cloud CLI your operating system must be able to run a supported version of Python. 
     * The installer installs all necessary dependencies, including the needed Python version. While Google Cloud CLI installs and manages Python 3 by default, you can use an existing Python installation if necessary by **unchecking** the option to Install Bundled Python. See [`gcloud topic startup`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/startup) to learn how to use an existing Python installation. 
  3. After installation is complete, the installer gives you the option to create Start Menu and Desktop shortcuts, start the Google Cloud CLI shell, and configure the gcloud CLI. Leave the options to start the shell and configure your installation selected. The installer starts a terminal window and runs the [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) command to initialize, authorize, and configure the gcloud CLI. 
  4. The default installation doesn't include the App Engine extensions required to deploy an application using `gcloud` commands. These components can be installed using the [gcloud CLI component manager](https://docs.cloud.google.com/sdk/docs/managing-components). 



**Troubleshooting tips**

  * If your installation is unsuccessful due to the `find` command not being recognized, ensure your `PATH` environment variable is set to include the folder containing `find`. Usually, this is `C:\WINDOWS\system32;`.
  * If you uninstalled the gcloud CLI, you must reboot your system before installing the gcloud CLI again.
  * If unzipping fails, run the installer as an administrator.

Windows (Zip)

You can also install the latest version from a downloaded `.zip` file:

  1. Download [google-cloud-sdk.zip](https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip) and extract its contents. (Right click on the downloaded file and select **Extract All**.) 

  2. Launch the `google-cloud-sdk\install.bat` script and follow the installation prompts. 

  3. When the installation finishes, restart the command prompt (`cmd.exe`). 

  4. Run [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init): 
         
         C:\> gcloud init




## Non-interactive (silent) deployment

You can automate Google Cloud CLI installation using the install script.

**For Linux and MacOS:**

Save the install script locally instead of piping it to bash.

  1. Enter the following at a command prompt: 
         
         curl https://sdk.cloud.google.com > install.sh

  2. Run the script, passing arguments described as follows: 
         
         bash install.sh --disable-prompts




The `install.sh` options are:

  * `--disable-prompts` \- disable prompts.
  * `--install-dir=DIRECTORY` \- set the installation root directory to `DIRECTORY`. The Google Cloud CLI is installed in `DIRECTORY/google-cloud-sdk`. The default is $HOME.



**For Windows:**

**Important:** These flags are for the [Windows installer](https://docs.cloud.google.com/sdk/docs/install-sdk) and are case sensitive.

  * `/S` \- install silently. No installer pages are displayed. Use flags to change install settings.
  * `/D` \- set the default installation directory. It must be the last parameter used in the command line and must not contain any quotes, even if the path contains spaces. Only absolute paths are supported, for example `/D=C:\CloudSDK`
  * `/allusers` \- install for all users
  * `/singleuser` \- install for current user (default)
  * `/screenreader` \- turn on screen reader mode (default is to turn it off)
  * `/reporting` \- enable usage reporting (default is to turn off usage reporting)
  * `/noreporting` \- disable usage reporting (default is to turn off usage reporting)
  * `/nostartmenu` \- don't create start menu shortcut (default is to create shortcut)
  * `/nodesktop` \- don't create desktop shortcut (default is to create shortcut)



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
