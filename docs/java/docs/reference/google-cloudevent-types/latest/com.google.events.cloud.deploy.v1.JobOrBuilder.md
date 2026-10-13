---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.JobOrBuilder
title: Interface JobOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:06.678985+00:00
---

# Interface JobOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.JobOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface JobOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.JobOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.deploy.v1.JobOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.deploy.v1.JobOrBuilder)


    
    
    public interface JobOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAdvanceChildRolloutJob()
    
    
    public abstract AdvanceChildRolloutJob getAdvanceChildRolloutJob()

Output only. An advanceChildRollout Job.

`.google.events.cloud.deploy.v1.AdvanceChildRolloutJob advance_child_rollout_job = 7; `

**Returns**  
---  
**Type** | **Description**  
`[AdvanceChildRolloutJob](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.AdvanceChildRolloutJob)` | The advanceChildRolloutJob.  
  
### getAdvanceChildRolloutJobOrBuilder()
    
    
    public abstract AdvanceChildRolloutJobOrBuilder getAdvanceChildRolloutJobOrBuilder()

Output only. An advanceChildRollout Job.

`.google.events.cloud.deploy.v1.AdvanceChildRolloutJob advance_child_rollout_job = 7; `

**Returns**  
---  
**Type** | **Description**  
`[AdvanceChildRolloutJobOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.AdvanceChildRolloutJobOrBuilder)` |   
  
### getCreateChildRolloutJob()
    
    
    public abstract CreateChildRolloutJob getCreateChildRolloutJob()

Output only. A createChildRollout Job.

`.google.events.cloud.deploy.v1.CreateChildRolloutJob create_child_rollout_job = 6;`

**Returns**  
---  
**Type** | **Description**  
`[CreateChildRolloutJob](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.CreateChildRolloutJob)` | The createChildRolloutJob.  
  
### getCreateChildRolloutJobOrBuilder()
    
    
    public abstract CreateChildRolloutJobOrBuilder getCreateChildRolloutJobOrBuilder()

Output only. A createChildRollout Job.

`.google.events.cloud.deploy.v1.CreateChildRolloutJob create_child_rollout_job = 6;`

**Returns**  
---  
**Type** | **Description**  
`[CreateChildRolloutJobOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.CreateChildRolloutJobOrBuilder)` |   
  
### getDeployJob()
    
    
    public abstract DeployJob getDeployJob()

Output only. A deploy Job.

`.google.events.cloud.deploy.v1.DeployJob deploy_job = 4;`

**Returns**  
---  
**Type** | **Description**  
`[DeployJob](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.DeployJob)` | The deployJob.  
  
### getDeployJobOrBuilder()
    
    
    public abstract DeployJobOrBuilder getDeployJobOrBuilder()

Output only. A deploy Job.

`.google.events.cloud.deploy.v1.DeployJob deploy_job = 4;`

**Returns**  
---  
**Type** | **Description**  
`[DeployJobOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.DeployJobOrBuilder)` |   
  
### getId()
    
    
    public abstract String getId()

Output only. The ID of the Job.

`string id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public abstract ByteString getIdBytes()

Output only. The ID of the Job.

`string id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
### getJobRun()
    
    
    public abstract String getJobRun()

Output only. The name of the `JobRun` responsible for the most recent invocation of this Job.

`string job_run = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The jobRun.  
  
### getJobRunBytes()
    
    
    public abstract ByteString getJobRunBytes()

Output only. The name of the `JobRun` responsible for the most recent invocation of this Job.

`string job_run = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for jobRun.  
  
### getJobTypeCase()
    
    
    public abstract Job.JobTypeCase getJobTypeCase()

**Returns**  
---  
**Type** | **Description**  
`[Job.JobTypeCase](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.Job.JobTypeCase)` |   
  
### getPostdeployJob()
    
    
    public abstract PostdeployJob getPostdeployJob()

Output only. A postdeploy Job.

`.google.events.cloud.deploy.v1.PostdeployJob postdeploy_job = 10;`

**Returns**  
---  
**Type** | **Description**  
`[PostdeployJob](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.PostdeployJob)` | The postdeployJob.  
  
### getPostdeployJobOrBuilder()
    
    
    public abstract PostdeployJobOrBuilder getPostdeployJobOrBuilder()

Output only. A postdeploy Job.

`.google.events.cloud.deploy.v1.PostdeployJob postdeploy_job = 10;`

**Returns**  
---  
**Type** | **Description**  
`[PostdeployJobOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.PostdeployJobOrBuilder)` |   
  
### getPredeployJob()
    
    
    public abstract PredeployJob getPredeployJob()

Output only. A predeploy Job.

`.google.events.cloud.deploy.v1.PredeployJob predeploy_job = 9;`

**Returns**  
---  
**Type** | **Description**  
`[PredeployJob](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.PredeployJob)` | The predeployJob.  
  
### getPredeployJobOrBuilder()
    
    
    public abstract PredeployJobOrBuilder getPredeployJobOrBuilder()

Output only. A predeploy Job.

`.google.events.cloud.deploy.v1.PredeployJob predeploy_job = 9;`

**Returns**  
---  
**Type** | **Description**  
`[PredeployJobOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.PredeployJobOrBuilder)` |   
  
### getSkipMessage()
    
    
    public abstract String getSkipMessage()

Output only. Additional information on why the Job was skipped, if available.

`string skip_message = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The skipMessage.  
  
### getSkipMessageBytes()
    
    
    public abstract ByteString getSkipMessageBytes()

Output only. Additional information on why the Job was skipped, if available.

`string skip_message = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for skipMessage.  
  
### getState()
    
    
    public abstract Job.State getState()

Output only. The current state of the Job.

`.google.events.cloud.deploy.v1.Job.State state = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Job.State](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.Job.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. The current state of the Job.

`.google.events.cloud.deploy.v1.Job.State state = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getVerifyJob()
    
    
    public abstract VerifyJob getVerifyJob()

Output only. A verify Job.

`.google.events.cloud.deploy.v1.VerifyJob verify_job = 5;`

**Returns**  
---  
**Type** | **Description**  
`[VerifyJob](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.VerifyJob)` | The verifyJob.  
  
### getVerifyJobOrBuilder()
    
    
    public abstract VerifyJobOrBuilder getVerifyJobOrBuilder()

Output only. A verify Job.

`.google.events.cloud.deploy.v1.VerifyJob verify_job = 5;`

**Returns**  
---  
**Type** | **Description**  
`[VerifyJobOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.deploy.v1.VerifyJobOrBuilder)` |   
  
### hasAdvanceChildRolloutJob()
    
    
    public abstract boolean hasAdvanceChildRolloutJob()

Output only. An advanceChildRollout Job.

`.google.events.cloud.deploy.v1.AdvanceChildRolloutJob advance_child_rollout_job = 7; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the advanceChildRolloutJob field is set.  
  
### hasCreateChildRolloutJob()
    
    
    public abstract boolean hasCreateChildRolloutJob()

Output only. A createChildRollout Job.

`.google.events.cloud.deploy.v1.CreateChildRolloutJob create_child_rollout_job = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createChildRolloutJob field is set.  
  
### hasDeployJob()
    
    
    public abstract boolean hasDeployJob()

Output only. A deploy Job.

`.google.events.cloud.deploy.v1.DeployJob deploy_job = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the deployJob field is set.  
  
### hasPostdeployJob()
    
    
    public abstract boolean hasPostdeployJob()

Output only. A postdeploy Job.

`.google.events.cloud.deploy.v1.PostdeployJob postdeploy_job = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the postdeployJob field is set.  
  
### hasPredeployJob()
    
    
    public abstract boolean hasPredeployJob()

Output only. A predeploy Job.

`.google.events.cloud.deploy.v1.PredeployJob predeploy_job = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the predeployJob field is set.  
  
### hasVerifyJob()
    
    
    public abstract boolean hasVerifyJob()

Output only. A verify Job.

`.google.events.cloud.deploy.v1.VerifyJob verify_job = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the verifyJob field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
