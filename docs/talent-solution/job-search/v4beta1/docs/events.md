---
url: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/events/
title: Improve the pre-trained model with client event data (v4beta1) \u00a0|\u00a0 Cloud Talent Solution - Job Search v4beta1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:02:52.277604+00:00
---

# Improve the pre-trained model with client event data (v4beta1)  |  Cloud Talent Solution - Job Search v4beta1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v4beta1 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs)



Send feedback 

#  Improve the pre-trained model with client event data (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

[Cloud Talent Solution](https://docs.cloud.google.com/talent-solution/job-search) is a service that brings machine learning to your job search experience, returning high quality results to job seekers far beyond the limitations of typical keyword-based methods. Right out of the box, CTS applies relevance models and job/skill ontologies to your job details. You can improve the results returned to job seekers by recording client events based on the activity of the job seeker.

## Record client events using `createClientEventRequest`

When a job seeker performs a specific action, you can use Job Search to record that action. For example, the job seeker or other entity interacting with the service has had a job (or a list of jobs) rendered in their view, such as in a list of search results in a compressed or clipped format. You can send an IMPRESSION event to Cloud Talent Solution to provide data on the context of the search and the results that a job seeker can see. When the job seeker clicks on a job result to view the full job description, you can send a VIEW event that registers the job seeker's interest in the chosen position.

The following example illustrates how to send a message to Cloud Talent Solution using an API. The job seeker or other entity interacting with the service has had a job (or a list of jobs) rendered in their view, such as in a list of search results in a compressed or clipped format. This event is typically associated with a job seeker viewing a list of jobs on a single page.

### Go

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	talent "cloud.google.com/go/talent/apiv4beta1"
    	"cloud.google.com/go/talent/apiv4beta1/talentpb"
    	"github.com/golang/protobuf/ptypes"
    )
    
    // createClientEvent creates a client event.
    func createClientEvent(w io.Writer, projectID string, requestID string, eventID string, relatedJobNames []string) (*talentpb.ClientEvent, error) {
    	ctx := context.Background()
    
    	// Create an eventService client.
    	c, err := talent.[NewEventClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1.html#cloud_google_com_go_talent_apiv4beta1_EventClient_NewEventClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("talent.NewEventClient: %w", err)
    	}
    	defer c.Close()
    
    	createTime, _ := ptypes.TimestampProto(time.Now())
    	clientEventToCreate := &talentpb.ClientEvent{
    		RequestId:  requestID,
    		EventId:    eventID,
    		CreateTime: createTime,
    		Event: &talentpb.ClientEvent_JobEvent{
    			JobEvent: &talentpb.JobEvent{
    				Type: talentpb.[JobEvent_VIEW](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_JobEvent_JOB_EVENT_TYPE_UNSPECIFIED_JobEvent_IMPRESSION_JobEvent_VIEW_JobEvent_VIEW_REDIRECT_JobEvent_APPLICATION_START_JobEvent_APPLICATION_FINISH_JobEvent_APPLICATION_QUICK_SUBMISSION_JobEvent_APPLICATION_REDIRECT_JobEvent_APPLICATION_START_FROM_SEARCH_JobEvent_APPLICATION_REDIRECT_FROM_SEARCH_JobEvent_APPLICATION_COMPANY_SUBMIT_JobEvent_BOOKMARK_JobEvent_NOTIFICATION_JobEvent_HIRED_JobEvent_SENT_CV_JobEvent_INTERVIEW_GRANTED),
    				Jobs: relatedJobNames,
    			},
    		},
    	}
    
    	// Construct a createJob request.
    	req := &talentpb.CreateClientEventRequest{
    		Parent:      fmt.Sprintf("projects/%s", projectID),
    		ClientEvent: clientEventToCreate,
    	}
    
    	resp, err := c.CreateClientEvent(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("CreateClientEvent: %w", err)
    	}
    
    	fmt.Fprintf(w, "Client event created: %v\n", resp.GetEvent())
    
    	return resp, nil
    }
    

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    import com.google.cloud.talent.v4beta1.ClientEvent;
    import com.google.cloud.talent.v4beta1.CreateClientEventRequest;
    import com.google.cloud.talent.v4beta1.EventServiceClient;
    import com.google.cloud.talent.v4beta1.JobEvent;
    import com.google.cloud.talent.v4beta1.TenantName;
    import com.google.protobuf.[Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;
    
    public class JobSearchCreateClientEvent {
    
      public static void createClientEvent() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String tenantId = "your-tenant-id";
        String requestId = "your-req-id-from-response-metadata";
        String eventId = "your-unique-identifier-id";
        createClientEvent(projectId, tenantId, requestId, eventId);
      }
    
      // Creates a client event.
      public static void createClientEvent(
          String projectId, String tenantId, String requestId, String eventId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try (EventServiceClient eventServiceClient = EventServiceClient.create()) {
          TenantName parent = TenantName.of(projectId, tenantId);
    
          // The timestamp of the event as seconds of UTC time since Unix epoch
          // For more information on how to create google.protobuf.Timestamps
          // See:
          // https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto
          long seconds = 3L;
          [Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html) createTime = [Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html).newBuilder().setSeconds(seconds).build();
    
          // The type of event attributed to the behavior of the end user
          JobEvent.JobEventType type = JobEvent.JobEventType.VIEW;
    
          // List of job names associated with this event
          String jobsElement = "projects/[Project ID]/tenants/[Tenant ID]/jobs/[Job ID]";
          String jobsElement2 = "projects/[Project ID]/tenants/[Tenant ID]/jobs/[Job ID]";
    
          List<String> jobs = Arrays.asList(jobsElement, jobsElement2);
          JobEvent jobEvent = JobEvent.newBuilder().setType(type).addAllJobs(jobs).build();
          ClientEvent clientEvent =
              ClientEvent.newBuilder()
                  .setRequestId(requestId)
                  .setEventId(eventId)
                  .setCreateTime(createTime)
                  .setJobEvent(jobEvent)
                  .build();
          CreateClientEventRequest request =
              CreateClientEventRequest.newBuilder()
                  .setParent(parent.toString())
                  .setClientEvent(clientEvent)
                  .build();
          ClientEvent response = eventServiceClient.createClientEvent(request);
          System.out.println("Created client event. ");
          System.out.println(response.toString());
        }
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    from google.cloud import talent
    from google.cloud.talent import enums
    
    
    def create_client_event(project_id, tenant_id, request_id, event_id):
        """
        Creates a client event
    
        Args:
          project_id Your Google Cloud Project ID
          tenant_id Identifier of the Tenant
          request_id A unique ID generated in the API responses.
          Value should be set to the request_id from an API response.
          event_id A unique identifier, generated by the client application
        """
    
        client = talent.[EventServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient.html)()
    
        # project_id = 'Your Google Cloud Project ID'
        # tenant_id = 'Your Tenant ID (using tenancy is optional)'
        # request_id = '[request_id from ResponseMetadata]'
        # event_id = '[Set this to a unique identifier]'
    
        if isinstance(project_id, bytes):
            project_id = project_id.decode("utf-8")
        if isinstance(tenant_id, bytes):
            tenant_id = tenant_id.decode("utf-8")
        if isinstance(request_id, bytes):
            request_id = request_id.decode("utf-8")
        if isinstance(event_id, bytes):
            event_id = event_id.decode("utf-8")
        parent = f"projects/{project_id}/tenants/{tenant_id}"
    
        # The timestamp of the event as seconds of UTC time since Unix epoch
        # For more information on how to create google.protobuf.Timestamps
        # See:
        # https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto
        seconds = 0
        create_time = {"seconds": seconds}
    
        # The type of event attributed to the behavior of the end user
        type_ = enums.[JobEvent](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.JobEvent.html).[JobEventType](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.JobEvent.JobEventType.html).VIEW
    
        # List of job names associated with this event
        jobs_element = "projects/[Project ID]/tenants/[Tenant ID]/jobs/[Job ID]"
        jobs_element_2 = "projects/[Project ID]/tenants/[Tenant ID]/jobs/[Job ID]"
        jobs = [jobs_element, jobs_element_2]
        job_event = {"type": type_, "jobs": jobs}
        client_event = {
            "request_id": request_id,
            "event_id": event_id,
            "create_time": create_time,
            "job_event": job_event,
        }
    
        response = client.create_client_event(parent=parent, client_event=client_event)
        print(response)
    
    

## Event messages

Required fields:

  * `eventId` (Customer defined): Each message sent to Cloud Talent Solution must have a unique `eventId`. As a best practice, incorporate the timestamp while defining this field to ensure non-duplicity. The maximum length of this field is 255 characters.

  * `requestId`: The value of the `requestId` returned by the search response object. This value is unique to a particular `SearchJobsRequest` API call. It is used for all subsequent messages stemming from the original search IMPRESSION event. When a new `SearchJobsRequest` API call is made (for example: job seeker goes to the next page of results) the `requestId` changes.

  * `createTime` The timestamp of the event (in [Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp) format, accurate to nanoseconds. This timestamp should reflect when the event actually occurred, not when the message was sent.

  * Union field `event`: Can be one of either `jobEvent` or `profileEvent`. [`jobEvent`](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/ClientEvent#JobEvent) objects are used with the Job Search feature and are issued when a job seeker interacts with the service. 




## Sample event message

The API call in the code sample above should generate a JSON message in the following format:

### JSON
    
    
    {
      "requestId": string,
      "eventId": string,
      "createTime": string,
      "eventNotes": string,
    
    
    
    // Union field event can be only one of the following:
      "jobEvent": {
        object (JobEvent)
      },
      "profileEvent": {
        object (ProfileEvent)
      }
      // End of list of possible types for union field event.
    }
        

## Scenarios and workflows

The following are two example scenarios of the job seeker searching, viewing, and applying for a job.

### Workflow 1

  1. Job seeker performs a search. For example: _Product mgr SF_

Search results are returned to the job seeker.

The job search response object sent back to the customer's server contains a unique `requestId` (for example: `8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==`). Use this `requestId` for all future messages related to this particular SearchJobsRequest API call.

Send Cloud Talent Solution an [IMPRESSION](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/client-event#EventType.ENUM_VALUES.IMPRESSION) message.

Sample event message:
         
         {
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "eventId": "ID1",
           "createTime": "2018-12-19T16:39:57-08:00",
           "jobEvent":
           {"type":"IMPRESSION",
           "jobs":["jobs/4000000000", "jobs/4000000001","jobs/4000000002",
           "jobs/4000000003", "jobs/4000000004"]}
         }
         

  2. Job seeker selects a result (a job posting) to view the full details of the job.

Send Cloud Talent Solution a VIEW message.
         
         {
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "eventId": "ID2",
           "createTime": "2018-12-19T16:40:57-08:00",
           "jobEvent":
           {"type":"VIEW",
           "jobs":["jobs/4000000000"]}
         
         }
         

**Note:** A VIEW event follows an IMPRESSION event.
  3. Job seeker applies to the viewed job posting.

a. If the job seeker is redirected to a page within the same domain (an internal application page), send Cloud Talent Solution an APPLICATION_START message.
         
         {
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "eventId": "ID3",
           "createTime": "2018-12-19T16:41:57-08:00",
           "jobEvent":
           {"type":"APPLICATION_START",
         "jobs":["jobs/4000000000"]}
         }
         

b. If the job seeker is redirected to an external application page, send Cloud Talent Solution an APPLICATION_REDIRECT message.
         
         {
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "eventId": "ID3",
           "createTime": "2018-12-19T16:41:57-08:00",
           "jobEvent":
           {"type":"APPLICATION_REDIRECT",
           "jobs":["jobs/4000000000"]}
         
         }
         

  4. When the job seeker completes an internal application, send Cloud Talent Solution an APPLICATION_FINISH message:
         
         {
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "eventId": "ID4",
           "createTime": "2018-12-19T16:43:57-08:00",
           "jobEvent":
           {"type":"APPLICATION_FINISH",
           "jobs":["jobs/4000000000"]}
         
         }
         

  5. The job seeker goes back to the search results and continues to page 2 (or they continue to page 2 without having clicked on a job posting).

Send Cloud Talent Solution an IMPRESSION message with the next set of results from page 2. Note: There's a new `requestId` that is generated in the response of the `SearchJobsRequest` API call that generates the second page of results. (for example, `99e5b99c-f1ba-4f85-b17d-ccf878f451f9:APAb7IRESj+/Hzwa3bBd54P3qPx2yOWm5w==`).
         
         {
           "requestId": "99e5b99c-f1ba-4f85-b17d-ccf878f451f9:APAb7IRESj+/Hzwa3bBd54P3qPx2yOWm5w==",
           "eventId": "ID5",
           "createTime": "2018-12-19T18:39:57-08:00",
           "jobEvent":
           {"type":"IMPRESSION",
           "jobs":["jobs/4000000005", "jobs/4000000006","jobs/4000000007",
           "jobs/4000000008", "jobs/4000000009"]}
         }
         

  6. Job seeker continues to page 3 of the search results.

Send Cloud Talent Solution an IMPRESSION message with the next set of results. NOTE: There's a new `requestId` (for example, `e2d2b916-78c3-4c65-aecc-d8452bc0afb0:APAb7IRvCsNPiRXYkgF8PN5e8BkbFzKOyg==`).
         
         {
           "requestId": "e2d2b916-78c3-4c65-aecc-d8452bc0afb0:APAb7IRvCsNPiRXYkgF8PN5e8BkbFzKOyg==",
           "eventId": "ID6",
           "createTime": "2018-12-19T16:41:57-08:00",
           "jobEvent":
           {"type":"IMPRESSION",
           "jobs":["jobs/4000000010", "jobs/4000000011","jobs/4000000012",
           "jobs/400000013", "jobs/4000000014"]}
         }
         




### Workflow 2

  1. Job seeker performs a search. For example: _Product mgr SF_

Search results are returned to the job seeker.

The job search response object contains a unique `requestId` (for example: `a2179a9b-cf73-413e-8076-98af08b991ad`). Use this `requestId` for all future messages related to this `SearchJobsRequest` API call.

Send Cloud Talent Solution an IMPRESSION message.
         
         {
           "requestId": "a2179a9b-cf73-413e-8076-98af08b991ad",
           "eventId": "ID1",
           "createTime": "2018-12-19T16:39:57-08:00",
           "jobEvent":
           {"type":"IMPRESSION",
           "jobs":["jobs/4000000000", "jobs/4000000001","jobs/4000000002",
           "jobs/4000000003", "jobs/4000000004"]}
         }
         

  2. Job seeker selects a result (a job posting) to view the full details of the job.

Send Cloud Talent Solution a VIEW message.
         
         {
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "eventId": "ID2",
           "createTime": "2018-12-19T16:40:57-08:00",
           "jobEvent":
           {"type":"VIEW",
           "jobs":["jobs/4000000000"]}
         }
         

**Note:** A VIEW event follows an IMPRESSION event.
  3. Job seeker performs a single click application to a job, as outlined in [APPLICATION_QUICK_SUBMISSION](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/client-event#eventtype).

Send Cloud Talent Solution an APPLICATION_QUICK_SUBMISSION message with the next set of results.
         
         {
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "eventId": "ID3",
           "createTime": "2018-12-19T16:41:57-08:00",
           "jobEvent":
           {"type":"APPLICATION_QUICK_SUBMISSION",
           "jobs":["jobs/4000000000"]}
          }
         

  4. Job seeker performs the following actions.

a. Job seeker goes back to the search results applies for a job directly from the search results page. The application process is a longer process than defined in APPLICATION_QUICK_SUBMISSION (that is, it's a multi-step application process).

Send Cloud Talent Solution an APPLICATION_START_FROM_SERP message.
         
         {
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "eventId": "ID4",
           "createTime": "2018-12-19T16:43:57-08:00",
           "jobEvent":
           {"type":"APPLICATION_START_FROM_SERP",
           "jobs":["jobs/4000000000"]}
         }
         

b. Job seeker completes the application for the job. Send Cloud Talent Solution an APPLICATION_FINISH message.
         
         {
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "eventId": "ID5",
           "createTime": "2018-12-19T16:44:57-08:00",
           "jobEvent":
           {"type":"APPLICATION_FINISH",
           "jobs":["jobs/4000000000"]}
         }
         

  5. Job seeker goes back to the search results and applies to a job directly from the search results page. The application process redirects the job seeker to another domain that is outside the tenant site (external application) from which, the progress of the applicant cannot be tracked.

Send Cloud Talent Solution an APPLICATION_REDIRECT_FROM_SERP message.
         
         {
           "requestId": "8d2bdd5d-1361-42a5-a0fd-bd2b58b7d8fb:APAb7ISd4Sc5faibw2V5hTU/OoC2WAW5AA==",
           "eventId": "ID6",
           "createTime": "2018-12-19T16:45:57-08:00",
           "jobEvent":
           {"type":"APPLICATION_START_FROM_SERP",
           "jobs":["jobs/4000000001"]}
         }
         

This is different from APPLICATION_REDIRECT where a job seeker is on the job description page when re-routed.




## Verify client event implementation

Cloud Talent Solution provides you with self service tools that you can use to verify implementation of client events. See [management tools](https://docs.cloud.google.com/talent-solution/docs/management-tools) for more information about the available self service options.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
