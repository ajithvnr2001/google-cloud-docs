---
url: https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate/
title: Method: projects.platforms.gke.policies.evaluate \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:14:00.645085+00:00
---

# Method: projects.platforms.gke.policies.evaluate  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Reference ](https://docs.cloud.google.com/binary-authorization/docs/api)



Send feedback 

#  Method: projects.platforms.gke.policies.evaluate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * Verdict
  * PodResult
    * JSON representation
  * PodVerdict
  * ImageResult
    * JSON representation
  * ImageVerdict
  * AllowlistResult
    * JSON representation
  * CheckSetResult
    * JSON representation
  * CheckResults
    * JSON representation
  * CheckResult
    * JSON representation
  * EvaluationResult
    * JSON representation
  * CheckVerdict



Evaluates a Kubernetes object versus a GKE `[platform policy](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.policies#PlatformPolicy)`. Returns `NOT_FOUND` if the policy doesn't exist, `INVALID_ARGUMENT` if the policy or request is malformed and `PERMISSION_DENIED` if the client does not have sufficient permissions.

### HTTP request

`POST https://binaryauthorization.googleapis.com/v1/{name=projects/*/platforms/gke/policies/*}:evaluate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the `[platform policy](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.policies#PlatformPolicy)` to evaluate in the format `projects/*/platforms/*/policies/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `binaryauthorization.platformPolicies.evaluatePolicy`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "resource": {
        object
      }
    }  
  
Fields  
---  
`resource` |  `object (`[Struct](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Struct)` format)` Required. JSON or YAML blob representing a Kubernetes resource.  
  
### Response body

Response message for `[PlatformPolicyEvaluationService.EvaluateGkePolicy](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#google.cloud.binaryauthorization.v1.PlatformPolicyEvaluationService.EvaluateGkePolicy)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "verdict": enum ([Verdict](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#Verdict)),
      "results": [
        {
          object ([PodResult](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#PodResult))
        }
      ]
    }  
  
Fields  
---  
`verdict` |  `enum (`[Verdict](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#Verdict)`)` The result of evaluating all Pods in the request.  
`results[]` |  `object (`[PodResult](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#PodResult)`)` Evaluation result for each Pod contained in the request.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## Verdict

Whether the Pods passed, failed, or couldn't be evaluated.

Enums  
---  
`VERDICT_UNSPECIFIED` | Not specified. This should never be used.  
`CONFORMANT` | All Pods in the request conform to the policy.  
`NON_CONFORMANT` | At least one Pod does not conform to the policy.  
`ERROR` | Encountered at least one error evaluating a Pod and all other Pods conform to the policy. Non-conformance has precedence over errors.  
  
## PodResult

Result of evaluating the whole GKE policy for one Pod.

JSON representation  
---  
      
    
    {
      "podName": string,
      "kubernetesNamespace": string,
      "kubernetesServiceAccount": string,
      "verdict": enum ([PodVerdict](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#PodVerdict)),
      "imageResults": [
        {
          object ([ImageResult](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#ImageResult))
        }
      ]
    }  
  
Fields  
---  
`podName` |  `string` The name of the Pod.  
`kubernetesNamespace` |  `string` The Kubernetes namespace of the Pod.  
`kubernetesServiceAccount` |  `string` The Kubernetes service account of the Pod.  
`verdict` |  `enum (`[PodVerdict](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#PodVerdict)`)` The result of evaluating this Pod.  
`imageResults[]` |  `object (`[ImageResult](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#ImageResult)`)` Per-image details.  
  
## PodVerdict

Whether the Pod passed, failed, or couldn't be evaluated.

Enums  
---  
`POD_VERDICT_UNSPECIFIED` | Not specified. This should never be used.  
`CONFORMANT` | All images conform to the policy.  
`NON_CONFORMANT` | At least one image does not conform to the policy.  
`ERROR` | Encountered at least one error evaluating an image and all other images with non-error verdicts conform to the policy. Non-conformance has precedence over errors.  
  
## ImageResult

Result of evaluating one image.

JSON representation  
---  
      
    
    {
      "imageUri": string,
      "verdict": enum ([ImageVerdict](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#ImageVerdict)),
      "explanation": string,
    
      // Union field result can be only one of the following:
      "allowlistResult": {
        object ([AllowlistResult](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#AllowlistResult))
      },
      "checkSetResult": {
        object ([CheckSetResult](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#CheckSetResult))
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`imageUri` |  `string` Image URI from the request.  
`verdict` |  `enum (`[ImageVerdict](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#ImageVerdict)`)` The result of evaluating this image.  
`explanation` |  `string` Explanation of this image result. Only populated if no check sets were evaluated.  
Union field `result`. How the image was evaluated. `result` can be only one of the following:  
`allowlistResult` |  `object (`[AllowlistResult](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#AllowlistResult)`)` If the image was exempted by a top-level `[allowPattern](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.policies#ImageAllowlist)`, contains the allowlist pattern that the image name matched.  
`checkSetResult` |  `object (`[CheckSetResult](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#CheckSetResult)`)` If a check set was evaluated, contains the result of the check set. Empty if there were no check sets.  
  
## ImageVerdict

Whether the image passed, failed, or couldn't be evaluated.

Enums  
---  
`IMAGE_VERDICT_UNSPECIFIED` | Not specified. This should never be used.  
`CONFORMANT` | Image conforms to the policy.  
`NON_CONFORMANT` | Image does not conform to the policy.  
`ERROR` | Error evaluating the image. Non-conformance has precedence over errors.  
  
## AllowlistResult

Result of evaluating an image name allowlist.

JSON representation  
---  
      
    
    {
      "matchedPattern": string
    }  
  
Fields  
---  
`matchedPattern` |  `string` The allowlist pattern that the image matched.  
  
## CheckSetResult

Result of evaluating one check set.

JSON representation  
---  
      
    
    {
      "index": string,
      "displayName": string,
      "scope": {
        object ([Scope](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.policies#Scope))
      },
      "explanation": string,
    
      // Union field result can be only one of the following:
      "allowlistResult": {
        object ([AllowlistResult](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#AllowlistResult))
      },
      "checkResults": {
        object ([CheckResults](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#CheckResults))
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`index` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The index of the check set.  
`displayName` |  `string` The name of the check set.  
`scope` |  `object (`[Scope](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.policies#Scope)`)` The scope of the check set.  
`explanation` |  `string` Explanation of this check set result. Only populated if no checks were evaluated.  
Union field `result`. How the check set was evaluated. `result` can be only one of the following:  
`allowlistResult` |  `object (`[AllowlistResult](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#AllowlistResult)`)` If the image was exempted by an `[allowPattern](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.policies#ImageAllowlist)` in the check set, contains the pattern that the image name matched.  
`checkResults` |  `object (`[CheckResults](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#CheckResults)`)` If checks were evaluated, contains the results of evaluating each check.  
  
## CheckResults

Result of evaluating one or more checks.

JSON representation  
---  
      
    
    {
      "results": [
        {
          object ([CheckResult](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#CheckResult))
        }
      ]
    }  
  
Fields  
---  
`results[]` |  `object (`[CheckResult](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#CheckResult)`)` Per-check details.  
  
## CheckResult

Result of evaluating one check.

JSON representation  
---  
      
    
    {
      "index": string,
      "displayName": string,
      "type": string,
      "explanation": string,
    
      // Union field result can be only one of the following:
      "allowlistResult": {
        object ([AllowlistResult](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#AllowlistResult))
      },
      "evaluationResult": {
        object ([EvaluationResult](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#EvaluationResult))
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`index` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The index of the check.  
`displayName` |  `string` The name of the check.  
`type` |  `string` The type of the check.  
`explanation` |  `string` Explanation of this check result.  
Union field `result`. How the check was evaluated. `result` can be only one of the following:  
`allowlistResult` |  `object (`[AllowlistResult](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#AllowlistResult)`)` If the image was exempted by an `[allowPattern](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.policies#ImageAllowlist)` in the check, contains the pattern that the image name matched.  
`evaluationResult` |  `object (`[EvaluationResult](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#EvaluationResult)`)` If a check was evaluated, contains the result of the check.  
  
## EvaluationResult

Result of evaluating one check.

JSON representation  
---  
      
    
    {
      "verdict": enum ([CheckVerdict](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#CheckVerdict))
    }  
  
Fields  
---  
`verdict` |  `enum (`[CheckVerdict](https://docs.cloud.google.com/binary-authorization/docs/reference/rest/v1/projects.platforms.gke.policies/evaluate#CheckVerdict)`)` The result of evaluating this check.  
  
## CheckVerdict

Whether the check passed, failed, or couldn't be evaluated.

Enums  
---  
`CHECK_VERDICT_UNSPECIFIED` | Not specified. This should never be used.  
`CONFORMANT` | The check was successfully evaluated and the image satisfied the check.  
`NON_CONFORMANT` | The check was successfully evaluated and the image did not satisfy the check.  
`ERROR` | The check was not successfully evaluated.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
