---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.SpacesServiceGrpc.AsyncService
title: Interface SpacesServiceGrpc.AsyncService (0.66.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:51.605650+00:00
---

# Interface SpacesServiceGrpc.AsyncService (0.66.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.SpacesServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SpacesServiceGrpc.AsyncService (0.66.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.66.0 (latest)  0.62.0  0.61.0  0.60.0  0.58.0  0.55.0  0.54.0  0.52.0  0.50.0  0.49.0  0.47.0  0.45.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.31.0  0.30.0  0.29.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface SpacesServiceGrpc.AsyncService

REST API for services dealing with spaces.

## Methods 

### batchUpdateMembers(BatchUpdateMembersRequest request, StreamObserver<BatchUpdateMembersResponse> responseObserver)
    
    
    public default void batchUpdateMembers(BatchUpdateMembersRequest request, StreamObserver<BatchUpdateMembersResponse> responseObserver)

Updates members of one space within a batch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateMembersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.BatchUpdateMembersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BatchUpdateMembersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.BatchUpdateMembersResponse)>`  
  
  
### connectActiveConference(ConnectActiveConferenceRequest request, StreamObserver<ConnectActiveConferenceResponse> responseObserver)
    
    
    public default void connectActiveConference(ConnectActiveConferenceRequest request, StreamObserver<ConnectActiveConferenceResponse> responseObserver)

[Developer Preview](https://developers.google.com/workspace/preview): Broker a WebRTC connection to the active conference of a space. On success, clients must use the resulting SDP (Session Description Protocol) answer to establish a WebRTC connection. Once connected, additional functionality is available across WebRTC data channels. See [Meet Media API overview](https://developers.google.com/workspace/meet/media-api/guides/overview) for more details about this connection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ConnectActiveConferenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ConnectActiveConferenceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ConnectActiveConferenceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ConnectActiveConferenceResponse)>`  
  
  
### createMember(CreateMemberRequest request, StreamObserver<Member> responseObserver)
    
    
    public default void createMember(CreateMemberRequest request, StreamObserver<Member> responseObserver)

Creates a member. This API supports the `fields` parameter in [SystemParameterContext](https://cloud.google.com/apis/docs/system-parameters). When the `fields` parameter is omitted, this API response will default to "name,email,role,user".

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMemberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.CreateMemberRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Member](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.Member)>`  
  
  
### createSpace(CreateSpaceRequest request, StreamObserver<Space> responseObserver)
    
    
    public default void createSpace(CreateSpaceRequest request, StreamObserver<Space> responseObserver)

Creates a space.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.CreateSpaceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.Space)>`  
  
  
### deleteMember(DeleteMemberRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteMember(DeleteMemberRequest request, StreamObserver<Empty> responseObserver)

Deletes the member who was previously assigned roles in the space.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteMemberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.DeleteMemberRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### endActiveConference(EndActiveConferenceRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void endActiveConference(EndActiveConferenceRequest request, StreamObserver<Empty> responseObserver)

Ends an active conference (if there's one). For an example, see [End active conference](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#end-active-conference).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EndActiveConferenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.EndActiveConferenceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### getMember(GetMemberRequest request, StreamObserver<Member> responseObserver)
    
    
    public default void getMember(GetMemberRequest request, StreamObserver<Member> responseObserver)

Gets a member. This API supports the `fields` parameter in [SystemParameterContext](https://cloud.google.com/apis/docs/system-parameters). When the `fields` parameter is omitted, this API response will default to "name,email,role,user".

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMemberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.GetMemberRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Member](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.Member)>`  
  
  
### getSpace(GetSpaceRequest request, StreamObserver<Space> responseObserver)
    
    
    public default void getSpace(GetSpaceRequest request, StreamObserver<Space> responseObserver)

Gets details about a meeting space. For an example, see [Get a meeting space](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#get-meeting-space).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.GetSpaceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.Space)>`  
  
  
### listMembers(ListMembersRequest request, StreamObserver<ListMembersResponse> responseObserver)
    
    
    public default void listMembers(ListMembersRequest request, StreamObserver<ListMembersResponse> responseObserver)

Lists members. This API supports the `fields` parameter in [SystemParameterContext](https://cloud.google.com/apis/docs/system-parameters). When the `fields` parameter is omitted this API response will default to "name,email,role,user".

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMembersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ListMembersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListMembersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ListMembersResponse)>`  
  
  
### updateMember(UpdateMemberRequest request, StreamObserver<Member> responseObserver)
    
    
    public default void updateMember(UpdateMemberRequest request, StreamObserver<Member> responseObserver)

Updates a member.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMemberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.UpdateMemberRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Member](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.Member)>`  
  
  
### updateSpace(UpdateSpaceRequest request, StreamObserver<Space> responseObserver)
    
    
    public default void updateSpace(UpdateSpaceRequest request, StreamObserver<Space> responseObserver)

Updates details about a meeting space. For an example, see [Update a meeting space](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#update-meeting-space).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.UpdateSpaceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.Space)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
