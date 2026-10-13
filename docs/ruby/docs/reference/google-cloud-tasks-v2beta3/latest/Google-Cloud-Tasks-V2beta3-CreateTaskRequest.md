---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-CreateTaskRequest/
title: Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::CreateTaskRequest (v0.20.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:47.446317+00:00
---

# Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::CreateTaskRequest (v0.20.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-CreateTaskRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::CreateTaskRequest (v0.20.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.2 (latest)  0.20.1  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.0  0.13.1  0.12.3  0.11.0  0.10.2  0.9.0  0.8.0  0.7.0  0.6.6 

Reference documentation and code samples for the Cloud Tasks V2beta3 API class Google::Cloud::Tasks::V2beta3::CreateTaskRequest.

Request message for [CreateTask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-CloudTasks-Client#Google__Cloud__Tasks__V2beta3__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2beta3::CloudTasks::Client#create_task \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`

The queue must already exist. 




### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`

The queue must already exist. 




**Returns**

  * (::String) — Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`

The queue must already exist. 




### #response_view
    
    
    def response_view() -> ::Google::Cloud::Tasks::V2beta3::Task::View

**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::Task::View](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task-View)) — The response_view specifies which subset of the [Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task "Google::Cloud::Tasks::V2beta3::Task \(class\)") will be returned.

By default response_view is [BASIC](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task-View#Google__Cloud__Tasks__V2beta3__Task__View__BASIC "Google::Cloud::Tasks::V2beta3::Task::View::BASIC \(constant\)"); not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains.

Authorization for [FULL](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task-View#Google__Cloud__Tasks__V2beta3__Task__View__FULL "Google::Cloud::Tasks::V2beta3::Task::View::FULL \(constant\)") requires `cloudtasks.tasks.fullView` [Google IAM](https://cloud.google.com/iam/) permission on the [Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task "Google::Cloud::Tasks::V2beta3::Task \(class\)") resource. 




### #response_view=
    
    
    def response_view=(value) -> ::Google::Cloud::Tasks::V2beta3::Task::View

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta3::Task::View](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task-View)) — The response_view specifies which subset of the [Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task "Google::Cloud::Tasks::V2beta3::Task \(class\)") will be returned.

By default response_view is [BASIC](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task-View#Google__Cloud__Tasks__V2beta3__Task__View__BASIC "Google::Cloud::Tasks::V2beta3::Task::View::BASIC \(constant\)"); not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains.

Authorization for [FULL](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task-View#Google__Cloud__Tasks__V2beta3__Task__View__FULL "Google::Cloud::Tasks::V2beta3::Task::View::FULL \(constant\)") requires `cloudtasks.tasks.fullView` [Google IAM](https://cloud.google.com/iam/) permission on the [Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task "Google::Cloud::Tasks::V2beta3::Task \(class\)") resource. 




**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::Task::View](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task-View)) — The response_view specifies which subset of the [Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task "Google::Cloud::Tasks::V2beta3::Task \(class\)") will be returned.

By default response_view is [BASIC](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task-View#Google__Cloud__Tasks__V2beta3__Task__View__BASIC "Google::Cloud::Tasks::V2beta3::Task::View::BASIC \(constant\)"); not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains.

Authorization for [FULL](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task-View#Google__Cloud__Tasks__V2beta3__Task__View__FULL "Google::Cloud::Tasks::V2beta3::Task::View::FULL \(constant\)") requires `cloudtasks.tasks.fullView` [Google IAM](https://cloud.google.com/iam/) permission on the [Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task "Google::Cloud::Tasks::V2beta3::Task \(class\)") resource. 




### #task
    
    
    def task() -> ::Google::Cloud::Tasks::V2beta3::Task

**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task)) — Required. The task to add.

Task names have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`. The user can optionally specify a task [name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task#Google__Cloud__Tasks__V2beta3__Task_name_instance_ "Google::Cloud::Tasks::V2beta3::Task#name \(method\)"). If a name is not specified then the system will generate a random unique task id, which will be set in the task returned in the [response](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task#Google__Cloud__Tasks__V2beta3__Task_name_instance_ "Google::Cloud::Tasks::V2beta3::Task#name \(method\)").

If [schedule_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task#Google__Cloud__Tasks__V2beta3__Task_schedule_time_instance_ "Google::Cloud::Tasks::V2beta3::Task#schedule_time \(method\)") is not set or is in the past then Cloud Tasks will set it to the current time.

Task De-duplication:

Explicitly specifying a task ID enables task de-duplication. If a task's ID is identical to that of an existing task or a task that was deleted or executed recently then the call will fail with [ALREADY_EXISTS][google.rpc.Code.ALREADY_EXISTS]. The IDs of deleted tasks are not immediately available for reuse. It can take up to 24 hours (or 9 days if the task's queue was created using a queue.yaml or queue.xml) for the task ID to be released and made available again.

Because there is an extra lookup cost to identify duplicate task names, these [CreateTask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-CloudTasks-Client#Google__Cloud__Tasks__V2beta3__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2beta3::CloudTasks::Client#create_task \(method\)") calls have significantly increased latency. Using hashed strings for the task id or for the prefix of the task id is recommended. Choosing task ids that are sequential or have sequential prefixes, for example using a timestamp, causes an increase in latency and error rates in all task commands. The infrastructure relies on an approximately uniform distribution of task ids to store and serve tasks efficiently. 




### #task=
    
    
    def task=(value) -> ::Google::Cloud::Tasks::V2beta3::Task

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta3::Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task)) — Required. The task to add.

Task names have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`. The user can optionally specify a task [name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task#Google__Cloud__Tasks__V2beta3__Task_name_instance_ "Google::Cloud::Tasks::V2beta3::Task#name \(method\)"). If a name is not specified then the system will generate a random unique task id, which will be set in the task returned in the [response](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task#Google__Cloud__Tasks__V2beta3__Task_name_instance_ "Google::Cloud::Tasks::V2beta3::Task#name \(method\)").

If [schedule_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task#Google__Cloud__Tasks__V2beta3__Task_schedule_time_instance_ "Google::Cloud::Tasks::V2beta3::Task#schedule_time \(method\)") is not set or is in the past then Cloud Tasks will set it to the current time.

Task De-duplication:

Explicitly specifying a task ID enables task de-duplication. If a task's ID is identical to that of an existing task or a task that was deleted or executed recently then the call will fail with [ALREADY_EXISTS][google.rpc.Code.ALREADY_EXISTS]. The IDs of deleted tasks are not immediately available for reuse. It can take up to 24 hours (or 9 days if the task's queue was created using a queue.yaml or queue.xml) for the task ID to be released and made available again.

Because there is an extra lookup cost to identify duplicate task names, these [CreateTask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-CloudTasks-Client#Google__Cloud__Tasks__V2beta3__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2beta3::CloudTasks::Client#create_task \(method\)") calls have significantly increased latency. Using hashed strings for the task id or for the prefix of the task id is recommended. Choosing task ids that are sequential or have sequential prefixes, for example using a timestamp, causes an increase in latency and error rates in all task commands. The infrastructure relies on an approximately uniform distribution of task ids to store and serve tasks efficiently. 




**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task)) — Required. The task to add.

Task names have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`. The user can optionally specify a task [name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task#Google__Cloud__Tasks__V2beta3__Task_name_instance_ "Google::Cloud::Tasks::V2beta3::Task#name \(method\)"). If a name is not specified then the system will generate a random unique task id, which will be set in the task returned in the [response](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task#Google__Cloud__Tasks__V2beta3__Task_name_instance_ "Google::Cloud::Tasks::V2beta3::Task#name \(method\)").

If [schedule_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task#Google__Cloud__Tasks__V2beta3__Task_schedule_time_instance_ "Google::Cloud::Tasks::V2beta3::Task#schedule_time \(method\)") is not set or is in the past then Cloud Tasks will set it to the current time.

Task De-duplication:

Explicitly specifying a task ID enables task de-duplication. If a task's ID is identical to that of an existing task or a task that was deleted or executed recently then the call will fail with [ALREADY_EXISTS][google.rpc.Code.ALREADY_EXISTS]. The IDs of deleted tasks are not immediately available for reuse. It can take up to 24 hours (or 9 days if the task's queue was created using a queue.yaml or queue.xml) for the task ID to be released and made available again.

Because there is an extra lookup cost to identify duplicate task names, these [CreateTask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-CloudTasks-Client#Google__Cloud__Tasks__V2beta3__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2beta3::CloudTasks::Client#create_task \(method\)") calls have significantly increased latency. Using hashed strings for the task id or for the prefix of the task id is recommended. Choosing task ids that are sequential or have sequential prefixes, for example using a timestamp, causes an increase in latency and error rates in all task commands. The infrastructure relies on an approximately uniform distribution of task ids to store and serve tasks efficiently. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
