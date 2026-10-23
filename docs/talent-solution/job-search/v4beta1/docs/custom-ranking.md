---
url: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/custom-ranking/
title: Custom ranking (v4beta1) \u00a0|\u00a0 Cloud Talent Solution - Job Search v4beta1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:40.322478+00:00
---

# Custom ranking (v4beta1)  |  Cloud Talent Solution - Job Search v4beta1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/custom-ranking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v4beta1 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs)



Send feedback 

#  Custom ranking (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

The custom ranking feature allows you to introduce your own business logic to control the ranking of jobs returned by Cloud Talent Solution. A job seeker searching on a site can set their search query and other filters as always, and you can add a ranking expression to the search request. Cloud Talent Solution determines the relevant jobs to the query defined by the job seeker, and ranks the results based on the custom ranking expression. This ranked list is then returned to you so that you can display it to the job seeker. A video tutorial on implementing custom ranking is also [available](https://docs.cloud.google.com/talent-solutuon/job-search/v4beta1/docs/video).

## Benefits

Custom ranking allows you to control on how the results are listed. Using a custom ranking lets you define weights you can assign to custom attributes. You can use a combination of weights and custom attributes to build a custom ranking expression to determine the order the returned listings.

Custom ranking is built on the existing search service. It leverages the values provided in any customer-defined combination of the custom attributes.

### Example use case

The end user searches for "Software Engineer". Your business wants to showcase higher return listings for "Software Engineer". Using Custom Ranking allows you to place a value on these listings and show them to the end user in the order determined by the custom ranking expression.

For example, you have two nearly identical job listings with job-A having a higher cost per click (CPC) value than job-B. You can use custom ranking to increase the visibility of job-A by setting the adjusting the ranking of the CPC custom attribute with weights.

## How to use

Custom ranking supports the following mathematical operators: `+`, `-`, `*`, `/`, `(`, `)`

You can use the field names of custom attributes and these mathematical operators to define a custom ranking expression.

For example, consider that you have two custom attributes: CPC and freshness, where freshness is the number of days since the job was posted. You want to rank jobs by CPC and freshness, where CPC counts for 75% of the ranking and freshness counts for 25%. You can create a custom ranking expression as follows:
    
    
    (0.75*CPC) + (0.25 *Freshness)
    

## Code Sample

The following example creates a custom ranking expression using two custom attributes, `cpc_value` and `freshness_value`. It sets the custom ranking expression to `(cpc_value / 2) - freshness_value`.

### Go

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	talent "cloud.google.com/go/talent/apiv4beta1"
    	"cloud.google.com/go/talent/apiv4beta1/talentpb"
    )
    
    // customRankingSearch searches for jobs based on custom ranking.
    func customRankingSearch(w io.Writer, projectID, companyID string) error {
    	ctx := context.Background()
    
    	// Initialize a jobService client.
    	c, err := talent.[NewJobClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1.html#cloud_google_com_go_talent_apiv4beta1_JobClient_NewJobClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("taleng.NewJobClient: %w", err)
    	}
    	defer c.Close()
    
    	// Construct a searchJobs request.
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
    		JobQuery: &talentpb.JobQuery{
    			Companies: []string{fmt.Sprintf("projects/%s/companies/%s", projectID, companyID)},
    		},
    		// More info on customRankingInfo.
    		// https://godoc.org/google.golang.org/genproto/googleapis/cloud/talent/v4beta1#SearchJobsRequest_CustomRankingInfo
    		CustomRankingInfo: &talentpb.SearchJobsRequest_CustomRankingInfo{
    			ImportanceLevel:   talentpb.[SearchJobsRequest_CustomRankingInfo_EXTREME](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/talent/latest/apiv4beta1/talentpb.html#cloud_google_com_go_talent_apiv4beta1_talentpb_SearchJobsRequest_CustomRankingInfo_IMPORTANCE_LEVEL_UNSPECIFIED_SearchJobsRequest_CustomRankingInfo_NONE_SearchJobsRequest_CustomRankingInfo_LOW_SearchJobsRequest_CustomRankingInfo_MILD_SearchJobsRequest_CustomRankingInfo_MEDIUM_SearchJobsRequest_CustomRankingInfo_HIGH_SearchJobsRequest_CustomRankingInfo_EXTREME),
    			RankingExpression: "(someFieldLong + 25) * 0.25",
    		},
    		OrderBy: "custom_ranking desc",
    	}
    
    	resp, err := c.SearchJobs(ctx, req)
    	if err != nil {
    		return fmt.Errorf("SearchJobs: %w", err)
    	}
    
    	for _, job := range resp.GetMatchingJobs() {
    		fmt.Fprintf(w, "Job: %q\n", job.GetJob().GetName())
    	}
    
    	return nil
    }
    

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    import com.google.cloud.talent.v4beta1.Job;
    import com.google.cloud.talent.v4beta1.JobServiceClient;
    import com.google.cloud.talent.v4beta1.RequestMetadata;
    import com.google.cloud.talent.v4beta1.SearchJobsRequest;
    import com.google.cloud.talent.v4beta1.SearchJobsResponse;
    import com.google.cloud.talent.v4beta1.TenantName;
    import java.io.IOException;
    
    public class CustomRankingSearchJobs {
    
      public static void searchCustomRankingJobs() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String tenantId = "your-tenant-id";
        searchCustomRankingJobs(projectId, tenantId);
      }
    
      // Search Jobs using custom rankings.
      public static void searchCustomRankingJobs(String projectId, String tenantId) throws IOException {
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
          SearchJobsRequest.CustomRankingInfo.ImportanceLevel importanceLevel =
              SearchJobsRequest.CustomRankingInfo.ImportanceLevel.EXTREME;
          String rankingExpression = "(someFieldLong + 25) * 0.25";
          SearchJobsRequest.CustomRankingInfo customRankingInfo =
              SearchJobsRequest.CustomRankingInfo.newBuilder()
                  .setImportanceLevel(importanceLevel)
                  .setRankingExpression(rankingExpression)
                  .build();
          String orderBy = "custom_ranking desc";
          SearchJobsRequest request =
              SearchJobsRequest.newBuilder()
                  .setParent(parent.toString())
                  .setRequestMetadata(requestMetadata)
                  .setCustomRankingInfo(customRankingInfo)
                  .setOrderBy(orderBy)
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

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    
    from google.cloud import talent
    
    
    def search_jobs(project_id, tenant_id):
        """Search Jobs using custom rankings"""
    
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
        importance_level = (
            talent.[SearchJobsRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsRequest.html).[CustomRankingInfo](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsRequest.CustomRankingInfo.html).[ImportanceLevel](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsRequest.CustomRankingInfo.ImportanceLevel.html).EXTREME
        )
        ranking_expression = "(someFieldLong + 25) * 0.25"
        custom_ranking_info = {
            "importance_level": importance_level,
            "ranking_expression": ranking_expression,
        }
        order_by = "custom_ranking desc"
    
        # Iterate over all results
        results = []
        request = talent.[SearchJobsRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.SearchJobsRequest.html)(
            parent=parent,
            request_metadata=request_metadata,
            custom_ranking_info=custom_ranking_info,
            order_by=order_by,
        )
        for response_item in client.[search_jobs](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient.html#google_cloud_talent_v4_services_job_service_JobServiceClient_search_jobs)(request=request).matching_jobs:
            print(f"Job summary: {response_item.job_summary}")
            print(f"Job title snippet: {response_item.job_title_snippet}")
            job = response_item.job
            results.append(job.name)
            print(f"Job name: {job.name}")
            print(f"Job title: {job.title}")
        return results
    
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
