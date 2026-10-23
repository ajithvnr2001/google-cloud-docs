---
url: https://docs.cloud.google.com/storage/docs/objects/
title: About Cloud Storage objects \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:55.806685+00:00
---

# About Cloud Storage objects  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  About Cloud Storage objects Stay organized with collections  Save and categorize content based on your preferences. 

Objects are the individual pieces of data that you store in Cloud Storage buckets. You can upload, organize, and retrieve unstructured data in a variety of formats and sizes.

For a general overview of how Cloud Storage works, see the [Cloud Storage product overview](https://docs.cloud.google.com/storage/docs/introduction).

## Objects

Objects have two components: _object data_ and _object metadata_. Object data is typically a file that you want to store in Cloud Storage and is completely opaque to Cloud Storage. [Object metadata](https://docs.cloud.google.com/storage/docs/metadata) is a collection of name-value pairs that describe various object qualities.

Two important pieces of object metadata common to all objects are the object's _name_ and its [_generation number_](https://docs.cloud.google.com/storage/docs/metadata#generation-number). When you add an object to a Cloud Storage bucket, you specify the object name and Cloud Storage assigns the generation number. Together, the name and generation uniquely identify the object within that bucket.

There is no limit on the number of objects that you can create in a bucket.

You can use [Identity and Access Management (IAM)](https://docs.cloud.google.com/storage/docs/access-control/iam) to control access to all of the objects within a bucket or a managed folder. You can also use [access control lists (ACLs)](https://docs.cloud.google.com/storage/docs/access-control/lists) to control access to individual objects.

### Naming considerations

When naming objects in Cloud Storage, it's essential to adhere to specific requirements to ensure compatibility and prevent errors. These requirements apply to both flat namespace buckets and hierarchical namespace enabled buckets.

#### General requirements

  * Object names can contain any sequence of valid Unicode characters.
  * Object names cannot contain [Carriage Return or Line Feed characters](https://en.wikipedia.org/wiki/Newline#Unicode). 
    * Note, backslashes sent through interfaces such as the gcloud CLI and Google Cloud console are escaped under the hood. For example, `\n` becomes `\\n`. The Carriage Return and Line Feed restriction refers strictly to ANSI escape characters.
  * Object names cannot start with `.well-known/acme-challenge/`.
  * Objects cannot be named `.` or `..`.



#### Namespace-specific object size limits

The maximum size of an object name varies depending on the namespace of the bucket:

  * **Object name size in a flat namespace bucket** : 1-1024 bytes when UTF-8 encoded.
  * **Object name size in buckets enabled with[Hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview)**: Object names in buckets with hierarchical namespace enabled are divided into two parts: the folder name segment and the base name segment.

    * **Folder name segment** : The segment of an object's path that defines the folder(s) in which the object resides. The maximum size of the folder name segment is 512 bytes when UTF-8 encoded.
    * **Base name segment** : The segment of an object's path that defines the file itself, separate from any parent folders it resides in. The maximum size of the base name segment is 512 bytes when UTF-8 encoded.

For example, in the object path `my-folder-1/my-folder-2/my-object.txt`, the folder name segment is `my-folder-1/my-folder-2/` and the base name segment is `my-object.txt`.




#### Recommendations

It is strongly recommended that you avoid the following in your object names:

  * [Control characters](http://www.w3.org/TR/xml/#charsets) that are illegal in XML 1.0 (#x7F–#x84 and #x86–#x9F). These characters cause XML listing issues when you try to list your objects.
  * The `#` character. Google Cloud CLI commands interpret object names ending with `#NUMERIC_STRING` as [version identifiers](https://docs.cloud.google.com/storage/docs/using-versioned-objects#access), so including `#` in object names can make it difficult or impossible to perform operations on such versioned objects using the gcloud CLI.
  * The `[`, `]`, `*`, or `?` characters. Google Cloud CLI commands interpret these characters as wildcards, so including them in object names can make it difficult or impossible to perform [wildcard operations](https://docs.cloud.google.com/storage/docs/wildcards). Additionally, `*` and `?` are not valid characters for file names in Windows.
  * The `:`, `"`, `<`, `>`, or `|` characters. These are not valid characters for file names in Windows, so attempts to download an object that uses such characters in its name to a Windows file fail unless the download method includes renaming the resulting Windows file. The `/` character, while also not a valid character for file names in Windows, is typically OK to use in object names for mimicking a directory structure; tools such as the Google Cloud CLI automatically convert the character to `\` when downloading to a Windows environment.
  * The character sequences `./` and `../`. These character sequences create simulated folders using single or double periods for the folder name, such as `folder/./object.txt` or `folder/../object.txt`. However, when you download a folder, client libraries and the gcloud CLI interpret period-only path segments as relative file paths. This behavior means that objects might be overwritten or fail to download. 
    * A single period in the path segment is interpreted as the current directory. For example, say you download the objects `my-object.txt` and `./my-object.txt` to the same destination. The first object is downloaded to `/destination-directory/my-object.txt`. The `.` reference on the second object is resolved and the effective path changes from `/destination-directory/./my-object.txt` to `/destination-directory/my-object.txt`, overwriting the other object that already exists at the same path.
    * A double period in the path segment is interpreted as the parent directory. If the final path of a downloaded object is outside the destination directory, the object isn't downloaded. The objects that fail to download are returned in the response to a download directory request.
  * Sensitive or personally identifiable information (PII). Object names are more broadly visible than object data. For example, object names appear in URLs for the object and when listing objects in a bucket.



Existing objects cannot be directly renamed, but you can [indirectly rename an object](https://docs.cloud.google.com/storage/docs/copying-renaming-moving-objects) by copying and deleting the original object.

## Object namespace

You can store objects in the following namespaces:

  * Flat namespace
  * Hierarchical namespace



### Flat namespace

Buckets that are configured to store objects in a flat namespace always create objects directly under the bucket. In such flat namespace buckets, there is no hierarchy within the bucket, and there are no directories or folders that objects exist within.

For convenience, there are several ways that objects in flat namespace buckets are treated _as if_ they were stored in a folder hierarchy:

  * [Managed folders](https://docs.cloud.google.com/storage/docs/managed-folders) are a Cloud Storage resource that provides expanded access to groups of objects with a shared name prefix.

  * Tools such as the [Google Cloud console](https://console.cloud.google.com/) and the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) interpret the slash (`/`) character in an object's name as a delimiter, in order to simulate folders in buckets that use a flat namespace for objects.




For example, if you create an object named `folder1/file.txt` in the bucket `your-bucket`, the path to the object is `your-bucket/folder1/file.txt`, and Cloud Storage has no folder named `folder1` stored within it. From the perspective of Cloud Storage, the string `folder1/` is part of the object's name.

However, because the object has a `/` in its name, some tools implement the appearance of folders. For example, when using the Google Cloud console, you would navigate to the object `folder1/file1.txt` _as if_ it were an object named `file1.txt` in a folder named `folder1`. Similarly, you could create a [managed folder](https://docs.cloud.google.com/storage/docs/managed-folders) named `folder1`, and then `file1.txt` would be subject to the access policy set by this managed folder.

Note that because objects reside in a flat namespace, deeply nested, directory-like structures don't have the performance that a native filesystem has when listing deeply nested sub-directories.

See [Request rate best practices](https://docs.cloud.google.com/storage/docs/request-rate#naming-convention) for recommendations on how to optimize performance by avoiding sequential names during large-scale uploads. Objects uploaded with sequential names are likely to reach the same backend server and constrain performance.

#### Simulated folders

In order to help you organize objects in your Cloud Storage buckets, some tools simulate folders, and both the JSON and XML APIs have capabilities that let you design your own naming scheme to simulate folders. Click the following tabs to see how different tools handle simulated folders.

### Console

The Google Cloud console creates a visual representation of folders that resembles a local file browser.

In the Google Cloud console, you can create an empty folder in a bucket, or upload an existing folder.

When you upload an existing folder, the name of the folder becomes part of the path for all the objects contained in the folder. Any subfolders and the objects they contain are also included in the upload.

To create a folder:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Navigate to the bucket.

  3. Click **Create folder** to create an empty new folder, or **Upload folder** to upload an existing folder.




### Command line

Cloud Storage CLIs simulate the typical command-line directory experience using a variety of rules.

To achieve the illusion of a hierarchical file tree, the gcloud CLI applies the following rules to determine whether the destination URL in a command should be treated as an object name or a folder:

  1. If the destination URL ends with a `/` character, gcloud CLI commands treat the destination URL as a folder. For example, consider the following command, where `your-file` is the name of a file:
         
         gcloud storage cp your-file gs://your-bucket/abc/

As a result of this command, Cloud Storage creates an object named `abc/your-file` in the bucket `your-bucket`.

  2. If you copy multiple source files to a destination URL, either by using the `--recursive` flag or a [wildcard](https://docs.cloud.google.com/storage/docs/wildcards) such as `**`, the gcloud CLI treats the destination URL as a folder. For example, consider the following command where `top-dir` is a folder containing files such as `file1` and `file2`:
         
         gcloud storage cp top-dir gs://your-bucket/abc --recursive

As a result of this command, Cloud Storage creates the objects `abc/top-dir/file1` and `abc/top-dir/file2` in the bucket `your-bucket`.

  3. If neither of these rules apply, the gcloud CLI checks the objects in the bucket to determine if the destination URL is an object name or a folder. For example, consider the following command where `your-file` is the name of a file:
         
         gcloud storage cp your-file gs://your-bucket/abc

The gcloud CLI makes an object listing request for `your-bucket`, using the `/` delimiter and prefix=`abc`, to determine whether there are objects in `your-bucket` whose path starts with `abc/`. If so, the gcloud CLI treats `abc/` as a folder name, and the command creates the object `abc/your-file` in the bucket `your-bucket`. Otherwise, the gcloud CLI creates the object `abc` in `your-bucket`.




This rule-based approach differs from the way many tools work, which create 0-byte objects to mark the existence of folders. The gcloud CLI understands several conventions used by such tools, such as the convention of adding `_$folder$` to the end of the name of the 0-byte object, but it doesn't require such marker objects to implement naming behavior consistent with UNIX commands.

In addition to these rules, how gcloud CLI treats source files depends on whether or not you use the `--recursive` flag. If you use the flag, the gcloud CLI constructs object names to mirror the source directory structure, starting at the point of recursive processing. For example, consider the following command where `home/top-dir` is a folder containing files such as `file1` and `sub-dir/file2`:
    
    
    gcloud storage cp home/top-dir gs://your-bucket --recursive

As a result of this command, Cloud Storage creates the objects `top-dir/file1` and `top-dir/sub-dir/file2` in the bucket `your-bucket`.

In contrast, copying without the `--recursive` flag, even if multiple files are copied due to the presence of a wildcard such as `**`, results in objects named by the final path component of the source files. For example, assuming again that `home/top-dir` is a folder that contains files such as `file1` and `sub-dir/file2`, then the command:
    
    
    gcloud storage cp home/top-dir/** gs://your-bucket

creates an object named `file1` and an object named `file2` in the bucket `your-bucket`.

#### Retries and naming

When the gcloud CLI [retries an interrupted request](https://docs.cloud.google.com/storage/docs/retry-strategy#tools), you might encounter a problem where the first attempt copies a subset of files, and subsequent attempts encounter an already existing destination folder, which causes your objects to be named incorrectly.

For example, consider the following command, where there are subfolders under `your-dir/` such as `dir1` and `dir2`, and both subfolders contain the file `abc`:
    
    
    gcloud storage cp ./your-dir gs://your-bucket/new --recursive

If the path `gs://your-bucket/new` doesn't exist yet, the gcloud CLI creates the following objects on the first successful attempt:
    
    
    new/dir1/abc
    new/dir2/abc

However, on the next successful attempt of the same command, the gcloud CLI creates the following objects:
    
    
    new/your-dir/dir1/abc
    new/your-dir/dir2/abc

To make the gcloud CLI work consistently on every attempt, try the following:

  1. Add a slash to the end of the destination URL so the gcloud CLI always treats it as a folder.

  2. Use [`gcloud storage rsync`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rsync). Since `rsync` doesn't use the Unix cp-defined folder naming rules, it works consistently whether the destination subfolder exists or not.




#### Additional notes

  * You cannot create a zero-byte object to mimic an empty folder using the gcloud CLI.

  * When downloading to a local file system, gcloud CLI skips objects whose name end with a `/` character, because creating a file that ends with a `/` is not allowed on Linux and macOS.

  * If you use scripts to build file paths by combining subpaths, note that because `/` is just a character that happens to be in the name of the object, the CLIs interpret `gs://your-bucket/folder/` to be a different object from `gs://your-bucket/folder`.




### REST APIs

### JSON API

Folders don't exist in the JSON API. You can narrow down the [objects you list](https://docs.cloud.google.com/storage/docs/listing-objects) and simulate folders by using the `prefix` and `delimiter` [query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list#parameters).

For example, to list all the objects in the bucket `my-bucket` with the prefix `folder/subfolder/`, make an object listing request using this URL:

`"https://storage.googleapis.com/storage/v1/b/my-bucket/o?prefix=folder/subfolder/"`

### XML API

Folders don't exist in the XML API, You can narrow down the [objects you list](https://docs.cloud.google.com/storage/docs/listing-objects) and simulate folders by using the [`prefix`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#prefix) and [`delimiter`](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#delimiter) query parameters.

For example, to list all the objects in the bucket `my-bucket` with the prefix `folder/subfolder/`, make an object listing request using this URL:

`"https://storage.googleapis.com/my-bucket?prefix=folder/subfolder/"`

**Note:** If you create an empty folder using the Google Cloud console, Cloud Storage creates a zero-byte object as a placeholder. For example, if you create a folder called `folder` in a bucket called `my-bucket`, a zero- byte object called `folder/` is created. This placeholder is discoverable by other tools when listing the objects in the bucket, for example when using the `list` method in the JSON API.

#### Removing simulated folders

Because simulated folders don't actually exist, you can typically remove simulated folders by renaming objects so that the simulated folder is no longer a part of the object's name. For example, if you have an object named `folder1/file`, you can remove the simulated folder `folder1/` by renaming the object to just `file`.

However, if you have used a tool that creates zero-byte objects as folder placeholders, such as the Google Cloud console, you must [delete the zero-byte object](https://docs.cloud.google.com/storage/docs/deleting-objects) to remove the folder.

#### Renaming or moving simulated folders

Renaming or moving a simulated folder requires copying and deleting each object within it. If your simulated folder contains many objects, the rename process can be inefficient and costly. Renaming or moving a simulated folder is non-atomic, meaning if the process fails, your bucket might be left in an inconsistent state, with only some objects moved.

### Hierarchical namespace

Hierarchical namespace lets you organize objects within a Cloud Storage bucket in a file system like a hierarchy of [folders](https://docs.cloud.google.com/storage/docs/folders-overview). Hierarchical namespace improves performance and helps you efficiently manage your data. To learn more about hierarchical namespace and when to use it, see [Hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview).

## Object immutability

Objects are immutable, which means that an uploaded object cannot change throughout its storage lifetime. An object's storage lifetime is the time between successful object creation, such as uploading, and successful object deletion. In practice, this means that you cannot make incremental changes to objects, such as append operations or truncate operations. However, it is possible to replace objects that are stored in Cloud Storage, and doing so happens atomically: until the new upload completes, the old version of the object is served to readers, and after the upload completes, the new version of the object is served to readers. A single replacement operation marks the end of one immutable object's lifetime and the beginning of a new immutable object's lifetime.

The [generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number) for an object changes each time you replace the object's data. Thus, the generation number uniquely identifies an immutable object.

Note that there is a once-per-second [limit](https://docs.cloud.google.com/storage/quotas) for rapidly replacing the _same_ object. Replacing the same object more frequently might result in `429 Too Many Requests` errors. You should design your application to upload data for a particular object no more than once per second and handle occasional `429 Too Many Requests` errors using an exponential backoff [retry strategy](https://docs.cloud.google.com/storage/docs/retry-strategy).

## What's next

  * [Upload](https://docs.cloud.google.com/storage/docs/uploading-objects) and [download](https://docs.cloud.google.com/storage/docs/downloading-objects) objects.
  * [Move an existing object](https://docs.cloud.google.com/storage/docs/copying-renaming-moving-objects).
  * Learn about [buckets](https://docs.cloud.google.com/storage/docs/buckets), which are containers for objects.
  * Learn about [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
