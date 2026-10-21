---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-apigeectl/
title: Step 3: Install apigeectl \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:18:34.617664+00:00
---

# Step 3: Install apigeectl  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-apigeectl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 3: Install apigeectl Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.11 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.11 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-apigeectl.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-apigeectl.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-apigeectl.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-apigeectl.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-apigeectl.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-apigeectl.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-apigeectl.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-apigeectl.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-apigeectl.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-apigeectl.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-apigeectl.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-apigeectl.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-apigeectl.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-apigeectl.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-apigeectl.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-apigeectl.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-apigeectl.html)



This step explains how to download and install [apigeectl](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cli-reference). 

##  Download and install `apigeectl`

`apigeectl` is the command-line interface (CLI) for installing and managing Apigee hybrid in a Kubernetes cluster.

The following steps describe how to download and install `apigeectl`:

###  Linux 

  1. Store the latest version number in a variable using the following command: 
         
         export VERSION=$(curl -s \
             "https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/current-version.txt?ignoreCache=1")

  2. Check that the variable was populated with a version number using the following command. If you want to use a different version, you can save that in an environment variable instead. 
         
         echo $VERSION
         
         1.11.2

  3. Download the release package for your operating system using the following command:
         
         curl -LO \
             https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**$VERSION** /apigeectl_linux_64.tar.gz

  4. Create a directory on your system to serve as the **base directory** for the Apigee hybrid installation. 
  5. Extract the downloaded gzip file (tar.gz) contents into the base directory you just created using the following command:
         
         tar xvzf filename -C path-to-base-directory

  6. Change directory to the base directory using the `cd` command. 
  7. The tar contents are, by default, expanded into a directory with the version and platform in its name. For example: `./apigeectl_1.11.2-d591b23_linux_64`. Rename that directory to `apigeectl` using the following command:
         
         mv apigeectl_1.11.2-d591b23_linux_64/ apigeectl

  8. Change to the directory using the following command: 
         
         cd ./apigeectl

This directory is the `apigeectl` home directory. It is where the `apigeectl` executable command is located. 

  9. Verify the version of `apigeectl` with the `version` command: 
         
         ./apigeectl version
         
         Version: 1.11.2

  10. Create an environment variable to hold this home directory path using the following command: 
         
         export APIGEECTL_HOME=$PWD

  11. Verify that the variable holds the correct path using the following command: 
         
         echo $APIGEECTL_HOME




###  Mac OS 

  1. Store the latest version number in a variable using the following command: 
         
         export VERSION=$(curl -s \
             "https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/current-version.txt?ignoreCache=1")

  2. Check that the variable was populated with a version number using the following command. If you want to use a different version, you can save that in an environment variable instead. 
         
         echo $VERSION
         
         1.11.2

  3. Download the release package for your operating system using the following command:
         
         curl -LO \
             https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**$VERSION** /apigeectl_mac_64.tar.gz

  4. Create a directory on your system to serve as the **base directory** for the Apigee hybrid installation. 
  5. Extract the downloaded gzip file contents into the base directory you just created using the following command:
         
         tar xvzf filename.tar.gz -C path-to-base-directory

  6. Change directory to the base directory using the `cd` command. 
  7. The tar contents are, by default, expanded into a directory with the version and platform in its name. For example: `./apigeectl_1.11.2-d591b23_mac_64`. Rename that directory to `apigeectl` using the following command:
         
         mv apigeectl_1.11.2-d591b23_mac_64 apigeectl

  8. Change to the directory using the following command: 
         
         cd ./apigeectl

This directory is the `apigeectl` home directory. It is where the `apigeectl` executable command is located. 

  9. Verify the version of `apigeectl` with the `version` command: 
         
         ./apigeectl version
         
         Version: 1.11.2

  10. Create an environment variable to hold this home directory path using the following command: 
         
         export APIGEECTL_HOME=$PWD

  11. Verify that the variable holds the correct path using the following command: 
         
         echo $APIGEECTL_HOME




###  Windows 

  1. Store the latest version number in a variable using the following command: 
         
         for /f "tokens=*" %a in ('curl -s ^
           https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/current-version.txt') ^
         do set VERSION=%a

  2. Check that the variable was populated with a version number using the following command. If you want to use a different version, you can save that in an environment variable instead. 
         
         echo %VERSION%
         
         1.11.2

  3. Download the release package for your operating system using the following command:
         
         curl -LO ^
           https://storage.googleapis.com/apigee-release/hybrid/apigee-hybrid-setup/**%VERSION%** /apigeectl_windows_64.zip

  4. Create a directory on your system to serve as the **base directory** for the Apigee hybrid installation. 
  5. Extract the downloaded .zip file contents into the current directory using the following command:
         
         tar xvzf filename.zip -C path-to-base-directory

  6. Change directory to the base directory using the `cd` command. 
  7. The tar file contents are, by default, expanded into a directory with the version and platform in its name. For example: `.\apigeectl_1.11.2-d591b23_windows_64`. Rename that directory to `apigeectl` using the following command:
         
         rename apigeectl_1.11.2-d591b23_windows_64 apigeectl

  8. Change to the directory using the following command: 
         
         cd .\apigeectl

This directory is the `apigeectl` home directory. It is where the `apigeectl` executable command is located. 

  9. Verify the version of `apigeectl` with the `version` command: 
         
         ./apigeectl version
         
         Version: 1.11.2

  10. Create an environment variable to hold this home directory path using the following command: 
         
         set APIGEECTL_HOME=%CD%

  11. Verify that the variable holds the correct path using the following command: 
         
         echo %APIGEECTL_HOME%




##  Set up the project directory structure 

The following directory structure is a suggested approach. It separates Apigee hybrid release software from configuration files that you must create. Through the use of the `$APIGEECTL_HOME` variable and symbolic links that you create, you can easily switch to a new software version if you choose to. See also [Upgrading Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/upgrade). 

**Note:** For the purpose of this quickstart, subsequent installation steps assume that you created the project structure as described in this section. If you follow this suggested structure, you can copy and paste most installation commands directly into your terminal. 

###  Linux 

  1. Be sure you are in the base directory (the directory where the `apigeectl` directory is located) by using the following command: 
         
         cd $APIGEECTL_HOME/..

  2. Create a new folder called `hybrid-files` using the following command. You can give the directory any name you wish, but in the docs, the name `hybrid-files` is used consistently. Later, you will store configuration files, service account keys, and TLS certificates in this folder. This folder lets you keep your config files separate from the `apigeectl` software installation. 
         
         mkdir hybrid-files

  3. The current directory structure now looks like the following: 
         
         pwd && ls
         
         /hybrid-base-directory
           apigeectl
           hybrid-files

  4. Change directory into the `hybrid-files` folder using the following command: 
         
         

  5. Create an environment variable to hold the path to your `hybrid-files` directory: 
         
         export HYBRID_FILES=$PWD
         
         echo $HYBRID_FILES

  6. Inside the `hybrid-files` directory, create the following subdirectories to organize files that you will create later: 
         
         mkdir overrides
         mkdir certs

  7. Inside the `hybrid-files` directory, create the following symbolic links to `$APIGEECTL_HOME`. These links allow you to run the `apigeectl` command from inside the `hybrid-files` directory as the following example shows: 

**Note:** If this is not the first time you have used this process, the following symbolic links may already exist. Check to see if the links already exist using the following command. If the directories exist, skip this step. 
         
         ls -l | grep ^l
         
         
         ln -s $APIGEECTL_HOME/tools tools
         ln -s $APIGEECTL_HOME/config config
         ln -s $APIGEECTL_HOME/templates templates
         ln -s $APIGEECTL_HOME/plugins plugins

  8. To check that the symlinks were created correctly, execute the following command and make sure the link paths point to the correct locations: 
         
         ls -l | grep ^l




###  Mac OS 

  1. Be sure you are in the base directory (the directory where the `apigeectl` directory is located) by using the following command: 
         
         cd $APIGEECTL_HOME/..

  2. Create a new folder called `hybrid-files` using the following command. You can give the directory any name you wish, but in the docs, the name `hybrid-files` is used consistently. Later, you will store configuration files, service account keys, and TLS certificates in this folder. This folder lets you keep your config files separate from the `apigeectl` software installation. 
         
         mkdir hybrid-files

  3. The current directory structure now looks like the following: 
         
         pwd && ls
         
         /hybrid-base-directory
           apigeectl
           hybrid-files

  4. Change directory into the `hybrid-files`folder using the following command: 
         
         cd hybrid-files

  5. Create an environment variable to hold the path to your `hybrid-files` directory: 
         
         export HYBRID_FILES=$PWD
         
         echo $HYBRID_FILES

  6. Inside the `hybrid-files` directory, create the following subdirectories to organize files that you will create later: 
         
         mkdir overrides
         mkdir certs

  7. Inside the `hybrid-files` directory, create the following symbolic links to `$APIGEECTL_HOME`. These links allow you to run the `apigeectl` command from inside the `hybrid-files` directory as the following example shows: 

**Note:** If this is not the first time you have used this process, the following symbolic links may already exist. Check to see if the links already exist using the following command. If the directories exist, skip this step. 
         
         ls -l | grep ^l
         
         
         ln -s $APIGEECTL_HOME/tools tools
         ln -s $APIGEECTL_HOME/config config
         ln -s $APIGEECTL_HOME/templates templates
         ln -s $APIGEECTL_HOME/plugins plugins

  8. To check that the symlinks were created correctly, execute the following command and make sure the link paths point to the correct locations: 
         
         ls -l | grep ^l




###  Windows 

  1. Be sure you are in the base directory (the directory where the `apigeectl` directory is located) by using the following command: 
         
         cd %APIGEECTL_HOME%\..

  2. Create a new folder called `hybrid-files` using the following command. You can give the directory any name you wish, but in the docs, the name `hybrid-files` is used consistently. Later, you will store configuration files, service account keys, and TLS certificates in this folder. This folder lets you keep your config files separate from the `apigeectl` software installation. 
         
         mkdir hybrid-files

  3. The current directory structure now looks like the following: 
         
         dir
         
         Directory of C:\Users\example\hybrid
         
         08/05/2021  01:38 PM    <DIR>          .
         08/05/2021  01:38 PM    <DIR>          ..
         08/02/2021  01:11 PM    <DIR>          apigeectl
         08/02/2021  11:13 AM         5,803,963 apigeectl_1.11.2rc1-437dccc_windows_64.zip
         08/05/2021  01:38 PM    <DIR>          hybrid-files

  4. Change directory into the `hybrid-files`folder.
  5. Create an environment variable to hold the path to your `hybrid-files` directory: 
         
         set HYBRID_FILES=%CD%
         
         echo %HYBRID_FILES%

  6. Inside the `hybrid-files` directory, create the following subdirectories to organize files that you will create later: 
         
         mkdir overrides
         mkdir certs

  7. Inside the `hybrid-files` directory, create the following symbolic links to `$APIGEECTL_HOME`. These links allow you to run the `apigeectl` command from inside the `hybrid-files` directory as the following example shows: **Note:** You will need administrator privilege on your Windows computer to run the `mklink` command. You can achieve this by running your command terminal as administrator or by using the `runas` command. For example: 
         
         runas /noprofile /user:mymachine\administrator "mklink /d config %APIGEECTL_HOME%\config"
         
         
         mklink /d config %APIGEECTL_HOME%\config\
         mklink /d plugins %APIGEECTL_HOME%\plugins\
         mklink /d templates %APIGEECTL_HOME%\templates\
         mklink /d tools %APIGEECTL_HOME%\tools\

  8. To check that the symlinks were created correctly, use `dir`: 
         
         dir
         
         Directory of C:\Users\example\hybrid\hybrid-files
         
         08/05/2021  01:56 PM    <DIR>          .
         08/05/2021  01:56 PM    <DIR>          ..
         08/05/2021  01:46 PM    <DIR>          certs
         08/05/2021  01:55 PM    **< SYMLINKD>     config [C:\Users\example\hybrid\apigeectl\config\]**
         08/05/2021  01:46 PM    <DIR>          overrides
         08/05/2021  01:56 PM    **< SYMLINKD>     plugins [C:\Users\example\hybrid\apigeectl\plugins\]**
         08/05/2021  01:56 PM    **< SYMLINKD>     templates [C:\Users\example\hybrid\apigeectl\templates\]**
         08/05/2021  01:56 PM    **< SYMLINKD>     tools [C:\Users\example\hybrid\apigeectl\tools\]**
             




You now have a home base from which you can configure, deploy, and manage Apigee hybrid in your Kubernetes cluster. Next, you will create the Google Cloud service accounts and credentials required to configure hybrid runtime components. 

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-cert-manager) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-apigeectl) [(NEXT) Step 4: Set up service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-create-tls-certificates) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-configure-cluster) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-enable-synchronizer-access) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-check-cluster) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-hybrid-runtime) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-workload-identity)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
