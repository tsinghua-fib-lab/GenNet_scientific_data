# GenNet_scientific_data Overview
 The repository offers the GenNet (an interactive simulator that generates a Synthetic Data Ecosystem for Mobile Communication Networks) along with the Synthetic Data (including the user data, the wireless environment data, and the network performance data).

# Welcome to the GenNet Repository

GenNet is an interactive simulator designed to generate a Synthetic Data Ecosystem for Mobile Communication Networks. This repository provides both the GenNet simulator itself and a comprehensive collection of synthetic data, which includes:

- User Data: Simulated user profiles, behaviors, and preferences for realistic mobile network scenarios.
- Wireless Environment Data: Detailed information on signal strengths, interference, and network topology.
- Network Performance Data: Metrics and statistics related to network performance, including latency, throughput, and packet loss.

Key Features:
- GenNet Simulator: A user-friendly, interactive simulator for generating synthetic data ecosystems, allowing researchers and developers to emulate mobile communication networks.
- Versatile Data Sets: High-quality synthetic data sets that can be used for various research, testing, and training purposes in the field of mobile networks.
- Open Source: GenNet and the synthetic data are open-source and freely available for academic, research, and development purposes.

Usage:
1. Clone or download this repository to access the GenNet simulator and synthetic data.
2. Refer to the provided documentation for instructions on using the simulator and integrating the synthetic data into your projects.
3. Contribute: Feel free to contribute to the development of GenNet or share your research findings using the synthetic data. We welcome collaboration from the community.

Explore the possibilities of mobile communication network research and development with GenNet and its synthetic data. Join us in advancing the field of mobile networks!

# File Description

This repository includes the following key components:

## GenNet - Interactive Simulator

GenNet is an interactive simulator designed to generate a Synthetic Data Ecosystem for Mobile Communication Networks. It allows researchers and developers to emulate mobile network scenarios and experiment with various parameters. In this release, you will find:

- **the GenNet Executable:** The core executable file for running the GenNet simulator.

## pycomm

- **pycomm:** A Python reinforcement learning client that facilitates communication with the simulator, enabling dynamic interactions and experiments.

## Reinforcement Learning Optimization Codes

We provide three sets of reinforcement learning optimization codes tailored to enhance the performance of the GenNet simulator in different ways:

- **Coverage Optimization:** Optimize network coverage and quality of service.
- **Energy Efficiency Optimization:** Reduce energy consumption in mobile networks.
- **Dynamic Resource Allocation Optimization:** Optimize resource allocation in dynamic network environments.

## Synthetic Data

To support your experiments and research, we include a comprehensive set of synthetic data:

- **User Data:** Simulated user profiles, behaviors, and preferences.
- **Wireless Environment Data:** Detailed information on signal strengths, interference, and network topology.
- **Network Performance Data:** Metrics and statistics related to network performance.

## README Documentation

For detailed instructions on how to get started, configure, and use GenNet, please refer to the README documentation provided in this repository.


# Utilization of GenNet

GenNet is a powerful software tool that serves as "A Generative AI-Powered Synthetic Data Ecosystem for Mobile Networks." This part provides a comprehensive guide on how to use GenNet, including startup parameters with examples and detailed explanations for all possible parameter values in the configuration file.

## Startup Parameters and Their Meanings

GenNet accepts several startup parameters that control its behavior. Here are the main parameters with examples and their meanings:

- `job`: Specifies the name of the whole simulation task. (Example: `"job0"`)
- `grpcEndpoint`: Sets the gRPC listening address. (Example: `"localhost:51402"`)
- `pprofAddr`: Specifies the pprof listening address for debugging and profiling purposes. 
- `configPath`: Specifies the path to the configuration file. (Example: `"config.yml"`)
- `useRL`: Allows you to use Reinforcement Learning (RL) for optimization instead of normal simulation. (Example: `true` or `false`)

## How to Use GenNet

To use GenNet, follow these steps:

1. **Download Files**: Ensure that the complete `pycomm` folder and the RL optimization code are placed in the main directory.

2. **Start the Simulator**: Open a terminal and navigate to the directory containing GenNet. Use the following command to start the simulator: ./comm_docker -rl -config config.yml -listen "localhost:port_xxx" -h. Replace `"port_xxx"` with the desired port number for the listening address.

3. **Start Interaction**: Open a new shell and activate the conda environment to initiate RL interaction.

## Configuration File Options

The `config.yml` file contains various configuration options. Here are detailed explanations for all possible parameter values:

- `ChannelType`: Specifies the type of channel used in the simulation. Possible values:
  - `CHANNEL_TYPE_UNSPECIFIED` (0)
  - `CHANNEL_TYPE_EQUATION` (1)    // Based on ray tracing
  - `CHANNEL_TYPE_RAY_TRACING` (2)
  - `CHANNEL_TYPE_3GPP` (3)
  - `CHANNEL_TYPE_FREESPACE` (4)    //	Based on electromagnetic computation.
  - `CHANNEL_TYPE_CEM` (5)

- `AntennaType`: Specifies the type of antenna used in the simulation. Possible values:
  - `ANTENNA_TYPE_UNSPECIFIED` (0)
  - `ANTENNA_TYPE_SISO` (1)
  - `ANTENNA_TYPE_MIMO` (2)

- `Control`: Controls various aspects of the simulation, such as steps, threads, and display options.
  - `step` (ControlStep): Specifies the control step.
  - `thread` (ControlThread): Specifies the control thread.
  - `microscopic_range` (ControlOutput): Defines the range of the microscopic area.
  - `macroscopic_range` (ControlOutput): Defines the range of the macroscopic area.
  - `enable_controlled` (bool): Indicates whether the simulator uses external control.
  - `enable_optimize` (bool): Specifies if communication uses optimized allocation.
  - `optimize_interval` (optional int32): Sets the communication optimization allocation interval in steps.
  - `display_guomao` (bool): Determines whether to display the microscopic area.
  - `coverage_range` (double): Sets the initial coverage range of base stations in meters.
  - `handover_interval` (int32): Defines the handover frequency of base stations in seconds.
  - `channel_type` (ChannelType): Specifies the channel model used in the simulation.
  - `antenna_type` (AntennaType): Specifies the type of antenna used in the simulation.

- `OutputSwitch`: Specifies which types of data to output. Options include:
  - `person` (1)
  - `base_station` (2)
  - `aoi` (3)
  - `heatmap` (4)
  - `stats` (5)

## Database Dependencies

GenNet relies on a MongoDB database for its functionality. Make sure you have MongoDB installed and configured properly.

---

For more detailed information and specific instructions, please refer to the RL Algorithm User Guide. If you have any further questions or need assistance, please don't hesitate to reach out.

**Note**: Ensure that you have all the necessary dependencies and permissions to run GenNet effectively.
