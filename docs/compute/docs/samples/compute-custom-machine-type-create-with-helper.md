---
url: https://docs.cloud.google.com/compute/docs/samples/compute-custom-machine-type-create-with-helper/
title: Create a VM with a custom machine type \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:47.488001+00:00
---

# Create a VM with a custom machine type  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-custom-machine-type-create-with-helper/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a VM with a custom machine type Stay organized with collections  Save and categorize content based on your preferences. 

Create a VM with the specified number of vCPUs and the specified amount of memory.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a VM with a custom machine type](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    func customMachineTypeURI(zone, cpuSeries string, coreCount, memory int) (string, error) {
    	const (
    		n1       = "custom"
    		n2       = "n2-custom"
    		n2d      = "n2d-custom"
    		e2       = "e2-custom"
    		e2Micro  = "e2-custom-micro"
    		e2Small  = "e2-custom-small"
    		e2Medium = "e2-custom-medium"
    	)
    
    	type typeLimit struct {
    		allowedCores     []int
    		minMemPerCore    int
    		maxMemPerCore    int
    		allowExtraMemory bool
    		extraMemoryLimit int
    	}
    
    	makeRange := func(start, end, step int) []int {
    		if step <= 0 || end < start {
    			return []int{}
    		}
    		s := make([]int, 0, 1+(end-start)/step)
    		for start <= end {
    			s = append(s, start)
    			start += step
    		}
    		return s
    	}
    
    	containsString := func(s []string, str string) bool {
    		for _, v := range s {
    			if v == str {
    				return true
    			}
    		}
    
    		return false
    	}
    
    	containsInt := func(nums []int, n int) bool {
    		for _, v := range nums {
    			if v == n {
    				return true
    			}
    		}
    
    		return false
    	}
    
    	var (
    		cpuSeriesE2Limit = typeLimit{
    			allowedCores:  makeRange(2, 33, 2),
    			minMemPerCore: 512,
    			maxMemPerCore: 8192,
    		}
    		cpuSeriesE2MicroLimit  = typeLimit{minMemPerCore: 1024, maxMemPerCore: 2048}
    		cpuSeriesE2SmallLimit  = typeLimit{minMemPerCore: 2048, maxMemPerCore: 4096}
    		cpuSeriesE2MeidumLimit = typeLimit{minMemPerCore: 4096, maxMemPerCore: 8192}
    		cpuSeriesN2Limit       = typeLimit{
    			allowedCores:  append(makeRange(2, 33, 2), makeRange(36, 129, 4)...),
    			minMemPerCore: 512, maxMemPerCore: 8192,
    			allowExtraMemory: true,
    			extraMemoryLimit: 624 << 10,
    		}
    		cpuSeriesN2DLimit = typeLimit{
    			allowedCores:  []int{2, 4, 8, 16, 32, 48, 64, 80, 96},
    			minMemPerCore: 512, maxMemPerCore: 8192,
    			allowExtraMemory: true,
    			extraMemoryLimit: 768 << 10,
    		}
    		cpuSeriesN1Limit = typeLimit{
    			allowedCores:     append([]int{1}, makeRange(2, 97, 2)...),
    			minMemPerCore:    922,
    			maxMemPerCore:    6656,
    			allowExtraMemory: true,
    			extraMemoryLimit: 624 << 10,
    		}
    	)
    
    	typeLimitsMap := map[string]typeLimit{
    		n1:       cpuSeriesN1Limit,
    		n2:       cpuSeriesN2Limit,
    		n2d:      cpuSeriesN2DLimit,
    		e2:       cpuSeriesE2Limit,
    		e2Micro:  cpuSeriesE2MicroLimit,
    		e2Small:  cpuSeriesE2SmallLimit,
    		e2Medium: cpuSeriesE2MeidumLimit,
    	}
    
    	if !containsString([]string{e2, n1, n2, n2d}, cpuSeries) {
    		return "", fmt.Errorf("incorrect cpu type: %v", cpuSeries)
    	}
    
    	tl := typeLimitsMap[cpuSeries]
    
    	// Check whether the requested parameters are allowed.
    	// Find more information about limitations of custom machine types at:
    	// https://cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types
    
    	// Check the number of cores
    	if len(tl.allowedCores) > 0 && !containsInt(tl.allowedCores, coreCount) {
    		return "", fmt.Errorf(
    			"invalid number of cores requested. Allowed number of cores for %v is: %v",
    			cpuSeries,
    			tl.allowedCores,
    		)
    	}
    
    	// Memory must be a multiple of 256 MB
    	if memory%256 != 0 {
    		return "", fmt.Errorf("requested memory must be a multiple of 256 MB")
    	}
    
    	// Check if the requested memory isn't too little
    	if memory < coreCount*tl.minMemPerCore {
    		return "", fmt.Errorf(
    			"requested memory is too low. Minimal memory for %v is %v MB per core",
    			cpuSeries,
    			tl.minMemPerCore,
    		)
    	}
    
    	// Check if the requested memory isn't too much
    	if memory > coreCount*tl.maxMemPerCore && !tl.allowExtraMemory {
    		return "", fmt.Errorf(
    			"requested memory is too large.. Maximum memory allowed for %v is %v MB per core",
    			cpuSeries,
    			tl.maxMemPerCore,
    		)
    	}
    	if memory > tl.extraMemoryLimit && tl.allowExtraMemory {
    		return "", fmt.Errorf(
    			"requested memory is too large.. Maximum memory allowed for %v is %v MB",
    			cpuSeries,
    			tl.extraMemoryLimit,
    		)
    	}
    
    	// Return the custom machine type in form of a string acceptable by Compute Engine API.
    	if containsString([]string{e2Small, e2Micro, e2Medium}, cpuSeries) {
    		return fmt.Sprintf("zones/%v/machineTypes/%v-%v", zone, cpuSeries, memory), nil
    	}
    
    	if memory > coreCount*tl.maxMemPerCore {
    		return fmt.Sprintf(
    			"zones/%v/machineTypes/%v-%v-%v-ext",
    			zone,
    			cpuSeries,
    			coreCount,
    			memory,
    		), nil
    	}
    
    	return fmt.Sprintf("zones/%v/machineTypes/%v-%v-%v", zone, cpuSeries, coreCount, memory), nil
    }
    
    // createInstanceWithCustomMachineTypeWithHelper creates a new VM instance with a custom machine type.
    func createInstanceWithCustomMachineTypeWithHelper(
    	w io.Writer,
    	projectID, zone, instanceName, cpuSeries string,
    	coreCount, memory int,
    ) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// cpuSeries := "e2-custom-micro" // the type of CPU you want to use"
    	// coreCount := 2 // number of CPU cores you want to use.
    	// memory := 256 // the amount of memory for the VM instance, in megabytes.
    
    	machineType, err := customMachineTypeURI(zone, cpuSeries, coreCount, memory)
    	if err != nil {
    		return fmt.Errorf("unable to create custom machine type string: %w", err)
    	}
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	req := &computepb.InsertInstanceRequest{
    		Project: projectID,
    		Zone:    zone,
    		InstanceResource: &computepb.Instance{
    			Name: proto.String(instanceName),
    			Disks: []*computepb.AttachedDisk{
    				{
    					InitializeParams: &computepb.AttachedDiskInitializeParams{
    						DiskSizeGb: proto.Int64(10),
    						SourceImage: proto.String(
    							"projects/debian-cloud/global/images/family/debian-12",
    						),
    					},
    					AutoDelete: proto.Bool(true),
    					Boot:       proto.Bool(true),
    				},
    			},
    			MachineType: proto.String(machineType),
    			NetworkInterfaces: []*computepb.NetworkInterface{
    				{
    					Name: proto.String("global/networks/default"),
    				},
    			},
    		},
    	}
    
    	op, err := instancesClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create instance: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance created\n")
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html);
    import com.google.cloud.compute.v1.[AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html);
    import com.google.cloud.compute.v1.[InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.common.collect.ImmutableMap;
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.Collections;
    import java.util.Map;
    import java.util.Objects;
    import java.util.concurrent.ConcurrentHashMap;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    import java.util.stream.IntStream;
    
    public class CreateWithHelper {
    
      // This class defines the configurable parameters for a custom VM.
      static final class TypeLimits {
    
        int[] allowedCores;
        int minMemPerCore;
        int maxMemPerCore;
        int extraMemoryLimit;
        boolean allowExtraMemory;
    
        TypeLimits(int[] allowedCores, int minMemPerCore, int maxMemPerCore, boolean allowExtraMemory,
            int extraMemoryLimit) {
          this.allowedCores = allowedCores;
          this.minMemPerCore = minMemPerCore;
          this.maxMemPerCore = maxMemPerCore;
          this.allowExtraMemory = allowExtraMemory;
          this.extraMemoryLimit = extraMemoryLimit;
        }
      }
    
      public enum CpuSeries {
        N1("custom"),
        N2("n2-custom"),
        N2D("n2d-custom"),
        E2("e2-custom"),
        E2_MICRO("e2-custom-micro"),
        E2_SMALL("e2-custom-small"),
        E2_MEDIUM("e2-custom-medium");
    
        private static final Map<String, CpuSeries> ENUM_MAP;
    
        static {
          ENUM_MAP = init();
        }
    
        // Build an immutable map of String name to enum pairs.
        public static Map<String, CpuSeries> init() {
          Map<String, CpuSeries> map = new ConcurrentHashMap<>();
          for (CpuSeries instance : CpuSeries.values()) {
            map.put(instance.getCpuSeries(), instance);
          }
          return Collections.unmodifiableMap(map);
        }
    
        private final String cpuSeries;
    
        CpuSeries(String cpuSeries) {
          this.cpuSeries = cpuSeries;
        }
    
        public static CpuSeries get(String name) {
          return ENUM_MAP.get(name);
        }
    
        public String getCpuSeries() {
          return this.cpuSeries;
        }
      }
    
      // This enum correlates a machine type with its limits.
      // The limits for various CPU types are described in:
      // https://cloud.google.com/compute/docs/general-purpose-machines
      enum Limits {
        CPUSeries_E2(new TypeLimits(getNumsInRangeWithStep(2, 33, 2), 512, 8192, false, 0)),
        CPUSeries_E2MICRO(new TypeLimits(new int[]{}, 1024, 2048, false, 0)),
        CPUSeries_E2SMALL(new TypeLimits(new int[]{}, 2048, 4096, false, 0)),
        CPUSeries_E2MEDIUM(new TypeLimits(new int[]{}, 4096, 8192, false, 0)),
        CPUSeries_N2(
            new TypeLimits(concat(getNumsInRangeWithStep(2, 33, 2), getNumsInRangeWithStep(36, 129, 4)),
                512, 8192, true, gbToMb(624))),
        CPUSeries_N2D(
            new TypeLimits(new int[]{2, 4, 8, 16, 32, 48, 64, 80, 96}, 512, 8192, true, gbToMb(768))),
        CPUSeries_N1(
            new TypeLimits(concat(new int[]{1}, getNumsInRangeWithStep(2, 97, 2)), 922, 6656, true,
                gbToMb(624)));
    
        private final TypeLimits typeLimits;
    
        Limits(TypeLimits typeLimits) {
          this.typeLimits = typeLimits;
        }
    
        public TypeLimits getTypeLimits() {
          return typeLimits;
        }
      }
    
      static ImmutableMap<String, Limits> typeLimitsMap = ImmutableMap.<String, Limits>builder()
          .put("N1", Limits.CPUSeries_N1)
          .put("N2", Limits.CPUSeries_N2)
          .put("N2D", Limits.CPUSeries_N2D)
          .put("E2", Limits.CPUSeries_E2)
          .put("E2_MICRO", Limits.CPUSeries_E2MICRO)
          .put("E2_SMALL", Limits.CPUSeries_E2SMALL)
          .put("E2_MEDIUM", Limits.CPUSeries_E2SMALL)
          .build();
    
      // Returns the array of integers within the given range, incremented by the specified step.
      // start (inclusive): starting number of the range
      // stop (inclusive): ending number of the range
      // step : increment value
      static int[] getNumsInRangeWithStep(int start, int stop, int step) {
        return IntStream.range(start, stop).filter(x -> (x - start) % step == 0).toArray();
      }
    
      static int gbToMb(int value) {
        return value << 10;
      }
    
      static int[] concat(int[] a, int[] b) {
        int[] result = new int[a.length + b.length];
        System.arraycopy(a, 0, result, 0, a.length);
        System.arraycopy(b, 0, result, a.length, b.length);
        return result;
      }
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "your-google-cloud-project-id";
        // Name of the zone to create the instance in. For example: "us-west3-b".
        String zone = "google-cloud-zone";
        // Name of the new virtual machine (VM) instance.
        String instanceName = "instance-name";
        String cpuSeries = "N1";
        // Number of CPU cores you want to use.
        int coreCount = 2;
        // The amount of memory for the VM instance, in megabytes.
        int memory = 256;
    
        createInstanceWithCustomMachineTypeWithHelper(
            projectId, zone, instanceName, cpuSeries, coreCount, memory);
      }
    
      // Create a VM instance with a custom machine type.
      public static void createInstanceWithCustomMachineTypeWithHelper(
          String project, String zone, String instanceName, String cpuSeries, int coreCount, int memory)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Construct the URI string identifying the machine type.
        String machineTypeUri = customMachineTypeUri(zone, cpuSeries, coreCount, memory);
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `instancesClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
    
          [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) attachedDisk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
              .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)(
                  // Describe the size and source image of the boot disk to attach to the instance.
                  // The list of public images available in Compute Engine can be found here:
                  // https://cloud.google.com/compute/docs/images#list_of_public_images_available_on
                  [AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                      .setSourceImage(
                          String.format("projects/%s/global/images/family/%s", "debian-cloud",
                              "debian-13"))
                      .setDiskSizeGb(10)
                      .build()
              )
              // Remember to set auto_delete to True if you want the disk to be deleted when you delete
              // your VM instance.
              .setAutoDelete(true)
              .setBoot(true)
              .build();
    
          // Create the Instance object with the relevant information.
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html).newBuilder()
              .setName(instanceName)
              .addDisks(attachedDisk)
              .setMachineType(machineTypeUri)
              .addNetworkInterfaces(
                  [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder().setName("global/networks/default").build())
              .build();
    
          // Create the insert instance request object.
          [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html) insertInstanceRequest = [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html).newBuilder()
              .setProject(project)
              .setZone(zone)
              .setInstanceResource(instance)
              .build();
    
          // Invoke the API with the request object and wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = instancesClient.insertAsync(insertInstanceRequest)
              .get(3, TimeUnit.MINUTES);
    
          // Check for errors.
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("Instance creation failed!!" + response);
          }
          System.out.printf("Instance created : %s", instanceName);
          System.out.println("Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    
      public static String customMachineTypeUri(String zone, String cpuSeries, int coreCount,
          int memory) {
    
        if (!Arrays.asList(CpuSeries.E2.cpuSeries, CpuSeries.N1.cpuSeries, CpuSeries.N2.cpuSeries,
            CpuSeries.N2D.cpuSeries).contains(cpuSeries)) {
          throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)(String.format("Incorrect cpu type: %s", cpuSeries));
        }
    
        TypeLimits typeLimit = Objects.requireNonNull(
            typeLimitsMap.get(CpuSeries.get(cpuSeries).name())).typeLimits;
    
        // Perform the following checks to verify if the requested parameters are allowed.
        // Find more information about limitations of custom machine types at:
        // https://cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types
    
        // 1. Check the number of cores and if the coreCount is present in allowedCores.
        if (typeLimit.allowedCores.length > 0 && Arrays.stream(typeLimit.allowedCores)
            .noneMatch(x -> x == coreCount)) {
          throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)(String.format(
              "Invalid number of cores requested. "
                  + "Number of cores requested for CPU %s should be one of: %s",
              cpuSeries,
              Arrays.toString(typeLimit.allowedCores)));
        }
    
        // 2. Memory must be a multiple of 256 MB
        if (memory % 256 != 0) {
          throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("Requested memory must be a multiple of 256 MB");
        }
    
        // 3. Check if the requested memory isn't too little
        if (memory < coreCount * typeLimit.minMemPerCore) {
          throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)(
              String.format("Requested memory is too low. Minimum memory for %s is %s MB per core",
                  cpuSeries, typeLimit.minMemPerCore));
        }
    
        // 4. Check if the requested memory isn't too much
        if (memory > coreCount * typeLimit.maxMemPerCore && !typeLimit.allowExtraMemory) {
          throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)(String.format(
              "Requested memory is too large.. Maximum memory allowed for %s is %s MB per core",
              cpuSeries, typeLimit.extraMemoryLimit));
        }
    
        // 5. Check if the requested memory isn't too large
        if (memory > typeLimit.extraMemoryLimit && typeLimit.allowExtraMemory) {
          throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)(
              String.format("Requested memory is too large.. Maximum memory allowed for %s is %s MB",
                  cpuSeries, typeLimit.extraMemoryLimit));
        }
    
        // Check if the CPU Series is E2 and return the custom machine type in the form of a string
        // acceptable by Compute Engine API.
        if (Arrays.asList(CpuSeries.E2_SMALL.cpuSeries, CpuSeries.E2_MICRO.cpuSeries,
            CpuSeries.E2_MEDIUM.cpuSeries).contains(cpuSeries)) {
          return String.format("zones/%s/machineTypes/%s-%s", zone, cpuSeries, memory);
        }
    
        // Check if extended memory was requested and return the extended custom machine type
        // in the form of a string acceptable by Compute Engine API.
        if (memory > coreCount * typeLimit.maxMemPerCore) {
          return String.format("zones/%s/machineTypes/%s-%s-%s-ext", zone, cpuSeries, coreCount,
              memory);
        }
    
        // Return the custom machine type in the form of a standard string
        // acceptable by Compute Engine API.
        return String.format("zones/%s/machineTypes/%s-%s-%s", zone, cpuSeries, coreCount, memory);
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b';
    // const instanceName = 'YOUR_INSTANCE_NAME';
    // const cpuSeries = 'N1';
    // const coreCount = 2
    // const memory = 256
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    function range(from, to, step) {
      return [...Array(Math.floor((to - from) / step) + 1)].map(
        (_, i) => from + i * step
      );
    }
    
    class CustomMachineType {
      constructor(zone, cpuSeries, coreCount, memory) {
        this.zone = zone;
        this.cpuSeries = cpuSeries;
        this.coreCount = coreCount;
        this.memory = memory;
    
        this.N1 = 'custom';
        this.N2 = 'n2-custom';
        this.N2D = 'n2d-custom';
        this.E2 = 'e2-custom';
        this.E2Micro = 'e2-custom-micro';
        this.E2Small = 'e2-custom-small';
        this.E2Medium = 'e2-custom-medium';
    
        this.CpuSeriesE2Limit = {
          allowedCores: range(2, 33, 2),
          minMemPerCore: 512,
          maxMemPerCore: 8192,
          allowExtraMemory: false,
          extraMemoryLimit: 0,
        };
    
        this.CpuSeriesE2MicroLimit = {
          allowedCores: [],
          minMemPerCore: 1024,
          maxMemPerCore: 2048,
          allowExtraMemory: false,
          extraMemoryLimit: 0,
        };
    
        this.CpuSeriesE2SmallLimit = {
          allowedCores: [],
          minMemPerCore: 2048,
          maxMemPerCore: 4096,
          allowExtraMemory: false,
          extraMemoryLimit: 0,
        };
    
        this.CpuSeriesE2MediumLimit = {
          allowedCores: [],
          minMemPerCore: 4096,
          maxMemPerCore: 8192,
          allowExtraMemory: false,
          extraMemoryLimit: 0,
        };
    
        this.CpuSeriesN2Limit = {
          allowedCores: [...range(2, 33, 2), ...range(36, 129, 4)],
          minMemPerCore: 512,
          maxMemPerCore: 8192,
          allowExtraMemory: true,
          extraMemoryLimit: 624 << 10,
        };
    
        this.CpuSeriesN2DLimit = {
          allowedCores: [2, 4, 8, 16, 32, 48, 64, 80, 96],
          minMemPerCore: 512,
          maxMemPerCore: 8192,
          allowExtraMemory: true,
          extraMemoryLimit: 768 << 10,
        };
    
        this.CpuSeriesN1Limit = {
          allowedCores: [1, range(2, 97, 2)],
          minMemPerCore: 922,
          maxMemPerCore: 6656,
          allowExtraMemory: true,
          extraMemoryLimit: 624 << 10,
        };
    
        this.TYPE_LIMITS = {
          [this.N1]: this.CpuSeriesN1Limit,
          [this.N2]: this.CpuSeriesN2Limit,
          [this.N2D]: this.CpuSeriesN2DLimit,
          [this.E2]: this.CpuSeriesE2Limit,
          [this.E2Micro]: this.CpuSeriesE2MicroLimit,
          [this.E2Small]: this.CpuSeriesE2SmallLimit,
          [this.E2Medium]: this.CpuSeriesE2MediumLimit,
        };
    
        if (![this.E2, this.N1, this.N2, this.N2D].includes(cpuSeries)) {
          throw new Error(`Incorrect CPU type: ${this.cpuSeries}`);
        }
    
        this.typeLimit = this.TYPE_LIMITS[this.cpuSeries];
    
        // Check whether the requested parameters are allowed.
        // Find more information about limitations of custom machine types at:
        // https://cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types
    
        // Check the number of cores
        if (
          this.typeLimit.allowedCores.length > 0 &&
          !this.typeLimit.allowedCores.includes(coreCount)
        ) {
          throw new Error(
            `Invalid number of cores requested. Allowed number of cores for ${this.cpuSeries} is: ${this.typeLimit.allowedCores}`
          );
        }
    
        // Memory must be a multiple of 256 MB
        if (this.memory % 256 !== 0) {
          throw new Error('Requested memory must be a multiple of 256 MB');
        }
    
        // Check if the requested memory isn't too little
        if (this.memory < this.coreCount * this.typeLimit.minMemPerCore) {
          throw new Error(
            `Requested memory is too low. Minimal memory for ${this.cpuSeries} is ${this.typeLimit.minMemPerCore} MB per core`
          );
        }
    
        // Check if the requested memory isn't too much
        if (
          this.memory > this.coreCount * this.typeLimit.maxMemPerCore &&
          !this.typeLimit.allowExtraMemory
        ) {
          throw new Error(
            `Requested memory is too large.. Maximum memory allowed for ${this.cpuSeries} is ${this.typeLimit.maxMemPerCore} MB per core`
          );
        }
    
        if (
          this.memory > this.typeLimit.extraMemoryLimit &&
          this.typeLimit.allowExtraMemory
        ) {
          throw new Error(
            `Requested memory is too large.. Maximum memory allowed for ${this.cpuSeries} is ${this.typeLimit.extraMemoryLimit} MB`
          );
        }
      }
    
      // Returns the custom machine type in form of a string acceptable by Compute Engine API.
      getMachineTypeURI() {
        if (
          [this.E2Small, this.E2Micro, this.E2Medium].includes(this.cpuSeries)
        ) {
          return `zones/${this.zone}/machineTypes/${this.cpuSeries}-${this.memory}`;
        }
    
        if (this.memory > this.coreCount * this.typeLimit.maxMemPerCore) {
          return `zones/${this.zone}/machineTypes/${this.cpuSeries}-${this.coreCount}-${this.memory}-ext`;
        }
    
        return `zones/${zone}/machineTypes/${this.cpuSeries}-${this.coreCount}-${this.memory}`;
      }
    }
    
    async function createInstanceWithCustomMachineTypeWithHelper() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const machineType = new CustomMachineType(
        zone,
        cpuSeries,
        coreCount,
        memory
      ).getMachineTypeURI();
    
      const [response] = await instancesClient.insert({
        instanceResource: {
          name: instanceName,
          disks: [
            {
              initializeParams: {
                diskSizeGb: '64',
                sourceImage:
                  'projects/debian-cloud/global/images/family/debian-11/',
              },
              autoDelete: true,
              boot: true,
            },
          ],
          machineType,
          networkInterfaces: [
            {
              name: 'global/networks/default',
            },
          ],
        },
        project: projectId,
        zone,
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the create operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log('Instance created.');
    }
    
    createInstanceWithCustomMachineTypeWithHelper();

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    from collections import namedtuple
    from enum import Enum
    from enum import unique
    import re
    import sys
    from typing import Any
    import warnings
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import compute_v1
    
    
    def gb_to_mb(value: int) -> int:
        return value << 10
    
    
    class CustomMachineType:
        """
        Allows to create custom machine types to be used with the VM instances.
        """
    
        @unique
        class CPUSeries(Enum):
            N1 = "custom"
            N2 = "n2-custom"
            N2D = "n2d-custom"
            E2 = "e2-custom"
            E2_MICRO = "e2-custom-micro"
            E2_SMALL = "e2-custom-small"
            E2_MEDIUM = "e2-custom-medium"
    
        TypeLimits = namedtuple(
            "TypeLimits",
            [
                "allowed_cores",
                "min_mem_per_core",
                "max_mem_per_core",
                "allow_extra_memory",
                "extra_memory_limit",
            ],
        )
    
        # The limits for various CPU types are described on:
        # https://cloud.google.com/compute/docs/general-purpose-machines
        LIMITS = {
            CPUSeries.E2: TypeLimits(frozenset(range(2, 33, 2)), 512, 8192, False, 0),
            CPUSeries.E2_MICRO: TypeLimits(frozenset(), 1024, 2048, False, 0),
            CPUSeries.E2_SMALL: TypeLimits(frozenset(), 2048, 4096, False, 0),
            CPUSeries.E2_MEDIUM: TypeLimits(frozenset(), 4096, 8192, False, 0),
            CPUSeries.N2: TypeLimits(
                frozenset(range(2, 33, 2)).union(set(range(36, 129, 4))),
                512,
                8192,
                True,
                gb_to_mb(624),
            ),
            CPUSeries.N2D: TypeLimits(
                frozenset({2, 4, 8, 16, 32, 48, 64, 80, 96}), 512, 8192, True, gb_to_mb(768)
            ),
            CPUSeries.N1: TypeLimits(
                frozenset({1}.union(range(2, 97, 2))), 922, 6656, True, gb_to_mb(624)
            ),
        }
    
        def __init__(
            self, zone: str, cpu_series: CPUSeries, memory_mb: int, core_count: int = 0
        ):
            self.zone = zone
            self.cpu_series = cpu_series
            self.limits = self.LIMITS[self.cpu_series]
            # Shared machine types (e2-small, e2-medium and e2-micro) always have
            # 2 vCPUs: https://cloud.google.com/compute/docs/general-purpose-machines#e2_limitations
            self.core_count = 2 if self.is_shared() else core_count
            self.memory_mb = memory_mb
            self._checked = False
            self._check_parameters()
            self.extra_memory_used = self._check_extra_memory()
    
        def is_shared(self):
            return self.cpu_series in (
                CustomMachineType.CPUSeries.E2_SMALL,
                CustomMachineType.CPUSeries.E2_MICRO,
                CustomMachineType.CPUSeries.E2_MEDIUM,
            )
    
        def _check_extra_memory(self) -> bool:
            if self._checked:
                return self.memory_mb > self.core_count * self.limits.max_mem_per_core
            else:
                raise RuntimeError(
                    "You need to call _check_parameters() before calling _check_extra_memory()"
                )
    
        def _check_parameters(self):
            """
            Check whether the requested parameters are allowed. Find more information about limitations of custom machine
            types at: https://cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types
            """
            # Check the number of cores
            if (
                self.limits.allowed_cores
                and self.core_count not in self.limits.allowed_cores
            ):
                raise RuntimeError(
                    f"Invalid number of cores requested. Allowed number of cores for {self.cpu_series.name} is: {sorted(self.limits.allowed_cores)}"
                )
    
            # Memory must be a multiple of 256 MB
            if self.memory_mb % 256 != 0:
                raise RuntimeError("Requested memory must be a multiple of 256 MB.")
    
            # Check if the requested memory isn't too little
            if self.memory_mb < self.core_count * self.limits.min_mem_per_core:
                raise RuntimeError(
                    f"Requested memory is too low. Minimal memory for {self.cpu_series.name} is {self.limits.min_mem_per_core} MB per core."
                )
    
            # Check if the requested memory isn't too much
            if self.memory_mb > self.core_count * self.limits.max_mem_per_core:
                if self.limits.allow_extra_memory:
                    if self.memory_mb > self.limits.extra_memory_limit:
                        raise RuntimeError(
                            f"Requested memory is too large.. Maximum memory allowed for {self.cpu_series.name} is {self.limits.extra_memory_limit} MB."
                        )
                else:
                    raise RuntimeError(
                        f"Requested memory is too large.. Maximum memory allowed for {self.cpu_series.name} is {self.limits.max_mem_per_core} MB per core."
                    )
    
            self._checked = True
    
        def __str__(self) -> str:
            """
            Return the custom machine type in form of a string acceptable by Compute Engine API.
            """
            if self.cpu_series in {
                self.CPUSeries.E2_SMALL,
                self.CPUSeries.E2_MICRO,
                self.CPUSeries.E2_MEDIUM,
            }:
                return f"zones/{self.zone}/machineTypes/{self.cpu_series.value}-{self.memory_mb}"
    
            if self.extra_memory_used:
                return f"zones/{self.zone}/machineTypes/{self.cpu_series.value}-{self.core_count}-{self.memory_mb}-ext"
    
            return f"zones/{self.zone}/machineTypes/{self.cpu_series.value}-{self.core_count}-{self.memory_mb}"
    
        def short_type_str(self) -> str:
            """
            Return machine type in a format without the zone. For example, n2-custom-0-10240.
            This format is used to create instance templates.
            """
            return str(self).rsplit("/", maxsplit=1)[1]
    
        @classmethod
        def from_str(cls, machine_type: str):
            """
            Construct a new object from a string. The string needs to be a valid custom machine type like:
             - https://www.googleapis.com/compute/v1/projects/diregapic-mestiv/zones/us-central1-b/machineTypes/e2-custom-4-8192
             - zones/us-central1-b/machineTypes/e2-custom-4-8192
             - e2-custom-4-8192 (in this case, the zone parameter will not be set)
            """
            zone = None
            if machine_type.startswith("http"):
                machine_type = machine_type[machine_type.find("zones/") :]
    
            if machine_type.startswith("zones/"):
                _, zone, _, machine_type = machine_type.split("/")
    
            extra_mem = machine_type.endswith("-ext")
    
            if machine_type.startswith("custom"):
                cpu = cls.CPUSeries.N1
                _, cores, memory = machine_type.rsplit("-", maxsplit=2)
            else:
                if extra_mem:
                    cpu_series, _, cores, memory, _ = machine_type.split("-")
                else:
                    cpu_series, _, cores, memory = machine_type.split("-")
                if cpu_series == "n2":
                    cpu = cls.CPUSeries.N2
                elif cpu_series == "n2d":
                    cpu = cls.CPUSeries.N2D
                elif cpu_series == "e2":
                    cpu = cls.CPUSeries.E2
                    if cores == "micro":
                        cpu = cls.CPUSeries.E2_MICRO
                        cores = 2
                    elif cores == "small":
                        cpu = cls.CPUSeries.E2_SMALL
                        cores = 2
                    elif cores == "medium":
                        cpu = cls.CPUSeries.E2_MEDIUM
                        cores = 2
                else:
                    raise RuntimeError("Unknown CPU series.")
    
            cores = int(cores)
            memory = int(memory)
    
            return cls(zone, cpu, memory, cores)
    
    
    def get_image_from_family(project: str, family: str) -> compute_v1.Image:
        """
        Retrieve the newest image that is part of a given family in a project.
    
        Args:
            project: project ID or project number of the Cloud project you want to get image from.
            family: name of the image family you want to get image from.
    
        Returns:
            An Image object.
        """
        image_client = compute_v1.ImagesClient()
        # List of public operating system (OS) images: https://cloud.google.com/compute/docs/images/os-details
        newest_image = image_client.get_from_family(project=project, family=family)
        return newest_image
    
    
    def disk_from_image(
        disk_type: str,
        disk_size_gb: int,
        boot: bool,
        source_image: str,
        auto_delete: bool = True,
    ) -> compute_v1.AttachedDisk:
        """
        Create an AttachedDisk object to be used in VM instance creation. Uses an image as the
        source for the new disk.
    
        Args:
             disk_type: the type of disk you want to create. This value uses the following format:
                "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
                For example: "zones/us-west3-b/diskTypes/pd-ssd"
            disk_size_gb: size of the new disk in gigabytes
            boot: boolean flag indicating whether this disk should be used as a boot disk of an instance
            source_image: source image to use when creating this disk. You must have read access to this disk. This can be one
                of the publicly available images or an image from one of your projects.
                This value uses the following format: "projects/{project_name}/global/images/{image_name}"
            auto_delete: boolean flag indicating whether this disk should be deleted with the VM that uses it
    
        Returns:
            AttachedDisk object configured to be created using the specified image.
        """
        boot_disk = compute_v1.AttachedDisk()
        initialize_params = compute_v1.AttachedDiskInitializeParams()
        initialize_params.source_image = source_image
        initialize_params.disk_size_gb = disk_size_gb
        initialize_params.disk_type = disk_type
        boot_disk.initialize_params = initialize_params
        # Remember to set auto_delete to True if you want the disk to be deleted when you delete
        # your VM instance.
        boot_disk.auto_delete = auto_delete
        boot_disk.boot = boot
        return boot_disk
    
    
    def wait_for_extended_operation(
        operation: ExtendedOperation, verbose_name: str = "operation", timeout: int = 300
    ) -> Any:
        """
        Waits for the extended (long-running) operation to complete.
    
        If the operation is successful, it will return its result.
        If the operation ends with an error, an exception will be raised.
        If there were any warnings during the execution of the operation
        they will be printed to sys.stderr.
    
        Args:
            operation: a long-running operation you want to wait on.
            verbose_name: (optional) a more verbose name of the operation,
                used only during error and warning reporting.
            timeout: how long (in seconds) to wait for operation to finish.
                If None, wait indefinitely.
    
        Returns:
            Whatever the operation.result() returns.
    
        Raises:
            This method will raise the exception received from `operation.exception()`
            or RuntimeError if there is no exception set, but there is an `error_code`
            set for the `operation`.
    
            In case of an operation taking longer than `timeout` seconds to complete,
            a `concurrent.futures.TimeoutError` will be raised.
        """
        result = operation.result(timeout=timeout)
    
        if operation.error_code:
            print(
                f"Error during {verbose_name}: [Code: {operation.error_code}]: {operation.error_message}",
                file=sys.stderr,
                flush=True,
            )
            print(f"Operation ID: {operation.name}", file=sys.stderr, flush=True)
            raise operation.exception() or RuntimeError(operation.error_message)
    
        if operation.warnings:
            print(f"Warnings during {verbose_name}:\n", file=sys.stderr, flush=True)
            for warning in operation.warnings:
                print(f" - {warning.code}: {warning.message}", file=sys.stderr, flush=True)
    
        return result
    
    
    def create_instance(
        project_id: str,
        zone: str,
        instance_name: str,
        disks: list[compute_v1.AttachedDisk],
        machine_type: str = "n1-standard-1",
        network_link: str = "global/networks/default",
        subnetwork_link: str = None,
        internal_ip: str = None,
        external_access: bool = False,
        external_ipv4: str = None,
        accelerators: list[compute_v1.AcceleratorConfig] = None,
        preemptible: bool = False,
        spot: bool = False,
        instance_termination_action: str = "STOP",
        custom_hostname: str = None,
        delete_protection: bool = False,
    ) -> compute_v1.Instance:
        """
        Send an instance creation request to the Compute Engine API and wait for it to complete.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone to create the instance in. For example: "us-west3-b"
            instance_name: name of the new virtual machine (VM) instance.
            disks: a list of compute_v1.AttachedDisk objects describing the disks
                you want to attach to your new instance.
            machine_type: machine type of the VM being created. This value uses the
                following format: "zones/{zone}/machineTypes/{type_name}".
                For example: "zones/europe-west3-c/machineTypes/f1-micro"
            network_link: name of the network you want the new instance to use.
                For example: "global/networks/default" represents the network
                named "default", which is created automatically for each project.
            subnetwork_link: name of the subnetwork you want the new instance to use.
                This value uses the following format:
                "regions/{region}/subnetworks/{subnetwork_name}"
            internal_ip: internal IP address you want to assign to the new instance.
                By default, a free address from the pool of available internal IP addresses of
                used subnet will be used.
            external_access: boolean flag indicating if the instance should have an external IPv4
                address assigned.
            external_ipv4: external IPv4 address to be assigned to this instance. If you specify
                an external IP address, it must live in the same region as the zone of the instance.
                This setting requires `external_access` to be set to True to work.
            accelerators: a list of AcceleratorConfig objects describing the accelerators that will
                be attached to the new instance.
            preemptible: boolean value indicating if the new instance should be preemptible
                or not. Preemptible VMs have been deprecated and you should now use Spot VMs.
            spot: boolean value indicating if the new instance should be a Spot VM or not.
            instance_termination_action: What action should be taken once a Spot VM is terminated.
                Possible values: "STOP", "DELETE"
            custom_hostname: Custom hostname of the new VM instance.
                Custom hostnames must conform to RFC 1035 requirements for valid hostnames.
            delete_protection: boolean value indicating if the new virtual machine should be
                protected against deletion or not.
        Returns:
            Instance object.
        """
        instance_client = compute_v1.InstancesClient()
    
        # Use the network interface provided in the network_link argument.
        network_interface = compute_v1.NetworkInterface()
        network_interface.network = network_link
        if subnetwork_link:
            network_interface.subnetwork = subnetwork_link
    
        if internal_ip:
            network_interface.network_i_p = internal_ip
    
        if external_access:
            access = compute_v1.AccessConfig()
            access.type_ = compute_v1.AccessConfig.Type.ONE_TO_ONE_NAT.name
            access.name = "External NAT"
            access.network_tier = access.NetworkTier.PREMIUM.name
            if external_ipv4:
                access.nat_i_p = external_ipv4
            network_interface.access_configs = [access]
    
        # Collect information into the Instance object.
        instance = compute_v1.Instance()
        instance.network_interfaces = [network_interface]
        instance.name = instance_name
        instance.disks = disks
        if re.match(r"^zones/[a-z\d\-]+/machineTypes/[a-z\d\-]+$", machine_type):
            instance.machine_type = machine_type
        else:
            instance.machine_type = f"zones/{zone}/machineTypes/{machine_type}"
    
        instance.scheduling = compute_v1.Scheduling()
        if accelerators:
            instance.guest_accelerators = accelerators
            instance.scheduling.on_host_maintenance = (
                compute_v1.Scheduling.OnHostMaintenance.TERMINATE.name
            )
    
        if preemptible:
            # Set the preemptible setting
            warnings.warn(
                "Preemptible VMs are being replaced by Spot VMs.", DeprecationWarning
            )
            instance.scheduling = compute_v1.Scheduling()
            instance.scheduling.preemptible = True
    
        if spot:
            # Set the Spot VM setting
            instance.scheduling.provisioning_model = (
                compute_v1.Scheduling.ProvisioningModel.SPOT.name
            )
            instance.scheduling.instance_termination_action = instance_termination_action
    
        if custom_hostname is not None:
            # Set the custom hostname for the instance
            instance.hostname = custom_hostname
    
        if delete_protection:
            # Set the delete protection bit
            instance.deletion_protection = True
    
        # Prepare the request to insert an instance.
        request = compute_v1.InsertInstanceRequest()
        request.zone = zone
        request.project = project_id
        request.instance_resource = instance
    
        # Wait for the create operation to complete.
        print(f"Creating the {instance_name} instance in {zone}...")
    
        operation = instance_client.insert(request=request)
    
        wait_for_extended_operation(operation, "instance creation")
    
        print(f"Instance {instance_name} created.")
        return instance_client.get(project=project_id, zone=zone, instance=instance_name)
    
    
    def create_custom_instance(
        project_id: str,
        zone: str,
        instance_name: str,
        cpu_series: CustomMachineType.CPUSeries,
        core_count: int,
        memory: int,
    ) -> compute_v1.Instance:
        """
        Create a new VM instance with a custom machine type.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone to create the instance in. For example: "us-west3-b"
            instance_name: name of the new virtual machine (VM) instance.
            cpu_series: the type of CPU you want to use. Select one value from the CustomMachineType.CPUSeries enum.
                For example: CustomMachineType.CPUSeries.N2
            core_count: number of CPU cores you want to use.
            memory: the amount of memory for the VM instance, in megabytes.
    
        Return:
            Instance object.
        """
        assert cpu_series in (
            CustomMachineType.CPUSeries.E2,
            CustomMachineType.CPUSeries.N1,
            CustomMachineType.CPUSeries.N2,
            CustomMachineType.CPUSeries.N2D,
        )
        custom_type = CustomMachineType(zone, cpu_series, memory, core_count)
    
        newest_debian = get_image_from_family(project="debian-cloud", family="debian-12")
        disk_type = f"zones/{zone}/diskTypes/pd-standard"
        disks = [disk_from_image(disk_type, 10, True, newest_debian.self_link)]
    
        return create_instance(project_id, zone, instance_name, disks, str(custom_type))
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
