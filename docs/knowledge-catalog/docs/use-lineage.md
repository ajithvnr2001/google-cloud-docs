---
url: https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage/
title: View data lineage for Google Cloud systems \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:03.045688+00:00
---

# View data lineage for Google Cloud systems  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  View data lineage for Google Cloud systems Stay organized with collections  Save and categorize content based on your preferences. 

View data lineage to understand the relationships between your project's resources and the processes that created them. These relationships show how data assets, such as tables and datasets, are transformed by processes like queries and pipelines. This guide describes how to view data lineage details in the Google Cloud console or retrieve them by using the Data Lineage API.

## Roles and permissions

Data lineage tracks lineage information automatically when you enable the [Data Lineage API](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest). You don't need any administrator or editor roles to capture lineage for your data assets.

To view data lineage, you need specific Identity and Access Management (IAM) permissions. Lineage information is captured across projects, so you need permissions in multiple projects.

  * When viewing lineage in Knowledge Catalog, BigQuery, or Vertex AI: you need permissions to view lineage information in the project where you are viewing it.

  * When viewing lineage that was recorded in other projects: you need permissions to view lineage information in those projects where it was recorded.




To get the permissions that you need to view data lineage, ask your administrator to grant you the following IAM roles: 

  * All: [**Data Lineage Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer) (`roles/datalineage.viewer`) on the project where lineage is recorded, and the project where lineage is viewed 
  * View BigQuery table details: [**BigQuery Metadata Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.metadataViewer) (`roles/bigquery.metadataViewer`) on the table's storage project 
  * View BigQuery job details: [**BigQuery Resource Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.resourceViewer) (`roles/bigquery.resourceViewer`) on the job's compute project 
  * View details for other cataloged assets: [**Dataplex Catalog Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) on the project where catalog entries are stored 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view data lineage. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view data lineage:

  * View BigQuery table details: `bigquery.tables.get` \- the table's storage project 
  * View BigQuery job details: `bigquery.jobs.get` \- the job's compute project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Types of data lineage views

You can view lineage information as an interactive graph or a structured list in the Google Cloud console.

For a detailed description of the graph elements (such as nodes, edges, process icons, and labels) and the columns available in the list views, see [About data lineage visualization in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views).

## Enable data lineage

**Caution:** Data lineage is enabled on a per-project basis, not a per-service basis. After you enable the Data Lineage API, lineage information is automatically reported for multiple Google Cloud services in the project, depending on their product-level lineage control. For more details, see [Data lineage considerations and limitations](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage#lineage-considerations). 

Enable data lineage to begin automatically tracking lineage information for supported systems. By default, enabling the API activates lineage tracking for most supported services. For more information, see [Automated data lineage tracking](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage#lineage-supported-systems) and [About data lineage ingestion control](https://docs.cloud.google.com/knowledge-catalog/docs/control-lineage-ingestion).

The Data Lineage API is billed under the Knowledge Catalog Premium Processing SKU. For more information, see [Knowledge Catalog pricing](https://cloud.google.com/products/knowledge-catalog/pricing).

You must enable the Data Lineage API in both the project where you view lineage and the projects where lineage is recorded. For more information, see [Project types](https://docs.cloud.google.com/knowledge-catalog/docs/troubleshooting-lineage#project_types).

  1. To capture lineage information, complete the following steps: 
     1. In the Google Cloud console, on the **Project selector** page, select the project where you want to record lineage.

[Go to Project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     2. Enable the Data Lineage API.

[Enable API](https://console.cloud.google.com/apis/enableflow?apiid=datalineage.googleapis.com)

     3. Repeat the previous steps for each project where you want to record lineage.
  2. In the project where you view lineage, enable the Data Lineage API and the Dataplex API.

[Enable APIs](https://console.cloud.google.com/apis/enableflow?apiid=datalineage.googleapis.com,dataplex.googleapis.com)




## Control lineage ingestion for a service

You can selectively enable or disable automatic lineage tracking for specific services at the project, folder, or organization level.

For details about how these configurations are applied hierarchically through the resource tree, see [About data lineage ingestion control](https://docs.cloud.google.com/knowledge-catalog/docs/control-lineage-ingestion).

## View lineage

**Note:** The primary and recommended way to retrieve lineage programmatically is using the preview `searchLineageStreaming` API. For more information and examples, see [Search multi-region lineage using server-side automation](https://docs.cloud.google.com/knowledge-catalog/docs/search-lineage-streaming-api). The following tabbed API examples demonstrate manual, client-side graph traversal.

To track how data is transformed and moves across systems, you can view data lineage using the Google Cloud console or the API.

### Console

**Note:** Depending on the volume of data being processed, it takes time for data lineage to display a graph. For most jobs, it takes three hours, and for some jobs it can take up to 24 hours.

You can access data lineage information in the Google Cloud console from various starting points:

  * **Knowledge Catalog:** Go to the Knowledge Catalog **Search** page, select **Knowledge Catalog** as the search mode, search for the entry you want to view, and then click it. For more information, see [Search for data assets in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets).
  * **BigQuery:** Go to the **BigQuery** page and open the table for which you want to see the data lineage.
  * **Vertex AI:** Go to the **Datasets** or **Model Registry** page, and click the dataset or model for which you want to see the data lineage.



To view the lineage graph, follow these steps:

  1. Click the **Lineage** tab.

The default **Graph** view opens, showing table-level lineage across systems and regions. For more information, see [Lineage graph view](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views#lineage-graph-view).

  2. To manually explore the lineage graph, click **Expand** next to a node to load five more nodes at a time.

For more information, see [Explore the lineage graph](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views#lineage-manual-exploration).

  3. Click a node in the **Graph** view.

The **Details** panel opens with information about the asset, such as fully qualified name and type. For more information, see [View lineage node details](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views#lineage-node-details).

**Note:** Systems like Vertex AI Pipelines generate lineage data for Vertex AI models and datasets. For these assets, you can click **Open in Vertex AI** in the **Details** panel to view the lineage graph details directly in Vertex AI.
  4. Click an edge with a process icon in the **Graph** view.

The **Query** panel opens. For more information, see [Inspect transformation logic](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views#lineage-inspect-logic) and [Audit and history of runs](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views#lineage-audit-runs).

     * To inspect transformation logic, click the **Details** tab.
     * To see audit and history of runs, click the **Runs** tab.
**Note:** On the lineage graph, the ![Vertex AI lineage
icon](https://docs.cloud.google.com/static/knowledge-catalog/images/vertex-lineage-icon.png) appears before Vertex AI processes (like components and templates). If a process is cataloged in Knowledge Catalog with a fully qualified domain name (FQN), you can click it to view its details, or click **Open in Vertex AI** in the **Details** panel to view the graph in Vertex AI. To view the lineage of deeper operations—like training data, test data, or hyperparameters applied—see [Track the lineage of pipeline artifacts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/lineage).
  5. In the **Lineage explorer** panel, select filter criteria—for example, **Direction** , **Dependency type** , or **Time range** —and then click **Apply**.

This opens a focused view within a specific region (Preview). This view automatically expands the graph up to three levels of nodes. For more information, see [Filter and highlight data lineage views](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views#lineage-filtered-view).

  6. In the focused **Graph** view, select a node, and then in the node's details panel, click **Visualize Path** to visualize the lineage path from the selected node back to the root entry (only in focused view).

For more information, see [Visualize a data lineage path](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views#visualize-path).

  7. To view column-level lineage (only for BigQuery and Managed Service for Apache Spark jobs), do one of the following:

     * In a focused **Graph** view, click the column icon on a table. ![Icon used to switch to column-level lineage.](https://docs.cloud.google.com/static/knowledge-catalog/images/column-icon.png)Column icon
     * In the **Lineage explorer** panel, filter by column name, and click **Apply**.

For more information, see [When to use column-level lineage](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views#column-level-lineage).

  8. Click restart_alt **Reset**.

This action removes all applied filters and takes you to the beginning of the graph view.

  9. Click **List** to switch to the list view.

The **List** view offers simplified and detailed tabular representations of lineage for both table-level and column-level lineage, synchronized with the **Graph** view. By default, simplified list view is displayed, and you can toggle to detailed list view for analyzing individual source-target relationships. You can configure which columns are displayed and export lineage data. For more information, see [Lineage list view](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-views#lineage-list-view).




### Java
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.datacatalog.lineage.v1.[BatchSearchLinkProcessesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.BatchSearchLinkProcessesRequest.html);
    import com.google.cloud.datacatalog.lineage.v1.[EntityReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.EntityReference.html);
    import com.google.cloud.datacatalog.lineage.v1.[EventLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.EventLink.html);
    import com.google.cloud.datacatalog.lineage.v1.[LineageClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.html);
    import com.google.cloud.datacatalog.lineage.v1.[LineageEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageEvent.html);
    import com.google.cloud.datacatalog.lineage.v1.[Link](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.Link.html);
    import com.google.cloud.datacatalog.lineage.v1.[ListLineageEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ListLineageEventsRequest.html);
    import com.google.cloud.datacatalog.lineage.v1.[ListRunsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ListRunsRequest.html);
    import com.google.cloud.datacatalog.lineage.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LocationName.html);
    import com.google.cloud.datacatalog.lineage.v1.[ProcessLinks](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ProcessLinks.html);
    import com.google.cloud.datacatalog.lineage.v1.[Run](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.Run.html);
    import com.google.cloud.datacatalog.lineage.v1.[SearchLinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLinksRequest.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.HashSet;
    import java.util.LinkedList;
    import java.util.List;
    import java.util.Queue;
    import java.util.Set;
    
    public class ViewLineageExample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us";
        String targetFullyQualifiedName = "bigquery:my-project-id.my_dataset.my_table";
        int maxDepth = 3;
    
        viewLineage(projectId, location, targetFullyQualifiedName, maxDepth);
      }
    
      static class Node {
        String fqn;
        int depth;
        Node(String fqn, int depth) {
          this.fqn = fqn;
          this.depth = depth;
        }
      }
    
      public static void viewLineage(
          String projectId, String location, String targetFullyQualifiedName, int maxDepth)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs
        // to be created once, and can be reused for multiple requests.
        try ([LineageClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.html) client = [LineageClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.html).create()) {
          String parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LocationName.html).of(projectId, location).toString();
    
          Set<String> visitedNodes = new HashSet<>();
          Queue<Node> queue = new LinkedList<>();
    
          visitedNodes.[add](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.RequestParamsBuilder.html#com_google_api_gax_rpc_RequestParamsBuilder_add_java_lang_String_java_lang_String_)(targetFullyQualifiedName);
          queue.offer(new Node(targetFullyQualifiedName, 0));
    
          while (!queue.[isEmpty](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LibraryMetadata.html#com_google_api_gax_rpc_LibraryMetadata_isEmpty__)()) {
            Node current = queue.poll();
            System.out.printf("\nExploring node (Depth %d): %s\n", current.depth, current.fqn);
    
            if (current.depth >= maxDepth) {
              continue;
            }
    
            [EntityReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.EntityReference.html) targetEntity =
                [EntityReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.EntityReference.html).newBuilder().[setFullyQualifiedName](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.EntityReference.Builder.html#com_google_cloud_datacatalog_lineage_v1_EntityReference_Builder_setFullyQualifiedName_java_lang_String_)(current.fqn).build();
            [SearchLinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLinksRequest.html) searchLinksRequest =
                [SearchLinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLinksRequest.html).newBuilder().setParent(parent).setTarget(targetEntity).build();
    
            List<String> linkNames = new ArrayList<>();
            try {
              // 1. Search for links related to the target entity
              for ([Link](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.Link.html) link : client.searchLinks(searchLinksRequest).iterateAll()) {
                linkNames.[add](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.RequestParamsBuilder.html#com_google_api_gax_rpc_RequestParamsBuilder_add_java_lang_String_java_lang_String_)(link.getName());
              }
            } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
              System.out.printf("  Failed to retrieve links for %s: %s\n", current.fqn, e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
              continue;
            }
    
            if (linkNames.[isEmpty](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LibraryMetadata.html#com_google_api_gax_rpc_LibraryMetadata_isEmpty__)()) {
              continue;
            }
    
            // 2. Batch search for processes in chunks of 100
            for (int i = 0; i < linkNames.size(); i += 100) {
              List<String> batch = linkNames.subList(i, Math.min(linkNames.size(), i + 100));
              [BatchSearchLinkProcessesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.BatchSearchLinkProcessesRequest.html) batchSearchRequest =
                  [BatchSearchLinkProcessesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.BatchSearchLinkProcessesRequest.html).newBuilder()
                      .setParent(parent)
                      .addAllLinks(batch)
                      .build();
    
              try {
                for ([ProcessLinks](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ProcessLinks.html) processLinks :
                    client.batchSearchLinkProcesses(batchSearchRequest).iterateAll()) {
                  String processName = processLinks.getProcess();
                  System.out.printf("  Process: %s\n", processName);
    
                  // 3. List runs for the process
                  [ListRunsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ListRunsRequest.html) runsRequest =
                      [ListRunsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ListRunsRequest.html).newBuilder().setParent(processName).build();
                  for ([Run](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.Run.html) run : client.listRuns(runsRequest).iterateAll()) {
                    System.out.printf("    Run: %s\n", [run](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.Watchdog.html#com_google_api_gax_rpc_Watchdog_run__).getName());
    
                    // 4. List events for the run
                    [ListLineageEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ListLineageEventsRequest.html) eventsRequest =
                        [ListLineageEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ListLineageEventsRequest.html).newBuilder().setParent([run](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.Watchdog.html#com_google_api_gax_rpc_Watchdog_run__).getName()).build();
                    for ([LineageEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageEvent.html) event : client.listLineageEvents(eventsRequest).iterateAll()) {
                      for ([EventLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.EventLink.html) eventLink : event.getLinksList()) {
                        String sourceFqn = eventLink.getSource().getFullyQualifiedName();
                        // If exploring upstream, queue the source
                        if (!sourceFqn.isEmpty() && !visitedNodes.contains(sourceFqn)) {
                          visitedNodes.[add](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.RequestParamsBuilder.html#com_google_api_gax_rpc_RequestParamsBuilder_add_java_lang_String_java_lang_String_)(sourceFqn);
                          queue.offer(new Node(sourceFqn, current.depth + 1));
                        }
                      }
                    }
                  }
                }
              } catch ([ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) e) {
                System.out.printf("  Failed to retrieve processes/runs: %s\n", e.[getMessage](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.html#com_google_api_gax_rpc_ErrorDetails__T_getMessage_java_lang_Class_T__)());
              }
            }
          }
        }
      }
    }
    

### Python
    
    
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    from google.api_core.exceptions import GoogleAPICallError
    
    def view_lineage(project_id: str, location: str, target_fully_qualified_name: str, max_depth: int = 3):
        """Retrieves lineage for a given entity using a depth-limited search."""
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
        parent = f"projects/{project_id}/locations/{location}"
    
        # Store visited nodes to avoid infinite loops in cyclic graphs
        visited_nodes = set([target_fully_qualified_name])
        queue = [(target_fully_qualified_name, 0)]
    
        while queue:
            current_node, current_depth = queue.pop(0)
            print(f"\nExploring node (Depth {current_depth}): {current_node}")
    
            if current_depth >= max_depth:
                continue
    
            target_entity = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[EntityReference](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.EntityReference.html)(
                fully_qualified_name=current_node
            )
            search_links_request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[SearchLinksRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.SearchLinksRequest.html)(
                parent=parent,
                target=target_entity,
            )
    
            try:
                links = list(client.[search_links](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_search_links)(request=search_links_request))
            except GoogleAPICallError as e:
                print(f"  Failed to retrieve links for {current_node}: {e.message}")
                continue
    
            if not links:
                continue
    
            # Extract link names to query processes in batches
            link_names = [link.name for link in links]
    
            # Batch max size is 100
            for i in range(0, len(link_names), 100):
                batch = link_names[i:i + 100]
                batch_request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[BatchSearchLinkProcessesRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.BatchSearchLinkProcessesRequest.html)(
                    parent=parent,
                    links=batch
                )
    
                try:
                    for process_links in client.[batch_search_link_processes](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_batch_search_link_processes)(request=batch_request):
                        process_name = process_links.process
                        print(f"  Process: {process_name}")
    
                        runs_request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[ListRunsRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.ListRunsRequest.html)(parent=process_name)
                        for run in client.[list_runs](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_list_runs)(request=runs_request):
                            print(f"    Run: {run.name}")
    
                            events_request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[ListLineageEventsRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.ListLineageEventsRequest.html)(parent=run.name)
                            for event in client.[list_lineage_events](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_list_lineage_events)(request=events_request):
                                for event_link in event.links:
                                    source_fqn = event_link.source.fully_qualified_name
    
                                    # If exploring upstream, queue the source
                                    if source_fqn and source_fqn not in visited_nodes:
                                        visited_nodes.add(source_fqn)
                                        queue.append((source_fqn, current_depth + 1))
    
                except GoogleAPICallError as e:
                     print(f"  Failed to retrieve processes/runs: {e.message}")
    

## Refine the lineage visualization

To refine the lineage visualization, you can use highlighting and filtering options in **Lineage explorer** :

  1. To search for specific projects, datasets, or entity names, use the **Filters** panel.

After you apply filters, lineage nodes that match your filter criteria are considered matching nodes. You can refine how matching and non-matching nodes are displayed.

  2. In the lineage graph, click the **More actions** more_vert icon located next to the **Clear filters** button to see display options.

  3. Select one or both of the following options:


[ ![Highlight and filter options in lineage explorer.](https://docs.cloud.google.com/static/knowledge-catalog/images/filters%20and%20highlights.png)](https://docs.cloud.google.com/static/knowledge-catalog/images/filters%20and%20highlights.png) Highlight and filter options.

You can select both options at the same time. If both options are selected, unfiltered nodes are hidden, and matching nodes are highlighted in the filtered graph view.

## Turn off data lineage

To stop tracking lineage and avoid data lineage charges, disable the Data Lineage API (`datalineage.googleapis.com`) in each project where it is enabled.

Disabling the Dataplex API does not turn off data lineage or stop its charges. You must disable the Data Lineage API.

To turn off data lineage, select one of the following tabs and complete the steps for each project where lineage tracking was enabled:

### Console

  1. In the Google Cloud console, go to the **Enabled APIs & services** page.

[Go to Enabled APIs & services](https://console.cloud.google.com/apis/dashboard)

  2. In the list of APIs, click **Data Lineage API**.

  3. Click **Disable API**.

[ ![Disable API button on the Data Lineage API details page.](https://docs.cloud.google.com/static/knowledge-catalog/images/disable-api.png)](https://docs.cloud.google.com/static/knowledge-catalog/images/disable-api.png) Disable API button on the Data Lineage API details page.
  4. When prompted, click **Disable**.




###  gcloud 

To disable the Data Lineage API, use the [`gcloud services disable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/disable) command:
    
    
    gcloud services disable datalineage.googleapis.com --project=PROJECT_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project



If you want to stop lineage tracking for specific services without disabling the API completely, see [Configure data lineage ingestion for a service](https://docs.cloud.google.com/knowledge-catalog/docs/configure-lineage-ingestion).

## What's next

  * [Track data lineage for a BigQuery table](https://docs.cloud.google.com/knowledge-catalog/docs/track-lineage-quickstart).
  * Learn about the [data lineage information model](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage#information-model).
  * Learn about [data lineage considerations and limitations](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage#lineage-considerations).
  * Learn about [Data Lineage API audit logging](https://docs.cloud.google.com/knowledge-catalog/docs/lineage-audit-logging).
  * [Troubleshoot data lineage issues](https://docs.cloud.google.com/knowledge-catalog/docs/troubleshooting-lineage).
  * [Integrate with OpenLineage](https://docs.cloud.google.com/knowledge-catalog/docs/open-lineage).
  * [Use data lineage with Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/guides/data-lineage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
