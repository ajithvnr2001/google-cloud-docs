---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquerystorage-quickstart/
title: Download table data in the Avro data format \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:33.622359+00:00
---

# Download table data in the Avro data format  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquerystorage-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Download table data in the Avro data format Stay organized with collections  Save and categorize content based on your preferences. 

Download table data using the Avro data format and deserialize the data into row objects.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [BigQuery Storage API Client Libraries](https://docs.cloud.google.com/bigquery/docs/reference/storage/libraries)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-bigquery/latest/). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    #include "google/cloud/bigquery/storage/v1/bigquery_read_client.h"
    #include <iostream>
    
    namespace {
    void ProcessRowsInAvroFormat(
        ::google::cloud::bigquery::storage::v1::AvroSchema const&,
        ::google::cloud::bigquery::storage::v1::AvroRows const&) {
      // Code to deserialize avro rows should be added here.
    }
    }  // namespace
    
    int main(int argc, char* argv[]) try {
      if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <project-id> <table-name>\n";
        return 1;
      }
    
      // project_name should be in the format "projects/<your-gcp-project>"
      std::string const project_name = "projects/" + std::string(argv[1]);
      // table_name should be in the format:
      // "projects/<project-table-resides-in>/datasets/<dataset-table_resides-in>/tables/<table
      // name>" The project values in project_name and table_name do not have to be
      // identical.
      std::string const table_name = argv[2];
    
      // Create a namespace alias to make the code easier to read.
      namespace bigquery_storage = ::google::cloud::bigquery_storage_v1;
      constexpr int kMaxReadStreams = 1;
      // Create the ReadSession.
      auto client = bigquery_storage::BigQueryReadClient(
          bigquery_storage::MakeBigQueryReadConnection());
      ::google::cloud::bigquery::storage::v1::ReadSession read_session;
      read_session.set_data_format(
          google::cloud::bigquery::storage::v1::DataFormat::AVRO);
      read_session.set_table(table_name);
      auto session =
          client.CreateReadSession(project_name, read_session, kMaxReadStreams);
      if (!session) throw std::move(session).status();
    
      // Read rows from the ReadSession.
      constexpr int kRowOffset = 0;
      auto read_rows = client.ReadRows(session->streams(0).name(), kRowOffset);
    
      std::int64_t num_rows = 0;
      for (auto const& row : read_rows) {
        if (row.ok()) {
          num_rows += row->row_count();
          ProcessRowsInAvroFormat(session->avro_schema(), row->avro_rows());
        }
      }
    
      std::cout << num_rows << " rows read from table: " << table_name << "\n";
      return 0;
    } catch (google::cloud::Status const& status) {
      std::cerr << "google::cloud::Status thrown: " << status << "\n";
      return 1;
    }

### C#

Before trying this sample, follow the C# setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    using [Avro](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.DataFormat.html#Google_Cloud_BigQuery_Storage_V1_DataFormat_Avro);
    using Avro.IO;
    using Avro.Specific;
    using BigQueryStorage.Samples.Utilities;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.BigQuery.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.html);
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;
    using System.Threading.Tasks;
    using static Google.Cloud.BigQuery.Storage.V1.ReadSession.Types;
    
    public class QuickstartSample
    {
    
        public async Task<List<BabyNamesData>> QuickstartAsync(string projectId)
        {
            var bigQueryReadClient = [BigQueryReadClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.BigQueryReadClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.BigQueryReadClient.html#Google_Cloud_BigQuery_Storage_V1_BigQueryReadClient_Create)();
            [CreateReadSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.CreateReadSessionRequest.html) createReadSessionRequest = new [CreateReadSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.CreateReadSessionRequest.html)
            {
                ParentAsProjectName = new [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)(projectId),
                ReadSession = new [ReadSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession.html)
                {
                    // This example uses baby name data from the public datasets.
                    TableAsTableName = new [TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.TableName.html)("bigquery-public-data", "usa_names", "usa_1910_current"),
                    DataFormat = [DataFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.DataFormat.html).[Avro](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.DataFormat.html#Google_Cloud_BigQuery_Storage_V1_DataFormat_Avro),
                    ReadOptions = new [TableReadOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession.Types.TableReadOptions.html)
                    {
                        // Specify the columns to be projected by adding them to the selected fields.
                        SelectedFields = { "name", "number", "state" },
                        RowRestriction = "state = \"WA\"",
                    },
                },
                // Sets maximum number of reading streams to 1.
                MaxStreamCount = 1,
            };
            var readSession = bigQueryReadClient.CreateReadSession(createReadSessionRequest);
    
            // Uses the first (and only) stream to read data from and reading starts from offset 0.
            var readRowsStream = bigQueryReadClient.ReadRows(readSession.[Streams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSession.html#Google_Cloud_BigQuery_Storage_V1_ReadSession_Streams).First().Name, 0).GetResponseStream();
            var schema = [Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.AvroSchema.html#Google_Cloud_BigQuery_Storage_V1_AvroSchema_Schema).Parse(readSession.[AvroSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.AvroSchema.html).[Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.AvroSchema.html#Google_Cloud_BigQuery_Storage_V1_AvroSchema_Schema));
    
            // BabyNamesData has been generated using AvroGen, version 1.11.1.
            // The file is available here https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/main/bigquery-storage/api/BigQueryStorage.Samples/Utilities/BabyNamesData.g.cs
            var reader = new SpecificDatumReader<BabyNamesData>(schema, schema);
            var dataList = new List<BabyNamesData>();
            await foreach (var readRowResponse in readRowsStream)
            {
                var byteArray = readRowResponse.[AvroRows](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.AvroRows.html).[SerializedBinaryRows](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.AvroRows.html#Google_Cloud_BigQuery_Storage_V1_AvroRows_SerializedBinaryRows).ToByteArray();
                var decoder = new BinaryDecoder(new MemoryStream(byteArray));
                for (int row = 0; row < readRowResponse.RowCount; row++)
                {
                    var record = reader.Read(new BabyNamesData(), decoder);
                    dataList.Add(record);
                    Console.WriteLine($"name: {record.name}, state: {record.state}, number: {record.number}");
                }
            }
            return dataList;
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    // The bigquery_storage_quickstart application demonstrates usage of the
    // BigQuery Storage read API.  It demonstrates API features such as column
    // projection (limiting the output to a subset of a table's columns),
    // column filtering (using simple predicates to filter records on the server
    // side), establishing the snapshot time (reading data from the table at a
    // specific point in time), decoding Avro row blocks using the third party
    // "github.com/linkedin/goavro" library, and decoding Arrow row blocks using
    // the third party "github.com/apache/arrow/go" library.
    package main
    
    import (
    	"bytes"
    	"context"
    	"encoding/json"
    	"flag"
    	"fmt"
    	"io"
    	"log"
    	"sort"
    	"strings"
    	"sync"
    	"time"
    
    	bqStorage "cloud.google.com/go/bigquery/storage/apiv1"
    	"cloud.google.com/go/bigquery/storage/apiv1/storagepb"
    	"github.com/apache/arrow/go/v10/arrow"
    	"github.com/apache/arrow/go/v10/arrow/ipc"
    	"github.com/apache/arrow/go/v10/arrow/memory"
    	gax "github.com/googleapis/gax-go/v2"
    	goavro "github.com/linkedin/goavro/v2"
    	"google.golang.org/genproto/googleapis/rpc/errdetails"
    	"google.golang.org/grpc"
    	"google.golang.org/grpc/codes"
    	"google.golang.org/grpc/status"
    	"google.golang.org/protobuf/types/known/timestamppb"
    )
    
    // rpcOpts is used to configure the underlying gRPC client to accept large
    // messages.  The BigQuery Storage API may send message blocks up to 128MB
    // in size.
    var rpcOpts = gax.WithGRPCOptions(
    	grpc.MaxCallRecvMsgSize(1024 * 1024 * 129),
    )
    
    // Available formats
    const (
    	AVRO_FORMAT  = "avro"
    	ARROW_FORMAT = "arrow"
    )
    
    // Command-line flags.
    var (
    	projectID = flag.String("project_id", "",
    		"Cloud Project ID, used for session creation.")
    	snapshotMillis = flag.Int64("snapshot_millis", 0,
    		"Snapshot time to use for reads, represented in epoch milliseconds format.  Default behavior reads current data.")
    	format = flag.String("format", AVRO_FORMAT, "format to read data from storage API. Default is avro.")
    )
    
    func main() {
    	flag.Parse()
    	ctx := context.Background()
    	bqReadClient, err := bqStorage.NewBigQueryReadClient(ctx)
    	if err != nil {
    		log.Fatalf("NewBigQueryStorageClient: %v", err)
    	}
    	defer bqReadClient.Close()
    
    	// Verify we've been provided a parent project which will contain the read session.  The
    	// session may exist in a different project than the table being read.
    	if *projectID == "" {
    		log.Fatalf("No parent project ID specified, please supply using the --project_id flag.")
    	}
    
    	// This example uses baby name data from the public datasets.
    	srcProjectID := "bigquery-public-data"
    	srcDatasetID := "usa_names"
    	srcTableID := "usa_1910_current"
    	readTable := fmt.Sprintf("projects/%s/datasets/%s/tables/%s",
    		srcProjectID,
    		srcDatasetID,
    		srcTableID,
    	)
    
    	// We limit the output columns to a subset of those allowed in the table,
    	// and set a simple filter to only report names from the state of
    	// Washington (WA).
    	tableReadOptions := &storagepb.ReadSession_TableReadOptions{
    		SelectedFields: []string{"name", "number", "state"},
    		RowRestriction: `state = "WA"`,
    	}
    
    	dataFormat := storagepb.[DataFormat_AVRO](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/storage/apiv1/storagepb.html#cloud_google_com_go_bigquery_storage_apiv1_storagepb_DataFormat_DATA_FORMAT_UNSPECIFIED_DataFormat_AVRO_DataFormat_ARROW)
    	if *format == ARROW_FORMAT {
    		dataFormat = storagepb.[DataFormat_ARROW](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/storage/apiv1/storagepb.html#cloud_google_com_go_bigquery_storage_apiv1_storagepb_DataFormat_DATA_FORMAT_UNSPECIFIED_DataFormat_AVRO_DataFormat_ARROW)
    	}
    	createReadSessionRequest := &storagepb.CreateReadSessionRequest{
    		Parent: fmt.Sprintf("projects/%s", *projectID),
    		ReadSession: &storagepb.ReadSession{
    			Table:       readTable,
    			DataFormat:  dataFormat,
    			ReadOptions: tableReadOptions,
    		},
    		MaxStreamCount: 1,
    	}
    
    	// Set a snapshot time if it's been specified.
    	if *snapshotMillis > 0 {
    		ts := timestamppb.New(time.Unix(0, *snapshotMillis*1000))
    		if !ts.IsValid() {
    			log.Fatalf("Invalid snapshot millis (%d): %v", *snapshotMillis, err)
    		}
    		createReadSessionRequest.ReadSession.[TableModifiers](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/storage/apiv1beta1/storagepb.html#cloud_google_com_go_bigquery_storage_apiv1beta1_storagepb_TableModifiers) = &storagepb.ReadSession_TableModifiers{
    			SnapshotTime: ts,
    		}
    	}
    
    	// Create the session from the request.
    	session, err := bqReadClient.CreateReadSession(ctx, createReadSessionRequest, rpcOpts)
    	if err != nil {
    		log.Fatalf("CreateReadSession: %v", err)
    	}
    	fmt.Printf("Read session: %s\n", session.GetName())
    
    	if len(session.GetStreams()) == 0 {
    		log.Fatalf("no streams in session.  if this was a small query result, consider writing to output to a named table.")
    	}
    
    	// We'll use only a single stream for reading data from the table.  Because
    	// of dynamic sharding, this will yield all the rows in the table. However,
    	// if you wanted to fan out multiple readers you could do so by having a
    	// increasing the MaxStreamCount.
    	readStream := session.GetStreams()[0].Name
    
    	ch := make(chan *storagepb.ReadRowsResponse)
    
    	// Use a waitgroup to coordinate the reading and decoding goroutines.
    	var wg sync.WaitGroup
    
    	// Start the reading in one goroutine.
    	wg.Add(1)
    	go func() {
    		defer wg.Done()
    		if err := processStream(ctx, bqReadClient, readStream, ch); err != nil {
    			log.Fatalf("processStream failure: %v", err)
    		}
    		close(ch)
    	}()
    
    	// Start Avro processing and decoding in another goroutine.
    	wg.Add(1)
    	go func() {
    		defer wg.Done()
    		var err error
    		switch *format {
    		case ARROW_FORMAT:
    			err = processArrow(ctx, session.GetArrowSchema().GetSerializedSchema(), ch)
    		case AVRO_FORMAT:
    			err = processAvro(ctx, session.GetAvroSchema().GetSchema(), ch)
    		}
    		if err != nil {
    			log.Fatalf("error processing %s: %v", *format, err)
    		}
    	}()
    
    	// Wait until both the reading and decoding goroutines complete.
    	wg.Wait()
    
    }
    
    // printDatum prints the decoded row datum.
    func printDatum(d interface{}) {
    	m, ok := d.(map[string]interface{})
    	if !ok {
    		log.Printf("failed type assertion: %v", d)
    	}
    	// Go's map implementation returns keys in a random ordering, so we sort
    	// the keys before accessing.
    	keys := make([]string, len(m))
    	i := 0
    	for k := range m {
    		keys[i] = k
    		i++
    	}
    	sort.Strings(keys)
    	for _, key := range keys {
    		fmt.Printf("%s: %-20v ", key, valueFromTypeMap(m[key]))
    	}
    	fmt.Println()
    }
    
    // printRecordBatch prints the arrow record batch
    func printRecordBatch(record arrow.Record) error {
    	out, err := record.MarshalJSON()
    	if err != nil {
    		return err
    	}
    	list := []map[string]interface{}{}
    	err = json.Unmarshal(out, &list)
    	if err != nil {
    		return err
    	}
    	if len(list) == 0 {
    		return nil
    	}
    	first := list[0]
    	keys := make([]string, len(first))
    	i := 0
    	for k := range first {
    		keys[i] = k
    		i++
    	}
    	sort.Strings(keys)
    	builder := strings.Builder{}
    	for _, m := range list {
    		for _, key := range keys {
    			builder.WriteString(fmt.Sprintf("%s: %-20v ", key, m[key]))
    		}
    		builder.WriteString("\n")
    	}
    	fmt.Print(builder.String())
    	return nil
    }
    
    // valueFromTypeMap returns the first value/key in the type map.  This function
    // is only suitable for simple schemas, as complex typing such as arrays and
    // records necessitate a more robust implementation.  See the goavro library
    // and the Avro specification for more information.
    func valueFromTypeMap(field interface{}) interface{} {
    	m, ok := field.(map[string]interface{})
    	if !ok {
    		return nil
    	}
    	for _, v := range m {
    		// Return the first key encountered.
    		return v
    	}
    	return nil
    }
    
    // processStream reads rows from a single storage Stream, and sends the Storage Response
    // data blocks to a channel. This function will retry on transient stream
    // failures and bookmark progress to avoid re-reading data that's already been
    // successfully transmitted.
    func processStream(ctx context.Context, client *bqStorage.BigQueryReadClient, st string, ch chan<- *storagepb.ReadRowsResponse) error {
    	var offset int64
    
    	// Streams may be long-running.  Rather than using a global retry for the
    	// stream, implement a retry that resets once progress is made.
    	retryLimit := 3
    	retries := 0
    	for {
    		// Send the initiating request to start streaming row blocks.
    		rowStream, err := client.ReadRows(ctx, &storagepb.ReadRowsRequest{
    			ReadStream: st,
    			Offset:     offset,
    		}, rpcOpts)
    		if err != nil {
    			return fmt.Errorf("couldn't invoke ReadRows: %w", err)
    		}
    
    		// Process the streamed responses.
    		for {
    			r, err := rowStream.Recv()
    			if err == io.EOF {
    				return nil
    			}
    			if err != nil {
    				// If there is an error, check whether it is a retryable
    				// error with a retry delay and sleep instead of increasing
    				// retries count.
    				var retryDelayDuration time.Duration
    				if errorStatus, ok := status.FromError(err); ok && errorStatus.Code() == codes.ResourceExhausted {
    					for _, detail := range errorStatus.Details() {
    						retryInfo, ok := detail.(*errdetails.RetryInfo)
    						if !ok {
    							continue
    						}
    						retryDelay := retryInfo.GetRetryDelay()
    						retryDelayDuration = time.Duration(retryDelay.Seconds)*time.Second + time.Duration(retryDelay.Nanos)*time.Nanosecond
    						break
    					}
    				}
    				if retryDelayDuration != 0 {
    					log.Printf("processStream failed with a retryable error, retrying in %v", retryDelayDuration)
    					time.Sleep(retryDelayDuration)
    				} else {
    					retries++
    					if retries >= retryLimit {
    						return fmt.Errorf("processStream retries exhausted: %w", err)
    					}
    				}
    				// break the inner loop, and try to recover by starting a new streaming
    				// ReadRows call at the last known good offset.
    				break
    			} else {
    				// Reset retries after a successful response.
    				retries = 0
    			}
    
    			rc := r.GetRowCount()
    			if rc > 0 {
    				// Bookmark our progress in case of retries and send the rowblock on the channel.
    				offset = offset + rc
    				// We're making progress, reset retries.
    				retries = 0
    				ch <- r
    			}
    		}
    	}
    }
    
    // processArrow receives row blocks from a channel, and uses the provided Arrow
    // schema to decode the blocks into individual row messages for printing.  Will
    // continue to run until the channel is closed or the provided context is
    // cancelled.
    func processArrow(ctx context.Context, schema []byte, ch <-chan *storagepb.ReadRowsResponse) error {
    	mem := memory.NewGoAllocator()
    	buf := bytes.NewBuffer(schema)
    	r, err := ipc.NewReader(buf, ipc.WithAllocator(mem))
    	if err != nil {
    		return err
    	}
    	aschema := r.Schema()
    	for {
    		select {
    		case <-ctx.Done():
    			// Context was cancelled.  Stop.
    			return ctx.Err()
    		case rows, ok := <-ch:
    			if !ok {
    				// Channel closed, no further arrow messages.  Stop.
    				return nil
    			}
    			undecoded := rows.GetArrowRecordBatch().GetSerializedRecordBatch()
    			if len(undecoded) > 0 {
    				buf = bytes.NewBuffer(schema)
    				buf.Write(undecoded)
    				r, err = ipc.NewReader(buf, ipc.WithAllocator(mem), ipc.WithSchema(aschema))
    				if err != nil {
    					return err
    				}
    				for r.Next() {
    					rec := r.Record()
    					err = printRecordBatch(rec)
    					if err != nil {
    						return err
    					}
    				}
    			}
    		}
    	}
    }
    
    // processAvro receives row blocks from a channel, and uses the provided Avro
    // schema to decode the blocks into individual row messages for printing.  Will
    // continue to run until the channel is closed or the provided context is
    // cancelled.
    func processAvro(ctx context.Context, schema string, ch <-chan *storagepb.ReadRowsResponse) error {
    	// Establish a decoder that can process blocks of messages using the
    	// reference schema. All blocks share the same schema, so the decoder
    	// can be long-lived.
    	codec, err := goavro.NewCodec(schema)
    	if err != nil {
    		return fmt.Errorf("couldn't create codec: %w", err)
    	}
    
    	for {
    		select {
    		case <-ctx.Done():
    			// Context was cancelled.  Stop.
    			return ctx.Err()
    		case rows, ok := <-ch:
    			if !ok {
    				// Channel closed, no further avro messages.  Stop.
    				return nil
    			}
    			undecoded := rows.GetAvroRows().GetSerializedBinaryRows()
    			for len(undecoded) > 0 {
    				datum, remainingBytes, err := codec.NativeFromBinary(undecoded)
    
    				if err != nil {
    					if err == io.EOF {
    						break
    					}
    					return fmt.Errorf("decoding error with %d bytes remaining: %v", len(undecoded), err)
    				}
    				printDatum(datum)
    				undecoded = remainingBytes
    			}
    		}
    	}
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[ServerStream](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStream.html);
    import com.google.cloud.bigquery.storage.v1.[AvroRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroRows.html);
    import com.google.cloud.bigquery.storage.v1.[BigQueryReadClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadClient.html);
    import com.google.cloud.bigquery.storage.v1.[CreateReadSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest.html);
    import com.google.cloud.bigquery.storage.v1.[DataFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.DataFormat.html);
    import com.google.cloud.bigquery.storage.v1.[ReadRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsRequest.html);
    import com.google.cloud.bigquery.storage.v1.[ReadRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.html);
    import com.google.cloud.bigquery.storage.v1.[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html);
    import com.google.cloud.bigquery.storage.v1.[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html).[TableModifiers](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableModifiers.html);
    import com.google.cloud.bigquery.storage.v1.[ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html).[TableReadOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.html);
    import com.google.common.base.Preconditions;
    import com.google.protobuf.[Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html);
    import java.io.IOException;
    import org.apache.avro.Schema;
    import org.apache.avro.generic.GenericDatumReader;
    import org.apache.avro.generic.GenericRecord;
    import org.apache.avro.io.BinaryDecoder;
    import org.apache.avro.io.DatumReader;
    import org.apache.avro.io.DecoderFactory;
    
    public class StorageSample {
    
      /*
       * SimpleRowReader handles deserialization of the Avro-encoded row blocks transmitted
       * from the storage API using a generic datum decoder.
       */
      private static class SimpleRowReader {
    
        private final DatumReader<GenericRecord> datumReader;
    
        // Decoder object will be reused to avoid re-allocation and too much garbage collection.
        private BinaryDecoder decoder = null;
    
        // GenericRecord object will be reused.
        private GenericRecord row = null;
    
        public SimpleRowReader(Schema schema) {
          Preconditions.checkNotNull(schema);
          datumReader = new GenericDatumReader<>(schema);
        }
    
        /**
         * Sample method for processing AVRO rows which only validates decoding.
         *
         * @param avroRows object returned from the ReadRowsResponse.
         */
        public void processRows([AvroRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroRows.html) avroRows) throws IOException {
          decoder =
              DecoderFactory.get()
                  .binaryDecoder(avroRows.[getSerializedBinaryRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroRows.html#com_google_cloud_bigquery_storage_v1_AvroRows_getSerializedBinaryRows__)().toByteArray(), decoder);
    
          while (!decoder.isEnd()) {
            // Reusing object row
            row = datumReader.read(row, decoder);
            System.out.println(row.toString());
          }
        }
      }
    
      public static void main(String... args) throws Exception {
        // Sets your Google Cloud Platform project ID.
        // String projectId = "YOUR_PROJECT_ID";
        String projectId = args[0];
        Integer snapshotMillis = null;
        if (args.length > 1) {
          snapshotMillis = Integer.parseInt(args[1]);
        }
    
        try ([BigQueryReadClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadClient.html) client = [BigQueryReadClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BigQueryReadClient.html).create()) {
          String parent = String.format("projects/%s", projectId);
    
          // This example uses baby name data from the public datasets.
          String srcTable =
              String.format(
                  "projects/%s/datasets/%s/tables/%s",
                  "bigquery-public-data", "usa_names", "usa_1910_current");
    
          // We specify the columns to be projected by adding them to the selected fields,
          // and set a simple filter to restrict which rows are transmitted.
          [TableReadOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.html) options =
              [TableReadOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.html).newBuilder()
                  .[addSelectedFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_TableReadOptions_Builder_addSelectedFields_java_lang_String_)("name")
                  .[addSelectedFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_TableReadOptions_Builder_addSelectedFields_java_lang_String_)("number")
                  .[addSelectedFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_TableReadOptions_Builder_addSelectedFields_java_lang_String_)("state")
                  .[setRowRestriction](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_TableReadOptions_Builder_setRowRestriction_java_lang_String_)("state = \"WA\"")
                  .build();
    
          // Start specifying the read session we want created.
          [ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html).Builder sessionBuilder =
              [ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html).newBuilder()
                  .setTable(srcTable)
                  // This API can also deliver data serialized in Apache Avro format.
                  // This example leverages Apache Avro.
                  .[setDataFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_Builder_setDataFormat_com_google_cloud_bigquery_storage_v1_DataFormat_)([DataFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.DataFormat.html).AVRO)
                  .[setReadOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_Builder_setReadOptions_com_google_cloud_bigquery_storage_v1_ReadSession_TableReadOptions_)(options);
    
          // Optionally specify the snapshot time.  When unspecified, snapshot time is "now".
          if (snapshotMillis != null) {
            [Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html) t =
                [Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html).newBuilder()
                    .setSeconds(snapshotMillis / 1000)
                    .setNanos((int) ((snapshotMillis % 1000) * 1000000))
                    .build();
            [TableModifiers](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableModifiers.html) modifiers = [TableModifiers](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableModifiers.html).newBuilder().[setSnapshotTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.TableModifiers.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_TableModifiers_Builder_setSnapshotTime_com_google_protobuf_Timestamp_)(t).build();
            sessionBuilder.[setTableModifiers](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.Builder.html#com_google_cloud_bigquery_storage_v1_ReadSession_Builder_setTableModifiers_com_google_cloud_bigquery_storage_v1_ReadSession_TableModifiers_)(modifiers);
          }
    
          // Begin building the session creation request.
          [CreateReadSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest.html).Builder builder =
              [CreateReadSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest.html).newBuilder()
                  .setParent(parent)
                  .[setReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest.Builder.html#com_google_cloud_bigquery_storage_v1_CreateReadSessionRequest_Builder_setReadSession_com_google_cloud_bigquery_storage_v1_ReadSession_)(sessionBuilder)
                  .[setMaxStreamCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CreateReadSessionRequest.Builder.html#com_google_cloud_bigquery_storage_v1_CreateReadSessionRequest_Builder_setMaxStreamCount_int_)(1);
    
          // Request the session creation.
          [ReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html) session = client.createReadSession(builder.build());
    
          SimpleRowReader reader =
              new SimpleRowReader(new Schema.[Parser](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)().parse(session.[getAvroSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html#com_google_cloud_bigquery_storage_v1_ReadSession_getAvroSchema__)().getSchema()));
    
          // Assert that there are streams available in the session.  An empty table may not have
          // data available.  If no sessions are available for an anonymous (cached) table, consider
          // writing results of a query to a named table rather than consuming cached results directly.
          Preconditions.checkState(session.[getStreamsCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html#com_google_cloud_bigquery_storage_v1_ReadSession_getStreamsCount__)() > 0);
    
          // Use the first stream to perform reading.
          String streamName = session.[getStreams](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadSession.html#com_google_cloud_bigquery_storage_v1_ReadSession_getStreams_int_)(0).getName();
    
          [ReadRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsRequest.html) readRowsRequest =
              [ReadRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsRequest.html).newBuilder().[setReadStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsRequest.Builder.html#com_google_cloud_bigquery_storage_v1_ReadRowsRequest_Builder_setReadStream_java_lang_String_)(streamName).build();
    
          // Process each block of rows as they arrive and decode using our simple row reader.
          ServerStream<ReadRowsResponse> stream = client.readRowsCallable().call(readRowsRequest);
          for ([ReadRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.html) response : stream) {
            Preconditions.checkState(response.hasAvroRows());
            reader.processRows(response.getAvroRows());
          }
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-bigquery/latest/BigQueryClient). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    // Includes the autoloader for libraries installed with composer
    require __DIR__ . '/vendor/autoload.php';
    
    use Google\Cloud\BigQuery\Storage\V1\Client\BigQueryReadClient;
    use Google\Cloud\BigQuery\Storage\V1\CreateReadSessionRequest;
    use Google\Cloud\BigQuery\Storage\V1\DataFormat;
    use Google\Cloud\BigQuery\Storage\V1\ReadRowsRequest;
    use Google\Cloud\BigQuery\Storage\V1\ReadSession;
    use Google\Cloud\BigQuery\Storage\V1\ReadSession\TableModifiers;
    use Google\Cloud\BigQuery\Storage\V1\ReadSession\TableReadOptions;
    use Google\Protobuf\Timestamp;
    
    // Instantiates the client and sets the project
    $client = new BigQueryReadClient();
    $project = $client->projectName('YOUR_PROJECT_ID');
    $snapshotMillis = 'YOUR_SNAPSHOT_MILLIS';
    
    // This example reads baby name data from the below public dataset.
    $table = $client->tableName(
        'bigquery-public-data',
        'usa_names',
        'usa_1910_current'
    );
    
    //  This API can also deliver data serialized in Apache Arrow format.
    //  This example leverages Apache Avro.
    $readSession = new ReadSession();
    $readSession->setTable($table)->setDataFormat(DataFormat::AVRO);
    
    // We limit the output columns to a subset of those allowed in the table,
    // and set a simple filter to only report names from the state of
    // Washington (WA).
    $readOptions = new TableReadOptions();
    $readOptions->setSelectedFields(['name', 'number', 'state']);
    $readOptions->setRowRestriction('state = "WA"');
    $readSession->setReadOptions($readOptions);
    
    // With snapshot millis if present
    if (!empty($snapshotMillis)) {
        $timestamp = new Timestamp();
        $timestamp->setSeconds($snapshotMillis / 1000);
        $timestamp->setNanos((int) ($snapshotMillis % 1000) * 1000000);
        $tableModifier = new TableModifiers();
        $tableModifier->setSnapshotTime($timestamp);
        $readSession->setTableModifiers($tableModifier);
    }
    
    try {
        $createReadSessionRequest = (new CreateReadSessionRequest())
            ->setParent($project)
            ->setReadSession($readSession)
            ->setMaxStreamCount(1);
        $session = $client->createReadSession($createReadSessionRequest);
        $readRowsRequest = (new ReadRowsRequest())
            ->setReadStream($session->getStreams()[0]->getName());
        $stream = $client->readRows($readRowsRequest);
        // Do any local processing by iterating over the responses. The
        // google-cloud-bigquery-storage client reconnects to the API after any
        // transient network errors or timeouts.
        $schema = '';
        $names = [];
        $states = [];
        foreach ($stream->readAll() as $response) {
            $data = $response->getAvroRows()->getSerializedBinaryRows();
            if ($response->hasAvroSchema()) {
                $schema = $response->getAvroSchema()->getSchema();
            }
            $avroSchema = AvroSchema::parse($schema);
            $readIO = new AvroStringIO($data);
            $datumReader = new AvroIODatumReader($avroSchema);
    
            while (!$readIO->is_eof()) {
                $record = $datumReader->read(new AvroIOBinaryDecoder($readIO));
                $names[$record['name']] = '';
                $states[$record['state']] = '';
            }
        }
        $states = array_keys($states);
        printf(
            'Got %d unique names in states: %s' . PHP_EOL,
            count($names),
            implode(', ', $states)
        );
    } finally {
        $client->close();
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.cloud.bigquery_storage import BigQueryReadClient, [types](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.types.html)
    
    # TODO(developer): Set the project_id variable.
    # project_id = 'your-project-id'
    #
    # The read session is created in this project. This project can be
    # different from that which contains the table.
    
    client = BigQueryReadClient()
    
    # This example reads baby name data from the public datasets.
    table = "projects/{}/datasets/{}/tables/{}".format(
        "bigquery-public-data", "usa_names", "usa_1910_current"
    )
    
    requested_session = [types](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.types.html).[ReadSession](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.types.ReadSession.html)()
    requested_session.table = table
    # This API can also deliver data serialized in Apache Arrow format.
    # This example leverages Apache Avro.
    requested_session.data_format = [types](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.types.html).[DataFormat](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.types.DataFormat.html).AVRO
    
    # We limit the output columns to a subset of those allowed in the table,
    # and set a simple filter to only report names from the state of
    # Washington (WA).
    requested_session.read_options.selected_fields = ["name", "number", "state"]
    requested_session.read_options.row_restriction = 'state = "WA"'
    
    # Set a snapshot time if it's been specified.
    if snapshot_millis > 0:
        snapshot_time = [types](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.types.html).Timestamp()
        snapshot_time.FromMilliseconds(snapshot_millis)
        requested_session.table_modifiers.snapshot_time = snapshot_time
    
    parent = "projects/{}".format(project_id)
    session = [client](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.client.html).[create_read_session](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.services.big_query_read.BigQueryReadClient.html#google_cloud_bigquery_storage_v1_services_big_query_read_BigQueryReadClient_create_read_session)(
        parent=parent,
        read_session=requested_session,
        # We'll use only a single stream for reading data from the table. However,
        # if you wanted to fan out multiple readers you could do so by having a
        # reader process each individual stream.
        max_stream_count=1,
    )
    reader = [client](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.client.html).[read_rows](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.services.big_query_read.BigQueryReadClient.html#google_cloud_bigquery_storage_v1_services_big_query_read_BigQueryReadClient_read_rows)(session.streams[0].name)
    
    # The read stream contains blocks of Avro-encoded bytes. The rows() method
    # uses the fastavro library to parse these blocks as an iterable of Python
    # dictionaries. Install fastavro with the following command:
    #
    # pip install google-cloud-bigquery-storage[fastavro]
    rows = [reader](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.reader.html).[rows](https://docs.cloud.google.com/python/docs/reference/bigquerystorage/latest/google.cloud.bigquery_storage_v1.reader.ReadRowsStream.html#google_cloud_bigquery_storage_v1_reader_ReadRowsStream_rows)(session)
    
    # Do any local processing by iterating over the rows. The
    # google-cloud-bigquery-storage client reconnects to the API after any
    # transient network errors or timeouts.
    names = set()
    states = set()
    
    # fastavro returns EOFError instead of StopIterationError starting v1.8.4.
    # See https://github.com/googleapis/python-bigquery-storage/pull/687
    try:
        for row in rows:
            names.add(row["name"])
            states.add(row["state"])
    except EOFError:
        pass
    
    print("Got {} unique names in states: {}".format(len(names), ", ".join(states)))

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
