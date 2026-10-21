---
url: https://docs.cloud.google.com/shell/docs/using-cloud-shell-with-gcloud-cli/
title: Use Cloud Shell with the gcloud CLI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:31.434039+00:00
---

# Use Cloud Shell with the gcloud CLI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/using-cloud-shell-with-gcloud-cli/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)



Send feedback 

#  Use Cloud Shell with the gcloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

If you have the [gcloud CLI installed](https://docs.cloud.google.com/sdk/install), you can interact with Cloud Shell from your terminal and use it as a sandbox and a portable development environment. This provides the convenience of working with Cloud Shell resources, whether to quickly test an operation or use an IDE of your choice to edit a file saved on your Cloud Shell instance from your local desktop.

## Use `gcloud cloud-shell`

The current `gcloud cloud-shell` command group offering provides the following functionality:

  * Establishing an interactive SSH session with Cloud Shell using [`gcloud cloud-shell ssh`](https://docs.cloud.google.com/sdk/gcloud/reference/cloud-shell/ssh).
  * Copy files between your local and Cloud Shell machine via [scp](https://docs.cloud.google.com/sdk/gcloud/reference/cloud-shell/scp).
  * Mount your Cloud Shell directory to your local file system via [sshfs](https://docs.cloud.google.com/sdk/gcloud/reference/cloud-shell/get-mount-command).



For more detail, see the reference documentation for [`gcloud cloud-shell`](https://docs.cloud.google.com/sdk/gcloud/reference/cloud-shell).

**Note:** To propagate your credentials to your Cloud Shell when starting it from the Google Cloud CLI, use the [`--authorize-session`](https://docs.cloud.google.com/sdk/gcloud/reference/cloud-shell/ssh#--authorize-session) flag when running the `gcloud cloud-shell ssh` command.

## Example workflow

To illustrate the workings of `gcloud cloud-shell`, here is an example of how you can use these commands in practice:

  1. Start a SSH session:
         
         gcloud cloud-shell ssh
         

  2. Copy a file, `data.txt`, from Cloud Shell to your local machine:
         
         gcloud cloud-shell scp cloudshell:~/data.txt localhost:~data.txt
         

  3. If you're using Mac or Linux, you can mount your Cloud Shell home directory onto your local file system after installing [sshfs](https://github.com/libfuse/sshfs).

This allows you to edit the files in your Cloud Shell home directory using your choice of local tools. All the data in your remotely mounted file system is stored on a [Persistent Disk](https://docs.cloud.google.com/persistent-disk) and stored across sessions.
         
         gcloud cloud-shell get-mount-command ~/my-cloud-shell
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
