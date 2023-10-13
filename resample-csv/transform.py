import os
import sys
import argparse
import shutil
import pandas as pd
import numpy as np
import json

def save_metadata(metadata, out_directory):
    all_ok = all(metadata['metadata'][m] != 0 for m in metadata['metadata'])
    metadata['metadata']['ei_check'] = 1 if all_ok else 0
    with open(os.path.join(out_directory, 'ei-metadata.json'), 'w') as f:
        json.dump(metadata, f, indent=4)
    exit(0)

def main():
    parser = argparse.ArgumentParser(description='Organization transformation block')
    parser.add_argument('--in-file', type=str, required=True, help="Input file")
    parser.add_argument('--out-directory', type=str, required=False, help="Output directory")
    parser.add_argument('--sampling_rate', type=int, required=True, help="Sampling rate in milliseconds")
    parser.add_argument('--resampling_mode', type=str, required=False, help="Resampling mode (default is mean)")
    parser.add_argument('--metadata', type=json.loads, required=False, help="Existing metadata")

    args = parser.parse_args()
    print('--in-file:', args.in_file, flush=True)
    print('--out-directory:', args.out_directory, flush=True)
    print('--sampling_rate:', args.sampling_rate, flush=True)
    print('--resampling_mode:', args.resampling_mode, flush=True)
    print('--metadata:', args.metadata, flush=True)

    metadata = {
        "version": 1,
        "action": "replace",
        "metadata": args.metadata if args.metadata else {}
    }

    if not os.path.exists(args.in_file):
        print('--in-file argument', args.in_file, 'does not exist', flush=True)
        metadata['metadata']['ei_check_resampled'] = 0
        save_metadata(metadata, args.out_directory)
    else:
        print('--in-file path', args.in_file, 'exists', flush=True)
        print("filename:", os.path.basename(args.in_file))

        df = pd.read_csv(args.in_file)
        consecutive_deltas = df['time'].diff() * 1e-9  # Convert nanoseconds to seconds
        avg_sampling_rate = np.mean(consecutive_deltas)
        avg_frequency = 1 / np.mean(consecutive_deltas)
        total_num_of_samples = len(df.index)

        print("Average Sampling Rate:", avg_sampling_rate, flush=True)
        print("Average Frequency:", avg_frequency, flush=True)
        print("Total Number of Samples:", total_num_of_samples, flush=True)

        df['time'] = pd.to_datetime(df['time'], unit='ns')
        df.set_index('time', inplace=True)

        print("Resampling ...", flush=True)

        sampling_rate = str(args.sampling_rate) + 'ms'

        if args.resampling_mode == 'mean':
            df_resampled = df.resample(sampling_rate).mean()
        elif args.resampling_mode == 'median':
            df_resampled = df.resample(sampling_rate).median()
        else:
            print('Argument --resampling_mode not correct, select mean or median')
            metadata['metadata']['ei_check_resampled'] = 0
            save_metadata(metadata, args.out_directory)

        frequency = (1 / args.sampling_rate) * 1000
        if frequency > avg_frequency:
            print(f"Desired frequency ({frequency} Hz) is higher than average file frequency ({avg_frequency} Hz)...", flush=True)
            print("Upsampling using polynomial interpolation ...", flush=True)
            df_resampled = df_resampled.interpolate(method='polynomial', order=1)

        df_resampled = df_resampled.interpolate(method='linear', order=1, limit_direction='both')

        output_filename = f"{os.path.splitext(os.path.basename(args.in_file))[0]}.resampled.csv"
        df_resampled.to_csv(os.path.join(args.out_directory, output_filename))
        print("... Done", flush=True)

        print("Finished", flush=True)

        metadata['metadata']['ei_check_resampled'] = 1
        save_metadata(metadata, args.out_directory)

if __name__ == "__main__":
    main()