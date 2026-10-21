---
url: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/migrate-write-to-destination/
title: Write data to the Firestore database \u00a0|\u00a0 Firestore with MongoDB compatibility \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:24:14.026976+00:00
---

# Write data to the Firestore database  |  Firestore with MongoDB compatibility  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/migrate-write-to-destination/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore with MongoDB compatibility ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Write data to the Firestore database

This page describes the second stage of the [migration process](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/migrate-data) where you set up a Dataflow pipeline and begin a concurrent data move from the Cloud Storage bucket into your destination Firestore with MongoDB compatibility database. This operation will run concurrently with the Datastream stream.

## Start the Dataflow pipeline

The following command starts a new, uniquely named, Dataflow pipeline.

**Note:** The start timestamp of the job is captured in the `DATAFLOW_START_TIME` environment variable. Make a note of this timestamp: it will appear as part of the job name in the Dataflow console. Also note that the Dataflow template does not support wildcard expressions for Cloud Storage paths.

The following formats are acceptable:

  * `inputFilePattern=gs://bucket-name/migration/attempt_1/`
  * `inputFilePattern=gs://bucket-name/migration/`
  * `inputFilePattern=gs://bucket-name/`



Not supported:

  * `inputFilePattern=gs://bucket-name/**/*`


    
    
    DATAFLOW_START_TIME="$(date +'%Y%m%d%H%M%S')"
    
    gcloud dataflow flex-template run "dataflow-mongodb-to-firestore-$DATAFLOW_START_TIME" \
    --template-file-gcs-location gs://dataflow-templates-us-central1/latest/flex/Cloud_Datastream_MongoDB_to_Firestore \
    --region $LOCATION \
    --num-workers $NUM_WORKERS \
    --temp-location $TEMP_OUTPUT_LOCATION \
    --additional-user-labels "" \
    --parameters inputFilePattern=$INPUT_FILE_LOCATION,\
    inputFileFormat=avro,\
    fileReadConcurrency=10,\
    connectionUri=$FIRESTORE_CONNECTION_URI,\
    databaseName=$FIRESTORE_DATABASE_NAME,\
    shadowCollectionPrefix=shadow_,\
    batchSize=500,\
    deadLetterQueueDirectory=$DLQ_LOCATION,\
    dlqRetryMinutes=10,\
    dlqMaxRetryCount=500,\
    processBackfillFirst=false,\
    useShadowTablesForBackfill=true,\
    runMode=regular,\
    directoryWatchDurationInMinutes=20,\
    streamName=$DATASTREAM_NAME,\
    stagingLocation=$STAGING_LOCATION,\
    autoscalingAlgorithm=THROUGHPUT_BASED,\
    maxNumWorkers=$MAX_WORKERS,\
    workerMachineType=$WORKER_TYPE
    

**Note:** To ensure correct sequencing of document updates and deletions, the Dataflow job creates shadow collections in your destination database. For example, if your source database contains a collection named `users`, the destination Firestore database will have both `shadow_users` and `users` collections after the migration completes. You can delete the contents of the shadow collection after migrating. The naming prefix for the shadow collection is controlled by the `shadowCollectionPrefix` Dataflow template parameter.

For more information about monitoring the Dataflow pipeline, see [Troubleshooting](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/migrate-troubleshooting).

## What's next

Proceed to [Migrate traffic to Firestore](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/migrate-traffic).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
