---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-create-client-event/
title: Create client (v4beta1) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:22.829733+00:00
---

# Create client (v4beta1)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-create-client-event/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Create client (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

Create client.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Improve the pre-trained model with client event data](https://docs.cloud.google.com/talent-solution/job-search/docs/events)
  * [Improve the pre-trained model with client event data (v4beta1)](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/events)



## Code sample

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

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/overview). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Node.js

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const talent = require('[@google-cloud/talent](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)').v4;
    
    /**
     * Creates a client event
     *
     * @param projectId {string} Your Google Cloud Project ID
     * @param tenantId {string} Identifier of the Tenant
     * @param requestId {string} A unique ID generated in the API responses.
     * Value should be set to the request_id from an API response.
     * @param eventId {string} A unique identifier, generated by the client application
     */
    function sampleCreateClientEvent(projectId, tenantId, requestId, eventId) {
      const client = new talent.[EventServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)();
      // const projectId = 'Your Google Cloud Project ID';
      // const tenantId = 'Your Tenant ID (using tenancy is optional)';
      // const requestId = '[request_id from ResponseMetadata]';
      // const eventId = '[Set this to a unique identifier]';
      const formattedParent = client.tenantPath(projectId, tenantId);
    
      // The timestamp of the event as seconds of UTC time since Unix epoch
      // For more information on how to create google.protobuf.Timestamps
      // See: https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto
      const seconds = 0;
      const createTime = {
        seconds: seconds,
      };
    
      // The type of event attributed to the behavior of the end user
      const type = 'VIEW';
    
      // List of job names associated with this event
      const jobsElement = 'projects/[Project ID]/tenants/[Tenant ID]/jobs/[Job ID]';
      const jobsElement2 =
        'projects/[Project ID]/tenants/[Tenant ID]/jobs/[Job ID]';
      const jobs = [jobsElement, jobsElement2];
      const jobEvent = {
        type: type,
        jobs: jobs,
      };
      const clientEvent = {
        requestId: requestId,
        eventId: eventId,
        createTime: createTime,
        jobEvent: jobEvent,
      };
      const request = {
        parent: formattedParent,
        clientEvent: clientEvent,
      };
      client
        .createClientEvent(request)
        .then(responses => {
          const response = responses[0];
          console.log('Created client event');
          console.log(`Response: ${response}`);
        })
        .catch(err => {
          console.error(err);
        });
    }
    

### Python

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
