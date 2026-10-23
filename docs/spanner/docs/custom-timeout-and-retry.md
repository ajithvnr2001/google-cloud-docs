---
url: https://docs.cloud.google.com/spanner/docs/custom-timeout-and-retry/
title: Configure custom timeouts and retries \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:47.305659+00:00
---

# Configure custom timeouts and retries  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/custom-timeout-and-retry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Configure custom timeouts and retries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to override the default timeout configuration and configure a retry policy using the Spanner client libraries.

The client libraries use default timeout and retry policy settings which are defined in the following configuration files.

  * [spanner_grpc_service_config.json](https://github.com/googleapis/googleapis/blob/master/google/spanner/v1/spanner_grpc_service_config.json)
  * [spanner_admin_instance_grpc_service_config.json](https://github.com/googleapis/googleapis/blob/master/google/spanner/admin/instance/v1/spanner_admin_instance_grpc_service_config.json)
  * [spanner_admin_database_grpc_service_config.json](https://github.com/googleapis/googleapis/blob/master/google/spanner/admin/database/v1/spanner_admin_database_grpc_service_config.json)



In the configuration files, the default timeout for operations that take a short amount of time, such as `CreateSession`, is 30 seconds. Longer operations, such as queries or reads, have a default timeout of 3600 seconds. We recommend using these defaults. However, you can set a custom timeout or retry policy in your application if necessary.

If you decide to change the timeout, set it to the actual amount of time that the application is configured to wait for the result.

**Note:** Never set a timeout that is shorter than the actual time that the application is configured to wait. Short timeouts cause your application to retry the operation more frequently than necessary.

Don't configure a retry policy that is more aggressive than the default, because too many retries might overload the backend and throttle your requests.

A retry policy is defined in each snippet, with the following characteristics:

  * The initial, or starting, wait time duration before retrying the request.
  * A maximum delay.
  * A multiplier to use with the previous wait time to calculate the next wait time, until the max is reached.
  * A set of error codes for retry operations.



In the following sample, a timeout of 60 seconds is set for the given operation. If the operation takes longer than this timeout, the operation fails with a `DEADLINE_EXCEEDED` error.

If the operation fails with an `UNAVAILABLE` error code, for example, if there is a transient network problem, the operation is retried. The client waits for 500 ms before starting the first retry attempt. If the first retry fails, the client waits for 1.5 * 500 ms = 750 ms before starting the second retry. This retry delay continues to increase until the operation either succeeds or reaches the maximum retry delay of 16 seconds. The operation fails with a `DEADLINE_EXCEEDED` error if the total time that is spent on trying the operation exceeds the total timeout value of 60 seconds.

### C++
    
    
    namespace spanner = ::google::cloud::spanner;
    using ::google::cloud::StatusOr;
    [](std::string const& project_id, std::string const& instance_id,
       std::string const& database_id) {
      // Use a truncated exponential backoff with jitter to wait between
      // retries:
      //   https://en.wikipedia.org/wiki/Exponential_backoff
      //   https://cloud.google.com/storage/docs/exponential-backoff
      auto client = spanner::Client(spanner::MakeConnection(
          spanner::Database(project_id, instance_id, database_id),
          google::cloud::Options{}
              .set<spanner::SpannerRetryPolicyOption>(
                  std::make_shared<spanner::LimitedTimeRetryPolicy>(
                      /*maximum_duration=*/std::chrono::seconds(60)))
              .set<spanner::SpannerBackoffPolicyOption>(
                  std::make_shared<spanner::ExponentialBackoffPolicy>(
                      /*initial_delay=*/std::chrono::milliseconds(500),
                      /*maximum_delay=*/std::chrono::seconds(16),
                      /*scaling=*/1.5))));
    
      std::int64_t rows_inserted;
      auto commit_result = client.Commit(
          [&client, &rows_inserted](
              spanner::Transaction txn) -> StatusOr<spanner::Mutations> {
            auto insert = client.ExecuteDml(
                std::move(txn),
                spanner::SqlStatement(
                    "INSERT INTO Singers (SingerId, FirstName, LastName)"
                    "  VALUES (20, 'George', 'Washington')"));
            if (!insert) return std::move(insert).status();
            rows_inserted = insert->RowsModified();
            return spanner::Mutations{};
          });
      if (!commit_result) throw std::move(commit_result).status();
      std::cout << "Rows inserted: " << rows_inserted;
    }

### C#
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Api.Gax.Grpc](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.html);
    using [Google.Cloud.Spanner.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.html);
    using [Google.Cloud.Spanner.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.html);
    using [Grpc.Core](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.html);
    using System;
    using System.Threading;
    using System.Threading.Tasks;
    using static Google.Cloud.Spanner.V1.TransactionOptions.Types;
    
    public class CustomTimeoutsAndRetriesAsyncSample
    {
        public async Task<long> CustomTimeoutsAndRetriesAsync(string projectId, string instanceId, string databaseId)
        {
            // Create a SessionPool.
            [SpannerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SpannerClient.html) client = [SpannerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SpannerClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SpannerClient.html#Google_Cloud_Spanner_V1_SpannerClient_Create)();
            [SessionPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SessionPool.html) sessionPool = new [SessionPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SessionPool.html)(client, new [SessionPoolOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SessionPoolOptions.html)());
    
            // Acquire a session with a read-write transaction to run a query.
            [DatabaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html) databaseName =
                [DatabaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html).[FromProjectInstanceDatabase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.Common.V1/latest/Google.Cloud.Spanner.Common.V1.DatabaseName.html#Google_Cloud_Spanner_Common_V1_DatabaseName_FromProjectInstanceDatabase_System_String_System_String_System_String_)(projectId, instanceId, databaseId);
            [TransactionOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.TransactionOptions.html) transactionOptions = new [TransactionOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.TransactionOptions.html)
            {
                ReadWrite = new ReadWrite()
            };
            using [PooledSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.PooledSession.html) session = await sessionPool.[AcquireSessionAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SessionPool.html#Google_Cloud_Spanner_V1_SessionPool_AcquireSessionAsync_Google_Cloud_Spanner_Common_V1_DatabaseName_Google_Cloud_Spanner_V1_TransactionOptions_System_Threading_CancellationToken_)(
                databaseName, transactionOptions, CancellationToken.None);
    
            [ExecuteSqlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ExecuteSqlRequest.html) request = new [ExecuteSqlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ExecuteSqlRequest.html)
            {
                Sql = "INSERT Singers (SingerId, FirstName, LastName) VALUES (20, 'George', 'Washington')"
            };
    
            // Prepare the call settings with custom timeout and retry settings.
            [CallSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html) settings = [CallSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)
                .FromExpiration([Expiration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Expiration.html).[FromTimeout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Expiration.html#Google_Api_Gax_Expiration_FromTimeout_System_TimeSpan_)(TimeSpan.[FromSeconds](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.Interval.html#Google_Cloud_Spanner_V1_Interval_FromSeconds_System_Decimal_)(60)))
                .WithRetry([RetrySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html).[FromExponentialBackoff](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html#Google_Api_Gax_Grpc_RetrySettings_FromExponentialBackoff_System_Int32_System_TimeSpan_System_TimeSpan_System_Double_System_Predicate_System_Exception__Google_Api_Gax_Grpc_RetrySettings_IJitter_)(
                    maxAttempts: 12,
                    initialBackoff: TimeSpan.[FromMilliseconds](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.Interval.html#Google_Cloud_Spanner_V1_Interval_FromMilliseconds_System_Numerics_BigInteger_)(500),
                    maxBackoff: TimeSpan.[FromSeconds](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.Interval.html#Google_Cloud_Spanner_V1_Interval_FromSeconds_System_Decimal_)(16),
                    backoffMultiplier: 1.5,
                    retryFilter: [RetrySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html).[FilterForStatusCodes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.RetrySettings.html#Google_Api_Gax_Grpc_RetrySettings_FilterForStatusCodes_Grpc_Core_StatusCode___)(
                        new [StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html)[] { [StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html).[Unavailable](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_Unavailable) })));
    
            [ResultSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ResultSet.html) result = await session.[ExecuteSqlAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.PooledSession.html#Google_Cloud_Spanner_V1_PooledSession_ExecuteSqlAsync_Google_Cloud_Spanner_V1_ExecuteSqlRequest_Google_Api_Gax_Grpc_CallSettings_)(request, settings);
            await session.[CommitAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.PooledSession.html#Google_Cloud_Spanner_V1_PooledSession_CommitAsync_Google_Cloud_Spanner_V1_CommitRequest_Google_Api_Gax_Grpc_CallSettings_)(new [CommitRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.CommitRequest.html)(), null);
    
            return result.[Stats](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ResultSet.html#Google_Cloud_Spanner_V1_ResultSet_Stats).RowCountExact;
        }
    }

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/spanner"
    	spapi "cloud.google.com/go/spanner/apiv1"
    	gax "github.com/googleapis/gax-go/v2"
    	"google.golang.org/grpc/codes"
    )
    
    func setCustomTimeoutAndRetry(w io.Writer, db string) error {
    	// Set a custom retry setting.
    	co := &spapi.CallOptions{
    		ExecuteSql: []gax.CallOption{
    			gax.WithRetry(func() gax.Retryer {
    				return gax.OnCodes([]codes.Code{
    					codes.Unavailable,
    				}, gax.Backoff{
    					Initial:    500 * time.Millisecond,
    					Max:        16000 * time.Millisecond,
    					Multiplier: 1.5,
    				})
    			}),
    		},
    	}
    	client, err := spanner.[NewClientWithConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Client_NewClientWithConfig)(context.Background(), db, spanner.[ClientConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_ClientConfig){CallOptions: co})
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	// Set timeout to 60s.
    	ctx, cancel := context.WithTimeout(context.Background(), 60*time.Second)
    	defer cancel()
    
    	_, err = client.ReadWriteTransaction(ctx, func(ctx context.Context, txn *spanner.ReadWriteTransaction) error {
    		stmt := spanner.[Statement](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/spanner/latest/index.html#cloud_google_com_go_spanner_Statement){
    			SQL: `INSERT Singers (SingerId, FirstName, LastName)
    					VALUES (20, 'George', 'Washington')`,
    		}
    
    		rowCount, err := txn.Update(ctx, stmt)
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "%d record(s) inserted.\n", rowCount)
    		return nil
    	})
    	return err
    }
    

### Java
    
    
    import com.google.api.gax.retrying.[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html);
    import com.google.api.gax.rpc.StatusCode.[Code](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Type.Code.html);
    import com.google.cloud.spanner.[DatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html);
    import com.google.cloud.spanner.[DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseId.html);
    import com.google.cloud.spanner.[Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html);
    import com.google.cloud.spanner.[SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html);
    import com.google.cloud.spanner.[Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Statement.html);
    import org.threeten.bp.Duration;
    
    class CustomTimeoutAndRetrySettingsExample {
    
      static void executeSqlWithCustomTimeoutAndRetrySettings() {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String instanceId = "my-instance";
        String databaseId = "my-database";
    
        executeSqlWithCustomTimeoutAndRetrySettings(projectId, instanceId, databaseId);
      }
    
      // Create a Spanner client with custom ExecuteSql timeout and retry settings.
      static void executeSqlWithCustomTimeoutAndRetrySettings(
          String projectId, String instanceId, String databaseId) {
        [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).Builder builder = [SpannerOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.html).newBuilder().setProjectId(projectId);
        // Set custom timeout and retry settings for the ExecuteSql RPC.
        // This must be done in a separate chain as the setRetryableCodes and setRetrySettings methods
        // return a UnaryCallSettings.Builder instead of a SpannerOptions.Builder.
        [builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Interval.html#com_google_cloud_spanner_Interval_builder__)
            .[getSpannerStubSettingsBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.Builder.html#com_google_cloud_spanner_SpannerOptions_Builder_getSpannerStubSettingsBuilder__)()
            .executeSqlSettings()
            // Configure which errors should be retried.
            .setRetryableCodes([Code](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Type.Code.html).UNAVAILABLE)
            .[setRetrySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.SpannerOptions.Builder.html#com_google_cloud_spanner_SpannerOptions_Builder_setRetrySettings_com_google_api_gax_retrying_RetrySettings_)(
                [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html).newBuilder()
                    // Configure retry delay settings.
                    // The initial amount of time to wait before retrying the request.
                    .[setInitialRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRetryDelay_org_threeten_bp_Duration_)(Duration.[ofMillis](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Interval.html#com_google_cloud_spanner_Interval_ofMillis_long_)(500))
                    // The maximum amount of time to wait before retrying. I.e. after this value is
                    // reached, the wait time will not increase further by the multiplier.
                    .[setMaxRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRetryDelay_org_threeten_bp_Duration_)(Duration.[ofSeconds](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Interval.html#com_google_cloud_spanner_Interval_ofSeconds_long_)(16))
                    // The previous wait time is multiplied by this multiplier to come up with the next
                    // wait time, until the max is reached.
                    .[setRetryDelayMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRetryDelayMultiplier_double_)(1.5)
    
                    // Configure RPC and total timeout settings.
                    // Timeout for the first RPC call. Subsequent retries will be based off this value.
                    .[setInitialRpcTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRpcTimeout_org_threeten_bp_Duration_)(Duration.[ofSeconds](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Interval.html#com_google_cloud_spanner_Interval_ofSeconds_long_)(60))
                    // The max for the per RPC timeout.
                    .[setMaxRpcTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRpcTimeout_org_threeten_bp_Duration_)(Duration.[ofSeconds](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Interval.html#com_google_cloud_spanner_Interval_ofSeconds_long_)(60))
                    // Controls the change of timeout for each retry.
                    .[setRpcTimeoutMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRpcTimeoutMultiplier_double_)(1.0)
                    // The timeout for all calls (first call + all retries).
                    .[setTotalTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setTotalTimeout_org_threeten_bp_Duration_)(Duration.[ofSeconds](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Interval.html#com_google_cloud_spanner_Interval_ofSeconds_long_)(60))
                    .build());
        // Create a Spanner client using the custom retry and timeout settings.
        try ([Spanner](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Spanner.html) spanner = [builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Interval.html#com_google_cloud_spanner_Interval_builder__).build().getService()) {
          [DatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html) client =
              spanner.getDatabaseClient([DatabaseId](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseId.html).of(projectId, instanceId, databaseId));
          client
              .[readWriteTransaction](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.DatabaseClient.html#com_google_cloud_spanner_DatabaseClient_readWriteTransaction_com_google_cloud_spanner_Options_TransactionOption____)()
              .run(transaction -> {
                String sql =
                    "INSERT INTO Singers (SingerId, FirstName, LastName)\n"
                        + "VALUES (20, 'George', 'Washington')";
                long rowCount = transaction.executeUpdate([Statement](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.Statement.html).of(sql));
                System.out.printf("%d record inserted.%n", rowCount);
                return null;
              });
        }
      }
    }

### Node.js
    
    
    // Imports the Google Cloud client library
    const {Spanner} = require('[@google-cloud/spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/overview.html)');
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'my-project-id';
    // const instanceId = 'my-instance';
    // const databaseId = 'my-database';
    
    // Creates a client
    const spanner = new [Spanner](https://docs.cloud.google.com/nodejs/docs/reference/spanner/latest/spanner/spanner.html)({
      projectId: projectId,
    });
    const UNAVAILABLE_STATUS_CODE = 14;
    const retryAndTimeoutSettings = {
      retry: {
        // The set of error codes that will be retried.
        retryCodes: [UNAVAILABLE_STATUS_CODE],
        backoffSettings: {
          // Configure retry delay settings.
          // The initial amount of time to wait before retrying the request.
          initialRetryDelayMillis: 500,
          // The maximum amount of time to wait before retrying. I.e. after this
          // value is reached, the wait time will not increase further by the
          // multiplier.
          maxRetryDelayMillis: 16000,
          // The previous wait time is multiplied by this multiplier to come up
          // with the next wait time, until the max is reached.
          retryDelayMultiplier: 1.5,
    
          // Configure RPC and total timeout settings.
          // Timeout for the first RPC call. Subsequent retries will be based off
          // this value.
          initialRpcTimeoutMillis: 60000,
          // Controls the change of timeout for each retry.
          rpcTimeoutMultiplier: 1.0,
          // The max for the per RPC timeout.
          maxRpcTimeoutMillis: 60000,
          // The timeout for all calls (first call + all retries).
          totalTimeoutMillis: 60000,
        },
      },
    };
    
    // Gets a reference to a Cloud Spanner instance and database
    const instance = spanner.instance(instanceId);
    const database = instance.database(databaseId);
    const table = database.table('Singers');
    
    const row = {
      SingerId: 16,
      FirstName: 'Martha',
      LastName: 'Waller',
    };
    
    await table.insert(row, retryAndTimeoutSettings);
    
    console.log('record inserted.');

### Python
    
    
    from google.api_core import exceptions as core_exceptions
    from google.api_core import retry
    
    # instance_id = "your-spanner-instance"
    # database_id = "your-spanner-db-id"
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    
    retry = retry.Retry(
        # Customize retry with an initial wait time of 500 milliseconds.
        initial=0.5,
        # Customize retry with a maximum wait time of 16 seconds.
        maximum=16,
        # Customize retry with a wait time multiplier per iteration of 1.5.
        multiplier=1.5,
        # Customize retry with a timeout on
        # how long a certain RPC may be retried in
        # case the server returns an error.
        timeout=60,
        # Configure which errors should be retried.
        predicate=retry.if_exception_type(
            core_exceptions.ServiceUnavailable,
        ),
    )
    
    # Set a custom retry and timeout setting.
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            "SELECT SingerId, AlbumId, AlbumTitle FROM Albums",
            # Set custom retry setting for this request
            retry=retry,
            # Set custom timeout of 60 seconds for this request
            timeout=60,
        )
    
        for row in results:
            print("SingerId: {}, AlbumId: {}, AlbumTitle: {}".format(*row))
    

### Ruby
    
    
    # project_id  = "Your Google Cloud project ID"
    # instance_id = "Your Spanner instance ID"
    # database_id = "Your Spanner database ID"
    
    require "google/cloud/spanner"
    
    spanner   = Google::Cloud::Spanner.new project: project_id
    client    = spanner.client instance_id, database_id
    row_count = 0
    
    timeout = 60.0
    retry_policy = {
      initial_delay: 0.5,
      max_delay:     16.0,
      multiplier:    1.5,
      retry_codes:   ["UNAVAILABLE"]
    }
    call_options = { timeout: timeout, retry_policy: retry_policy }
    
    client.transaction do |transaction|
      row_count = transaction.execute_update(
        "INSERT INTO Singers (SingerId, FirstName, LastName) VALUES (10, 'Virginia', 'Watson')",
        call_options: call_options
      )
    end
    
    puts "#{row_count} record inserted."

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
