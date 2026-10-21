---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1
title: Package google.api.servicecontrol.v1 \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:35.291998+00:00
---

# Package google.api.servicecontrol.v1  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Package google.api.servicecontrol.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[QuotaController](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.QuotaController)` (interface)
  * `[ServiceController](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.ServiceController)` (interface)
  * `[AllocateQuotaRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.AllocateQuotaRequest)` (message)
  * `[AllocateQuotaResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.AllocateQuotaResponse)` (message)
  * `[CheckError](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.CheckError)` (message)
  * `[CheckError.Code](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.CheckError.Code)` (enum)
  * `[CheckRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.CheckRequest)` (message)
  * `[CheckResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.CheckResponse)` (message)
  * `[CheckResponse.CheckInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.CheckResponse.CheckInfo)` (message)
  * `[CheckResponse.ConsumerInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.CheckResponse.ConsumerInfo)` (message)
  * `[CheckResponse.ConsumerInfo.ConsumerType](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.CheckResponse.ConsumerInfo.ConsumerType)` (enum)
  * `[Distribution](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Distribution)` (message)
  * `[Distribution.ExplicitBuckets](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Distribution.ExplicitBuckets)` (message)
  * `[Distribution.ExponentialBuckets](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Distribution.ExponentialBuckets)` (message)
  * `[Distribution.LinearBuckets](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Distribution.LinearBuckets)` (message)
  * `[HttpRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.HttpRequest)` (message)
  * `[LogEntry](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.LogEntry)` (message)
  * `[LogEntryOperation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.LogEntryOperation)` (message)
  * `[LogEntrySourceLocation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.LogEntrySourceLocation)` (message)
  * `[MetricValue](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.MetricValue)` (message)
  * `[MetricValueSet](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.MetricValueSet)` (message)
  * `[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation)` (message)
  * `[Operation.Importance](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation.Importance)` (enum)
  * `[QuotaError](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.QuotaError)` (message)
  * `[QuotaError.Code](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.QuotaError.Code)` (enum)
  * `[QuotaOperation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.QuotaOperation)` (message)
  * `[QuotaOperation.QuotaMode](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.QuotaOperation.QuotaMode)` (enum)
  * `[ReportRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.ReportRequest)` (message)
  * `[ReportResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.ReportResponse)` (message)
  * `[ReportResponse.ReportError](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.ReportResponse.ReportError)` (message)
  * `[TraceSpan](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TraceSpan)` (message)
  * `[TraceSpan.AttributeValue](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TraceSpan.AttributeValue)` (message)
  * `[TraceSpan.Attributes](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TraceSpan.Attributes)` (message)
  * `[TraceSpan.SpanKind](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TraceSpan.SpanKind)` (enum)
  * `[TruncatableString](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TruncatableString)` (message)



## QuotaController

[Google Quota Control API](https://docs.cloud.google.com/service-control/overview)

Allows clients to allocate and release quota against a [managed service](https://cloud.google.com/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService).

AllocateQuota  
---  
` rpc AllocateQuota(`[AllocateQuotaRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.AllocateQuotaRequest)`) returns (`[AllocateQuotaResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.AllocateQuotaResponse)`) ` Attempts to allocate quota for the specified consumer. It should be called before the operation is executed.This method requires the `servicemanagement.services.quota` permission on the specified service. For more information, see [Cloud IAM](https://cloud.google.com/iam).**NOTE:** The client **must** fail-open on server errors `INTERNAL`, `UNKNOWN`, `DEADLINE_EXCEEDED`, and `UNAVAILABLE`. To ensure system reliability, the server may inject these errors to prohibit any hard dependency on the quota functionality.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/servicecontrol`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## ServiceController

[Google Service Control API](https://docs.cloud.google.com/service-control/overview)

Lets clients check and report operations against a [managed service](https://cloud.google.com/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService).

Check  
---  
` rpc Check(`[CheckRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.CheckRequest)`) returns (`[CheckResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.CheckResponse)`) ` Checks whether an operation on a service should be allowed to proceed based on the configuration of the service and related policies. It must be called before the operation is executed.If feasible, the client should cache the check results and reuse them for 60 seconds. In case of any server errors, the client should rely on the cached results for much longer time to avoid outage. WARNING: There is general 60s delay for the configuration and policy propagation, therefore callers MUST NOT depend on the `Check` method having the latest policy information.NOTE: the `[CheckRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.CheckRequest)` has the size limit of 64KB.This method requires the `servicemanagement.services.check` permission on the specified service. For more information, see [Cloud IAM](https://cloud.google.com/iam).

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/servicecontrol`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
Report  
---  
` rpc Report(`[ReportRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.ReportRequest)`) returns (`[ReportResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.ReportResponse)`) ` Reports operation results to Google Service Control, such as logs and metrics. It should be called after an operation is completed.If feasible, the client should aggregate reporting data for up to 5 seconds to reduce API traffic. Limiting aggregation to 5 seconds is to reduce data loss during client crashes. Clients should carefully choose the aggregation time window to avoid data loss risk more than 0.01% for business and compliance reasons.NOTE: the `[ReportRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.ReportRequest)` has the size limit (wire-format byte size) of 1MB.This method requires the `servicemanagement.services.report` permission on the specified service. For more information, see [Google Cloud IAM](https://cloud.google.com/iam).

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/servicecontrol`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## AllocateQuotaRequest

Request message for the AllocateQuota method.

Fields  
---  
`service_name` |  `string` Name of the service as specified in the service configuration. For example, `"pubsub.googleapis.com"`.See `google.api.Service` for the definition of a service name. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.quota`

  
`allocate_operation` |  ``[QuotaOperation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.QuotaOperation)`` Operation that describes the quota allocation.  
`service_config_id` |  `string` Specifies which version of service configuration should be used to process the request. If unspecified or no matching version can be found, the latest one will be used.  
  
## AllocateQuotaResponse

Response message for the AllocateQuota method.

Fields  
---  
`operation_id` |  `string` The same operation_id value used in the AllocateQuotaRequest. Used for logging and diagnostics purposes.  
`allocate_errors[]` |  ``[QuotaError](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.QuotaError)`` Indicates the decision of the allocate.  
`quota_metrics[]` |  ``[MetricValueSet](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.MetricValueSet)`` Quota metrics to indicate the result of allocation. Depending on the request, one or more of the following metrics will be included:

  1. Per quota group or per quota metric incremental usage will be specified using the following delta metric : "serviceruntime.googleapis.com/api/consumer/quota_used_count"
  2. The quota limit reached condition will be specified using the following boolean metric : "serviceruntime.googleapis.com/quota/exceeded"

  
`service_config_id` |  `string` ID of the actual config used to process the request.  
  
## CheckError

Defines the errors to be returned in `[google.api.servicecontrol.v1.CheckResponse.check_errors](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.CheckResponse.FIELDS.repeated.google.api.servicecontrol.v1.CheckError.google.api.servicecontrol.v1.CheckResponse.check_errors)`.

Fields  
---  
`code` |  ``[Code](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.CheckError.Code)`` The error code.  
`subject` |  `string` Subject to whom this error applies. See the specific code enum for more details on this field. For example:

  * "project:"
  * "folder:"
  * "organization:"

  
`detail` |  `string` Free-form text providing details on the error cause of the error.  
`status` |  ``[Status](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc#google.rpc.Status)`` Contains public information about the check error. If available, `status.code` will be non zero and client can propagate it out as public error.  
  
## Code

Error codes for Check responses.

Enums  
---  
`ERROR_CODE_UNSPECIFIED` | This is never used in `CheckResponse`.  
`NOT_FOUND` | The consumer's project id, network container, or resource container was not found. Same as `[google.rpc.Code.NOT_FOUND](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.NOT_FOUND)`.  
`PERMISSION_DENIED` | The consumer doesn't have access to the specified resource. Same as `[google.rpc.Code.PERMISSION_DENIED](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.PERMISSION_DENIED)`.  
`RESOURCE_EXHAUSTED` | Quota check failed. Same as `[google.rpc.Code.RESOURCE_EXHAUSTED](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.RESOURCE_EXHAUSTED)`.  
`SERVICE_NOT_ACTIVATED` | The consumer hasn't activated the service.  
`BILLING_DISABLED` | The consumer cannot access the service because billing is disabled.  
`PROJECT_DELETED` | The consumer's project has been marked as deleted (soft deletion).  
`PROJECT_INVALID` | The consumer's project number or id does not represent a valid project.  
`CONSUMER_INVALID` | The input consumer info does not represent a valid consumer folder or organization.  
`IP_ADDRESS_BLOCKED` | The IP address of the consumer is invalid for the specific consumer project.  
`REFERER_BLOCKED` | The referer address of the consumer request is invalid for the specific consumer project.  
`CLIENT_APP_BLOCKED` | The client application of the consumer request is invalid for the specific consumer project.  
`API_TARGET_BLOCKED` | The API targeted by this request is invalid for the specified consumer project.  
`API_KEY_INVALID` | The consumer's API key is invalid.  
`API_KEY_EXPIRED` | The consumer's API Key has expired.  
`API_KEY_NOT_FOUND` | The consumer's API Key was not found in config record.  
`INVALID_CREDENTIAL` | The credential in the request can not be verified.  
`NAMESPACE_LOOKUP_UNAVAILABLE` | The backend server for looking up project id/number is unavailable.  
`SERVICE_STATUS_UNAVAILABLE` | The backend server for checking service status is unavailable.  
`BILLING_STATUS_UNAVAILABLE` | The backend server for checking billing status is unavailable.  
`CLOUD_RESOURCE_MANAGER_BACKEND_UNAVAILABLE` | Cloud Resource Manager backend server is unavailable.  
  
## CheckRequest

Request message for the Check method.

Fields  
---  
`service_name` |  `string` The service name as specified in its service configuration. For example, `"pubsub.googleapis.com"`.See [google.api.Service](https://cloud.google.com/service-management/reference/rpc/google.api#google.api.Service) for the definition of a service name. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.check`

  
`operation` |  ``[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation)`` The operation to be checked.  
`service_config_id` |  `string` Specifies which version of service configuration should be used to process the request.If unspecified or no matching version can be found, the latest one will be used.  
  
## CheckResponse

Response message for the Check method.

Fields  
---  
`operation_id` |  `string` The same operation_id value used in the `[CheckRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.CheckRequest)`. Used for logging and diagnostics purposes.  
`check_errors[]` |  ``[CheckError](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.CheckError)`` Indicate the decision of the check.If no check errors are present, the service should process the operation. Otherwise the service should use the list of errors to determine the appropriate action.  
`service_config_id` |  `string` The actual config id used to process the request.  
`service_rollout_id` |  `string` The current service rollout id used to process the request.  
`check_info` |  ``[CheckInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.CheckResponse.CheckInfo)`` Feedback data returned from the server during processing a Check request.  
  
## CheckInfo

Contains additional information about the check operation.

Fields  
---  
`unused_arguments[]` |  `string` A list of fields and label keys that are ignored by the server. The client doesn't need to send them for following requests to improve performance and allow better aggregation.  
`consumer_info` |  ``[ConsumerInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.CheckResponse.ConsumerInfo)`` Consumer info of this check.  
  
## ConsumerInfo

`ConsumerInfo` provides information about the consumer.

Fields  
---  
`project_number` |  `int64` The Google cloud project number, e.g. 1234567890. A value of 0 indicates no project number is found.NOTE: This field is deprecated after Chemist support flexible consumer id. New code should not depend on this field anymore.  
`type` |  ``[ConsumerType](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.CheckResponse.ConsumerInfo.ConsumerType)`` The type of the consumer which should have been defined in [Google Resource Manager](https://cloud.google.com/resource-manager/).  
`consumer_number` |  `int64` The consumer identity number, can be Google cloud project number, folder number or organization number e.g. 1234567890. A value of 0 indicates no consumer number is found.  
  
## ConsumerType

The type of the consumer as defined in [Google Resource Manager](https://cloud.google.com/resource-manager/).

Enums  
---  
`CONSUMER_TYPE_UNSPECIFIED` | This is never used.  
`PROJECT` | The consumer is a Google Cloud Project.  
`FOLDER` | The consumer is a Google Cloud Folder.  
`ORGANIZATION` | The consumer is a Google Cloud Organization.  
`SERVICE_SPECIFIC` | Service-specific resource container which is defined by the service producer to offer their users the ability to manage service control functionalities at a finer level of granularity than the PROJECT.  
  
## Distribution

Distribution represents a frequency distribution of double-valued sample points. It contains the size of the population of sample points plus additional optional information:

  * the arithmetic mean of the samples
  * the minimum and maximum of the samples
  * the sum-squared-deviation of the samples, used to compute variance
  * a histogram of the values of the sample points

Fields  
---  
`count` |  `int64` The total number of samples in the distribution. Must be >= 0.  
`mean` |  `double` The arithmetic mean of the samples in the distribution. If `count` is zero then this field must be zero.  
`minimum` |  `double` The minimum of the population of values. Ignored if `count` is zero.  
`maximum` |  `double` The maximum of the population of values. Ignored if `count` is zero.  
`sum_of_squared_deviation` |  `double` The sum of squared deviations from the mean: Sum[i=1..count]((x_i - mean)^2) where each x_i is a sample values. If `count` is zero then this field must be zero, otherwise validation of the request fails.  
`bucket_counts[]` |  `int64` The number of samples in each histogram bucket. `bucket_counts` are optional. If present, they must sum to the `count` value.The buckets are defined below in `bucket_option`. There are N buckets. `bucket_counts[0]` is the number of samples in the underflow bucket. `bucket_counts[1]` to `bucket_counts[N-1]` are the numbers of samples in each of the finite buckets. And `bucket_counts[N] is the number of samples in the overflow bucket. See the comments of`bucket_option` below for more details.Any suffix of trailing zeros may be omitted.  
`exemplars[]` |  ``[Exemplar](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api#google.api.Distribution.Exemplar)`` Example points. Must be in increasing order of `value` field.  
Union field `bucket_option`. Defines the buckets in the histogram. `bucket_option` and `bucket_counts` must be both set, or both unset.Buckets are numbered in the range of [0, N], with a total of N+1 buckets. There must be at least two buckets (a single-bucket histogram gives no information that isn't already provided by `count`).The first bucket is the underflow bucket which has a lower bound of -inf. The last bucket is the overflow bucket which has an upper bound of +inf. All other buckets (if any) are called "finite" buckets because they have finite lower and upper bounds. As described below, there are three ways to define the finite buckets.(1) Buckets with constant width. (2) Buckets with exponentially growing widths. (3) Buckets with arbitrary user-provided widths.In all cases, the buckets cover the entire real number line (-inf, +inf). Bucket upper bounds are exclusive and lower bounds are inclusive. The upper bound of the underflow bucket is equal to the lower bound of the smallest finite bucket; the lower bound of the overflow bucket is equal to the upper bound of the largest finite bucket. `bucket_option` can be only one of the following:  
`linear_buckets` |  ``[LinearBuckets](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Distribution.LinearBuckets)`` Buckets with constant width.  
`exponential_buckets` |  ``[ExponentialBuckets](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Distribution.ExponentialBuckets)`` Buckets with exponentially growing width.  
`explicit_buckets` |  ``[ExplicitBuckets](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Distribution.ExplicitBuckets)`` Buckets with arbitrary user-provided width.  
  
## ExplicitBuckets

Describing buckets with arbitrary user-provided width.

Fields  
---  
`bounds[]` |  `double` 'bound' is a list of strictly increasing boundaries between buckets. Note that a list of length N-1 defines N buckets because of fenceposting. See comments on `bucket_options` for details.The i'th finite bucket covers the interval [bound[i-1], bound[i]) where i ranges from 1 to bound_size() - 1. Note that there are no finite buckets at all if 'bound' only contains a single element; in that special case the single bound defines the boundary between the underflow and overflow buckets.bucket number lower bound upper bound i == 0 (underflow) -inf bound[i] 0 < i < bound_size() bound[i-1] bound[i] i == bound_size() (overflow) bound[i-1] +inf  
  
## ExponentialBuckets

Describing buckets with exponentially growing width.

Fields  
---  
`num_finite_buckets` |  `int32` The number of finite buckets. With the underflow and overflow buckets, the total number of buckets is `num_finite_buckets` \+ 2. See comments on `bucket_options` for details.  
`growth_factor` |  `double` The i'th exponential bucket covers the interval [scale * growth_factor^(i-1), scale * growth_factor^i) where i ranges from 1 to num_finite_buckets inclusive. Must be larger than 1.0.  
`scale` |  `double` The i'th exponential bucket covers the interval [scale * growth_factor^(i-1), scale * growth_factor^i) where i ranges from 1 to num_finite_buckets inclusive. Must be > 0.  
  
## LinearBuckets

Describing buckets with constant width.

Fields  
---  
`num_finite_buckets` |  `int32` The number of finite buckets. With the underflow and overflow buckets, the total number of buckets is `num_finite_buckets` \+ 2. See comments on `bucket_options` for details.  
`width` |  `double` The i'th linear bucket covers the interval [offset + (i-1) * width, offset + i * width) where i ranges from 1 to num_finite_buckets, inclusive. Must be strictly positive.  
`offset` |  `double` The i'th linear bucket covers the interval [offset + (i-1) * width, offset + i * width) where i ranges from 1 to num_finite_buckets, inclusive.  
  
## HttpRequest

A common proto for logging HTTP requests. Only contains semantics defined by the HTTP specification. Product-specific logging information MUST be defined in a separate message.

Fields  
---  
`request_method` |  `string` The request method. Examples: `"GET"`, `"HEAD"`, `"PUT"`, `"POST"`.  
`request_url` |  `string` The scheme (http, https), the host name, the path, and the query portion of the URL that was requested. Example: `"http://example.com/some/info?color=red"`.  
`request_size` |  `int64` The size of the HTTP request message in bytes, including the request headers and the request body.  
`status` |  `int32` The response code indicating the status of the response. Examples: 200, 404.  
`response_size` |  `int64` The size of the HTTP response message sent back to the client, in bytes, including the response headers and the response body.  
`user_agent` |  `string` The user agent sent by the client. Example: `"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Q312461; .NET CLR 1.0.3705)"`.  
`remote_ip` |  `string` The IP address (IPv4 or IPv6) of the client that issued the HTTP request. Examples: `"192.168.1.1"`, `"FE80::0202:B3FF:FE1E:8329"`.  
`server_ip` |  `string` The IP address (IPv4 or IPv6) of the origin server that the request was sent to.  
`referer` |  `string` The referer URL of the request, as defined in [HTTP/1.1 Header Field Definitions](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).  
`latency` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` The request processing latency on the server, from the time the request was received until the response was sent.  
`cache_lookup` |  `bool` Whether or not a cache lookup was attempted.  
`cache_hit` |  `bool` Whether or not an entity was served from cache (with or without validation).  
`cache_validated_with_origin_server` |  `bool` Whether or not the response was validated with the origin server before being served from cache. This field is only meaningful if `cache_hit` is True.  
`cache_fill_bytes` |  `int64` The number of HTTP response bytes inserted into cache. Set only when a cache fill was attempted.  
`protocol` |  `string` Protocol used for the request. Examples: "HTTP/1.1", "HTTP/2", "websocket"  
  
## LogEntry

An individual log entry.

Fields  
---  
`name` |  `string` Required. The log to which this log entry belongs. Examples: `"syslog"`, `"book_log"`.  
`timestamp` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The time the event described by the log entry occurred. If omitted, defaults to operation start time.  
`severity` |  ``[LogSeverity](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.logging.type#google.logging.type.LogSeverity)`` The severity of the log entry. The default value is `LogSeverity.DEFAULT`.  
`http_request` |  ``[HttpRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.HttpRequest)`` Optional. Information about the HTTP request associated with this log entry, if applicable.  
`trace` |  `string` Optional. Resource name of the trace associated with the log entry, if any. If this field contains a relative resource name, you can assume the name is relative to `//tracing.googleapis.com`. Example: `projects/my-projectid/traces/06796866738c859f2f19b7cfb3214824`  
`insert_id` |  `string` A unique ID for the log entry used for deduplication. If omitted, the implementation will generate one based on operation_id.  
`labels` |  `map<string, string>` A set of user-defined (key, value) data that provides additional information about the log entry.  
`operation` |  ``[LogEntryOperation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.LogEntryOperation)`` Optional. Information about an operation associated with the log entry, if applicable.  
`source_location` |  ``[LogEntrySourceLocation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.LogEntrySourceLocation)`` Optional. Source code location information associated with the log entry, if any.  
Union field `payload`. The log entry payload, which can be one of multiple types. `payload` can be only one of the following:  
`proto_payload` |  ``[Any](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Any)`` The log entry payload, represented as a protocol buffer that is expressed as a JSON object. The only accepted type currently is `[AuditLog](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.cloud.audit#google.cloud.audit.AuditLog)`.  
`text_payload` |  `string` The log entry payload, represented as a Unicode string (UTF-8).  
`struct_payload` |  ``[Struct](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Struct)`` The log entry payload, represented as a structure that is expressed as a JSON object.  
  
## LogEntryOperation

Additional information about a potentially long-running operation with which a log entry is associated.

Fields  
---  
`id` |  `string` Optional. An arbitrary operation identifier. Log entries with the same identifier are assumed to be part of the same operation.  
`producer` |  `string` Optional. An arbitrary producer identifier. The combination of `id` and `producer` must be globally unique. Examples for `producer`: `"MyDivision.MyBigCompany.com"`, `"github.com/MyProject/MyApplication"`.  
`first` |  `bool` Optional. Set this to True if this is the first log entry in the operation.  
`last` |  `bool` Optional. Set this to True if this is the last log entry in the operation.  
  
## LogEntrySourceLocation

Additional information about the source code location that produced the log entry.

Fields  
---  
`file` |  `string` Optional. Source file name. Depending on the runtime environment, this might be a simple name or a fully-qualified name.  
`line` |  `int64` Optional. Line within the source file. 1-based; 0 indicates no line number available.  
`function` |  `string` Optional. Human-readable name of the function or method being invoked, with optional context such as the class or package name. This information may be used in contexts such as the logs viewer, where a file and line number are less meaningful. The format can vary by language. For example: `qual.if.ied.Class.method` (Java), `dir/package.func` (Go), `function` (Python).  
  
## MetricValue

Represents a single metric value.

Fields  
---  
`labels` |  `map<string, string>` The labels describing the metric value. See comments on `[google.api.servicecontrol.v1.Operation.labels](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation.FIELDS.repeated.google.api.servicecontrol.v1.Operation.LabelsEntry.google.api.servicecontrol.v1.Operation.labels)` for the overriding relationship. Note that this map must not contain monitored resource labels.  
`start_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The start of the time period over which this metric value's measurement applies. The time period has different semantics for different metric types (cumulative, delta, and gauge). See the metric definition documentation in the service configuration for details. If not specified, `[google.api.servicecontrol.v1.Operation.start_time](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation.FIELDS.google.protobuf.Timestamp.google.api.servicecontrol.v1.Operation.start_time)` will be used.  
`end_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The end of the time period over which this metric value's measurement applies. If not specified, `[google.api.servicecontrol.v1.Operation.end_time](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation.FIELDS.google.protobuf.Timestamp.google.api.servicecontrol.v1.Operation.end_time)` will be used.  
Union field `value`. The value. The type of value used in the request must agree with the metric definition in the service configuration, otherwise the MetricValue is rejected. `value` can be only one of the following:  
`bool_value` |  `bool` A boolean value.  
`int64_value` |  `int64` A signed 64-bit integer value.  
`double_value` |  `double` A double precision floating point value.  
`string_value` |  `string` A text string value.  
`distribution_value` |  ``[Distribution](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Distribution)`` A distribution value.  
  
## MetricValueSet

Represents a set of metric values in the same metric. Each metric value in the set should have a unique combination of start time, end time, and label values.

Fields  
---  
`metric_name` |  `string` The metric name defined in the service configuration.  
`metric_values[]` |  ``[MetricValue](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.MetricValue)`` The values in this metric.  
  
## Operation

Represents information regarding an operation.

Fields  
---  
`operation_id` |  `string` Identity of the operation. This must be unique within the scope of the service that generated the operation. If the service calls Check() and Report() on the same operation, the two calls should carry the same id.UUID version 4 is recommended, though not required. In scenarios where an operation is computed from existing information and an idempotent id is desirable for deduplication purpose, UUID version 5 is recommended. See RFC 4122 for details.  
`operation_name` |  `string` Fully qualified name of the operation. Reserved for future use.  
`consumer_id` |  `string` Identity of the consumer who is using the service. This field should be filled in for the operations initiated by a consumer, but not for service-initiated operations that are not related to a specific consumer.

  * This can be in one of the following formats: 
    * project:PROJECT_ID,
    * project`_`number:PROJECT_NUMBER,
    * projects/PROJECT_ID or PROJECT_NUMBER,
    * folders/FOLDER_NUMBER,
    * organizations/ORGANIZATION_NUMBER,
    * api`_`key:API_KEY.

  
`start_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Required. Start time of the operation.  
`end_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` End time of the operation. Required when the operation is used in `[ServiceController.Report](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.ServiceController.Report)`, but optional when the operation is used in `[ServiceController.Check](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.ServiceController.Check)`.  
`labels` |  `map<string, string>` Labels describing the operation. Only the following labels are allowed:

  * Labels describing monitored resources as defined in the service configuration.
  * Default labels of metric values. When specified, labels defined in the metric value override these default.
  * The following labels defined by Google Cloud Platform: 
    * `cloud.googleapis.com/location` describing the location where the operation happened,
    * `servicecontrol.googleapis.com/user_agent` describing the user agent of the API request,
    * `servicecontrol.googleapis.com/service_agent` describing the service used to handle the API request (e.g. ESP),
    * `servicecontrol.googleapis.com/platform` describing the platform where the API is served, such as App Engine, Compute Engine, or Kubernetes Engine.

  
`metric_value_sets[]` |  ``[MetricValueSet](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.MetricValueSet)`` Represents information about this operation. Each MetricValueSet corresponds to a metric defined in the service configuration. The data type used in the MetricValueSet must agree with the data type specified in the metric definition.Within a single operation, it is not allowed to have more than one MetricValue instances that have the same metric names and identical label value combinations. If a request has such duplicated MetricValue instances, the entire request is rejected with an invalid argument error.  
`log_entries[]` |  ``[LogEntry](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.LogEntry)`` Represents information to be logged.  
`importance` |  ``[Importance](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation.Importance)`` DO NOT USE. This is an experimental field.  
`user_labels` |  `map<string, string>` Private Preview. This feature is only available for approved services.User defined labels for the resource that this operation is associated with. Only a combination of 1000 user labels per consumer project are allowed.  
`trace_spans[]` |  ``[TraceSpan](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TraceSpan)`` Unimplemented. A list of Cloud Trace spans. The span names shall contain the id of the destination project which can be either the produce or the consumer project.  
`extensions[]` |  ``[Any](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Any)`` Unimplemented.  
  
## Importance

Defines the importance of the data contained in the operation.

Enums  
---  
`LOW` | Allows data caching, batching, and aggregation. It provides higher performance with higher data loss risk.  
`HIGH` | Disables data aggregation to minimize data loss. It is for operations that contains significant monetary value or audit trail. This feature only applies to the client libraries.  
  
## QuotaError

Represents error information for `[QuotaOperation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.QuotaOperation)`.

Fields  
---  
`code` |  ``[Code](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.QuotaError.Code)`` Error code.  
`subject` |  `string` Subject to whom this error applies. See the specific enum for more details on this field. For example, "clientip:" or "project:".  
`description` |  `string` Free-form text that provides details on the cause of the error.  
`status` |  ``[Status](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc#google.rpc.Status)`` Contains additional information about the quota error. If available, `status.code` will be non zero.  
  
## Code

Error codes related to project config validations are deprecated since the quota controller methods do not perform these validations. Instead services have to call the Check method, without quota_properties field, to perform these validations before calling the quota controller methods. These methods check only for project deletion to be wipe out compliant.

Enums  
---  
`UNSPECIFIED` | This is never used.  
`RESOURCE_EXHAUSTED` | Quota allocation failed. Same as `[google.rpc.Code.RESOURCE_EXHAUSTED](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.RESOURCE_EXHAUSTED)`.  
`BILLING_NOT_ACTIVE` | Consumer cannot access the service because the service requires active billing.  
`PROJECT_DELETED` | Consumer's project has been marked as deleted (soft deletion).  
`API_KEY_INVALID` | Specified API key is invalid.  
`API_KEY_EXPIRED` | Specified API Key has expired.  
  
## QuotaOperation

Represents information regarding a quota operation.

Fields  
---  
`operation_id` |  `string` Identity of the operation. This is expected to be unique within the scope of the service that generated the operation, and guarantees idempotency in case of retries.In order to ensure best performance and latency in the Quota backends, operation_ids are optimally associated with time, so that related operations can be accessed fast in storage. For this reason, the recommended token for services that intend to operate at a high QPS is Unix time in nanos + UUID  
`method_name` |  `string` Fully qualified name of the API method for which this quota operation is requested. This name is used for matching quota rules or metric rules and billing status rules defined in service configuration.This field should not be set if any of the following is true: (1) the quota operation is performed on non-API resources. (2) quota_metrics is set because the caller is doing quota override.Example of an RPC method name: google.example.library.v1.LibraryService.CreateShelf  
`consumer_id` |  `string` Identity of the consumer for whom this quota operation is being performed.This can be in one of the following formats: project:, project_number:, api_key:.  
`labels` |  `map<string, string>` Labels describing the operation.  
`quota_metrics[]` |  ``[MetricValueSet](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.MetricValueSet)`` Represents information about this operation. Each MetricValueSet corresponds to a metric defined in the service configuration. The data type used in the MetricValueSet must agree with the data type specified in the metric definition.Within a single operation, it is not allowed to have more than one MetricValue instances that have the same metric names and identical label value combinations. If a request has such duplicated MetricValue instances, the entire request is rejected with an invalid argument error.This field is mutually exclusive with method_name.  
`quota_mode` |  ``[QuotaMode](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.QuotaOperation.QuotaMode)`` Quota mode for this operation.  
  
## QuotaMode

Supported quota modes.

Enums  
---  
`UNSPECIFIED` | Guard against implicit default. Must not be used.  
`NORMAL` | For AllocateQuota request, allocates quota for the amount specified in the service configuration or specified using the quota metrics. If the amount is higher than the available quota, allocation error will be returned and no quota will be allocated. If multiple quotas are part of the request, and one fails, none of the quotas are allocated or released.  
`BEST_EFFORT` | The operation allocates quota for the amount specified in the service configuration or specified using the quota metrics. If the amount is higher than the available quota, request does not fail but all available quota will be allocated. For rate quota, BEST_EFFORT will continue to deduct from other groups even if one does not have enough quota. For allocation, it will find the minimum available amount across all groups and deduct that amount from all the affected groups.  
`CHECK_ONLY` | For AllocateQuota request, only checks if there is enough quota available and does not change the available quota. No lock is placed on the available quota either.  
`QUERY_ONLY` | Unimplemented. When used in AllocateQuotaRequest, this returns the effective quota limit(s) in the response, and no quota check will be performed. Not supported for other requests, and even for AllocateQuotaRequest, this is currently supported only for allowlisted services.  
`ADJUST_ONLY` | The operation allocates quota for the amount specified in the service configuration or specified using the quota metrics. If the requested amount is higher than the available quota, request does not fail and remaining quota would become negative (going over the limit). Not supported for Rate Quota.  
  
## ReportRequest

Request message for the Report method.

Fields  
---  
`service_name` |  `string` The service name as specified in its service configuration. For example, `"pubsub.googleapis.com"`.See [google.api.Service](https://cloud.google.com/service-management/reference/rpc/google.api#google.api.Service) for the definition of a service name. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.report`

  
`operations[]` |  ``[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation)`` Operations to be reported.Typically the service should report one operation per request. Putting multiple operations into a single request is allowed, but should be used only when multiple operations are natually available at the time of the report.There is no limit on the number of operations in the same ReportRequest, however the ReportRequest size should be no larger than 1MB. See `[ReportResponse.report_errors](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.ReportResponse.FIELDS.repeated.google.api.servicecontrol.v1.ReportResponse.ReportError.google.api.servicecontrol.v1.ReportResponse.report_errors)` for partial failure behavior.  
`service_config_id` |  `string` Specifies which version of service config should be used to process the request.If unspecified or no matching version can be found, the latest one will be used.  
  
## ReportResponse

Response message for the Report method.

Fields  
---  
`report_errors[]` |  ``[ReportError](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.ReportResponse.ReportError)`` Partial failures, one for each `Operation` in the request that failed processing. There are three possible combinations of the RPC status:

  1. The combination of a successful RPC status and an empty `report_errors` list indicates a complete success where all `Operations` in the request are processed successfully.
  2. The combination of a successful RPC status and a non-empty `report_errors` list indicates a partial success where some `Operations` in the request succeeded. Each `Operation` that failed processing has a corresponding item in this list.
  3. A failed RPC status indicates a general non-deterministic failure. When this happens, it's impossible to know which of the 'Operations' in the request succeeded or failed.

  
`service_config_id` |  `string` The actual config id used to process the request.  
`service_rollout_id` |  `string` The current service rollout id used to process the request.  
  
## ReportError

Represents the processing error of one `[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation)` in the request.

Fields  
---  
`operation_id` |  `string` The `[Operation.operation_id](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation.FIELDS.string.google.api.servicecontrol.v1.Operation.operation_id)` value from the request.  
`status` |  ``[Status](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc#google.rpc.Status)`` Details of the error when processing the `[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation)`.  
  
## TraceSpan

A span represents a single operation within a trace. Spans can be nested to form a trace tree. Often, a trace contains a root span that describes the end-to-end latency, and one or more subspans for its sub-operations. A trace can also contain multiple root spans, or none at all. Spans do not need to be contiguous—there may be gaps or overlaps between spans in a trace.

Fields  
---  
`name` |  `string` The resource name of the span in the following format:
    
    
    projects/[PROJECT_ID]/traces/[TRACE_ID]/spans/[SPAN_ID]
    

[TRACE_ID] is a unique identifier for a trace within a project; it is a 32-character hexadecimal encoding of a 16-byte array.[SPAN_ID] is a unique identifier for a span within a trace; it is a 16-character hexadecimal encoding of an 8-byte array.  
`span_id` |  `string` The [SPAN_ID] portion of the span's resource name.  
`parent_span_id` |  `string` The [SPAN_ID] of this span's parent span. If this is a root span, then this field must be empty.  
`display_name` |  ``[TruncatableString](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TruncatableString)`` A description of the span's operation (up to 128 bytes). Stackdriver Trace displays the description in the Google Cloud Platform Console. For example, the display name can be a qualified method name or a file name and a line number where the operation is called. A best practice is to use the same display name within an application and at the same call point. This makes it easier to correlate spans in different traces.  
`start_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The start time of the span. On the client side, this is the time kept by the local machine where the span execution starts. On the server side, this is the time when the server's application handler starts running.  
`end_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The end time of the span. On the client side, this is the time kept by the local machine where the span execution ends. On the server side, this is the time when the server application handler stops running.  
`attributes` |  ``[Attributes](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TraceSpan.Attributes)`` A set of attributes on the span. You can have up to 32 attributes per span.  
`status` |  ``[Status](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc#google.rpc.Status)`` An optional final status for this span.  
`same_process_as_parent_span` |  ``[BoolValue](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.BoolValue)`` (Optional) Set this parameter to indicate whether this span is in the same process as its parent. If you do not set this parameter, Stackdriver Trace is unable to take advantage of this helpful information.  
`child_span_count` |  ``[Int32Value](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Int32Value)`` An optional number of child spans that were generated while this span was active. If set, allows implementation to detect missing child spans.  
`span_kind` |  ``[SpanKind](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TraceSpan.SpanKind)`` Distinguishes between spans generated in a particular context. For example, two spans with the same name may be distinguished using `CLIENT` (caller) and `SERVER` (callee) to identify an RPC call.  
  
## AttributeValue

The allowed types for [VALUE] in a `[KEY]:[VALUE]` attribute.

Fields  
---  
Union field `value`. The type of the value. `value` can be only one of the following:  
`string_value` |  ``[TruncatableString](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TruncatableString)`` A string up to 256 bytes long.  
`int_value` |  `int64` A 64-bit signed integer.  
`bool_value` |  `bool` A Boolean value represented by `true` or `false`.  
  
## Attributes

A set of attributes, each in the format `[KEY]:[VALUE]`.

Fields  
---  
`attribute_map` |  `map<string, `[AttributeValue](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TraceSpan.AttributeValue)`>` The set of attributes. Each attribute's key can be up to 128 bytes long. The value can be a string up to 256 bytes, a signed 64-bit integer, or the Boolean values `true` and `false`. For example:
    
    
    "/instance_id": "my-instance"
    "/http/user_agent": ""
    "/http/request_bytes": 300
    "example.com/myattribute": true
      
  
`dropped_attributes_count` |  `int32` The number of attributes that were discarded. Attributes can be discarded because their keys are too long or because there are too many attributes. If this value is 0 then all attributes are valid.  
  
## SpanKind

Type of span. Can be used to specify additional relationships between spans in addition to a parent/child relationship.

Enums  
---  
`SPAN_KIND_UNSPECIFIED` | Unspecified. Do NOT use as default. Implementations MAY assume SpanKind.INTERNAL to be default.  
`INTERNAL` | Indicates that the span is used internally. Default value.  
`SERVER` | Indicates that the span covers server-side handling of an RPC or other remote network request.  
`CLIENT` | Indicates that the span covers the client-side wrapper around an RPC or other remote request.  
`PRODUCER` | Indicates that the span describes producer sending a message to a broker. Unlike client and server, there is no direct critical path latency relationship between producer and consumer spans (e.g. publishing a message to a pubsub service).  
`CONSUMER` | Indicates that the span describes consumer receiving a message from a broker. Unlike client and server, there is no direct critical path latency relationship between producer and consumer spans (e.g. receiving a message from a pubsub service subscription).  
  
## TruncatableString

Represents a string that might be shortened to a specified length.

Fields  
---  
`value` |  `string` The shortened string. For example, if the original string is 500 bytes long and the limit of the string is 128 bytes, then `value` contains the first 128 bytes of the 500-byte string.Truncation always happens on a UTF8 character boundary. If there are multi-byte characters in the string, then the length of the shortened string might be less than the size limit.  
`truncated_byte_count` |  `int32` The number of bytes removed from the original string. If this value is 0, then the string was not shortened.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
