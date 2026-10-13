---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ConferenceRecordsServiceGrpc.ConferenceRecordsServiceFutureStub
title: Class ConferenceRecordsServiceGrpc.ConferenceRecordsServiceFutureStub (0.66.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:59.607890+00:00
---

# Class ConferenceRecordsServiceGrpc.ConferenceRecordsServiceFutureStub (0.66.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ConferenceRecordsServiceGrpc.ConferenceRecordsServiceFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConferenceRecordsServiceGrpc.ConferenceRecordsServiceFutureStub (0.66.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.66.0 (latest)  0.62.0  0.61.0  0.60.0  0.58.0  0.55.0  0.54.0  0.52.0  0.50.0  0.49.0  0.47.0  0.45.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.31.0  0.30.0  0.29.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class ConferenceRecordsServiceGrpc.ConferenceRecordsServiceFutureStub extends AbstractFutureStub<ConferenceRecordsServiceGrpc.ConferenceRecordsServiceFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service ConferenceRecordsService.

REST API for services dealing with conference records.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > ConferenceRecordsServiceGrpc.ConferenceRecordsServiceFutureStub

## Inherited Members

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### build(Channel channel, CallOptions callOptions)
    
    
    protected ConferenceRecordsServiceGrpc.ConferenceRecordsServiceFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConferenceRecordsServiceGrpc.ConferenceRecordsServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ConferenceRecordsServiceGrpc.ConferenceRecordsServiceFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### getConferenceRecord(GetConferenceRecordRequest request)
    
    
    public ListenableFuture<ConferenceRecord> getConferenceRecord(GetConferenceRecordRequest request)

Gets a conference record by conference ID.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConferenceRecordRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.GetConferenceRecordRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ConferenceRecord](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ConferenceRecord)>` |   
  
### getParticipant(GetParticipantRequest request)
    
    
    public ListenableFuture<Participant> getParticipant(GetParticipantRequest request)

Gets a participant by participant ID.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetParticipantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.GetParticipantRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Participant](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.Participant)>` |   
  
### getParticipantSession(GetParticipantSessionRequest request)
    
    
    public ListenableFuture<ParticipantSession> getParticipantSession(GetParticipantSessionRequest request)

Gets a participant session by participant session ID.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetParticipantSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.GetParticipantSessionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ParticipantSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ParticipantSession)>` |   
  
### getRecording(GetRecordingRequest request)
    
    
    public ListenableFuture<Recording> getRecording(GetRecordingRequest request)

Gets a recording by recording ID.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRecordingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.GetRecordingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Recording](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.Recording)>` |   
  
### getSmartNote(GetSmartNoteRequest request)
    
    
    public ListenableFuture<SmartNote> getSmartNote(GetSmartNoteRequest request)

Gets smart notes by smart note ID.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSmartNoteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.GetSmartNoteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[SmartNote](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.SmartNote)>` |   
  
### getTranscript(GetTranscriptRequest request)
    
    
    public ListenableFuture<Transcript> getTranscript(GetTranscriptRequest request)

Gets a transcript by transcript ID.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTranscriptRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.GetTranscriptRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Transcript](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.Transcript)>` |   
  
### getTranscriptEntry(GetTranscriptEntryRequest request)
    
    
    public ListenableFuture<TranscriptEntry> getTranscriptEntry(GetTranscriptEntryRequest request)

Gets a `TranscriptEntry` resource by entry ID. Note: The transcript entries returned by the Google Meet API might not match the transcription found in the Google Docs transcript file. This can occur when 1) we have interleaved speakers within milliseconds, or 2) the Google Docs transcript file is modified after generation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTranscriptEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.GetTranscriptEntryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[TranscriptEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.TranscriptEntry)>` |   
  
### listConferenceRecords(ListConferenceRecordsRequest request)
    
    
    public ListenableFuture<ListConferenceRecordsResponse> listConferenceRecords(ListConferenceRecordsRequest request)

Lists the conference records. By default, ordered by start time and in descending order.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListConferenceRecordsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ListConferenceRecordsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListConferenceRecordsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ListConferenceRecordsResponse)>` |   
  
### listParticipantSessions(ListParticipantSessionsRequest request)
    
    
    public ListenableFuture<ListParticipantSessionsResponse> listParticipantSessions(ListParticipantSessionsRequest request)

Lists the participant sessions of a participant in a conference record. By default, ordered by join time and in descending order. This API supports `fields` as standard parameters like every other API. However, when the `fields` request parameter is omitted this API defaults to `'participantsessions/*, next_page_token'`.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListParticipantSessionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ListParticipantSessionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListParticipantSessionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ListParticipantSessionsResponse)>` |   
  
### listParticipants(ListParticipantsRequest request)
    
    
    public ListenableFuture<ListParticipantsResponse> listParticipants(ListParticipantsRequest request)

Lists the participants in a conference record. By default, ordered by join time and in descending order. This API supports `fields` as standard parameters like every other API. However, when the `fields` request parameter is omitted, this API defaults to `'participants/*, next_page_token'`.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListParticipantsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ListParticipantsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListParticipantsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ListParticipantsResponse)>` |   
  
### listRecordings(ListRecordingsRequest request)
    
    
    public ListenableFuture<ListRecordingsResponse> listRecordings(ListRecordingsRequest request)

Lists the recording resources from the conference record. By default, ordered by start time and in ascending order.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRecordingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ListRecordingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListRecordingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ListRecordingsResponse)>` |   
  
### listSmartNotes(ListSmartNotesRequest request)
    
    
    public ListenableFuture<ListSmartNotesResponse> listSmartNotes(ListSmartNotesRequest request)

Lists the set of smart notes from the conference record. By default, ordered by start time and in ascending order.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSmartNotesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ListSmartNotesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListSmartNotesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ListSmartNotesResponse)>` |   
  
### listTranscriptEntries(ListTranscriptEntriesRequest request)
    
    
    public ListenableFuture<ListTranscriptEntriesResponse> listTranscriptEntries(ListTranscriptEntriesRequest request)

Lists the structured transcript entries per transcript. By default, ordered by start time and in ascending order. Note: The transcript entries returned by the Google Meet API might not match the transcription found in the Google Docs transcript file. This can occur when 1) we have interleaved speakers within milliseconds, or 2) the Google Docs transcript file is modified after generation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTranscriptEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ListTranscriptEntriesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListTranscriptEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ListTranscriptEntriesResponse)>` |   
  
### listTranscripts(ListTranscriptsRequest request)
    
    
    public ListenableFuture<ListTranscriptsResponse> listTranscripts(ListTranscriptsRequest request)

Lists the set of transcripts from the conference record. By default, ordered by start time and in ascending order.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTranscriptsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ListTranscriptsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListTranscriptsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2beta.ListTranscriptsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
