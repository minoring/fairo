export LOCOBOT_IP=$1
export SAVE_EXPLORATION=True
export DATA_PATH=baselinev3_noisy
export HEURISTIC=baseline
export VISUALIZE_EXAMINE=True
export CONTINUOUS_EXPLORE=True
source activate /private/home/apratik/miniconda3/envs/droidlet
python agents/locobot/locobot_agent.py --dev --data_store_path /checkpoint/apratik/data_reexplore