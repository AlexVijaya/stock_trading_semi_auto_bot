import multiprocessing
import os
import datetime
import time

# Record the start time
start_time = time.time()

# Get the current date
today = datetime.datetime.now().strftime("%Y-%m-%d")

# Create the output file path
subfolder = "current_rebound_breakout_and_false_breakout"
output_file_path = os.path.join(subfolder, f"{today}.txt")

# Create the subfolder if it doesn't exist
if not os.path.exists(subfolder):
    os.makedirs(subfolder)

def run_script(script_path):
    # Run the script and redirect its output to the output file
    os.system(f"python {script_path} >> {output_file_path}")

if __name__ == "__main__":
    # List of script paths
    script_paths = ['current_search_for_tickers_with_breakout_situations_of_ath_position_entry_next_day.py',
             'current_search_for_tickers_with_breakout_situations_of_ath_position_entry_on_day_two.py',
             'current_search_for_tickers_with_breakout_situations_of_atl_position_entry_next_day.py',
             'current_search_for_tickers_with_breakout_situations_of_atl_position_entry_on_day_two.py',
             'current_search_for_tickers_with_false_breakout_of_ath_by_one_bar.py',
             'current_search_for_tickers_with_false_breakout_of_ath_by_two_bars.py',
             'current_search_for_tickers_with_false_breakout_of_atl_by_one_bar.py',
             'current_search_for_tickers_with_false_breakout_of_atl_by_two_bars.py',
             'current_search_for_tickers_with_rebound_situations_off_ath.py',
             'current_search_for_tickers_with_rebound_situations_off_atl.py',
             'not_in_hindsight_search_for_tickers_with_ath_equal_to_limit_level.py',
             'not_in_hindsight_search_for_tickers_with_atl_equal_to_limit_level.py']
    processes = []
    for script_path in script_paths:
        process = multiprocessing.Process(target=run_script, args=(script_path,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time
print(f"Elapsed time: {elapsed_time:.2f} seconds")
