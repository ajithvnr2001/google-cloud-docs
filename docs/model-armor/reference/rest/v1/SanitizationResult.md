---
url: https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult/
title: SanitizationResult \u00a0|\u00a0 Model Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:46:30.768463+00:00
---

# SanitizationResult  |  Model Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Reference ](https://docs.cloud.google.com/model-armor/reference/libraries)



Send feedback 

#  SanitizationResult Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * FilterMatchState
  * FilterResult
    * JSON representation
  * RaiFilterResult
    * JSON representation
  * FilterExecutionState
  * MessageItem
    * JSON representation
  * MessageType
  * RaiFilterTypeResult
    * JSON representation
  * SdpFilterResult
    * JSON representation
  * SdpInspectResult
    * JSON representation
  * SdpFinding
    * JSON representation
  * SdpFindingLikelihood
  * SdpFindingLocation
    * JSON representation
  * RangeInfo
    * JSON representation
  * SdpContentLocation
    * JSON representation
  * SdpImageFindingLocation
    * JSON representation
  * SdpBoundingBox
    * JSON representation
  * SdpDeidentifyResult
    * JSON representation
  * SdpRedactResult
    * JSON representation
  * PiAndJailbreakFilterResult
    * JSON representation
  * MaliciousUriFilterResult
    * JSON representation
  * MaliciousUriMatchedItem
    * JSON representation
  * CsamFilterResult
    * JSON representation
  * VirusScanFilterResult
    * JSON representation
  * ScannedContentType
  * VirusDetail
    * JSON representation
  * ThreatType
  * InvocationResult
  * SanitizationMetadata
    * JSON representation
  * FilterVersionConfig
    * JSON representation
  * Date
    * JSON representation



Sanitization result after applying all the filters on input content.

JSON representation  
---  
      
    
    {
      "filterMatchState": enum ([FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)),
      "filterResults": {
        string: {
          object ([FilterResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterResult))
        },
        ...
      },
      "invocationResult": enum ([InvocationResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#InvocationResult)),
      "sanitizationMetadata": {
        object ([SanitizationMetadata](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SanitizationMetadata))
      }
    }  
  
Fields  
---  
`filterMatchState` |  `enum (`[FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)`)` Output only. Overall filter match state for Sanitization. The state can have below two values.1) NO_MATCH_FOUND: No filters in configuration satisfy matching criteria. In other words, input passed all filters.2) MATCH_FOUND: At least one filter in configuration satisfies matching. In other words, input did not pass one or more filters.  
`filterResults` |  `map (key: string, value: object (`[FilterResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterResult)`))` Output only. Results for all filters where the key is the filter name - either of "csam", "malicious_uris", "rai", "pi_and_jailbreak", "sdp".An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`invocationResult` |  `enum (`[InvocationResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#InvocationResult)`)` Output only. A field indicating the outcome of the invocation, irrespective of match status. It can have the following three values: SUCCESS: All filters were executed successfully. PARTIAL: Some filters were skipped or failed execution. FAILURE: All filters were skipped or failed execution.  
`sanitizationMetadata` |  `object (`[SanitizationMetadata](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SanitizationMetadata)`)` Output only. Metadata related to Sanitization.  
  
## FilterMatchState

Option to specify filter match state.

Enums  
---  
`FILTER_MATCH_STATE_UNSPECIFIED` | Unused  
`NO_MATCH_FOUND` | Matching criteria is not achieved for filters.  
`MATCH_FOUND` | Matching criteria is achieved for the filter.  
  
## FilterResult

Filter Result obtained after Sanitization operations.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "raiFilterResult": {
        object ([RaiFilterResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#RaiFilterResult))
      },
      "sdpFilterResult": {
        object ([SdpFilterResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpFilterResult))
      },
      "piAndJailbreakFilterResult": {
        object ([PiAndJailbreakFilterResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#PiAndJailbreakFilterResult))
      },
      "maliciousUriFilterResult": {
        object ([MaliciousUriFilterResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MaliciousUriFilterResult))
      },
      "csamFilterFilterResult": {
        object ([CsamFilterResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#CsamFilterResult))
      },
      "virusScanFilterResult": {
        object ([VirusScanFilterResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#VirusScanFilterResult))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Encapsulates one of responsible AI, Sensitive Data Protection, Prompt Injection and Jailbreak, Malicious URI, CSAM, Virus Scan related filter results. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`raiFilterResult` |  `object (`[RaiFilterResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#RaiFilterResult)`)` Responsible AI filter results.  
`sdpFilterResult` |  `object (`[SdpFilterResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpFilterResult)`)` Sensitive Data Protection results.  
`piAndJailbreakFilterResult` |  `object (`[PiAndJailbreakFilterResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#PiAndJailbreakFilterResult)`)` Prompt injection and Jailbreak filter results.  
`maliciousUriFilterResult` |  `object (`[MaliciousUriFilterResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MaliciousUriFilterResult)`)` Malicious URI filter results.  
`csamFilterFilterResult` |  `object (`[CsamFilterResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#CsamFilterResult)`)` CSAM filter results.  
`virusScanFilterResult` |  `object (`[VirusScanFilterResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#VirusScanFilterResult)`)` Virus scan results.  
End of mutually exclusive fields.  
  
## RaiFilterResult

Responsible AI Result.

JSON representation  
---  
      
    
    {
      "executionState": enum ([FilterExecutionState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterExecutionState)),
      "messageItems": [
        {
          object ([MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem))
        }
      ],
      "matchState": enum ([FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)),
      "raiFilterTypeResults": {
        string: {
          object ([RaiFilterTypeResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#RaiFilterTypeResult))
        },
        ...
      }
    }  
  
Fields  
---  
`executionState` |  `enum (`[FilterExecutionState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterExecutionState)`)` Output only. Reports whether the RAI filter was successfully executed or not.  
`messageItems[]` |  `object (`[MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem)`)` Optional messages corresponding to the result. A message can provide warnings or error details. For example, if execution state is skipped then this field provides related reason/explanation.  
`matchState` |  `enum (`[FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)`)` Output only. Overall filter match state for RAI. Value is MATCH_FOUND if at least one RAI filter confidence level is equal to or higher than the confidence level defined in configuration.  
`raiFilterTypeResults` |  `map (key: string, value: object (`[RaiFilterTypeResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#RaiFilterTypeResult)`))` The map of RAI filter results where the key is the RAI filter type and the value is the RAI filter's result. Allowed keys are "sexually_explicit", "hate_speech", "harassment", and "dangerous".An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## FilterExecutionState

Enum which reports whether a specific filter executed successfully or not.

Enums  
---  
`FILTER_EXECUTION_STATE_UNSPECIFIED` | Unused  
`EXECUTION_SUCCESS` | Filter executed successfully  
`EXECUTION_SKIPPED` | Filter execution was skipped. This can happen due to server-side error or permission issue.  
  
## MessageItem

Message item to report information, warning or error messages.

JSON representation  
---  
      
    
    {
      "messageType": enum ([MessageType](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageType)),
      "message": string
    }  
  
Fields  
---  
`messageType` |  `enum (`[MessageType](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageType)`)` Type of message.  
`message` |  `string` The message content.  
  
## MessageType

Option to specify the type of message.

Enums  
---  
`MESSAGE_TYPE_UNSPECIFIED` | Unused  
`INFO` | Information related message.  
`WARNING` | Warning related message.  
`ERROR` | Error message.  
  
## RaiFilterTypeResult

Detailed Filter result for each of the responsible AI Filter Types.

JSON representation  
---  
      
    
    {
      "filterType": enum ([RaiFilterType](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#RaiFilterType)),
      "confidenceLevel": enum ([DetectionConfidenceLevel](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#DetectionConfidenceLevel)),
      "matchState": enum ([FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState))
    }  
  
Fields  
---  
`filterType` |  `enum (`[RaiFilterType](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#RaiFilterType)`)` Type of responsible AI filter.  
`confidenceLevel` |  `enum (`[DetectionConfidenceLevel](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#DetectionConfidenceLevel)`)` Confidence level identified for this RAI filter.  
`matchState` |  `enum (`[FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)`)` Output only. Match state for this RAI filter.  
  
## SdpFilterResult

Sensitive Data Protection filter result.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "inspectResult": {
        object ([SdpInspectResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpInspectResult))
      },
      "deidentifyResult": {
        object ([SdpDeidentifyResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpDeidentifyResult))
      },
      "redactResult": {
        object ([SdpRedactResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpRedactResult))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Either of Sensitive Data Protection Inspect result or Deidentify result. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`inspectResult` |  `object (`[SdpInspectResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpInspectResult)`)` Sensitive Data Protection Inspection result if inspection is performed.  
`deidentifyResult` |  `object (`[SdpDeidentifyResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpDeidentifyResult)`)` Sensitive Data Protection Deidentification result if deidentification is performed.  
`redactResult` |  `object (`[SdpRedactResult](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpRedactResult)`)` Sensitive Data Protection Redaction result if redaction is performed. This is primarily used for image redaction.  
End of mutually exclusive fields.  
  
## SdpInspectResult

Sensitive Data Protection Inspection Result.

JSON representation  
---  
      
    
    {
      "executionState": enum ([FilterExecutionState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterExecutionState)),
      "messageItems": [
        {
          object ([MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem))
        }
      ],
      "matchState": enum ([FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)),
      "findings": [
        {
          object ([SdpFinding](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpFinding))
        }
      ],
      "findingsTruncated": boolean,
      "extractedImageText": string
    }  
  
Fields  
---  
`executionState` |  `enum (`[FilterExecutionState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterExecutionState)`)` Output only. Reports whether Sensitive Data Protection inspection was successfully executed or not.  
`messageItems[]` |  `object (`[MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem)`)` Optional messages corresponding to the result. A message can provide warnings or error details. For example, if execution state is skipped then this field provides related reason/explanation.  
`matchState` |  `enum (`[FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)`)` Output only. Match state for SDP Inspection. Value is MATCH_FOUND if at least one Sensitive Data Protection finding is identified.  
`findings[]` |  `object (`[SdpFinding](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpFinding)`)` List of Sensitive Data Protection findings.  
`findingsTruncated` |  `boolean` If true, then there is possibility that more findings were identified and the findings returned are a subset of all findings. The findings list might be truncated because the input items were too large, or because the server reached the maximum amount of resources allowed for a single API call.  
`extractedImageText` |  `string` Contains text extracted from the image, if applicable.  
  
## SdpFinding

Finding corresponding to Sensitive Data Protection filter.

JSON representation  
---  
      
    
    {
      "infoType": string,
      "likelihood": enum ([SdpFindingLikelihood](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpFindingLikelihood)),
      "location": {
        object ([SdpFindingLocation](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpFindingLocation))
      }
    }  
  
Fields  
---  
`infoType` |  `string` Name of Sensitive Data Protection info type for this finding.  
`likelihood` |  `enum (`[SdpFindingLikelihood](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpFindingLikelihood)`)` Identified confidence likelihood for `infoType`.  
`location` |  `object (`[SdpFindingLocation](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpFindingLocation)`)` Location for this finding.  
  
## SdpFindingLikelihood

For more information about each Sensitive Data Protection likelihood level, see <https://cloud.google.com/sensitive-data-protection/docs/likelihood>.

Enums  
---  
`SDP_FINDING_LIKELIHOOD_UNSPECIFIED` | Default value; same as POSSIBLE.  
`VERY_UNLIKELY` | Highest chance of a false positive.  
`UNLIKELY` | High chance of a false positive.  
`POSSIBLE` | Some matching signals. The default value.  
`LIKELY` | Low chance of a false positive.  
`VERY_LIKELY` | Confidence level is high. Lowest chance of a false positive.  
  
## SdpFindingLocation

Location of this Sensitive Data Protection Finding within input content.

JSON representation  
---  
      
    
    {
      "byteRange": {
        object ([RangeInfo](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#RangeInfo))
      },
      "codepointRange": {
        object ([RangeInfo](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#RangeInfo))
      },
      "contentLocations": [
        {
          object ([SdpContentLocation](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpContentLocation))
        }
      ]
    }  
  
Fields  
---  
`byteRange` |  `object (`[RangeInfo](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#RangeInfo)`)` Zero-based byte offsets delimiting the finding. These are relative to the finding's containing element. Note that when the content is not textual, this references the UTF-8 encoded textual representation of the content. Note: Omitted if content is an image.  
`codepointRange` |  `object (`[RangeInfo](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#RangeInfo)`)` Unicode character offsets delimiting the finding. These are relative to the finding's containing element. Provided when the content is text. Note: Omitted if content is an image.  
`contentLocations[]` |  `object (`[SdpContentLocation](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpContentLocation)`)` List of nested objects pointing to the precise location of the finding within an image, file or record.For example, a single finding might be detected in two separate bounding boxes within an image (e.g., if it wraps across a line or is partially obscured). In such cases, contentLocations would contain two SdpContentLocation entries, each with an imageFindingLocation pointing to a different bounding box.  
  
## RangeInfo

Half-open range interval [start, end)

JSON representation  
---  
      
    
    {
      "start": string,
      "end": string
    }  
  
Fields  
---  
`start` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` For proto3, value cannot be set to 0 unless the field is optional. Ref: <https://protobuf.dev/programming-guides/proto3/#default> Index of first character (inclusive).  
`end` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Index of last character (exclusive).  
  
## SdpContentLocation

Precise location of the finding within a document, record, image, or metadata container.

JSON representation  
---  
      
    
    {
      "containerName": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "imageFindingLocation": {
        object ([SdpImageFindingLocation](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpImageFindingLocation))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`containerName` |  `string` Name of the container where the finding is located. The top level name is the source file name or table name.Nested names could be absent if the embedded object has no string identifier (for example, an image contained within a document).  
Type of the container within the file with location of the finding. This may be extended to include other container types like audio, video, etc in future. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`imageFindingLocation` |  `object (`[SdpImageFindingLocation](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpImageFindingLocation)`)` Location within an image's pixels.  
End of mutually exclusive fields.  
  
## SdpImageFindingLocation

Location of the finding within an image.

JSON representation  
---  
      
    
    {
      "boundingBoxes": [
        {
          object ([SdpBoundingBox](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpBoundingBox))
        }
      ]
    }  
  
Fields  
---  
`boundingBoxes[]` |  `object (`[SdpBoundingBox](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpBoundingBox)`)` Bounding boxes locating the pixels within the image containing the finding.  
  
## SdpBoundingBox

Bounding box encompassing a finding within an image.

JSON representation  
---  
      
    
    {
      "top": integer,
      "left": integer,
      "width": integer,
      "height": integer
    }  
  
Fields  
---  
`top` |  `integer` Top coordinate of the bounding box. (0,0) is upper left.  
`left` |  `integer` Left coordinate of the bounding box. (0,0) is upper left.  
`width` |  `integer` Width of the bounding box in pixels.  
`height` |  `integer` Height of the bounding box in pixels.  
  
## SdpDeidentifyResult

Sensitive Data Protection Deidentification Result.

JSON representation  
---  
      
    
    {
      "executionState": enum ([FilterExecutionState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterExecutionState)),
      "messageItems": [
        {
          object ([MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem))
        }
      ],
      "matchState": enum ([FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)),
      "data": {
        object ([DataItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/DataItem))
      },
      "transformedBytes": string,
      "infoTypes": [
        string
      ]
    }  
  
Fields  
---  
`executionState` |  `enum (`[FilterExecutionState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterExecutionState)`)` Output only. Reports whether Sensitive Data Protection deidentification was successfully executed or not.  
`messageItems[]` |  `object (`[MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem)`)` Optional messages corresponding to the result. A message can provide warnings or error details. For example, if execution state is skipped then this field provides related reason/explanation.  
`matchState` |  `enum (`[FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)`)` Output only. Match state for Sensitive Data Protection Deidentification. Value is MATCH_FOUND if content is de-identified.  
`data` |  `object (`[DataItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/DataItem)`)` De-identified data.  
`transformedBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total size in bytes that were transformed during deidentification.  
`infoTypes[]` |  `string` List of Sensitive Data Protection info-types that were de-identified.  
  
## SdpRedactResult

Sensitive Data Protection Redaction Result.

JSON representation  
---  
      
    
    {
      "executionState": enum ([FilterExecutionState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterExecutionState)),
      "messageItems": [
        {
          object ([MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem))
        }
      ],
      "matchState": enum ([FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)),
      "redactedImage": string,
      "findings": [
        {
          object ([SdpFinding](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpFinding))
        }
      ],
      "extractedImageText": string
    }  
  
Fields  
---  
`executionState` |  `enum (`[FilterExecutionState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterExecutionState)`)` Output only. Reports whether Sensitive Data Protection redaction was successfully executed or not.  
`messageItems[]` |  `object (`[MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem)`)` Output only. Optional messages corresponding to the result. A message can provide warnings or error details. For example, if execution state is skipped then this field provides related reason/explanation.  
`matchState` |  `enum (`[FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)`)` Output only. Match state for Sensitive Data Protection Redaction. Value is MATCH_FOUND if content is redacted.  
`redactedImage` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The redacted image. The type will be the same as the original image.A base64-encoded string.  
`findings[]` |  `object (`[SdpFinding](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#SdpFinding)`)` Output only. The findings. This field is populated in the response only when include_findings in the SDP template is set to true.  
`extractedImageText` |  `string` The extracted text from the image.  
  
## PiAndJailbreakFilterResult

Prompt injection and Jailbreak Filter Result.

JSON representation  
---  
      
    
    {
      "executionState": enum ([FilterExecutionState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterExecutionState)),
      "messageItems": [
        {
          object ([MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem))
        }
      ],
      "matchState": enum ([FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)),
      "confidenceLevel": enum ([DetectionConfidenceLevel](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#DetectionConfidenceLevel))
    }  
  
Fields  
---  
`executionState` |  `enum (`[FilterExecutionState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterExecutionState)`)` Output only. Reports whether Prompt injection and Jailbreak filter was successfully executed or not.  
`messageItems[]` |  `object (`[MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem)`)` Optional messages corresponding to the result. A message can provide warnings or error details. For example, if execution state is skipped then this field provides related reason/explanation.  
`matchState` |  `enum (`[FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)`)` Output only. Match state for Prompt injection and Jailbreak.  
`confidenceLevel` |  `enum (`[DetectionConfidenceLevel](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#DetectionConfidenceLevel)`)` Confidence level identified for Prompt injection and Jailbreak.  
  
## MaliciousUriFilterResult

Malicious URI Filter Result.

JSON representation  
---  
      
    
    {
      "executionState": enum ([FilterExecutionState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterExecutionState)),
      "messageItems": [
        {
          object ([MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem))
        }
      ],
      "matchState": enum ([FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)),
      "maliciousUriMatchedItems": [
        {
          object ([MaliciousUriMatchedItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MaliciousUriMatchedItem))
        }
      ]
    }  
  
Fields  
---  
`executionState` |  `enum (`[FilterExecutionState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterExecutionState)`)` Output only. Reports whether Malicious URI filter was successfully executed or not.  
`messageItems[]` |  `object (`[MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem)`)` Optional messages corresponding to the result. A message can provide warnings or error details. For example, if execution state is skipped then this field provides related reason/explanation.  
`matchState` |  `enum (`[FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)`)` Output only. Match state for this Malicious URI. Value is MATCH_FOUND if at least one Malicious URI is found.  
`maliciousUriMatchedItems[]` |  `object (`[MaliciousUriMatchedItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MaliciousUriMatchedItem)`)` List of Malicious URIs found in data.  
  
## MaliciousUriMatchedItem

Information regarding malicious URI and its location within the input content.

JSON representation  
---  
      
    
    {
      "uri": string,
      "locations": [
        {
          object ([RangeInfo](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#RangeInfo))
        }
      ]
    }  
  
Fields  
---  
`uri` |  `string` Malicious URI.  
`locations[]` |  `object (`[RangeInfo](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#RangeInfo)`)` List of locations where Malicious URI is identified. The `locations` field is supported only for plaintext content i.e. ByteItemType.PLAINTEXT_UTF8  
  
## CsamFilterResult

CSAM (Child Safety Abuse Material) Filter Result

JSON representation  
---  
      
    
    {
      "executionState": enum ([FilterExecutionState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterExecutionState)),
      "messageItems": [
        {
          object ([MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem))
        }
      ],
      "matchState": enum ([FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState))
    }  
  
Fields  
---  
`executionState` |  `enum (`[FilterExecutionState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterExecutionState)`)` Output only. Reports whether the CSAM filter was successfully executed or not.  
`messageItems[]` |  `object (`[MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem)`)` Optional messages corresponding to the result. A message can provide warnings or error details. For example, if execution state is skipped then this field provides related reason/explanation.  
`matchState` |  `enum (`[FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)`)` Output only. Match state for CSAM.  
  
## VirusScanFilterResult

Virus scan results.

JSON representation  
---  
      
    
    {
      "executionState": enum ([FilterExecutionState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterExecutionState)),
      "messageItems": [
        {
          object ([MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem))
        }
      ],
      "matchState": enum ([FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)),
      "scannedContentType": enum ([ScannedContentType](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#ScannedContentType)),
      "virusDetails": [
        {
          object ([VirusDetail](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#VirusDetail))
        }
      ],
      "scannedSize": string
    }  
  
Fields  
---  
`executionState` |  `enum (`[FilterExecutionState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterExecutionState)`)` Output only. Reports whether Virus Scan was successfully executed or not.  
`messageItems[]` |  `object (`[MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem)`)` Optional messages corresponding to the result. A message can provide warnings or error details. For example, if execution status is skipped then this field provides related reason/explanation.  
`matchState` |  `enum (`[FilterMatchState](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterMatchState)`)` Output only. Match status for Virus. Value is MATCH_FOUND if the data is infected with a virus.  
`scannedContentType` |  `enum (`[ScannedContentType](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#ScannedContentType)`)` Type of content scanned.  
`virusDetails[]` |  `object (`[VirusDetail](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#VirusDetail)`)` List of Viruses identified. This field will be empty if no virus was detected.  
`scannedSize` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Size of scanned content in bytes.  
  
## ScannedContentType

Type of content scanned.

Enums  
---  
`SCANNED_CONTENT_TYPE_UNSPECIFIED` | Unused  
`UNKNOWN` | Unknown content  
`PLAINTEXT` | Plaintext  
`PDF` | PDF Scanning for only PDF is supported.  
  
## VirusDetail

Details of an identified virus

JSON representation  
---  
      
    
    {
      "vendor": string,
      "names": [
        string
      ],
      "threatType": enum ([ThreatType](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#ThreatType))
    }  
  
Fields  
---  
`vendor` |  `string` Name of vendor that produced this virus identification.  
`names[]` |  `string` Names of this Virus.  
`threatType` |  `enum (`[ThreatType](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#ThreatType)`)` Threat type of the identified virus  
  
## ThreatType

Defines all the threat types of a virus

Enums  
---  
`THREAT_TYPE_UNSPECIFIED` | Unused  
`UNKNOWN` | Unable to categorize threat  
`VIRUS_OR_WORM` | Virus or Worm threat.  
`MALICIOUS_PROGRAM` | Malicious program. E.g. Spyware, Trojan.  
`POTENTIALLY_HARMFUL_CONTENT` | Potentially harmful content. E.g. Injected code, Macro  
`POTENTIALLY_UNWANTED_CONTENT` | Potentially unwanted content. E.g. Adware.  
  
## InvocationResult

A field indicating the outcome of the invocation, irrespective of match status.

Enums  
---  
`INVOCATION_RESULT_UNSPECIFIED` | Unused. Default value.  
`SUCCESS` | All filters were invoked successfully.  
`PARTIAL` | Some filters were skipped or failed.  
`FAILURE` | All filters were skipped or failed.  
  
## SanitizationMetadata

Message describing Sanitization metadata.

JSON representation  
---  
      
    
    {
      "errorCode": string,
      "errorMessage": string,
      "ignorePartialInvocationFailures": boolean,
      "streamChunkProcessed": {
        object ([DataItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/DataItem))
      },
      "filterVersionConfig": {
        object ([FilterVersionConfig](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterVersionConfig))
      }
    }  
  
Fields  
---  
`errorCode` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Error code if any.  
`errorMessage` |  `string` Error message if any.  
`ignorePartialInvocationFailures` |  `boolean` Passthrough field defined in TemplateMetadata to indicate whether to ignore partial invocation failures.  
`streamChunkProcessed` |  `object (`[DataItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/DataItem)`)` Output only. The stream chunk processed by the Sanitization service.  
`filterVersionConfig` |  `object (`[FilterVersionConfig](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#FilterVersionConfig)`)` Output only. Provides details about the Filter Version configuration used to sanitize this request.  
  
## FilterVersionConfig

Message describing a Filter Version Configuration.

JSON representation  
---  
      
    
    {
      "filterVersion": string,
      "messageItems": [
        {
          object ([MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem))
        }
      ],
      "filterVersionAlias": enum ([FilterVersionAlias](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#FilterVersionAlias)),
      "releaseDate": {
        object ([Date](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#Date))
      },
      "projectedDeprecationDate": {
        object ([Date](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#Date))
      }
    }  
  
Fields  
---  
`filterVersion` |  `string` Output only. The identifier for this specific version.  
`messageItems[]` |  `object (`[MessageItem](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#MessageItem)`)` Output only. Extra information regarding this filter version  
`filterVersionAlias` |  `enum (`[FilterVersionAlias](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#FilterVersionAlias)`)` Output only. The alias associated with this version, if any (e.g., "STABLE", "LATEST"). This will be populated if this version is currently mapped to an alias.  
`releaseDate` |  `object (`[Date](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#Date)`)` Output only. The date when this version was released.  
`projectedDeprecationDate` |  `object (`[Date](https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult#Date)`)` Output only. The estimated date when this version is projected to be deprecated.  
  
## Date

Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following:

  * A full date, with non-zero year, month, and day values.
  * A month and day, with a zero year (for example, an anniversary).
  * A year on its own, with a zero month and a zero day.
  * A year and month, with a zero day (for example, a credit card expiration date).



Related types:

  * `google.type.TimeOfDay`
  * `google.type.DateTime`
  * `[google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`

JSON representation  
---  
      
    
    {
      "year": integer,
      "month": integer,
      "day": integer
    }  
  
Fields  
---  
`year` |  `integer` Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.  
`month` |  `integer` Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.  
`day` |  `integer` Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
