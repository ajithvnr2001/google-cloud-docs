---
url: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt/
title: TransactionAttempt \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:06.548110+00:00
---

# TransactionAttempt  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  TransactionAttempt Stay organized with collections  Save and categorize content based on your preferences. 

The state of an attempted transaction submission.

JSON representation  
---  
      
    
    {
      "status": enum ([TransactionStatus](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionStatus)),
      "proofOfInclusion": {
        object ([ProofOfInclusion](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#ProofOfInclusion))
      },
      "statusEvents": [
        {
          object ([StatusEvent](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#StatusEvent))
        }
      ]
    }  
  
Fields  
---  
`status` |  `enum (`[TransactionStatus](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionStatus)`)` Output only. The current status of the transaction attempt.  
`proofOfInclusion` |  `object (`[ProofOfInclusion](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#ProofOfInclusion)`)` Output only. Certificate of the inclusion of the transaction effects in the world state. Only provided if status is `FINALIZED`.  
`statusEvents[]` |  `object (`[StatusEvent](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#StatusEvent)`)` Output only. The ordered status events recorded for the transaction attempt.  
  
## TransactionStatus

The status of the transaction attempt.

Enums  
---  
`TRANSACTION_STATUS_UNSPECIFIED` | Unknown or uninitialized state.  
`PENDING` | The transaction is known to this validator, but it is not finalized yet.  
`FINALIZED` | The transaction is finalized. Its effects have been persisted on the blockchain and cannot be reversed.  
  
## ProofOfInclusion

Certificate of the inclusion of the effects of a transaction in the world state.

JSON representation  
---  
      
    
    {
      "transactionCertificate": {
        object ([TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionCertificate))
      },
      "roundCertificate": {
        object ([RoundCertificate](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#RoundCertificate))
      },
      "pathToRoundRoot": [
        {
          object ([MerkleTreeNode](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#MerkleTreeNode))
        }
      ]
    }  
  
Fields  
---  
`transactionCertificate` |  `object (`[TransactionCertificate](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionCertificate)`)` Output only. Certificate of the inclusion of the transaction effects in a specific round.  
`roundCertificate` |  `object (`[RoundCertificate](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#RoundCertificate)`)` Output only. Certificate of the execution of the round.  
`pathToRoundRoot[]` |  `object (`[MerkleTreeNode](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#MerkleTreeNode)`)` Output only. Cryptographic proof of inclusion of the transaction effects in the execution round.It is given as a path from a given leaf (a transaction digest) to the root of the execution round. The path is represented as a list of (left child, right child) pairs, and the first pair is the left and right children of the given leaf's parent node. For example, assuming the Merkle tree was built with eight leaf digests `[t0, t1, t2, t3, t4, t5, t6, t7]`, having the following structure:
    
    
           _____root_digest____
          |                    |
       __ h20__             __h21__
      |        |           |       |
     h10     h11          h12     h13
     | |     | |          | |     | |
    t0 t1   t2 t3        t4 t5   t6 t7
    

In here, `pathToRoundRoot` for `t0` will contain: `[(t0, t1), (h10, h11), (h20, h21)]`.One can consecutively compute SHA-256 digests of each path node to verify that the digest of the path produces the same value as the `roundCertificate.merkle_tree.root_digest_hex`. Thus, verifying that the leaf was included in the round's Merkle tree.  
  
## TransactionCertificate

Certificate of the execution of a specific transaction in a round.

JSON representation  
---  
      
    
    {
      "transactionDigestHex": string,
      "roundId": string,
      "transactionEffects": {
        object ([TransactionEffects](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionEffects))
      },
      "events": [
        {
          object ([TransactionEvent](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionEvent))
        }
      ],
      "transactionEffectsStateChecksumHex": string,
      "certificationResultsDigestHex": string
    }  
  
Fields  
---  
`transactionDigestHex` |  `string` Output only. The ID of the transaction this certificate is for.  
`roundId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The ID of the execution round at which this transaction was executed in.  
`transactionEffects` |  `object (`[TransactionEffects](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionEffects)`)` Output only. The effects from the transaction execution.  
`events[]` |  `object (`[TransactionEvent](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionEvent)`)` Output only. Events produced by the transaction.  
`transactionEffectsStateChecksumHex` |  `string` Output only. Homomorphic checksum of the effects. A 2048 byte value encoded as a hexadecimal string.  
`certificationResultsDigestHex` |  `string` Output only. The cryptographic digest of all the previous fields in sequence. Used to build a Merkle tree for the proof of inclusion.  
  
## TransactionEffects

Effects of the execution of a transaction.

JSON representation  
---  
      
    
    {
      "status": {
        object ([TransactionStatus](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionStatus_1))
      },
      "effects": [
        {
          object ([TransactionEffect](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionEffect))
        }
      ]
    }  
  
Fields  
---  
`status` |  `object (`[TransactionStatus](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionStatus_1)`)` Output only. The resulting status of the transaction execution.  
`effects[]  
**(deprecated)**` |  `object (`[TransactionEffect](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#TransactionEffect)`)` This item is deprecated!Output only. Deprecated: Query the network state instead to determine any changes to the world state. The effects of the transaction in the world state.  
  
## TransactionStatus

Represents the status of a transaction execution.

JSON representation  
---  
      
    
    {
      "code": integer,
      "message": string
    }  
  
Fields  
---  
`code` |  `integer` Output only. The status code, a numeric value whose meaning is defined by the corresponding [gRPC status code](https://github.com/grpc/grpc/blob/master/doc/statuscodes.md).  
`message` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The error message, if any. Set only if code is not `OK`. This is a string encoded as utf-8 bytes. Stored as bytes to prevent any issues with the determinism of the encoding.A base64-encoded string.  
  
## TransactionEffect

Represents an update by some transaction to the world state.

If it has a `deltaVal`, it is assumed to be a delta (an integer offset) applied to the previously stored value on a given key. In that case, `newVal` and `oldVal` should be empty.

Otherwise, it is assumed to have at least one of `oldVal` or `newVal` (or both). An empty `oldVal` indicates the value was inserted. An empty `newVal` indicates the value was deleted.

JSON representation  
---  
      
    
    {
      "key": string,
      "oldVal": string,
      "newVal": string,
      "deltaVal": string
    }  
  
Fields  
---  
`key` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The key in the world state that was updated.A base64-encoded string.  
`oldVal` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The value of the key before the transaction was executed.A base64-encoded string.  
`newVal` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. The value of the key after the transaction was executed.A base64-encoded string.  
`deltaVal` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. An integer offset that was applied to the previously stored value.  
  
## TransactionEvent

An event produced by a transaction.

JSON representation  
---  
      
    
    {
      "type": string,
      "attributes": [
        {
          object ([EventAttribute](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#EventAttribute))
        }
      ]
    }  
  
Fields  
---  
`type` |  `string` Output only. The type of event. A special event of type `transaction_output` contains the outputs produced by the transaction—for example, the account ID of a newly created account.  
`attributes[]` |  `object (`[EventAttribute](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#EventAttribute)`)` Output only. The event attributes as arbitrary key-value pairs.  
  
## EventAttribute

An individual attribute as a key-value pair.

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string` Output only. The key of the attribute.  
`value` |  `string` Output only. The value of the attribute.  
  
## RoundCertificate

Certificate of the execution of a round by a specific validator.

JSON representation  
---  
      
    
    {
      "roundId": string,
      "validatorId": string,
      "roundStateChecksumHex": string,
      "roundDeltaChecksumHex": string,
      "merkleTree": {
        object ([MerkleTree](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#MerkleTree))
      },
      "validatorSignatures": [
        string
      ],
      "isFinalized": boolean
    }  
  
Fields  
---  
`roundId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The ID of the round for which the certificate is for.  
`validatorId` |  `string` Output only. The human readable validator identifier. This is used to look up the public key against which the `validatorSignatures` is verified.  
`roundStateChecksumHex` |  `string` Output only. The hex representation of the homomorphic digest over the world state after the effects of this round are applied.  
`roundDeltaChecksumHex` |  `string` Output only. The hex representation of the homomorphic digest over the aggregated transaction effects of this round.  
`merkleTree` |  `object (`[MerkleTree](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#MerkleTree)`)` Output only. Merkle tree having this round as root node and transaction batches (executed in the round) as the leaves.  
`validatorSignatures[]` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. The signature of the validator. This is signed over the digest of the preceding payload of this record.A base64-encoded string.  
`isFinalized` |  `boolean` Output only. Boolean to indicate if the round is finalized, i.e., whether a sufficient quorum of validators have certified this round with the same certificate.  
  
## MerkleTree

A Merkle tree with a cryptographic digest of the root node.

JSON representation  
---  
      
    
    {
      "rootHashHex": string,
      "rootDigestHex": string,
      "numTransactions": string
    }  
  
Fields  
---  
`rootHashHex  
**(deprecated)**` |  `string` This item is deprecated!Output only. The cryptographic digest of the root node. Deprecated: Use `[rootDigestHex](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#MerkleTree.FIELDS.root_digest_hex)` instead.  
`rootDigestHex` |  `string` Output only. The hexadecimal representation of the digest of the root node. Format: A 64-character hexadecimal string.  
`numTransactions` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The number of transactions in the tree.  
  
## MerkleTreeNode

Represents a node in a Merkle tree path.

JSON representation  
---  
      
    
    {
      "leftChildHashHex": string,
      "rightChildHashHex": string,
      "leftChildDigestHex": string,
      "rightChildDigestHex": string
    }  
  
Fields  
---  
`leftChildHashHex  
**(deprecated)**` |  `string` This item is deprecated!Output only. The hexadecimal representation of the digest of the left child of a node. Deprecated: Use `[leftChildDigestHex](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#MerkleTreeNode.FIELDS.left_child_digest_hex)` instead.  
`rightChildHashHex  
**(deprecated)**` |  `string` This item is deprecated!Output only. The hexadecimal representation of the digest of the right child of a node. Deprecated: Use `[rightChildDigestHex](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#MerkleTreeNode.FIELDS.right_child_digest_hex)` instead.  
`leftChildDigestHex` |  `string` Output only. The hexadecimal representation of the digest of the left child of a node. Format: A 64-character hexadecimal string.  
`rightChildDigestHex` |  `string` Output only. The hexadecimal representation of the digest of the right child of a node. Format: A 64-character hexadecimal string.  
  
## StatusEvent

Represents an event in the processing of a transaction as observed by a single validator.

All values reported are from the perspective of the validator handling the request and may differ from the view of other validators.

JSON representation  
---  
      
    
    {
      "eventTime": string,
      "eventType": enum ([EventType](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#EventType)),
      "eventDetails": {
        object ([EventDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#EventDetails))
      }
    }  
  
Fields  
---  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the event was recorded by this validator.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`eventType` |  `enum (`[EventType](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#EventType)`)` Output only. The type of the event.  
`eventDetails` |  `object (`[EventDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#EventDetails)`)` Output only. Additional details associated with the event.  
  
## EventType

Represents the type of an event in the processing of a transaction, as observed by the validator that the request was routed to.

Enums  
---  
`EVENT_TYPE_UNSPECIFIED` | Unknown or unspecified event.  
`EVENT_TYPE_RECEIVED` | The transaction was received by this validator directly from a client.  
`EVENT_TYPE_BROADCASTED` | The transaction was broadcasted by this to other validators.  
`EVENT_TYPE_ORDERED` | The transaction was ordered and scheduled for execution by this validator.  
`EVENT_TYPE_EXECUTION_STARTED` | The execution of the transaction has started.  
`EVENT_TYPE_EXECUTION_COMPLETED` | The execution of the transaction has completed.  
`EVENT_TYPE_FINALIZED` | The transaction has been finalized by this validator.  
  
## EventDetails

Represents additional details of a status event.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "executionDetails": {
        object ([ExecutionDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#ExecutionDetails))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The details of the event. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`executionDetails` |  `object (`[ExecutionDetails](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt#ExecutionDetails)`)` Output only. Additional details for an execution event.  
End of mutually exclusive fields.  
  
## ExecutionDetails

Additional details for an execution event.

JSON representation  
---  
      
    
    {
      "roundId": string
    }  
  
Fields  
---  
`roundId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The round ID at which the execution event occurred.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
