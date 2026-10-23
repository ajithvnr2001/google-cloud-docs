---
url: https://docs.cloud.google.com/shell/docs/how-cloud-shell-works/
title: How Cloud Shell works \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:46:42.748285+00:00
---

# How Cloud Shell works  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/how-cloud-shell-works/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)



Send feedback 

#  How Cloud Shell works Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Shell provisions a Compute Engine virtual machine running a Debian-based Linux operating system for your temporary use. This virtual machine is owned and managed by Google Cloud, so will not appear within any of your Google Cloud projects.

**Note:** Your organization controls whether you have access to Cloud Shell.

Cloud Shell instances are provisioned on a per-user, per-session basis. The instance persists while your Cloud Shell session is active; after an hour of inactivity, your session terminates and its VM is discarded. For more on usage quotas, refer to the [limitations guide](https://docs.cloud.google.com/shell/docs/limitations#usage_limits).

With the default Cloud Shell experience, you are allocated with an ephemeral, pre-configured VM and the environment you work with is a Docker container running on that VM. You can also [customize your environment](https://docs.cloud.google.com/shell/docs/custom-environments) automatically on VM boot to ensure that your Cloud Shell instance includes your preferred tools.

## Persistent disk storage

Cloud Shell provisions 5 GB of free [persistent disk storage](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) mounted as your `$HOME` directory on the virtual machine instance. This storage is on a per-user basis and is available across projects. Unlike the instance itself, this storage does not time out on inactivity. All files you store in your home directory, including installed software, scripts and user configuration files like `.bashrc` and `.vimrc`, persist between sessions. Your `$HOME` directory is private to you and can't be accessed by other users.

**Warning:** If you delete your `$HOME` directory, or if you don't access Cloud Shell for 120 days, Cloud Shell automatically deletes your `$HOME` directory and can't recover your files. You'll receive an email notification before this occurs. Starting a Cloud Shell session prevents the `$HOME` directory persistent storage from being recycled.

When using Cloud Shell, you cannot expand persistent disk storage space. For more control of your storage persistence, and for more storage space, you can use [Cloud Workstations](https://cloud.google.com/workstations/docs/overview).

Cloud Shell also offers [Ephemeral mode](https://docs.cloud.google.com/shell/docs/using-cloud-shell#choosing_ephemeral_mode) which is the Cloud Shell experience without persistent disk storage. With Ephemeral mode, you'll have faster startup times but all the files you create in your session are lost on session end.

## Authorization

When you make a Google Cloud API call or use a command-line tool that requires credentials (such as the Google Cloud CLI) with Cloud Shell for the first time, Cloud Shell prompts you to authorize. Click **Authorize** to allow the tool to use your credentials to make calls.

Refer to the [Authorizing with Cloud Shell](https://docs.cloud.google.com/shell/docs/auth) for more details.

## Pre-configured environment variables

When Cloud Shell is started, the active project in the Google Cloud console is propagated to your `gcloud` configuration inside Cloud Shell for immediate use. `GOOGLE_CLOUD_PROJECT`, the environmental variable used by Application Default Credentials library support to define the project ID, is also set to point to the active project in the Google Cloud console. The environment variable `WEB_HOST` points to the hostname of your Cloud Shell VM which you can use to make HTTPS requests to the environment.

**Note:** While `GOOGLE_CLOUD_PROJECT` inherits the active project from the Google Cloud console, your Cloud Shell instance is not directly associated with or managed by this project.

## Zone selection

Cloud Shell is globally distributed across multiple Google Cloud regions. When you first connect to Cloud Shell, you are automatically assigned to the closest available region. You can't pick your own region and if Cloud Shell doesn't pick the closest region, Cloud Shell tries to migrate your Cloud Shell VM to a closer region when your Cloud Shell VM isn't in use.

To view your current region, run the following command from a Cloud Shell session:
    
    
    curl metadata/computeMetadata/v1/instance/zone
    

## Image rollout

The Cloud Shell container image is updated weekly to keep prepackaged tools up to date. This means Cloud Shell always comes with the latest versions of the gcloud CLI, Docker, and other utilities.

## Root user

When you set up a Cloud Shell session, you get a regular Unix user account with a username based on your email address. With this access, you have full root privileges on your allocated VM and can even run sudo commands, if you need to.

## Available tools

The Cloud Shell virtual machine instance has the following pre-installed tools:

Type | Tool  
---|---  
Linux shell interpreters |  bash  
sh   
Linux utilities | Standard Debian system utilities  
gcloud CLI and tools | [Google Cloud CLI](https://docs.cloud.google.com/sdk) including the gcloud CLI  
Text editors |  Emacs  
Vim  
Nano   
Build and package tools |  Gradle  
Helm  
Make  
Maven  
Bazel  
npm  
nvm  
pip  
uv  
Composer  
  
Source control tools |  Git  
Mercurial  
  
Additional tools |  Docker  
iPython  
MySQL client  
gRPC compiler  
TensorFlow   
  
You can install additional software packages on the virtual machine instance but the installation will not persist after the instance terminates unless you install the software in your `$HOME` directory or create a [custom environment](https://docs.cloud.google.com/shell/docs/custom-environments).

## Language support

**Note:** Language versions might change. You can however install different versions if you need to using the [environment customization script](https://docs.cloud.google.com/shell/docs/configuring-cloud-shell#environment_customization).

The Cloud Shell virtual machine instance provides pre-installed language support for the following:

Language | Version  
---|---  
Java | JRE/JDK 17 (OpenJDK)  
Go | Latest  
Python | 3.12  
Node.js | LTS  
Ruby | 3.2  
PHP | 8.3  
.NET Core | SDKs 6.0, 7.0, and 8.0  
  
The default version of the Java environment is 17. To change the current Cloud Shell session to use version 1.11 of the JRE and JDK, enter the following at the Cloud Shell command prompt:
    
    
    sudo update-java-alternatives -s java-1.11.0-openjdk-amd64 && export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
    

To change to 21:
    
    
    sudo update-java-alternatives -s java-1.21.0-openjdk-amd64 && export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
    

To change back to 17:
    
    
    sudo update-java-alternatives -s java-1.17.0-openjdk-amd64 && export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64/jre
    

## Safe mode

If there's a problem in your `.bashrc` or `.tmux.conf` files, Cloud Shell immediately closes after connection. Safe mode restarts your Cloud Shell instance and logs you in as root, allowing you to fix any issues in the files.

To open Cloud Shell in safe mode:

  * Append `cloudshellsafemode=true` to the URL.
  * In Cloud Shell, click more_vert, click **Safe Mode** , and then click **Restart**.



To permanently delete all files in your home directory and restore your Cloud Shell home directory to a clean state, you can [reset your Cloud Shell VM](https://docs.cloud.google.com/shell/docs/resetting-cloud-shell).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
