---
url: https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-cloud-storage/
title: Troubleshooting file synchronization issues \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:10.314001+00:00
---

# Troubleshooting file synchronization issues  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-cloud-storage/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Troubleshooting file synchronization issues Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-cloud-storage "View this page for Managed Airflow \(Gen 2\)") | Managed Airflow (Legacy Gen 1)

Managed Airflow synchronizes specific folders in your environment's bucket to Airflow components that run in your environment. See [Data stored in Cloud Storage](https://docs.cloud.google.com/composer/docs/composer-3/cloud-storage) for more information. This page refers to issues that could disrupt the synchronization process and how to troubleshoot them.

## Common Issues

The following sections describe symptoms and potential fixes for some common file synchronization issues.

### Handling a large number of DAGs and plugins in dags and plugins folders

Contents of `/dags` and `/plugins` folders are synchronized from your environment's bucket to local file systems of Airflow workers and schedulers.

The more data stored in these folders, the longer it takes to perform the synchronization. To address such situations:

  * Limit the number of files in `/dags` and `/plugins` folders. Store only the minimum of required files.

  * Increase the disk space available to Airflow schedulers and workers.

  * Increase CPU and memory of Airflow schedulers and workers, so that the sync operation is performed faster.

  * In case of a very large number of DAGs, divide DAGs into batches, compress them into zip archives and deploy these archives into the `/dags` folder. This approach speeds up the DAGs syncing process. Airflow components extract zip archives before processing DAGs.

  * Generating DAGs in a programmatic way might also be a method for limiting the number of DAG files stored in the `/dags` folder. See the **Programmatic DAGs** section in the [DAGs Troubleshooting page](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-dags#programmatic-dags) to avoid problems with scheduling and executing DAGs generated programmatically.




### Anti-patterns impacting DAGs and plugins syncing to schedulers, workers and web servers

Managed Airflow synchronizes the content of `/dags` and `/plugins` folders to schedulers and workers. Certain objects in `/dags` and `/plugins` folders might prevent this synchronization to work correctly or slow it down.

  * The `/dags` folder is synchronized to schedulers and workers.

This folder is not synchronized to the web server. 

  * The `/plugins` folder is synchronized to schedulers, workers and web servers.




You might encounter the following issues:

  * You uploaded gzip-compressed files that use [compression transcoding](https://docs.cloud.google.com/storage/docs/transcoding) to `/dags` and `/plugins` folders. It usually happens if you use the `--gzip-local-all` flag in a `gcloud storage cp` command to upload data to the bucket.

Solution: Delete the object that used compression transcoding and re-upload it to the bucket.

  * One of the objects is named `.`. Such an object is not synchronized to schedulers and workers, and it might stop synchronizing at all.

Solution: Rename the object.

  * A folder and a DAG Python file have the same names, for example `a.py`. In this case, the DAG file is not properly synchronized to Airflow components.

Solution: Remove the folder that has the same name as the DAG Python file.

  * One of the objects in `/dags` or `/plugins` folders contains a `/` symbol at the end of the object's name. Such objects can interfere with the synchronization process because the `/` symbol means that an object is a folder, not a file.

Solution: Remove the `/` symbol from the name of the problematic object.

  * Don't store unnecessary files in `/dags` and `/plugins` folders.

Sometimes DAGs and plugins that you implement come with additional files, such as files that store tests for these components. These files are synchronized to workers and schedulers and impact the time needed to copy these files to schedulers, workers and web servers.

Solution: Don't store any additional and unnecessary files in `/dags` and `/plugins` folders.




### Workers and DAG processors generate 'Is a directory' or 'Is a file' errors

This problem happens because objects can have overlapping namespace in Cloud Storage, while at the same time Airflow components of your environment use conventional Linux file systems. In Cloud Storage, it is possible to add both a folder and an object with the same name to a bucket. When the bucket is synchronized to the environment's Airflow components, an error is generated:

  * If the object was synchronized first, then contents of the folder won't be synchronized and the `Is a file` error is generated.
  * If the folder was synchronized first, then the object isn't synchronized and `Is a directory` error is generated.



Example:
    
    
    Done [Errno 21] Is a directory: '/home/airflow/gcs/dags/...'
    

Both of these errors can lead to task failures because of missing files. In some cases, the synchronization process can be disrupted and other objects in the environment's bucket won't be synchronized as well.

**Solution** :

To fix this problem, make sure that there are no overlapping namespaces in the environment's bucket.

For example, if both `/dags/misc` (an object) and `/dags/misc/example_file.txt` (another object) are in a bucket, rename either the `misc` object or the folder where `example_file.txt` is located, so that there's no overlap.

## What's next

  * [Troubleshooting DAG Processor issues](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-dag-processor#inspect-dag-processor-logs)
  * [Troubleshooting Airflow scheduler issues](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-scheduling)
  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-dags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
