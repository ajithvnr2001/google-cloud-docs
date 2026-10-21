---
url: https://docs.cloud.google.com/document-warehouse/docs/samples/contentwarehouse-create-rule-set/
title: Create a rule set \u00a0|\u00a0 Document AI Warehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:45:27.072711+00:00
---

# Create a rule set  |  Document AI Warehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/samples/contentwarehouse-create-rule-set/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Samples ](https://docs.cloud.google.com/document-warehouse/docs/samples)



#  Create a rule set Stay organized with collections  Save and categorize content based on your preferences. 

Create a rule set

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Set up policies](https://docs.cloud.google.com/document-warehouse/docs/policy-engine)



## Code sample

### Java

For more information, see the [Document AI Warehouse Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/overview). 

To authenticate to Document AI Warehouse, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.contentwarehouse.v1.[Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Action.html);
    import com.google.cloud.contentwarehouse.v1.[ActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ActionOrBuilder.html);
    import com.google.cloud.contentwarehouse.v1.[CreateRuleSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateRuleSetRequest.html);
    import com.google.cloud.contentwarehouse.v1.[CreateRuleSetRequestOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateRuleSetRequestOrBuilder.html);
    import com.google.cloud.contentwarehouse.v1.[DeleteDocumentAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DeleteDocumentAction.html);
    import com.google.cloud.contentwarehouse.v1.[DeleteDocumentActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DeleteDocumentActionOrBuilder.html);
    import com.google.cloud.contentwarehouse.v1.[ListRuleSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListRuleSetsRequest.html);
    import com.google.cloud.contentwarehouse.v1.[ListRuleSetsRequestOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListRuleSetsRequestOrBuilder.html);
    import com.google.cloud.contentwarehouse.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.LocationName.html);
    import com.google.cloud.contentwarehouse.v1.[Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Rule.html);
    import com.google.cloud.contentwarehouse.v1.[Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Rule.html).[TriggerType](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Rule.TriggerType.html);
    import com.google.cloud.contentwarehouse.v1.[RuleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleOrBuilder.html);
    import com.google.cloud.contentwarehouse.v1.[RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet.html);
    import com.google.cloud.contentwarehouse.v1.[RuleSetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetOrBuilder.html);
    import com.google.cloud.contentwarehouse.v1.[RuleSetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceClient.html);
    import com.google.cloud.contentwarehouse.v1.[RuleSetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceClient.html).[ListRuleSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceClient.ListRuleSetsPagedResponse.html);
    import com.google.cloud.contentwarehouse.v1.[RuleSetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceSettings.html);
    import com.google.cloud.resourcemanager.v3.[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.Project.html);
    import com.google.cloud.resourcemanager.v3.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html);
    import com.google.cloud.resourcemanager.v3.[ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeoutException;
    
    
    public class CreateRuleSet {
    
      public static void createRuleSet() throws IOException, 
            InterruptedException, ExecutionException, TimeoutException { 
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String location = "your-region"; // Format is "us" or "eu".
        createRuleSet(projectId, location);
      }
    
      public static void createRuleSet(String projectId, String location)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        String projectNumber = getProjectNumber(projectId);
    
        String endpoint = "contentwarehouse.googleapis.com:443";
        if (!"us".equals(location)) {
          endpoint = String.format("%s-%s", location, endpoint);
        }
        [RuleSetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceSettings.html) ruleSetServiceSettings =
            [RuleSetServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
    
        // Create a Rule Set Service Client 
        try ([RuleSetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceClient.html) ruleSetServiceClient = 
            [RuleSetServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceClient.html).create(ruleSetServiceSettings)) {
          /*  The full resource name of the location, e.g.:
          projects/{project_number}/locations/{location} */
          String parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.LocationName.html).format(projectNumber, location); 
    
          // Create a Delete Document Action to be added to the Rule Set 
          [DeleteDocumentActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DeleteDocumentActionOrBuilder.html) deleteDocumentAction = 
              [DeleteDocumentAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DeleteDocumentAction.html).newBuilder().[setEnableHardDelete](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DeleteDocumentAction.Builder.html#com_google_cloud_contentwarehouse_v1_DeleteDocumentAction_Builder_setEnableHardDelete_boolean_)(true).build();
    
          // Add Delete Document Action to Action Object 
          [ActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ActionOrBuilder.html) action = [Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Action.html).newBuilder()
                .[setDeleteDocumentAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Action.Builder.html#com_google_cloud_contentwarehouse_v1_Action_Builder_setDeleteDocumentAction_com_google_cloud_contentwarehouse_v1_DeleteDocumentAction_)(([DeleteDocumentAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DeleteDocumentAction.html)) deleteDocumentAction).build();
    
          // Create rule to add to rule set 
          [RuleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleOrBuilder.html) rule = [Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Rule.html).newBuilder()
              .[setTriggerType](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Rule.Builder.html#com_google_cloud_contentwarehouse_v1_Rule_Builder_setTriggerType_com_google_cloud_contentwarehouse_v1_Rule_TriggerType_)([TriggerType](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Rule.TriggerType.html).ON_CREATE)
              .setCondition("documentType == 'W9' && STATE =='CA' ")
              .[addActions](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Rule.Builder.html#com_google_cloud_contentwarehouse_v1_Rule_Builder_addActions_com_google_cloud_contentwarehouse_v1_Action_)(0, ([Action](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Action.html)) action).build();
    
          // Create rule set and add rule to it
          [RuleSetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetOrBuilder.html) ruleSetOrBuilder = [RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet.html).newBuilder()
              .setDescription("W9: Basic validation check rules.")
              .[setSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet.Builder.html#com_google_cloud_contentwarehouse_v1_RuleSet_Builder_setSource_java_lang_String_)("My Organization")
              .[addRules](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet.Builder.html#com_google_cloud_contentwarehouse_v1_RuleSet_Builder_addRules_com_google_cloud_contentwarehouse_v1_Rule_)(([Rule](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Rule.html)) rule).build();
    
          // Create and prepare rule set request to client
          [CreateRuleSetRequestOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateRuleSetRequestOrBuilder.html) createRuleSetRequest = 
              [CreateRuleSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateRuleSetRequest.html).newBuilder()
                  .setParent(parent)
                  .setRuleSet(([RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet.html)) ruleSetOrBuilder).build();
    
          [RuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSet.html) response = ruleSetServiceClient.createRuleSet(
              ([CreateRuleSetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateRuleSetRequest.html)) createRuleSetRequest);
    
          System.out.println("Rule set created: " + response.toString());
    
          [ListRuleSetsRequestOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListRuleSetsRequestOrBuilder.html) listRuleSetsRequest = 
              [ListRuleSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListRuleSetsRequest.html).newBuilder()
                  .setParent(parent).build();
    
          [ListRuleSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.RuleSetServiceClient.ListRuleSetsPagedResponse.html) listRuleSetsPagedResponse = 
              ruleSetServiceClient.listRuleSets(([ListRuleSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.ListRuleSetsRequest.html)) listRuleSetsRequest);
    
          listRuleSetsPagedResponse.iterateAll().forEach(
              (ruleSet -> System.out.print(ruleSet))
          );
        }
      }
    
      private static String getProjectNumber(String projectId) throws IOException { 
        try ([ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) projectsClient = [ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html).create()) { 
          [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html) projectName = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html).of(projectId); 
          [Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.Project.html) project = projectsClient.getProject(projectName);
          String projectNumber = project.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.Project.html#com_google_cloud_resourcemanager_v3_Project_getName__)(); // Format returned is projects/xxxxxx
          return projectNumber.substring(projectNumber.lastIndexOf("/") + 1);
        } 
      }
    }

### Python

For more information, see the [Document AI Warehouse Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest). 

To authenticate to Document AI Warehouse, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import contentwarehouse
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_number = "YOUR_PROJECT_NUMBER"
    # location = "us" # Format is 'us' or 'eu'
    
    
    def create_rule_set(project_number: str, location: str) -> None:
        # Create a client
        client = contentwarehouse.[RuleSetServiceClient](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.rule_set_service.RuleSetServiceClient.html)()
    
        # The full resource name of the location, e.g.:
        # projects/{project_number}/locations/{location}
        parent = client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.rule_set_service.RuleSetServiceClient.html#google_cloud_contentwarehouse_v1_services_rule_set_service_RuleSetServiceClient_common_location_path)(project=project_number, location=location)
    
        actions = contentwarehouse.[Action](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.Action.html)(
            delete_document_action=contentwarehouse.[DeleteDocumentAction](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.DeleteDocumentAction.html)(
                enable_hard_delete=True
            )
        )
    
        rules = contentwarehouse.[Rule](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.Rule.html)(
            trigger_type="ON_CREATE",
            condition="documentType == 'W9' && STATE =='CA'",
            actions=[actions],
        )
    
        rule_set = contentwarehouse.[RuleSet](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.RuleSet.html)(
            description="W9: Basic validation check rules.",
            source="My Organization",
            rules=[rules],
        )
    
        # Initialize request argument(s)
        request = contentwarehouse.[CreateRuleSetRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.CreateRuleSetRequest.html)(parent=parent, rule_set=rule_set)
    
        # Make the request
        response = client.[create_rule_set](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.rule_set_service.RuleSetServiceClient.html#google_cloud_contentwarehouse_v1_services_rule_set_service_RuleSetServiceClient_create_rule_set)(request=request)
    
        # Handle the response
        print(f"Rule Set Created: {response}")
    
        # Initialize request argument(s)
        request = contentwarehouse.[ListRuleSetsRequest](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.ListRuleSetsRequest.html)(
            parent=parent,
        )
    
        # Make the request
        page_result = client.[list_rule_sets](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.services.rule_set_service.RuleSetServiceClient.html#google_cloud_contentwarehouse_v1_services_rule_set_service_RuleSetServiceClient_list_rule_sets)(request=request)
    
        # Handle the response
        for response in page_result:
            print(f"Rule Sets: {response}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=contentwarehouse). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
