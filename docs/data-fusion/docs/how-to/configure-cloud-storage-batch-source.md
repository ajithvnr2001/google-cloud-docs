---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/configure-cloud-storage-batch-source/
title: Cloud Storage batch source \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:17.471358+00:00
---

# Cloud Storage batch source  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/configure-cloud-storage-batch-source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Cloud Storage batch source Stay organized with collections  Save and categorize content based on your preferences. 

This page provides guidance about configuring the Cloud Storage batch source plugin in Cloud Data Fusion. 

The Cloud Storage batch source plugin lets you read data from Cloud Storage buckets and bring it into Cloud Data Fusion for further processing and transformation. It lets you load data from multiple file formats, including the following:

  * **Structured** : CSV, Avro, Parquet, ORC
  * **Semi-structured** : JSON, XML
  * **Others** : Text, Binary



## Before you begin

Cloud Data Fusion typically has two service accounts:

  * Design-time service account: [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/data-fusion/docs/concepts/service-accounts)
  * Execution-time service account: [Compute Engine Service Account ](https://docs.cloud.google.com/data-fusion/docs/concepts/service-accounts)



Before using the Cloud Storage batch source plugin, grant the following role or permissions to each service account.

### Cloud Data Fusion API Service Agent

This service account already has all the required permissions and you don't need to add additional permissions.

**Note:** When you design a pipeline, you need `storage.buckets.list` permission on the bucket used by the pipeline. It isn't required to execute the pipeline.

### Compute Engine Service Account

In your Google Cloud project, grant the following IAM roles or permissions to the Compute Engine Service Account:

  * [Storage Legacy Bucket Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketReader) (`roles/storage.legacyBucketReader`). This predefined role contains the required `storage.buckets.get` permission.
  * [Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.legacyBucketReader`). This predefined role contains the following required permissions:

    * `storage.objects.get`
    * `storage.objects.list`



## Configure the plugin

  1. [Go to the Cloud Data Fusion web interface](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline#navigate-web-interface) and click **Studio**.
  2. Check that **Data Pipeline - Batch** is selected (not **Realtime**).
  3. In the **Source** menu, click **GCS**. The Cloud Storage node appears in your pipeline.
  4. To configure the source, go to the Cloud Storage node and click **Properties**.
  5. Enter the following properties. For a complete list, see Properties.

     1. Enter a **Label** for the Cloud Storage node—for example, `Cloud Storage tables`.
     2. Enter the connection details. You can set up a new, one-time connection, or an existing, reusable connection.

### New connection

To add a one-time connection to Cloud Storage, follow these steps:

        1. Keep **Use connection** turned off.
        2. In the **Project ID** field, leave the value as auto-detect.
        3. In the **Service account type** field, leave the value as **File path** and the **Service account file path** as auto-detect.

**Note:** If the plugin isn't running on a Managed Service for Apache Spark cluster, enter the values for **Service account type** and **Service account file path**. For more information, see Properties.

### Reusable connection

To reuse an existing connection, follow these steps:

        1. Turn on **Use connection**.
        2. Click **Browse connections**.
        3. Click the connection name—for example, **Cloud Storage Default**.

**Note:** For more information about adding, importing, and editing the connections that appear when you browse connections, see [Manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections).
        4. Optional: if a connection doesn't exist and you want to create a new reusable connection, click **Add connection** and refer to the steps in the **New connection** tab on this page.

     3. In the **Reference name** field, enter a name to use for lineage—for example, `data-fusion-gcs-campaign`.

     4. In the **Path** field, enter the path to read from—for example, `gs://BUCKET_PATH`.

     5. In the **Format** field, select one of the following file formats for the data being read:

        * **avro**
        * **blob** (the blob format requires a schema that contains a field named body of type bytes)
        * **csv**
        * **delimited**
        * **json**
        * **parquet**
        * **text** (the text format requires a schema that contains a field named body of type string)
        * **tsv**
        * The name of any format plugin that you have deployed in your environment
**Note:** If you use a macro in this field, you must use one of the predefined formats. Macros don't support formats added by plugins.
     6. Optional: to test connectivity, click **Get schema**.

     7. Optional: in the **Sample size** field, enter the maximum rows to check for the selected data type—for example, `1000`.

     8. Optional: in the **Override** field, enter the column names and their respective data types to skip.

     9. Optional: enter **Advanced properties** , such as a minimum split size or a regular expression path filter (see Properties).

     10. Optional: in the **Temporary bucket name** field, enter a name for the Cloud Storage bucket.

  6. Optional: click **Validate** and address any errors found.

  7. Click **Close**. Properties are saved and you can continue to build your data pipeline in the Cloud Data Fusion Studio.




### Properties

Property | Macro enabled | Required property | Description  
---|---|---|---  
**Label** | No | Yes | The name of the node in your data pipeline.  
**Use connection** | No | No | Browse for a reusable connection to the source. For more information about adding, importing, and editing the connections that appear when you browse connections, see [Manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections).  
**Connection** | Yes | Yes | If **Use connection** is turned on, the name of the reusable connection you select appears in this field.  
**Project ID** | Yes | No | Used only when **Use connection** is turned off. A globally unique identifier for the project.  
Default is `auto-detect`.  
**Service account type** | Yes | No | Select one of the following options:  


  * **File path** : the path where the service account is located.
  * **JSON** : JSON content of the service account.

  
**Service account file path** | Yes | No | Used only when the Service account type value is **File path**. The path on the local file system of the service account key used for authorization. If jobs run on Managed Service for Apache Spark clusters, set the value to auto-detect. If jobs run on other types of clusters, the file must be present on every node in the cluster.  
Default is `auto-detect`.  
**Service account JSON** | Yes | No | Used only when the Service account type value is **JSON**. The JSON file content of the service account.  
**Reference name** | No | Yes | Name that uniquely identifies this source for other services, such as lineage and annotating metadata.  
**Path** | Yes | Yes | Path to the files to be read. If a directory is specified, terminate the path with a backslash (`/`). For example, `gs://bucket/path/to/directory/`. To match a filename pattern, you can use an asterisk (`*`) as a wildcard. If no files are found or matched, the pipeline fails.  
**Format** | No | Yes | Format of the data to read. The format must be one of the following: 

  * **avro**
  * **blob** (the blob format requires a schema that contains a field named body of type bytes)
  * **csv**
  * **delimited**
  * **json**
  * **parquet**
  * **text** (the text format requires a schema that contains a field named body of type string)
  * **tsv**
  * The name of any format plugin that you have deployed in your environment
  * If the format is a macro, only the pre-packaged formats can be used

  
**Sample size** | Yes | No | The maximum number of rows that are investigated for automatic data type detection. Default is **1000**.  
**Override** | Yes | No | A list of columns with the corresponding data from which the automatic data type detection gets skipped.  
**Delimiter** | Yes | No | Delimiter to use when the format is **delimited**. This property is ignored for other formats.  
**Enable quoted values** | Yes | No | Whether to treat content between quotes as a value. This property is only used for the **csv** , **tsv** , or **delimited** formats. For example, if this property is set to true, the following outputs two fields: `1, "a, b, c"`. The first field has `1` as its value. The second has `a, b, c`. The quotation mark characters are trimmed. The newline delimiter cannot be within quotes.  
The plugin assumes the quotes are correctly enclosed, for example, `"a, b, c"`. Not closing a quote (`"a,b,c,`) causes an error.  
Default value is **False**.  
**Use first row as header** | Yes | No | Whether to use the first line of each file as the column header. Supported formats are **text** , **csv** , **tsv** , and **delimited**.  
Default is **False**.  
**Minimum split size** | Yes | No | Minimum size, in bytes, for each input partition. Smaller partitions increase the level of parallelism, but require more resources and overhead.   
If the **Format** value is `blob`, you cannot split the data.  
**Maximum split size** | Yes |  No | Maximum size, in bytes, for each input partition. Smaller partitions increase the level of parallelism, but require more resources and overhead.   
If the **Format** value is `blob`, you cannot split the data.  
Default is **128 MB**.  
**Regex path filter** | Yes | No | Regular expression that file paths must match to be included in the input. The full path is compared, not just the filename. If no file is given, no file filtering is done. For more information about regular expression syntax, see [Pattern](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html).  
**Path field** | Yes | No | Output field to place the path of the file that the record was read from. If not specified, the path isn't included in output records. If specified, the field must exist in the output schema as a string.  
**Path filename only** | Yes | No | If a **Path field** property is set, use only the filename and not the URI of the path.  
Default is **False**.  
**Read files recursively** | Yes | No | Whether files are to be read recursively from the path.  
Default is **False**.  
**Allow empty input** | Yes | No | Whether to allow an input path that contains no data. When set to **False** , the plugin will error when there is no data to read. When set to **True** , no error is thrown and zero records are read.  
Default is **False**.  
**Data file encrypted** | Yes | No | Whether files are encrypted. For more information, see Data file encryption.  
Default is **False**.  
**Encryption metadata file suffix** | Yes | No | The filename suffix for the encryption metadata file.  
Default is **metadata**.  
**File system properties** | Yes |  No | Additional properties to use with the InputFormat when reading the data.  
**File encoding** | Yes | No | The character encoding for the files to be read.  
Default is **UTF-8**.  
**Output schema** | Yes | No | If a **Path field** property is set, it must be present in the schema as a string.  
  
## Data file encryption

This section describes the **Data file encryption** property. If you set it to **true** , files are decrypted using the Streaming AEAD provided by the [Tink library](https://github.com/google/tink). Each data file must be accompanied with a metadata file that contains the cipher information. For example, an encrypted data file at `gs://BUCKET/PATH_TO_DIRECTORY/file1.csv.enc ` must have a metadata file at `gs://BUCKET/ PATH_TO_DIRECTORY/file1.csv.enc.metadata`. The metadata file contains a JSON object with the following properties:

Property | Description  
---|---  
`kms` | The Cloud Key Management Service URI that was used to encrypt the Data Encryption Key.  
`aad` | The Base64 encoded Additional Authenticated Data used in the encryption.  
`key set` | A JSON object representing the serialized keyset information from the Tink library.  
  
**Example**
    
    
        /* Counting example */
        {
    
          "kms": "gcp-kms://projects/my-key-project/locations/us-west1/keyRings/my-key-ring/cryptoKeys/mykey",
    
          "aad": "73iT4SUJBM24umXecCCf3A==",
    
          "keyset": {
    
              "keysetInfo": {
    
                  "primaryKeyId": 602257784,
    
                  "keyInfo": [{
    
                      "typeUrl": "type.googleapis.com/google.crypto.tink.AesGcmHkdfStreamingKey",
    
                      "outputPrefixType": "RAW",
    
                      "keyId": 602257784,
    
                      "status": "ENABLED"
    
                  }]
    
              },
    
              "encryptedKeyset": "CiQAz5HH+nUA0Zuqnz4LCnBEVTHS72s/zwjpcnAMIPGpW6kxLggSrAEAcJKHmXeg8kfJ3GD4GuFeWDZzgGn3tfolk6Yf5d7rxKxDEChIMWJWGhWlDHbBW5B9HqWfKx2nQWSC+zjM8FLefVtPYrdJ8n6Eg8ksAnSyXmhN5LoIj6az3XBugtXvCCotQHrBuyoDY+j5ZH9J4tm/bzrLEjCdWAc+oAlhsUAV77jZhowJr6EBiyVuRVfcwLwiscWkQ9J7jjHc7ih9HKfnqAZmQ6iWP36OMrEn"
    
          }
    
        }
        

## Release notes

  * [September 6, 2023](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1280901131/CDAP+Hub+Release+Log#September-6%2C-2023)



## What's next

  * Learn more about [plugins in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/plugins).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
