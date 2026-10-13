---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.GrafeasV1Beta1Grpc.GrafeasV1Beta1BlockingStub
title: Class GrafeasV1Beta1Grpc.GrafeasV1Beta1BlockingStub (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:47:54.999311+00:00
---

# Class GrafeasV1Beta1Grpc.GrafeasV1Beta1BlockingStub (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.GrafeasV1Beta1Grpc.GrafeasV1Beta1BlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GrafeasV1Beta1Grpc.GrafeasV1Beta1BlockingStub (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.10  2.3.1  2.2.16 
    
    
    public static final class GrafeasV1Beta1Grpc.GrafeasV1Beta1BlockingStub extends AbstractBlockingStub<GrafeasV1Beta1Grpc.GrafeasV1Beta1BlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service GrafeasV1Beta1.

[Grafeas](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/grafeas.io) API. Retrieves analysis results of Cloud components such as Docker container images. Analysis results are stored as a series of occurrences. An `Occurrence` contains information about a specific analysis instance on a resource. An occurrence refers to a `Note`. A note contains details describing the analysis and is generally stored in a separate project, called a `Provider`. Multiple occurrences can refer to the same note. For example, an SSL vulnerability could affect multiple images. In this case, there would be one note for the vulnerability and an occurrence for each image with the vulnerability referring to that note.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > GrafeasV1Beta1Grpc.GrafeasV1Beta1BlockingStub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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

### batchCreateNotes(BatchCreateNotesRequest request)
    
    
    public BatchCreateNotesResponse batchCreateNotes(BatchCreateNotesRequest request)

Creates new notes in batch.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateNotesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.BatchCreateNotesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateNotesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.BatchCreateNotesResponse)` |   
  
### batchCreateOccurrences(BatchCreateOccurrencesRequest request)
    
    
    public BatchCreateOccurrencesResponse batchCreateOccurrences(BatchCreateOccurrencesRequest request)

Creates new occurrences in batch.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateOccurrencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.BatchCreateOccurrencesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateOccurrencesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.BatchCreateOccurrencesResponse)` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected GrafeasV1Beta1Grpc.GrafeasV1Beta1BlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[GrafeasV1Beta1Grpc.GrafeasV1Beta1BlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.GrafeasV1Beta1Grpc.GrafeasV1Beta1BlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createNote(CreateNoteRequest request)
    
    
    public Note createNote(CreateNoteRequest request)

Creates a new note.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateNoteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.CreateNoteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Note](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.Note)` |   
  
### createOccurrence(CreateOccurrenceRequest request)
    
    
    public Occurrence createOccurrence(CreateOccurrenceRequest request)

Creates a new occurrence.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateOccurrenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.CreateOccurrenceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Occurrence](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.Occurrence)` |   
  
### deleteNote(DeleteNoteRequest request)
    
    
    public Empty deleteNote(DeleteNoteRequest request)

Deletes the specified note.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNoteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.DeleteNoteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### deleteOccurrence(DeleteOccurrenceRequest request)
    
    
    public Empty deleteOccurrence(DeleteOccurrenceRequest request)

Deletes the specified occurrence. For example, use this method to delete an occurrence when the occurrence is no longer applicable for the given resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteOccurrenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.DeleteOccurrenceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### getNote(GetNoteRequest request)
    
    
    public Note getNote(GetNoteRequest request)

Gets the specified note.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNoteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.GetNoteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Note](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.Note)` |   
  
### getOccurrence(GetOccurrenceRequest request)
    
    
    public Occurrence getOccurrence(GetOccurrenceRequest request)

Gets the specified occurrence.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOccurrenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.GetOccurrenceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Occurrence](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.Occurrence)` |   
  
### getOccurrenceNote(GetOccurrenceNoteRequest request)
    
    
    public Note getOccurrenceNote(GetOccurrenceNoteRequest request)

Gets the note attached to the specified occurrence. Consumer projects can use this method to get a note that belongs to a provider project.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOccurrenceNoteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.GetOccurrenceNoteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Note](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.Note)` |   
  
### getVulnerabilityOccurrencesSummary(GetVulnerabilityOccurrencesSummaryRequest request)
    
    
    public VulnerabilityOccurrencesSummary getVulnerabilityOccurrencesSummary(GetVulnerabilityOccurrencesSummaryRequest request)

Gets a summary of the number and severity of occurrences.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetVulnerabilityOccurrencesSummaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.GetVulnerabilityOccurrencesSummaryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VulnerabilityOccurrencesSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.VulnerabilityOccurrencesSummary)` |   
  
### listNoteOccurrences(ListNoteOccurrencesRequest request)
    
    
    public ListNoteOccurrencesResponse listNoteOccurrences(ListNoteOccurrencesRequest request)

Lists occurrences referencing the specified note. Provider projects can use this method to get all occurrences across consumer projects referencing the specified note.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNoteOccurrencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.ListNoteOccurrencesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListNoteOccurrencesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.ListNoteOccurrencesResponse)` |   
  
### listNotes(ListNotesRequest request)
    
    
    public ListNotesResponse listNotes(ListNotesRequest request)

Lists notes for the specified project.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNotesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.ListNotesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListNotesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.ListNotesResponse)` |   
  
### listOccurrences(ListOccurrencesRequest request)
    
    
    public ListOccurrencesResponse listOccurrences(ListOccurrencesRequest request)

Lists occurrences for the specified project.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOccurrencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.ListOccurrencesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListOccurrencesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.ListOccurrencesResponse)` |   
  
### updateNote(UpdateNoteRequest request)
    
    
    public Note updateNote(UpdateNoteRequest request)

Updates the specified note.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateNoteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.UpdateNoteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Note](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.Note)` |   
  
### updateOccurrence(UpdateOccurrenceRequest request)
    
    
    public Occurrence updateOccurrence(UpdateOccurrenceRequest request)

Updates the specified occurrence.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateOccurrenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.UpdateOccurrenceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Occurrence](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.Occurrence)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
