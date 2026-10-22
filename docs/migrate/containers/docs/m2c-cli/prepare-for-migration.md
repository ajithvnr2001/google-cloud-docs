---
url: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/prepare-for-migration/
title: Set up for migration \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:20.005190+00:00
---

# Set up for migration  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/prepare-for-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Set up for migration 

Before you start the modernization process, you need to check whether your application component is compatible for modernization and prepare your setup for modernization.

This page describes how to prepare your source and local machines for modernization.

## Set up the Linux source machine

**Note:** If you're going to migrate Windows IIS applications, you don't need to perform the steps to set up the Windows source machine for migration.

  * Install `rsync`:

    * On Debian:
          
          sudo apt install rsync
          

    * On Fedora:
          
          sudo dnf install rsync
          

Ensure that `rsync` is available in the `PATH` setting.




## Set up the Linux local machine

  * [Install Docker](https://docs.docker.com/engine/install) and ensure that it is available in the `PATH`.

**Note:** To avoid [issues that might occur while using Snap version of Docker](https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/issues-with-m2c-cli#the_analyze_command_fails_when_using_the_snap_version_of_docker), ensure that you install Docker without using Snap.

If the user running Migrate to Containers CLI is a non-root user, then [allow the non-root user to run containers](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).




### Download or upgrade Migrate to Containers CLI

  * Download or upgrade the Migrate to Containers CLI on a Linux machine:
        
        curl -O "https://m2c-cli-release.storage.googleapis.com/$(curl -s https://m2c-cli-release.storage.googleapis.com/latest)/linux/amd64/m2c"
        chmod +x ./m2c
        

This downloads the latest version of the Migrate to Containers CLI and Migrate to Containers plugins.




### Check connectivity

Ensure that you can access the source machine from the local machine using either direct SSH or the `gcloud compute ssh` command.

**Note:** The user used for SSH connection must be either a sudoer or root. If the user used to perform SSH can't act as root, then Migrate to Containers CLI might not be able to examine files and directories relevant to the modernization process.

### Optional: Set up for offline migration

If you want to perform migration on your local network without pulling resources from the internet, then you can complete the following steps to prepare your local machine for offline migrations.

After you've downloaded Migrate to Containers CLI, perform the following steps:

  1. Download the offline Migrate to Containers CLI plugins bundle:
         
         curl -O https://storage.googleapis.com/modernize-plugins-prod/$(curl -s https://storage.googleapis.com/modernize-plugins-prod/latest)/m2c-offline-bundle-linux.tar
         

  2. If required, copy the Migrate to Containers CLI and offline Migrate to Containers CLI plugins bundle to the offline environment.

  3. Unpack the offline Migrate to Containers CLI plugins bundle:
         
         ./m2c plugins unpack -i m2c-offline-bundle-linux.tar
         

To add support for offline data migration, specify a container registry that is available in your local network:
         
         ./m2c plugins unpack -i m2c-offline-bundle-linux.tar --registry HOSTNAME
         

Replace HOSTNAME with the container registry hostname.




Your local machine is set up for offline migration. To upgrade the offline Migrate to Containers CLI plugins bundle, upgrade Migrate to Containers CLI to the latest version, and then repeat the steps to download and unpack the plugins bundle.

If you want to turn off the offline mode later, then you can use the `config set` command to set the `offline` option to `false`.

## Set up the Windows local machine

  * You must be able to run as administrator on the local machine.
  * [Install Docker](https://docs.docker.com/engine/install).



### Download or upgrade Migrate to Containers CLI

To download or upgrade Migrate to Containers CLI on a Windows machine, perform the following steps:

###  cmd 

  1. Find the latest version of Migrate to Containers CLI:
         
         curl -s https://m2c-cli-release.storage.googleapis.com/latest
         

  2. Download the latest version of Migrate to Containers CLI:
         
         curl -O "https://m2c-cli-release.storage.googleapis.com/VERSION/windows/amd64/m2c.exe"
         

Replace VERSION with the latest version of Migrate to Containers CLI.




###  PowerShell 

  * Download the latest version of Migrate to Containers CLI:
        
        curl.exe -O https://m2c-cli-release.storage.googleapis.com/$(curl.exe -s https://m2c-cli-release.storage.googleapis.com/latest)/windows/amd64/m2c.exe
        




This downloads the latest version of the Migrate to Containers CLI and Migrate to Containers plugins.

## What's next

  * Learn how to [copy the source machine's file system](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/copy-file-system).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
