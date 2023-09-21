import os, sys, argparse, shutil
import pandas as pd
import numpy as np

# Set the arguments
parser = argparse.ArgumentParser(description='Organization transformation block')
parser.add_argument('--in_file', type=str, required=True, help="Argument passed by Edge Impulse transformation block when the --in-file option is selected")
parser.add_argument('--out_directory', type=str, required=False, help="Argument passed by Edge Impulse transformation block when the --out-directory option is selected")
parser.add_argument('--sampling_rate', type=int, required=True, help="Sampling rate in milliseconds")
parser.add_argument('--resampling_mode', type=str, required=False, help="Resampling mode, by default mean")

args, unknown = parser.parse_known_args()
print('--in_file: ', args.in_file, flush=True)
print('--out_directory: ', args.out_directory, flush=True)
print('--sampling_rate: ', args.sampling_rate, flush=True)
print('--resampling_mode: ', args.resampling_mode, flush=True)


# verify that the input file exists
if args.in_file:
    if not os.path.exists(args.in_file):
        print('--in-file argument', args.in_file, 'does not exist', flush=True)
    else:
        print('--in-file path', args.in_file, 'exist', flush=True)
        print("filename: ", os.path.basename(args.in_file))

        # Read csv
        df = pd.read_csv(args.in_file)

        # First diagnose the sampling rate
        consecutive_deltas = df['seconds_elapsed'].diff()
        avg_sampling_rate = np.mean(consecutive_deltas)
        avg_frequency = 1 / np.mean(consecutive_deltas)
        shortest_gap = np.min(consecutive_deltas)
        maximum_gap = np.max(consecutive_deltas)
        total_num_of_samples = len(df.index)

        print("Average Sampling Rate:", avg_sampling_rate, flush=True)
        print("Average Frequency:", avg_frequency, flush=True)
        print("Shortest Gap:", shortest_gap, flush=True)
        print("Maximum Gap:", maximum_gap, flush=True)
        print("Total Number of Samples:", total_num_of_samples, flush=True)

        # Now resample
        print("Resampling ...", flush=True)
        df.index = pd.to_datetime(df['time'], unit='ns')
        sampling_rate = str(args.sampling_rate)+'ms'
        
        if args.resampling_mode == 'mean':
            df_resampled = df.resample(sampling_rate).mean()
        elif args.resampling_mode == 'median':
            df_resampled = df.resample(sampling_rate).median()
        else:
            print('Argument --resampling_mode not corect, select mean or median')
            sys.exit(1)
        
    
        # If the desired frequency is higher than the average one, upsample using interpolation
        frequency = (1/args.sampling_rate) * 1000
        if frequency > avg_frequency:
            print("Desired frequency (", frequency, "Hz ) is higher than average file frequency (", avg_frequency,"Hz )...", flush=True)
            print("Upsampling using polynomial interpolation ...", flush=True)
            df_resampled = df_resampled.interpolate(method='polynomial', order=1)

        # Save resampled file
        df_resampled.to_csv(os.path.join(args.out_directory, os.path.basename(args.in_file)), index=False)
        print("... Done", flush=True)
        # Diagnose the output file
        
        consecutive_deltas = df_resampled['seconds_elapsed'].diff()
        avg_sampling_rate = np.mean(consecutive_deltas)
        avg_frequency = 1 / np.mean(consecutive_deltas)
        shortest_gap = np.min(consecutive_deltas)
        maximum_gap = np.max(consecutive_deltas)
        total_num_of_samples = len(df_resampled.index)

        print("Average Sampling Rate:", avg_sampling_rate, flush=True)
        print("Average Frequency:", avg_frequency, flush=True)
        print("Shortest Gap:", shortest_gap, flush=True)
        print("Maximum Gap:", maximum_gap, flush=True)
        print("Total Number of Samples:", total_num_of_samples, flush=True)

        print("Finished", flush=True)
        exit(0)

else:
    print('Missing argument --in-file not exist')
    sys.exit(1)





