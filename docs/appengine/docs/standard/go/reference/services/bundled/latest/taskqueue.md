---
url: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/taskqueue/
title: Package google.golang.org/appengine/v2/taskqueue (v2.0.6) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:52.186096+00:00
---

# Package google.golang.org/appengine/v2/taskqueue (v2.0.6)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/taskqueue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package google.golang.org/appengine/v2/taskqueue (v2.0.6) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/google.golang.org/appengine/v2/taskqueue). 

Package taskqueue provides a client for App Engine's taskqueue service. Using this service, applications may perform work outside a user's request. 

A Task may be constructed manually; alternatively, since the most common taskqueue operation is to add a single POST task, NewPOSTTask makes it easy.
    
    
    t := taskqueue.NewPOSTTask("/worker", url.Values{
        "key": {key},
    })
    taskqueue.Add(c, t, "") // add t to the default queue

## Variables 

### ErrTaskAlreadyAdded
    
    
    var (
    	// ErrTaskAlreadyAdded is the error returned by Add and AddMulti when a task has already been added with a particular name.
    	ErrTaskAlreadyAdded = [errors](https://pkg.go.dev/errors).[New](https://pkg.go.dev/errors#New)("taskqueue: task has already been added")
    )

## Functions 

### func Delete 
    
    
    func Delete(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), task *Task, queueName [string](https://pkg.go.dev/builtin#string)) [error](https://pkg.go.dev/builtin#error)

Delete deletes a task from a named queue.

### func DeleteMulti 
    
    
    func DeleteMulti(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), tasks []*Task, queueName [string](https://pkg.go.dev/builtin#string)) [error](https://pkg.go.dev/builtin#error)

DeleteMulti deletes multiple tasks from a named queue. If a given task could not be deleted, an appengine.MultiError is returned. Each task is deleted independently; one may fail to delete while the others are successfully deleted.

### func ModifyLease 
    
    
    func ModifyLease(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), task *Task, queueName [string](https://pkg.go.dev/builtin#string), leaseTime [int](https://pkg.go.dev/builtin#int)) [error](https://pkg.go.dev/builtin#error)

ModifyLease modifies the lease of a task. Used to request more processing time, or to abandon processing. leaseTime is in seconds and must not be negative.

### func Purge 
    
    
    func Purge(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), queueName [string](https://pkg.go.dev/builtin#string)) [error](https://pkg.go.dev/builtin#error)

Purge removes all tasks from a queue.

## QueueStatistics
    
    
    type QueueStatistics struct {
    	Tasks     [int](https://pkg.go.dev/builtin#int)       // may be an approximation
    	OldestETA [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time) // zero if there are no pending tasks
    
    	Executed1Minute [int](https://pkg.go.dev/builtin#int)     // tasks executed in the last minute
    	InFlight        [int](https://pkg.go.dev/builtin#int)     // tasks executing now
    	EnforcedRate    [float64](https://pkg.go.dev/builtin#float64) // requests per second
    }

QueueStatistics represents statistics about a single task queue.

### func QueueStats 
    
    
    func QueueStats(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), queueNames [][string](https://pkg.go.dev/builtin#string)) ([]QueueStatistics, [error](https://pkg.go.dev/builtin#error))

QueueStats retrieves statistics about queues.

## RequestHeaders
    
    
    type RequestHeaders struct {
    	QueueName          [string](https://pkg.go.dev/builtin#string)
    	TaskName           [string](https://pkg.go.dev/builtin#string)
    	TaskRetryCount     [int64](https://pkg.go.dev/builtin#int64)
    	TaskExecutionCount [int64](https://pkg.go.dev/builtin#int64)
    	TaskETA            [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)
    
    	TaskPreviousResponse [int](https://pkg.go.dev/builtin#int)
    	TaskRetryReason      [string](https://pkg.go.dev/builtin#string)
    	FailFast             [bool](https://pkg.go.dev/builtin#bool)
    }

RequestHeaders are the special HTTP request headers available to push task HTTP request handlers. These headers are set internally by App Engine. See <https://cloud.google.com/appengine/docs/standard/go/taskqueue/push/creating-handlers#reading_request_headers> for a description of the fields.

### func ParseRequestHeaders 
    
    
    func ParseRequestHeaders(h [http](https://pkg.go.dev/net/http).[Header](https://pkg.go.dev/net/http#Header)) *RequestHeaders

ParseRequestHeaders parses the special HTTP request headers available to push task request handlers. This function silently ignores values of the wrong format.

## RetryOptions
    
    
    type RetryOptions struct {
    	// Number of tries/leases after which the task fails permanently and is deleted.
    	// If AgeLimit is also set, both limits must be exceeded for the task to fail permanently.
    	RetryLimit [int32](https://pkg.go.dev/builtin#int32)
    
    	// Maximum time allowed since the task's first try before the task fails permanently and is deleted (only for push tasks).
    	// If RetryLimit is also set, both limits must be exceeded for the task to fail permanently.
    	AgeLimit [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)
    
    	// Minimum time between successive tries (only for push tasks).
    	MinBackoff [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)
    
    	// Maximum time between successive tries (only for push tasks).
    	MaxBackoff [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration)
    
    	// Maximum number of times to double the interval between successive tries before the intervals increase linearly (only for push tasks).
    	MaxDoublings [int32](https://pkg.go.dev/builtin#int32)
    
    	// If MaxDoublings is zero, set ApplyZeroMaxDoublings to true to override the default non-zero value.
    	// Otherwise a zero MaxDoublings is ignored and the default is used.
    	ApplyZeroMaxDoublings [bool](https://pkg.go.dev/builtin#bool)
    }

RetryOptions let you control whether to retry a task and the backoff intervals between tries.

## Task
    
    
    type Task struct {
    	// Path is the worker URL for the task.
    	// If unset, it will default to /_ah/queue/

A Task represents a task to be executed.

### func Add 
    
    
    func Add(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), task *Task, queueName [string](https://pkg.go.dev/builtin#string)) (*Task, [error](https://pkg.go.dev/builtin#error))

Add adds the task to a named queue. An empty queue name means that the default queue will be used. Add returns an equivalent Task with defaults filled in, including setting the task's Name field to the chosen name if the original was empty.

### func AddMulti 
    
    
    func AddMulti(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), tasks []*Task, queueName [string](https://pkg.go.dev/builtin#string)) ([]*Task, [error](https://pkg.go.dev/builtin#error))

AddMulti adds multiple tasks to a named queue. An empty queue name means that the default queue will be used. AddMulti returns a slice of equivalent tasks with defaults filled in, including setting each task's Name field to the chosen name if the original was empty. If a given task is badly formed or could not be added, an appengine.MultiError is returned.

### func Lease 
    
    
    func Lease(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), maxTasks [int](https://pkg.go.dev/builtin#int), queueName [string](https://pkg.go.dev/builtin#string), leaseTime [int](https://pkg.go.dev/builtin#int)) ([]*Task, [error](https://pkg.go.dev/builtin#error))

Lease leases tasks from a queue. leaseTime is in seconds. The number of tasks fetched will be at most maxTasks.

### func LeaseByTag 
    
    
    func LeaseByTag(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), maxTasks [int](https://pkg.go.dev/builtin#int), queueName [string](https://pkg.go.dev/builtin#string), leaseTime [int](https://pkg.go.dev/builtin#int), tag [string](https://pkg.go.dev/builtin#string)) ([]*Task, [error](https://pkg.go.dev/builtin#error))

LeaseByTag leases tasks from a queue, grouped by tag. If tag is empty, then the returned tasks are grouped by the tag of the task with earliest ETA. leaseTime is in seconds. The number of tasks fetched will be at most maxTasks.

### func NewPOSTTask 
    
    
    func NewPOSTTask(path [string](https://pkg.go.dev/builtin#string), params [url](https://pkg.go.dev/net/url).[Values](https://pkg.go.dev/net/url#Values)) *Task

NewPOSTTask creates a Task that will POST to a path with the given form data.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
