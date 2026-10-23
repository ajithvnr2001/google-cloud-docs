---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/search-commute/
title: Commute search \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:10.725529+00:00
---

# Commute search  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/search-commute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Guides ](https://docs.cloud.google.com/talent-solution/job-search/docs/basics)



Send feedback 

#  Commute search Stay organized with collections  Save and categorize content based on your preferences. 

Search requests can include a commute time filter that restricts returned jobs to those within a specified travel time from a start point. Results include the estimated commute time in seconds for matched jobs.

## Specific commute time search

To return jobs within a specific commute time, send a [`jobs.search`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs/search) request and include a `CommuteFilter` object in the `JobQuery.commuteFilter` field. Cloud Talent Solution uses the job's [`address`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/projects.tenants.jobs#Job.FIELDS.addresses) to calculate the commute time to that job. When a detailed address is not provided Cloud Talent Solution attempts to infer the actual street address of the job.

### Java

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/overview). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.talent.v4.[CommuteFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CommuteFilter.html);
    import com.google.cloud.talent.v4.[CommuteMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CommuteMethod.html);
    import com.google.cloud.talent.v4.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html);
    import com.google.cloud.talent.v4.[JobQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobQuery.html);
    import com.google.cloud.talent.v4.[JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobServiceClient.html);
    import com.google.cloud.talent.v4.[RequestMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.RequestMetadata.html);
    import com.google.cloud.talent.v4.[SearchJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsRequest.html);
    import com.google.cloud.talent.v4.[SearchJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsResponse.html);
    import com.google.cloud.talent.v4.[TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html);
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
        try ([JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobServiceClient.html) jobServiceClient = [JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobServiceClient.html).create()) {
          [TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html) parent = [TenantName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html).of(projectId, tenantId);
          String domain = "www.example.com";
          String sessionId = "Hashed session identifier";
          String userId = "Hashed user identifier";
          [RequestMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.RequestMetadata.html) requestMetadata =
              [RequestMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.RequestMetadata.html).newBuilder()
                  .[setDomain](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.RequestMetadata.Builder.html#com_google_cloud_talent_v4_RequestMetadata_Builder_setDomain_java_lang_String_)(domain)
                  .[setSessionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.RequestMetadata.Builder.html#com_google_cloud_talent_v4_RequestMetadata_Builder_setSessionId_java_lang_String_)(sessionId)
                  .[setUserId](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.RequestMetadata.Builder.html#com_google_cloud_talent_v4_RequestMetadata_Builder_setUserId_java_lang_String_)(userId)
                  .build();
    
          [CommuteMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CommuteMethod.html) commuteMethod = [CommuteMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CommuteMethod.html).DRIVING;
          long seconds = 3600L;
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) travelDuration = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(seconds).build();
    
          double latitude = 37.422408;
          double longitude = -122.084068;
          [LatLng](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.LatLng.html) startCoordinates =
              [LatLng](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.LatLng.html).newBuilder().[setLatitude](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.LatLng.Builder.html#com_google_type_LatLng_Builder_setLatitude_double_)(latitude).[setLongitude](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.LatLng.Builder.html#com_google_type_LatLng_Builder_setLongitude_double_)(longitude).build();
    
          [CommuteFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CommuteFilter.html) commuteFilter =
              [CommuteFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CommuteFilter.html).newBuilder()
                  .[setCommuteMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CommuteFilter.Builder.html#com_google_cloud_talent_v4_CommuteFilter_Builder_setCommuteMethod_com_google_cloud_talent_v4_CommuteMethod_)(commuteMethod)
                  .setTravelDuration(travelDuration)
                  .[setStartCoordinates](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.CommuteFilter.Builder.html#com_google_cloud_talent_v4_CommuteFilter_Builder_setStartCoordinates_com_google_type_LatLng_)(startCoordinates)
                  .build();
    
          [JobQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobQuery.html) jobQuery = [JobQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobQuery.html).newBuilder().[setCommuteFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.JobQuery.Builder.html#com_google_cloud_talent_v4_JobQuery_Builder_setCommuteFilter_com_google_cloud_talent_v4_CommuteFilter_)(commuteFilter).build();
          [SearchJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsRequest.html) request =
              [SearchJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsRequest.html).newBuilder()
                  .setParent(parent.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.TenantName.html#com_google_cloud_talent_v4_TenantName_toString__)())
                  .[setRequestMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsRequest.Builder.html#com_google_cloud_talent_v4_SearchJobsRequest_Builder_setRequestMetadata_com_google_cloud_talent_v4_RequestMetadata_)(requestMetadata)
                  .[setJobQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsRequest.Builder.html#com_google_cloud_talent_v4_SearchJobsRequest_Builder_setJobQuery_com_google_cloud_talent_v4_JobQuery_)(jobQuery)
                  .build();
    
          for ([SearchJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsResponse.html).[MatchingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.SearchJobsResponse.MatchingJob.html) responseItem :
              jobServiceClient.searchJobs(request).getMatchingJobsList()) {
            System.out.format("Job summary: %s%n", responseItem.getJobSummary());
            System.out.format("Job title snippet: %s%n", responseItem.getJobTitleSnippet());
            [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html) job = responseItem.getJob();
            System.out.format("Job name: %s%n", job.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html#com_google_cloud_talent_v4_Job_getName__)());
            System.out.format("Job title: %s%n", job.[getTitle](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4.Job.html#com_google_cloud_talent_v4_Job_getTitle__)());
          }
        }
      }
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
    
    

## Required fields

  * `commuteMethod`: The method of transportation used to calculate the commute time. Options are `DRIVING`, `TRANSIT`, `WALKING` and `CYCLING` transit modes. **Walking and cycling routes may not reflect real-world conditions such as construction or include clear walking or cycling paths. These responses include`warnings` in the returned result which you must display to your users.**

  * `travelDuration`: The maximum travel time in seconds. The maximum allowed value is `3600s` (one hour). The format is `123s`.

  * `startCoordinates`: The latitude and longitude of the location from which to calculate the commute time. This field accepts a [`LatLng`](https://docs.cloud.google.com/talent-solution/job-search/docs/reference/rest/v4/Location#LatLng) object.

  * Either `roadTraffic` or `departureTime`: Commute search results are based on historical and aggregated data rather than live traffic conditions. Users receive the same commute search results no matter what time of day they send a query.

    * `roadTraffic`: Specifies the traffic density to use when calculating commute time. The `BUSY_HOUR`/`TRAFFIC_FREE` options are the calculated average traffic conditions at morning rush hour and midnight, respectively. This field must not be present if `departureTime` is specified.

    * `departureTime`: The departure hour to use to calculate traffic impact. Accepts an integer between 0 and 23, representing the hour in the timezone of the `startLocation`. Traffic conditions are calculated from average historical traffic conditions at the specified time of day. This field must not be present if `roadTraffic` is specified.




## Optional fields

  * `allowImpreciseAddresses`: "Precise" addresses are defined as either street level addresses or GPS coordinates. If `allowImpreciseAddresses` is set to `true`, jobs with "imprecise" addresses (city, state, or country only) might also be returned. For city level and coarser level addresses, the API uses text matching to return results. If this field is set to `false` or is not specified, only jobs that include precise addresses are returned.

**Note:** If `allowImpreciseAddresses` is set to `true`, Job Search is not able to calculate accurate commute times to jobs with city level and coarser address information. Jobs with imprecise addresses return a `travelDuration` time of 2147483647 (`INT-MAX`) regardless of their distance from the job seeker.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
