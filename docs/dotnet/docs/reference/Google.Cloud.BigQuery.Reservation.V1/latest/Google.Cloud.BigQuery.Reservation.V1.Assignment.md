---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Reservation.V1/latest/Google.Cloud.BigQuery.Reservation.V1.Assignment
title: BigQuery Reservation v1 API - Class Assignment (2.14.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:26.184334+00:00
---

# BigQuery Reservation v1 API - Class Assignment (2.14.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Reservation.V1/latest/Google.Cloud.BigQuery.Reservation.V1.Assignment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  BigQuery Reservation v1 API - Class Assignment (2.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.14.0 (latest)  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0 
    
    
    public sealed class Assignment : IMessage<Assignment>, IEquatable<Assignment>, IDeepCloneable<Assignment>, IBufferMessage, IMessage

Reference documentation and code samples for the BigQuery Reservation v1 API class Assignment.

An assignment allows a project to submit jobs of a certain type using slots from the specified reservation.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Assignment

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Assignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Reservation.V1/latest/Google.Cloud.BigQuery.Reservation.V1.Assignment), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Assignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Reservation.V1/latest/Google.Cloud.BigQuery.Reservation.V1.Assignment), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Assignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Reservation.V1/latest/Google.Cloud.BigQuery.Reservation.V1.Assignment), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BigQuery.Reservation.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Reservation.V1/latest/Google.Cloud.BigQuery.Reservation.V1)

## Assembly

Google.Cloud.BigQuery.Reservation.V1.dll

## Constructors 

### Assignment()
    
    
    public Assignment()

### Assignment(Assignment)
    
    
    public Assignment(Assignment other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Assignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Reservation.V1/latest/Google.Cloud.BigQuery.Reservation.V1.Assignment)`  
  
  
## Properties 

### Assignee
    
    
    public string Assignee { get; set; }

Optional. The resource which will use the reservation. E.g. `projects/myproject`, `folders/123`, or `organizations/456`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AssignmentName
    
    
    public AssignmentName AssignmentName { get; set; }

[AssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Reservation.V1/latest/Google.Cloud.BigQuery.Reservation.V1.AssignmentName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Reservation.V1/latest/Google.Cloud.BigQuery.Reservation.V1.Assignment#Google_Cloud_BigQuery_Reservation_V1_Assignment_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Reservation.V1/latest/Google.Cloud.BigQuery.Reservation.V1.AssignmentName)` |   
  
### Condition
    
    
    public Expr Condition { get; set; }

Optional. Common Expression Language (CEL) condition that defines the matching criteria for this assignment. The condition must resolve to a boolean value. Supported variables will be added later.

**Property Value**  
---  
**Type** | **Description**  
`[Expr](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Expr.html)` |   
  
### EnableGeminiInBigquery
    
    
    [Obsolete]
    public bool EnableGeminiInBigquery { get; set; }

Optional. Deprecated: "Gemini in BigQuery" is now available by default for all BigQuery editions and should not be explicitly set. Controls if "Gemini in BigQuery" (<https://cloud.google.com/gemini/docs/bigquery/overview>) features should be enabled for this reservation assignment.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### JobType
    
    
    public Assignment.Types.JobType JobType { get; set; }

Optional. Which type of jobs will use the reservation.

**Property Value**  
---  
**Type** | **Description**  
`[Assignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Reservation.V1/latest/Google.Cloud.BigQuery.Reservation.V1.Assignment)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Reservation.V1/latest/Google.Cloud.BigQuery.Reservation.V1.Assignment.Types)[JobType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Reservation.V1/latest/Google.Cloud.BigQuery.Reservation.V1.Assignment.Types.JobType)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. Name of the resource. E.g.: `projects/myproject/locations/US/reservations/team1-prod/assignments/123`. The assignment_id must only contain lower case alphanumeric characters or dashes and the max length is 64 characters.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Precedence
    
    
    public long Precedence { get; set; }

Optional. Specifies the priority precedence for this assignment. Used to resolve ambiguity when multiple assignments match a single job. Higher numerical values represent higher priority (e.g., 20 is higher than 10). If unspecified, it defaults to 0. Multiple assignments can share the same precedence, but it is recommended to use unique precedence values for assignments within the same assignee scope.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### Principal
    
    
    public string Principal { get; set; }

Optional. Represents the principal for this assignment. If not empty, jobs run by this principal utilize the associated reservation. Otherwise, jobs fall back to using the reservation assigned to the project, folder, or organization, in that order. If no reservation is assigned at any of these levels, on-demand capacity is used.

The supported formats are:

  * `principal://goog/subject/USER_EMAIL_ADDRESS` for users,
  * `principal://iam.googleapis.com/projects/-/serviceAccounts/SA_EMAIL_ADDRESS` for service accounts,
  * `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT_ID` for workload identity pool identities.
  * The special value `unknown_or_deleted_user` represents principals which cannot be read from the user info service, for example, deleted users.



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SchedulingPolicy
    
    
    public SchedulingPolicy SchedulingPolicy { get; set; }

Optional. The scheduling policy to use for jobs and queries of this assignee when running under the associated reservation. The scheduling policy controls how the reservation's resources are distributed. This overrides the default scheduling policy specified on the reservation.

This feature is not yet generally available.

**Property Value**  
---  
**Type** | **Description**  
`[SchedulingPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Reservation.V1/latest/Google.Cloud.BigQuery.Reservation.V1.SchedulingPolicy)` |   
  
### State
    
    
    public Assignment.Types.State State { get; set; }

Output only. State of the assignment.

**Property Value**  
---  
**Type** | **Description**  
`[Assignment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Reservation.V1/latest/Google.Cloud.BigQuery.Reservation.V1.Assignment)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Reservation.V1/latest/Google.Cloud.BigQuery.Reservation.V1.Assignment.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Reservation.V1/latest/Google.Cloud.BigQuery.Reservation.V1.Assignment.Types.State)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
