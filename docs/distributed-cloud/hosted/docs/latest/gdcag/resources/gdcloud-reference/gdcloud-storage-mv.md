---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-storage-mv/
title: gdcloud storage mv \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:33.493190+00:00
---

# gdcloud storage mv  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-storage-mv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud storage mv Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud storage mv - Move or rename objects.

## SYNOPSIS
    
    
    gdcloud storage mv SOURCE [SOURCE ...] DESTINATION
        [--all-versions, -A]
        [--no-clobber, -n]
        [--continue-on-error, -c]
        [--daisy-chain, -D]
        [--do-not-decompress]
        [--ignore-symlinks]
        [--preserve-posix, -P]
        [--print-created-message],
        [--cache-control=CACHE_CONTROL]
        [--content-disposition=CONTENT_DISPOSITION]
        [--content-encoding=CONTENT_ENCODING]
        [--content-language=CONTENT_LANGUAGE]
        [--content-md5=MD5_DIGEST]
        [--content-type=CONTENT_TYPE]
        [--custom-metadata=[CUSTOM_METADATA,...]]
        [--clear-custom-metadata]
        [--remove-custom-metadata=[CUSTOM_METADATA,...]]
        [--update-custom-metadata=[CUSTOM_METADATA,...]]
        [--format=FORMAT]
        [--log-http]
        [--verbosity=VERBOSITY] [flags]
    

## DESCRIPTION

Move data between your local file system and the cloud, move data within the cloud, and move data between cloud storage providers.

### EXAMPLES
    
    
    To move all objects from a bucket to a local directory, run:
    
        gdcloud storage mv s3://my-bucket/* dir
    
    Similarly, to move all objects from a local directory to a bucket, run:
    
        gdcloud storage mv ./dir s3://my-bucket/
    
    The following command renames all objects under s3://my_bucket/oldprefix
    to be under s3://my_bucket/newprefix, otherwise preserving the naming structure:
    
        gdcloud storage mv s3://my-bucket/oldprefix s3://my-bucket/newprefix
    

### OPTIONAL FLAGS
    
    
      -A, --all-versions                            Copy all source versions from a source bucket or folder. If not set, only
                                                    the live version of each source object is copied. Note: This option is only
                                                    useful when the destination bucket has Object Versioning enabled.
                                                    Additionally, the generation numbers of copied versions do not necessarily
                                                    match the order of the original generation numbers.
          --cache-control string                    How caches should handle requests and responses.
          --clear-custom-metadata                   Clear all custom metadata on objects. When used with --preserve-posix,
                                                    POSIX attributes are still stored in custom metadata.
          --content-disposition string              How content should be displayed.
          --content-encoding string                 How content is encoded (e.g. gzip).
          --content-language string                 Content's language (e.g. "en" signifies "English").
          --content-md5 string                      Manually specified MD5 hash digest for the contents of an uploaded
                                                    file. This flag cannot be used when uploading multiple files.
          --content-type string                     Type of data contained in the object (e.g. text/html).
      -c, --continue-on-error                       If any operations are unsuccessful, the command will exit with a non-zero
                                                    exit status after completing the remaining operations. This flag takes
                                                    effect only in sequential execution mode (i.e. processor and thread count
                                                    are set to 1). Parallelism is default.
          --custom-metadata stringToString          Set custom metadata on objects. When used with --preserve-posix, POSIX
                                                    attributes are also stored in custom metadata. (default [])
      -D, --daisy-chain                             Copy in "daisy chain" mode, which means copying an object by first
                                                    downloading it to the machine where the command is run, then uploading it
                                                    to the destination bucket. The default mode is a "copy in the cloud,"
                                                    where data is copied without uploading or downloading. During a copy in
                                                    the cloud, a source composite object remains composite at its destination.
                                                    However, you can use daisy chain mode to change a composite object into a
                                                    non-composite object.
          --do-not-decompress                       Do not automatically decompress downloaded gzip files.
          --ignore-symlinks                         Ignore file symlinks instead of copying what they point to. Symlinks
                                                    pointing to directories are always ignored.
          --log-http                                Log all HTTP server requests and responses to stderr.
      -n, --no-clobber                              Do not overwrite existing files or objects at the destination. Skipped
                                                    items will be printed. This option performs an additional GET request for
                                                    cloud objects before attempting an upload.
      -P, --preserve-posix                          Preserve POSIX attributes when objects are copied. With this
                                                    feature enabled, gdcloud storage will copy several fields provided by the
                                                    stat command: access time, modification time, owner UID, owner group GID,
                                                    and the mode (permissions) of the file.
                                                    For uploads, these attributes are read off of local files and stored in the
                                                    cloud as custom metadata. For downloads, custom cloud metadata is set as
                                                    POSIX attributes on files after they are downloaded.
          --print-created-message                   Print the version-specific URL for each copied object.
          --remove-custom-metadata stringArray      Remove individual custom metadata keys from objects. This flag can be
                                                    used with --update-custom-metadata. When used with --preserve-posix,
                                                    POSIX attributes specified by this flag are not preserved.
          --update-custom-metadata stringToString   Add or set individual custom metadata key-value pairs on objects.
                                                    Existing custom metadata not specified with this flag is not changed.   This
                                                    flag can be used with --remove-custom-metadata. When keys overlap with
                                                    those provided by --preserve-posix, values specified by this flag are used. (default [])
          --verbosity string                        Override the default verbosity for this command. VERBOSITY must be one of:
                                                    debug, info, warning, error, critical, none. (default "warning")
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
