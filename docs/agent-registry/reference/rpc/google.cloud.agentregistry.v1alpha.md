---
url: https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha
title: Package google.cloud.agentregistry.v1alpha \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:47.205876+00:00
---

# Package google.cloud.agentregistry.v1alpha  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  Package google.cloud.agentregistry.v1alpha Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[AgentRegistry](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.AgentRegistry)` (interface)
  * `[Agent](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Agent)` (message)
  * `[Agent.Card](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Agent.Card)` (message)
  * `[Agent.Card.Type](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Agent.Card.Type)` (enum)
  * `[Agent.Protocol](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Agent.Protocol)` (message)
  * `[Agent.Protocol.Type](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Agent.Protocol.Type)` (enum)
  * `[Agent.Skill](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Agent.Skill)` (message)
  * `[ArchiveUploadSource](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ArchiveUploadSource)` (message)
  * `[Binding](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Binding)` (message)
  * `[Binding.AuthProviderBinding](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Binding.AuthProviderBinding)` (message)
  * `[Binding.Source](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Binding.Source)` (message)
  * `[Binding.Target](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Binding.Target)` (message)
  * `[CreateBindingRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.CreateBindingRequest)` (message)
  * `[CreateServiceRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.CreateServiceRequest)` (message)
  * `[CreateSkillRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.CreateSkillRequest)` (message)
  * `[CreateSkillRevisionRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.CreateSkillRevisionRequest)` (message)
  * `[DeleteBindingRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.DeleteBindingRequest)` (message)
  * `[DeleteServiceRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.DeleteServiceRequest)` (message)
  * `[DeleteSkillRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.DeleteSkillRequest)` (message)
  * `[DeleteSkillRevisionRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.DeleteSkillRevisionRequest)` (message)
  * `[Endpoint](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Endpoint)` (message)
  * `[FetchAvailableBindingsRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.FetchAvailableBindingsRequest)` (message)
  * `[FetchAvailableBindingsResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.FetchAvailableBindingsResponse)` (message)
  * `[Frontmatter](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Frontmatter)` (message)
  * `[GcsSource](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.GcsSource)` (message)
  * `[GetAgentRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.GetAgentRequest)` (message)
  * `[GetBindingRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.GetBindingRequest)` (message)
  * `[GetEndpointRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.GetEndpointRequest)` (message)
  * `[GetMcpServerRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.GetMcpServerRequest)` (message)
  * `[GetPublisherRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.GetPublisherRequest)` (message)
  * `[GetServiceRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.GetServiceRequest)` (message)
  * `[Interface](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Interface)` (message)
  * `[Interface.ProtocolBinding](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Interface.ProtocolBinding)` (enum)
  * `[ListAgentsRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListAgentsRequest)` (message)
  * `[ListAgentsResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListAgentsResponse)` (message)
  * `[ListBindingsRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListBindingsRequest)` (message)
  * `[ListBindingsResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListBindingsResponse)` (message)
  * `[ListEndpointsRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListEndpointsRequest)` (message)
  * `[ListEndpointsResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListEndpointsResponse)` (message)
  * `[ListMcpServersRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListMcpServersRequest)` (message)
  * `[ListMcpServersResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListMcpServersResponse)` (message)
  * `[ListPublishersRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListPublishersRequest)` (message)
  * `[ListPublishersResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListPublishersResponse)` (message)
  * `[ListServicesRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListServicesRequest)` (message)
  * `[ListServicesResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListServicesResponse)` (message)
  * `[ListSkillRevisionsRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListSkillRevisionsRequest)` (message)
  * `[ListSkillRevisionsResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListSkillRevisionsResponse)` (message)
  * `[ListSkillsRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListSkillsRequest)` (message)
  * `[ListSkillsResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListSkillsResponse)` (message)
  * `[McpServer](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.McpServer)` (message)
  * `[McpServer.Tool](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.McpServer.Tool)` (message)
  * `[McpServer.Tool.Annotations](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.McpServer.Tool.Annotations)` (message)
  * `[OperationMetadata](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.OperationMetadata)` (message)
  * `[Publisher](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Publisher)` (message)
  * `[Publisher.PublisherTier](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Publisher.PublisherTier)` (enum)
  * `[SearchAgentsRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.SearchAgentsRequest)` (message)
  * `[SearchAgentsResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.SearchAgentsResponse)` (message)
  * `[SearchMcpServersRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.SearchMcpServersRequest)` (message)
  * `[SearchMcpServersResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.SearchMcpServersResponse)` (message)
  * `[SearchSkillsRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.SearchSkillsRequest)` (message)
  * `[SearchSkillsResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.SearchSkillsResponse)` (message)
  * `[SearchType](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.SearchType)` (enum)
  * `[Service](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Service)` (message)
  * `[Service.AgentSpec](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Service.AgentSpec)` (message)
  * `[Service.AgentSpec.Type](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Service.AgentSpec.Type)` (enum)
  * `[Service.EndpointSpec](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Service.EndpointSpec)` (message)
  * `[Service.EndpointSpec.Type](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Service.EndpointSpec.Type)` (enum)
  * `[Service.McpServerSpec](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Service.McpServerSpec)` (message)
  * `[Service.McpServerSpec.Type](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Service.McpServerSpec.Type)` (enum)
  * `[Skill.State](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Skill.State)` (enum)
  * `[Skill.TargetState](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Skill.TargetState)` (enum)
  * `[Skill.Type](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Skill.Type)` (enum)
  * `[SkillRevision.State](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.SkillRevision.State)` (enum)
  * `[UpdateBindingRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.UpdateBindingRequest)` (message)
  * `[UpdateServiceRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.UpdateServiceRequest)` (message)
  * `[UpdateSkillRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.UpdateSkillRequest)` (message)



## AgentRegistry

CreateBinding  
---  
` rpc CreateBinding(`[CreateBindingRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.CreateBindingRequest)`) returns (`[Operation](https://docs.cloud.google.com/agent-registry/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new Binding in a given project and location.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.bindings.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateService  
---  
` rpc CreateService(`[CreateServiceRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.CreateServiceRequest)`) returns (`[Operation](https://docs.cloud.google.com/agent-registry/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new Service in a given project and location.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.services.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateSkill  
---  
` rpc CreateSkill(`[CreateSkillRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.CreateSkillRequest)`) returns (`[Operation](https://docs.cloud.google.com/agent-registry/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` =========================================================================Creates a Skill resource container, optionally publishing the initial SkillRevision inline in a single, atomic CRUD roundtrip.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.skills.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateSkillRevision  
---  
` rpc CreateSkillRevision(`[CreateSkillRevisionRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.CreateSkillRevisionRequest)`) returns (`[Operation](https://docs.cloud.google.com/agent-registry/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new immutable revision and triggers validation pipelines.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.skillRevisions.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteBinding  
---  
` rpc DeleteBinding(`[DeleteBindingRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.DeleteBindingRequest)`) returns (`[Operation](https://docs.cloud.google.com/agent-registry/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a single Binding.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `agentregistry.bindings.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteService  
---  
` rpc DeleteService(`[DeleteServiceRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.DeleteServiceRequest)`) returns (`[Operation](https://docs.cloud.google.com/agent-registry/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a single Service.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `agentregistry.services.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteSkill  
---  
` rpc DeleteSkill(`[DeleteSkillRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.DeleteSkillRequest)`) returns (`[Operation](https://docs.cloud.google.com/agent-registry/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a Skill container along with all its revisions.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `agentregistry.skills.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteSkillRevision  
---  
` rpc DeleteSkillRevision(`[DeleteSkillRevisionRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.DeleteSkillRevisionRequest)`) returns (`[Operation](https://docs.cloud.google.com/agent-registry/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a specific revision (restricted to admins to purge accidentally committed secrets).

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `agentregistry.skillRevisions.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
FetchAvailableBindings  
---  
` rpc FetchAvailableBindings(`[FetchAvailableBindingsRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.FetchAvailableBindingsRequest)`) returns (`[FetchAvailableBindingsResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.FetchAvailableBindingsResponse)`) ` Fetches available Bindings.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.bindings.fetchAvailable`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetAgent  
---  
` rpc GetAgent(`[GetAgentRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.GetAgentRequest)`) returns (`[Agent](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Agent)`) ` Gets details of a single Agent.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `agentregistry.agents.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetBinding  
---  
` rpc GetBinding(`[GetBindingRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.GetBindingRequest)`) returns (`[Binding](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Binding)`) ` Gets details of a single Binding.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `agentregistry.bindings.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetEndpoint  
---  
` rpc GetEndpoint(`[GetEndpointRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.GetEndpointRequest)`) returns (`[Endpoint](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Endpoint)`) ` Gets details of a single Endpoint.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `agentregistry.endpoints.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetMcpServer  
---  
` rpc GetMcpServer(`[GetMcpServerRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.GetMcpServerRequest)`) returns (`[McpServer](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.McpServer)`) ` Gets details of a single McpServer.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `agentregistry.mcpServers.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetPublisher  
---  
` rpc GetPublisher(`[GetPublisherRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.GetPublisherRequest)`) returns (`[Publisher](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Publisher)`) ` Fetches details of a specific Publisher.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `agentregistry.publishers.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetService  
---  
` rpc GetService(`[GetServiceRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.GetServiceRequest)`) returns (`[Service](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Service)`) ` Gets details of a single Service.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `agentregistry.services.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListAgents  
---  
` rpc ListAgents(`[ListAgentsRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListAgentsRequest)`) returns (`[ListAgentsResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListAgentsResponse)`) ` Lists Agents in a given project and location.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.agents.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListBindings  
---  
` rpc ListBindings(`[ListBindingsRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListBindingsRequest)`) returns (`[ListBindingsResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListBindingsResponse)`) ` Lists Bindings in a given project and location.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.bindings.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListEndpoints  
---  
` rpc ListEndpoints(`[ListEndpointsRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListEndpointsRequest)`) returns (`[ListEndpointsResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListEndpointsResponse)`) ` Lists Endpoints in a given project and location.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.endpoints.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListMcpServers  
---  
` rpc ListMcpServers(`[ListMcpServersRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListMcpServersRequest)`) returns (`[ListMcpServersResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListMcpServersResponse)`) ` Lists McpServers in a given project and location.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.mcpServers.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListPublishers  
---  
` rpc ListPublishers(`[ListPublishersRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListPublishersRequest)`) returns (`[ListPublishersResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListPublishersResponse)`) ` Lists all Publishers in a location.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.publishers.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListServices  
---  
` rpc ListServices(`[ListServicesRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListServicesRequest)`) returns (`[ListServicesResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListServicesResponse)`) ` Lists Services in a given project and location.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.services.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListSkillRevisions  
---  
` rpc ListSkillRevisions(`[ListSkillRevisionsRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListSkillRevisionsRequest)`) returns (`[ListSkillRevisionsResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListSkillRevisionsResponse)`) ` Lists all revisions belonging to a parent Skill.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.skillRevisions.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListSkills  
---  
` rpc ListSkills(`[ListSkillsRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListSkillsRequest)`) returns (`[ListSkillsResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.ListSkillsResponse)`) ` Lists logical Skills available in a project.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.skills.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
SearchAgents  
---  
` rpc SearchAgents(`[SearchAgentsRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.SearchAgentsRequest)`) returns (`[SearchAgentsResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.SearchAgentsResponse)`) ` Searches Agents in a given project and location.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.agents.search`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
SearchMcpServers  
---  
` rpc SearchMcpServers(`[SearchMcpServersRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.SearchMcpServersRequest)`) returns (`[SearchMcpServersResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.SearchMcpServersResponse)`) ` Searches McpServers in a given project and location.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.mcpServers.search`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
SearchSkills  
---  
` rpc SearchSkills(`[SearchSkillsRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.SearchSkillsRequest)`) returns (`[SearchSkillsResponse](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.SearchSkillsResponse)`) ` Custom deep-search method to filter by frontmatter or query SKILL.md text blobs.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.skills.search`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateBinding  
---  
` rpc UpdateBinding(`[UpdateBindingRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.UpdateBindingRequest)`) returns (`[Operation](https://docs.cloud.google.com/agent-registry/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates the parameters of a single Binding.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `agentregistry.bindings.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateService  
---  
` rpc UpdateService(`[UpdateServiceRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.UpdateServiceRequest)`) returns (`[Operation](https://docs.cloud.google.com/agent-registry/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates the parameters of a single Service.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `agentregistry.services.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateSkill  
---  
` rpc UpdateSkill(`[UpdateSkillRequest](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.UpdateSkillRequest)`) returns (`[Operation](https://docs.cloud.google.com/agent-registry/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates Skill metadata or overrides active pointers/state using REST standard PATCH.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `agentregistry.skills.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
  
## Agent

Represents an Agent. "A2A" below refers to the Agent-to-Agent protocol.

Fields  
---  
`name` |  `string` Identifier. The resource name of an Agent. Format: `projects/{project}/locations/{location}/agents/{agent}`.  
`agent_id` |  `string` Output only. A stable, globally unique identifier for agents.  
`location` |  `string` Output only. The location where agent is hosted. The value is defined by the hosting environment (i.e. cloud provider).  
`display_name` |  `string` Output only. The display name of the agent, often obtained from the A2A Agent Card.  
`description` |  `string` Output only. The description of the Agent, often obtained from the A2A Agent Card. Empty if Agent Card has no description.  
`version` |  `string` Output only. The version of the Agent, often obtained from the A2A Agent Card. Empty if Agent Card has no version or agent is not an A2A Agent.  
`protocols[]` |  `[Protocol](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Agent.Protocol)` Output only. The connection details for the Agent.  
`skills[]` |  `[Skill](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Agent.Skill)` Output only. Skills the agent possesses, often obtained from the A2A Agent Card.  
`uid` |  `string` Output only. A universally unique identifier for the Agent.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Create time.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Update time.  
`attributes` |  `map<string, `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)`>` Output only. Attributes of the Agent. Valid values:

  * `agentregistry.googleapis.com/system/Framework`: {"framework": "google-adk"} - the agent framework used to develop the Agent. Example values: "google-adk", "langchain", "custom".
  * `agentregistry.googleapis.com/system/RuntimeIdentity`: {"principal": "principal://..."} - the runtime identity associated with the Agent.
  * `agentregistry.googleapis.com/system/RuntimeReference`: {"uri": "//..."}
  * the URI of the underlying resource hosting the Agent, for example, the Reasoning Engine URI.

  
`card` |  `[Card](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Agent.Card)` Output only. Full Agent Card payload, when available.  
  
## Card

Full Agent Card payload, often obtained from the A2A Agent Card.

Fields  
---  
`type` |  `[Type](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Agent.Card.Type)` Output only. The type of agent card.  
`content` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Output only. The content of the agent card.  
  
## Type

Represents the type of the agent card.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`A2A_AGENT_CARD` | Indicates that the card is an A2A Agent Card.  
  
## Protocol

Represents the protocol of an Agent.

Fields  
---  
`type` |  `[Type](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Agent.Protocol.Type)` Output only. The type of the protocol.  
`protocol_version` |  `string` Output only. The version of the protocol, for example, the A2A Agent Card version.  
`interfaces[]` |  `[Interface](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Interface)` Output only. The connection details for the Agent.  
  
## Type

The type of the protocol.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`A2A_AGENT` | The interfaces point to an A2A Agent following the A2A specification.  
`CUSTOM` | Agent does not follow any standard protocol.  
  
## Skill

Represents the skills of an Agent.

Fields  
---  
`id` |  `string` Output only. A unique identifier for the agent's skill.  
`name` |  `string` Output only. A human-readable name for the agent's skill.  
`description` |  `string` Output only. A more detailed description of the skill.  
`tags[]` |  `string` Output only. Keywords describing the skill.  
`examples[]` |  `string` Output only. Example prompts or scenarios this skill can handle.  
  
## ArchiveUploadSource

Direct write-only raw archive payload upload.

Fields  
---  
`archive_content` |  `bytes` Required. Input only. Write-only raw ZIP/TAR archive payload bytes containing the skill package.  
  
## Binding

Represents a user-defined Binding.

Fields  
---  
`name` |  `string` Required. Identifier. The resource name of the Binding. Format: `projects/{project}/locations/{location}/bindings/{binding}`.  
`display_name` |  `string` Optional. User-defined display name for the Binding. Can have a maximum length of `63` characters.  
`description` |  `string` Optional. User-defined description of a Binding. Can have a maximum length of `2048` characters.  
`source` |  `[Source](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Binding.Source)` Optional. The source Agent of the Binding.  
`target` |  `[Target](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Binding.Target)` Required. The target Agent Registry Resource of the Binding.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when this binding was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when this binding was last updated.  
Union field `binding`. The configuration for the Binding. `binding` can be only one of the following:  
`auth_provider_binding` |  `[AuthProviderBinding](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Binding.AuthProviderBinding)` The binding for AuthProvider.  
  
## AuthProviderBinding

The AuthProvider of the Binding.

Fields  
---  
`auth_provider` |  `string` Required. The resource name of the target AuthProvider. Format:

  * `projects/{project}/locations/{location}/authProviders/{auth_provider}`

  
`scopes[]` |  `string` Optional. The list of OAuth2 scopes of the AuthProvider.  
`continue_uri` |  `string` Optional. The continue URI of the AuthProvider. The URI is used to reauthenticate the user and finalize the managed OAuth flow.  
  
## Source

The source of the Binding.

Fields  
---  
Union field `source_type`. The type of the source, currently only supports Agents. Potential future fields include 'tag', etc. `source_type` can be only one of the following:  
`identifier` |  `string` The identifier of the source Agent. Format:

  * `urn:agent:{publisher}:{namespace}:{name}`

  
  
## Target

The target of the Binding.

Fields  
---  
Union field `target_type`. The type of the target, currently only supports an AgentRegistry Resource. Potential future fields include 'tag', etc. `target_type` can be only one of the following:  
`identifier` |  `string` The identifier of the target Agent, MCP Server, or Endpoint. Format:

  * `urn:agent:{publisher}:{namespace}:{name}`
  * `urn:mcp:{publisher}:{namespace}:{name}`
  * `urn:endpoint:{publisher}:{namespace}:{name}`

  
  
## CreateBindingRequest

Message for creating a Binding

Fields  
---  
`parent` |  `string` Required. The project and location to create the Binding in. Expected format: `projects/{project}/locations/{location}`.  
`binding_id` |  `string` Required. The ID to use for the binding, which will become the final component of the binding's resource name.This value should be 4-63 characters, and must conform to RFC-1034. Specifically, it must match the regular expression `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.  
`binding` |  `[Binding](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Binding)` Required. The Binding resource that is being created.  
`request_id` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
## CreateServiceRequest

Message for creating a Service

Fields  
---  
`parent` |  `string` Required. The project and location to create the Service in. Expected format: `projects/{project}/locations/{location}`.  
`service_id` |  `string` Required. The ID to use for the service, which will become the final component of the service's resource name.This value should be 4-63 characters, and valid characters are `/[a-z][0-9]-/`.  
`service` |  `[Service](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Service)` Required. The Service resource that is being created. Format: `projects/{project}/locations/{location}/services/{service}`.  
`request_id` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
## CreateSkillRequest

=========================================================================

#### Skills Messages

Message requesting creation of a logical Skill container.

Fields  
---  
`parent` |  `string` Required. The project and location location to bootstrap.  
`skill_id` |  `string` Required. Custom, user-defined unique container identifier. Must be unique within the parent project and location. This value should be 4-64 characters, and valid characters are `/[a-z][0-9]-/`.  
`skill` |  `Skill` Required. Skill container body config.  
`request_id` |  `string` Optional. Signed UUID request idempotency token.  
  
## CreateSkillRevisionRequest

Requesting creation of a new SkillRevision snapshot.

Fields  
---  
`parent` |  `string` Required. Parent logical container name.  
`skill_revision` |  `SkillRevision` Required. Immutable SkillRevision snapshot definition schema.  
`skill_revision_id` |  `string` Optional. Custom, user-defined unique revision identifier. Format: 4-63 characters, matching regex `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`  
`request_id` |  `string` Optional. Signed UUID request idempotency token.  
  
## DeleteBindingRequest

Message for deleting a Binding

Fields  
---  
`name` |  `string` Required. The name of the Binding. Format: `projects/{project}/locations/{location}/bindings/{binding}`.  
`request_id` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
## DeleteServiceRequest

Message for deleting a Service

Fields  
---  
`name` |  `string` Required. The name of the Service. Format: `projects/{project}/locations/{location}/services/{service}`.  
`request_id` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
## DeleteSkillRequest

Message requesting deletion of a Skill.

Fields  
---  
`name` |  `string` Required. Target Skill container name to remove.  
`request_id` |  `string` Optional. Signed UUID request idempotency token.  
`force` |  `bool` Optional. If set to true, any child SkillRevisions under this Skill will also be deleted. Otherwise, the request will only succeed if the Skill has no child SkillRevisions.  
  
## DeleteSkillRevisionRequest

Requesting deletion of a specific Revision.

Fields  
---  
`name` |  `string` Required. Target revision name to remove.  
`request_id` |  `string` Optional. Signed UUID request idempotency token.  
  
## Endpoint

Represents an Endpoint.

Fields  
---  
`name` |  `string` Identifier. The resource name of the Endpoint. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`.  
`endpoint_id` |  `string` Output only. A stable, globally unique identifier for Endpoint.  
`display_name` |  `string` Output only. Display name for the Endpoint.  
`description` |  `string` Output only. Description of an Endpoint.  
`interfaces[]` |  `[Interface](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Interface)` Required. The connection details for the Endpoint.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Create time.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Update time.  
`attributes` |  `map<string, `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)`>` Output only. Attributes of the Endpoint.Valid values:

  * `agentregistry.googleapis.com/system/RuntimeReference`: {"uri": "//..."} - the URI of the underlying resource hosting the Endpoint, for example, the GKE Deployment.

  
  
## FetchAvailableBindingsRequest

Message for fetching available Bindings.

Fields  
---  
`parent` |  `string` Required. The parent, in the format `projects/{project}/locations/{location}`.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. Page size is 500 if unspecified and is capped at `500` even if a larger value is given.  
`page_token` |  `string` Optional. A token identifying a page of results the server should return.  
Union field `source`. Required. The reference of the source Agent Registry resource. `source` can be only one of the following:  
`source_identifier` |  `string` The identifier of the source Agent. Format:

  * `urn:agent:{publisher}:{namespace}:{name}`

  
Union field `target`. The reference of the target Agent Registry resource. `target` can be only one of the following:  
`target_identifier` |  `string` Optional. The identifier of the target Agent, MCP Server, or Endpoint. Format:

  * `urn:agent:{publisher}:{namespace}:{name}`
  * `urn:mcp:{publisher}:{namespace}:{name}`
  * `urn:endpoint:{publisher}:{namespace}:{name}`

  
  
## FetchAvailableBindingsResponse

Message for response to fetching available Bindings.

Fields  
---  
`bindings[]` |  `[Binding](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Binding)` The list of Bindings.  
`next_page_token` |  `string` A token identifying a page of results the server should return.  
  
## Frontmatter

Structured metadata attributes extracted from the package's local SKILL.md frontmatter.

Fields  
---  
`name` |  `string` Required. The name of the skill.  
`description` |  `string` Required. Functional description.  
`license` |  `string` Optional. License.  
`compatibility` |  `string` Optional. Environmental dependencies or local sidecars.  
`metadata` |  `map<string, string>` Optional. Extensible flattened map mapping custom tags, authors, and version parameters.  
  
## GcsSource

Specifications for Cloud Storage objects.

Fields  
---  
`uri` |  `string` Required. Cloud Storage object URI. Format: `gs://{bucket_name}/{object_name}`  
`generation` |  `int64` Optional. Cloud Storage object generation ID. If not specified, the latest generation is used.  
  
## GetAgentRequest

Message for getting a Agent

Fields  
---  
`name` |  `string` Required. Name of the resource  
  
## GetBindingRequest

Message for getting a Binding

Fields  
---  
`name` |  `string` Required. The name of the Binding. Format: `projects/{project}/locations/{location}/bindings/{binding}`.  
  
## GetEndpointRequest

Message for getting a Endpoint

Fields  
---  
`name` |  `string` Required. The name of the endpoint to retrieve. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
  
## GetMcpServerRequest

Message for getting a McpServer

Fields  
---  
`name` |  `string` Required. Name of the resource  
  
## GetPublisherRequest

Requesting details of a specific Publisher.

Fields  
---  
`name` |  `string` Required. Target publisher resource name. Format: `projects/{project}/locations/{location}/publishers/{publisher}`  
  
## GetServiceRequest

Message for getting a Service

Fields  
---  
`name` |  `string` Required. The name of the Service. Format: `projects/{project}/locations/{location}/services/{service}`.  
  
## Interface

Represents the connection details for an Agent or MCP Server.

Fields  
---  
`url` |  `string` Required. The destination URL.  
`protocol_binding` |  `[ProtocolBinding](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Interface.ProtocolBinding)` Required. The protocol binding of the interface.  
  
## ProtocolBinding

The protocol binding of the interface.

Enums  
---  
`PROTOCOL_BINDING_UNSPECIFIED` | Unspecified transport protocol.  
`JSONRPC` | JSON-RPC specification.  
`GRPC` | gRPC specification.  
`HTTP_JSON` | HTTP+JSON specification.  
  
## ListAgentsRequest

Message for requesting list of Agents

Fields  
---  
`parent` |  `string` Required. Parent value for ListAgentsRequest  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. Filtering results  
`order_by` |  `string` Optional. Hint for how to order the results  
  
## ListAgentsResponse

Message for response to listing Agents

Fields  
---  
`agents[]` |  `[Agent](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Agent)` The list of Agents.  
`next_page_token` |  `string` A token identifying a page of results the server should return.  
  
## ListBindingsRequest

Message for requesting a list of Bindings.

Fields  
---  
`parent` |  `string` Required. The project and location to list bindings in. Expected format: `projects/{project}/locations/{location}`.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. Page size is 500 if unspecified and is capped at `500` even if a larger value is given.  
`page_token` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. A query string used to filter the list of bindings returned. The filter expression must follow AIP-160 syntax.  
`order_by` |  `string` Optional. Hint for how to order the results  
  
## ListBindingsResponse

Message for response to listing Bindings

Fields  
---  
`bindings[]` |  `[Binding](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Binding)` The list of Binding resources matching the parent and filter criteria in the request. Each Binding resource follows the format: `projects/{project}/locations/{location}/bindings/{binding}`.  
`next_page_token` |  `string` A token identifying a page of results the server should return. Used in `page_token`.  
  
## ListEndpointsRequest

Message for requesting list of Endpoints

Fields  
---  
`parent` |  `string` Required. The project and location to list endpoints in. Expected format: `projects/{project}/locations/{location}`.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. A query string used to filter the list of endpoints returned. The filter expression must follow AIP-160 syntax.Filtering is supported on the `name`, `display_name`, `description`, `version`, and `interfaces` fields.Some examples:

  * `name = "projects/p1/locations/l1/endpoints/e1"`
  * `display_name = "my-endpoint"`
  * `description = "my-endpoint-description"`
  * `version = "v1"`
  * `interfaces.transport = "HTTP_JSON"`

  
  
## ListEndpointsResponse

Message for response to listing Endpoints

Fields  
---  
`endpoints[]` |  `[Endpoint](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Endpoint)` The list of Endpoint resources matching the parent and filter criteria in the request. Each Endpoint resource follows the format: `projects/{project}/locations/{location}/endpoints/{endpoint}`.  
`next_page_token` |  `string` A token identifying a page of results the server should return. Used in `page_token`.  
  
## ListMcpServersRequest

Message for requesting list of McpServers

Fields  
---  
`parent` |  `string` Required. Parent value for ListMcpServersRequest. Format: `projects/{project}/locations/{location}`.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. Filtering results  
`order_by` |  `string` Optional. Hint for how to order the results  
  
## ListMcpServersResponse

Message for response to listing McpServers

Fields  
---  
`mcp_servers[]` |  `[McpServer](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.McpServer)` The list of McpServers.  
`next_page_token` |  `string` A token identifying a page of results the server should return.  
  
## ListPublishersRequest

Requesting a list of Publishers.

Fields  
---  
`parent` |  `string` Required. Parent location to query. Format: `projects/{project}/locations/{location}`  
`page_size` |  `int32` Optional. Page limit size.  
`page_token` |  `string` Optional. Page offset token.  
  
## ListPublishersResponse

Response listing Publishers.

Fields  
---  
`publishers[]` |  `[Publisher](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Publisher)` The returned list of Publishers.  
`next_page_token` |  `string` Page offset continuation token.  
  
## ListServicesRequest

Message for requesting list of Services

Fields  
---  
`parent` |  `string` Required. The project and location to list services in. Expected format: `projects/{project}/locations/{location}`.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. A query string used to filter the list of services returned. The filter expression must follow AIP-160 syntax.Filtering is supported on the `name`, `display_name`, `description`, and `labels` fields.Some examples:

  * `name = "projects/p1/locations/l1/services/s1"`
  * `display_name = "my-service"`
  * `description : "myservice description"`
  * `labels.env = "prod"`

  
  
## ListServicesResponse

Message for response to listing Services

Fields  
---  
`services[]` |  `[Service](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Service)` The list of Service resources matching the parent and filter criteria in the request. Each Service resource follows the format: `projects/{project}/locations/{location}/services/{service}`.  
`next_page_token` |  `string` A token identifying a page of results the server should return. Used in `page_token`.  
  
## ListSkillRevisionsRequest

Requesting a list of Revisions under a Skill.

Fields  
---  
`parent` |  `string` Required. Parent logical container name to query.  
`page_size` |  `int32` Optional. Page limit size.  
`page_token` |  `string` Optional. Page offset token.  
  
## ListSkillRevisionsResponse

Response listing Revisions.

Fields  
---  
`skill_revisions[]` |  `SkillRevision` Returned version snapshot list.  
`next_page_token` |  `string` Page offset continuation token.  
  
## ListSkillsRequest

Requesting a list of Skills inside a location.

Fields  
---  
`parent` |  `string` Required. Parent value for ListSkillsRequest  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. Use this field to specify filter criteria on list results. Filter expressions can be used to restrict results based upon filterable fields, where equality operators can be used. See [instructions](https://docs.cloud.google.com/agent-registry/search-agents-and-tools) for more details.Allowed operators: `=`, `<`, `>`, `NOT`, `AND`, `OR`, and `()`. | Field  | `=` | `<`, `>`  
---|---|---  
state  | Yes  | No   
targetState  | Yes  | No   
createTime  | Yes  | Yes   
updateTime  | Yes  | Yes   
  
Examples:

  * `state=ACTIVE` to restrict results to skills in the `ACTIVE` state.

  
`order_by` |  `string` Optional. Hint for how to order the results  
  
## ListSkillsResponse

Response structure listing logical Skills.

Fields  
---  
`skills[]` |  `Skill` Returned container list.  
`next_page_token` |  `string` Page continuation continuation token.  
`unreachable[]` |  `string` Unreachable locations or failures.  
  
## McpServer

Represents an MCP (Model Context Protocol) Server.

Fields  
---  
`name` |  `string` Identifier. The resource name of the MCP Server. Format: `projects/{project}/locations/{location}/mcpServers/{mcp_server}`.  
`mcp_server_id` |  `string` Output only. A stable, globally unique identifier for MCP Servers.  
`display_name` |  `string` Output only. The display name of the MCP Server.  
`description` |  `string` Output only. The description of the MCP Server.  
`interfaces[]` |  `[Interface](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Interface)` Output only. The connection details for the MCP Server.  
`tools[]` |  `[Tool](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.McpServer.Tool)` Output only. Tools provided by the MCP Server.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Create time.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Update time.  
`attributes` |  `map<string, `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)`>` Output only. Attributes of the MCP Server. Valid values:

  * `agentregistry.googleapis.com/system/RuntimeIdentity`: {"principal": "principal://..."} - the runtime identity associated with the MCP Server.
  * `agentregistry.googleapis.com/system/RuntimeReference`: {"uri": "//..."}
  * the URI of the underlying resource hosting the MCP Server, for example, the GKE Deployment.

  
  
## Tool

Represents a single tool provided by an MCP Server.

Fields  
---  
`name` |  `string` Output only. Human-readable name of the tool.  
`description` |  `string` Output only. Description of what the tool does.  
`annotations` |  `[Annotations](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.McpServer.Tool.Annotations)` Output only. Annotations associated with the tool.  
  
## Annotations

Annotations describing the characteristics and behavior of a tool or operation.

Fields  
---  
`title` |  `string` Output only. A human-readable title for the tool.  
`destructive_hint` |  `bool` Output only. If true, the tool may perform destructive updates to its environment. If false, the tool performs only additive updates. NOTE: This property is meaningful only when `read_only_hint == false` Default: true  
`idempotent_hint` |  `bool` Output only. If true, calling the tool repeatedly with the same arguments will have no additional effect on its environment. NOTE: This property is meaningful only when `read_only_hint == false` Default: false  
`open_world_hint` |  `bool` Output only. If true, this tool may interact with an "open world" of external entities. If false, the tool's domain of interaction is closed. For example, the world of a web search tool is open, whereas that of a memory tool is not. Default: true  
`read_only_hint` |  `bool` Output only. If true, the tool does not modify its environment. Default: false  
  
## OperationMetadata

Represents the metadata of the long-running operation.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`target` |  `string` Output only. Server-defined resource path for the target of the operation.  
`verb` |  `string` Output only. Name of the verb executed by the operation.  
`status_message` |  `string` Output only. Human-readable status of the operation, if any.  
`requested_cancellation` |  `bool` Output only. Identifies whether the user has requested cancellation of the operation. Operations that have been cancelled successfully have `[google.longrunning.Operation.error](https://docs.cloud.google.com/agent-registry/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.rpc.Status.google.longrunning.Operation.error)` value with a `[google.rpc.Status.code](https://docs.cloud.google.com/agent-registry/reference/rpc/google.rpc#google.rpc.Status.FIELDS.int32.google.rpc.Status.code)` of `1`, corresponding to `Code.CANCELLED`.  
`api_version` |  `string` Output only. API version used to start the operation.  
  
## Publisher

Represents a verified Publisher of Skills. Prepopulated publishers include `publishers/cloud.google.com` and `publishers/workspace.google.com`.

Fields  
---  
`name` |  `string` Identifier. Resource name of the publisher. Format: `projects/{project}/locations/{location}/publishers/{publisher}`  
`verified_prefix` |  `string` Required. The verified prefix (e.g. "snowflake-", "google-") associated with this publisher. The system uses this prefix to enforce name-squatting rules during Skill registration. Must be globally unique across all publishers.  
`display_name` |  `string` Optional. Human readable display name of the publisher.  
`publisher_tier` |  `[PublisherTier](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Publisher.PublisherTier)` Output only. The curation tier of the publisher.  
`documentation_uri` |  `string` Optional. URI pointing to official publisher documentation.  
`support_uri` |  `string` Optional. URI pointing to the support portal or email.  
  
## PublisherTier

Curation tier representing the publisher's level of verification.

Enums  
---  
`PUBLISHER_TIER_UNSPECIFIED` | Default value. Unspecified.  
`FIRST_PARTY` | First-party Google-curated and verified global publishers.  
`THIRD_PARTY` | Third-party verified enterprise partner publishers.  
`PRIVATE` | Private publishers within the developer's workspace/project.  
  
## SearchAgentsRequest

Message for searching Agents

Fields  
---  
`parent` |  `string` Required. Parent value for SearchAgentsRequest. Format: `projects/{project}/locations/{location}`.  
`search_string` |  `string` Optional. Search criteria used to select the Agents to return. If no search criteria is specified then all accessible Agents will be returned.Search expressions can be used to restrict results based upon searchable fields, where the operators can be used along with the suffix wildcard symbol `*`. See [instructions](https://docs.cloud.google.com/agent-registry/search-agents-and-tools) for more details.Allowed operators: `=`, `:`, `NOT`, `AND`, `OR`, and `()`.Searchable fields: | Field  | `=` | `:` | `*` | Keyword Search   
---|---|---|---|---  
agentId  | Yes  | Yes  | Yes  | Included   
name  | No  | Yes  | Yes  | Included   
displayName  | No  | Yes  | Yes  | Included   
description  | No  | Yes  | No  | Included   
skills  | No  | Yes  | No  | Included   
skills.id  | No  | Yes  | No  | Included   
skills.name  | No  | Yes  | No  | Included   
skills.description  | No  | Yes  | No  | Included   
skills.tags  | No  | Yes  | No  | Included   
skills.examples  | No  | Yes  | No  | Included   
  
Examples:

  * `agentId="urn:agent:projects-123:projects:123:locations:us-central1:aiplatform:reasoningEngines:1234"` to find the agent with the specified agent ID.
  * `name:important` to find agents whose name contains `important` as a word.
  * `displayName:works*` to find agents whose display name contains words that start with `works`.
  * `skills.tags:test` to find agents whose skills tags contain `test`.
  * `planner OR booking` to find agents whose metadata contains the words `planner` or `booking`.

  
`page_size` |  `int32` Optional. The maximum number of search results to return per page. The page size is capped at `100`, even if a larger value is specified. A negative value will result in an `INVALID_ARGUMENT` error. If unspecified or set to `0`, a default value of `20` will be used. The server may return fewer results than requested.  
`page_token` |  `string` Optional. If present, retrieve the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of all other method parameters, must be identical to those in the previous call.  
  
## SearchAgentsResponse

Message for response to searching Agents

Fields  
---  
`agents[]` |  `[Agent](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Agent)` A list of Agents that match the `search_string`.  
`next_page_token` |  `string` If there are more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`.  
  
## SearchMcpServersRequest

Message for searching MCP Servers

Fields  
---  
`parent` |  `string` Required. Parent value for SearchMcpServersRequest. Format: `projects/{project}/locations/{location}`.  
`search_string` |  `string` Optional. Search criteria used to select the MCP Servers to return. If no search criteria is specified then all accessible MCP Servers will be returned.Search expressions can be used to restrict results based upon searchable fields, where the operators can be used along with the suffix wildcard symbol `*`. See [instructions](https://docs.cloud.google.com/agent-registry/search-agents-and-tools) for more details.Allowed operators: `=`, `:`, `NOT`, `AND`, `OR`, and `()`.Searchable fields: | Field  | `=` | `:` | `*` | Keyword Search   
---|---|---|---|---  
mcpServerId  | Yes  | Yes  | Yes  | Included   
name  | No  | Yes  | Yes  | Included   
displayName  | No  | Yes  | Yes  | Included   
  
Examples:

  * `mcpServerId="urn:mcp:projects-123:projects:123:locations:us-central1:agentregistry:services:service-id"` to find the MCP Server with the specified MCP Server ID.
  * `name:important` to find MCP Servers whose name contains `important` as a word.
  * `displayName:works*` to find MCP Servers whose display name contains words that start with `works`.
  * `planner OR booking` to find MCP Servers whose metadata contains the words `planner` or `booking`.
  * `mcpServerId:service-id AND (displayName:planner OR displayName:booking)` to find MCP Servers whose MCP Server ID contains `service-id` and whose display name contains `planner` or `booking`.

  
`page_size` |  `int32` Optional. The maximum number of search results to return per page. The page size is capped at `100`, even if a larger value is specified. A negative value will result in an `INVALID_ARGUMENT` error. If unspecified or set to `0`, a default value of `20` will be used. The server may return fewer results than requested.  
`page_token` |  `string` Optional. If present, retrieve the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of all other method parameters, must be identical to those in the previous call.  
  
## SearchMcpServersResponse

Message for response to searching MCP Servers

Fields  
---  
`mcp_servers[]` |  `[McpServer](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.McpServer)` A list of McpServers that match the `search_string`.  
`next_page_token` |  `string` If there are more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`.  
  
## SearchSkillsRequest

Requesting a deep search of Skills.

Fields  
---  
`parent` |  `string` Required. Parent value for SearchSkillsRequest. Format: `projects/{project}/locations/{location}`.  
`search_type` |  `[SearchType](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.SearchType)` Optional. The type of search.  
`search_string` |  `string` Optional. Search criteria used to select the Skills to return. If no search criteria is specified then all accessible Skills will be returned.Search expressions can be used to restrict results based upon searchable fields, where the operators can be used along with the suffix wildcard symbol `*`. See [instructions](https://docs.cloud.google.com/agent-registry/search-agents-and-tools) for more details.Allowed operators: `=`, `:`, `NOT`, `AND`, `OR`, and `()`.Searchable fields: | Field  | `=` | `:` | `*` | Keyword Search   
---|---|---|---|---  
skillId  | Yes  | Yes  | Yes  | Included   
name  | No  | Yes  | Yes  | Included   
displayName  | No  | Yes  | Yes  | Included   
description  | No  | Yes  | No  | Included   
frontmatter.name  | No  | Yes  | No  | Included   
frontmatter.description  | No  | Yes  | No  | Included   
frontmatter.compatibility  | No  | Yes  | No  | Included   
frontmatter.license  | No  | Yes  | No  | Included   
  
Examples:

  * `skillId="urn:skill:projects-1234:locations:global:private-important-skill"` to find the skill with the specified skill ID.
  * `name:important` to find skills whose name contains `important` as a word.
  * `displayName:works*` to find skills whose display name contains words that start with `works`.

  
`filter` |  `string` Optional. Use this field to specify additional filter criteria on search results. Filter expressions can be used to restrict results based upon filterable fields, where equality operators can be used. See [instructions](https://docs.cloud.google.com/agent-registry/search-agents-and-tools) for more details.Allowed operators: `=`, `<`, `>`, `NOT`, `AND`, `OR`, and `()`. | Field  | `=` | `<`, `>`  
---|---|---  
state  | Yes  | No   
targetState  | Yes  | No   
createTime  | Yes  | Yes   
updateTime  | Yes  | Yes   
  
Examples:

  * `state=ACTIVE` to restrict results to skills in the `ACTIVE` state.

  
`page_size` |  `int32` Optional. The maximum number of search results to return per page. The page size is capped at `100`, even if a larger value is specified. A negative value will result in an `INVALID_ARGUMENT` error. If unspecified or set to `0`, a default value of `20` will be used. The server may return fewer results than requested.  
`page_token` |  `string` Optional. If present, retrieve the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of all other method parameters, must be identical to those in the previous call.  
  
## SearchSkillsResponse

Response listing searched Skills.

Fields  
---  
`skills[]` |  `Skill` Matched Skills list.  
`next_page_token` |  `string` Query page offset continuation token.  
  
## SearchType

The type of search to perform. Additional search types may be supported in the future.

Enums  
---  
`SEARCH_TYPE_UNSPECIFIED` | Invalid search type.  
`KEYWORD` | Search for a keyword across all searchable fields.  
`SEMANTIC` | Search based on the meaning and intent of a natural language query.  
  
## Service

Represents a user-defined Service.

Fields  
---  
`name` |  `string` Identifier. The resource name of the Service. Format: `projects/{project}/locations/{location}/services/{service}`.  
`display_name` |  `string` Optional. User-defined display name for the Service. Can have a maximum length of `63` characters.  
`description` |  `string` Optional. User-defined description of an Service. Can have a maximum length of `2048` characters.  
`interfaces[]` |  `[Interface](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Interface)` Optional. The connection details for the Service.  
`registry_resource` |  `string` Output only. The resource name of the resulting Agent, MCP Server, or Endpoint. Format:

  * `projects/{project}/locations/{location}/mcpServers/{mcp_server}`
  * `projects/{project}/locations/{location}/agents/{agent}`
  * `projects/{project}/locations/{location}/endpoints/{endpoint}`

  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Create time.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Update time.  
Union field `spec`. The spec of the service. At least one of the specs must be set. `spec` can be only one of the following:  
`agent_spec` |  `[AgentSpec](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Service.AgentSpec)` Optional. The spec of the Agent. When `agent_spec` is set, the type of the service is Agent.  
`mcp_server_spec` |  `[McpServerSpec](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Service.McpServerSpec)` Optional. The spec of the MCP Server. When `mcp_server_spec` is set, the type of the service is MCP Server.  
`endpoint_spec` |  `[EndpointSpec](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Service.EndpointSpec)` Optional. The spec of the Endpoint. When `endpoint_spec` is set, the type of the service is Endpoint.  
  
## AgentSpec

The spec of the agent.

Fields  
---  
`type` |  `[Type](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Service.AgentSpec.Type)` Required. The type of the agent spec content.  
`content` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. The content of the Agent spec in the JSON format. This payload is validated against the schema for the specified type. The content size is limited to `10KB`.  
  
## Type

The type of the agent spec.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`NO_SPEC` | There is no spec for the Agent. The `content` field must be empty.  
`A2A_AGENT_CARD` | The content is an A2A Agent Card following the A2A specification. The `interfaces` field must be empty.  
  
## EndpointSpec

The spec of the endpoint.

Fields  
---  
`type` |  `[Type](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Service.EndpointSpec.Type)` Required. The type of the endpoint spec content.  
`content` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. The content of the endpoint spec. Reserved for future use.  
  
## Type

The type of the endpoint spec. Additional values may be added in the future.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`NO_SPEC` | There is no spec for the Endpoint. The `content` field must be empty.  
  
## McpServerSpec

The spec of the MCP Server.

Fields  
---  
`type` |  `[Type](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Service.McpServerSpec.Type)` Required. The type of the MCP Server spec content.  
`content` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. The content of the MCP Server spec. This payload is validated against the schema for the specified type. The content size is limited to `10KB`.  
  
## Type

The type of the MCP Server spec. Additional values may be added in the future.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`NO_SPEC` | There is no spec for the MCP Server. The `content` field must be empty.  
`TOOL_SPEC` | The content is a MCP Tool Spec following the One MCP specification. The payload is the same as the `tools/list` response.  
  
## State

System-managed state.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`STATE_CREATING` | The skill is being created. It is not served.  
`STATE_DRAFT` | The skill is in draft, or lacks a valid payload. It is not served.  
`STATE_ACTIVE` | The skill is active and is served.  
`STATE_DISABLED` | The skill is disabled and is not served.  
`STATE_DEPRECATED` | The skill is deprecated. It is served, but emits warnings.  
`STATE_DECOMMISSIONED` | The skill is decommissioned and is not served.  
`STATE_DELETING` | The skill is being deleted. It is not served.  
  
## TargetState

User-configurable target state.

Enums  
---  
`TARGET_STATE_UNSPECIFIED` | Default value. This value is unused.  
`TARGET_STATE_DRAFT` | The skill is in draft and cannot be served.  
`TARGET_STATE_ACTIVE` | The skill is active and can be served.  
`TARGET_STATE_DISABLED` | The skill is disabled and cannot be served.  
`TARGET_STATE_DEPRECATED` | The skill is deprecated. It can still be served, but emits warnings.  
`TARGET_STATE_DECOMMISSIONED` | The skill is decommissioned and cannot be served.  
  
## Type

The structural type of the Skill.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value. This value is unused.  
`SIMPLE` | A standard, leaf executable skill containing natural language and code.  
  
## State

System-managed computed state.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`CREATING` | The revision is being created.  
`ACTIVE` | The revision is active.  
`FAILED` | The revision failed to compile or ingest.  
`DELETING` | The revision is being deleted.  
  
## UpdateBindingRequest

Message for updating a Binding

Fields  
---  
`binding` |  `[Binding](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Binding)` Required. The Binding resource that is being updated.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to specify the fields to be overwritten in the Binding resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields present in the request will be overwritten.  
`request_id` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
## UpdateServiceRequest

Message for updating a Service

Fields  
---  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to specify the fields to be overwritten in the Service resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields present in the request will be overwritten.  
`service` |  `[Service](https://docs.cloud.google.com/agent-registry/reference/rpc/google.cloud.agentregistry.v1alpha#google.cloud.agentregistry.v1alpha.Service)` Required. The Service resource that is being updated. Format: `projects/{project}/locations/{location}/services/{service}`.  
`request_id` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
## UpdateSkillRequest

Message requesting a metadata update of a Skill.

Fields  
---  
`skill` |  `Skill` Required. Mutable Skill container config fields to write.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Standard update target mask mapping relative fields.  
`request_id` |  `string` Optional. Signed UUID request idempotency token.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
