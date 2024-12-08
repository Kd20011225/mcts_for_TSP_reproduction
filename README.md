This README provides step-by-step instructions for reproducing the results presented in the research on solving large-scale Traveling Salesman Problems (TSP) using heatmap-guided Monte Carlo Tree Search (MCTS). The guide includes setting up the environment, running the code, and generating the figures and tables presented in the research paper.

Environment Setup: The project relies on the fire, lkh, numpy, and torch libraries. Install them using the following commands:

pip install fire
pip install lkh
pip install numpy
Install torch according to your CUDA version. For CUDA 11.4, use:

pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113

Heatmap Loading

Step 1: Extract Heatmaps

Unzip all heatmaps from the all_heatmap folder:

cd all_heatmap/attgcn
unzip heatmap.zip
cd ../difusco
unzip heatmap.zip
cd ../dimes
unzip heatmap.zip
cd ../utsp
unzip TSP500_Input.zip
unzip TSP1000_Input.zip

Step 2: Format Conversion for UTSP

Convert UTSP heatmap formats to default format:

python reformat_to_default.py 500
python reformat_to_default.py 1000

Step 3: Generate SoftDist Heatmaps

Unzip input files:

cd ../../default_mcts
unzip tsp500_test_concorde.zip
unzip tsp1000_test_concorde.zip
unzip tsp10000_test_concorde.zip

cd ../all_heatmap/softdist
python batch_generate_heatmap.py 500 0.0066
python batch_generate_heatmap.py 1000 0.0051
python batch_generate_heatmap.py 10000 0.0018


Running Tests

Test with Default MCTS Parameters

Run MCTS with default parameters. Example for SoftDist on TSP-500:

cd default_mcts
cp -r ../all_heatmap/softdist/heatmap .
bash solve-500.sh
python summarize.py 500

Test with Varying Time Budgets

Run MCTS with different time budgets. Example for TSP-500:

cd default_mcts_varying_time
unzip tsp500_test_concorde.zip
cp -r ../all_heatmap/softdist/heatmap .
bash multiT-500.sh

Test with UTSP MCTS Parameters

Convert SoftDist heatmaps to UTSP format:

cd utsp
python reformat_to_utsp.py softdist 500
python reformat_to_utsp.py softdist 1000

Run UTSP MCTS:
cd Search
bash ./new-solve-500.sh 0 5 100 0 50 2 1 1
python summarize.py 500
bash ./new-solve-1000.sh 0 5 10 0 150 3 1
python summarize.py 1000

For larger TSP problems, update #define Max_City_Num in TSP_IO.h accordingly.

Test UTSP MCTS with Varying Time Budgets

Run UTSP MCTS with time budgets. Example for TSP-500:

cd utsp_varying_time
python reformat_to_utsp.py softdist 500
python reformat_to_utsp.py softdist 1000
cd Search
bash multiT-500.sh

Update #define Max_City_Num in TSP_IO.h as needed.

Calculating Metric Score

Test performance of LKH-3 for metrics calculation:

cd calculate_score_metric
unzip tsp500_test_concorde.zip
python lkh_solve.py --N 500 --runs 5

Ensure LKH-3 is installed and configured in lkh_solve.py

Grid Search for SoftDist Temperature

Generate training dataset for grid search:

cd grid_search
python generate_training_data.py --N 500 --batch 1024

Run grid search for temperature parameter:
bash grid_search-500.sh
