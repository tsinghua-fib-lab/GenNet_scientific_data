# pycomm

Python reinforcement learning client for communication with the simulator.

## Usage

### Initialization: (Using Dynamic Optimization Environment as an Example)

```
	from pycomm.pycomm import DynamicEnv
	env = DynamicEnv(
	    channel_type: int = 1,      # Channel type
	    antenna_type: int = 1,     # Antenna type
	    job: str = 'job0',             # Job name
	    output: bool = False,      # Enable output
	    display_micro: bool = True,  # Macro and micro area selection
	    coverage_range: int = 1000,  # Coverage range
	    handover_interval: int = 1,  # Handover interval
	)

```


###  Simulator Step: Control the simulation steps of the simulator

#### Parameters:

 - action: Actions provided by RL (Reinforcement Learning)

 - start: Starting step of the simulator

 - total: Total number of steps the simulator should execute (end step = starting step + total steps)

 - interval: Time interval for each step

 
#### Return Values:

 - async_coroutine_step: Contains state and reward

 - state: State returned by the simulator, used for RL optimization training

 - reward: Result of taking action in the simulator, providing reward feedback

 - terminated: Indicates when the simulation is finished
 
```
	async_coroutine_step, terminated, _ = await env.step(action, start, total, interval )
```

### Closing the Simulator: Terminate the simulator process when RL training is complete.
```
	 await env.reset()
```

