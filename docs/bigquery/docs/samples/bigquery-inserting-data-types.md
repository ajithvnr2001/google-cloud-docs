---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-inserting-data-types/
title: Streaming insert with complex data types \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:58.746621+00:00
---

# Streaming insert with complex data types  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-inserting-data-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Streaming insert with complex data types Stay organized with collections  Save and categorize content based on your preferences. 

Insert data of various BigQuery-supported types into a table.

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"time"
    
    	"cloud.google.com/go/bigquery"
    	"cloud.google.com/go/civil"
    )
    
    // ComplexType represents a complex row item
    type ComplexType struct {
    	Name         string                 `bigquery:"name"`
    	Age          int                    `bigquery:"age"`
    	School       []byte                 `bigquery:"school"`
    	Location     bigquery.[NullGeography](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_NullGeography) `bigquery:"location"`
    	Measurements []float64              `bigquery:"measurements"`
    	DatesTime    DatesTime              `bigquery:"datesTime"`
    }
    
    // DatesTime shows different date/time representation
    type DatesTime struct {
    	Day        civil.[Date](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/latest/civil.html#cloud_google_com_go_civil_Date)     `bigquery:"day"`
    	FirstTime  civil.[DateTime](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/latest/civil.html#cloud_google_com_go_civil_DateTime) `bigquery:"firstTime"`
    	SecondTime civil.[Time](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/latest/civil.html#cloud_google_com_go_civil_Time)     `bigquery:"secondTime"`
    	ThirdTime  time.[Time](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/latest/civil.html#cloud_google_com_go_civil_Time)      `bigquery:"thirdTime"`
    }
    
    // insertingDataTypes demonstrates inserting data into a table using the streaming insert mechanism.
    func insertingDataTypes(projectID, datasetID, tableID string) error {
    	// projectID := "my-project-id"
    	// datasetID := "mydataset"
    	// tableID := "mytable"
    	ctx := context.Background()
    	client, err := bigquery.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("bigquery.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// Manually defining schema
    	schema := bigquery.[Schema](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Schema){
    		{Name: "name", Type: bigquery.[StringFieldType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_StringFieldType_BytesFieldType_IntegerFieldType_FloatFieldType_BooleanFieldType_TimestampFieldType_RecordFieldType_DateFieldType_TimeFieldType_DateTimeFieldType_NumericFieldType_GeographyFieldType_BigNumericFieldType_IntervalFieldType_JSONFieldType_RangeFieldType)},
    		{Name: "age", Type: bigquery.[IntegerFieldType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_StringFieldType_BytesFieldType_IntegerFieldType_FloatFieldType_BooleanFieldType_TimestampFieldType_RecordFieldType_DateFieldType_TimeFieldType_DateTimeFieldType_NumericFieldType_GeographyFieldType_BigNumericFieldType_IntervalFieldType_JSONFieldType_RangeFieldType)},
    		{Name: "school", Type: bigquery.[BytesFieldType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_StringFieldType_BytesFieldType_IntegerFieldType_FloatFieldType_BooleanFieldType_TimestampFieldType_RecordFieldType_DateFieldType_TimeFieldType_DateTimeFieldType_NumericFieldType_GeographyFieldType_BigNumericFieldType_IntervalFieldType_JSONFieldType_RangeFieldType)},
    		{Name: "location", Type: bigquery.[GeographyFieldType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_StringFieldType_BytesFieldType_IntegerFieldType_FloatFieldType_BooleanFieldType_TimestampFieldType_RecordFieldType_DateFieldType_TimeFieldType_DateTimeFieldType_NumericFieldType_GeographyFieldType_BigNumericFieldType_IntervalFieldType_JSONFieldType_RangeFieldType)},
    		{Name: "measurements", Type: bigquery.[FloatFieldType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_StringFieldType_BytesFieldType_IntegerFieldType_FloatFieldType_BooleanFieldType_TimestampFieldType_RecordFieldType_DateFieldType_TimeFieldType_DateTimeFieldType_NumericFieldType_GeographyFieldType_BigNumericFieldType_IntervalFieldType_JSONFieldType_RangeFieldType), Repeated: true},
    		{Name: "datesTime", Type: bigquery.[RecordFieldType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_StringFieldType_BytesFieldType_IntegerFieldType_FloatFieldType_BooleanFieldType_TimestampFieldType_RecordFieldType_DateFieldType_TimeFieldType_DateTimeFieldType_NumericFieldType_GeographyFieldType_BigNumericFieldType_IntervalFieldType_JSONFieldType_RangeFieldType), Schema: bigquery.[Schema](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Schema){
    			{Name: "day", Type: bigquery.[DateFieldType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_StringFieldType_BytesFieldType_IntegerFieldType_FloatFieldType_BooleanFieldType_TimestampFieldType_RecordFieldType_DateFieldType_TimeFieldType_DateTimeFieldType_NumericFieldType_GeographyFieldType_BigNumericFieldType_IntervalFieldType_JSONFieldType_RangeFieldType)},
    			{Name: "firstTime", Type: bigquery.[DateTimeFieldType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_StringFieldType_BytesFieldType_IntegerFieldType_FloatFieldType_BooleanFieldType_TimestampFieldType_RecordFieldType_DateFieldType_TimeFieldType_DateTimeFieldType_NumericFieldType_GeographyFieldType_BigNumericFieldType_IntervalFieldType_JSONFieldType_RangeFieldType)},
    			{Name: "secondTime", Type: bigquery.[TimeFieldType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_StringFieldType_BytesFieldType_IntegerFieldType_FloatFieldType_BooleanFieldType_TimestampFieldType_RecordFieldType_DateFieldType_TimeFieldType_DateTimeFieldType_NumericFieldType_GeographyFieldType_BigNumericFieldType_IntervalFieldType_JSONFieldType_RangeFieldType)},
    			{Name: "thirdTime", Type: bigquery.[TimestampFieldType](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_StringFieldType_BytesFieldType_IntegerFieldType_FloatFieldType_BooleanFieldType_TimestampFieldType_RecordFieldType_DateFieldType_TimeFieldType_DateTimeFieldType_NumericFieldType_GeographyFieldType_BigNumericFieldType_IntervalFieldType_JSONFieldType_RangeFieldType)},
    		}},
    	}
    	// Infer schema from struct
    	// schema, err := bigquery.InferSchema(ComplexType{})
    
    	table := client.Dataset(datasetID).Table(tableID)
    	err = table.Create(ctx, &bigquery.[TableMetadata](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_TableMetadata){
    		Schema: schema,
    	})
    	if err != nil {
    		return fmt.Errorf("table.Create: %w", err)
    	}
    	day, err := civil.[ParseDate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/latest/civil.html#cloud_google_com_go_civil_Date_ParseDate)("2019-01-12")
    	if err != nil {
    		return fmt.Errorf("civil.ParseDate: %w", err)
    	}
    	firstTime, err := civil.[ParseDateTime](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/latest/civil.html#cloud_google_com_go_civil_DateTime_ParseDateTime)("2019-02-17T11:24:00.000")
    	if err != nil {
    		return fmt.Errorf("civil.ParseDateTime: %w", err)
    	}
    	secondTime, err := civil.[ParseTime](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/latest/civil.html#cloud_google_com_go_civil_Time_ParseTime)("14:00:00")
    	if err != nil {
    		return fmt.Errorf("civil.ParseTime: %w", err)
    	}
    	thirdTime, err := time.Parse(time.RFC3339Nano, "2020-04-27T18:07:25.356Z")
    	if err != nil {
    		return fmt.Errorf("time.Parse: %w", err)
    	}
    	row := &ComplexType{
    		Name:         "Tom",
    		Age:          30,
    		School:       []byte("Test University"),
    		Location:     bigquery.[NullGeography](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_NullGeography){GeographyVal: "POINT(1 2)", Valid: true},
    		Measurements: []float64{50.05, 100.5},
    		DatesTime: DatesTime{
    			Day:        day,
    			FirstTime:  firstTime,
    			SecondTime: secondTime,
    			ThirdTime:  thirdTime,
    		},
    	}
    	rows := []*ComplexType{row}
    	// Uncomment to simulate insert errors.
    	// This example row is missing required fields.
    	// badRow := &ComplexType{
    	// 	Name: "John",
    	// 	Age:  24,
    	// }
    	// rows = append(rows, badRow)
    
    	inserter := table.Inserter()
    	err = inserter.[Put](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_Inserter_Put)(ctx, rows)
    	if err != nil {
    		if multiErr, ok := err.(bigquery.[PutMultiError](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/index.html#cloud_google_com_go_bigquery_PutMultiError)); ok {
    			for _, putErr := range multiErr {
    				fmt.Printf("failed to insert row %d with err: %v \n", putErr.RowIndex, putErr.Error())
    			}
    		}
    		return err
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryError](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryError.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[Field](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Field.html);
    import com.google.cloud.bigquery.[InsertAllRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.InsertAllRequest.html);
    import com.google.cloud.bigquery.[InsertAllResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.InsertAllResponse.html);
    import com.google.cloud.bigquery.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.Schema.html);
    import com.google.cloud.bigquery.[StandardSQLTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.StandardSQLTypeName.html);
    import com.google.cloud.bigquery.[StandardTableDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.StandardTableDefinition.html);
    import com.google.cloud.bigquery.[TableDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableDefinition.html);
    import com.google.cloud.bigquery.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html);
    import com.google.cloud.bigquery.[TableInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableInfo.html);
    import java.util.Base64;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;
    
    // Sample to insert data types in a table
    public class InsertingDataTypes {
    
      public static void main(String[] args) {
        // TODO(developer): Replace these variables before running the sample.
        String datasetName = "MY_DATASET_NAME";
        String tableName = "MY_TABLE_NAME";
        insertingDataTypes(datasetName, tableName);
      }
    
      public static void insertingDataTypes(String datasetName, String tableName) {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          BigQuery bigquery = BigQueryOptions.getDefaultInstance().getService();
    
          // Inserting data types
          Field name = Field.of("name", StandardSQLTypeName.STRING);
          Field age = Field.of("age", StandardSQLTypeName.INT64);
          Field school = Field.of("school", StandardSQLTypeName.BYTES);
          Field location = Field.of("location", StandardSQLTypeName.GEOGRAPHY);
          Field measurements =
              Field.newBuilder("measurements", StandardSQLTypeName.FLOAT64)
                  .setMode(Field.Mode.REPEATED)
                  .build();
          Field day = Field.of("day", StandardSQLTypeName.DATE);
          Field firstTime = Field.of("firstTime", StandardSQLTypeName.DATETIME);
          Field secondTime = Field.of("secondTime", StandardSQLTypeName.TIME);
          Field thirdTime = Field.of("thirdTime", StandardSQLTypeName.TIMESTAMP);
          Field datesTime =
              Field.of("datesTime", StandardSQLTypeName.STRUCT, day, firstTime, secondTime, thirdTime);
          Schema schema = Schema.of(name, age, school, location, measurements, datesTime);
    
          TableId tableId = TableId.of(datasetName, tableName);
          TableDefinition tableDefinition = StandardTableDefinition.of(schema);
          TableInfo tableInfo = TableInfo.newBuilder(tableId, tableDefinition).build();
    
          bigquery.create(tableInfo);
    
          // Inserting Sample data
          Map<String, Object> datesTimeContent = new HashMap<>();
          datesTimeContent.put("day", "2019-1-12");
          datesTimeContent.put("firstTime", "2019-02-17 11:24:00.000");
          datesTimeContent.put("secondTime", "14:00:00");
          datesTimeContent.put("thirdTime", "2020-04-27T18:07:25.356Z");
    
          Map<String, Object> rowContent = new HashMap<>();
          rowContent.put("name", "Tom");
          rowContent.put("age", 30);
          rowContent.put("school", Base64.getEncoder().encodeToString("Test University".getBytes()));
          rowContent.put("location", "POINT(1 2)");
          rowContent.put("measurements", new Float[] {50.05f, 100.5f});
          rowContent.put("datesTime", datesTimeContent);
    
          InsertAllResponse response =
              bigquery.insertAll(InsertAllRequest.newBuilder(tableId).addRow(rowContent).build());
    
          if (response.hasErrors()) {
            // If any of the insertions failed, this lets you inspect the errors
            for (Map.Entry<Long, List<BigQueryError>> entry : response.getInsertErrors().entrySet()) {
              System.out.println("Response error: \n" + entry.getValue());
            }
          }
          System.out.println("Rows successfully inserted into table");
        } catch (BigQueryException e) {
          System.out.println("Insert operation not performed \n" + e.toString());
        }
      }
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-bigquery/latest/Google/Cloud/Bigquery.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    require "google/cloud/bigquery"
    require "base64"
    
    ##
    # Inserts a row with various data types into a table.
    #
    # @param dataset_id [String] The ID of the dataset to create the table in.
    # @param table_id   [String] The ID of the table to create.
    def inserting_data_types dataset_id, table_id
      bigquery = Google::Cloud::Bigquery.new
      dataset = bigquery.dataset dataset_id
      table = dataset.table table_id
    
      # Create the table if it doesn't exist.
      unless table
        dataset.create_table table_id do |t|
          t.string "name"
          t.integer "age"
          t.bytes "school"
          t.geography "location"
          t.float "measurements", mode: :repeated
          t.record "datesTime" do |s|
            s.date "day"
            s.datetime "firstTime"
            s.time "secondTime"
            s.timestamp "thirdTime"
          end
        end
        table = dataset.table table_id
      end
    
      dates_time_content = {
        "day"        => "2019-1-12",
        "firstTime"  => "2019-02-17 11:24:00.000",
        "secondTime" => "14:00:00",
        "thirdTime"  => "2020-04-27T18:07:25.356Z"
      }
    
      row_content = {
        "name"         => "Tom",
        "age"          => 30,
        "school"       => Base64.strict_encode64("Test University"),
        "location"     => "POINT(1 2)",
        "measurements" => [50.05, 100.5],
        "datesTime"    => dates_time_content
      }
    
      response = table.insert [row_content]
    
      if response.success?
        puts "Rows successfully inserted into table"
      else
        puts "Insert operation not performed"
        response.insert_errors.each do |error|
          puts "Error: #{error.errors}"
        end
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
