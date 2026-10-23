---
url: https://docs.cloud.google.com/storage/docs/gsutil/
title: gsutil tool \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:16.223815+00:00
---

# gsutil tool  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/gsutil/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  gsutil tool Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** gsutil is not the recommended CLI for Cloud Storage. [Use `gcloud storage`](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud) commands in the Google Cloud CLI instead.**Important:** After March 2027, gsutil will no longer be available as part of the Google Cloud CLI installation package. gsutil will only be distributed as a standalone tool that can be installed by using PyPI. We recommend that you migrate to using `gcloud storage` commands in the Google Cloud CLI instead of using gsutil. However, if you want to continue using gsutil with your existing scripts and receiving updates for gsutil, you can [install gsutil as a standalone tool](https://docs.cloud.google.com/storage/docs/gsutil_install#install). If you've already installed gsutil as part of the Google Cloud CLI, [remove the gsutil component from your Google Cloud CLI installation](https://docs.cloud.google.com/storage/docs/gsutil_install#gsutil-uninstall-from-sdk) before installing gsutil as a standalone tool.

gsutil is a Python application that lets you access Cloud Storage from the command line. You can use gsutil to do a wide range of bucket and object management tasks, including:

  * Creating and deleting buckets.
  * Uploading, downloading, and deleting objects.
  * Listing buckets and objects.
  * Moving, copying, and renaming objects.
  * Editing object and bucket ACLs.



gsutil performs all operations, including uploads and downloads, using HTTPS and transport-layer security (TLS).

## Should you use gsutil?

Generally, you should [use `gcloud storage` commands](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud) instead of `gsutil` commands:

  * The gsutil tool is a legacy Cloud Storage CLI and minimally maintained.

  * The gsutil tool does not support working with newer Cloud Storage features, such as [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) and [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders).

  * `gcloud storage` commands require less manual optimization in order to achieve the fastest upload and download rates.




### Migrating to the gcloud CLI

If you are a gsutil user wanting to migrate to the gcloud CLI, you should first check if you're using a standalone version of gsutil by running the following command:
    
    
    gsutil version -l

  * If the result of the command includes `using cloud sdk: False`, then you are using a standalone version of gsutil. To migrate to the gcloud CLI, start by [Installing the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).

  * If the result of the command includes `using cloud sdk: True`, then you already have the gcloud CLI installed.




Once the gcloud CLI is installed, you can use `gcloud storage` commands just like you use `gsutil` commands. The following resources can help you get started:

  * Explore `gcloud storage` commands by following the quickstart [Discover object storage with gcloud CLI](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud).

  * Read the [`gcloud storage` reference](https://docs.cloud.google.com/sdk/gcloud/reference/storage).


**Note:** Shim, which translated your gsutil commands to gcloud CLI commands, is no longer recommended. If you still need documentation or help related to the shim, reach out to Google Cloud Support team.

## Syntax for accessing resources

gsutil uses the prefix `gs://` to indicate a resource in Cloud Storage:
    
    
    gs://BUCKET_NAME/OBJECT_NAME

In addition to specifying exact resources, gsutil supports the use of [wildcards](https://docs.cloud.google.com/storage/docs/wildcards) in your commands.

### Accessing a file list

For operations involving a large number of files, you can pass a list of source files to gsutil by using the `-I` flag. This tells gsutil to read the list of files or object URLs from stdin rather than from the command-line arguments.

The input must be a list of local file paths or Cloud Storage object URLs, with one path per line. For example, you can create a file named `example_file_list.txt` that contains the following paths:
    
    
    gs://example-source-bucket/data-01.csv
    gs://example-source-bucket/images/logo.png
    /local/logs/error_log_20251226.txt

The following example commands read the file paths from `example_file_list.txt` and copy them to a destination bucket named `gs://example-destination-bucket`:
    
    
    cat example_file_list.txt | gsutil -m cp -I gs://example-destination-bucket/

You can also generate the list of paths on the fly and pipe it directly into gsutil. For example, the following commands upload all JPG files found in your current directory and copy them to `gs://example-destination-bucket`:
    
    
    find . -name "*.jpg" | gsutil -m cp -I gs://example-destination-bucket

## Built-in help

gsutil contains thorough built-in help about every command as well as a number of topics, which you can list and read with the `gsutil help` command.

To get information about a specific command or topic, use `gsutil help` followed by the intended command or topic name. For example, `gsutil help cp` and `gsutil help options` are a command help page and a topic help page, respectively.

To get information about your gsutil installation, use the `gsutil version` command:
    
    
    gsutil version -l

## Usage statistics

During the installation process, you can opt-in to tracking usage statistics which helps improve the gsutil tool. If you subsequently decide that you want to disable these usage statistics, see [Usage statistics](https://docs.cloud.google.com/sdk/docs/usage-statistics).

## About gsutil

gsutil is an open-source project. To download the developer version of gsutil or [volunteer to help develop gsutil](https://github.com/GoogleCloudPlatform/gsutil/blob/master/gslib/addlhelp/dev.py), visit the [gsutil project](https://github.com/GoogleCloudPlatform/gsutil/) on GitHub.

### Limitations

  * When using gsutil with Windows, commands that use the `-m` global flag cannot be canceled using `Ctrl-C`.



## What's next

  * [Install gsutil](https://docs.cloud.google.com/storage/docs/gsutil_install#install).
  * See community discussion in [gsutil Stack Overflow questions](http://stackoverflow.com/questions/tagged/google-cloud-storage+gsutil).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
