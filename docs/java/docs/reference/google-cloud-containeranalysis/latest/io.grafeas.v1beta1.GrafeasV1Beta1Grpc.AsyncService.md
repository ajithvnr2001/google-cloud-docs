---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.GrafeasV1Beta1Grpc.AsyncService
title: Interface GrafeasV1Beta1Grpc.AsyncService (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:57.490015+00:00
---

# Interface GrafeasV1Beta1Grpc.AsyncService (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.GrafeasV1Beta1Grpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GrafeasV1Beta1Grpc.AsyncService (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.10  2.3.1  2.2.16 
    
    
    public static interface GrafeasV1Beta1Grpc.AsyncService

[Grafeas](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/grafeas.io) API. Retrieves analysis results of Cloud components such as Docker container images. Analysis results are stored as a series of occurrences. An `Occurrence` contains information about a specific analysis instance on a resource. An occurrence refers to a `Note`. A note contains details describing the analysis and is generally stored in a separate project, called a `Provider`. Multiple occurrences can refer to the same note. For example, an SSL vulnerability could affect multiple images. In this case, there would be one note for the vulnerability and an occurrence for each image with the vulnerability referring to that note.

## Methods 

### batchCreateNotes(BatchCreateNotesRequest request, StreamObserver<BatchCreateNotesResponse> responseObserver)
    
    
    public default void batchCreateNotes(BatchCreateNotesRequest request, StreamObserver<BatchCreateNotesResponse> responseObserver)

Creates new notes in batch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateNotesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.BatchCreateNotesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BatchCreateNotesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.BatchCreateNotesResponse)>`  
  
  
### batchCreateOccurrences(BatchCreateOccurrencesRequest request, StreamObserver<BatchCreateOccurrencesResponse> responseObserver)
    
    
    public default void batchCreateOccurrences(BatchCreateOccurrencesRequest request, StreamObserver<BatchCreateOccurrencesResponse> responseObserver)

Creates new occurrences in batch.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateOccurrencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.BatchCreateOccurrencesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BatchCreateOccurrencesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.BatchCreateOccurrencesResponse)>`  
  
  
### createNote(CreateNoteRequest request, StreamObserver<Note> responseObserver)
    
    
    public default void createNote(CreateNoteRequest request, StreamObserver<Note> responseObserver)

Creates a new note.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateNoteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.CreateNoteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Note](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.Note)>`  
  
  
### createOccurrence(CreateOccurrenceRequest request, StreamObserver<Occurrence> responseObserver)
    
    
    public default void createOccurrence(CreateOccurrenceRequest request, StreamObserver<Occurrence> responseObserver)

Creates a new occurrence.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateOccurrenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.CreateOccurrenceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Occurrence](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.Occurrence)>`  
  
  
### deleteNote(DeleteNoteRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteNote(DeleteNoteRequest request, StreamObserver<Empty> responseObserver)

Deletes the specified note.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteNoteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.DeleteNoteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteOccurrence(DeleteOccurrenceRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteOccurrence(DeleteOccurrenceRequest request, StreamObserver<Empty> responseObserver)

Deletes the specified occurrence. For example, use this method to delete an occurrence when the occurrence is no longer applicable for the given resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteOccurrenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.DeleteOccurrenceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### getNote(GetNoteRequest request, StreamObserver<Note> responseObserver)
    
    
    public default void getNote(GetNoteRequest request, StreamObserver<Note> responseObserver)

Gets the specified note.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetNoteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.GetNoteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Note](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.Note)>`  
  
  
### getOccurrence(GetOccurrenceRequest request, StreamObserver<Occurrence> responseObserver)
    
    
    public default void getOccurrence(GetOccurrenceRequest request, StreamObserver<Occurrence> responseObserver)

Gets the specified occurrence.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOccurrenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.GetOccurrenceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Occurrence](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.Occurrence)>`  
  
  
### getOccurrenceNote(GetOccurrenceNoteRequest request, StreamObserver<Note> responseObserver)
    
    
    public default void getOccurrenceNote(GetOccurrenceNoteRequest request, StreamObserver<Note> responseObserver)

Gets the note attached to the specified occurrence. Consumer projects can use this method to get a note that belongs to a provider project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetOccurrenceNoteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.GetOccurrenceNoteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Note](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.Note)>`  
  
  
### getVulnerabilityOccurrencesSummary(GetVulnerabilityOccurrencesSummaryRequest request, StreamObserver<VulnerabilityOccurrencesSummary> responseObserver)
    
    
    public default void getVulnerabilityOccurrencesSummary(GetVulnerabilityOccurrencesSummaryRequest request, StreamObserver<VulnerabilityOccurrencesSummary> responseObserver)

Gets a summary of the number and severity of occurrences.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetVulnerabilityOccurrencesSummaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.GetVulnerabilityOccurrencesSummaryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[VulnerabilityOccurrencesSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.VulnerabilityOccurrencesSummary)>`  
  
  
### listNoteOccurrences(ListNoteOccurrencesRequest request, StreamObserver<ListNoteOccurrencesResponse> responseObserver)
    
    
    public default void listNoteOccurrences(ListNoteOccurrencesRequest request, StreamObserver<ListNoteOccurrencesResponse> responseObserver)

Lists occurrences referencing the specified note. Provider projects can use this method to get all occurrences across consumer projects referencing the specified note.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListNoteOccurrencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.ListNoteOccurrencesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListNoteOccurrencesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.ListNoteOccurrencesResponse)>`  
  
  
### listNotes(ListNotesRequest request, StreamObserver<ListNotesResponse> responseObserver)
    
    
    public default void listNotes(ListNotesRequest request, StreamObserver<ListNotesResponse> responseObserver)

Lists notes for the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListNotesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.ListNotesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListNotesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.ListNotesResponse)>`  
  
  
### listOccurrences(ListOccurrencesRequest request, StreamObserver<ListOccurrencesResponse> responseObserver)
    
    
    public default void listOccurrences(ListOccurrencesRequest request, StreamObserver<ListOccurrencesResponse> responseObserver)

Lists occurrences for the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListOccurrencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.ListOccurrencesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListOccurrencesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.ListOccurrencesResponse)>`  
  
  
### updateNote(UpdateNoteRequest request, StreamObserver<Note> responseObserver)
    
    
    public default void updateNote(UpdateNoteRequest request, StreamObserver<Note> responseObserver)

Updates the specified note.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateNoteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.UpdateNoteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Note](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.Note)>`  
  
  
### updateOccurrence(UpdateOccurrenceRequest request, StreamObserver<Occurrence> responseObserver)
    
    
    public default void updateOccurrence(UpdateOccurrenceRequest request, StreamObserver<Occurrence> responseObserver)

Updates the specified occurrence.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateOccurrenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.UpdateOccurrenceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Occurrence](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/io.grafeas.v1beta1.Occurrence)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
