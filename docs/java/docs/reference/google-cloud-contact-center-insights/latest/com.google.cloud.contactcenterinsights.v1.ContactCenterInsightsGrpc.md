---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsGrpc
title: Class ContactCenterInsightsGrpc (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:18.026042+00:00
---

# Class ContactCenterInsightsGrpc (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ContactCenterInsightsGrpc (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.10  2.2.7 
    
    
    public final class ContactCenterInsightsGrpc

An API that lets users analyze and explore their business conversation data.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ContactCenterInsightsGrpc

## Inherited Members

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

## Static Fields 

### SERVICE_NAME
    
    
    public static final String SERVICE_NAME

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### bindService(ContactCenterInsightsGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(ContactCenterInsightsGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[ContactCenterInsightsGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getBulkAnalyzeConversationsMethod()
    
    
    public static MethodDescriptor<BulkAnalyzeConversationsRequest,Operation> getBulkAnalyzeConversationsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[BulkAnalyzeConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.BulkAnalyzeConversationsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getBulkDeleteConversationsMethod()
    
    
    public static MethodDescriptor<BulkDeleteConversationsRequest,Operation> getBulkDeleteConversationsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[BulkDeleteConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.BulkDeleteConversationsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getBulkDownloadFeedbackLabelsMethod()
    
    
    public static MethodDescriptor<BulkDownloadFeedbackLabelsRequest,Operation> getBulkDownloadFeedbackLabelsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[BulkDownloadFeedbackLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.BulkDownloadFeedbackLabelsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getBulkUploadFeedbackLabelsMethod()
    
    
    public static MethodDescriptor<BulkUploadFeedbackLabelsRequest,Operation> getBulkUploadFeedbackLabelsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[BulkUploadFeedbackLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.BulkUploadFeedbackLabelsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCalculateIssueModelStatsMethod()
    
    
    public static MethodDescriptor<CalculateIssueModelStatsRequest,CalculateIssueModelStatsResponse> getCalculateIssueModelStatsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CalculateIssueModelStatsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.CalculateIssueModelStatsRequest),[CalculateIssueModelStatsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.CalculateIssueModelStatsResponse)>` |   
  
### getCalculateStatsMethod()
    
    
    public static MethodDescriptor<CalculateStatsRequest,CalculateStatsResponse> getCalculateStatsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CalculateStatsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.CalculateStatsRequest),[CalculateStatsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.CalculateStatsResponse)>` |   
  
### getCreateAnalysisMethod()
    
    
    public static MethodDescriptor<CreateAnalysisRequest,Operation> getCreateAnalysisMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateAnalysisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.CreateAnalysisRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateAnalysisRuleMethod()
    
    
    public static MethodDescriptor<CreateAnalysisRuleRequest,AnalysisRule> getCreateAnalysisRuleMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateAnalysisRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.CreateAnalysisRuleRequest),[AnalysisRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.AnalysisRule)>` |   
  
### getCreateConversationMethod()
    
    
    public static MethodDescriptor<CreateConversationRequest,Conversation> getCreateConversationMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.CreateConversationRequest),[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Conversation)>` |   
  
### getCreateFeedbackLabelMethod()
    
    
    public static MethodDescriptor<CreateFeedbackLabelRequest,FeedbackLabel> getCreateFeedbackLabelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateFeedbackLabelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.CreateFeedbackLabelRequest),[FeedbackLabel](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.FeedbackLabel)>` |   
  
### getCreateIssueModelMethod()
    
    
    public static MethodDescriptor<CreateIssueModelRequest,Operation> getCreateIssueModelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateIssueModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.CreateIssueModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreatePhraseMatcherMethod()
    
    
    public static MethodDescriptor<CreatePhraseMatcherRequest,PhraseMatcher> getCreatePhraseMatcherMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreatePhraseMatcherRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.CreatePhraseMatcherRequest),[PhraseMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher)>` |   
  
### getCreateQaQuestionMethod()
    
    
    public static MethodDescriptor<CreateQaQuestionRequest,QaQuestion> getCreateQaQuestionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateQaQuestionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.CreateQaQuestionRequest),[QaQuestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.QaQuestion)>` |   
  
### getCreateQaScorecardMethod()
    
    
    public static MethodDescriptor<CreateQaScorecardRequest,QaScorecard> getCreateQaScorecardMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateQaScorecardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.CreateQaScorecardRequest),[QaScorecard](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.QaScorecard)>` |   
  
### getCreateQaScorecardRevisionMethod()
    
    
    public static MethodDescriptor<CreateQaScorecardRevisionRequest,QaScorecardRevision> getCreateQaScorecardRevisionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateQaScorecardRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.CreateQaScorecardRevisionRequest),[QaScorecardRevision](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.QaScorecardRevision)>` |   
  
### getCreateViewMethod()
    
    
    public static MethodDescriptor<CreateViewRequest,View> getCreateViewMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.CreateViewRequest),[View](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.View)>` |   
  
### getDeleteAnalysisMethod()
    
    
    public static MethodDescriptor<DeleteAnalysisRequest,Empty> getDeleteAnalysisMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteAnalysisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.DeleteAnalysisRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeleteAnalysisRuleMethod()
    
    
    public static MethodDescriptor<DeleteAnalysisRuleRequest,Empty> getDeleteAnalysisRuleMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteAnalysisRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.DeleteAnalysisRuleRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeleteConversationMethod()
    
    
    public static MethodDescriptor<DeleteConversationRequest,Empty> getDeleteConversationMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.DeleteConversationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeleteFeedbackLabelMethod()
    
    
    public static MethodDescriptor<DeleteFeedbackLabelRequest,Empty> getDeleteFeedbackLabelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteFeedbackLabelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.DeleteFeedbackLabelRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeleteIssueMethod()
    
    
    public static MethodDescriptor<DeleteIssueRequest,Empty> getDeleteIssueMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteIssueRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.DeleteIssueRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeleteIssueModelMethod()
    
    
    public static MethodDescriptor<DeleteIssueModelRequest,Operation> getDeleteIssueModelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteIssueModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.DeleteIssueModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeletePhraseMatcherMethod()
    
    
    public static MethodDescriptor<DeletePhraseMatcherRequest,Empty> getDeletePhraseMatcherMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeletePhraseMatcherRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.DeletePhraseMatcherRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeleteQaQuestionMethod()
    
    
    public static MethodDescriptor<DeleteQaQuestionRequest,Empty> getDeleteQaQuestionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteQaQuestionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.DeleteQaQuestionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeleteQaScorecardMethod()
    
    
    public static MethodDescriptor<DeleteQaScorecardRequest,Empty> getDeleteQaScorecardMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteQaScorecardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.DeleteQaScorecardRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeleteQaScorecardRevisionMethod()
    
    
    public static MethodDescriptor<DeleteQaScorecardRevisionRequest,Empty> getDeleteQaScorecardRevisionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteQaScorecardRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.DeleteQaScorecardRevisionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeleteViewMethod()
    
    
    public static MethodDescriptor<DeleteViewRequest,Empty> getDeleteViewMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.DeleteViewRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeployIssueModelMethod()
    
    
    public static MethodDescriptor<DeployIssueModelRequest,Operation> getDeployIssueModelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeployIssueModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.DeployIssueModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeployQaScorecardRevisionMethod()
    
    
    public static MethodDescriptor<DeployQaScorecardRevisionRequest,QaScorecardRevision> getDeployQaScorecardRevisionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeployQaScorecardRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.DeployQaScorecardRevisionRequest),[QaScorecardRevision](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.QaScorecardRevision)>` |   
  
### getExportInsightsDataMethod()
    
    
    public static MethodDescriptor<ExportInsightsDataRequest,Operation> getExportInsightsDataMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ExportInsightsDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ExportInsightsDataRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getExportIssueModelMethod()
    
    
    public static MethodDescriptor<ExportIssueModelRequest,Operation> getExportIssueModelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ExportIssueModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ExportIssueModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getGetAnalysisMethod()
    
    
    public static MethodDescriptor<GetAnalysisRequest,Analysis> getGetAnalysisMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetAnalysisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.GetAnalysisRequest),[Analysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Analysis)>` |   
  
### getGetAnalysisRuleMethod()
    
    
    public static MethodDescriptor<GetAnalysisRuleRequest,AnalysisRule> getGetAnalysisRuleMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetAnalysisRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.GetAnalysisRuleRequest),[AnalysisRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.AnalysisRule)>` |   
  
### getGetConversationMethod()
    
    
    public static MethodDescriptor<GetConversationRequest,Conversation> getGetConversationMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.GetConversationRequest),[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Conversation)>` |   
  
### getGetEncryptionSpecMethod()
    
    
    public static MethodDescriptor<GetEncryptionSpecRequest,EncryptionSpec> getGetEncryptionSpecMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetEncryptionSpecRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.GetEncryptionSpecRequest),[EncryptionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.EncryptionSpec)>` |   
  
### getGetFeedbackLabelMethod()
    
    
    public static MethodDescriptor<GetFeedbackLabelRequest,FeedbackLabel> getGetFeedbackLabelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetFeedbackLabelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.GetFeedbackLabelRequest),[FeedbackLabel](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.FeedbackLabel)>` |   
  
### getGetIssueMethod()
    
    
    public static MethodDescriptor<GetIssueRequest,Issue> getGetIssueMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetIssueRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.GetIssueRequest),[Issue](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Issue)>` |   
  
### getGetIssueModelMethod()
    
    
    public static MethodDescriptor<GetIssueModelRequest,IssueModel> getGetIssueModelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetIssueModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.GetIssueModelRequest),[IssueModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.IssueModel)>` |   
  
### getGetPhraseMatcherMethod()
    
    
    public static MethodDescriptor<GetPhraseMatcherRequest,PhraseMatcher> getGetPhraseMatcherMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetPhraseMatcherRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.GetPhraseMatcherRequest),[PhraseMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher)>` |   
  
### getGetQaQuestionMethod()
    
    
    public static MethodDescriptor<GetQaQuestionRequest,QaQuestion> getGetQaQuestionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetQaQuestionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.GetQaQuestionRequest),[QaQuestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.QaQuestion)>` |   
  
### getGetQaScorecardMethod()
    
    
    public static MethodDescriptor<GetQaScorecardRequest,QaScorecard> getGetQaScorecardMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetQaScorecardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.GetQaScorecardRequest),[QaScorecard](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.QaScorecard)>` |   
  
### getGetQaScorecardRevisionMethod()
    
    
    public static MethodDescriptor<GetQaScorecardRevisionRequest,QaScorecardRevision> getGetQaScorecardRevisionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetQaScorecardRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.GetQaScorecardRevisionRequest),[QaScorecardRevision](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.QaScorecardRevision)>` |   
  
### getGetSettingsMethod()
    
    
    public static MethodDescriptor<GetSettingsRequest,Settings> getGetSettingsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.GetSettingsRequest),[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Settings)>` |   
  
### getGetViewMethod()
    
    
    public static MethodDescriptor<GetViewRequest,View> getGetViewMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.GetViewRequest),[View](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.View)>` |   
  
### getImportIssueModelMethod()
    
    
    public static MethodDescriptor<ImportIssueModelRequest,Operation> getImportIssueModelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ImportIssueModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ImportIssueModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getIngestConversationsMethod()
    
    
    public static MethodDescriptor<IngestConversationsRequest,Operation> getIngestConversationsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[IngestConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.IngestConversationsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getInitializeEncryptionSpecMethod()
    
    
    public static MethodDescriptor<InitializeEncryptionSpecRequest,Operation> getInitializeEncryptionSpecMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[InitializeEncryptionSpecRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.InitializeEncryptionSpecRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getListAllFeedbackLabelsMethod()
    
    
    public static MethodDescriptor<ListAllFeedbackLabelsRequest,ListAllFeedbackLabelsResponse> getListAllFeedbackLabelsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListAllFeedbackLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListAllFeedbackLabelsRequest),[ListAllFeedbackLabelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListAllFeedbackLabelsResponse)>` |   
  
### getListAnalysesMethod()
    
    
    public static MethodDescriptor<ListAnalysesRequest,ListAnalysesResponse> getListAnalysesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListAnalysesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListAnalysesRequest),[ListAnalysesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListAnalysesResponse)>` |   
  
### getListAnalysisRulesMethod()
    
    
    public static MethodDescriptor<ListAnalysisRulesRequest,ListAnalysisRulesResponse> getListAnalysisRulesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListAnalysisRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListAnalysisRulesRequest),[ListAnalysisRulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListAnalysisRulesResponse)>` |   
  
### getListConversationsMethod()
    
    
    public static MethodDescriptor<ListConversationsRequest,ListConversationsResponse> getListConversationsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListConversationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListConversationsRequest),[ListConversationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListConversationsResponse)>` |   
  
### getListFeedbackLabelsMethod()
    
    
    public static MethodDescriptor<ListFeedbackLabelsRequest,ListFeedbackLabelsResponse> getListFeedbackLabelsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListFeedbackLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListFeedbackLabelsRequest),[ListFeedbackLabelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListFeedbackLabelsResponse)>` |   
  
### getListIssueModelsMethod()
    
    
    public static MethodDescriptor<ListIssueModelsRequest,ListIssueModelsResponse> getListIssueModelsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListIssueModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListIssueModelsRequest),[ListIssueModelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListIssueModelsResponse)>` |   
  
### getListIssuesMethod()
    
    
    public static MethodDescriptor<ListIssuesRequest,ListIssuesResponse> getListIssuesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListIssuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListIssuesRequest),[ListIssuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListIssuesResponse)>` |   
  
### getListPhraseMatchersMethod()
    
    
    public static MethodDescriptor<ListPhraseMatchersRequest,ListPhraseMatchersResponse> getListPhraseMatchersMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListPhraseMatchersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListPhraseMatchersRequest),[ListPhraseMatchersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListPhraseMatchersResponse)>` |   
  
### getListQaQuestionsMethod()
    
    
    public static MethodDescriptor<ListQaQuestionsRequest,ListQaQuestionsResponse> getListQaQuestionsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListQaQuestionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListQaQuestionsRequest),[ListQaQuestionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListQaQuestionsResponse)>` |   
  
### getListQaScorecardRevisionsMethod()
    
    
    public static MethodDescriptor<ListQaScorecardRevisionsRequest,ListQaScorecardRevisionsResponse> getListQaScorecardRevisionsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListQaScorecardRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListQaScorecardRevisionsRequest),[ListQaScorecardRevisionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListQaScorecardRevisionsResponse)>` |   
  
### getListQaScorecardsMethod()
    
    
    public static MethodDescriptor<ListQaScorecardsRequest,ListQaScorecardsResponse> getListQaScorecardsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListQaScorecardsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListQaScorecardsRequest),[ListQaScorecardsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListQaScorecardsResponse)>` |   
  
### getListViewsMethod()
    
    
    public static MethodDescriptor<ListViewsRequest,ListViewsResponse> getListViewsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListViewsRequest),[ListViewsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ListViewsResponse)>` |   
  
### getQueryMetricsMethod()
    
    
    public static MethodDescriptor<QueryMetricsRequest,Operation> getQueryMetricsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[QueryMetricsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.QueryMetricsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getTuneQaScorecardRevisionMethod()
    
    
    public static MethodDescriptor<TuneQaScorecardRevisionRequest,Operation> getTuneQaScorecardRevisionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[TuneQaScorecardRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.TuneQaScorecardRevisionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getUndeployIssueModelMethod()
    
    
    public static MethodDescriptor<UndeployIssueModelRequest,Operation> getUndeployIssueModelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UndeployIssueModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.UndeployIssueModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getUndeployQaScorecardRevisionMethod()
    
    
    public static MethodDescriptor<UndeployQaScorecardRevisionRequest,QaScorecardRevision> getUndeployQaScorecardRevisionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UndeployQaScorecardRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.UndeployQaScorecardRevisionRequest),[QaScorecardRevision](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.QaScorecardRevision)>` |   
  
### getUpdateAnalysisRuleMethod()
    
    
    public static MethodDescriptor<UpdateAnalysisRuleRequest,AnalysisRule> getUpdateAnalysisRuleMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateAnalysisRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.UpdateAnalysisRuleRequest),[AnalysisRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.AnalysisRule)>` |   
  
### getUpdateConversationMethod()
    
    
    public static MethodDescriptor<UpdateConversationRequest,Conversation> getUpdateConversationMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.UpdateConversationRequest),[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Conversation)>` |   
  
### getUpdateFeedbackLabelMethod()
    
    
    public static MethodDescriptor<UpdateFeedbackLabelRequest,FeedbackLabel> getUpdateFeedbackLabelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateFeedbackLabelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.UpdateFeedbackLabelRequest),[FeedbackLabel](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.FeedbackLabel)>` |   
  
### getUpdateIssueMethod()
    
    
    public static MethodDescriptor<UpdateIssueRequest,Issue> getUpdateIssueMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateIssueRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.UpdateIssueRequest),[Issue](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Issue)>` |   
  
### getUpdateIssueModelMethod()
    
    
    public static MethodDescriptor<UpdateIssueModelRequest,IssueModel> getUpdateIssueModelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateIssueModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.UpdateIssueModelRequest),[IssueModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.IssueModel)>` |   
  
### getUpdatePhraseMatcherMethod()
    
    
    public static MethodDescriptor<UpdatePhraseMatcherRequest,PhraseMatcher> getUpdatePhraseMatcherMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdatePhraseMatcherRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.UpdatePhraseMatcherRequest),[PhraseMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.PhraseMatcher)>` |   
  
### getUpdateQaQuestionMethod()
    
    
    public static MethodDescriptor<UpdateQaQuestionRequest,QaQuestion> getUpdateQaQuestionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateQaQuestionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.UpdateQaQuestionRequest),[QaQuestion](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.QaQuestion)>` |   
  
### getUpdateQaScorecardMethod()
    
    
    public static MethodDescriptor<UpdateQaScorecardRequest,QaScorecard> getUpdateQaScorecardMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateQaScorecardRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.UpdateQaScorecardRequest),[QaScorecard](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.QaScorecard)>` |   
  
### getUpdateSettingsMethod()
    
    
    public static MethodDescriptor<UpdateSettingsRequest,Settings> getUpdateSettingsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.UpdateSettingsRequest),[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.Settings)>` |   
  
### getUpdateViewMethod()
    
    
    public static MethodDescriptor<UpdateViewRequest,View> getUpdateViewMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.UpdateViewRequest),[View](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.View)>` |   
  
### getUploadConversationMethod()
    
    
    public static MethodDescriptor<UploadConversationRequest,Operation> getUploadConversationMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UploadConversationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.UploadConversationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static ContactCenterInsightsGrpc.ContactCenterInsightsBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContactCenterInsightsGrpc.ContactCenterInsightsBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsGrpc.ContactCenterInsightsBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static ContactCenterInsightsGrpc.ContactCenterInsightsBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContactCenterInsightsGrpc.ContactCenterInsightsBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsGrpc.ContactCenterInsightsBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static ContactCenterInsightsGrpc.ContactCenterInsightsFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContactCenterInsightsGrpc.ContactCenterInsightsFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsGrpc.ContactCenterInsightsFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static ContactCenterInsightsGrpc.ContactCenterInsightsStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContactCenterInsightsGrpc.ContactCenterInsightsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-contact-center-insights/latest/com.google.cloud.contactcenterinsights.v1.ContactCenterInsightsGrpc.ContactCenterInsightsStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
