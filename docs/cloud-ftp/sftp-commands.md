---
url: https://docs.cloud.google.com/cloud-ftp/sftp-commands/
title: Transfer data by using SFTP commands \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:20.586803+00:00
---

# Transfer data by using SFTP commands  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/sftp-commands/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ Guides ](https://docs.cloud.google.com/cloud-ftp/overview)



Send feedback 

#  Transfer data by using SFTP commands Stay organized with collections  Save and categorize content based on your preferences. 

You can upload, download, and manage files in Cloud Storage buckets by using standard SFTP commands. The following table describes the SFTP commands and optional flags that are supported by Cloud FTP.

Command | Description  
---|---  
`cd PATH` | Change directory.  
`get REMOTE_PATH [LOCAL_PATH]` |  Download a file from a bucket. If you omit the `LOCAL_PATH` name, the file is downloaded with the same name as the Cloud Storage file. To recursively download all files from a folder, include the `-R` flag: `get -R REMOTE_PATH`.  
`ls` |  List the files in the current directory. You can refine the list of files by including one or more of the following flags:

  * `-1`: list the files in a single column.
  * `-a`: list all files, including files that start with a dot (`.`).
  * `-f`: don't sort the files. The default sort order is lexicographical.
  * `-h`: when used with the `-l` flag, include unit suffixes for file size.
  * `-l`: include additional file information, like file size and last modified time.
  * `-r`: sort files in reverse order.
  * `-S`: sort files by file size.
  * `-t`: sort files by last modification time.

To list the files within a different directory, include the directory name: `ls PATH`.  
`mkdir PATH` | Create a directory.  
`put LOCAL_PATH [REMOTE_PATH]` |  Upload a local file to a bucket. If you omit the `REMOTE_PATH` name, the file is uploaded to Cloud Storage with the same name as the local file. If a file with this name already exists, the new file overwrites the existing file. To recursively upload all files in a folder, use the `-R` flag: `put -R LOCAL_PATH`.  
`progress` | Toggle the display of the progress meter.  
`pwd` | Display the current remote working directory.  
`rename OLD_PATH NEW_PATH` |  Rename a file. Rename a directory, in buckets that have hierarchical namespace enabled. The file that you're renaming must be in the current directory, and the destination directory must already exist.  
`rm PATH` | Delete a file from a bucket.  
`rmdir PATH` | Delete a directory. You must delete all files from a directory before you can delete the directory.  
`version` | Display the SFTP protocol version.  
`bye`, `exit`, or `quit` | Exit the SFTP session.  
  
## What's next

  * [Connect to an external SFTP server](https://docs.cloud.google.com/cloud-ftp/connect-to-external-server)
  * [Connect to an internal SFTP server](https://docs.cloud.google.com/cloud-ftp/connect-to-internal-server)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
