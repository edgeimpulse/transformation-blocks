import os, sys, argparse, shutil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the arguments
parser = argparse.ArgumentParser(description='Organization transformation block')
parser.add_argument('--in-file', type=str, required=True, help="Argument passed by Edge Impulse transformation block when the --in-file option is selected")
parser.add_argument('--out-directory', type=str, required=False, help="Argument passed by Edge Impulse transformation block when the --out-directory option is selected")
parser.add_argument('--time-column', type=str, required=True, help="Name of the time column in the CSV")

args, unknown = parser.parse_known_args()
print('--in_file: ', args.in_file, flush=True)
print('--out_directory: ', args.out_directory, flush=True)
print('--time-column: ', args.time_column, flush=True)

# Verify that the input file exists
if args.in_file:
    if not os.path.exists(args.in_file):
        print('--in-file argument', args.in_file, 'does not exist', flush=True)
    else:
        print('--in-file path', args.in_file, 'exists', flush=True)
        print("filename: ", os.path.basename(args.in_file))

        # Read CSV
        df = pd.read_csv(args.in_file)
        df.index = pd.to_datetime(df[args.time_column], unit='ns')

        # Get a list of all columns except 'time' and 'seconds_elapsed'
        columns_to_plot = [col for col in df.columns if col not in [args.time_column, 'seconds_elapsed']]

        # Create subplots for each selected column
        fig, axes = plt.subplots(nrows=len(columns_to_plot), ncols=1, figsize=(12, 6 * len(columns_to_plot)))

        for i, col in enumerate(columns_to_plot):
            axes[i].plot(df.index, df[col])
            axes[i].set_title(f'{col} over time')
            axes[i].set_xlabel('time')
            axes[i].set_ylabel(col)
            axes[i].grid(True)

        # Save the figure with all subplots
        plt.tight_layout()
        print("Graph created", flush=True)
        plt.savefig(os.path.join(args.out_directory, f"{os.path.splitext(os.path.basename(args.in_file))[0]}.graph.png"))

        # Display the plots (optional)
        # plt.show()

        print("Time series graphs saved.", flush=True)
        print("Finished", flush=True)
        exit(0)
else:
    print('Missing argument --in-file does not exist')
    sys.exit(1)