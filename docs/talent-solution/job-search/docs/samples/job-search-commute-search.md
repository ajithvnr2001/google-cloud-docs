---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-commute-search/
title: Search jobs by commute distance (v4beta1) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:45.912660+00:00
---

# Search jobs by commute distance (v4beta1)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-commute-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Search jobs by commute distance (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

Search jobs by commute distance.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Commute search](https://docs.cloud.google.com/talent-solution/job-search/docs/search-commute)
  * [Commute search (v4beta1)](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/search-commute)
  * [Implementing commute search in your UI](https://docs.cloud.google.com/talent-solution/job-search/docs/commute-search)
  * [Implementing commute search in your UI (v4beta1)](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/commute-search)



## Code sample

### Go

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	talent "cloud.google.com/go/talent/apiv4beta1"
    	"cloud.google.com/go/talent/apiv4beta1/talentpb"
    	"github.com/golang/protobuf/ptypes/duration"
    	"google.golang.org/genproto/googleapis/type/latlng"
    )
    
    // commuteSearch searches for jobs within commute filter.
    func commuteSearch(w io.Writer, projectID, companyID string) error {
    	ctx := context.Background()
    
    	// Initialize a jobService client.
    	c, err := talent.[NewJobClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1.html#cloud_google_com_go_talent_apiv4beta1_JobClient_NewJobClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("talent.NewJobClient: %w", err)
    	}
    	defer c.Close()
    
    	// Construct a jobQuery request with a commute filter.
    	jobQuery := &talentpb.JobQuery{
    		CommuteFilter: &talentpb.CommuteFilter{
    			CommuteMethod:  talentpb.[CommuteMethod_TRANSIT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_CommuteMethod_COMMUTE_METHOD_UNSPECIFIED_CommuteMethod_DRIVING_CommuteMethod_TRANSIT_CommuteMethod_WALKING_CommuteMethod_CYCLING),
    			TravelDuration: &duration.Duration{Seconds: 1800},
    			StartCoordinates: &latlng.LatLng{
    				Latitude:  37.422408,
    				Longitude: -122.085609,
    			},
    		},
    	}
    	if companyID != "" {
    		jobQuery.Companies = []string{fmt.Sprintf("projects/%s/companies/%s", projectID, companyID)}
    	}
    
    	// Construct a searchJobs request with a jobQuery.
    	req := &talentpb.SearchJobsRequest{
    		Parent: fmt.Sprintf("projects/%s", projectID),
    		// Make sure to set the RequestMetadata the same as the associated
    		// search request.
    		RequestMetadata: &talentpb.RequestMetadata{
    			// Make sure to hash your userID.
    			UserId: "HashedUsrID",
    			// Make sure to hash the sessionID.
    			SessionId: "HashedSessionID",
    			// Domain of the website where the search is conducted.
    			Domain: "www.googlesample.com",
    		},
    		// Set the actual search term as defined in the jobQuery.
    		JobQuery: jobQuery,
    	}
    
    	resp, err := c.SearchJobs(ctx, req)
    	if err != nil {
    		return fmt.Errorf("SearchJobs: %w", err)
    	}
    
    	for _, job := range resp.GetMatchingJobs() {
    		fmt.Fprintf(w, "Matcing Job: %q\n", job.GetJob().GetName())
    		fmt.Fprintf(w, "Job address: %v\n", job.GetCommuteInfo().GetJobLocation().GetPostalAddress().GetAddressLines())
    	}
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/overview). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.talent.v4beta1.CommuteFilter;
    import com.google.cloud.talent.v4beta1.CommuteMethod;
    import com.google.cloud.talent.v4beta1.Job;
    import com.google.cloud.talent.v4beta1.JobQuery;
    import com.google.cloud.talent.v4beta1.JobServiceClient;
    import com.google.cloud.talent.v4beta1.RequestMetadata;
    import com.google.cloud.talent.v4beta1.SearchJobsRequest;
    import com.google.cloud.talent.v4beta1.SearchJobsResponse;
    import com.google.cloud.talent.v4beta1.TenantName;
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import com.google.type.[LatLng](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.LatLng.html);
    import java.io.IOException;
    
    public class CommuteSearchJobs {
    
      public static void searchJobs() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String tenantId = "your-tenant-id";
        searchJobs(projectId, tenantId);
      }
    
      // Search Jobs with histogram queries.
      public static void searchJobs(String projectId, String tenantId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
          TenantName parent = TenantName.of(projectId, tenantId);
          String domain = "www.example.com";
          String sessionId = "Hashed session identifier";
          String userId = "Hashed user identifier";
          RequestMetadata requestMetadata =
              RequestMetadata.newBuilder()
                  .setDomain(domain)
                  .setSessionId(sessionId)
                  .setUserId(userId)
                  .build();
    
          CommuteMethod commuteMethod = CommuteMethod.DRIVING;
          long seconds = 3600L;
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) travelDuration = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(seconds).build();
    
          double latitude = 37.422408;
          double longitude = -122.084068;
          [LatLng](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.LatLng.html) startCoordinates =
              [LatLng](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.LatLng.html).newBuilder().[setLatitude](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.LatLng.Builder.html#com_google_type_LatLng_Builder_setLatitude_double_)(latitude).[setLongitude](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.LatLng.Builder.html#com_google_type_LatLng_Builder_setLongitude_double_)(longitude).build();
    
          CommuteFilter commuteFilter =
              CommuteFilter.newBuilder()
                  .setCommuteMethod(commuteMethod)
                  .setTravelDuration(travelDuration)
                  .setStartCoordinates(startCoordinates)
                  .build();
    
          JobQuery jobQuery = JobQuery.newBuilder().setCommuteFilter(commuteFilter).build();
          SearchJobsRequest request =
              SearchJobsRequest.newBuilder()
                  .setParent(parent.toString())
                  .setRequestMetadata(requestMetadata)
                  .setJobQuery(jobQuery)
                  .build();
    
          for (SearchJobsResponse.MatchingJob responseItem :
              jobServiceClient.searchJobs(request).iterateAll()) {
            System.out.format("Job summary: %s%n", responseItem.getJobSummary());
            System.out.format("Job title snippet: %s%n", responseItem.getJobTitleSnippet());
            Job job = responseItem.getJob();
            System.out.format("Job name: %s%n", job.getName());
            System.out.format("Job title: %s%n", job.getTitle());
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const talent = require('[@google-cloud/talent](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)').v4;
    
    /** Search Jobs using commute distance */
    function sampleSearchJobs(projectId, tenantId) {
      const client = new talent.[JobServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)();
      // Iterate over all elements.
      // const projectId = 'Your Google Cloud Project ID';
      // const tenantId = 'Your Tenant ID (using tenancy is optional)';
      const formattedParent = client.tenantPath(projectId, tenantId);
      const domain = 'www.example.com';
      const sessionId = 'Hashed session identifier';
      const userId = 'Hashed user identifier';
      const requestMetadata = {
        domain: domain,
        sessionId: sessionId,
        userId: userId,
      };
      const commuteMethod = 'TRANSIT';
      const seconds = 1800;
      const travelDuration = {
        seconds: seconds,
      };
      const latitude = 37.422408;
      const longitude = 122.084068;
      const startCoordinates = {
        latitude: latitude,
        longitude: longitude,
      };
      const commuteFilter = {
        commuteMethod: commuteMethod,
        travelDuration: travelDuration,
        startCoordinates: startCoordinates,
      };
      const jobQuery = {
        commuteFilter: commuteFilter,
      };
      const request = {
        parent: formattedParent,
        requestMetadata: requestMetadata,
        jobQuery: jobQuery,
      };
    
      client
        .searchJobs(request)
        .then(responses => {
          const resources = responses[0];
          for (const resource of resources) {
            console.log(`Job summary: ${resource.jobSummary}`);
            console.log(`Job title snippet: ${resource.jobTitleSnippet}`);
            const job = resource.job;
            console.log(`Job name: ${job.name}`);
            console.log(`Job title: ${job.title}`);
          }
        })
        .catch(err => {
          console.error(err);
        });
    }
    

### Python

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import talent
    
    
    def search_jobs(project_id, tenant_id):
        """Search Jobs using commute distance"""
    
        client = talent.[JobServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient.html)()
    
        # project_id = 'Your Google Cloud Project ID'
        # tenant_id = 'Your Tenant ID (using tenancy is optional)'
    
        if isinstance(project_id, bytes):
            project_id = project_id.decode("utf-8")
        if isinstance(tenant_id, bytes):
            tenant_id = tenant_id.decode("utf-8")
        parent = f"projects/{project_id}/tenants/{tenant_id}"
        domain = "www.example.com"
        session_id = "Hashed session identifier"
        user_id = "Hashed user identifier"
        request_metadata = talent.[RequestMetadata](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.RequestMetadata.html)(
            domain=domain, session_id=session_id, user_id=user_id
        )
        commute_method = talent.[CommuteMethod](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CommuteMethod.html).TRANSIT
        seconds = 1800
        travel_duration = {"seconds": seconds}
        latitude = 37.422408
        longitude = -122.084068
        start_coordinates = {"latitude": latitude, "longitude": longitude}
        commute_filter = talent.[CommuteFilter](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CommuteFilter.html)(
            commute_method=commute_method,
            travel_duration=travel_duration,
            start_coordinates=start_coordinates,
        )
        job_query = talent.[JobQuery](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.JobQuery.html)(commute_filter=commute_filter)
    
        # Iterate over all results
        results = []
        request = talent.[SearchJobsRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsRequest.html)(
            parent=parent,
            request_metadata=request_metadata,
            job_query=job_query,
        )
        for response_item in client.[search_jobs](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient.html#google_cloud_talent_v4_services_job_service_JobServiceClient_search_jobs)(request=request).matching_jobs:
            print(f"Job summary: {response_item.job_summary}")
            print(f"Job title snippet: {response_item.job_title_snippet}")
            job = response_item.job
            results.append(job.name)
            print(f"Job name: {job.name}")
            print(f"Job title: {job.title}")
        return results
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
