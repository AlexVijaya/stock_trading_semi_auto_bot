import threading
import os
import datetime
import time

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
    start_time = time.time()
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
    threads = []
    for script_path in script_paths:
        thread = threading.Thread(target=run_script, args=(script_path,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    end_time = time.time()
    overall_time = end_time - start_time
    print('overall time in minutes=', overall_time / 60.0)
    print('overall time in hours=', overall_time / 60.0 / 60.0)
