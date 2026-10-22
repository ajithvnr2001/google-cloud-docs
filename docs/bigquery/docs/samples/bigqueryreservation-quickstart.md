---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-quickstart/
title: Report capacity commitments and reservations \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:31.237895+00:00
---

# Report capacity commitments and reservations  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigqueryreservation-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Report capacity commitments and reservations Stay organized with collections  Save and categorize content based on your preferences. 

List all capacity commitments and reservations in a particular project and location. Print the results to the Cloud Console.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [BigQuery Reservation API Client Libraries](https://docs.cloud.google.com/bigquery/docs/reference/reservations)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Go API reference documentation](https://godoc.org/cloud.google.com/go/bigquery). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    // The bigquery_reservation_quickstart application demonstrates usage of the
    // BigQuery reservation API by enumerating some of the resources that can be
    // associated with a cloud project.
    package main
    
    import (
    	"bytes"
    	"context"
    	"flag"
    	"fmt"
    	"log"
    
    	reservation "cloud.google.com/go/bigquery/reservation/apiv1"
    	"cloud.google.com/go/bigquery/reservation/apiv1/reservationpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    
    	// Define two command line flags for controlling the behavior of this quickstart.
    	var (
    		projectID = flag.String("project_id", "", "Cloud Project ID, used for session creation.")
    		location  = flag.String("location", "US", "BigQuery location used for interactions.")
    	)
    	// Parse flags and do some minimal validation.
    	flag.Parse()
    	if *projectID == "" {
    		log.Fatal("empty --project_id specified, please provide a valid project ID")
    	}
    	if *location == "" {
    		log.Fatal("empty --location specified, please provide a valid location")
    	}
    
    	ctx := context.Background()
    	bqResClient, err := reservation.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/reservation/apiv1.html#cloud_google_com_go_bigquery_reservation_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("NewClient: %v", err)
    	}
    	defer bqResClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/reservation/apiv1.html#cloud_google_com_go_bigquery_reservation_apiv1_Client_Close)()
    
    	s, err := reportCapacityCommitments(ctx, bqResClient, *projectID, *location)
    	if err != nil {
    		log.Fatalf("printCapacityCommitments: %v", err)
    	}
    	fmt.Println(s)
    
    	s, err = reportReservations(ctx, bqResClient, *projectID, *location)
    	if err != nil {
    		log.Fatalf("printReservations: %v", err)
    	}
    	fmt.Println(s)
    }
    
    // printCapacityCommitments iterates through the capacity commitments and returns a byte buffer with details.
    func reportCapacityCommitments(ctx context.Context, client *reservation.[Client](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/reservation/apiv1.html#cloud_google_com_go_bigquery_reservation_apiv1_Client), projectID, location string) (string, error) {
    	var buf bytes.Buffer
    	fmt.Fprintf(&buf, "Capacity commitments in project %s in location %s:\n", projectID, location)
    
    	req := &reservationpb.ListCapacityCommitmentsRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    	}
    	totalCommitments := 0
    	it := client.ListCapacityCommitments(ctx, req)
    	for {
    		commitment, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return "", err
    		}
    		fmt.Fprintf(&buf, "\tCommitment %s in state %s\n", commitment.GetName(), commitment.GetState().String())
    		totalCommitments++
    	}
    	fmt.Fprintf(&buf, "\n%d commitments processed.\n", totalCommitments)
    	return buf.String(), nil
    }
    
    // printReservations iterates through reservations defined in an admin project.
    func reportReservations(ctx context.Context, client *reservation.[Client](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigquery/latest/reservation/apiv1.html#cloud_google_com_go_bigquery_reservation_apiv1_Client), projectID, location string) (string, error) {
    	var buf bytes.Buffer
    	fmt.Fprintf(&buf, "Reservations in project %s in location %s:\n", projectID, location)
    
    	req := &reservationpb.ListReservationsRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    	}
    	totalReservations := 0
    	it := client.ListReservations(ctx, req)
    	for {
    		reservation, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return "", err
    		}
    		fmt.Fprintf(&buf, "\tReservation %s has %d slot capacity.\n", reservation.GetName(), reservation.GetSlotCapacity())
    		totalReservations++
    	}
    	fmt.Fprintf(&buf, "\n%d reservations processed.\n", totalReservations)
    	return buf.String(), nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.bigquery.reservation.v1.[ReservationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationServiceClient.html);
    import java.io.IOException;
    
    public class QuickstartSample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR_PROJECT_ID";
        String location = "LOCATION";
        quickStartSample(projectId, location);
      }
    
      public static void quickStartSample(String projectId, String location) throws IOException {
        try ([ReservationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationServiceClient.html) client = [ReservationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigqueryreservation/latest/com.google.cloud.bigquery.reservation.v1.ReservationServiceClient.html).create()) {
          // list reservations in the project
          String parent = String.format("projects/%s/locations/%s", projectId, location);
          client
              .listReservations(parent)
              .iterateAll()
              .forEach(res -> System.out.println("Reservation resource name: " + res.getName()));
    
          // list capacity commitments in the project
          client
              .listCapacityCommitments(parent)
              .iterateAll()
              .forEach(
                  commitment ->
                      System.out.println("Capacity commitment resource name: " + commitment.getName()));
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Node.js API reference documentation](https://googleapis.dev/nodejs/bigquery/latest/index.html). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    // Imports the Google Cloud client library
    const {
      ReservationServiceClient,
    } = require('[@google-cloud/bigquery-reservation](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)');
    
    // Creates a client
    const client = new [ReservationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)();
    
    // project = 'my-project' // Project to list reservations for.
    // location = 'US' // BigQuery location.
    
    async function listReservations() {
      const [reservations] = await client.listReservations({
        parent: `projects/${project}/locations/${location}`,
      });
    
      console.info(`found ${reservations.length} reservations`);
      console.info(reservations);
    }
    
    async function listCapacityCommitments() {
      const [commitments] = await client.listCapacityCommitments({
        parent: `projects/${project}/locations/${location}`,
      });
    
      console.info(`found ${commitments.length} commitments`);
      console.info(commitments);
    }
    
    listReservations();
    listCapacityCommitments();

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import argparse
    
    from google.cloud import [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest)
    
    
    def main(
        project_id: str = "your-project-id", location: str = "US", transport: str = "grpc"
    ) -> None:
        # Constructs the client for interacting with the service.
        client = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[ReservationServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html)(transport=transport)
    
        report_reservations(client, project_id, location)
    
    
    def report_reservations(
        client: [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[ReservationServiceClient](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html),
        project_id: str,
        location: str,
    ) -> None:
        """Prints details and summary information about reservations defined within
        a given admin project and location.
        """
        print("Reservations in project {} in location {}".format(project_id, location))
        req = [bigquery_reservation_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest).[ListReservationsRequest](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.types.ListReservationsRequest.html)(
            parent=client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_common_location_path)(project_id, location)
        )
        total_reservations = 0
        for reservation in client.[list_reservations](https://docs.cloud.google.com/python/docs/reference/bigqueryreservation/latest/google.cloud.bigquery_reservation_v1.services.reservation_service.ReservationServiceClient.html#google_cloud_bigquery_reservation_v1_services_reservation_service_ReservationServiceClient_list_reservations)(request=req):
            print(
                f"\tReservation {reservation.name} "
                f"has {reservation.slot_capacity} slot capacity."
            )
            total_reservations = total_reservations + 1
        print(f"\n{total_reservations} reservations processed.")
    
    
    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--project_id", type=str)
        parser.add_argument("--location", default="US", type=str)
        args = parser.parse_args()
        main(project_id=args.project_id, location=args.location)
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
