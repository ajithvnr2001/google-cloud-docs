---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/ingest/how-to-ingest-batch-data/
title: Ingest data in batch \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:01.061091+00:00
---

# Ingest data in batch  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/ingest/how-to-ingest-batch-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Ingest data in batch

Although the main way to ingest data into Manufacturing Data Engine (MDE) is using streaming through Manufacturing Connect edge (MCe) or sending messages to Pub/Sub, it's also possible to ingest files in batch. This is can be useful for reprocessing data or to import data from external systems.

Batch loading works by creating an `IngestionSpecification` using de web interface or the API and then uploading one or more files to a folder in a Cloud Storage bucket setup by MDE, which by default has the name `<project-id>-batch-ingestion`. When a new file is uploaded to this bucket it will be detected by the Cloud Storage Reader Dataflow job, the job will split the file into each individual message and send each one to the input-messages Pub/Sub topic.

## Supported formats

Batch loading supports the following data formats:

  * **JSON** : Newline delimited. Each line will be sent as a new message.
  * **CSV** : With or without headers (can be defined), supports row skipping and different separators. The message is converted to JSON using each header column as key and the corresponding row column as value.
  * **AVRO** : Maps each row from AVRO to JSON.
  * **AVRO_RAW_WRITER** : Reads the unprocessed messages written by the Cloud Storage Writer and writes each message back preserving the Pub/Sub message Id.



## Configuration

In order for the Cloud Storage Reader to process files, it needs a `File Ingestion Specification` that defines what type of file it should expect, its options and which folder it will be uploaded to.

All formats require the following parameters:

  * **name** : Name for the `File Ingestion Specification`.
  * **folderName** : Folder where files for this `File Ingestion Specification` will be uploaded to.
  * **source** : Format to use (`JSON`/`CSV`/`AVRO`/`AVRO_RAW_WRITER`).



In addition, CSV source supports the following:

  * **separator** : Separator to use (`,` is used if none is provided).
  * **skip_rows** : Whether to skip any rows before starting reading the CSV file.
  * **headers** : 
    * **infer_headers** : If the heathers should be inferred by the first row read.
    * **headerNames** : Provide an ordered list of header names to use.
  * **insert_metadata** : Whether to include metadata related to the file ingested (`filePath`, `fileName`, `ingestionName`). These are added as additional key value pairs to the sent message.

**Important:** When ingesting CSV data, all columns will be passed as string, so it's important to parse them in Whistle if they need to be a different type.

## Example configurations

This section contains some example configurations for batch loading.

### Ingest newline JSON delimited files

### REST

`POST configuration/v1/ingestions`
    
    
    {
      "name": "json-simple",
      "source": "JSON",
      "folderName": "jsonFiles"
    }
    

### Console

  1. Access the configuration of **File Ingestion Specification**.
  2. Open the section **FILE INGESTION** in the Top menu of the **'Cloud Management'** section.

![File Ingestion - List file ingestion specifications](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-main.png)

  3. Existing **File Ingestion Specifications** are listed in the **FILE INGESTION** section . They can be modified, enabled, disabled, or deleted using the **'Actions'** icon on the side of each ingestion specification.

![File Ingestion - Action available on ingestion specifications](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-actions.png)

  4. To create a new **File Ingestion Specification** click **'ADD NEW INGESTION SPECIFICATION'**. A new side menu will be displayed on the right of the screen containing all necessary parameters to define the new **File Ingestion Specification** :

![File Ingestion - New file ingestion specification](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-new.png)

  5. To create a new **newline JSON delimited files** ingestion specification select **JSON** from the **'Source Type'** menu and provide the two required parameters, in this example:

     * **name** : Name for the File Ingestion Specification.
     * **folderName** : Folder where files for this File Ingestion Specification will be uploaded to.

![File Ingestion - New JSON file ingestion specification](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-json.png)

  6. After the parameters are completed click **'CREATE'**. If the new file ingestion specification has been created successfully a confirmation message will appear.




### Ingest AVRO files

### REST

`POST configuration/v1/ingestions`
    
    
    {
      "name": "avro-simple",
      "source": "AVRO",
      "folderName": "avroFiles"
    }
    

### Console

  1. Access the configuration of **File Ingestion Specification**.
  2. Open the section **FILE INGESTION** in the Top menu of the **'Cloud Management'** section.

![File Ingestion - List file ingestion specifications](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-main.png)

  3. Existing **File Ingestion Specifications** are listed in the **FILE INGESTION** section . They can be modified, enabled, disabled, or deleted using the **'Actions'** icon on the side of each ingestion specification.

![File Ingestion - Action available on ingestion specifications](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-actions.png)

  4. To create a new **File Ingestion Specification** click **ADD NEW INGESTION SPECIFICATION**.

  5. A new side menu will be displayed on the right of the screen containing all necessary parameters to define the new **File Ingestion Specification** :

![File Ingestion - New file ingestion specification](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-new.png)

  6. To create a new **AVRO File** ingestion specification select **AVRO** from the **'Source Type'** menu.

  7. Provide the two required parameters, in this example:

     * **name** : Name for the File Ingestion Specification.
     * **folderName** : Folder where files for this File Ingestion Specification will be uploaded to.

![File Ingestion - New AVRO file ingestion specification](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-avro.png)

  8. After the parameters are completed click **'CREATE'**. If the new file ingestion specification has been created successfully a confirmation message will appear.




### Ingest CSV files inferring column names from headers

### REST

`POST configuration/v1/ingestions`
    
    
    {
      "name": "csv-simple",
      "source": "CSV",
      "folderName": "csv-simple",
      "separator": ",",
      "headers": {
        "inferHeaders": true
      }
    }
    

### Console

  1. Navigate to the **Manufacturing Connect web interface**.
  2. Access the configuration of **File Ingestion Specification**.
  3. Open the section **FILE INGESTION** in the Top menu of the **'Cloud Management'** section.

![File Ingestion - List file ingestion specifications](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-main.png)

  4. Existing **File Ingestion Specifications** are listed in the **FILE INGESTION** section . They can be modified, enabled, disabled, or deleted using the **'Actions'** icon on the side of each ingestion specification.

![File Ingestion - Action available on ingestion specifications](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-actions.png)

  5. To create a new **File Ingestion Specification** click **ADD NEW INGESTION SPECIFICATION**.

  6. A new side menu will be displayed on the right of the screen containing all necessary parameters to define the new **File Ingestion Specification** :

![File Ingestion - New file ingestion specification](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-new.png)

  7. To create a new **File Ingestion Specification** click the **'ADD NEW INGESTION SPECIFICATION'**.

  8. A new side menu will be displayed on the right of the screen containing all necessary parameters to define.

**File Ingestion Specification** :

![File Ingestion - New file ingestion specification](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-new.png)

  9. To create a new **CSV files inferring column names from headers** ingestion specification select **CSV** from the **'Source Type'** menu and provide the seven required parameters, in this example:

     * **name** : Name for the File Ingestion Specification.
     * **folderName** : Folder where files for this File Ingestion Specification will be uploaded to.
     * **separator** : Separator to use (`,` is used if none is provided).
     * **skip_rows** : Whether to skip any rows before starting reading the CSV file.
     * **headers** :
     * **infer_headers** : If the heathers should be inferred by the first row read. Select **'YES'** to infer column names from headers.
     * **insert_metadata** : Whether to include metadata related to the file ingested (filePath, fileName, ingestionName).

![File Ingestion - New CSV file ingestion specification](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-csv-simple.png)

  10. After the parameters are completed click **'CREATE'**.

  11. If the new file ingestion specification has been created successfully a confirmation message will appear.




### Ingest CSV files providing column names and adding ingestion metadata

### REST

`POST configuration/v1/ingestions`
    
    
    {
      "name": "csv-headers-metadata",
      "source": "CSV",
      "folderName": "csv-headers",
      "separator": ",",
      "insertMetadata": true,
      "headers": {
        "headerNames": {
          "names": ["one", "two", "three"]
        }
      }
    }
    

### Console

  1. Access the configuration of **File Ingestion Specification**.
  2. Open the section **FILE INGESTION** in the Top menu of the **'Cloud Management'** section.

![File Ingestion - List file ingestion specifications](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-main.png)

  3. Existing **File Ingestion Specifications** are listed in the **FILE INGESTION** section . They can be modified, enabled, disabled, or deleted using the **'Actions'** icon on the side of each ingestion specification.

![File Ingestion - Action available on ingestion specifications](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-actions.png)

  4. To create a new **File Ingestion Specification** click **ADD NEW INGESTION SPECIFICATION**.

  5. A new side menu will be displayed on the right of the screen containing all necessary parameters to define the new **File Ingestion Specification** :

![File Ingestion - New file ingestion specification](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-new.png)

  6. To create a new **CSV files providing column names and adding ingestion metadata** ingestion specification, select **CSV** from the **'Source Type'**.

  7. Provide the eight required parameters, in this example:

     * **name** : Name for the File Ingestion Specification.
     * **folderName** : Folder where files for this File Ingestion Specification will be uploaded to.
     * **separator** : Separator to use (`,` is used if none is provided).
     * **skip_rows** : Whether to skip any rows before starting reading the CSV file.
     * **headers** : 
       * **infer_headers** : If the heathers should be inferred by the first row read. Select **'NO'** to not infer column names from headers.
       * **headerNames** : Provide an order list of header names to use.
     * **insert_metadata** : Whether to include metadata related to the file ingested (filePath, fileName, ingestionName).

![File Ingestion - New advanced CSV file ingestion specification](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-csv-complex.png)

  8. After the parameters are completed click **'CREATE'** button. If the new file ingestion specification has been created successfully a confirmation message will appear.




### Ingest CSV files inferring header names and skipping 5 rows before starting reading the file

### REST

`POST configuration/v1/ingestions`
    
    
    {
      "name": "csv-skip-rows",
      "source": "CSV",
      "folderName": "csv-skip",
      "skipRows": 5,
      "separator": ",",
      "headers": {
        "inferHeaders": true
      }
    }
    

### Console

  1. Access the configuration of **File Ingestion Specification**.
  2. Open the section **FILE INGESTION** in the Top menu of the **'Cloud Management'** section.

![File Ingestion - List file ingestion specifications](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-main.png)

  3. Existing **File Ingestion Specifications** are listed in the **FILE INGESTION** section . They can be modified, enabled, disabled, or deleted using the **'Actions'** icon on the side of each ingestion specification.

![File Ingestion - Action available on ingestion specifications](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-actions.png)

  4. To create a new **File Ingestion Specification** click **ADD NEW INGESTION SPECIFICATION**.

  5. A new side menu will be displayed on the right of the screen containing all necessary parameters to define the new **File Ingestion Specification** :

![File Ingestion - New file ingestion specification](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-new.png)

  6. To create a new **CSV files inferring header names and skipping 5 rows** ingestion specification select **CSV** from the **'Source Type'** menu.

  7. Provide the seven required parameters, in this example:

     * **name** : Name for the File Ingestion Specification.
     * **folderName** : Folder where files for this File Ingestion Specification will be uploaded to.
     * **separator** : Separator to use (`,` is used if none is provided).
     * **skip_rows** : Select the number of rows to skip, in this case 5.
     * **headers** : 
       * **infer_headers** : If the heathers should be inferred by the first row read. Select **'YES'** to infer column names from headers.
     * **insert_metadata** : Whether to include metadata related to the file ingested (filePath, fileName, ingestionName).

![File Ingestion - New skip row CSV file ingestion specification](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-csv-skip-rows.png)

  8. After the parameters are completed click **'CREATE'**.

  9. If the new file ingestion specification has been created successfully a confirmation message will appear.




### Ingest AVRO files generated by the Cloud Storage Writer raw path

### REST

`POST configuration/v1/ingestions`
    
    
    {
      "name": "avro-reprocess",
      "source": "AVRO_RAW_WRITER",
      "folderName": "avro-raw"
    }
    

This is particularly useful if you need to reprocess files. You can use the date partition in the raw files folder to only copy the files from the time range needed. For example:
    
    
    gcloud storage cp "gs://<project-id>-raw/v1/dt=2023-06-19/*" \
    gs://<project-id>-batch-ingestion/avro-raw/
    

### Console

  1. Access the configuration of **File Ingestion Specification**.
  2. Open the section **FILE INGESTION** in the Top menu of the **'Cloud Management'** section.

![File Ingestion - List file ingestion specifications](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-main.png)

  3. Existing **File Ingestion Specifications** are listed in the **FILE INGESTION** section . They can be modified, enabled, disabled, or deleted using the **'Actions'** icon on the side of each ingestion specification.

![File Ingestion - Action available on ingestion specifications](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-actions.png)

  4. To create a new **File Ingestion Specification** click **ADD NEW INGESTION SPECIFICATION**.

  5. A new side menu will be displayed on the right of the screen containing all necessary parameters to define the new **File Ingestion Specification** :

![File Ingestion - New file ingestion specification](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-new.png)

  6. To create a new **AVRO files generated by the Cloud Storage Writer raw paths** ingestion specification select **AVRO Raw** from the **'Source Type'** menu and provide the two required parameters, in this example:

     * **name** : Name for the File Ingestion Specification.
     * **folderName** : Folder where files for this File Ingestion Specification will be uploaded to.

![File Ingestion - New AVRO Raw file ingestion specification](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-file-ingestion-avro-raw.png)

  7. After the parameters are completed click **'CREATE'**.

  8. If the new file ingestion specification has been created successfully a confirmation message will appear.




This is particularly useful if you need to reprocess files. You can use the date partition in the raw files folder to only copy the files from the time range needed, for example:
    
    
      gcloud storage cp "gs://<project-id>-raw/v1/dt=2023-06-19/*" \
      gs://<project-id>-batch-ingestion/avro-raw/
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
