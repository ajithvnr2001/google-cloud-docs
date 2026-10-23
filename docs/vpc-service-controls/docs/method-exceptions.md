---
url: https://docs.cloud.google.com/vpc-service-controls/docs/method-exceptions/
title: Service method exceptions \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:49.682202+00:00
---

# Service method exceptions  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/method-exceptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Reference ](https://docs.cloud.google.com/vpc-service-controls/docs/apis)



Send feedback 

#  Service method exceptions Stay organized with collections  Save and categorize content based on your preferences. 

When you secure a [service supported by VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products) with a perimeter, you can control or restrict access to the service methods using [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules). However, VPC Service Controls can't control some service methods, which can cross the perimeter boundaries.

This page lists the service methods that VPC Service Controls can't control.

## Service method exceptions

Service name | Method  
---|---  
adsdatahub.googleapis.com  | google.ads.adsdatahub.v1.CustomerService.ListCustomers   
adsdatahub.googleapis.com  | google.ads.adsdatahub.v1.OutageService.ListOutages   
adsdatahub.googleapis.com  | google.ads.adsdatahub.v1.VendorService.LookupVocSalt   
agentcommunication.googleapis.com  | google.cloud.agentcommunication.v1.AgentCommunication.StreamAgentMessages   
aiplatform.googleapis.com  | google.cloud.aiplatform.ui.ModelGardenService.CheckAccess   
aiplatform.googleapis.com  | google.cloud.aiplatform.ui.ModelGardenService.CheckPublisherModelAccessControl   
aiplatform.googleapis.com  | google.cloud.aiplatform.ui.ModelGardenService.EnablePublisherModel   
aiplatform.googleapis.com  | google.cloud.aiplatform.ui.ModelGardenService.GetPublisherModel   
aiplatform.googleapis.com  | google.cloud.aiplatform.ui.ModelGardenService.ListPublisherModels   
aiplatform.googleapis.com  | google.cloud.aiplatform.ui.ModelGardenService.ListPublisherModelVersions   
aiplatform.googleapis.com  | google.cloud.aiplatform.ui.ModelGardenService.RequestAccess   
aiplatform.googleapis.com  | google.cloud.aiplatform.ui.ModelGardenService.SearchPublisherModels   
aiplatform.googleapis.com  | google.cloud.aiplatform.v1.ModelGardenService.GetPublisherModel   
aiplatform.googleapis.com  | google.cloud.aiplatform.v1beta1.ModelGardenService.GetPublisherModel   
aiplatform.googleapis.com  | google.cloud.aiplatform.v1beta1.ModelGardenService.ListPublisherModels   
apigee.googleapis.com  | google.cloud.apigee.v1.EndpointAttachmentService.CreateEndpointAttachment   
apigee.googleapis.com  | google.cloud.apigee.v1.HybridIssuersService.ListHybridIssuers   
apigee.googleapis.com  | google.cloud.apigee.v1.InstanceService.CreateInstance   
apigee.googleapis.com  | google.cloud.apigee.v1.InstanceService.CreateInstanceAndAttachments   
apigee.googleapis.com  | google.cloud.apigee.v1.OrganizationService.CreateOrganization   
apigee.googleapis.com  | google.cloud.apigee.v1.OrganizationService.ListOrganizations   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.v1.AssuredWorkloadsService.ListWorkloads   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.AcknowledgeViolation   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.CreateWorkload   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.DeleteWorkload   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.EnableResourceMonitoring   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.GetViolation   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.ListViolations   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1.AssuredWorkloadsV1MainService.MutatePartnerPermissions   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.AcknowledgeViolation   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.ApplyWorkloadUpdate   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.CreateWorkload   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.DeleteWorkload   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.EnableComplianceUpdates   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.EnableResourceMonitoring   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.GetViolation   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.ListViolations   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1beta1.AssuredWorkloadsV1MainService.ListWorkloadUpdates   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1main.AssuredWorkloadsV1MainService.CheckOnboardingState   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1main.AssuredWorkloadsV1MainService.CreateWorkload   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1main.AssuredWorkloadsV1MainService.DeleteWorkload   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1main.AssuredWorkloadsV1MainService.EnableResourceMonitoring   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1main.AssuredWorkloadsV1MainService.GetComplianceStats   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1main.AssuredWorkloadsV1MainService.GetOnboardingChecklist   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1main.AssuredWorkloadsV1MainService.GetViolation   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1main.AssuredWorkloadsV1MainService.GetWorkload   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1main.AssuredWorkloadsV1MainService.ListViolationQuickFilters   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1main.AssuredWorkloadsV1MainService.ListViolations   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1main.AssuredWorkloadsV1MainService.ListWorkloads   
assuredworkloads.googleapis.com  | google.cloud.assuredworkloads.versioning.v1main.AssuredWorkloadsV1MainService.ListWorkloadUpdates   
backupdr.googleapis.com  | google.cloud.backupdr.v1.BackupDR.TestIamPermissions   
binaryauthorization.googleapis.com  | google.cloud.binaryauthorization.v1.BinaryAuthorizationUiHelpersV1.ValidatePublicKey   
binaryauthorization.googleapis.com  | google.cloud.binaryauthorization.v1.PlatformPolicyManagementService.ListPlatforms   
binaryauthorization.googleapis.com  | google.cloud.binaryauthorization.v1.SystemPolicyV1.GetSystemPolicy   
binaryauthorization.googleapis.com  | google.cloud.binaryauthorization.v1beta1.SystemPolicyV1Beta1.GetSystemPolicy   
cloud.googleapis.com  | google.cloud.location.Locations.GetLocation   
cloudbuild.googleapis.com  | google.cloud.location.Locations.GetLocation   
cloudbuild.googleapis.com  | google.devtools.cloudbuild.v1.CloudBuild.ListGitHubRepositories   
cloudbuild.googleapis.com  | google.devtools.cloudbuild.v1.CloudBuild.ReceiveGitHubDotComWebhook   
cloudbuild.googleapis.com  | google.devtools.cloudbuild.v1.CloudBuild.ReceiveRegionalWebhook   
cloudbuild.googleapis.com  | google.devtools.cloudbuild.v1.CloudBuild.ReceiveTriggerWebhook   
cloudbuild.googleapis.com  | google.devtools.cloudbuild.v1.CloudBuild.ReceiveWebhook   
cloudbuild.googleapis.com  | google.devtools.cloudbuild.v2.RepositoryManager.ProcessWebhook   
cloudfunctions.googleapis.com  | google.cloud.functions.v2.FunctionService.ListRuntimes   
cloudfunctions.googleapis.com  | google.cloud.functions.v2alpha.FunctionService.ListRuntimes   
cloudfunctions.googleapis.com  | google.cloud.functions.v2beta.FunctionService.ListRuntimes   
cloudkms.googleapis.com  | google.cloud.location.Locations.GetLocation   
cloudresourcemanager.googleapis.com  | google.cloud.lien.v1.Liens.CreateLien   
cloudresourcemanager.googleapis.com  | google.cloud.lien.v1.Liens.DeleteLien   
cloudresourcemanager.googleapis.com  | google.cloud.lien.v1.Liens.DeleteLien   
cloudresourcemanager.googleapis.com  | google.cloud.lien.v1.Liens.GetLien   
cloudresourcemanager.googleapis.com  | google.cloud.lien.v1.Liens.GetLien   
cloudresourcemanager.googleapis.com  | google.cloud.lien.v1.Liens.ListLiens   
cloudresourcemanager.googleapis.com  | google.cloud.orgpolicy.v1.OrgPolicy.ClearOrgPolicy   
cloudresourcemanager.googleapis.com  | google.cloud.orgpolicy.v1.OrgPolicy.GetEffectiveOrgPolicy   
cloudresourcemanager.googleapis.com  | google.cloud.orgpolicy.v1.OrgPolicy.GetOrgPolicy   
cloudresourcemanager.googleapis.com  | google.cloud.orgpolicy.v1.OrgPolicy.ListAvailableOrgPolicyConstraints   
cloudresourcemanager.googleapis.com  | google.cloud.orgpolicy.v1.OrgPolicy.ListOrgPolicies   
cloudresourcemanager.googleapis.com  | google.cloud.orgpolicy.v1.OrgPolicy.SetOrgPolicy   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v2.Folders.CreateFolder   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v2.Folders.DeleteFolder   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v2.Folders.GetFolder   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v2.Folders.GetIamPolicy   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v2.Folders.ListFolders   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v2.Folders.MoveFolder   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v2.Folders.SetIamPolicy   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v2.Folders.TestIamPermissions   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v2.Folders.UndeleteFolder   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v2.Folders.UpdateFolder   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Folders.CreateFolder   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Folders.DeleteFolder   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Folders.GetFolder   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Folders.GetIamPolicy   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Folders.ListFolders   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Folders.MoveFolder   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Folders.SetIamPolicy   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Folders.TestIamPermissions   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Folders.UndeleteFolder   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Folders.UpdateFolder   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Organizations.GetIamPolicy   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Organizations.GetOrganization   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Organizations.SetIamPolicy   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Organizations.TestIamPermissions   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Projects.DeleteProject   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Projects.GetIamPolicy   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Projects.GetProject   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Projects.GetProjectAncestry   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Projects.ListProjects   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Projects.MoveProject   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Projects.TestIamPermissions   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Projects.UndeleteProject   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.Projects.UpdateProject   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.ResourceManagerEffectiveSettings.GetEffectiveSetting   
cloudresourcemanager.googleapis.com  | google.cloud.resourcemanager.v3.ResourceManagerSettings.GetSetting   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.projects.v1beta1.DeveloperProjects   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.projects.v1beta1.DeveloperProjects.GetAncestry   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.projects.v1beta1.DeveloperProjects.GetIamPolicy   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.projects.v1beta1.DeveloperProjects.GetProject   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.projects.v1beta1.DeveloperProjects.ListProjects   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.projects.v1beta1.DeveloperProjects.TestIamPermissions   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.v1.OrganizationsV1.DeleteOrganization   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.v1.OrganizationsV1.GetIamPolicy   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.v1.OrganizationsV1.GetOrganization   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.v1.OrganizationsV1.SetIamPolicy   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.v1.OrganizationsV1.TestIamPermissions   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.v1.OrganizationsV1.UndeleteOrganization   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.v1.Projects   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.v1.Projects.GetAncestry   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.v1.Projects.GetIamPolicy   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.v1.Projects.GetProject   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.v1.Projects.ListProjects   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.v1.Projects.TestIamPermissions   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.v1beta1.organizations.Organizations.DeleteOrganization   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.v1beta1.organizations.Organizations.GetIamPolicy   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.v1beta1.organizations.Organizations.GetOrganization   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.v1beta1.organizations.Organizations.SetIamPolicy   
cloudresourcemanager.googleapis.com  | google.cloudresourcemanager.v1beta1.organizations.Organizations.UndeleteOrganization   
cloudsupport.googleapis.com  | google.cloud.support.v2.CaseService.SearchCaseClassifications   
cloudsupport.googleapis.com  | google.cloud.support.v2beta.CaseService.SearchCaseClassifications   
cloudtasks.googleapis.com  | google.cloud.tasks.v2beta2.CloudTasks.PullTasks   
compute.googleapis.com  | compute.beta.NetworkInstancesService.Get   
compute.googleapis.com  | compute.beta.NetworkInstancesService.Insert   
container.googleapis.com  | google.container.v1.AuditService.CheckPolicy   
container.googleapis.com  | google.container.v1.ClusterManager.GetJSONWebKeys   
container.googleapis.com  | google.container.v1.ClusterManager.GetOpenIDConfig   
container.googleapis.com  | google.container.v1.HostedMasterService.AcknowledgeRepairWork   
container.googleapis.com  | google.container.v1.HostedMasterService.Authenticate   
container.googleapis.com  | google.container.v1.HostedMasterService.Authorize   
container.googleapis.com  | google.container.v1.HostedMasterService.AuthorizeSAMapping   
container.googleapis.com  | google.container.v1.HostedMasterService.CheckAuditPolicy   
container.googleapis.com  | google.container.v1.HostedMasterService.CreateSignedUrls   
container.googleapis.com  | google.container.v1.HostedMasterService.CreateToken   
container.googleapis.com  | google.container.v1.HostedMasterService.GetAutoscalerFlags   
container.googleapis.com  | google.container.v1.HostedMasterService.GetMasterMetadata   
container.googleapis.com  | google.container.v1.HostedMasterService.GetPrivateEndpointAuthorizedNetworks   
container.googleapis.com  | google.container.v1.HostedMasterService.GetRepairWork   
container.googleapis.com  | google.container.v1.HostedMasterService.ReportPodUsage   
container.googleapis.com  | google.container.v1.HostedMasterService.SignCertificate   
container.googleapis.com  | google.container.v1.HostedMasterService.SyncNode   
container.googleapis.com  | google.container.v1beta1.ClusterManager.GetOpenIDConfig   
container.googleapis.com  | google.container.v1beta1.ClusterManager.ListLocations   
discoveryengine.googleapis.com  | google.cloud.discoveryengine.v1alpha.DataConnectorService.GetConnectorSource   
discoveryengine.googleapis.com  | google.cloud.discoveryengine.v1alpha.DataConnectorService.ListConnectorSources   
discoveryengine.googleapis.com  | google.cloud.discoveryengine.v1alpha.WidgetService.LookupWidgetConfig   
discoveryengine.googleapis.com  | google.cloud.discoveryengine.v1alpha.WidgetService.SendFeedback   
discoveryengine.googleapis.com  | google.cloud.discoveryengine.v1alpha.WidgetService.WidgetConverseConversation   
dlp.googleapis.com  | google.privacy.dlp.v2.DlpService.ListInfoTypes   
earthengine.googleapis.com  | google.earthengine.v1.EarthEngine.AppealRestriction   
earthengine.googleapis.com  | google.earthengine.v1.EarthEngine.ChangeSubscriptionType   
earthengine.googleapis.com  | google.earthengine.v1.EarthEngine.GetCapabilities   
earthengine.googleapis.com  | google.earthengine.v1.EarthEngine.ListSubscriptions   
earthengine.googleapis.com  | google.earthengine.v1alpha.EarthEngine.GetCapabilities   
earthengine.googleapis.com  | google.earthengine.v1beta.EarthEngine.GetCapabilities   
essentialcontacts.googleapis.com  | google.cloud.essentialcontacts.v1.EssentialContactsService.SendTestMessage   
essentialcontacts.googleapis.com  | google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.ResendVerification   
essentialcontacts.googleapis.com  | google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.SendTestMessage   
essentialcontacts.googleapis.com  | google.cloud.essentialcontacts.v1alpha1.EssentialContactsService.VerifyContact   
essentialcontacts.googleapis.com  | google.cloud.essentialcontacts.v1beta1.EssentialContactsService.SendTestMessage   
gkemulticloud.googleapis.com  | google.cloud.gkemulticloud.v1.AttachedClusters.GenerateAttachedClusterAgentToken   
gkemulticloud.googleapis.com  | google.cloud.gkemulticloud.v1.AwsClusters.GenerateAwsClusterAgentToken   
gkemulticloud.googleapis.com  | google.cloud.gkemulticloud.v1.AwsClusters.GetAwsJsonWebKeys   
gkemulticloud.googleapis.com  | google.cloud.gkemulticloud.v1.AwsClusters.GetAwsOpenIdConfig   
gkemulticloud.googleapis.com  | google.cloud.gkemulticloud.v1.AzureClusters.GenerateAzureClusterAgentToken   
gkemulticloud.googleapis.com  | google.cloud.gkemulticloud.v1.AzureClusters.GetAzureJsonWebKeys   
gkemulticloud.googleapis.com  | google.cloud.gkemulticloud.v1.AzureClusters.GetAzureOpenIdConfig   
iam.googleapis.com  | google.iam.admin.v1.IAM.LintPolicy   
iam.googleapis.com  | google.iam.admin.v1.IAM.QueryAuditableServices   
iam.googleapis.com  | google.iam.admin.v1.IAM.QueryTestablePermissions   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.CreateWorkforcePool   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProvider   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.CreateWorkforcePoolProviderKey   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.DeleteWorkforcePool   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProvider   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolProviderKey   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.DeleteWorkforcePoolSubject   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.GetIamPolicy   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.GetWorkforcePool   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProvider   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.GetWorkforcePoolProviderKey   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviderKeys   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.ListWorkforcePoolProviders   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.ListWorkforcePools   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.SetIamPolicy   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.TestIamPermissions   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePool   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProvider   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolProviderKey   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.UndeleteWorkforcePoolSubject   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.UpdateWorkforcePool   
iam.googleapis.com  | google.iam.admin.v1.WorkforcePools.UpdateWorkforcePoolProvider   
identitytoolkit.googleapis.com  | google.cloud.identitytoolkit.admin.v2.ProjectConfigService.ListDefaultSupportedIdps   
identitytoolkit.googleapis.com  | google.cloud.identitytoolkit.v1.AuthenticationService.GetPublicKeys   
identitytoolkit.googleapis.com  | google.cloud.identitytoolkit.v1.SessionManagementService.GetSessionCookiePublicKeys   
identitytoolkit.googleapis.com  | google.cloud.identitytoolkit.v2beta1.ProjectConfigService.ListDefaultSupportedIdps   
lifesciences.googleapis.com  | google.genomics.v2alpha1.WorkerV2Alpha1.CheckIn   
logging.googleapis.com  | google.logging.v2.RoutingConfigService.GetMetricBucket   
logging.googleapis.com  | google.logging.v2.UiSupportService.TranslateQuery   
logging.googleapis.com  | google.logging.v2.UiSupportService.ValidateAndGetExpression   
metastore.googleapis.com  | google.cloud.metastore.v1main.DataprocMetastore.AlterMetadataResourceLocation   
metastore.googleapis.com  | google.cloud.metastore.v1main.DataprocMetastore.AlterTableProperties   
metastore.googleapis.com  | google.cloud.metastore.v1main.DataprocMetastore.MoveTableToDatabase   
monitoring.googleapis.com  | google.monitoring.v3.UptimeCheckService.ListUptimeCheckIps   
osconfig.googleapis.com  | google.cloud.osconfig.agentendpoint.v1.AgentEndpointService.ReceiveTaskNotification   
osconfig.googleapis.com  | google.cloud.osconfig.agentendpoint.v1.AgentEndpointService.RegisterAgent   
osconfig.googleapis.com  | google.cloud.osconfig.agentendpoint.v1.AgentEndpointService.ReportInventory   
osconfig.googleapis.com  | google.cloud.osconfig.agentendpoint.v1.AgentEndpointService.ReportTaskComplete   
osconfig.googleapis.com  | google.cloud.osconfig.agentendpoint.v1.AgentEndpointService.ReportTaskProgress   
osconfig.googleapis.com  | google.cloud.osconfig.agentendpoint.v1.AgentEndpointService.StartNextTask   
osconfig.googleapis.com  | google.cloud.osconfig.agentendpoint.v1beta.AgentEndpointService.LookupEffectiveGuestPolicy   
osconfig.googleapis.com  | google.cloud.osconfig.agentendpoint.v1beta.AgentEndpointService.ReceiveTaskNotification   
osconfig.googleapis.com  | google.cloud.osconfig.agentendpoint.v1beta.AgentEndpointService.ReportTaskComplete   
osconfig.googleapis.com  | google.cloud.osconfig.agentendpoint.v1beta.AgentEndpointService.ReportTaskProgress   
osconfig.googleapis.com  | google.cloud.osconfig.agentendpoint.v1beta.AgentEndpointService.StartNextTask   
oslogin.googleapis.com  | google.cloud.oslogin.v1.OsLoginService.CreateSshPublicKey   
oslogin.googleapis.com  | google.cloud.oslogin.v1.OsLoginService.DeletePosixAccount   
oslogin.googleapis.com  | google.cloud.oslogin.v1.OsLoginService.DeleteSshPublicKey   
oslogin.googleapis.com  | google.cloud.oslogin.v1.OsLoginService.GetLoginProfile   
oslogin.googleapis.com  | google.cloud.oslogin.v1.OsLoginService.GetSshPublicKey   
oslogin.googleapis.com  | google.cloud.oslogin.v1.OsLoginService.ImportSshPublicKey   
oslogin.googleapis.com  | google.cloud.oslogin.v1.OsLoginService.UpdateSshPublicKey   
oslogin.googleapis.com  | google.cloud.oslogin.v1alpha.OsLoginService.CreateSshPublicKey   
oslogin.googleapis.com  | google.cloud.oslogin.v1alpha.OsLoginService.DeletePosixAccount   
oslogin.googleapis.com  | google.cloud.oslogin.v1alpha.OsLoginService.DeleteSshPublicKey   
oslogin.googleapis.com  | google.cloud.oslogin.v1alpha.OsLoginService.GetLoginProfile   
oslogin.googleapis.com  | google.cloud.oslogin.v1alpha.OsLoginService.GetSshPublicKey   
oslogin.googleapis.com  | google.cloud.oslogin.v1alpha.OsLoginService.ImportSshPublicKey   
oslogin.googleapis.com  | google.cloud.oslogin.v1alpha.OsLoginService.SignSshPublicKey   
oslogin.googleapis.com  | google.cloud.oslogin.v1alpha.OsLoginService.UpdateSshPublicKey   
oslogin.googleapis.com  | google.cloud.oslogin.v1beta.OsLoginService.CreateSshPublicKey   
oslogin.googleapis.com  | google.cloud.oslogin.v1beta.OsLoginService.DeletePosixAccount   
oslogin.googleapis.com  | google.cloud.oslogin.v1beta.OsLoginService.DeleteSshPublicKey   
oslogin.googleapis.com  | google.cloud.oslogin.v1beta.OsLoginService.GetLoginProfile   
oslogin.googleapis.com  | google.cloud.oslogin.v1beta.OsLoginService.GetSshPublicKey   
oslogin.googleapis.com  | google.cloud.oslogin.v1beta.OsLoginService.ImportSshPublicKey   
oslogin.googleapis.com  | google.cloud.oslogin.v1beta.OsLoginService.SignSshPublicKey   
oslogin.googleapis.com  | google.cloud.oslogin.v1beta.OsLoginService.UpdateSshPublicKey   
recommender.googleapis.com  | google.cloud.recommender.v1beta1.Recommender.ListInsightTypes   
recommender.googleapis.com  | google.cloud.recommender.v1beta1.Recommender.ListRecommenders   
securesourcemanager.googleapis.com  | google.cloud.securesourcemanager.internalv1.SecureSourceManagerDataPlane.CreateRepository   
securesourcemanager.googleapis.com  | google.cloud.securesourcemanager.internalv1.SecureSourceManagerDataPlane.DeleteBranchRule   
securesourcemanager.googleapis.com  | google.cloud.securesourcemanager.internalv1.SecureSourceManagerDataPlane.DeleteRepository   
securesourcemanager.googleapis.com  | google.cloud.securesourcemanager.internalv1.SecureSourceManagerDataPlane.GetBranchRule   
securesourcemanager.googleapis.com  | google.cloud.securesourcemanager.internalv1.SecureSourceManagerDataPlane.GetRepository   
securesourcemanager.googleapis.com  | google.cloud.securesourcemanager.internalv1.SecureSourceManagerDataPlane.ListBranchRules   
securesourcemanager.googleapis.com  | google.cloud.securesourcemanager.internalv1.SecureSourceManagerDataPlane.ListRepositories   
securesourcemanager.googleapis.com  | google.cloud.securesourcemanager.internalv1.SecureSourceManagerDataPlane.UpdateBranchRule   
sts.googleapis.com  | google.identity.sts.v1.SecurityTokenService.ExchangeOauthToken   
sts.googleapis.com  | google.identity.sts.v1.SecurityTokenService.ExchangeToken   
sts.googleapis.com  | google.identity.sts.v1.SecurityTokenService.IntrospectToken   
sts.googleapis.com  | google.identity.sts.v1beta.SecurityTokenService.ExchangeToken   
webrisk.googleapis.com  | google.cloud.webrisk.v1.WebRiskService.ComputeThreatListDiff   
webrisk.googleapis.com  | google.cloud.webrisk.v1.WebRiskService.CreateSubmission   
webrisk.googleapis.com  | google.cloud.webrisk.v1.WebRiskService.SearchHashes   
webrisk.googleapis.com  | google.cloud.webrisk.v1.WebRiskService.SearchUris   
webrisk.googleapis.com  | google.cloud.webrisk.v1.WebRiskService.SubmitUri   
webrisk.googleapis.com  | google.cloud.webrisk.v1alpha1.WebRiskServiceV1Alpha1.FetchThreatListUpdates   
webrisk.googleapis.com  | google.cloud.webrisk.v1alpha1.WebRiskServiceV1Alpha1.FindFullHashes   
webrisk.googleapis.com  | google.cloud.webrisk.v1alpha1.WebRiskServiceV1Alpha1.FindThreatMatches   
webrisk.googleapis.com  | google.cloud.webrisk.v1alpha1.WebRiskServiceV1Alpha1.ListThreatLists   
webrisk.googleapis.com  | google.cloud.webrisk.v1beta1.WebRiskServiceV1Beta1.ComputeThreatListDiff   
webrisk.googleapis.com  | google.cloud.webrisk.v1beta1.WebRiskServiceV1Beta1.SearchHashes   
webrisk.googleapis.com  | google.cloud.webrisk.v1beta1.WebRiskServiceV1Beta1.SearchUris   
webrisk.googleapis.com  | google.cloud.webrisk.v1eap1.WebRiskServiceV1EAP1.EvaluateUri   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
