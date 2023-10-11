import os
import sys
import argparse
import shutil
import pandas as pd
import numpy as np

# Set the arguments
parser = argparse.ArgumentParser(description='Organization transformation block')
parser.add_argument('--in-file', type=str, required=True, help="Argument passed by Edge Impulse transformation block when the --in-file option is selected")
parser.add_argument('--out-directory', type=str, required=False, help="Argument passed by Edge Impulse transformation block when the --out-directory option is selected")
parser.add_argument('--split-interval', type=int, required=True, help="Time interval in seconds for splitting the CSV")
parser.add_argument('--time-column', type=str, required=True, help="Name of the time column in the CSV")

args, unknown = parser.parse_known_args()
print('--in_file: ', args.in_file, flush=True)
print('--out_directory: ', args.out_directory, flush=True)
print('--split_interval: ', args.split_interval, flush=True)
print('--time-column: ', args.time_column, flush=True)

# Verify that the input file exists
if args.in_file:
    if not os.path.exists(args.in_file):
        print('--in-file argument', args.in_file, 'does not exist', flush=True)
    else:
        print('--in-file path', args.in_file, 'exists', flush=True)
        print("filename: ", os.path.basename(args.in_file))

        # Read csv
        df = pd.read_csv(args.in_file)
        # Convert the specified time column to a datetime format
        df[args.time_column] = pd.to_datetime(df[args.time_column], unit='ns')
        # Set the 'time' column as the index
        df.set_index('time', inplace=True)

        # Define a function to split the DataFrame into smaller DataFrames
        def split_dataframe(df, split_interval_seconds):
            split_dataframes = []
            start_time = df.index[0]
            while start_time < df.index[-1]:
                end_time = start_time + pd.Timedelta(seconds=split_interval_seconds)
                split_df = df[(df.index >= start_time) & (df.index < end_time)]
                split_dataframes.append(split_df)
                # Save each split with a filename based on the Unix timestamp
                start_unix_timestamp = int(start_time.timestamp())
                end_unix_timestamp = int(end_time.timestamp())
                output_filename = os.path.join(args.out_directory, f"{os.path.splitext(os.path.basename(args.in_file))[0]}.split_{start_unix_timestamp}_{end_unix_timestamp}.csv")
                split_df.to_csv(output_filename)
                print(f"Saved {output_filename}", flush=True)
                start_time = end_time
            return split_dataframes

        # Split the DataFrame into smaller DataFrames
        split_dataframes = split_dataframe(df, args.split_interval)

        print("Finished", flush=True)
        exit(0)
else:
    print('Missing argument --in-file not exist')
    sys.exit(1)