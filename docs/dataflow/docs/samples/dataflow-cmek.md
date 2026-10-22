---
url: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-cmek/
title: Use customer-managed encryption keys \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:39.017905+00:00
---

# Use customer-managed encryption keys  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/samples/dataflow-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Samples ](https://docs.cloud.google.com/dataflow/docs/samples)



#  Use customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

This sample shows how to use encryption keys managed by the customer, with a Dataflow pipeline.

## Code sample

### Java

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Query from the NASA wildfires public dataset:
    // https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=nasa_wildfire&t=past_week&page=table
    String query =
        "SELECT latitude,longitude,acq_date,acq_time,bright_ti4,confidence "
        + "FROM `bigquery-public-data.nasa_wildfire.past_week` "
        + "LIMIT 10";
    
    // Schema for the output BigQuery table.
    final TableSchema outputSchema = new TableSchema().setFields(Arrays.asList(
        new TableFieldSchema().setName("latitude").setType("FLOAT"),
        new TableFieldSchema().setName("longitude").setType("FLOAT"),
        new TableFieldSchema().setName("acq_date").setType("DATE"),
        new TableFieldSchema().setName("acq_time").setType("TIME"),
        new TableFieldSchema().setName("bright_ti4").setType("FLOAT"),
        new TableFieldSchema().setName("confidence").setType("STRING")));
    
    // Create the BigQuery options from the command line arguments.
    BigQueryKmsKeyOptions options = PipelineOptionsFactory.fromArgs(args)
        .withValidation().as(BigQueryKmsKeyOptions.class);
    
    // String outputBigQueryTable = "<project>:<dataset>.<table>";
    String outputBigQueryTable = options.getOutputBigQueryTable();
    
    // String kmsKey =
    //    "projects/<project>/locations/<kms-location>/keyRings/<kms-keyring>/cryptoKeys/<kms-key>";
    String kmsKey = options.getKmsKey();
    
    // Create and run an Apache Beam pipeline.
    Pipeline pipeline = Pipeline.create(options);
    pipeline
        .apply("Read from BigQuery with KMS key",
            BigQueryIO.readTableRows()
                .fromQuery(query)
                .usingStandardSql()
                .withKmsKey(kmsKey))
        .apply("Write to BigQuery with KMS key",
            BigQueryIO.writeTableRows()
                .to(outputBigQueryTable)
                .withSchema(outputSchema)
                .withWriteDisposition(WriteDisposition.WRITE_TRUNCATE)
                .withKmsKey(kmsKey));
    pipeline.run().waitUntilFinish();

### Python

To authenticate to Dataflow, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import apache_beam as beam
    
    # output_bigquery_table = '<project>:<dataset>.<table>'
    # kms_key = 'projects/<project>/locations/<kms-location>/keyRings/<kms-keyring>/cryptoKeys/<kms-key>' # noqa
    # beam_args = [
    #     '--project', 'your-project-id',
    #     '--runner', 'DataflowRunner',
    #     '--temp_location', 'gs://your-bucket/samples/dataflow/kms/tmp',
    #     '--region', 'us-central1',
    # ]
    
    # Query from the NASA wildfires public dataset:
    # https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=nasa_wildfire&t=past_week&page=table
    query = """
        SELECT latitude,longitude,acq_date,acq_time,bright_ti4,confidence
        FROM `bigquery-public-data.nasa_wildfire.past_week`
        LIMIT 10
    """
    
    # Schema for the output BigQuery table.
    schema = {
        "fields": [
            {"name": "latitude", "type": "FLOAT"},
            {"name": "longitude", "type": "FLOAT"},
            {"name": "acq_date", "type": "DATE"},
            {"name": "acq_time", "type": "TIME"},
            {"name": "bright_ti4", "type": "FLOAT"},
            {"name": "confidence", "type": "STRING"},
        ],
    }
    
    options = beam.options.pipeline_options.PipelineOptions(beam_args)
    with beam.Pipeline(options=options) as pipeline:
        (
            pipeline
            | "Read from BigQuery with KMS key"
            >> beam.io.Read(
                beam.io.BigQuerySource(
                    query=query,
                    use_standard_sql=True,
                    kms_key=kms_key,
                )
            )
            | "Write to BigQuery with KMS key"
            >> beam.io.WriteToBigQuery(
                output_bigquery_table,
                schema=schema,
                write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
                kms_key=kms_key,
            )
        )

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataflow). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
