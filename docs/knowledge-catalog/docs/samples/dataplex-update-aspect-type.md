---
url: https://docs.cloud.google.com/knowledge-catalog/docs/samples/dataplex-update-aspect-type/
title: Update aspect type \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:12.252759+00:00
---

# Update aspect type  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/samples/dataplex-update-aspect-type/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Samples ](https://docs.cloud.google.com/knowledge-catalog/docs/samples)



#  Update aspect type Stay organized with collections  Save and categorize content based on your preferences. 

Update an aspect type.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html);
    import com.google.cloud.dataplex.v1.[AspectTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectTypeName.html);
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.util.List;
    
    public class UpdateAspectType {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "MY_PROJECT_ID";
        // Available locations: https://cloud.google.com/dataplex/docs/locations
        String location = "MY_LOCATION";
        String aspectTypeId = "MY_ASPECT_TYPE_ID";
    
        [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html).[MetadataTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.MetadataTemplate.html) aspectField =
            [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html).MetadataTemplate.newBuilder()
                // The name must follow regex ^(([a-zA-Z]{1})([\\w\\-_]{0,62}))$
                // That means name must only contain alphanumeric character or dashes or underscores,
                // start with an alphabet, and must be less than 63 characters.
                .setName("name_of_the_field")
                // Metadata Template is recursive structure,
                // primitive types such as "string" or "integer" indicate leaf node,
                // complex types such as "record" or "array" would require nested Metadata Template
                .setType("string")
                .setIndex(1)
                .[setAnnotations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.MetadataTemplate.Builder.html#com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_Builder_setAnnotations_com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_Annotations_)(
                    [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html).MetadataTemplate.Annotations.newBuilder()
                        .setDescription("updated description of the field")
                        .build())
                .[setConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.MetadataTemplate.Builder.html#com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_Builder_setConstraints_com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_Constraints_)(
                    [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html).MetadataTemplate.Constraints.newBuilder()
                        // Specifies if field will be required in Aspect Type
                        .[setRequired](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.MetadataTemplate.Constraints.Builder.html#com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_Constraints_Builder_setRequired_boolean_)(true)
                        .build())
                .build();
        List<AspectType.[MetadataTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.MetadataTemplate.html)> aspectFields = List.of(aspectField);
        [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html) updatedAspectType =
            updateAspectType(projectId, location, aspectTypeId, aspectFields);
        System.out.println("Successfully updated aspect type: " + updatedAspectType.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html#com_google_cloud_dataplex_v1_AspectType_getName__)());
      }
    
      // Method to update Aspect Type located in projectId, location and with aspectTypeId and
      // aspectFields specifying schema of the Aspect Type
      public static [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html) updateAspectType(
          String projectId,
          String location,
          String aspectTypeId,
          List<AspectType.[MetadataTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.MetadataTemplate.html)> aspectFields)
          throws Exception {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) client = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html) aspectType =
              [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html).newBuilder()
                  .setName([AspectTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectTypeName.html).of(projectId, location, aspectTypeId).toString())
                  .setDescription("updated description of the aspect type")
                  .[setMetadataTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.Builder.html#com_google_cloud_dataplex_v1_AspectType_Builder_setMetadataTemplate_com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_)(
                      [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html).MetadataTemplate.newBuilder()
                          // Because Record Fields is an array, it needs to be fully replaced.
                          // It is because you do not have a way to specify array elements in update
                          // mask.
                          .[addAllRecordFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.MetadataTemplate.Builder.html#com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_Builder_addAllRecordFields_java_lang_Iterable___extends_com_google_cloud_dataplex_v1_AspectType_MetadataTemplate__)(aspectFields)
                          .build())
                  .build();
    
          // Update mask specifies which fields will be updated.
          // For more information on update masks, see: https://google.aip.dev/161
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask =
              [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder()
                  .addPaths("description")
                  .addPaths("metadata_template.record_fields")
                  .build();
          return client.[updateAspectTypeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html#com_google_cloud_dataplex_v1_CatalogServiceClient_updateAspectTypeAsync_com_google_cloud_dataplex_v1_AspectType_com_google_protobuf_FieldMask_)(aspectType, updateMask).get();
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def update_aspect_type(
        project_id: str,
        location: str,
        aspect_type_id: str,
        aspect_fields: List[[dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[AspectType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.html).[MetadataTemplate](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.html)],
    ) -> dataplex_v1.AspectType:
        """Method to update Aspect Type located in project_id, location and with aspect_type_id and
        aspect_fields specifying schema of the Aspect Type"""
    
        # Initialize client that will be used to send requests across threads. This
        # client only needs to be created once, and can be reused for multiple requests.
        # After completing all of your requests, call the "__exit__()" method to safely
        # clean up any remaining background resources. Alternatively, use the client as
        # a context manager.
        with [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)() as client:
            # The resource name of the Aspect Type
            name = (
                f"projects/{project_id}/locations/{location}/aspectTypes/{aspect_type_id}"
            )
            aspect_type = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[AspectType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.html)(
                name=name,
                description="updated description of the aspect type",
                metadata_template=[dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[AspectType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.html).[MetadataTemplate](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.html)(
                    # Because Record Fields is an array, it needs to be fully replaced.
                    # It is because you do not have a way to specify array elements in update mask.
                    record_fields=aspect_fields
                ),
            )
    
            # Update mask specifies which fields will be updated.
            # For more information on update masks, see: https://google.aip.dev/161
            update_mask = {"paths": ["description", "metadata_template.record_fields"]}
            update_operation = client.update_aspect_type(
                aspect_type=aspect_type, update_mask=update_mask
            )
            return update_operation.result(60)
    
    
    if __name__ == "__main__":
        # TODO(developer): Replace these variables before running the sample.
        project_id = "MY_PROJECT_ID"
        # Available locations: https://cloud.google.com/dataplex/docs/locations
        location = "MY_LOCATION"
        aspect_type_id = "MY_ASPECT_TYPE_ID"
        aspect_field = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[AspectType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.html).[MetadataTemplate](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.html)(
            # The name must follow regex ^(([a-zA-Z]{1})([\\w\\-_]{0,62}))$
            # That means name must only contain alphanumeric character or dashes or underscores,
            # start with an alphabet, and must be less than 63 characters.
            name="name_of_the_field",
            # Metadata Template is recursive structure,
            # primitive types such as "string" or "integer" indicate leaf node,
            # complex types such as "record" or "array" would require nested Metadata Template
            type="string",
            index=1,
            annotations=[dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[AspectType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.html).[MetadataTemplate](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.html).[Annotations](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.Annotations.html)(
                description="updated description of the field"
            ),
            constraints=[dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[AspectType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.html).[MetadataTemplate](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.html).[Constraints](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.Constraints.html)(
                # Specifies if field will be required in Aspect Type.
                required=True
            ),
        )
        aspect_fields = [aspect_field]
    
        updated_aspect_type = update_aspect_type(
            project_id, location, aspect_type_id, aspect_fields
        )
        print(f"Successfully updated aspect type: {updated_aspect_type.name}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataplex). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
