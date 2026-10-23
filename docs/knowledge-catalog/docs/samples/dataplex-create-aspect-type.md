---
url: https://docs.cloud.google.com/knowledge-catalog/docs/samples/dataplex-create-aspect-type/
title: Create aspect type \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:54.131374+00:00
---

# Create aspect type  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/samples/dataplex-create-aspect-type/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Samples ](https://docs.cloud.google.com/knowledge-catalog/docs/samples)



#  Create aspect type Stay organized with collections  Save and categorize content based on your preferences. 

Create an aspect type.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Knowledge Catalog client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html);
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html);
    import java.util.List;
    
    public class CreateAspectType {
    
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
                        .setDescription("description of the field")
                        .build())
                .[setConstraints](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.MetadataTemplate.Builder.html#com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_Builder_setConstraints_com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_Constraints_)(
                    [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html).MetadataTemplate.Constraints.newBuilder()
                        // Specifies if field will be required in Aspect Type.
                        .[setRequired](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.MetadataTemplate.Constraints.Builder.html#com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_Constraints_Builder_setRequired_boolean_)(true)
                        .build())
                .build();
        List<AspectType.[MetadataTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.MetadataTemplate.html)> aspectFields = List.of(aspectField);
        [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html) createdAspectType =
            createAspectType(projectId, location, aspectTypeId, aspectFields);
        System.out.println("Successfully created aspect type: " + createdAspectType.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html#com_google_cloud_dataplex_v1_AspectType_getName__)());
      }
    
      // Method to create Aspect Type located in projectId, location and with aspectTypeId and
      // aspectFields specifying schema of the Aspect Type
      public static [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html) createAspectType(
          String projectId,
          String location,
          String aspectTypeId,
          List<AspectType.[MetadataTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.MetadataTemplate.html)> aspectFields)
          throws Exception {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) client = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html) locationName = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html).of(projectId, location);
          [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html) aspectType =
              [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html).newBuilder()
                  .setDescription("description of the aspect type")
                  .[setMetadataTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.Builder.html#com_google_cloud_dataplex_v1_AspectType_Builder_setMetadataTemplate_com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_)(
                      [AspectType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.html).MetadataTemplate.newBuilder()
                          // The name must follow regex ^(([a-zA-Z]{1})([\\w\\-_]{0,62}))$
                          // That means name must only contain alphanumeric character or dashes or
                          // underscores, start with an alphabet, and must be less than 63 characters.
                          .setName("name_of_the_template")
                          .setType("record")
                          // Aspect Type fields, that themselves are Metadata Templates
                          .[addAllRecordFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.AspectType.MetadataTemplate.Builder.html#com_google_cloud_dataplex_v1_AspectType_MetadataTemplate_Builder_addAllRecordFields_java_lang_Iterable___extends_com_google_cloud_dataplex_v1_AspectType_MetadataTemplate__)(aspectFields)
                          .build())
                  .build();
          return client.[createAspectTypeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html#com_google_cloud_dataplex_v1_CatalogServiceClient_createAspectTypeAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_LocationName_com_google_cloud_dataplex_v1_AspectType_java_lang_String_)(locationName, aspectType, aspectTypeId).get();
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    # Method to create Aspect Type located in project_id, location and with aspect_type_id and
    # aspect_fields specifying schema of the Aspect Type
    def create_aspect_type(
        project_id: str,
        location: str,
        aspect_type_id: str,
        aspect_fields: List[[dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[AspectType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.html).[MetadataTemplate](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.html)],
    ) -> dataplex_v1.AspectType:
        """Method to create Aspect Type located in project_id, location and with aspect_type_id and
        aspect_fields specifying schema of the Aspect Type"""
    
        # Initialize client that will be used to send requests across threads. This
        # client only needs to be created once, and can be reused for multiple requests.
        # After completing all of your requests, call the "__exit__()" method to safely
        # clean up any remaining background resources. Alternatively, use the client as
        # a context manager.
        with [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)() as client:
            # The resource name of the Aspect Type location
            parent = f"projects/{project_id}/locations/{location}"
            aspect_type = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[AspectType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.html)(
                description="description of the aspect type",
                metadata_template=[dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[AspectType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.html).[MetadataTemplate](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.html)(
                    # The name must follow regex ^(([a-zA-Z]{1})([\\w\\-_]{0,62}))$
                    # That means name must only contain alphanumeric character or dashes or underscores,
                    # start with an alphabet, and must be less than 63 characters.
                    name="name_of_the_template",
                    type="record",
                    # Aspect Type fields, that themselves are Metadata Templates.
                    record_fields=aspect_fields,
                ),
            )
            create_operation = client.create_aspect_type(
                parent=parent, aspect_type=aspect_type, aspect_type_id=aspect_type_id
            )
            return create_operation.result(60)
    
    
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
                description="description of the field"
            ),
            constraints=[dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[AspectType](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.html).[MetadataTemplate](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.html).[Constraints](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.Constraints.html)(
                # Specifies if field will be required in Aspect Type.
                required=True
            ),
        )
        aspect_fields = [aspect_field]
    
        created_aspect_type = create_aspect_type(
            project_id, location, aspect_type_id, aspect_fields
        )
        print(f"Successfully created aspect type: {created_aspect_type.name}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=dataplex). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
