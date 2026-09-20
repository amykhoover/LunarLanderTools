import os
import gym
from PIL import Image
from lunar_lander_controllers import pd_heuristic_controller

run_number_in_save_folder = 17
max_steps = 400
folder_name = f"lunar_lander_examples/Run{run_number_in_save_folder}-MaxSteps{max_steps}"
action_list_file_name = f"{folder_name}/action_list.txt"

if __name__ == "__main__":

    ## Make a Save Folder, Make a Run Folder
    output_dir = "lunar_lander_examples"
    os.makedirs(output_dir, exist_ok=True)
    output_dir = folder_name
    os.makedirs(output_dir, exist_ok=True)

    ## Setup the Environment
    env = gym.make("LunarLander-v2")
    obs = env.reset()
    total_reward = 0.0
    reward = 0
    step = 1
    done = False

    ## Logging
    current_seeds = env.seed()
    with open(action_list_file_name, "a", encoding="utf-8") as file:
        file.write(f"Current random seed: {current_seeds[0]}\n")
    print(f"Current random seed: {current_seeds[0]}")
    frame = env.render(mode="rgb_array")
    Image.fromarray(frame).save(os.path.join(output_dir, "frame_0000.png"))
    with open(action_list_file_name, "a", encoding="utf-8") as file:
        file.write(f"Observation: {obs}, Reward: {reward}, total_reward = {total_reward}\n")


    while not done and step <= max_steps:

        action = pd_heuristic_controller(obs)

        if action == 0:
            action_string = f"Step {step}: 0 (No Operation: Do nothing)" # Action 0
            print(action_string)
            with open(action_list_file_name, "a", encoding="utf-8") as file:
                file.write(f"{action_string}\n")
        elif action == 1:
            action_string = f"Step {step}: 1 (Fire left engine -> tilt right)" # Action 1
            print(action_string)
            with open(action_list_file_name, "a", encoding="utf-8") as file:
                file.write(f"{action_string}\n")
        elif action ==2: 
            action_string = f"Step {step}: 2 (Fire main engine -> upward thrust)" # Action 2
            print(action_string)
            with open(action_list_file_name, "a", encoding="utf-8") as file:
                file.write(f"{action_string}\n")
        elif action == 3:
            action_string = f"Step {step}: 3 (Fire right engine -> tilt left)" # Action 3
            print(action_string)
            with open(action_list_file_name, "a", encoding="utf-8") as file:
                file.write(f"{action_string}\n")

       
        obs, reward, done, info = env.step(action) # Note: Gym 0.17.0
        total_reward += reward
        with open(action_list_file_name, "a", encoding="utf-8") as file:
            file.write(f"Observation: {obs}, Reward: {reward}, total_reward = {total_reward}\n")

        # Save this frame
        frame = env.render(mode="rgb_array")
        filename = os.path.join(output_dir, f"frame_{step:04d}.png")
        Image.fromarray(frame).save(filename)

        step += 1
        frame +=1

    
    env.close()
    print(f"Episode finished in {step - 1} steps with total reward: {total_reward:.2f}")
