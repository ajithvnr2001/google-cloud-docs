---
url: https://docs.cloud.google.com/storage/docs/gsutil-transition-to-gcloud/
title: Transition from gsutil to gcloud storage \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:08.466400+00:00
---

# Transition from gsutil to gcloud storage  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/gsutil-transition-to-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Transition from gsutil to gcloud storage Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud CLI is the recommended command-line tool for interacting with Cloud Storage. This page helps you transition from `gsutil` to the gcloud CLI's `gcloud storage` commands by describing the major differences and command mappings between the two tools. If you have scripts that use `gsutil`, you can use the information on this page to update your scripts with the comparable `gcloud storage` commands instead.

To learn how to start using the gcloud CLI, see [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).

For a detailed description of `gcloud storage` commands, see the [`gcloud storage` reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

## Behavioral differences

The following sections describe the behavioral differences between `gsutil` and `gcloud storage`.

### Parallel invocations

`gcloud storage` doesn't support parallel invocations using multiple terminals on the same machine.

### Parallel processing

`gcloud storage` supports parallel processing.

### Wildcard handling

`gcloud storage` simplifies multiple asterisks. If you use three or more asterisks in a row (`***`), it treats them as a single asterisk (`*`).

### Handling of hierarchical namespace buckets

`gcloud storage` can be used to create and manage buckets with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled.

### Support for local-to-local file copying

`gcloud storage` is designed exclusively for interacting with Cloud Storage and doesn't support local-to-local file copying. To move data successfully using `gcloud storage`, at least one argument (source or destination) must be a Cloud Storage resource URI. For example: `gs://my-bucket`.

### Output formatting

The `gcloud storage` and `gsutil` commands format their output differently. While minor changes like logging format might not affect you, more significant differences in error messages and data listings can break automated scripts.

If you have scripts that rely on parsing `gsutil` command output, you should review and update them for the `gcloud storage` format before transitioning them.

## gcloud command equivalents

All existing `gsutil` commands have equivalent commands in `gcloud storage`, with a few exceptions. You can get a full list of the `gcloud storage` commands by visiting the [reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/storage) or by running `gcloud storage --help`. The following table briefly outlines the changes from popular `gsutil` commands.

Operation | gsutil command | gcloud storage command  
---|---|---  
Manage Access Control Lists (ACLs) | 
    
    
    gsutil acl get
    gsutil acl set
    gsutil acl ch
    

| 
    
    
    gcloud storage RESOURCE describe --format="multi(acl:format=json)"
    gcloud storage RESOURCE update --acl-file=ACL_FILE_PATH
    gcloud storage RESOURCE update --add-acl-grant=GRANT
    gcloud storage RESOURCE update --remove-acl-grant=GRANT  
  
Operation | gsutil command | gcloud storage command  
---|---|---  
Concatenate objects and display object content | 
    
    
    gsutil cat

| 
    
    
    gcloud storage cat  
  
Operation | gsutil command | gcloud storage command  
---|---|---  
Concatenate objects by combining them into a new object | 
    
    
    gsutil compose

| 
    
    
    gcloud storage objects compose  
  
###### Notes

To apply [preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions) in `gcloud storage objects compose`, use specific flags, such as `--if-generation-match` or `--if-metageneration-match`.   
Operation | gsutil command | gcloud storage command  
---|---|---  
Copy objects and other resources | 
    
    
    gsutil cp

| 
    
    
    gcloud storage cp  
  
###### Notes

[Simulated folders](https://docs.cloud.google.com/storage/docs/folder-types#simulated-folders) created using the Google Cloud console are recognized as 0-byte placeholder objects. `gcloud storage cp` can be used to copy simulated folders, whereas `gsutil cp` cannot. When handling errors, `gcloud storage cp` attempts to copy all resources, even if one of the resources is invalid or doesn't exist. `gsutil cp` might stop the entire operation as soon as it encounters an invalid resource. When downloading an object, `gcloud storage cp` creates any missing local directories that are specified in the destination path. `gsutil cp` fails if the destination directory doesn't exist.  
Operation | gsutil command | gcloud storage command  
---|---|---  
Display the total disk space used by objects | 
    
    
    gsutil du

| 
    
    
    gcloud storage du  
  
Operation | gsutil command | gcloud storage command  
---|---|---  
Calculate file hashes | 
    
    
    gsutil hash

| 
    
    
    gcloud storage hash  
  
###### Notes

`gsutil hash` uses additive flags to include specific hashes, such as `-c` or `-m`. `gcloud storage hash` uses subtractive flags to exclude hashes, such as `--skip-md5` or `--skip-crc32c`.  
Operation | gsutil command | gcloud storage command  
---|---|---  
Manage bucket labels | 
    
    
    gsutil label get
    gsutil label set
    gsutil label ch
    

| 
    
    
    gcloud storage buckets describe
    gcloud storage buckets update
    gcloud storage buckets update
      
  
###### Notes

The combination of adding, updating, and removing labels in a single `gsutil label ch` command can behave differently than the equivalent operations using `gcloud storage buckets update`. Scripts relying on specific read-modify-write behavior of `gsutil` should be tested carefully after transitioning to `gcloud storage`.  
Operation | gsutil command | gcloud storage command  
---|---|---  
List buckets, objects, and folders | 
    
    
    gsutil ls

| 
    
    
    gcloud storage ls  
  
###### Notes

When a wildcard is used to list objects in a project, `gsutil ls` returns a flat list of objects, whereas `gcloud storage ls` returns objects grouped by bucket name. When using `gcloud storage ls -L` to return detailed listings as output, the following behaviors apply:

  * The labels for each piece of metadata (also known as a "key") has the first letter of each word capitalized.
  * If a piece of metadata for an object doesn't have a value, `gcloud storage` omits that line from the output.

`gcloud storage` always outputs datetimes in UTC. `gcloud storage` returns any error messages at the end of the command's output.  
Operation | gsutil command | gcloud storage command  
---|---|---  
Move and rename objects or directories | 
    
    
    gsutil mv

| 
    
    
    gcloud storage mv  
  
Operation | gsutil command | gcloud storage command  
---|---|---  
Rewrite objects in place | 
    
    
    gsutil rewrite

| 
    
    
    gcloud storage objects update  
  
###### Notes

If an `encryption_key` is set in your boto configuration file, `gsutil rewrite -k` applies the key to the objects. If `encryption_key` isn't set, the equivalent of `gsutil rewrite -k` is `gcloud storage objects update --clear-encryption-key`. This removes any customer-supplied encryption keys (CSEK) or customer-managed encryption keys (CMEK) from the object. The object is then encrypted with the bucket's default KMS key or with Google-managed encryption. `gsutil rewrite` includes logic to skip rewriting an object if the requested transformation wouldn't change its state (for example, if the object is already in a target storage class). `gcloud storage objects update` might not perform the same checks, potentially leading to unnecessary operations.  
Operation | gsutil command | gcloud storage command  
---|---|---  
Remove objects or buckets | 
    
    
    gsutil rm

| 
    
    
    gcloud storage rm  
  
###### Notes

The `gsutil` aliases `del`, `delete`, and `remove` aren't supported. There's a known issue where `gsutil` and `gcloud storage` behave differently when the `-l` and `-r` flags are used together. Scripts that pipe a list of directories to be recursively deleted should be thoroughly tested before transitioning from using `gsutil` to `gcloud storage`.  
Operation | gsutil command | gcloud storage command  
---|---|---  
Synchronize the contents of two buckets or directories | 
    
    
    gsutil rsync

| 
    
    
    gcloud storage rsync  
  
###### Notes

By default, `gsutil rsync` considers an object unchanged if its size and last modification time match between the source and destination. It only performs a more thorough checksum comparison if an object is missing its modification time, or if you manually force it to with the `-c` flag. `gcloud storage rsync` also starts by checking a file's size and last modification time; however, if the object sizes match but the modification times differ or are missing, it automatically performs a checksum comparison. `gcloud storage rsync` performs operations in parallel by default for better performance. `gsutil rsync` runs sequentially unless the top-level `-m` flag is used. `gsutil rsync` follows symbolic links by default. `gcloud storage rsync` ignores them by default unless the `--no-ignore-symlinks` flag is used.  
Operation | gsutil command | gcloud storage command  
---|---|---  
Set metadata on uploaded objects | 
    
    
    gsutil setmeta

| 
    
    
    gcloud storage objects update  
  
###### Notes

`gsutil setmeta` uses a single, repeatable `-h` flag to specify which metadata to set or remove. `gcloud storage objects update` uses distinct flags for each metadata field (for example: `--content-type`, `--clear-cache-control`, or `--update-custom-metadata`).  In `gsutil setmeta`, the `-h` flag is used to set the full header name (for example: `-h "x-goog-meta-icecreamflavor:vanilla"`). In `gcloud storage objects update`, the `--update-custom-metadata` flag is used instead and takes key-value pairs (for example: `--update-custom-metadata=icecreamflavor=vanilla`). To remove a custom metadata field, `gsutil setmeta` uses `-h "x-goog-meta-icecreamflavor"` while `gcloud storage objects update` uses `--remove-custom-metadata=icecreamflavor`.  
Operation | gsutil command | gcloud storage command  
---|---|---  
Display object status | 
    
    
    gsutil stat

| 
    
    
    gcloud storage objects list --stat --fetch-encrypted-object-hashes  
  
###### Notes

The output format of `gcloud storage objects list --stat` differs from the output format of `gsutil stat`, with known issues related to inconsistent spacing. Scripts that were written to parse the output of `gsutil stat` might require adjustments to handle the output format of `gcloud storage objects list --stat`.  
  
## What's next

For more details on command and flag mappings, see the [Migration reference](https://github.com/GoogleCloudPlatform/gsutil/blob/master/GCLOUD-MIGRATION.md) in the `gsutil` GitHub repository.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
