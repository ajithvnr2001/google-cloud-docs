---
url: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-grant-tag-template-user-role/
title: Grant tagTemplateUser role \u00a0|\u00a0 Data Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:50:07.106406+00:00
---

# Grant tagTemplateUser role  |  Data Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/samples/data-catalog-grant-tag-template-user-role/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Samples ](https://docs.cloud.google.com/data-catalog/docs/samples)



#  Grant tagTemplateUser role Stay organized with collections  Save and categorize content based on your preferences. 

Grant the tagTemplateUser role to a member of the project.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Enable your organization principals to use tags](https://docs.cloud.google.com/data-catalog/docs/how-to/template-user)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/overview). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.datacatalog.v1.[DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html);
    import com.google.cloud.datacatalog.v1.[TagTemplateName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplateName.html);
    import com.google.iam.v1.[Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import com.google.iam.v1.[SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html);
    import java.io.IOException;
    
    // Sample to grant tag access on template
    public class GrantTagTemplateUserRole {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project";
        String tagTemplateId = "my_tag_template";
        grantTagTemplateUserRole(projectId, tagTemplateId);
      }
    
      public static void grantTagTemplateUserRole(String projectId, String templateId)
          throws IOException {
        // Currently, Data Catalog stores metadata in the us-central1 region.
        String location = "us-central1";
    
        // Format the Template name.
        String templateName =
            [TagTemplateName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplateName.html).newBuilder()
                .setProject(projectId)
                .setLocation(location)
                .setTagTemplate(templateId)
                .build()
                .toString();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html) dataCatalogClient = [DataCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.html).create()) {
    
          // Create a Binding to add the Tag Template User role and member to the policy.
          [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding =
              [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html).newBuilder()
                  .setRole("roles/datacatalog.tagTemplateUser")
                  .[addMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addMembers_java_lang_String_)("group:example-analyst-group@google.com")
                  .build();
    
          // Create a Policy object to update Template's IAM policy by adding the new binding.
          [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policyUpdate = [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html).newBuilder().[addBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addBindings_com_google_iam_v1_Binding_)(binding).build();
    
          [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) request =
              [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html).newBuilder()
                  .[setPolicy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.Builder.html#com_google_iam_v1_SetIamPolicyRequest_Builder_setPolicy_com_google_iam_v1_Policy_)(policyUpdate)
                  .setResource(templateName)
                  .build();
    
          // Update Template's policy.
          dataCatalogClient.setIamPolicy(request);
          System.out.println("Role successfully granted");
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Node.js API reference documentation](https://googleapis.dev/nodejs/datacatalog/latest/index.html). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Google Cloud client library.
    const {DataCatalogClient} = require('[@google-cloud/datacatalog](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)').v1;
    const datacatalog = new [DataCatalogClient](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)();
    
    async function grantTagTemplateUserRole() {
      // Grant the tagTemplateUser role to a member of the project.
    
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // const projectId = 'my_project'; // Google Cloud Platform project
      // const templateId = 'my_existing_template';
      // const memberId = 'my_member_id'
    
      const location = 'us-central1';
    
      // Format the Template name.
      const templateName = datacatalog.tagTemplatePath(
        projectId,
        location,
        templateId
      );
    
      // Retrieve Template's current IAM Policy.
      const [getPolicyResponse] = await datacatalog.getIamPolicy({
        resource: templateName,
      });
      const policy = getPolicyResponse;
    
      // Add Tag Template User role and member to the policy.
      policy.bindings.push({
        role: 'roles/datacatalog.tagTemplateUser',
        members: [memberId],
      });
    
      const request = {
        resource: templateName,
        policy: policy,
      };
    
      // Update Template's policy.
      const [updatePolicyResponse] = await datacatalog.setIamPolicy(request);
    
      updatePolicyResponse.bindings.forEach(binding => {
        console.log(`Role: ${binding.role}, Members: ${binding.members}`);
      });
    }
    grantTagTemplateUserRole();

### Python

Before trying this sample, follow the Python setup instructions in the [Data Catalog quickstart using client libraries](https://docs.cloud.google.com/data-catalog/docs/reference/libraries). For more information, see the [Data Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest). 

To authenticate to Data Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest)
    from google.iam.v1 import iam_policy_pb2 as iam_policy
    from google.iam.v1 import policy_pb2
    
    datacatalog = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).[DataCatalogClient](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html)()
    
    # TODO: Set these values before running the sample.
    project_id = "project_id"
    tag_template_id = "existing_tag_template_id"
    # For a full list of values a member can have, see:
    # https://cloud.google.com/iam/docs/reference/rest/v1/Policy?hl=en#binding
    member_id = "user:super-cool.test-user@gmail.com"
    
    # For all regions available, see:
    # https://cloud.google.com/data-catalog/docs/concepts/regions
    location = "us-central1"
    
    # Format the Template name.
    template_name = [datacatalog_v1](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest).[DataCatalogClient](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html).tag_template_path(
        project_id, location, tag_template_id
    )
    
    # Retrieve Template's current IAM Policy.
    policy = datacatalog.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html#google_cloud_datacatalog_v1_services_data_catalog_DataCatalogClient_get_iam_policy)(resource=template_name)
    
    # Add Tag Template User role and member to the policy.
    binding = policy_pb2.Binding()
    binding.role = "roles/datacatalog.tagTemplateUser"
    binding.members.append(member_id)
    policy.bindings.append(binding)
    
    set_policy_request = iam_policy.SetIamPolicyRequest(
        resource=template_name, policy=policy
    )
    
    # Update Template's policy.
    policy = datacatalog.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/datacatalog/latest/google.cloud.datacatalog_v1.services.data_catalog.DataCatalogClient.html#google_cloud_datacatalog_v1_services_data_catalog_DataCatalogClient_set_iam_policy)(set_policy_request)
    
    for binding in policy.bindings:
        for member in binding.members:
            print(f"Member: {member}, Role: {binding.role}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=datacatalog). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
