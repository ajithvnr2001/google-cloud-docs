---
url: https://docs.cloud.google.com/storage/docs/wildcards/
title: URI wildcards \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:43.175602+00:00
---

# URI wildcards  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/wildcards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  URI wildcards Stay organized with collections  Save and categorize content based on your preferences. 

The [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/storage) supports the use of URI wildcards for files, buckets, and objects. Wildcards allow you to efficiently work with groups of files that match specified naming patterns. This page describes the wildcards that are supported and notes important considerations when using wildcards in commands.

**Note:** You cannot use the gcloud CLI to perform operations on folders that have wildcards in the folder's name. For example, you cannot use the gcloud CLI to list objects in the folder `gs://my-bucket/*my-folder/`, which contains the `*` wildcard. Instead, use the Google Cloud console.

## Wildcard characters

The gcloud CLI supports the following wildcards:

Character | Description  
---|---  
`*` | Match zero or more characters within the current directory level. For example, `cp gs://my-bucket/abc/d*` matches the object `abc/def.txt` but not the object `abc/def/g.txt`. In the case of listing commands such as `ls`, if a trailing `*` matches a sub-directory in the current directory level, the contents of the sub-directory are also listed.  
`**` | Match zero or more characters across directory boundaries. When used as part of a local file path, the `**` wildcard should always be immediately preceded by a directory delimiter. For example, `my-directory/**.txt` is valid, but `my-directory/abc**` is not.**Note** : Some command shells expand wildcard matches prior to running the command; however, most shells do not support recursive wildcards (`**`). You can skip command shell wildcard expansion and instead use gcloud CLI wildcarding support in such shells by single-quoting (on Linux) or double-quoting (on Windows) the argument. For example: `gcloud storage cp 'data/**' gs://bucket`  
`?` | Match a single character. For example `gs://bucket/??.txt` only matches objects with exactly two characters followed by `.txt`.  
`[CHARACTERS]` | Match any of the specified characters. For example, `gs://bucket/[aeiou].txt` matches objects that contain a single vowel character followed by `.txt`.  
`[CHARACTER_RANGE]` | Match any of the range of characters. For example, `gs://bucket/[a-e].txt` matches objects that contain the letter a, b, c, d, or e followed by `.txt`.  
  
You can combine wildcards to provide more powerful matches, for example:
    
    
    gs://*/[a-m]??.j*g

Note that unless your command includes a flag to return [noncurrent object versions](https://docs.cloud.google.com/storage/docs/object-versioning) in the results, these wildcards only match live object versions.

The gcloud CLI supports the same wildcards for both object and file names. Thus, for example:
    
    
    gcloud storage cp data/abc* gs://bucket

matches all files that start with `abc` in the `data` directory of the local file system.

## Behavior considerations

There are several cases where using wildcards can result in surprising behavior:

  * When using wildcards in bucket names, matches are limited to buckets in a single [project](https://docs.cloud.google.com/storage/docs/projects). Many commands allow you to specify a project using a flag. If a command does not include a project flag or does not support the use of a project flag, matches are limited to buckets in the default project.

  * Shells (like bash and zsh) can attempt to expand wildcards before passing the arguments to the gcloud CLI. If the wildcard was supposed to refer to a cloud object, this can result in surprising "Not found" errors. For example, the shell might try to expand the wildcard `gs://my-bucket/*` on the local machine, which would match no local files, causing the command to fail.

Additionally, some shells include other characters in their wildcard character sets. For example, if you use zsh with the extendedglob option enabled, it treats `#` as a special character, which conflicts with that character's use in referencing versioned objects (see [Restore noncurrent object versions](https://docs.cloud.google.com/storage/docs/using-versioned-objects#restore) for an example).

To avoid these problems, surround the wildcarded expression with single quotes (on Linux) or double quotes (on Windows).

  * Attempting to specify a filename that contains wildcard characters won't work, because the command line tools try to expand the wildcard characters rather than using them as literal characters. For example, running the command:
        
        gcloud storage cp './file[1]' gs://my-bucket

never copies a local file named `file[1]`. Instead, the gcloud CLI always treat the `[1]` as a wildcard.

The gcloud CLI does not support a "raw" mode that allows it to work with file names that contain wildcard characters. For such files, you should either use a different tool such as the Google Cloud console or use a wildcard to capture the files. For example, to capture a file named `file[1]`, you could use the following command:
        
        gcloud storage cp './file*1*' gs://my-bucket

  * Per standard Unix behavior, the wildcard `*` only matches files that don't start with a `.` character (to avoid confusion with the `.` and `..` directories present in all Unix directories). The gcloud CLI provides this same behavior when using wildcards over a file system URI, but does not provide this behavior over cloud URIs. For example, the following command copies all objects from `gs://bucket1` to `gs://bucket2`:
        
        gcloud storage cp gs://bucket1/* gs://bucket2

However, the following command copies only files that don't start with a `.` from the directory `dir` to `gs://bucket1`:
        
        gcloud storage cp dir/* gs://bucket1




## Efficiency considerations

  * It is more efficient, faster, and less network traffic-intensive to use wildcards that have a non-wildcard object-name prefix, such as:
        
        gs://bucket/abc*.txt

than it is to use wildcards as the first part of the object name, such as:
        
        gs://bucket/*abc.txt

This is because the request for `gs://bucket/abc*.txt` asks the server to send back the subset of results whose object name start with `abc` at the bucket root, and then filters the result list for objects whose name ends with `.txt`. In contrast, `gs://bucket/*abc.txt` asks the server for the complete list of objects in the bucket root, and then filters for those objects whose name ends with `abc.txt`. This efficiency consideration becomes increasingly noticeable when you use buckets containing thousands or more objects. It is sometimes possible to set up the names of your objects to fit with expected wildcard matching patterns to take advantage of the efficiency of doing server-side prefix requests.

  * Suppose you have a bucket with these objects:
        
        gs://bucket/obj1
        gs://bucket/obj2
        gs://bucket/obj3
        gs://bucket/obj4
        gs://bucket/dir1/obj5
        gs://bucket/dir2/obj6

If you run the command:
        
        gcloud storage ls gs://bucket/*/obj5

`gcloud storage` performs a `/`-delimited top-level bucket listing and then one bucket listing for each subdirectory, for a total of 3 bucket listings:
        
        GET /bucket/?delimiter=/
        GET /bucket/?prefix=dir1/obj5&delimiter=/
        GET /bucket/?prefix=dir2/obj5&delimiter=/
        

The more bucket listings your wildcard requires, the slower and more expensive it becomes. The number of bucket listings required grows as:

    * the number of wildcard components (e.g., `gs://bucket/a??b/c*/*/d` has 3 wildcard components);

    * the number of subdirectories that match each component; and

    * the number of results (pagination is implemented when the number of results is too large, specifying markers for each).

If you want to use a mid-path wildcard, you might try instead using a recursive wildcard, for example:
    
    gcloud storage ls gs://bucket/**/obj5

This matches more objects than `gs://bucket/*/obj5` (since it spans directories), but is implemented using a delimiter-less bucket listing request (which means fewer bucket requests, though it lists the entire bucket and filters locally, so that could require a non-trivial amount of network traffic).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
