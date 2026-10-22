---
url: https://docs.cloud.google.com/storage/docs/boto-gsutil/
title: Boto configuration file \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:32.145309+00:00
---

# Boto configuration file  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/boto-gsutil/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Boto configuration file Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** gsutil is not the recommended CLI for Cloud Storage. [Use `gcloud storage`](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud) commands in the Google Cloud CLI instead.

This page describes how gsutil uses a boto configuration file and provides a collaboration example that uses the file. The boto configuration file is also used by boto, which is the Amazon S3 SDK for Python.

**Note:** boto3 is not supported with gsutil.

## Configuration file overview

The boto configuration file contains values that control how gsutil behaves. For example, the `prefer_api` variable determines which API gsutil preferentially uses. Boto configuration file variables can be changed by editing the configuration file directly. While most users won't need to edit these variables, those who do typically do so for one of the following reasons:

  * Setting up gsutil to work through a proxy.
  * Using [customer-managed or customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption).
  * Performing specialized customization of global gsutil behavior.



### Location

The default location for the boto configuration file is in the user home directory, ~/.boto, for Linux and macOS, and in %HOMEDRIVE%%HOMEPATH%, for Windows. You can get the location of the configuration file by running the command `gsutil version -l`.

You can override where gsutil expects to find the config file by setting the `BOTO_CONFIG` environment variable. You can also set up a path of boto configuration files to load by setting the `BOTO_PATH` environment variable using a `:` delimited path (or `;` for Windows). For example, setting the `BOTO_PATH` environment variable to:
    
    
    /etc/projects/my_group_project.boto.cfg:/home/mylogin/.boto

causes gsutil to load each configuration file found in the path in order. This is useful if you want to set up some shared configuration state among many users. See the example of using the configuration file for such a data sharing and collaboration scenario.

### Structure

The configuration file contains a number of sections: `[Credentials]`, `[Boto]`, `[GSUtil]`, and `[OAuth2]`. The following are the configuration settings, broken down by section. Their use is documented in the boto configuration file itself, in comments preceding each setting:
    
    
    [Credentials]
      aws_access_key_id
      aws_secret_access_key
      gs_access_key_id
      gs_host
      gs_host_header
      gs_json_host
      gs_json_host_header
      gs_json_port
      gs_oauth2_refresh_token
      gs_port
      gs_secret_access_key
      gs_service_client_id
      gs_service_key_file
      gs_service_key_file_password
      s3_host
      s3_host_header
      s3_port
    
    [Boto]
      proxy
      proxy_type
      proxy_port
      proxy_user
      proxy_pass
      proxy_rdns
      http_socket_timeout
      ca_certificates_file
      https_validate_certificates
      debug
      max_retry_delay
      num_retries
    
    [GoogleCompute]
      service_account
    
    [GSUtil]
      check_hashes
      content_language
      decryption_key1 ... 100
      default_api_version
      disable_analytics_prompt
      encryption_key
      json_api_version
      max_upload_compression_buffer_size
      parallel_composite_upload_component_size
      parallel_composite_upload_threshold
      sliced_object_download_component_size
      sliced_object_download_max_components
      sliced_object_download_threshold
      parallel_process_count
      parallel_thread_count
      gzip_compression_level
      prefer_api
      resumable_threshold
      resumable_tracker_dir (deprecated in 4.6, use state_dir)
      rsync_buffer_lines
      software_update_check_period
      state_dir
      tab_completion_time_logs
      tab_completion_timeout
      task_estimation_threshold
      test_cmd_regional_bucket_location
      test_notification_url
      use_magicfile
      test_hmac_service_account
      test_hmac_alt_service_account
      test_hmac_list_service_account
    
    [OAuth2]
      client_id
      client_secret
      oauth2_refresh_retries
      provider_authorization_uri
      provider_label
      provider_token_uri
      token_cache
    

When you edit the file, be careful not to mis-edit any of the setting names, such as `gs_access_key_id`, and don't remove the section delimiters, such as `[Credentials]`.

### Updating to the latest configuration file

New configuration controllable features are added to the boto configuration file over time, but most gsutil users create a configuration file once and then keep it for a long time. This means that new features aren't apparent when you update to a newer version of gsutil. If you want to get the latest configuration file, which includes the latest settings and documentation, rename your current file (e.g., to `.boto_old`), run `gcloud init` (or if using a legacy stand-alone version of gustil, `gsutil config` with the `-a` or `-e` flags), and then transfer any configuration settings you want to keep from your old file into the newly created file. Note, however, that if you're using OAuth2 credentials and you go back through the OAuth2 configuration process, doing so invalidates your previous OAuth2 credentials.

## Example using the configuration file

In this example, a small company wants to use Cloud Storage as a storage system for their employees. As the IT administrator, you create a project in the Google Cloud console and create buckets for each employee. To make it easier for employees to use Cloud Storage, you want to create and store company-wide settings, such as a proxy configuration and parallel composite upload thresholds, in a central file that employees can point to in their BOTO configuration path. This eliminates the need for each employee to set the shared parts of the configuration manually and allows you, as the administrator, to easily change these shared configurations if necessary.

To accomplish this, perform the following steps:

  1. **Create a central boto configuration file that is readable by all employees.**

The boto configuration file might contain, for example:
         
         [Boto]
         proxy = yourproxy.com
         proxy_port = 8080
         proxy_type = http
          
         [GSUtil]
         parallel_composite_upload_threshold = 150M
         

**Note:** `socks4` and `socks5` proxies are also supported for `proxy_type`.
  2. **Instruct employees to[install](https://docs.cloud.google.com/storage/docs/gsutil_install) and authenticate gsutil.**

During installation, employees need to specify the project ID that the company is using as well as generate individual authentication credentials because you should never share authentication credentials centrally.

  3. **Instruct employees to add a BOTO_PATH environment variable.**

The BOTO_PATH environment variable lists the path of the centrally located configuration file, followed by the employee's local configuration file. For example, if the central configuration file is located in the directory `centralhub/`, then for user `jane`, the BOTO_PATH environment variable might be:
         
         BOTO_PATH =/centralhub/boto.cfg:home/jane/.boto




When employees run gsutil, they will automatically use the configuration specified in the central boto file. If necessary, the administrator can change the proxy settings, parallel composite upload threshold, and other settings in the central configuration file and have the changes reflected for all employees using the central configuration file.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
