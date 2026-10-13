---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.DashboardsServiceGrpc.AsyncService
title: Interface DashboardsServiceGrpc.AsyncService (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:04.357822+00:00
---

# Interface DashboardsServiceGrpc.AsyncService (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.DashboardsServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DashboardsServiceGrpc.AsyncService (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.0  2.3.0  2.2.6 
    
    
    public static interface DashboardsServiceGrpc.AsyncService

Manages Stackdriver dashboards. A dashboard is an arrangement of data display widgets in a specific layout.

## Methods 

### createDashboard(CreateDashboardRequest request, StreamObserver<Dashboard> responseObserver)
    
    
    public default void createDashboard(CreateDashboardRequest request, StreamObserver<Dashboard> responseObserver)

Creates a new custom dashboard. For examples on how you can use this API to create dashboards, see [Managing dashboards by API](https://cloud.google.com/monitoring/dashboards/api-dashboard). This method requires the `monitoring.dashboards.create` permission on the specified project. For more information about permissions, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDashboardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.CreateDashboardRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Dashboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.Dashboard)>`  
  
  
### deleteDashboard(DeleteDashboardRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteDashboard(DeleteDashboardRequest request, StreamObserver<Empty> responseObserver)

Deletes an existing custom dashboard. This method requires the `monitoring.dashboards.delete` permission on the specified dashboard. For more information, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDashboardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.DeleteDashboardRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### getDashboard(GetDashboardRequest request, StreamObserver<Dashboard> responseObserver)
    
    
    public default void getDashboard(GetDashboardRequest request, StreamObserver<Dashboard> responseObserver)

Fetches a specific dashboard. This method requires the `monitoring.dashboards.get` permission on the specified dashboard. For more information, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDashboardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.GetDashboardRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Dashboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.Dashboard)>`  
  
  
### listDashboards(ListDashboardsRequest request, StreamObserver<ListDashboardsResponse> responseObserver)
    
    
    public default void listDashboards(ListDashboardsRequest request, StreamObserver<ListDashboardsResponse> responseObserver)

Lists the existing dashboards. This method requires the `monitoring.dashboards.list` permission on the specified project. For more information, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDashboardsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.ListDashboardsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListDashboardsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.ListDashboardsResponse)>`  
  
  
### updateDashboard(UpdateDashboardRequest request, StreamObserver<Dashboard> responseObserver)
    
    
    public default void updateDashboard(UpdateDashboardRequest request, StreamObserver<Dashboard> responseObserver)

Replaces an existing custom dashboard with a new definition. This method requires the `monitoring.dashboards.update` permission on the specified dashboard. For more information, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDashboardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.UpdateDashboardRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Dashboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring-dashboard/latest/com.google.monitoring.dashboard.v1.Dashboard)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
