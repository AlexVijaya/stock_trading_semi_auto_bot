import subprocess
import sys
import time
def run_multiple_search_current_rebound_breakout_false_breakout_situations():
    # Run the Python script and capture its output

    # Get the path to the Python interpreter executable
    interpreter = sys.executable


    print(interpreter)
    files = ['current_search_for_tickers_with_breakout_situations_of_ath_position_entry_next_day.py',
             'current_search_for_tickers_with_breakout_situations_of_ath_position_entry_on_day_two.py',
             'current_search_for_tickers_with_breakout_situations_of_atl_position_entry_next_day.py',
             'current_search_for_tickers_with_breakout_situations_of_atl_position_entry_on_day_two.py',
             'current_search_for_tickers_with_false_breakout_of_ath_by_one_bar.py',
             'current_search_for_tickers_with_false_breakout_of_ath_by_two_bars.py',
             'current_search_for_tickers_with_false_breakout_of_atl_by_one_bar.py',
             'current_search_for_tickers_with_false_breakout_of_atl_by_two_bars.py',
             'current_search_for_tickers_with_rebound_situations_off_ath.py',
             'current_search_for_tickers_with_rebound_situations_off_atl.py']

    # Run each Python file in the list in parallel
    processes = []
    for file in files:
        process = subprocess.Popen([f'{interpreter}', file], stdout=subprocess.PIPE)
        processes.append(process)

    # Wait for the processes to complete and get their output
    outputs = []
    for process in processes:
        output, _ = process.communicate()
        outputs.append(output.decode())

    # Print the output of the processes
    for output in outputs:
        print(output)
if __name__=="__main__":
    start_time = time.time()
    run_multiple_search_current_rebound_breakout_false_breakout_situations()
    end_time = time.time()
    overall_time = end_time - start_time
    print('overall time in minutes=', overall_time / 60.0)
    print('overall time in hours=', overall_time / 60.0 / 60.0)