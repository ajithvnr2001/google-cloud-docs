---
url: https://docs.cloud.google.com/cluster-director/docs/workloads/mount-buckets/
title: Mount Cloud Storage buckets for specific jobs \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:41:57.962006+00:00
---

# Mount Cloud Storage buckets for specific jobs  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/workloads/mount-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Mount Cloud Storage buckets for specific jobs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to mount Cloud Storage buckets on your cluster for the duration of a job.

You can mount a bucket automatically for the duration of a Slurm job. This action lets you read and write files directly to Cloud Storage without permanently adding storage resources to your cluster. To permanently add storage resources to your cluster, see instead [Modify a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster).

## Before you begin

If you haven't already, then connect to a login node in your cluster. For instructions, see [Connect to a cluster's login node](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster#login).

### Required roles

To get the permissions that you need to mount and use Cloud Storage buckets, ask your administrator to grant you the [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) IAM role on the Compute Engine default service account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to mount and use Cloud Storage buckets. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to mount and use Cloud Storage buckets:

  * To view the details of a file in a Cloud Storage bucket: `storage.objects.get`
  * To view a list of files in a Cloud Storage bucket: `storage.objects.list`
  * To write files in a Cloud Storage bucket: `storage.objects.create`
  * To delete files in a Cloud Storage bucket: `storage.objects.delete`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Mount Cloud Storage buckets for the duration of a job

Cluster Director uses [Slurm Plug-in Architecture for Node and job (K)control (SPANK)](https://slurm.schedmd.com/spank.html) to mount Cloud Storage buckets on your cluster for the duration of a job. This plugin uses [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview) to manage the lifecycle of the mounted buckets, automatically mounting the buckets when the job starts and unmounting them when the job completes.

When you specify a directory on which to mount buckets, consider the following:

  * If the directory doesn't exist, then Slurm automatically creates it.

  * If the directory exists, then it must be empty, you must be the owner of the directory, and the directory must not be the `/home` directory of your cluster.




To mount one or more buckets for the duration of a job, include the `--gcsfuse-mount` flag in the [`salloc`](https://slurm.schedmd.com/salloc.html), [`sbatch`](https://slurm.schedmd.com/sbatch.html), or [`srun` commands](https://slurm.schedmd.com/srun.html). Based on the requirements of your workload, use the following syntax:

Use case | Mounting syntax | Example command  
---|---|---  
Mount a single bucket | `--gcsfuse-mount="BUCKET_NAME:LOCAL_PATH"` | `sbatch --gcsfuse-mount="my-bucket:/data" job.sh`  
Mount a read-only bucket | `--gcsfuse-mount="BUCKET_NAME:LOCAL_PATH:--read-only"` | `srun --gcsfuse-mount="my-bucket:/data:--read-only" hostname`  
Mount multiple buckets | `--gcsfuse-mount="BUCKET_NAME_1:LOCAL_PATH_1;BUCKET_NAME_2:LOCAL_PATH_2"` | `salloc --gcsfuse-mount="bucket-1:/data1;bucket-2:/data2"`  
Mount all buckets in your project | `--gcsfuse-mount=":LOCAL_PATH"` | `sbatch --gcsfuse-mount=":/all-data" job.sh`  
  
To customize how Slurm mounts your buckets, you can also specify additional Cloud Storage FUSE options or mount buckets from within a Slurm script.

### Specify additional Cloud Storage FUSE CLI options

To customize how Slurm mounts your Cloud Storage buckets, you can pass optional Cloud Storage FUSE CLI options by including them as a space-separated string after a third colon (`:`) in your command.

For example, to submit a batch job to the queue that includes the `--implicit-dirs` flag and restricts access to a directory named `logs` by using the `--only-dir` flag, run the following command:
    
    
    sbatch --gcsfuse-mount="my-bucket:/mnt/gcs:--implicit-dirs --only-dir logs" job.sh
    

For a complete list of supported options, see [Cloud Storage FUSE CLI options](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options).

### Mount buckets from within a Slurm script

To mount one or more Cloud Storage buckets within a single job, specify your bucket configurations as a semicolon-separated list inside the `#SBATCH --gcsfuse-mount` directive.

**Caution:** In your script, enclose the entire value of the `--gcsfuse-mount` flag in double quotes (`"`). Because standard shells like Bash use the semicolon to separate commands, omitting these quotes causes the shell to truncate your Slurm command and run the remaining configurations as standalone commands.

For example, to mount two buckets on compute nodes by using a Slurm script, complete the following steps:

  1. Create a script as follows:
         
         #!/bin/bash
         #SBATCH --gcsfuse-mount="BUCKET_NAME_1:LOCAL_PATH_1;BUCKET_NAME_2:LOCAL_PATH_2"
         
         # Run your application by using the temporarily mounted directories
         python3 PYTHON_SCRIPT --data_dir LOCAL_PATH_1/INPUT_DIRECTORY --output_dir LOCAL_PATH_2/OUTPUT_DIRECTORY
         

Replace the following:

     * `BUCKET_NAME_1` and `BUCKET_NAME_2`: the names of the two buckets.

     * `LOCAL_PATH_1` and `LOCAL_PATH_2`: the directories on which you want to mount your buckets—for example, `/gcs/data1` and `/gcs/data2`.

     * `PYTHON_SCRIPT`: the name of the Python script that you want to run.

     * `INPUT_DIRECTORY`: the subdirectory in your first bucket that contains your input files—for example, `input`.

     * `OUTPUT_DIRECTORY`: the subdirectory in your second bucket where you want to write files—for example, `output`.

  2. Submit your job to the Slurm queue:
         
         sbatch JOB_SCRIPT
         

Replace `JOB_SCRIPT` with the path to the job script that you created in the previous step.




## What's next

  * Monitor your cluster:

    * [Monitor cluster performance with prebuilt dashboards](https://docs.cloud.google.com/cluster-director/docs/monitor/dashboards)

    * [Monitor clusters with custom dashboards or alerts](https://docs.cloud.google.com/cluster-director/docs/monitor/custom-dashboards)

  * [Manage cluster health](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health)

  * [Troubleshoot cluster errors](https://docs.cloud.google.com/cluster-director/docs/troubleshoot/cluster-errors)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
