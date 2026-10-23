---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-deidentify-date-shift/
title: Date shifting of a CSV file \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:26.640064+00:00
---

# Date shifting of a CSV file  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-deidentify-date-shift/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Date shifting of a CSV file Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates date shifting of a CSV file.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [De-identifying sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data)
  * [Transformation reference](https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.IO;
    using System.Linq;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    
    public class DeidentifyWithDateShift
    {
        public static DeidentifyContentResponse Deidentify(
            string projectId,
            string inputCsvFilePath,
            int lowerBoundDays,
            int upperBoundDays,
            string dateFields,
            string contextField,
            string keyName,
            string wrappedKey)
        {
            var hasKeyName = !string.IsNullOrEmpty(keyName);
            var hasWrappedKey = !string.IsNullOrEmpty(wrappedKey);
            var hasContext = !string.IsNullOrEmpty(contextField);
            bool allFieldsSet = hasKeyName && hasWrappedKey && hasContext;
            bool noFieldsSet = !hasKeyName && !hasWrappedKey && !hasContext;
            if (!(allFieldsSet || noFieldsSet))
            {
                throw new ArgumentException("Must specify ALL or NONE of: {contextFieldId, keyName, wrappedKey}!");
            }
    
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Read file
            var csvLines = File.ReadAllLines(inputCsvFilePath);
            var csvHeaders = csvLines[0].Split(',');
            var csvRows = csvLines.Skip(1).ToArray();
    
            // Convert dates to protobuf format, and everything else to a string
            var protoHeaders = csvHeaders.Select(header => new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = header });
            var protoRows = csvRows.Select(csvRow =>
            {
                var rowValues = csvRow.Split(',');
                var protoValues = rowValues.Select(rowValue =>
                   System.[DateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DateTime.html).TryParse(rowValue, out var parsedDate)
                   ? new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { DateValue = Google.[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Type.html).[Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DateTime.html#Google_Cloud_Dlp_V2_DateTime_Date).[FromDateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html#Google_Protobuf_WellKnownTypes_Timestamp_FromDateTime_System_DateTime_)(parsedDate) }
                   : new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = rowValue });
    
                var rowObject = new Table.Types.Row();
                rowObject.Values.[Add](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ExtensionRegistry.html#Google_Protobuf_ExtensionRegistry_Add_Google_Protobuf_Extension_)(protoValues);
                return rowObject;
            });
    
            var dateFieldList = dateFields
                .Split(',')
                .Select(field => new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = field });
    
            // Construct + execute the request
            var dateShiftConfig = new [DateShiftConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DateShiftConfig.html)
            {
                LowerBoundDays = lowerBoundDays,
                UpperBoundDays = upperBoundDays
            };
    
            dateShiftConfig.Context = new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = contextField };
            dateShiftConfig.[CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.html) = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.html)
            {
                KmsWrapped = new [KmsWrappedCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.KmsWrappedCryptoKey.html)
                {
                    WrappedKey = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[FromBase64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_FromBase64_System_String_)(wrappedKey),
                    CryptoKeyName = keyName
                }
            };
    
            var deidConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                RecordTransformations = new [RecordTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordTransformations.html)
                {
                    FieldTransformations =
                    {
                        new [FieldTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldTransformation.html)
                        {
                            PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                            {
                                DateShiftConfig = dateShiftConfig
                            },
                            Fields = { dateFieldList }
                        }
                    }
                }
            };
    
            var response = dlp.DeidentifyContent(
                new [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest.html)
                {
                    Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                    DeidentifyConfig = deidConfig,
                    Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html)
                    {
                        Table = new [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html)
                        {
                            Headers = { protoHeaders },
                            Rows = { protoRows }
                        }
                    }
                });
    
            return response;
        }
    }

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // deidentifyDateShift shifts dates found in the input between lowerBoundDays and
    // upperBoundDays.
    func deidentifyDateShift(w io.Writer, projectID string, lowerBoundDays, upperBoundDays int32, input string) error {
    	// projectID := "my-project-id"
    	// lowerBoundDays := -1
    	// upperBound := -1
    	// input := "2016-01-10"
    	// Will print "2016-01-09"
    	ctx := context.Background()
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    	// Create a configured request.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		DeidentifyConfig: &dlppb.DeidentifyConfig{
    			Transformation: &dlppb.DeidentifyConfig_InfoTypeTransformations{
    				InfoTypeTransformations: &dlppb.InfoTypeTransformations{
    					Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    						{
    							InfoTypes: []*dlppb.InfoType{}, // Match all info types.
    							PrimitiveTransformation: &dlppb.PrimitiveTransformation{
    								Transformation: &dlppb.PrimitiveTransformation_DateShiftConfig{
    									DateShiftConfig: &dlppb.DateShiftConfig{
    										LowerBoundDays: lowerBoundDays,
    										UpperBoundDays: upperBoundDays,
    									},
    								},
    							},
    						},
    					},
    				},
    			},
    		},
    		// The InspectConfig is used to identify the DATE fields.
    		InspectConfig: &dlppb.InspectConfig{
    			InfoTypes: []*dlppb.InfoType{
    				{
    					Name: "DATE",
    				},
    			},
    		},
    		// The item to analyze.
    		Item: &dlppb.ContentItem{
    			DataItem: &dlppb.ContentItem_Value{
    				Value: input,
    			},
    		},
    	}
    	// Send the request.
    	r, err := client.DeidentifyContent(ctx, req)
    	if err != nil {
    		return fmt.Errorf("DeidentifyContent: %w", err)
    	}
    	// Print the result.
    	fmt.Fprint(w, r.GetItem().GetValue())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.common.base.Splitter;
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[DateShiftConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DateShiftConfig.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html);
    import com.google.privacy.dlp.v2.[FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html);
    import com.google.privacy.dlp.v2.[FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html);
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html);
    import com.google.type.[Date](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html);
    import java.io.BufferedReader;
    import java.io.BufferedWriter;
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Path;
    import java.nio.file.Paths;
    import java.time.LocalDate;
    import java.time.format.DateTimeFormatter;
    import java.util.Arrays;
    import java.util.List;
    import java.util.stream.Collectors;
    
    public class DeIdentifyWithDateShift {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        Path inputCsvFile = Paths.get("path/to/your/input/file.csv");
        Path outputCsvFile = Paths.get("path/to/your/output/file.csv");
        deIdentifyWithDateShift(projectId, inputCsvFile, outputCsvFile);
      }
    
      public static void deIdentifyWithDateShift(
          String projectId, Path inputCsvFile, Path outputCsvFile) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Read the contents of the CSV file into a Table
          List<FieldId> headers;
          List<Table.[Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html)> rows;
          try (BufferedReader input = Files.newBufferedReader(inputCsvFile)) {
            // Parse and convert the first line into header names
            headers =
                Arrays.stream(input.readLine().split(","))
                    .map(header -> [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName(header).build())
                    .collect(Collectors.toList());
            // Parse the remainder of the file as Table.Rows
            rows =
                input.lines().map(DeIdentifyWithDateShift::parseLineAsRow).collect(Collectors.toList());
          }
          [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) table = [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).newBuilder().[addAllHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addAllHeaders_java_lang_Iterable___extends_com_google_privacy_dlp_v2_FieldId__)(headers).[addAllRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addAllRows_java_lang_Iterable___extends_com_google_privacy_dlp_v2_Table_Row__)(rows).build();
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setTable(table).build();
    
          // Set the maximum days to shift dates backwards (lower bound) or forward (upper bound)
          [DateShiftConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DateShiftConfig.html) dateShiftConfig =
              [DateShiftConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DateShiftConfig.html).newBuilder().[setLowerBoundDays](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DateShiftConfig.Builder.html#com_google_privacy_dlp_v2_DateShiftConfig_Builder_setLowerBoundDays_int_)(5).[setUpperBoundDays](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DateShiftConfig.Builder.html#com_google_privacy_dlp_v2_DateShiftConfig_Builder_setUpperBoundDays_int_)(5).build();
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) transformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder().[setDateShiftConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setDateShiftConfig_com_google_privacy_dlp_v2_DateShiftConfig_)(dateShiftConfig).build();
          // Specify which fields the DateShift should apply too
          List<FieldId> dateFields = Arrays.asList(headers.get(1), headers.get(3));
          [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html) fieldTransformation =
              [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html).newBuilder()
                  .[addAllFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.Builder.html#com_google_privacy_dlp_v2_FieldTransformation_Builder_addAllFields_java_lang_Iterable___extends_com_google_privacy_dlp_v2_FieldId__)(dateFields)
                  .setPrimitiveTransformation(transformation)
                  .build();
          [RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html) recordTransformations =
              [RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html).newBuilder().addFieldTransformations(fieldTransformation).build();
          // Specify the config for the de-identify request
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) deidentifyConfig =
              [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder().[setRecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.Builder.html#com_google_privacy_dlp_v2_DeidentifyConfig_Builder_setRecordTransformations_com_google_privacy_dlp_v2_RecordTransformations_)(recordTransformations).build();
    
          // Combine configurations into a request for the service.
          [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html) request =
              [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setDeidentifyConfig(deidentifyConfig)
                  .build();
    
          // Send the request and receive response from the service
          [DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html) response = dlp.deidentifyContent(request);
    
          // Write the results to the target CSV file
          try (BufferedWriter writer = Files.newBufferedWriter(outputCsvFile)) {
            [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) outTable = response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getTable();
            String headerOut =
                outTable.[getHeadersList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html#com_google_privacy_dlp_v2_Table_getHeadersList__)().stream()
                    .map(FieldId::getName)
                    .collect(Collectors.joining(","));
            writer.write(headerOut + "\n");
    
            List<String> rowOutput =
                outTable.[getRowsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html#com_google_privacy_dlp_v2_Table_getRowsList__)().stream()
                    .map(row -> joinRow(row.getValuesList()))
                    .collect(Collectors.toList());
            for (String line : rowOutput) {
              writer.write(line + "\n");
            }
            System.out.println("Content written to file: " + outputCsvFile.toString());
          }
        }
      }
    
      // Convert the string from the csv file into com.google.type.Date
      public static [Date](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html) parseAsDate(String s) {
        LocalDate date = LocalDate.parse(s, DateTimeFormatter.ofPattern("MM/dd/yyyy"));
        return [Date](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html).newBuilder()
            .setDay(date.getDayOfMonth())
            .setMonth(date.getMonthValue())
            .setYear(date.getYear())
            .build();
      }
    
      // Each row is in the format: Name,BirthDate,CreditCardNumber,RegisterDate
      public static [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).[Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html) parseLineAsRow(String line) {
        List<String> values = Splitter.on(",").splitToList(line);
        [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html) name = [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)(values.get(0)).build();
        [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html) birthDate = [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setDateValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setDateValue_com_google_type_Date_)(parseAsDate(values.get(1))).build();
        [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html) creditCardNumber = [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)(values.get(2)).build();
        [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html) registerDate = [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setDateValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setDateValue_com_google_type_Date_)(parseAsDate(values.get(3))).build();
        return [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).Row.newBuilder()
            .addValues(name)
            .addValues(birthDate)
            .addValues(creditCardNumber)
            .addValues(registerDate)
            .build();
      }
    
      public static String formatDate([Date](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html) d) {
        return String.format("%s/%s/%s", d.[getMonth](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html#com_google_type_Date_getMonth__)(), d.[getDay](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html#com_google_type_Date_getDay__)(), d.[getYear](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html#com_google_type_Date_getYear__)());
      }
    
      public static String joinRow(List<Value> values) {
        String name = values.get(0).getStringValue();
        String birthDate = formatDate(values.get(1).getDateValue());
        String creditCardNumber = values.get(2).getStringValue();
        String registerDate = formatDate(values.get(3).getDateValue());
        return String.join(",", name, birthDate, creditCardNumber, registerDate);
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('@google-cloud/dlp');
    
    // Instantiates a client
    const dlp = new DLP.DlpServiceClient();
    
    // Import other required libraries
    const fs = require('fs');
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The path to the CSV file to deidentify
    // The first row of the file must specify column names, and all other rows
    // must contain valid values
    // const inputCsvFile = '/path/to/input/file.csv';
    
    // The path to save the date-shifted CSV file to
    // const outputCsvFile = '/path/to/output/file.csv';
    
    // The list of (date) fields in the CSV file to date shift
    // const dateFields = [{ name: 'birth_date'}, { name: 'register_date' }];
    
    // The maximum number of days to shift a date backward
    // const lowerBoundDays = 1;
    
    // The maximum number of days to shift a date forward
    // const upperBoundDays = 1;
    
    // (Optional) The column to determine date shift amount based on
    // If this is not specified, a random shift amount will be used for every row
    // If this is specified, then 'wrappedKey' and 'keyName' must also be set
    // const contextFieldId = [{ name: 'user_id' }];
    
    // (Optional) The name of the Cloud KMS key used to encrypt ('wrap') the AES-256 key
    // If this is specified, then 'wrappedKey' and 'contextFieldId' must also be set
    // const keyName = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME';
    
    // (Optional) The encrypted ('wrapped') AES-256 key to use when shifting dates
    // This key should be encrypted using the Cloud KMS key specified above
    // If this is specified, then 'keyName' and 'contextFieldId' must also be set
    // const wrappedKey = 'YOUR_ENCRYPTED_AES_256_KEY'
    
    // Helper function for converting CSV rows to Protobuf types
    const rowToProto = row => {
      const values = row.split(',');
      const convertedValues = values.map(value => {
        if (Date.parse(value)) {
          const date = new Date(value);
          return {
            dateValue: {
              year: date.getFullYear(),
              month: date.getMonth() + 1,
              day: date.getDate(),
            },
          };
        } else {
          // Convert all non-date values to strings
          return {stringValue: value.toString()};
        }
      });
      return {values: convertedValues};
    };
    
    async function deidentifyWithDateShift() {
      // Read and parse a CSV file
      const csvLines = fs
        .readFileSync(inputCsvFile)
        .toString()
        .split('\n')
        .filter(line => line.includes(','));
      const csvHeaders = csvLines[0].split(',');
      const csvRows = csvLines.slice(1);
    
      // Construct the table object
      const tableItem = {
        table: {
          headers: csvHeaders.map(header => {
            return {name: header};
          }),
          rows: csvRows.map(row => rowToProto(row)),
        },
      };
    
      // Construct DateShiftConfig
      const dateShiftConfig = {
        lowerBoundDays: lowerBoundDays,
        upperBoundDays: upperBoundDays,
      };
    
      if (contextFieldId && keyName && wrappedKey) {
        dateShiftConfig.context = {name: contextFieldId};
        dateShiftConfig.cryptoKey = {
          kmsWrapped: {
            wrappedKey: wrappedKey,
            cryptoKeyName: keyName,
          },
        };
      } else if (contextFieldId || keyName || wrappedKey) {
        throw new Error(
          'You must set either ALL or NONE of {contextFieldId, keyName, wrappedKey}!'
        );
      }
    
      // Construct deidentification request
      const request = {
        parent: `projects/${projectId}/locations/global`,
        deidentifyConfig: {
          recordTransformations: {
            fieldTransformations: [
              {
                fields: dateFields,
                primitiveTransformation: {
                  dateShiftConfig: dateShiftConfig,
                },
              },
            ],
          },
        },
        item: tableItem,
      };
    
      // Run deidentification request
      const [response] = await dlp.deidentifyContent(request);
      const tableRows = response.item.table.rows;
    
      // Write results to a CSV file
      tableRows.forEach((row, rowIndex) => {
        const rowValues = row.values.map(
          value =>
            value.stringValue ||
            `${value.dateValue.month}/${value.dateValue.day}/${value.dateValue.year}`
        );
        csvLines[rowIndex + 1] = rowValues.join(',');
      });
      csvLines.push('');
      fs.writeFileSync(outputCsvFile, csvLines.join('\n'));
    
      // Print status
      console.log(`Successfully saved date-shift output to ${outputCsvFile}`);
    }
    
    deidentifyWithDateShift();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use DateTime;
    use Exception;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CryptoKey;
    use Google\Cloud\Dlp\V2\DateShiftConfig;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\FieldTransformation;
    use Google\Cloud\Dlp\V2\KmsWrappedCryptoKey;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\RecordTransformations;
    use Google\Cloud\Dlp\V2\Table;
    use Google\Cloud\Dlp\V2\Table\Row;
    use Google\Cloud\Dlp\V2\Value;
    use Google\Type\Date;
    
    /**
     * Deidentify dates in a CSV file by pseudorandomly shifting them.
     * If contextFieldName is not specified, a random shift amount will be used for every row.
     * If contextFieldName is specified, then 'wrappedKey' and 'keyName' must also be set.
     *
     * @param string $callingProjectId  The GCP Project ID to run the API call under
     * @param string $inputCsvFile      The path to the CSV file to deidentify
     * @param string $outputCsvFile     The path to save the date-shifted CSV file to
     * @param string $dateFieldNames    The comma-separated list of (date) fields in the CSV file to date shift
     * @param int    $lowerBoundDays    The maximum number of days to shift a date backward
     * @param int    $upperBoundDays    The maximum number of days to shift a date forward
     * @param string $contextFieldName  (Optional) The column to determine date shift amount based on
     * @param string $keyName           (Optional) The encrypted ('wrapped') AES-256 key to use when shifting dates
     * @param string $wrappedKey        (Optional) The name of the Cloud KMS key used to encrypt (wrap) the AES-256 key
     */
    function deidentify_dates(
        string $callingProjectId,
        string $inputCsvFile,
        string $outputCsvFile,
        string $dateFieldNames,
        int $lowerBoundDays,
        int $upperBoundDays,
        string $contextFieldName = '',
        string $keyName = '',
        string $wrappedKey = ''
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Read a CSV file
        $csvLines = file($inputCsvFile, FILE_IGNORE_NEW_LINES);
        $csvHeaders = explode(',', $csvLines[0]);
        $csvRows = array_slice($csvLines, 1);
    
        // Convert CSV file into protobuf objects
        $tableHeaders = array_map(function ($csvHeader) {
            return (new FieldId)->setName($csvHeader);
        }, $csvHeaders);
    
        $tableRows = array_map(function ($csvRow) {
            $rowValues = array_map(function ($csvValue) {
                if ($csvDate = DateTime::createFromFormat('m/d/Y', $csvValue)) {
                    $date = (new Date())
                        ->setYear((int) $csvDate->format('Y'))
                        ->setMonth((int) $csvDate->format('m'))
                        ->setDay((int) $csvDate->format('d'));
                    return (new Value())
                        ->setDateValue($date);
                } else {
                    return (new Value())
                        ->setStringValue($csvValue);
                }
            }, explode(',', $csvRow));
    
            return (new Row())
                ->setValues($rowValues);
        }, $csvRows);
    
        // Convert date fields into protobuf objects
        $dateFields = array_map(function ($dateFieldName) {
            return (new FieldId())->setName($dateFieldName);
        }, explode(',', $dateFieldNames));
    
        // Construct the table object
        $table = (new Table())
            ->setHeaders($tableHeaders)
            ->setRows($tableRows);
    
        $item = (new ContentItem())
            ->setTable($table);
    
        // Construct dateShiftConfig
        $dateShiftConfig = (new DateShiftConfig())
            ->setLowerBoundDays($lowerBoundDays)
            ->setUpperBoundDays($upperBoundDays);
    
        if ($contextFieldName && $keyName && $wrappedKey) {
            $contextField = (new FieldId())
                ->setName($contextFieldName);
    
            // Create the wrapped crypto key configuration object
            $kmsWrappedCryptoKey = (new KmsWrappedCryptoKey())
                ->setWrappedKey(base64_decode($wrappedKey))
                ->setCryptoKeyName($keyName);
    
            $cryptoKey = (new CryptoKey())
                ->setKmsWrapped($kmsWrappedCryptoKey);
    
            $dateShiftConfig
                ->setContext($contextField)
                ->setCryptoKey($cryptoKey);
        } elseif ($contextFieldName || $keyName || $wrappedKey) {
            throw new Exception('You must set either ALL or NONE of {$contextFieldName, $keyName, $wrappedKey}!');
        }
    
        // Create the information transform configuration objects
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setDateShiftConfig($dateShiftConfig);
    
        $fieldTransformation = (new FieldTransformation())
            ->setPrimitiveTransformation($primitiveTransformation)
            ->setFields($dateFields);
    
        $recordTransformations = (new RecordTransformations())
            ->setFieldTransformations([$fieldTransformation]);
    
        // Create the deidentification configuration object
        $deidentifyConfig = (new DeidentifyConfig())
            ->setRecordTransformations($recordTransformations);
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Run request
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setDeidentifyConfig($deidentifyConfig)
            ->setItem($item);
        $response = $dlp->deidentifyContent($deidentifyContentRequest);
    
        // Check for errors
        foreach ($response->getOverview()->getTransformationSummaries() as $summary) {
            foreach ($summary->getResults() as $result) {
                if ($details = $result->getDetails()) {
                    printf('Error: %s' . PHP_EOL, $details);
                    return;
                }
            }
        }
    
        // Save the results to a file
        $csvRef = fopen($outputCsvFile, 'w');
        fputcsv($csvRef, $csvHeaders);
        foreach ($response->getItem()->getTable()->getRows() as $tableRow) {
            $values = array_map(function ($tableValue) {
                if ($tableValue->getStringValue()) {
                    return $tableValue->getStringValue();
                }
                $protoDate = $tableValue->getDateValue();
                $date = mktime(0, 0, 0, $protoDate->getMonth(), $protoDate->getDay(), $protoDate->getYear());
                return strftime('%D', $date);
            }, iterator_to_array($tableRow->getValues()));
            fputcsv($csvRef, $values);
        };
        fclose($csvRef);
        printf('Deidentified dates written to %s' . PHP_EOL, $outputCsvFile);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    import csv
    from datetime import datetime
    from typing import List
    
    import google.cloud.dlp
    from google.cloud.dlp_v2 import [types](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.html)
    
    
    def deidentify_with_date_shift(
        project: str,
        input_csv_file: str = None,
        output_csv_file: str = None,
        date_fields: List[str] = None,
        lower_bound_days: int = None,
        upper_bound_days: int = None,
        context_field_id: str = None,
        wrapped_key: str = None,
        key_name: str = None,
    ) -> None:
        """Uses the Data Loss Prevention API to deidentify dates in a CSV file by
            pseudorandomly shifting them.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            input_csv_file: The path to the CSV file to deidentify. The first row
                of the file must specify column names, and all other rows must
                contain valid values.
            output_csv_file: The path to save the date-shifted CSV file.
            date_fields: The list of (date) fields in the CSV file to date shift.
                Example: ['birth_date', 'register_date']
            lower_bound_days: The maximum number of days to shift a date backward
            upper_bound_days: The maximum number of days to shift a date forward
            context_field_id: (Optional) The column to determine date shift amount
                based on. If this is not specified, a random shift amount will be
                used for every row. If this is specified, then 'wrappedKey' and
                'keyName' must also be set. Example:
                contextFieldId = [{ 'name': 'user_id' }]
            key_name: (Optional) The name of the Cloud KMS key used to encrypt
                ('wrap') the AES-256 key. Example:
                key_name = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/
                keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME'
            wrapped_key: (Optional) The encrypted ('wrapped') AES-256 key to use.
                This key should be encrypted using the Cloud KMS key specified by
                key_name.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Convert date field list to Protobuf type
        def map_fields(field: str) -> dict:
            return {"name": field}
    
        if date_fields:
            date_fields = map(map_fields, date_fields)
        else:
            date_fields = []
    
        f = []
        with open(input_csv_file) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                f.append(row)
    
        #  Helper function for converting CSV rows to Protobuf types
        def map_headers(header: str) -> dict:
            return {"name": header}
    
        def map_data(value: str) -> dict:
            try:
                date = datetime.strptime(value, "%m/%d/%Y")
                return {
                    "date_value": {"year": date.year, "month": date.month, "day": date.day}
                }
            except ValueError:
                return {"string_value": value}
    
        def map_rows(row: str) -> dict:
            return {"values": map(map_data, row)}
    
        # Using the helper functions, convert CSV rows to protobuf-compatible
        # dictionaries.
        csv_headers = map(map_headers, f[0])
        csv_rows = map(map_rows, f[1:])
    
        # Construct the table dict
        table_item = {"table": {"headers": csv_headers, "rows": csv_rows}}
    
        # Construct date shift config
        date_shift_config = {
            "lower_bound_days": lower_bound_days,
            "upper_bound_days": upper_bound_days,
        }
    
        # If using a Cloud KMS key, add it to the date_shift_config.
        # The wrapped key is base64-encoded, but the library expects a binary
        # string, so decode it here.
        if context_field_id and key_name and wrapped_key:
            date_shift_config["context"] = {"name": context_field_id}
            date_shift_config["crypto_key"] = {
                "kms_wrapped": {
                    "wrapped_key": base64.b64decode(wrapped_key),
                    "crypto_key_name": key_name,
                }
            }
        elif context_field_id or key_name or wrapped_key:
            raise ValueError(
                """You must set either ALL or NONE of
            [context_field_id, key_name, wrapped_key]!"""
            )
    
        # Construct Deidentify Config
        deidentify_config = {
            "record_transformations": {
                "field_transformations": [
                    {
                        "fields": date_fields,
                        "primitive_transformation": {
                            "date_shift_config": date_shift_config
                        },
                    }
                ]
            }
        }
    
        # Write to CSV helper methods
        def write_header(header: [types](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.html).storage.[FieldId](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.FieldId.html)) -> str:
            return header.name
    
        def write_data(data: [types](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.html).storage.[Value](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Value.html)) -> str:
            return data.string_value or "{}/{}/{}".format(
                data.date_value.month,
                data.date_value.day,
                data.date_value.year,
            )
    
        # Call the API
        response = dlp.[deidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_deidentify_content)(
            request={
                "parent": parent,
                "deidentify_config": deidentify_config,
                "item": table_item,
            }
        )
    
        # Write results to CSV file
        with open(output_csv_file, "w") as csvfile:
            write_file = csv.writer(csvfile, delimiter=",")
            write_file.writerow(map(write_header, response.item.table.headers))
            for row in response.item.table.rows:
                write_file.writerow(map(write_data, row.values))
        # Print status
        print(f"Successfully saved date-shift output to {output_csv_file}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
