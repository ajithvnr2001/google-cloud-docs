---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig/
title: InspectConfig \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:46.053608+00:00
---

# InspectConfig  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  InspectConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Likelihood
  * InfoTypeLikelihood
    * JSON representation
  * FindingLimits
    * JSON representation
  * InfoTypeLimit
    * JSON representation
  * CustomInfoType
    * JSON representation
  * SurrogateType
  * StoredType
    * JSON representation
  * MetadataKeyValueExpression
    * JSON representation
  * FileLabelInfoType
    * JSON representation
  * SensitivityLabel
    * JSON representation
  * GoogleDriveLabel
    * JSON representation
  * LabelField
    * JSON representation
  * DetectionRule
    * JSON representation
  * HotwordRule
    * JSON representation
  * Proximity
    * JSON representation
  * LikelihoodAdjustment
    * JSON representation
  * ExclusionType
  * ContentOption
  * InspectionRuleSet
    * JSON representation
  * InspectionRule
    * JSON representation
  * ExclusionRule
    * JSON representation
  * ExcludeInfoTypes
    * JSON representation
  * ExcludeByHotword
    * JSON representation
  * ExcludeByImageFindings
    * JSON representation
  * ImageContainmentType
    * JSON representation
  * Encloses
  * FullyInside
  * Overlap
  * MatchingType
  * AdjustmentRule
    * JSON representation
  * AdjustByMatchingInfoTypes
    * JSON representation
  * AdjustByImageFindings
    * JSON representation



Configuration description of the scanning process. When used with redactContent only infoTypes and minLikelihood are currently used.

JSON representation  
---  
      
    
    {
      "infoTypes": [
        {
          object ([InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType))
        }
      ],
      "minLikelihood": enum ([Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood)),
      "minLikelihoodPerInfoType": [
        {
          object ([InfoTypeLikelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#InfoTypeLikelihood))
        }
      ],
      "limits": {
        object ([FindingLimits](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#FindingLimits))
      },
      "includeQuote": boolean,
      "excludeInfoTypes": boolean,
      "customInfoTypes": [
        {
          object ([CustomInfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#CustomInfoType))
        }
      ],
      "contentOptions": [
        enum ([ContentOption](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#ContentOption))
      ],
      "ruleSet": [
        {
          object ([InspectionRuleSet](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#InspectionRuleSet))
        }
      ]
    }  
  
Fields  
---  
`infoTypes[]` |  `object (`[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)`)` Restricts what infoTypes to look for. The values must correspond to InfoType values returned by infoTypes.list or listed at <https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference>.When no InfoTypes or CustomInfoTypes are specified in a request, the system may automatically choose a default list of detectors to run, which may change over time.If you need precise control and predictability as to what detectors are run you should specify specific InfoTypes listed in the reference, otherwise a default list will be used, which may change over time.  
`minLikelihood` |  `enum (`[Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood)`)` Only returns findings equal to or above this threshold. The default is POSSIBLE.In general, the highest likelihood setting yields the fewest findings in results and the lowest chance of a false positive. For more information, see [Match likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood).  
`minLikelihoodPerInfoType[]` |  `object (`[InfoTypeLikelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#InfoTypeLikelihood)`)` Minimum likelihood per infotype. For each infotype, a user can specify a minimum likelihood. The system only returns a finding if its likelihood is above this threshold. If this field is not set, the system uses the InspectConfig minLikelihood.  
`limits` |  `object (`[FindingLimits](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#FindingLimits)`)` Configuration to control the number of findings returned. This is not used for data profiling.When redacting sensitive data from images, finding limits don't apply. They can cause unexpected or inconsistent results, where only some data is redacted. Don't include finding limits in `[image.redact](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.image/redact#google.privacy.dlp.v2.DlpService.RedactImage)` requests. Otherwise, Cloud DLP returns an error.When set within an `[InspectJobConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig)`, the specified maximum values aren't hard limits. If an inspection job reaches these limits, the job ends gradually, not abruptly. Therefore, the actual number of findings that Cloud DLP returns can be multiple times higher than these maximum values.  
`includeQuote` |  `boolean` When true, a contextual quote from the data that triggered a finding is included in the response; see `[Finding.quote](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#Finding.FIELDS.quote)`. This is not used for data profiling.  
`excludeInfoTypes` |  `boolean` When true, excludes type information of the findings. This is not used for data profiling.  
`customInfoTypes[]` |  `object (`[CustomInfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#CustomInfoType)`)` CustomInfoTypes provided by the user. See <https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes> to learn more.  
`contentOptions[]` |  `enum (`[ContentOption](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#ContentOption)`)` Deprecated and unused.  
`ruleSet[]` |  `object (`[InspectionRuleSet](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#InspectionRuleSet)`)` Set of rules to apply to the findings for this InspectConfig. Exclusion rules, contained in the set are executed in the end, other rules are executed in the order they are specified for each info type. Not supported for the `metadataKeyValueExpression` CustomInfoType.  
  
## Likelihood

Coarse-grained confidence level of how well a particular finding satisfies the criteria to match a particular infoType.

Likelihood is calculated based on the number of signals a finding has that implies that the finding matches the infoType. For example, a string that has an '@' and a '.com' is more likely to be a match for an email address than a string that only has an '@'.

In general, the highest likelihood level has the strongest signals that indicate a match. That is, a finding with a high likelihood has a low chance of being a false positive.

For more information about each likelihood level and how likelihood works, see [Match likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood).

Enums  
---  
`LIKELIHOOD_UNSPECIFIED` | Default value; same as POSSIBLE.  
`VERY_UNLIKELY` | Highest chance of a false positive.  
`UNLIKELY` | High chance of a false positive.  
`POSSIBLE` | Some matching signals. The default value.  
`LIKELY` | Low chance of a false positive.  
`VERY_LIKELY` | Confidence level is high. Lowest chance of a false positive.  
  
## InfoTypeLikelihood

Configuration for setting a minimum likelihood per infotype. Used to customize the minimum likelihood level for specific infotypes in the request. For example, use this if you want to lower the precision for PERSON_NAME without lowering the precision for the other infotypes in the request.

JSON representation  
---  
      
    
    {
      "infoType": {
        object ([InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType))
      },
      "minLikelihood": enum ([Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood))
    }  
  
Fields  
---  
`infoType` |  `object (`[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)`)` Type of information the likelihood threshold applies to. Only one likelihood per infoType should be provided. If InfoTypeLikelihood does not have an infoType, the configuration fails.  
`minLikelihood` |  `enum (`[Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood)`)` Only returns findings equal to or above this threshold. This field is required or else the configuration fails.  
  
## FindingLimits

Configuration to control the number of findings returned for inspection. This is not used for de-identification or data profiling.

When redacting sensitive data from images, finding limits don't apply. They can cause unexpected or inconsistent results, where only some data is redacted. Don't include finding limits in `[image.redact](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.image/redact#google.privacy.dlp.v2.DlpService.RedactImage)` requests. Otherwise, Cloud DLP returns an error.

JSON representation  
---  
      
    
    {
      "maxFindingsPerItem": integer,
      "maxFindingsPerRequest": integer,
      "maxFindingsPerInfoType": [
        {
          object ([InfoTypeLimit](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#InfoTypeLimit))
        }
      ]
    }  
  
Fields  
---  
`maxFindingsPerItem` |  `integer` Max number of findings that are returned for each item scanned.When set within an `InspectContentRequest`, this field is ignored.This value isn't a hard limit. If the number of findings for an item reaches this limit, the inspection of that item ends gradually, not abruptly. Therefore, the actual number of findings that Cloud DLP returns for the item can be multiple times higher than this value.  
`maxFindingsPerRequest` |  `integer` Max number of findings that are returned per request or job.If you set this field in an `InspectContentRequest`, the resulting maximum value is the value that you set or 3,000, whichever is lower.This value isn't a hard limit. If an inspection reaches this limit, the inspection ends gradually, not abruptly. Therefore, the actual number of findings that Cloud DLP returns can be multiple times higher than this value.  
`maxFindingsPerInfoType[]` |  `object (`[InfoTypeLimit](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#InfoTypeLimit)`)` Configuration of findings limit given for specified infoTypes.  
  
## InfoTypeLimit

Max findings configuration per infoType, per content item or long running DlpJob.

JSON representation  
---  
      
    
    {
      "infoType": {
        object ([InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType))
      },
      "maxFindings": integer
    }  
  
Fields  
---  
`infoType` |  `object (`[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)`)` Type of information the findings limit applies to. Only one limit per infoType should be provided. If InfoTypeLimit does not have an infoType, the DLP API applies the limit against all infoTypes that are found but not specified in another InfoTypeLimit.  
`maxFindings` |  `integer` Max findings limit for the given infoType.  
  
## CustomInfoType

Custom information type provided by the user. Used to find domain-specific sensitive information configurable to the data in question.

JSON representation  
---  
      
    
    {
      "infoType": {
        object ([InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType))
      },
      "likelihood": enum ([Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood)),
      "detectionRules": [
        {
          object ([DetectionRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#DetectionRule))
        }
      ],
      "exclusionType": enum ([ExclusionType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#ExclusionType)),
      "sensitivityScore": {
        object ([SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SensitivityScore))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "dictionary": {
        object ([Dictionary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Dictionary))
      },
      "regex": {
        object ([Regex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Regex))
      },
      "surrogateType": {
        object ([SurrogateType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#SurrogateType))
      },
      "storedType": {
        object ([StoredType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#StoredType))
      },
      "metadataKeyValueExpression": {
        object ([MetadataKeyValueExpression](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#MetadataKeyValueExpression))
      },
      "fileLabelInfoType": {
        object ([FileLabelInfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#FileLabelInfoType))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`infoType` |  `object (`[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)`)` CustomInfoType can either be a new infoType, or an extension of built-in infoType, when the name matches one of existing infoTypes and that infoType is specified in `content.inspect.info_types` field. Specifying the latter adds findings to the one detected by the system. If built-in info type is not specified in `content.inspect.info_types` list then the name is treated as a custom info type.  
`likelihood` |  `enum (`[Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood)`)` Likelihood to return for this CustomInfoType. This base value can be altered by a detection rule if the finding meets the criteria specified by the rule. Defaults to `VERY_LIKELY` if not specified.  
`detectionRules[]` |  `object (`[DetectionRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#DetectionRule)`)` Set of detection rules to apply to all findings of this CustomInfoType. Rules are applied in the order that they are specified. Only supported for the `dictionary`, `regex`, and `storedType` CustomInfoTypes.  
`exclusionType` |  `enum (`[ExclusionType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#ExclusionType)`)` If set to EXCLUSION_TYPE_EXCLUDE this infoType will not cause a finding to be returned. It still can be used for rules matching. Only supported for the `dictionary`, `regex`, and `storedType` CustomInfoTypes.  
`sensitivityScore` |  `object (`[SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SensitivityScore)`)` Sensitivity for this CustomInfoType. If this CustomInfoType extends an existing InfoType, the sensitivity here will take precedence over that of the original InfoType. If unset for a CustomInfoType, it will default to HIGH. This only applies to data profiling.  
Type of custom detector. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`dictionary` |  `object (`[Dictionary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Dictionary)`)` A list of phrases to detect as a CustomInfoType.  
`regex` |  `object (`[Regex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Regex)`)` Regular expression based CustomInfoType.  
`surrogateType` |  `object (`[SurrogateType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#SurrogateType)`)` Message for detecting output from deidentification transformations that support reversing.  
`storedType` |  `object (`[StoredType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#StoredType)`)` Loads an existing `StoredInfoType` resource.  
`metadataKeyValueExpression` |  `object (`[MetadataKeyValueExpression](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#MetadataKeyValueExpression)`)` Key-value pair to detect in the metadata.  
`fileLabelInfoType` |  `object (`[FileLabelInfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#FileLabelInfoType)`)` File label to detect.  
End of mutually exclusive fields.  
  
## SurrogateType

This type has no fields.

Message for detecting output from deidentification transformations such as [`CryptoReplaceFfxFpeConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates#cryptoreplaceffxfpeconfig). These types of transformations are those that perform pseudonymization, thereby producing a "surrogate" as output. This should be used in conjunction with a field on the transformation such as `surrogateInfoType`. This CustomInfoType does not support the use of `detectionRules`.

## StoredType

A reference to a StoredInfoType to use with scanning.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string
    }  
  
Fields  
---  
`name` |  `string` Resource name of the requested `StoredInfoType`, for example `organizations/433245324/storedInfoTypes/432452342` or `projects/project-id/storedInfoTypes/432452342`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp indicating when the version of the `StoredInfoType` used for inspection was created. Output-only field, populated by the system.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## MetadataKeyValueExpression

Configuration for a custom infoType that detects key-value pairs in the metadata matching the specified regular expressions.

JSON representation  
---  
      
    
    {
      "keyRegex": string,
      "valueRegex": string
    }  
  
Fields  
---  
`keyRegex` |  `string` The regular expression for the key. Key should be non-empty.  
`valueRegex` |  `string` The regular expression for the value. Value should be non-empty.  
  
## FileLabelInfoType

Configuration for a custom infoType that detects file labels.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "sensitivityLabel": {
        object ([SensitivityLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#SensitivityLabel))
      },
      "googleDriveLabel": {
        object ([GoogleDriveLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#GoogleDriveLabel))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The type of file label to detect. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`sensitivityLabel` |  `object (`[SensitivityLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#SensitivityLabel)`)` Sensitivity labels published by Microsoft.  
`googleDriveLabel` |  `object (`[GoogleDriveLabel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#GoogleDriveLabel)`)` Google Drive labels published by Google.  
End of mutually exclusive fields.  
  
## SensitivityLabel

Sensitivity labels published by Microsoft.

JSON representation  
---  
      
    
    {
      "guid": string
    }  
  
Fields  
---  
`guid` |  `string` The GUID of the sensitivity label.  
  
## GoogleDriveLabel

Google Drive labels published by Google.

JSON representation  
---  
      
    
    {
      "labelId": string,
      "labelFieldsToMatch": [
        {
          object ([LabelField](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#LabelField))
        }
      ]
    }  
  
Fields  
---  
`labelId` |  `string` The [label ID](https://developers.google.com/workspace/drive/labels/guides/overview) of the Google Drive label.  
`labelFieldsToMatch[]` |  `object (`[LabelField](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#LabelField)`)` The field values of the Google Drive label to match.  
  
## LabelField

The field values of the Google Drive label to match.

JSON representation  
---  
      
    
    {
      "id": string,
      "value": string
    }  
  
Fields  
---  
`id` |  `string` The identifier of the Label Field.  
`value` |  `string` The value of the Label Field to match.  
  
## DetectionRule

Deprecated; use `InspectionRuleSet` instead. Rule for modifying a `CustomInfoType` to alter behavior under certain circumstances, depending on the specific details of the rule. Not supported for the `surrogateType` custom infoType.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "hotwordRule": {
        object ([HotwordRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#HotwordRule))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Type of hotword rule. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`hotwordRule` |  `object (`[HotwordRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#HotwordRule)`)` Hotword-based detection rule.  
End of mutually exclusive fields.  
  
## HotwordRule

The rule that adjusts the likelihood of findings within a certain proximity of hotwords.

JSON representation  
---  
      
    
    {
      "hotwordRegex": {
        object ([Regex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Regex))
      },
      "proximity": {
        object ([Proximity](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Proximity))
      },
      "likelihoodAdjustment": {
        object ([LikelihoodAdjustment](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#LikelihoodAdjustment))
      }
    }  
  
Fields  
---  
`hotwordRegex` |  `object (`[Regex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Regex)`)` Regular expression pattern defining what qualifies as a hotword.  
`proximity` |  `object (`[Proximity](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Proximity)`)` Range of characters within which the entire hotword must reside. The total length of the window cannot exceed 1000 characters. The finding itself will be included in the window, so that hotwords can be used to match substrings of the finding itself. Suppose you want Cloud DLP to promote the likelihood of the phone number regex "(\d{3}) \d{3}-\d{4}" if the area code is known to be the area code of a company's office. In this case, use the hotword regex "(xxx)", where "xxx" is the area code in question.For tabular data, if you want to modify the likelihood of an entire column of findngs, see [Hotword example: Set the match likelihood of a table column](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood#match-column-values).  
`likelihoodAdjustment` |  `object (`[LikelihoodAdjustment](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#LikelihoodAdjustment)`)` Likelihood adjustment to apply to all matching findings.  
  
## Proximity

Message for specifying a window around a finding to apply a detection rule.

JSON representation  
---  
      
    
    {
      "windowBefore": integer,
      "windowAfter": integer
    }  
  
Fields  
---  
`windowBefore` |  `integer` Number of characters before the finding to consider. For tabular data, if you want to modify the likelihood of an entire column of findngs, set this to 1. For more information, see [Hotword example: Set the match likelihood of a table column](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood#match-column-values).  
`windowAfter` |  `integer` Number of characters after the finding to consider.  
  
## LikelihoodAdjustment

Message for specifying an adjustment to the likelihood of a finding as part of a detection rule.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "fixedLikelihood": enum ([Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood)),
      "relativeLikelihood": integer
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
How the likelihood will be modified. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`fixedLikelihood` |  `enum (`[Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood)`)` Set the likelihood of a finding to a fixed value.  
`relativeLikelihood` |  `integer` Increase or decrease the likelihood by the specified number of levels. For example, if a finding would be `POSSIBLE` without the detection rule and `relativeLikelihood` is 1, then it is upgraded to `LIKELY`, while a value of -1 would downgrade it to `UNLIKELY`. Likelihood may never drop below `VERY_UNLIKELY` or exceed `VERY_LIKELY`, so applying an adjustment of 1 followed by an adjustment of -1 when base likelihood is `VERY_LIKELY` will result in a final likelihood of `LIKELY`.  
End of mutually exclusive fields.  
  
## ExclusionType

Type of exclusion rule.

Enums  
---  
`EXCLUSION_TYPE_UNSPECIFIED` | A finding of this custom info type will not be excluded from results.  
`EXCLUSION_TYPE_EXCLUDE` | A finding of this custom info type will be excluded from final results, but can still affect rule execution.  
  
## ContentOption

Deprecated and unused.

Enums  
---  
`CONTENT_UNSPECIFIED` | Includes entire content of a file or a data stream.  
`CONTENT_TEXT` | Text content within the data, excluding any metadata.  
`CONTENT_IMAGE` | Images found in the data.  
  
## InspectionRuleSet

Rule set for modifying a set of infoTypes to alter behavior under certain circumstances, depending on the specific details of the rules within the set.

JSON representation  
---  
      
    
    {
      "infoTypes": [
        {
          object ([InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType))
        }
      ],
      "rules": [
        {
          object ([InspectionRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#InspectionRule))
        }
      ]
    }  
  
Fields  
---  
`infoTypes[]` |  `object (`[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)`)` List of infoTypes this rule set is applied to.  
`rules[]` |  `object (`[InspectionRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#InspectionRule)`)` Set of rules to be applied to infoTypes. The rules are applied in order.  
  
## InspectionRule

A single inspection rule to be applied to infoTypes, specified in `InspectionRuleSet`.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "hotwordRule": {
        object ([HotwordRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#HotwordRule))
      },
      "exclusionRule": {
        object ([ExclusionRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#ExclusionRule))
      },
      "adjustmentRule": {
        object ([AdjustmentRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#AdjustmentRule))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Inspection rule types. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`hotwordRule` |  `object (`[HotwordRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#HotwordRule)`)` Hotword-based detection rule.  
`exclusionRule` |  `object (`[ExclusionRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#ExclusionRule)`)` Exclusion rule.  
`adjustmentRule` |  `object (`[AdjustmentRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#AdjustmentRule)`)` Adjustment rule.  
End of mutually exclusive fields.  
  
## ExclusionRule

The rule that specifies conditions when findings of infoTypes specified in `InspectionRuleSet` are removed from results.

JSON representation  
---  
      
    
    {
      "matchingType": enum ([MatchingType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#MatchingType)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "dictionary": {
        object ([Dictionary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Dictionary))
      },
      "regex": {
        object ([Regex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Regex))
      },
      "excludeInfoTypes": {
        object ([ExcludeInfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#ExcludeInfoTypes))
      },
      "excludeByHotword": {
        object ([ExcludeByHotword](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#ExcludeByHotword))
      },
      "excludeByImageFindings": {
        object ([ExcludeByImageFindings](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#ExcludeByImageFindings))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`matchingType` |  `enum (`[MatchingType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#MatchingType)`)` How the rule is applied, see MatchingType documentation for details.  
Exclusion rule types. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`dictionary` |  `object (`[Dictionary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Dictionary)`)` Dictionary which defines the rule.  
`regex` |  `object (`[Regex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Regex)`)` Regular expression which defines the rule.  
`excludeInfoTypes` |  `object (`[ExcludeInfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#ExcludeInfoTypes)`)` Set of infoTypes for which findings would affect this rule.  
`excludeByHotword` |  `object (`[ExcludeByHotword](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#ExcludeByHotword)`)` Drop if the hotword rule is contained in the proximate context. For tabular data, the context includes the column name.  
`excludeByImageFindings` |  `object (`[ExcludeByImageFindings](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#ExcludeByImageFindings)`)` Exclude findings based on image containment rules. For example, exclude an image finding if it overlaps with another image finding.  
End of mutually exclusive fields.  
  
## ExcludeInfoTypes

List of excluded infoTypes.

JSON representation  
---  
      
    
    {
      "infoTypes": [
        {
          object ([InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType))
        }
      ]
    }  
  
Fields  
---  
`infoTypes[]` |  `object (`[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)`)` InfoType list in ExclusionRule rule drops a finding when it overlaps or contained within with a finding of an infoType from this list. For example, for `InspectionRuleSet.info_types` containing "PHONE_NUMBER"`and `exclusionRule`containing`excludeInfoTypes.info_types` with "EMAIL_ADDRESS" the phone number findings are dropped if they overlap with EMAIL_ADDRESS finding. That leads to "555-222-2222@example.org" to generate only a single finding, namely email address.  
  
## ExcludeByHotword

The rule to exclude findings based on a hotword. For record inspection of tables, column names are considered hotwords. An example of this is to exclude a finding if it belongs to a BigQuery column that matches a specific pattern.

JSON representation  
---  
      
    
    {
      "hotwordRegex": {
        object ([Regex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Regex))
      },
      "proximity": {
        object ([Proximity](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Proximity))
      }
    }  
  
Fields  
---  
`hotwordRegex` |  `object (`[Regex](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Regex)`)` Regular expression pattern defining what qualifies as a hotword.  
`proximity` |  `object (`[Proximity](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Proximity)`)` Range of characters within which the entire hotword must reside. The total length of the window cannot exceed 1000 characters. The windowBefore property in proximity should be set to 1 if the hotword needs to be included in a column header.  
  
## ExcludeByImageFindings

The rule to exclude image findings based on spatial relationships with other image findings. For example, exclude an image finding if it overlaps with another image finding. This rule is silently ignored if the content being inspected is not an image.

JSON representation  
---  
      
    
    {
      "infoTypes": [
        {
          object ([InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType))
        }
      ],
      "imageContainmentType": {
        object ([ImageContainmentType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#ImageContainmentType))
      }
    }  
  
Fields  
---  
`infoTypes[]` |  `object (`[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)`)` A list of image-supported infoTypes—excluding [document infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#documents)—to be used as context for the exclusion rule. A finding is excluded if its bounding box has the specified spatial relationship (defined by `imageContainmentType`) with a finding of an infoType in this list.For example, if `InspectionRuleSet.info_types` includes `OBJECT_TYPE/PERSON` and this `exclusionRule` specifies `infoTypes` as `OBJECT_TYPE/PERSON/PASSPORT` with `imageContainmentType` set to `encloses`, then `OBJECT_TYPE/PERSON` findings will be excluded if they are fully contained within the bounding box of an `OBJECT_TYPE/PERSON/PASSPORT` finding.  
`imageContainmentType` |  `object (`[ImageContainmentType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#ImageContainmentType)`)` Specifies the required spatial relationship between the bounding boxes of the target finding and the context infoType findings.  
  
## ImageContainmentType

Specifies the relationship between bounding boxes for image findings.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "encloses": {
        object ([Encloses](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Encloses))
      },
      "fullyInside": {
        object ([FullyInside](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#FullyInside))
      },
      "overlaps": {
        object ([Overlap](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Overlap))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The type of relationship to check between the target finding and the context finding. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`encloses` |  `object (`[Encloses](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Encloses)`)` The context finding's bounding box must fully contain the target finding's bounding box.  
`fullyInside` |  `object (`[FullyInside](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#FullyInside)`)` The context finding's bounding box must be fully inside the target finding's bounding box.  
`overlaps` |  `object (`[Overlap](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Overlap)`)` The context finding's bounding box and the target finding's bounding box must have a non-zero intersection.  
End of mutually exclusive fields.  
  
## Encloses

This type has no fields.

Defines a condition where one bounding box encloses another.

## FullyInside

This type has no fields.

Defines a condition where one bounding box is fully inside another.

## Overlap

This type has no fields.

Defines a condition for overlapping bounding boxes.

## MatchingType

Type of the match which can be applied to different ways of matching, like Dictionary, regular expression and intersecting with findings of another infoType.

Enums  
---  
`MATCHING_TYPE_UNSPECIFIED` | Invalid.  
`MATCHING_TYPE_FULL_MATCH` | Full match.

  * Dictionary: join of Dictionary results matched the complete finding quote
  * Regex: all regex matches fill a finding quote from start to end
  * Exclude infoType: completely inside affecting infoTypes findings

  
`MATCHING_TYPE_PARTIAL_MATCH` | Partial match.

  * Dictionary: at least one of the tokens in the finding matches
  * Regex: substring of the finding matches
  * Exclude infoType: intersects with affecting infoTypes findings

  
`MATCHING_TYPE_INVERSE_MATCH` | Inverse match.

  * Dictionary: no tokens in the finding match the dictionary
  * Regex: finding doesn't match the regex
  * Exclude infoType: no intersection with affecting infoTypes findings

  
`MATCHING_TYPE_RULE_SPECIFIC` | Rule-specific match.The matching logic is based on the specific rule being used. This is required for rules where the matching behavior is not a simple string comparison (e.g., image containment). This matching type can only be used with the `ExcludeByImageFindings` rule.

  * Exclude by image findings: The matching logic is defined within `ExcludeByImageFindings` based on spatial relationships between bounding boxes.

  
  
## AdjustmentRule

Rule that specifies conditions when a certain infoType's finding details should be adjusted.

JSON representation  
---  
      
    
    {
      "likelihoodAdjustment": {
        object ([LikelihoodAdjustment](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#LikelihoodAdjustment))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "adjustByMatchingInfoTypes": {
        object ([AdjustByMatchingInfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#AdjustByMatchingInfoTypes))
      },
      "adjustByImageFindings": {
        object ([AdjustByImageFindings](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#AdjustByImageFindings))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`likelihoodAdjustment` |  `object (`[LikelihoodAdjustment](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#LikelihoodAdjustment)`)` Likelihood adjustment to apply to the infoType.  
Condition under which the adjustment rule is applied. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`adjustByMatchingInfoTypes` |  `object (`[AdjustByMatchingInfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#AdjustByMatchingInfoTypes)`)` Set of infoTypes for which findings would affect this rule.  
`adjustByImageFindings` |  `object (`[AdjustByImageFindings](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#AdjustByImageFindings)`)` AdjustmentRule condition for image findings.  
End of mutually exclusive fields.  
  
## AdjustByMatchingInfoTypes

AdjustmentRule condition for matching infoTypes.

JSON representation  
---  
      
    
    {
      "infoTypes": [
        {
          object ([InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType))
        }
      ],
      "minLikelihood": enum ([Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood)),
      "matchingType": enum ([MatchingType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#MatchingType))
    }  
  
Fields  
---  
`infoTypes[]` |  `object (`[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)`)` Sensitive Data Protection adjusts the likelihood of a finding if that finding also matches one of these infoTypes.For example, you can create a rule to adjust the likelihood of a `PHONE_NUMBER` finding if the string is found within a document that is classified as `DOCUMENT_TYPE/HR/RESUME`. To configure this, set `PHONE_NUMBER` in `InspectionRuleSet.info_types`. Add an `adjustmentRule` with an `adjustByMatchingInfoTypes.info_types` that contains `DOCUMENT_TYPE/HR/RESUME`. In this case, the likelihood of the `PHONE_NUMBER` finding is adjusted, but the likelihood of the `DOCUMENT_TYPE/HR/RESUME` finding is not.  
`minLikelihood` |  `enum (`[Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood)`)` Required. Minimum likelihood of the `adjustByMatchingInfoTypes.info_types` finding. If the likelihood is lower than this value, Sensitive Data Protection doesn't adjust the likelihood of the `InspectionRuleSet.info_types` finding.  
`matchingType` |  `enum (`[MatchingType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#MatchingType)`)` How the adjustment rule is applied.Only `MATCHING_TYPE_PARTIAL_MATCH` is supported:

  * Partial match: adjusts the findings of infoTypes specified in the inspection rule when they have a nonempty intersection with a finding of an infoType specified in this adjustment rule.

  
  
## AdjustByImageFindings

AdjustmentRule condition for image findings. This rule is silently ignored if the content being inspected is not an image.

JSON representation  
---  
      
    
    {
      "infoTypes": [
        {
          object ([InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType))
        }
      ],
      "minLikelihood": enum ([Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood)),
      "imageContainmentType": {
        object ([ImageContainmentType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#ImageContainmentType))
      }
    }  
  
Fields  
---  
`infoTypes[]` |  `object (`[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)`)` A list of image-supported infoTypes—excluding [document infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#documents)—to be used as context for the adjustment rule. Sensitive Data Protection adjusts the likelihood of an image finding if its bounding box has the specified spatial relationship (defined by `imageContainmentType`) with a finding of an infoType in this list.For example, you can create a rule to adjust the likelihood of a `US_PASSPORT` finding if it is enclosed by a finding of `OBJECT_TYPE/PERSON/PASSPORT`. To configure this, set `US_PASSPORT` in `InspectionRuleSet.info_types`. Add an `adjustmentRule` with an `adjustByImageFindings.info_types` that contains `OBJECT_TYPE/PERSON/PASSPORT` and `imageContainmentType` set to `encloses`. In this case, the likelihood of the `US_PASSPORT` finding is adjusted, but the likelihood of the `OBJECT_TYPE/PERSON/PASSPORT` finding is not.  
`minLikelihood` |  `enum (`[Likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood)`)` Required. Minimum likelihood of the `adjustByImageFindings.info_types` finding. If the likelihood is lower than this value, Sensitive Data Protection doesn't adjust the likelihood of the `InspectionRuleSet.info_types` finding.  
`imageContainmentType` |  `object (`[ImageContainmentType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#ImageContainmentType)`)` Specifies the required spatial relationship between the bounding boxes of the target finding and the context infoType findings.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
