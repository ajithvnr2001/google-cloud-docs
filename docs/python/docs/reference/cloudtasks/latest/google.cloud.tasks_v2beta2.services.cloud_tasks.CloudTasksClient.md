---
url: https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient
title: Class CloudTasksClient (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:39.762422+00:00
---

# Class CloudTasksClient (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CloudTasksClient (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.3  2.18.0  2.17.1  2.16.5  2.15.1  2.14.2  2.13.2  2.12.1  2.11.0  2.10.4  2.9.1  2.8.1  2.7.2  2.6.0  2.5.3  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.5.2  1.4.0  1.3.0  1.2.1 
    
    
    CloudTasksClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.tasks_v2beta2.services.cloud_tasks.transports.base.CloudTasksTransport,
                typing.Callable[
                    [...],
                    google.cloud.tasks_v2beta2.services.cloud_tasks.transports.base.CloudTasksTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Cloud Tasks allows developers to manage the execution of background work in their applications.

## Properties 

### api_endpoint

Return the API endpoint used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The API endpoint used by the client instance.  
  
### transport

Returns the transport used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`CloudTasksTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### CloudTasksClient
    
    
    CloudTasksClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.tasks_v2beta2.services.cloud_tasks.transports.base.CloudTasksTransport,
                typing.Callable[
                    [...],
                    google.cloud.tasks_v2beta2.services.cloud_tasks.transports.base.CloudTasksTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the cloud tasks client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,CloudTasksTransport,Callable[..., CloudTasksTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the CloudTasksTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that the `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTLSChannelError` | If mutual TLS transport creation failed for any reason.  
  
### __exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

**Warning:** ONLY use as a context manager if the transport is NOT shared with other clients! Exiting the with block will CLOSE the transport and may cause errors in other clients! 

### acknowledge_task
    
    
    acknowledge_task(
        request: typing.Optional[
            typing.Union[
                google.cloud.tasks_v2beta2.types.cloudtasks.AcknowledgeTaskRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        schedule_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Acknowledges a pull task.

The worker, that is, the entity that xref_leased this task must call this method to indicate that the work associated with the task has finished.

The worker must acknowledge a task within the xref_lease_duration or the lease will expire and the task will become available to be leased again. After the task is acknowledged, it will not be returned by a later xref_LeaseTasks, xref_GetTask, or xref_ListTasks.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_acknowledge_task():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[AcknowledgeTaskRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.AcknowledgeTaskRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[acknowledge_task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_acknowledge_task)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.AcknowledgeTaskRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.AcknowledgeTaskRequest), dict]`   
The request object. Request message for acknowledging a task using AcknowledgeTask.  
`name` |  `str`   
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`schedule_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Required. The task's current schedule time, available in the schedule_time returned by LeaseTasks response or RenewLease response. This restriction is to ensure that your worker currently holds the lease. This corresponds to the `schedule_time` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### cancel_lease
    
    
    cancel_lease(
        request: typing.Optional[
            typing.Union[
                google.cloud.tasks_v2beta2.types.cloudtasks.CancelLeaseRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        schedule_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.tasks_v2beta2.types.task.Task

Cancel a pull task's lease.

The worker can use this method to cancel a task's lease by setting its xref_schedule_time to now. This will make the task available to be leased to the next caller of xref_LeaseTasks.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_cancel_lease():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[CancelLeaseRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.CancelLeaseRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[cancel_lease](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_cancel_lease)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.CancelLeaseRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.CancelLeaseRequest), dict]`   
The request object. Request message for canceling a lease using CancelLease.  
`name` |  `str`   
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`schedule_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Required. The task's current schedule time, available in the schedule_time returned by LeaseTasks response or RenewLease response. This restriction is to ensure that your worker currently holds the lease. This corresponds to the `schedule_time` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tasks_v2beta2.types.Task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Task)` | A unit of scheduled work.  
  
### common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

### common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

### common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

### common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

### common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

### create_queue
    
    
    create_queue(
        request: typing.Optional[
            typing.Union[
                google.cloud.tasks_v2beta2.types.cloudtasks.CreateQueueRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        queue: typing.Optional[google.cloud.tasks_v2beta2.types.queue.Queue] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.tasks_v2beta2.types.queue.Queue

Creates a queue.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read `Overview of Queue Management and queue.yaml <https://cloud.google.com/tasks/docs/queue-yaml>`__ before using this method.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_create_queue():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[CreateQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.CreateQueueRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = client.[create_queue](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_create_queue)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.CreateQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.CreateQueueRequest), dict]`   
The request object. Request message for CreateQueue.  
`parent` |  `str`   
Required. The location name in which the queue will be created. For example: `projects/PROJECT_ID/locations/LOCATION_ID` The list of allowed locations can be obtained by calling Cloud Tasks' implementation of ListLocations. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`queue` |  `[google.cloud.tasks_v2beta2.types.Queue](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Queue)`   
Required. The queue to create. [Queue's name][google.cloud.tasks.v2beta2.Queue.name] cannot be the same as an existing queue. This corresponds to the `queue` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tasks_v2beta2.types.Queue](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Queue)` | A queue is a container of related tasks. Queues are configured to manage how those tasks are dispatched. Configurable properties include rate limits, retry options, target types, and others.  
  
### create_task
    
    
    create_task(
        request: typing.Optional[
            typing.Union[
                google.cloud.tasks_v2beta2.types.cloudtasks.CreateTaskRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        task: typing.Optional[google.cloud.tasks_v2beta2.types.task.Task] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.tasks_v2beta2.types.task.Task

Creates a task and adds it to a queue.

Tasks cannot be updated after creation; there is no UpdateTask command.

  * For [App Engine queues][google.cloud.tasks.v2beta2.AppEngineHttpTarget], the maximum task size is 100KB.
  * For xref_pull queues, the maximum task size is 1MB.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_create_task():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[CreateTaskRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.CreateTaskRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = client.[create_task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_create_task)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.CreateTaskRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.CreateTaskRequest), dict]`   
The request object. Request message for CreateTask.  
`parent` |  `str`   
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` The queue must already exist. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`task` |  `[google.cloud.tasks_v2beta2.types.Task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Task)`   
Required. The task to add. Task names have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`. The user can optionally specify a task name. If a name is not specified then the system will generate a random unique task id, which will be set in the task returned in the response. If schedule_time is not set or is in the past then Cloud Tasks will set it to the current time. Task De-duplication: Explicitly specifying a task ID enables task de-duplication. If a task's ID is identical to that of an existing task or a task that was deleted or completed recently then the call will fail with `ALREADY_EXISTS][google.rpc.Code.ALREADY_EXISTS]`. If the task's queue was created using Cloud Tasks, then another task with the same name can't be created for `1` hour after the original task was deleted or completed. If the task's queue was created using queue.yaml or queue.xml, then another task with the same name can't be created for `9` days after the original task was deleted or completed. Because there is an extra lookup cost to identify duplicate task names, these CreateTask calls have significantly increased latency. Using hashed strings for the task id or for the prefix of the task id is recommended. Choosing task ids that are sequential or have sequential prefixes, for example using a timestamp, causes an increase in latency and error rates in all task commands. The infrastructure relies on an approximately uniform distribution of task ids to store and serve tasks efficiently. This corresponds to the `task` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tasks_v2beta2.types.Task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Task)` | A unit of scheduled work.  
  
### delete_queue
    
    
    delete_queue(
        request: typing.Optional[
            typing.Union[
                google.cloud.tasks_v2beta2.types.cloudtasks.DeleteQueueRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes a queue.

This command will delete the queue even if it has tasks in it.

Note: If you delete a queue, a queue with the same name can't be created for 7 days.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read `Overview of Queue Management and queue.yaml <https://cloud.google.com/tasks/docs/queue-yaml>`__ before using this method.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_delete_queue():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[DeleteQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.DeleteQueueRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_queue](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_delete_queue)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.DeleteQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.DeleteQueueRequest), dict]`   
The request object. Request message for DeleteQueue.  
`name` |  `str`   
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_task
    
    
    delete_task(
        request: typing.Optional[
            typing.Union[
                google.cloud.tasks_v2beta2.types.cloudtasks.DeleteTaskRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes a task.

A task can be deleted if it is scheduled or dispatched. A task cannot be deleted if it has completed successfully or permanently failed.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_delete_task():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[DeleteTaskRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.DeleteTaskRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_delete_task)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.DeleteTaskRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.DeleteTaskRequest), dict]`   
The request object. Request message for deleting a task using DeleteTask.  
`name` |  `str`   
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

**Parameter**  
---  
**Name** | **Description**  
`filename` |  `str`   
The path to the service account private key json file.  
**Returns**  
---  
**Type** | **Description**  
`CloudTasksClient` | The constructed client.  
  
### from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

**Parameter**  
---  
**Name** | **Description**  
`info` |  `dict`   
The service account private key info.  
**Returns**  
---  
**Type** | **Description**  
`CloudTasksClient` | The constructed client.  
  
### from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

**Parameter**  
---  
**Name** | **Description**  
`filename` |  `str`   
The path to the service account private key json file.  
**Returns**  
---  
**Type** | **Description**  
`CloudTasksClient` | The constructed client.  
  
### get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Gets the access control policy for a xref_Queue. Returns an empty policy if the resource exists and does not have a policy set.

Authorization requires the following `Google IAM <https://cloud.google.com/iam>`__ permission on the specified resource parent:

  * `cloudtasks.queues.getIamPolicy`


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    def sample_get_iam_policy():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.GetIamPolicyRequest(
            resource="resource_value",
        )
    
        # Make the request
        response = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_get_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L111-L118), dict]`   
The request object. Request message for `GetIamPolicy` method.  
`resource` |  `str`   
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.iam.v1.policy_pb2.Policy` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
### get_location
    
    
    get_location(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.GetLocationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.location.locations_pb2.Location

Gets information about a location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.GetLocationRequest``   
The request object. Request message for `GetLocation` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.location_pb2.Location`` | Location object.  
  
### get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated. Return the API endpoint and client cert source for mutual TLS.

The client cert source is determined in the following order: (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the client cert source is None. (2) if `client_options.client_cert_source` is provided, use the provided one; if the default client cert source exists, use the default one; otherwise the client cert source is None.

The API endpoint is determined in the following order: (1) if `client_options.api_endpoint` if provided, use the provided one. (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the default mTLS endpoint; if the environment variable is "never", use the default API endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise use the default API endpoint.

More details can be found at <https://google.aip.dev/auth/4114>.

**Parameter**  
---  
**Name** | **Description**  
`client_options` |  `google.api_core.client_options.ClientOptions`   
Custom options for the client. Only the `api_endpoint` and `client_cert_source` properties may be used in this method.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTLSChannelError` | If any errors happen.  
**Returns**  
---  
**Type** | **Description**  
`Tuple[str, Callable[[], Tuple[bytes, bytes]]]` | returns the API endpoint and the client cert source to use.  
  
### get_queue
    
    
    get_queue(
        request: typing.Optional[
            typing.Union[google.cloud.tasks_v2beta2.types.cloudtasks.GetQueueRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.tasks_v2beta2.types.queue.Queue

Gets a queue.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_get_queue():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[GetQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.GetQueueRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_queue](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_get_queue)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.GetQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.GetQueueRequest), dict]`   
The request object. Request message for GetQueue.  
`name` |  `str`   
Required. The resource name of the queue. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tasks_v2beta2.types.Queue](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Queue)` | A queue is a container of related tasks. Queues are configured to manage how those tasks are dispatched. Configurable properties include rate limits, retry options, target types, and others.  
  
### get_task
    
    
    get_task(
        request: typing.Optional[
            typing.Union[google.cloud.tasks_v2beta2.types.cloudtasks.GetTaskRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.tasks_v2beta2.types.task.Task

Gets a task.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_get_task():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[GetTaskRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.GetTaskRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_get_task)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.GetTaskRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.GetTaskRequest), dict]`   
The request object. Request message for getting a task using GetTask.  
`name` |  `str`   
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tasks_v2beta2.types.Task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Task)` | A unit of scheduled work.  
  
### lease_tasks
    
    
    lease_tasks(
        request: typing.Optional[
            typing.Union[
                google.cloud.tasks_v2beta2.types.cloudtasks.LeaseTasksRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        lease_duration: typing.Optional[google.protobuf.duration_pb2.Duration] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.tasks_v2beta2.types.cloudtasks.LeaseTasksResponse

Leases tasks from a pull queue for xref_lease_duration.

This method is invoked by the worker to obtain a lease. The worker must acknowledge the task via xref_AcknowledgeTask after they have performed the work associated with the task.

The xref_payload is intended to store data that the worker needs to perform the work associated with the task. To return the payloads in the xref_response, set xref_response_view to xref_FULL.

A maximum of 10 qps of xref_LeaseTasks requests are allowed per queue. `RESOURCE_EXHAUSTED][google.rpc.Code.RESOURCE_EXHAUSTED]` is returned when this limit is exceeded. `RESOURCE_EXHAUSTED][google.rpc.Code.RESOURCE_EXHAUSTED]` is also returned when xref_max_tasks_dispatched_per_second is exceeded.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_lease_tasks():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[LeaseTasksRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.LeaseTasksRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = client.[lease_tasks](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_lease_tasks)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.LeaseTasksRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.LeaseTasksRequest), dict]`   
The request object. Request message for leasing tasks using LeaseTasks.  
`parent` |  `str`   
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`lease_duration` |  `google.protobuf.duration_pb2.Duration`   
Required. The duration of the lease. Each task returned in the response will have its schedule_time set to the current time plus the `lease_duration`. The task is leased until its schedule_time; thus, the task will not be returned to another LeaseTasks call before its schedule_time. After the worker has successfully finished the work associated with the task, the worker must call via AcknowledgeTask before the schedule_time. Otherwise the task will be returned to a later LeaseTasks call so that another worker can retry it. The maximum lease duration is 1 week. `lease_duration` will be truncated to the nearest second. This corresponds to the `lease_duration` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tasks_v2beta2.types.LeaseTasksResponse](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.LeaseTasksResponse)` | Response message for leasing tasks using LeaseTasks.  
  
### list_locations
    
    
    list_locations(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.ListLocationsRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.location.locations_pb2.ListLocationsResponse

Lists information about the supported locations for this service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.ListLocationsRequest``   
The request object. Request message for `ListLocations` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.location_pb2.ListLocationsResponse`` | Response message for `ListLocations` method.  
  
### list_queues
    
    
    list_queues(
        request: typing.Optional[
            typing.Union[
                google.cloud.tasks_v2beta2.types.cloudtasks.ListQueuesRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.tasks_v2beta2.services.cloud_tasks.pagers.ListQueuesPager

Lists queues.

Queues are returned in lexicographical order.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_list_queues():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[ListQueuesRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.ListQueuesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_queues](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_list_queues)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.ListQueuesRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.ListQueuesRequest), dict]`   
The request object. Request message for ListQueues.  
`parent` |  `str`   
Required. The location name. For example: `projects/PROJECT_ID/locations/LOCATION_ID` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tasks_v2beta2.services.cloud_tasks.pagers.ListQueuesPager](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.pagers.ListQueuesPager)` | Response message for ListQueues. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_tasks
    
    
    list_tasks(
        request: typing.Optional[
            typing.Union[google.cloud.tasks_v2beta2.types.cloudtasks.ListTasksRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.tasks_v2beta2.services.cloud_tasks.pagers.ListTasksPager

Lists the tasks in a queue.

By default, only the xref_BASIC view is retrieved due to performance considerations; xref_response_view controls the subset of information which is returned.

The tasks may be returned in any order. The ordering may change at any time.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_list_tasks():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[ListTasksRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.ListTasksRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_tasks](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_list_tasks)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.ListTasksRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.ListTasksRequest), dict]`   
The request object. Request message for listing tasks using ListTasks.  
`parent` |  `str`   
Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tasks_v2beta2.services.cloud_tasks.pagers.ListTasksPager](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.pagers.ListTasksPager)` | Response message for listing tasks using ListTasks. Iterating over this object will yield results and resolve additional pages automatically.  
  
### parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

### parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

### parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

### parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

### parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

### parse_queue_path
    
    
    parse_queue_path(path: str) -> typing.Dict[str, str]

Parses a queue path into its component segments.

### parse_task_path
    
    
    parse_task_path(path: str) -> typing.Dict[str, str]

Parses a task path into its component segments.

### pause_queue
    
    
    pause_queue(
        request: typing.Optional[
            typing.Union[
                google.cloud.tasks_v2beta2.types.cloudtasks.PauseQueueRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.tasks_v2beta2.types.queue.Queue

Pauses the queue.

If a queue is paused then the system will stop dispatching tasks until the queue is resumed via xref_ResumeQueue. Tasks can still be added when the queue is paused. A queue is paused if its xref_state is xref_PAUSED.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_pause_queue():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[PauseQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.PauseQueueRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[pause_queue](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_pause_queue)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.PauseQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.PauseQueueRequest), dict]`   
The request object. Request message for PauseQueue.  
`name` |  `str`   
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tasks_v2beta2.types.Queue](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Queue)` | A queue is a container of related tasks. Queues are configured to manage how those tasks are dispatched. Configurable properties include rate limits, retry options, target types, and others.  
  
### purge_queue
    
    
    purge_queue(
        request: typing.Optional[
            typing.Union[
                google.cloud.tasks_v2beta2.types.cloudtasks.PurgeQueueRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.tasks_v2beta2.types.queue.Queue

Purges a queue by deleting all of its tasks.

All tasks created before this method is called are permanently deleted.

Purge operations can take up to one minute to take effect. Tasks might be dispatched before the purge takes effect. A purge is irreversible.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_purge_queue():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[PurgeQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.PurgeQueueRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[purge_queue](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_purge_queue)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.PurgeQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.PurgeQueueRequest), dict]`   
The request object. Request message for PurgeQueue.  
`name` |  `str`   
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tasks_v2beta2.types.Queue](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Queue)` | A queue is a container of related tasks. Queues are configured to manage how those tasks are dispatched. Configurable properties include rate limits, retry options, target types, and others.  
  
### queue_path
    
    
    queue_path(project: str, location: str, queue: str) -> str

Returns a fully-qualified queue string.

### renew_lease
    
    
    renew_lease(
        request: typing.Optional[
            typing.Union[
                google.cloud.tasks_v2beta2.types.cloudtasks.RenewLeaseRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        schedule_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        lease_duration: typing.Optional[google.protobuf.duration_pb2.Duration] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.tasks_v2beta2.types.task.Task

Renew the current lease of a pull task.

The worker can use this method to extend the lease by a new duration, starting from now. The new task lease will be returned in the task's xref_schedule_time.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_renew_lease():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[RenewLeaseRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.RenewLeaseRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[renew_lease](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_renew_lease)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.RenewLeaseRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.RenewLeaseRequest), dict]`   
The request object. Request message for renewing a lease using RenewLease.  
`name` |  `str`   
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`schedule_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Required. The task's current schedule time, available in the schedule_time returned by LeaseTasks response or RenewLease response. This restriction is to ensure that your worker currently holds the lease. This corresponds to the `schedule_time` field on the `request` instance; if `request` is provided, this should not be set.  
`lease_duration` |  `google.protobuf.duration_pb2.Duration`   
Required. The desired new lease duration, starting from now. The maximum lease duration is 1 week. `lease_duration` will be truncated to the nearest second. This corresponds to the `lease_duration` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tasks_v2beta2.types.Task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Task)` | A unit of scheduled work.  
  
### resume_queue
    
    
    resume_queue(
        request: typing.Optional[
            typing.Union[
                google.cloud.tasks_v2beta2.types.cloudtasks.ResumeQueueRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.tasks_v2beta2.types.queue.Queue

Resume a queue.

This method resumes a queue after it has been xref_PAUSED or xref_DISABLED. The state of a queue is stored in the queue's xref_state; after calling this method it will be set to xref_RUNNING.

WARNING: Resuming many high-QPS queues at the same time can lead to target overloading. If you are resuming high-QPS queues, follow the 500/50/5 pattern described in `Managing Cloud Tasks Scaling Risks <https://cloud.google.com/tasks/docs/manage-cloud-task-scaling>`__.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_resume_queue():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[ResumeQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.ResumeQueueRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[resume_queue](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_resume_queue)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.ResumeQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.ResumeQueueRequest), dict]`   
The request object. Request message for ResumeQueue.  
`name` |  `str`   
Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tasks_v2beta2.types.Queue](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Queue)` | A queue is a container of related tasks. Queues are configured to manage how those tasks are dispatched. Configurable properties include rate limits, retry options, target types, and others.  
  
### run_task
    
    
    run_task(
        request: typing.Optional[
            typing.Union[google.cloud.tasks_v2beta2.types.cloudtasks.RunTaskRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.tasks_v2beta2.types.task.Task

Forces a task to run now.

When this method is called, Cloud Tasks will dispatch the task, even if the task is already running, the queue has reached its xref_RateLimits or is xref_PAUSED.

This command is meant to be used for manual debugging. For example, xref_RunTask can be used to retry a failed task after a fix has been made or to manually force a task to be dispatched now.

The dispatched task is returned. That is, the task that is returned contains the xref_status after the task is dispatched but before the task is received by its target.

If Cloud Tasks receives a successful response from the task's target, then the task will be deleted; otherwise the task's xref_schedule_time will be reset to the time that xref_RunTask was called plus the retry delay specified in the queue's xref_RetryConfig.

xref_RunTask returns `NOT_FOUND][google.rpc.Code.NOT_FOUND]` when it is called on a task that has already succeeded or permanently failed.

xref_RunTask cannot be called on a [pull task][google.cloud.tasks.v2beta2.PullMessage].
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_run_task():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[RunTaskRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.RunTaskRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[run_task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_run_task)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.RunTaskRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.RunTaskRequest), dict]`   
The request object. Request message for forcing a task to run now using RunTask.  
`name` |  `str`   
Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tasks_v2beta2.types.Task](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Task)` | A unit of scheduled work.  
  
### set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Sets the access control policy for a xref_Queue. Replaces any existing policy.

Note: The Cloud Console does not check queue-level IAM permissions yet. Project-level permissions are required to use the Cloud Console.

Authorization requires the following `Google IAM <https://cloud.google.com/iam>`__ permission on the specified resource parent:

  * `cloudtasks.queues.setIamPolicy`


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    def sample_set_iam_policy():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.SetIamPolicyRequest(
            resource="resource_value",
        )
    
        # Make the request
        response = client.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_set_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L103-L109), dict]`   
The request object. Request message for `SetIamPolicy` method.  
`resource` |  `str`   
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.iam.v1.policy_pb2.Policy` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
### task_path
    
    
    task_path(project: str, location: str, queue: str, task: str) -> str

Returns a fully-qualified task string.

### test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        permissions: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Returns permissions that a caller has on a xref_Queue. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND][google.rpc.Code.NOT_FOUND]` error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    def sample_test_iam_permissions():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.TestIamPermissionsRequest(
            resource="resource_value",
            permissions=['permissions_value1', 'permissions_value2'],
        )
    
        # Make the request
        response = client.[test_iam_permissions](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_test_iam_permissions)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L120-L131), dict]`   
The request object. Request message for `TestIamPermissions` method.  
`resource` |  `str`   
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`permissions` |  `MutableSequence[str]`   
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see `IAM Overview <https://cloud.google.com/iam/docs/overview#permissions>`__. This corresponds to the `permissions` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L120-L131)` | Response message for TestIamPermissions method.  
  
### update_queue
    
    
    update_queue(
        request: typing.Optional[
            typing.Union[
                google.cloud.tasks_v2beta2.types.cloudtasks.UpdateQueueRequest, dict
            ]
        ] = None,
        *,
        queue: typing.Optional[google.cloud.tasks_v2beta2.types.queue.Queue] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.tasks_v2beta2.types.queue.Queue

Updates a queue.

This method creates the queue if it does not exist and updates the queue if it does exist.

Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not.

WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read `Overview of Queue Management and queue.yaml <https://cloud.google.com/tasks/docs/queue-yaml>`__ before using this method.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_update_queue():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[UpdateQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.UpdateQueueRequest.html)(
        )
    
        # Make the request
        response = client.[update_queue](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_update_queue)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.UpdateQueueRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.UpdateQueueRequest), dict]`   
The request object. Request message for UpdateQueue.  
`queue` |  `[google.cloud.tasks_v2beta2.types.Queue](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Queue)`   
Required. The queue to create or update. The queue's name must be specified. Output only fields cannot be modified using UpdateQueue. Any value specified for an output only field will be ignored. The queue's name cannot be changed. This corresponds to the `queue` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
A mask used to specify which fields of the queue are being updated. If empty, then all fields will be updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.tasks_v2beta2.types.Queue](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Queue)` | A queue is a container of related tasks. Queues are configured to manage how those tasks are dispatched. Configurable properties include rate limits, retry options, target types, and others.  
  
### upload_queue_yaml
    
    
    upload_queue_yaml(
        request: typing.Optional[
            typing.Union[
                google.cloud.tasks_v2beta2.types.cloudtasks.UploadQueueYamlRequest, dict
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Update queue list by uploading a queue.yaml file.

The queue.yaml file is supplied in the request body as a YAML encoded string. This method was added to support gcloud clients versions before 322.0.0. New clients should use CreateQueue instead of this method.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import tasks_v2beta2
    
    def sample_upload_queue_yaml():
        # Create a client
        client = tasks_v2beta2.[CloudTasksClient](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html)()
    
        # Initialize request argument(s)
        request = tasks_v2beta2.[UploadQueueYamlRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.UploadQueueYamlRequest.html)(
            app_id="app_id_value",
        )
    
        # Make the request
        client.[upload_queue_yaml](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.services.cloud_tasks.CloudTasksClient.html#google_cloud_tasks_v2beta2_services_cloud_tasks_CloudTasksClient_upload_queue_yaml)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.tasks_v2beta2.types.UploadQueueYamlRequest](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.UploadQueueYamlRequest), dict]`   
The request object. Request message for UploadQueueYaml.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
