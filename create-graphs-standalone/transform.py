import os, sys, argparse
import pandas as pd
import matplotlib.pyplot as plt

# Set the arguments
parser = argparse.ArgumentParser(description='Organization transformation block')
parser.add_argument('--sensor_name', type=str, required=True, help="Sensor data to extract to create the graph")
parser.add_argument('--bucket_name', type=str, required=False, help="Bucket where your dataset is hosted")
parser.add_argument('--bucket_directory', type=str, required=False, help="Directory in your bucket where your dataset is hosted")

args, unknown = parser.parse_known_args()

sensor_name = args.sensor_name

sensor_file = sensor_name + '.csv'
bucket_name = args.bucket_name
bucket_prefix = args.bucket_directory
mount_prefix = os.getenv('MOUNT_PREFIX', '/mnt/s3fs/')

folder = os.path.join(mount_prefix, bucket_name, bucket_prefix) if bucket_prefix else os.path.join(mount_prefix, bucket_name)

# Check if folder exists
if os.path.exists(folder):
    print('path exist', folder, flush=True)
    for dirpath, dirnames, filenames in os.walk(folder):
        print("dirpath:", dirpath, flush=True)
        if os.path.exists(os.path.join(dirpath, sensor_file)):
            print("File exist: ", os.path.join(dirpath, sensor_file), flush=True)
            
            df = pd.read_csv(os.path.join(dirpath, sensor_file))
            df.index = pd.to_datetime(df['time'], unit='ns')

            # Get a list of all columns except 'time' and 'seconds_elapsed'
            columns_to_plot = [col for col in df.columns if col not in ['time', 'seconds_elapsed']]

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
            plt.savefig(os.path.join(dirpath, sensor_name))

            # Display the plots (optional)
            # plt.show()

            
        else:
            print("file is missing in directory ", dirpath, flush=True)
     
else:
    print('Path does not exist')
    sys.exit(1)


print("Finished", flush=True)
exit(0)


